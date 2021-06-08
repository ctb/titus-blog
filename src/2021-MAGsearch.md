Title: Searching all public metagenomes with sourmash
Date: 2021-06-08
Category: science
Tags: sourmash, MAGsearch, SRA, software, k-mers, minhash
Slug: 2021-MAGsearch
Authors: C. Titus Brown
Summary: Searching all the things!

In preparation for an NIH/DOE workshop I'm attending today on
"Emerging Solutions in Petabyte Scale Sequence Search", I thought I'd
write down what we're currently doing with sourmash for public
metagenome search. I'm writing this blog post in a hurry, and I may
revise it later as I receive comments and feedback; I'll point to a
diff if I do.

This is based largely on work that was [done by Dr. Luiz Irber last year](https://blog.luizirber.org/2020/07/24/mag-results/), as part of this PhD work with me.

sourmash itself is available (see
[sourmash.readthedocs.io/](https://sourmash.readthedocs.io)), and we
just released v4.1.2 yesterday! It's under the BSD 3-clause license
and is fully available via conda and pip.

## In brief - lightweight metagenome search with MAGsearch

Today, we can use MAGsearch to robustly find matches to 10kb+ sequences (or collections of 10,000 or more k-mers) across all publicly available metagenomes, out to about 93% ANI.

It's particularly useful for -

* gathering candidates from public metagenomes for e.g. outbreak detection.
* finding matches to a particular species or genus so as to study its ecological distribution.
* gathering data sets to expand our knowledge of a species pangenome

A search with ~100 query genomes takes about 17 hours, today, and will search 580,000 metagenomes representing 530 TB of original sequence data.

## How it works underneath

We use [sourmash](https://sourmash.readthedocs.io/en/latest/) to support metagenome containment search with scaled signatures.

sourmash scaled signatures are derived from MinHash techniques. They are compressed representations of k-mer collections, and can reliably be used to find exact matches of ~10kb segments of DNA between any two collections; larger matches can be found out to about 93% ANI.

One key aspect here is that search can be done without access to the original data.

We maintain a collection of signatures for ~580,000 public metagenomes with the SRA for k=21, 31, and 51. A search with about 100 genome-sized queries currently takes about 17 hours using 32 threads with 48 GB of RAM (on our HPC).

Our complete collection of signatures is approximately 10 TB total, although this contains far more than the metagenome data - it contains 3.7m signatures, representing 1.3 PB of total data (SRA metagenomes + SRA non-plant/animals + Genbank/Refseq microbial genomes).

This collection of signatures is automatically updated by [wort](https://github.com/dib-lab/wort), which coordinates a distributed collection of workers to compute signatures as new data arrives at NCBI.

## Simple opportunities for improvement

MAGsearch is a robust prototype, with many straightforward opportunities for improvement. I would guess that with a few weeks of focused investment, we could get down to about ~1 hour per search.

First, the MAGsearch code doesn't do anything special in terms of loading; it's using the default sourmash signature format, which is JSON. For example, binary encodings would decrease the collection size a lot, while also speeding up search (by decreasing the load time).

Second, searching the signatures is done linearly, and uses Rust to do so in parallel. It uses the same Rust code that underlies sourmash (but is several versions behind the latest version). Making use of recent improvements in sourmash Rust code would probably speed this up several fold.

Third, we can now add protein signatures to our collection of DNA signatures, which would enable much more sensitive search. (We'd have to sketch a lot of data, though. :)

## Broader limitations

The internal data structures we use in sourmash are optimized for relatively small collections of k-mers, because sourmash is built around downsampling k-mer collections. We're slowly improving our internal structures, but supporting *all* k-mers is not straightforward and is not something on our current roadmap.

Our sketching techniques only support individual k-mer sizes/molecule types. So while we can compute, store and search multiple k-mer sizes for DNA, protein, Dayhoff encodings, etc., they are stored separately and don't "compress" together. This means that signature collections grow quickly in size as we provide more k-mer sizes and molecule types!

We're not quite sure how to provide our current databases to people. Personally I'm not really ready to support MAGsearch as a service, either, but that's partly because of a lack of funding.

## What else does sourmash offer?

sourmash itself is stable and well tested, and can be used with confidence to do many bioinformatics tasks. It is easy to install (pip/conda), and is reasonably well documented.

Our data structures and algorithms are simple and well-understood and straightforward to (re)implement. While they aren't yet all published, we are happy to explain them and tell you where they will and won't work.

sourmash is fast, and low memory, and requires little disk space for even pretty large collections of signatures.

sourmash has an increasingly useful command-line interface that supports many common k-mer and search operations. In this sense, it can be used as a partial guide for a good "default" set of operations that k-mer-based tools could support. We have paid a fair amount of attention to user experience, too.

Underneath, sourmash has a flexible Python API that is slowly being replaced with Rust underneath. This means that we can quickly prototype new functionality while refactoring critical functionality underneath, so sourmash performance is continually improving while we are also tackling new use cases.

We have an open, robust approach to software development, with an increasingly diverse array of contributors. I'm not sure we're ready to take on a lot of new contributors quite yet, because our roadmapping processes are not very mature, but we're working on that.

We use semantic versioning for the sourmash package itself, and we communicate clearly about breaking changes. As a result, sourmash can be cleanly integrated into workflows with simple versioning pinning requirements.

We support public and private collections of signatures, and all of our primary search and analysis approaches work with multiple databases or signature collections without needing to re-index them or combine them from scratch. 

We also support flexible "free-form" taxonomy, and in particular support both NCBI and GTDB taxonomies.

## Where would I like to see petabase-scale search go?

I wouldn't advocate for sourmash itself (either the software or the underlying techniques) as the one true method for searching all (meta)genomic data. Among other things, sourmash has a lot of other use cases that matter to us!

But I think we have a few experiences to offer to any such effort -

* we have functioning implementations that support a number of really useful use cases for metagenome search and analysis. It would be nice not to lose those use cases!
* high-sensitivity prefiltering approaches are good and  enable flexible triage afterwards. We mostly use sourmash as a lightweight way to find all the things that we *might* care about, before doing more in-depth analysis.
* having both command-line and Python APIs has been incredibly useful, and I think it would be a mistake to bypass good APIs in favor of a Web API. Of course, this also increases the developer effort by a lot, but the return is that you enable a lot more flexibility.
* riffing more on that, I think it would be a mistake to write a custom Web-hosted indexing and search tool that only works with NCBI formats and taxonomies.
* riffing even more on that, it's been great to be able to quickly add databases/collections to search, and supporting both completely private databases as well as rapid updating of public database collections is something that has been really useful in comparison to many other metagenome analysis tools.
* simplicity of data structures and algorithms has helped us a lot with sourmash. Software support is fundamentally a game of maintenance and it has been great to be able to reimplement our core data structures and algorithms in multiple languages. In particular, I worry a lot about premature optimization when I look at other packages.

Luiz has also done a lot of thinking about distributed computing and decentralization via Dat and IPFS that I think could be valuable, but I'm not expert enough to summarize it myself. Hopefully Luiz will write something up :). (You can already [check out his PhD thesis, chapters 4 and 5, for some juicy details and discussion, though!](https://github.com/luizirber/phd/tree/master/thesis))

## What other tools should we be looking at for large scale search?

I think [Serratus](https://www.biorxiv.org/content/10.1101/2020.08.07.241729v2) did an excellent job of showing some of the possibilities of massive-scale metagenome search!

There's lots of tools out there in various stages of development, but I am particularly interested in [metagraph](https://www.biorxiv.org/content/10.1101/2020.10.01.322164v1).

I'd love to hear about more tools and approaches - please drop them in the comments or on twitter!

--titus
