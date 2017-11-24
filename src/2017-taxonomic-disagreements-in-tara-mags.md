Title:  Why are taxonomic assignments so different for Tara bins? (Black Friday Morning Bioinformatics)
Date: 2017-11-24
Category: science
Tags: bioinformatics, tara, minhash, ngs, metagenomics, smb, taxonomy
Slug: 2017-taxonomic-disagreements-in-tara-mags
Authors: C. Titus Brown
Summary: A more refined taxonomic analysis 

Happy (day after) Thanksgiving!

Now that we can [parse custom taxonomies](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-try-again.html) in sourmash and [use them for genome classification (tutorial)](https://github.com/dib-lab/sourmash/blob/add/lca/doc/tutorials-lca.md) I thought I'd revisit the Tara ocean genome bins produced by Delmont et al. and Tully et al. (see [this blog post](http://ivory.idyll.org/blog/2017-taxonomy-of-tara-ocean-genomes.html) for details).

Back when I first [looked at the Tully and Delmont bins](http://ivory.idyll.org/blog/2017-taxonomy-of-tara-ocean-genomes.html), my tools for parsing taxonomy were quite poor, and I was limited to using the Genbank taxonomy.  This meant that I couldn't deal properly with places where the imputed taxonomies assigned by the authors extended beyond Genbank.

Due to requests from Trina McMahon and Sarah Stevens, this is no longer a constraint! We can now load in completely custom taxonomies and mix and match them as we wish.

How does this change things?

## A new `sourmash lca` command, `compare_csv`

For the purposes of today's blog post, I added a new command to `sourmash lca`. `compare_csv` takes in two taxonomy spreadsheets and compares the classifications, generating a list of compatible and incompatible classifications.

## Some quality control and evaluation

(Let's start by asking if our scripts work in the first
place!)

When I was working on the `sourmash lca` stuff I noticed something curious: when I read in the delmont classification spreadsheet and re-classified the delmont genomes, I found more classifications for the genomes than were in the input spreadsheet.

So, for example, when I do:

```
sourmash lca classify --db delmont-MAGs-k31.lca.json.gz \
    --query delmont-genome-sigs --traverse-directory \
    -o delmont-genome-sigs.classify.csv
```

and then compare the output CSV with the original table from the Delmont et al. paper,
```
sourmash lca compare_csv delmont-genome-sigs.classify.csv \
    tara-delmont-SuppTable3.csv
```

I get the following:

```
957 total assignments, 24 differ between spreadsheets.
24 are compatible (one lineage is ancestor of another.
0 are incompatible (there is a disagreement in the trees).
```

What!? Why would we be able to classify new things?

Looking into it, it turns out that these differences are because one input genome's classification informs others, but the way that Delmont et al. did their classifications did not take into account their own genome bins.

For example, `TARA_ASW_MAG_00041` is classified as genus `Emiliania` by sourmash, but is simply `Eukaryota` in Delmont et al.'s paper.  The new classification for `00041` comes from the other genome bin `TARA_ASW_MAG_00032` which was firmly classified as `Emiliana` and shares approximately 1.6% of its k-mers with the `00041`.

**If this holds up, it provides some nice context for Trina's original request for a quick way to classify new genomes against previously classified bins.** Quickly feeding custom classifications into new classifications seems quite useful!

We see the same thing when I reclassify the Tully et al. genome sigs against themselves. If I do:

```
sourmash lca classify \
    --db tully-MAGs-k31.lca.json.gz \
    --query tully-genome-sigs --traverse-directory \
    -o tully-genome-sigs.classify.csv
sourmash lca compare_csv tully-genome-sigs.classify.csv \
    tara-tully-Table4.csv
```
then I get:
```
2009 total assignments, 7 differ between spreadsheets.
7 are compatible (one lineage is ancestor of another.
0 are incompatible (there is a disagreement in the trees).
```

- so no incompatibilities, but a few "extensions".

## What about incompatibilities?

The above was really just internal validation - can we classify genomes against themselves and get consistent answers? It was unexpectedly interesting but not terribly so.

But what if we take the collections of genome bins from tully and reclassify them based on the delmont classifications? And vice versa?

### Reclassifying tully with delmont

Let's give it a try!

First, classify the tully genome signatures with an LCA database built from the delmont data:
```
sourmash lca classify \
    --db delmont-MAGs-k31.lca.json.gz \
    --query tully-genome-sigs --traverse-directory \
    -o tully-query.delmont-db.sigs.classify.csv
```

Then, compare:

```
sourmash lca compare_csv \
    tully-genome-sigs.classify.csv \
    tully-query.delmont-db.sigs.classify.csv \
    --start-column=3
```

and we get:

```
987 total assignments, 889 differ between spreadsheets.
296 are compatible (one lineage is ancestor of another.
593 are incompatible (there is a disagreement in the trees).
164 incompatible at rank superkingdom
255 incompatible at rank phylum
107 incompatible at rank class
54 incompatible at rank order
13 incompatible at rank family
0 incompatible at rank genus
0 incompatible at rank species
```

Ouch: almost two thirds are incompatible, 164 of them at the *superkingdom* level!

For example, in the tully data set, `TOBG_MED-875` is classified as a Euryarchaeota, novelFamily_I, but using the delmont data set, it gets classified as Actinobacteria! Digging a bit deeper, this is based on approximately 290kb of sequence, much of it from `TARA_MED_MAG_00029`, which is classified as Actinobacteria and shares about 8.6% of its k-mers with `TOBG_MED-875`. So that's the source of that disagreement.

(Some provisional digging suggests that there's a lot of Actinobacterial proteins in `TOBG_MED-875`, but this would need to be verified by someone more skilled in protein-based taxonomic analysis than me.)

### Reclassifying delmont with tully

What happens in the other direction?

First, classify the delmont signatures with the tully database:

```
sourmash lca classify \
    --db tully-MAGs-k31.lca.json.gz \
    --query delmont-genome-sigs --traverse-directory \
    -o delmont-query.tully-db.sigs.classify.csv

```

Then, compare:

```
sourmash lca compare_csv delmont-genome-sigs.classify.csv \
    delmont-query.tully-db.sigs.classify.csv \
    --start-column=3
```

And see:

```
604 total assignments, 537 differ between spreadsheets.
193 are compatible (one lineage is ancestor of another.
344 are incompatible (there is a disagreement in the trees).
95 incompatible at rank superkingdom
151 incompatible at rank phylum
66 incompatible at rank class
25 incompatible at rank order
7 incompatible at rank family
0 incompatible at rank genus
0 incompatible at rank species
```
As you'd expect, this more or less agrees with the results above - lots of incompatibilities, with fully 1/6th incompatible at the rank of superkingdom (!!).

## Why are thing classified so differently!?

First, a big caveat: my code may be completely wrong. If so, well, best to find out now!  I've done only the lightest of spot checks and I welcome further investigation.  (TBH, I'm actually kind of hoping that Meren, the senior author on the Delmont et al. study, dives into the Tully data sets and does a more robust reclassification using his methods - [he has an inspiring history of doing things like that. ;)](http://merenlab.org/2017/10/16/reply-to-probst-et-al/) 

But, assuming my code isn't *completely* wrong...

On first blush, there are three other possibilities. For each classification, the tully classification could be wrong, the delmont classification could be wrong, or both classifications could be wrong.  Either way, they're inconsistent!

On second blush, this all strikes me as a bit of a disaster. Were the taxonomic classification methods used by the Delmont and Tully papers really so different!? How do we trust our own classifications, much less anyone else's?

I will fall back on my usual refrain: we need tools that let us detect and resolve such disagreements quickly and reliably.  Maybe sourmash can provide the former, but I'm pretty sure k-mers [are too specific](http://ivory.idyll.org/blog/2017-how-specific-kmers.html) to do a good job of resolving disagreements above the genus level.

Anyhoo, I'm out of time for today, so I'll just end with some thoughts for What Next.

## What next?

Other than untangling disagreements, what other things could we do? Well, we've just added 60,000 genomes from the JGI IMG database to our previous collection of 100,000 genomes from Genbank, so we can do a classification against all available genomes!  And, if we're feeling ambitious, we could reclassify *all* the genomes against *themselves*. That might be interesting...

## Appendix: Building the databases

Install `sourmash lca` as in [the tutorial](https://github.com/dib-lab/sourmash/blob/add/lca/doc/tutorials-lca.md).

Grab and unpack the genome signatures for the tully and delmont studies:

```
curl -L https://osf.io/vngdz/download -o delmont-genome-sigs.tar.gz
tar xzf delmont-genome-sigs.tar.gz
curl -L https://osf.io/28r6m/download -o tully-genome-sigs.tar.gz
tar xzf tully-genome-sigs.tar.gz
```

Grab the classifications, too:

```
curl -L -O https://github.com/ctb/2017-sourmash-lca/raw/master/tara-delmont-SuppTable3.csv
curl -L -O https://github.com/ctb/2017-sourmash-lca/raw/master/tara-tully-Table4.csv
```

Then, build the databases:
```
sourmash lca index -k 31 --scaled=10000 \
    tara-tully-Table4.csv tully-MAGs-k31.lca.json.gz \
    tully-genome-sigs --traverse-directory
sourmash lca index -k 31 --scaled=10000 \
    tara-delmont-SuppTable3.csv delmont-MAGs-k31.lca.json.gz \
    delmont-genome-sigs --traverse-directory
```

and now all of the commands above should work.

The whole thing takes about 5 minutes on my laptop, and requires less than 1 GB of RAM and < 100 MB of disk space for the data.
