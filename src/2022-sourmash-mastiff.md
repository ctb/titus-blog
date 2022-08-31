Title: So! You want to search all the public metagenomes with a genome sequence!
Date: 2022-08-31
Category: science
Tags: sourmash, MAGsearch, SRA, software, k-mers, minhash, mastiff
Slug: 2022-sourmash-mastiff
Authors: C. Titus Brown
Summary: Searching all the things - faster!

Imagine you have a (microbial) genome. Or a contig. And you want to
find similar sequences, either in genomes or in metagenomes.

Looking for it in genomes is possible, if not always easy - you can go
to NCBI and do a BLAST of some sort, but BLAST is intended for more
sensitive and shorter matches. But there are other tools, including
[sourmash](https://sourmash.readthedocs.io/), a tool we've been
developing for a few years, that will happily do it for you.

Looking for something in _metagenomes_ is harder. Metagenomes are
hundreds, thousands, or even millions of times larger than genomes,
and doing _anything_ with them quickly is hard. sourmash supports
doing it one metagenome at a time, but it's slow and memory intensive;
[serratus](https://serratus.io/) will do it for you using the power of
the cloud, but it will cost you (at least) a few thousand $$.

If you're interested in how we're doing DNA sequence search, here's an
excerpt from
[a previous blog post about using SQLite to store our data](http://ivory.idyll.org/blog/2022-storing-ulong-in-sqlite-sourmash.html) -
> The basic idea is that we take long DNA sequences, extract
sub-sequences of a fixed length (say k=31), hash them, and then sketch
them by retaining only those that fall below a certain threshold
value. Then we search for matches between sketches based on number of
overlapping hashes. This is a proxy for the number of overlapping k=31
subsequences, which is in turn convertible into various sequence
similarity metrics.

## MAGsearch exists! It works! But it's hard to share.

For a couple of years now, we've had something called
[MAGsearch](http://ivory.idyll.org/blog/2021-MAGsearch.html) working
on our own private infrastructure.  MAGsearch is sourmash on steroids:
it uses the same underlying Rust library as sourmash and loads and
searches the metagenomes quickly.  And it will do all of this on
commodity hardware that many people have access to - a search of up to
a thousand genomes against the SRA takes under 12 GB of RAM, and under
11 hours, using 32 cores.

MAGsearch does a fairly straightforward thing: it loads all the query
genomes into memory and then iteratively loads each of ~700,000
metagenome sketches, reporting any overlaps. It does so in parallel,
which is why it's so fast - doing this with sourmash would take about
40 times as long, because sourmash isn't parallelized.

One problem with MAGsearch is that it's not real time. 10 hours is
great!!, especially for 1000 genomes, but that's still only about two
genomes a minute. And it's too slow for us to provide MAGsearch as a
service.

Another problem is that the underlying data is about 10 TB at the
moment, and we don't really have a way to share that data.

So we've been using MAGsearch a fair bit over the last two years to do
searches for others, but it's always done in a kind of batch mode
where we run it in between other things we're doing.

## Enter 'mastiff' - using RocksDB to do things faster

For the
[2022 JGI User Meeting](https://usermeeting.jgi.doe.gov/agenda/)
Dr. Luiz Irber was invited to talk about his MAGsearch work, and he
got inspired to try out an alternative solution.

He decided to implement an inverted index using
[RocksDB](http://rocksdb.org/), an embeddable database. I haven't dug
into [the implementation](https://github.com/sourmash-bio/mastiff),
but I believe mastiff uses individual hashes as keys and stores a
vector of dataset IDs as values. So a search for overlaps in the
database is done by using hashes from a query as keys, and then
intersecting the hashes in the values to find which dataset IDs have
sufficient estimated overlap to be reported.

Luiz reported that it took a bit under three weeks to build a RocksDB
index for 500,000 datasets at k=21, scaled=1000. The resulting
database is about 700 GB. He then wrote a Web server to enable queries
against the database.

## mastiff allows real-time search of SRA-scale data sets!

So... it's fast. Like, really fast.

It's so fast, you can just go try it out yourself - I've provided up a
simple notebook
[here](https://github.com/sourmash-bio/2022-search-sra-with-mastiff/blob/main/interpret-sra-live.ipynb)
in
[this github repo](https://github.com/sourmash-bio/2022-search-sra-with-mastiff),
and you can run it directly by clicking on the button below:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/sourmash-bio/2022-search-sra-with-mastiff/stable?labpath=interpret-sra-live.ipynb)

This notebook does the following:

* downloads some SRA metadata (once)
* loads and sketches a Shewanella genome query into a sourmash signature (~45 KB, for a ~5.3 Mbp genome)
* serializes the signatures and sends it to the mastiff server to run it against the SRA
* receives the resulting CSV of dataset + containment estimates
* interprets the CSV in light of the SRA metadata

What you'll see at the bottom of the notebook is that this particular
genome tends to show up in freshwater and wastewater.

The cool thing is that you can run your own queries if you like - just
replace the `shewanella.fa.gz` file references with your own queries
of interest!

(There's also
[a snakemake workflow](https://snakemake.readthedocs.io/) to query
mastiff if you want to run many queries, and a mastiff command-line
program that will sketch and query all in one go.)

## What can mastiff be used for?

MAGsearch is already being used by people for
[outbreak analysis](https://twitter.com/phiweger/status/1402506165452513283)
and biogeography studies, among other things. We have a few different
active research projects in the lab that are exploring its utility for
various questions. So we will soon be able to do those things a lot
faster. Yay!

I personally am looking forward to digging into strain dynamics and
content-based alerts of new metagenomes, among other things.

We can also enable other cool projects, including (perhaps most
importantly) things that we didn't think of.

A rule of thumb that I like is that a technology will be most useful
for researchers when a summer undergrad can casually use it to explore
wild-haired ideas and initiate summer projects based on rapidly
generated exploratory results - and I'm really curious to see what we
can enable others to do with this ;). I can imagine that once people
can casually search the SRA with queries, they'll come up with lots of
ideas and make lots of discoveries. (Of course, lots of follow-up work
would be needed, too - chasing down what detection of a genome in a
metagenome means _biologically_ is tough!)

It has not escaped our notice that this can be used for much smaller
databases, too. So we're looking forward to enabling real-time search
of all the NCBI microbial genomes, as well as ..well, whatever we can
get our hands on :).

mastiff will eventually (see below, "Whither mastiff?") be integrated
into sourmash and/or robustified, and then it will support private
databases, too.

## Well, but wait, you said "real-time"

Right, I did - it takes between 2 and 10 seconds to do a search, and
IIRC the server can handle up to 200 simultaneous queries at a time.

And I've gotta be honest... at first I missed the point that this was
real-time. And web-enabled.

I was describing it to some collaborators, and while I was describing
it I realized, oh, cool, we can actually do this all in JavaScript via
WebAssembly too, of course.

So, also coming eventually (if not, like, tomorrow), I expect we will
provide a Web site where you can sketch a genome client-side (e.g. in
the browser - see
[sourmash#1973](https://github.com/sourmash-bio/sourmash/issues/1973)),
and then receive near-instantaneous reporting on similarities to any
known genome as well as presence within public metagenomes.

And, once various things are worked out <waves hands about
infrastructure and sustainability and cost>, I hope we can provide
this as a generic service for others to use.

So that seems neat, right?

## Cautions, reservations, and limitations

There are a few things you should know before you get too excited. I
mean, you should totally be excited, but... read on.

First, this is a proof of concept. It shows it can be done, but it is
not (yet) something that anyone other than Luiz can run! Engineering
and testing and releasing needs to happen, and that will take time.

Second, there are reasonably significant limitations to this on the
scientific side. The search will only work out to about
[90% average nucleotide identity (ANI) - a containment of .01-.05](https://github.com/sourmash-bio/sourmash/issues/1859),
which means you can robustly find matches out to the genus level, but
not beyond. That's a limitation of nucleotide k-mers and it's
something we're working on.

Small-ish queries also don't work well - we can robustly find exact
matches to 10kb chunks of sequence, but not shorter.

Third, mastiff is mostly designed around searching for _small_
queries. Query times should scale approximately linearly with the
query size. Luiz has limited the server to a 5MB query for this
reason.

And last but by no means least, this is _not_ the entire SRA, it's
only about 480,000 records (of about 700,000). We'll update it
eventually, but for now it's a sufficient proof of concept ;).

## Whither mastiff?

We (mostly Luiz ;) are working to integrate mastiff functionality into
sourmash. There's a pretty wide gap between a proof-of-concept
implementation and mature, robust, end-user-usable software, of
course, but we know how to do it.

There's probably other super cool back-end approaches we could use,
and we'd love to talk to you about them if you're interested in trying
out alternative implementations. At this point we have a fairly good
understanding of the conceptual operations and can even convey them to
you in functioning code snippets :).

I also gotta tell you that we don't know how to support this kind of
work exactly. This developed out of Luiz's thesis work but is now done
on a volunteer basis by him. JGI is supporting the server development
for a year (thanks!!) but we are a bit bottlenecked on UX support and
backend/frontend development. So
[drop us a line](mailto:ctbrown@ucdavis.edu,lcirberjr@ucdavis.edu) if
you've got some spare change - we'd be looking for 3-5 years of
support.

(I'd be interested in exploring governance and sustainability issues
around this kind of thing, too.)

## Acknowledgements

The interpretation and understanding of MAGsearch results has been
tremendously helped by work from Dr. Tessa Pierce-Ward (ANI),
Dr. Adrian Viehweger (pathogen outbreaks), Dr. Jessica Lumian
(biogeography), Dr. Christy Grettenberger (biogeography and more), and
others. Thank you!!
