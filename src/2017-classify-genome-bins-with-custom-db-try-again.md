Title: Classifying genome bins using a custom reference database - maybe this time it'll work?
Date: 2017-10-29
Category: science
Tags: bioinformatics, tara, minhash, ngs, metagenomics, taxonomy,smb
Slug: 2017-classify-genome-bins-with-custom-db-try-again
Authors: C. Titus Brown
Summary: Classifying genome bins with a custom database! Another try!

## The story so far:

Trina [would like to taxonomically classify *new* genomes based on a custom classification of *old* genomes](https://twitter.com/quendi/status/905442912397348864).

Titus [wrote some trial code to do this](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-part-2.html).

Sarah (in Trina's lab) tried the code and realized that [it was limited by the NCBI taxonomy](http://ivory.idyll.org/blog/2017-grokking-the-taxonomies.html), which defeated the whole point of the thing.

Titus retired from the field to consider his options.

## My new attempt

We have [a new script, classify-free-tax.py](https://github.com/ctb/2017-sourmash-lca/blob/12ed23538640cdc64dca58fd88848ad3990aff89/classify-free-tax.py).

This script does the following:

* parses a spreadsheet containing custom taxonomic lineages (i.e. [this format](https://github.com/ctb/2017-sourmash-lca/blob/ab2f14ba5fe9a1bc50a2a4e27bc1c76482ac9a88/tara-delmont-SuppTable3.csv));
* builds a custom taxonomic classification based on the spreadsheet but rooted in NCBI taxonomies;
* creates a k-mer classifier that combines the k-mers from the custom classification with all of Genbank;
* applies that k-mer classifier to a set of query genomes.

It's a long, ugly script, but it seems to work OK on my test subsets.  Let's give it a try!

## Running `classify-free-tax.py`

Let's reclassify 100 randomly chosen genomes from the Delmont et al., 2017 study, as per [this blog post](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-part-2.html), but using our new code.

Here we're interested in validation, so we're going to *use* the 100 randomly chosen genomes to *classify* the 100 randomly chosen genomes and compare the results.



There are two new commands. The first indexes the custom genomes so we can use them in the next classification step:

```
2017-sourmash-revindex/extract-hashvals-by-sample.py delmont delmont/*.sig
```

The next command uses the indexed custom genomes, plus the Genbank LCA database, to classify all of the genomes under `delmont/`:
```
PYTHONPATH=$PYTHONPATH:2017-sourmash-revindex/ \
    ../classify-free-tax.py tara-delmont-SuppTable3.csv delmont \
    delmont/*.sig -o reclassify.csv
```

## Validating the results

To see how well things worked, we can now run a comparison of the input spreadsheet vs the reclassified spreadsheet using [cmp-csv.py](https://github.com/ctb/2017-sourmash-lca/blob/af8b62201e74a2c73bd28000db810ef96c521eb2/cmp-csv.py):

```
../cmp-csv.py tara-delmont-SuppTable3.csv reclassify.csv
```

The output is below. The first lineage line is from the input spreadsheet, and the second lineage line is the re-classification using our software.

tl;dr? Out of 100 genome bins from Delmont et al., we get five disagreements, and it looks like the reclassification is fine.

```
TARA_ANW_MAG_00051
         ['Bacteria', 'Proteobacteria', 'Alphaproteobacteria', 'Rickettsiales', 'Pelagibacteraceae', '', '']
         ['Bacteria', 'Proteobacteria', 'Alphaproteobacteria', 'Pelagibacterales', 'Pelagibacteraceae', '', '']
--
TARA_IOS_MAG_00076
         ['Eukaryota', '', '', '', '', '', '']
         ['Eukaryota', 'Haptophyta', 'Prymnesiophyceae', 'Isochrysidales', 'Noelaerhabdaceae', 'Emiliania', '']
--
TARA_PSE_MAG_00092
         ['Bacteria', 'Proteobacteria', 'Alphaproteobacteria', 'Rickettsiales', 'Pelagibacteraceae', '', '']
         ['Bacteria', 'Proteobacteria', 'Alphaproteobacteria', 'Pelagibacterales', 'Pelagibacteraceae', '', '']
--
TARA_PSW_MAG_00133
         ['Eukaryota', '', '', '', '', '', '']
         ['Eukaryota', 'Haptophyta', 'Prymnesiophyceae', 'Isochrysidales', 'Noelaerhabdaceae', 'Emiliania', '']
--
TARA_RED_MAG_00001
         ['Bacteria', 'Proteobacteria', 'Alphaproteobacteria', 'Sphingomonadales', 'Erythrobacteraceae', 'Citromicrobium', '']
         ['Bacteria', 'Proteobacteria', 'Alphaproteobacteria', 'Sphingomonadales', 'Sphingomonadaceae', 'Citromicrobium', '']
--
```

In three of the five, there is an internal disagreement in the taxonomies, e.g. Pelagibacteraceae has been rerooted under Pelagibacterales in our spreadsheet.  This is probably due to changes in the NCBI taxonomy between when Delmont et al. did their classification and when I downloaded the NCBI taxonomy a few months ago.

In the other two of the five, Delmont et al. could only classify the bins down to Eukaryota, but our k-mer classifier is telling us that they belong to genus Emiliana.  On inspection (hint: pass the `--debug` flag to the classify script), approximately 470,000 of the k-mers in TARA_IOS_MAG_00076 belong to genus Emiliana, and 1.41 million of the k-mers in TARA_PSW_MAG_00133 belong to genus Emiliana, so I'm going to provisionally argue that our re-classification is correct.

## What next?

The code is ugly and needs refactoring, tests, etc.

It'd be fun to repeat the [taxonomic examination of the Tara ocean bins](http://ivory.idyll.org/blog/2017-taxonomy-of-tara-ocean-genomes.html) once I have it working more nicely. I should be able to do a much better (more thorough) job of comparison than before!

More broadly, this is a useful extension of the [least-common-ancestor code that I posted a few weeks back](http://ivory.idyll.org/blog/2017-taxonomy-of-tara-ocean-genomes.html) and I need to revisit all the old code in light of this.  I think I'll be retooling the LCA code substantially to allow the use of custom taxonomies/genome classifications.

I really want to dig into the 8,000 genomes that were posted a little while back (from [this paper]()), and I should make sure my taxonomy code works with the [Genome Taxonomy Database](http://gtdb.ecogenomic.org/).

In the meantime, I'd love to get feedback on the above code if anyone is interested in trying it out!

## Appendix: full set of commands

First, repeat (most of) the steps in [this blog post](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-part-2.html) to install and compute a bunch of things.

```
# create a virtualenv and install sourmash
python3.5 -m venv ~/py3
. ~/py3/bin/activate
pip install -U pip
pip install -U Cython
pip install -U jupyter jupyter_client ipython pandas matplotlib scipy scikit-learn khmer

pip install -U https://github.com/dib-lab/sourmash/archive/master.zip

# grab the 2017-sourmash-lca repository
git clone https://github.com/ctb/2017-sourmash-lca

# download subsample data
cd 2017-sourmash-lca/
curl -L https://osf.io/73yfz/download?version=1 -o subsample.tar.gz
tar xzf subsample.tar.gz
cd subsample

# compute signatures for delmont
cd delmont
sourmash compute -k 21,31,51 --scaled 10000 --name-from-first *.fa.gz

# fix names to match identifiers in spreadsheet (below)
python ../delmont-fix-sig-names.py *.sig

for i in *.sig
do
    mv $i.fixed $i
done
cd ../

# download NCBI LCA database
curl -L https://osf.io/zfmbd/download?version=1 -o genbank-lca-2017.08.26.tar.gz
mkdir -p db
cd db/
tar xzf ../genbank-lca-2017.08.26.tar.gz
cd ../

# grab delmont spreadsheet
curl -O -L https://github.com/ctb/2017-sourmash-lca/raw/master/tara-delmont-SuppTable3.csv

```

If you've already done the above, you'll need to also clone the [2017-sourmash-revindex](https://github.com/ctb/2017-sourmash-revindex) repository:

```
git clone https://github.com/ctb/2017-sourmash-revindex.git

```

and now you're ready to run the commands above.
