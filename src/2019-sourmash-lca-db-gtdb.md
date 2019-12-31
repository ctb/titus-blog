Title: Sourmash LCA databases now available for the GTDB taxonomy
Date: 2019-12-30
Category: science
Tags: sourmash, taxonomy, metagenomics, minhash, gtdb
Slug: 2019-sourmash-lca-db-gtdb
Authors: C. Titus Brown
Summary: GTDB databases!

I am happy to announce that we have made available prepared sourmash
taxonomy ("LCA") databases for release 89 of the
[GTDB taxonomy](https://www.biorxiv.org/content/10.1101/256800v2).

The databases are available for download from the Open Science
Framework in [this project](https://osf.io/wxf9z/). There are prepared
databases avaialble for k=21, k=31, and k=51.

## What is the GTDB taxonomy?

GTDB is a revised bacterial and archaeal taxonomy based on
phylogenetic relations between proteins from approximately 25k
genomes. You can read more about it
[here](https://www.biorxiv.org/content/10.1101/256800v2).

GTDB is an alternative to the NCBI taxonomy. It is used by (among
others) [MGnify](https://www.ebi.ac.uk/metagenomics/), the EBI
metagenomics resource.

## What is sourmash?

Sourmash is a research platform and bioinformatics tool for searching
and analyzing genomes, based on a
[MinHash](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0997-x)-inspired
approach that allows genome similarity searches, genome containment
searches, and compositional analysis of k-mers in large sequence data
sets. You can read more about it
[here](https://f1000research.com/articles/8-1006).

## What do these databases let you do?

There are three immediate uses for these databases:

* you can use the
  [`sourmash lca classify`](https://sourmash.readthedocs.io/en/latest/command-line.html#sourmash-lca-classify)
  routine (and other LCA commands) to do taxonomic classification of
  genomes using the GTDB taxonomy. (See [our tutorial on sourmash lca!](https://sourmash.readthedocs.io/en/latest/tutorials-lca.html))

* you can do compositional analysis of metagenomes using
  [`sourmash lca summarize`](https://sourmash.readthedocs.io/en/latest/command-line.html#sourmash-lca-summarize).

* you can search for genomes in GTDB that are similar to genomes (or
  metagenomes) of interest, using
  [`sourmash search`](https://sourmash.readthedocs.io/en/latest/command-line.html#sourmash-search)
  and
  [`sourmash gather`](https://sourmash.readthedocs.io/en/latest/command-line.html#sourmash-gather).

## How much memory does sourmash need to use these databases?

LCA databases take up less disk space than SBT databases, but are more
memory intensive.  Using these databases requires about 5 GB of RAM.

--titus

## Appendix: How are these databases built?

We use a fully automated snakemake workflow to build them,
[here](https://github.com/dib-lab/sourmash_databases/tree/master/gtdb). It
takes about 12 hours and under 100 GB of RAM to build the databases from the
genomes under `release89/fastani/database/`.
