Title: Detecting microbial contamination in long-read assemblies (from known microbes)
Date: 2018-06-03
Category: science
Tags: sourmash, pacbio
Slug: 2018-detecting-contamination-in-long-read-assemblies
Authors: C. Titus Brown
Summary: Using sourmash to find candidate contaminants

A week ago, Erich Schwarz e-mailed our lab list asking,

>I would like to be able to download a set of between 1,000 and 
>10,000 bacterial genome assembly sequences that are reasonably 
>representative of known bacteria.  RefSeq's bacterial genome set is 
>easy to download, but absolutely freaking huge (the aggregate FASTA 
>file for its genome sequences is 410 GB).

After digging in a bit, Erich gave us his actual goal: to search for
potential microbial contaminants, like so:

> Do MegaBlastN on new genome assemblies from PacBio data.  With 
> PacBio one gets very few large contigs, so bacterial contamination 
> is really easy to filter out with a simple MegaBlastN.  However, I 
> did my last big download of 3,000 microbial genomes from EBI in 
> 2013.  There's a lot more of them now!

My response:

> I think sourmash gather on each contig would probably do the right
> thing for you, actually; https://sourmash.readthedocs.io/en/latest/tutorials.html
> if you have a "true positive" contaminated scaffold to share, I can test
> that fairly quickly.

> Also - I assume the contigs are never chimeric, so if you find contamination in
> one it's ok to discard the whole thing?

> Also - kraken should do a fine job of this albeit in a more memory intensive
> way.  MegaBlastN isn't not much more sensitive than k-mer based approaches,
> I think.

This would let Erich search all 100k+ bacterial genomes *without*
downloading the complete genomes.  My recommendation was to do this to
identify candidate genomes for contaminants, and then use something like
mashmap to do a more detailed alignment and contaminant removal.

Erich responded with some useful links.

> In fact, I have what should be both positive and negative 
> controls for microbial contamination:
   
>     http://woldlab.caltech.edu/~schwarz/caeno_pacbio.previous/nigoni_mhap.decont_2015.11.11.fa.gz
>     http://woldlab.caltech.edu/~schwarz/caeno_pacbio.previous/nigoni_mhap.CONTAM_2015.11.11.fa.gz
         
> which you are very welcome to try sourmashing!

After some other back and forth, I wrote a script to do the work; here's
a rough run protocol:

```
curl -O -L http://woldlab.caltech.edu/~schwarz/caeno_pacbio.previous/nigoni_mhap.decont_2015.11.11.fa.gz
./gather-by-contig.py nigoni_mhap.CONTAM_2015.11.11.fa.gz genbank-k31.sbt.json --output-match foo.txt --output-nomatch foo2.txt —csv summary.csv
```

which should take a minute or two to run on a modern SSD laptop, and requires
less than 1 GB of RAM (and about 18 GB of disk space for the genbank index).

A few comments before I go through the script in detail:

* this uses MinHash downsampling as implemented in sourmash, so you have to feed long contigs in. This is appropriate for PacBio and Nanopore assemblies, but not for raw reads of any kind, and probably not for Illumina assemblies.
* sourmash will happily do contaminant estimation of an entire data set (genomes, reads, etc.) - the goal here was to go line by line through the contigs and split them into "match" and "no match".
* the databases are downloadable [here](https://sourmash.readthedocs.io/en/latest/databases.html)

Last, but not least: this kind of ad hoc scripting functionality is
what we aspire to enable with all our software.  A command line
program can't address all needs, but a default set of functionality provided
via the command line, wrapping a more general purpose library, can!

You can download the script [here](https://gist.github.com/ctb/fa1c11b5e2f9614128685600911c842a); an annotated version is below.

## An annotate version of the script

First, import the necessary things:

```python
#! /usr/bin/env python
import argparse
import screed
import sourmash
from sourmash import sourmash_args, search
from sourmash.sbtmh import SearchMinHashesFindBestIgnoreMaxHash
import csv
```

In the main function, set up some arguments:

```python
def main():
    p = argparse.ArgumentParser()
    p.add_argument('input_seqs')
    p.add_argument('sbt_database')
    p.add_argument('--threshold', type=float, default=0.05)
    p.add_argument('--output-nomatch', type=argparse.FileType('wt'))
    p.add_argument('--output-match', type=argparse.FileType('wt'))
    p.add_argument('--csv', type=argparse.FileType('wt'))
    args = p.parse_args()
```

Then, find the SBT database to load:

```python
    tree = sourmash.load_sbt_index(args.sbt_database)
    print(f'found SBT database {args.sbt_database}')
```

Next, figure out the MinHash parameters used to construct this database, so we
can use them to construct MinHashes for each sequence in the input file:

```python
    leaf = next(iter(tree.leaves()))
    mh = leaf.data.minhash.copy_and_clear()

    print(f'using ksize={mh.ksize}, scaled={mh.scaled}')
```

Give some basic info:

```python
    print(f'loading sequences from {args.input_seqs}')
    if args.output_match:
        print(f'saving match sequences to {args.output_match.name}')
    if args.output_nomatch:
        print(f'saving nomatch sequences to {args.output_nomatch.name}')
    if args.csv:
        print(f'outputting CSV summary to {args.csv.name}')
```

In the main loop, we'll need to track found items (for CSV summary output),
and other basic stats:

```python
    found_list = []
    total = 0
    matches = 0
```

Now, for each sequence in the input file of contigs:

```python
    for record in screed.open(args.input_seqs):
        total += 1
        found = False
```

Set up a search function that finds the best match, and construct a new MinHash
for each query sequence:

```python
        search_fn = SearchMinHashesFindBestIgnoreMaxHash().search

        query_mh = mh.copy_and_clear()
        query_mh.add_sequence(record.sequence)
        query = sourmash.SourmashSignature(query_mh)
```

If the sequence is too small, quit.

```python
        # too small a sequence/not enough hashes? notify
        if not query_mh.get_mins():
            print(f'note: skipping {query.name[:20]}, no hashes in sketch')
            continue
```         

Now do the search, and pull off the first match:

```python
        for leaf in tree.find(search_fn, query, args.threshold):
            found = True
            matches += 1
            similarity = query.similarity(leaf.data)
            found_list.append((record.name, leaf.data.name(), similarity))
            break
```

Nothing found? That's ok, just indicate empty.

```python
        if not found:
            found_list.append((record.name, '', 0.0))
```

Output sequences appropriately:
```python
        if found and args.output_match:
            args.output_match.write(f'>{record.name}\n{record.sequence}')
        if not found and args.output_nomatch:
            args.output_match.write(f'>{record.name}\n{record.sequence}')
```

and update the user:

```python
        print(f'searched {total}, found {matches}', end='\r')
```

At the end, print out the summary (this merely leaves the preceding line
alone), and output CSVs:

```python
    print('')

    if args.csv:
        w = csv.DictWriter(args.csv, fieldnames=['query', 'match', 'score'])
        w.writeheader()
        for (query, match, score) in found_list:
            w.writerow(dict(query=query, match=match, score=score))
```

Finally, ...call the main function if this is run as a script:

```python
if __name__ == '__main__':
    main()
```

Comments and questions welcome, as always!

best,
--titus
