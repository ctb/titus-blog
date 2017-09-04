Title: Taxonomic examinations of genome bins from Tara Oceans (Honorary Sunday Morning Bioinformatics)
Date: 2017-09-04
Category: science
Tags: bioinformatics, tara, minhash, ngs, metagenomics, smb, taxonomy
Slug: 2017-taxonomy-of-tara-ocean-genomes
Authors: C. Titus Brown
Summary: An initial taxonomical investigation of the genome bins.

This is a follow-on to [Comparing genome sets extracted from metagenomes](http://ivory.idyll.org/blog/2017-comparing-genomes-from-metagenomes.html).

After my first foray into comparing the genome bins extracted from the Tara Oceans data by Tully et al. (2017) and Delmont et al. (2017), I got curious about the taxonomic assignments of the bins and decided to investigate those on this fine Labor Day morning.

In this, I could take advantage of a simple reimplementation of the [Kraken least-common-ancestor taxonomic classification algorithm described here](http://ivory.idyll.org/blog/2017-something-about-kmers.html) that works on MinHash signatures - more on that in another, later blog post.

Briefly, I did the following -

* used the posted lineages to assign NCBI taxonomic IDs to many of the [tully samples](https://github.com/ctb/2017-sourmash-lca/blob/master/tara_tully_taxids.csv) and the [delmont samples](https://github.com/ctb/2017-sourmash-lca/blob/master/tara_meren_taxids.csv) using [really](https://github.com/ctb/2017-sourmash-lca/blob/master/get_taxid_tara_tully.py) [ugly](https://github.com/ctb/2017-sourmash-lca/blob/master/get_taxid_tara_meren.py) scripts.
* found the least-common-ancestor LCA for each hash value across all the MinHash signatures in each data set and stored them in an LCA database;
* wrote a [custom script](https://github.com/ctb/2017-tara-binning/blob/master/examine-taxonomy.py) that loaded in all of the genbank, tully, and delmont LCA assignments together with the NCBI taxonomy and classified each of the tully and delmont genome bins, looking for disagreements.

This last step is the most interesting one for the purposes of this morning's blog post, so let's go into it in a bit more detail.

## Building the taxonomy databases for delmont and tully

I used an approach lifted from [Kraken](http://ivory.idyll.org/blog/2017-something-about-kmers.html) to build taxonomy classifiers for delmont and tully.

Kraken first links all k-mers in each genome to a list of taxonomic IDs, based on the taxonomic assignment for that genome.  Then, Kraken looks for the least-common-ancestor in the taxonomic tree for each k-mer.

I did this for each k-mer in each MinHash signature from the full genbank data set (100,000 genomes), as well as the ~3000 tully and delmont data sets.  (You have to use our super special opensauce if you want to do this on your own MinHash signatures.)

These databases are available for download, below.

## Computing taxonomic assignments for each genome bin

Now I wanted to get an estimate of taxonomic IDs for each genome bin.

So, I wrote [a script](https://github.com/ctb/2017-tara-binning/blob/master/examine-taxonomy.py) that loaded in all three LCA databases (genbank, tully, delmont) and, for each genome bin, extracted all of the taxonomic IDs for every hash value in the MinHash signature.  And, for each taxonomic ID, it computed the LCA across all three databases, obviating the need to do build a single gigantic database of genbank+tully+delmont.

This can all be boiled down to "this script computed the most specific taxonomic ID for a randomly chosen subset of k-mers in each bin."

## Finding disagreements in taxonomy in each bin

Next, I wanted to figure out where (if anywhere) there were disagreements in taxonomy for each bin.

So, in the script above, I took all taxonomic IDs for which there were five or more counts (i.e. five or more hash values with that specific assignment - randomly chosen but IMO conservative), and then found the lowest taxonomic rank at which there was a disagreement across all thresholded taxonomic IDs.

And then I summarized all of this :)

## Some output!

The full output can be seen [for delmont](https://github.com/ctb/2017-tara-binning/blob/master/delmont.taxinfo.txt) and [for tully](https://github.com/ctb/2017-tara-binning/blob/master/tully.taxinfo.txt).

For each genome bin, we either get no output or a line like this:
```
TOBG_MED-638 has multiple LCA at rank 'phylum': Proteobacteria, Bacteroidetes
```

and then we get summary information like so:

```
for tully-genome-sigs found 2631 signatures;
out of 2631 that could be classified, 73 disagree at some rank.
	superkingdom: 1
	phylum: 11
	order: 4
	class: 8
	family: 10
	genus: 10
	species: 29
```

and

```
for delmont-genome-sigs found 957 signatures;
out of 957 that could be classified, 4 disagree at some rank.
	class: 3
	species: 1
```

(Note, for the 50 E. coli signatures [in the sourmash tutorial](https://sourmash.readthedocs.io/en/latest/tutorials.html), we get no disagreements. Good!)

## Checking the results

I took a closer look at a few of the disagreements.

For `TOBG_ARS-21` from tully, which was classified as both Archaea and Bacteria, the hash value taxids seem to be ~evenly split between:

```
cellular organisms;Bacteria;FCB group;Bacteroidetes/Chlorobi group;Bacteroidetes;Flavobacteriia;Flavobacteriales
cellular organisms;Archaea
```

Interestingly, `TOBG_ARS-21` has no assignment in the associated spreadsheet, as far as I can tell.  Instead, the Flavobacterium assignment comes from the *delmont* data set, where a few overlapping genome bins (`TARA_ANW_MAG_00073` and `TARA_ANW_MAG_00082` ) are assigned to Flavobacterium.  And the archaeal assignment comes from the tully data set, but *not* from `TOBG_ARS-21` - rather, there is a ~10% overlap with another tully genome bin, `TOBG_RS-366`, which is assigned to Archaea (with no more refined assignment).

Verdict: genuinely confusing. My script works!

----

For `TOBG_IN-33`, we had a disagreement at phylum: Chlorophyta and Euryarchaeota. Here the hash value taxids are split between Euryarchaeota and genus Ostreococcus.

```
cellular organisms;Archaea;Euryarchaeota
cellular organisms;Eukaryota;Viridiplantae;Chlorophyta;prasinophytes;Mamiellophyceae;Mamiellales;Bathycoccaceae;Ostreococcus
```

Again, `TOBG_IN-33` has no direct taxonomic assignment in tully. The Euryarchaeota assignment comes from a match to `TARA_IOS_MAG_00045` in the delmont data set, as well as a match to delmont genomes `TOBG_EAC-675` and `TOBG_RS-356` (both Euryarchaeota). So where does the assignment to Eukaryota come from? 

If you dig a bit deeper, it turns out that there is ~5.8 - 7.6% similarity between `TOBG_IN-33` (from tully) and two delmont genome bins, `TARA_PSW_MAG_00136` and `TARA_ANE_MAG_00093`, both of which are assigned to `Eukaryota;Chlorophyta;Mamiellophyceae;Mamiellales;Bathycoccaceae;Ostreococcus`.  Maybe `TOBG_IN-33` is a chimeric bin?

Anyway, the verdict: genuinely confusing. My script works (again :)!

## Concluding thoughts

As with most bioinformatics analyses, this gives us some directions to pursue, rather than (m)any hard answers :).

But, with the caveat that this is an analysis that did in just about 3 hours this morning and so the code is probably broken in a myriad of ways:

The vast majority of both the tully and delmont genomes are taxonomically homogeneous under this analysis. In many cases this may be due to limited taxonomic assignment, and it also definitely reflects a lack of information about these genomes!

It seems like the delmont bins have been curated more than the tully bins, with the end effect of removing taxonomically confusing information. Whether this is good or bad will have to await a broader and deeper investigation of the genome bins - right now there are clearly some confounding issues within and between the data sets.

## Appendix: Running everything yourself

(This should take about 10-15 minutes to run on a laptop with ~10 GB of disk space and ~8 GB of RAM. This includes the downloads.)

Along with a sourmash install, you'll need two github repos: https://github.com/ctb/2017-tara-binning and https://github.com/ctb/2017-sourmash-lca.

```
git clone https://github.com/ctb/2017-sourmash-lca
git clone https://github.com/ctb/2017-tara-binning
```

Then set PYTHONPATH and change into the 2017-tara-binning directory:

```
export PYTHONPATH=$(pwd)/2017-sourmash-lca:$PYTHONPATH
cd 2017-tara-binning
```

Download the LCA databases:
```
curl -L https://osf.io/3pc7j/download -o tully-lca-2017.09.04.tar.gz 
curl -L https://osf.io/bw2dj/download -o delmont-lca-2017.09.04.tar.gz

curl -L https://osf.io/zfmbd/download?version=1 -o genbank-lca-2017.08.26.tar.gz
```

Unpack them:

```

tar xzf delmont-lca-2017.09.04.tar.gz
tar xzf tully-lca-2017.09.04.tar.gz
cd db
tar xzf ../genbank-lca-2017.08.26.tar.gz
cd ../
```

Now, grab the signature collections and unpack them, too:

```
curl -L https://osf.io/bh2jr/download -o delmont-genome-sigs.tar.gz
curl -L https://osf.io/28r6m/download -o tully-genome-sigs.tar.gz
tar xzf delmont-genome-sigs.tar.gz 
tar xzf tully-genome-sigs.tar.gz 
```

And we are ready!

Now, run:

```
./examine-taxonomy.py delmont-genome-sigs -k 31 > delmont.taxinfo.txt
./examine-taxonomy.py tully-genome-sigs -k 31 > tully.taxinfo.txt
```

and you should see the same results as in the github links above.
