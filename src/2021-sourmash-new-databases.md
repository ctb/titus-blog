Title: New sourmash databases are available!
Date: 2021-06-29
Category: science
Tags: sourmash, software, release, databases, gtdb
Slug: 2021-sourmash-new-databases
Authors: C. Titus Brown
Summary: Databases are now available for GTDB!

(Many thanks go to Dr. Tessa Pierce for refitting our database construction
process, to Dr. Luiz Irber for underlying infrastructure work, and to Dr.
Taylor Reiter for updating the docs :)

While we are working on releasing sourmash 4.2, I wanted to drop a
short note - we have some new databases (and database types!)
available for [sourmash](https://sourmash.readthedocs.io/en/latest/),
our genome and metagenome analysis tool.

If you go to the
[prepared databases](https://sourmash.readthedocs.io/en/latest/databases.html)
page for sourmash, you'll see that we now make three types of
databases available, for two different collections of GenBank genomes.

## Collections

We've created two collections of sourmash signatures for
GTDB 06-RS202, the latest release of the [Genome Taxonomy Database](https://gtdb.ecogenomic.org/). (Since every genome in GTDB is in GenBank, these are really just subsets of GenBank.)

The smaller collection contains the 48,000 genomic representatives, a collection of genomes that is non-redundant at the species level.

The larger collection contains all 258k GenBank genomes for which GTDB has calculated taxonomies.

Why do we have this focus on GTDB? It's a nice collection of high quality genomes; it covers most of the bacterial and archaeal species diversity present in GenBank; it's not massively redundant; and it's less monstrously huge than all of GenBank microbial (also see below.) And, since sourmash is (mostly) taxonomy agnostic, it doesn't matter whether you are fan of GTDB or a fan of NCBI taxonomies.

For all these reasons, GTDB has become our default for searches. But again, see below.

## Database types

We provide three database types: SBT, LCA, and Zipfile collections.

The SBT and LCA databases are the same database types that we've provided for several years, and you probably want one of these. They are compatible with sourmash 3.5 and sourmash 4.x both.

To quote from [the documentation](https://sourmash.readthedocs.io/en/docs_4.0/command-line.html#storing-and-searching-signatures),
>SBT databases are low memory and disk-intensive databases that allow for fast searches using a tree structure, while LCA databases are higher memory and (after a potentially significant load time) are quite fast.

But!

With [sourmash 4.1](https://github.com/sourmash-bio/sourmash/releases/tag/v4.1.0), we *also* support a new type of sourmash database - zipfile collections. These are unindexed collections of signatures, and now serve as the basis for our database release process. They are not (yet) that useful for users, is all.

## Do we provide anything else?

Why, yes, thanks for asking! Actually, yes - if you look at our full [google drive folder](https://drive.google.com/drive/folders/1ohyggli2FsOoA2PO9h74FMp8A4mznzjt), you'll see that we also provide full manifests for the content of these databases, along with a report from `sourmash lca index`.

## What other collections are we planning to provide?

We've spent much of the last year trying to figure out how to make all GenBank microbial genomes (=~ all non-animal/non-plant) searchable in a useful way - see e.g. [sourmash 4.1](https://github.com/sourmash-bio/sourmash/releases/tag/v4.1.0), which massively sped up search and gather. We'll probably provide that as a zip collection soon (not sure about an SBT, though! and almost certainly not as an LCA database).

## What about protein databases? And support for multiple taxonomies?

At the present time, I can neither confirm nor deny that we will soon be providing prepared database for protein search. Likewise, I can neither confirm nor deny that we will soon release support for doing taxonomic analysis with either NCBI or GTDB taxonomies, or indeed _both at the same time_. So please do not engage in unwarranted speculation.

## Questions? Comments? Thoughts? Requests?

File an [issue](https://github.com/sourmash-bio/sourmash/issues) or come chat with us over on our [new gitter channel, sourmash-bio/community](https://gitter.im/sourmash-bio/community#)!

And stay tuned!

--titus
