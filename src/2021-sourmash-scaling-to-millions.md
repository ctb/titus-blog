Title: Scaling sourmash to millions of samples
Date: 2021-07-13
Category: science
Tags: sourmash, software, genbank, SRA, gtdb, k-mers, minhash
Slug: 2021-sourmash-scaling-to-millions
Authors: C. Titus Brown
Summary: Bigger and better!


(Many thanks to Dr. Luiz Irber, who sunk the pillars and laid the foundations for a lot of the work below. Dr. Tessa Pierce and Dr. Taylor Reiter drove much of our engineering work by constantly coming up with new! and bigger! use cases that were also quite exciting and motivating ;)

[sourmash](https://sourmash.readthedocs.io/) is our software for quickly searching large volumes of genomic and metagenomic sequence data using k-mer sketching. We're up to version v4.2.0 now, and looking forward to releasing v4.2.1 sometime in the next month.

One emerging theme for sourmash for the v4 series has been *scaling*. There are a variety of large-scale data sets that continue to grow in size, and it sure would be nice to be able to work with them easily.

The challenges are big and growing. In no particular order,

* NCBI has about a million microbial genomes in their GenBank database;
* the Sequence Read Archive contains well over a million microbial shotgun sequencing data sets, with about 600,000 of them being large metagenomes;
* the [GTDB taxonomy group](https://gtdb.ecogenomic.org/) has produced revised taxonomic annotations for 250,000 of the GenBank genomes;
* individual research projects can now quickly and easily produce hundreds of genomes and dozens to hundreds of metagenomics samples, so the numbers above are growing rapidly.

Thanks to Luiz Irber's work, discussed in his [thesis](https://github.com/luizirber/phd/releases), we have a nice distributed system ('wort') that computes new sourmash sketches as new data enters the system. (Some of that is also described in [my blog post about searching all public metagenomes](http://ivory.idyll.org/blog/2021-MAGsearch.html).) Also thanks to Luiz, over the last two years sourmash was [refactored to use Rust underneath](https://blog.luizirber.org/2018/08/23/sourmash-rust/), and we've been enjoying a number of [raw performance gains](https://twitter.com/ctitusbrown/status/1356344041978228736).

The challenges we're struggling with now are because of all of this. We  *have* a lot of data that we *can* work with (package, search, etc.), but our processes and infrastructure for working with it haven't scaled to meet the new capabilities of sourmash. Briefly,

* we have several millions of files sitting in various directories, representing sketches for a lot of public data.
* it's prohibitively slow to scan through all of that information repeatedly, and difficult or impossible to fit it all in memory (depending on the collection in question).
* most sketches are not really interesting for any given operation, so a lot of our scanning would be redundant anyway.

Because of this, a lot of our work since the 4.0 release has been on technical changes to support *better processes* that will better handle searching, collating, and updating collections of bajillions of files.

## Motivation: building new database releases

One of the several major uses of sourmash is searching genome collections, with the goal of finding matches to and/or classifying genome or metagenome samples.  We variously use the GTDB genomic representatives database (48k genomes), the GTDB complete database (250k genomes), or the NCBI microbial database (~800k genomes). And we want to [provide these databases](https://sourmash.readthedocs.io/en/latest/databases.html) for download so that sourmash users don't have to do all the prep work themselves.

To provide these databases,

* first, we need to sketch all the genomes. This involves downloading each genome, running `sourmash sketch`, and saving the results somewhere. This is what wort does - it monitors NCBI for new genome entries, calculates the sketches, and makes them available for download.
* then we need to select a _specific_ set of sketches based on a catalog (GenBank microbial, or GTDB genomic reps, or whatnot) and a set of parameters (k-mer size, mostly).
* next we need to figure out which sketches do not exist in our overall collection, for whatever reason, and find/build those. (e.g. NCBI GenBank is somewhat fluid, and GTDB isn't always synced with its releases; or something just slipped through the wort cracks; or GenBank never actually _had_ the right sequence, so it needs to be calculated)

If you have 100, 1000, or even 10,000 sketches, this is all pretty easy. It only starts to get annoying when you have 100,000 and more. We have a million :).

## Investing in scaling - some principles

There are a number of techniques for working with large volumes of data.

First, **lazy loading**. Better known as [Lazy Evaluation](https://en.wikipedia.org/wiki/Lazy_evaluation), this is a CS concept where you pass around references to objects, and only resolve those references when you decide to actually use the object. Since references are usually (much) cheaper than the full object, you can save on memory.  In the case of sourmash, one of our on-disk search structures,  the Sequence Bloom Tree (SBT), has relied on lazy loading for years, and we've been expanding this to sketch collections more generally.

Second, **streaming input and output**. Another CS concept, [streaming](https://en.wikipedia.org/wiki/Stream_(computing)) means that you perform as many operations as possible on individual items, and don't hold all the items in memory (ever). We've always intended to support large-scale streaming I/O in sourmash, but it hasn't been a priority before this. Luckily Python gives us lots of tools - generators, in particular - for doing streaming!

A related concept to streaming is to **avoid accumulating anything big in memory**.  This is easier said than done - for one not-so-random example, if you're searching a big database for matches, it is very easy to just keep matches in memory and then deal with them as a single collection. But what if a large portion of that database matches? You need a place to store the matches!

Fourth, **use metadata to filter as much as possible**. This seems separate from but maybe overlaps with lazy loading... basically, you want to work with catalogs of your data (which are less bulky), rather than your data itself (which is usually much larger).

Fifth, **support flexible filtering**. It's very easy to write custom solutions that get you what you need today, but a more general solution may not be much more work and will save you time later, as your use cases evolve.

Sixth, **use databases**. This may be obvious, but it's always worth remembering that there are literally decades of work on storing and searching structured catalogs of data! We should make use of that software! And if we use sqlite3, we have a superbly engineered and high-performance SQL database that is embedded in many programming languages!

Seventh, **think declaratively** instead of procedurally. Try to describe *what* you want to do with the data, now *how* you want it done (and in particular, avoid for loops as much as possible :). Abstracting the operations you want to do into a declarative form permits refactoring and optimization of the underlying implementation. 

So how is this all shaking out in sourmash?

## Iterating towards nerdvana: a progress report

We've invested considerable amounts of effort into engineering over the last year, iterating towards implementations of the above practices.

### Round 0 (sourmash 3.x through sourmash 4.0)

By the release of [sourmash 4.0](https://github.com/sourmash-bio/sourmash/releases/tag/v4.0.0) in March 2021, we had included a lot of good optimizations and refactoring already.

Way back in 3.x sometime, Luiz had moved sketch loading into Rust. This led to a ridiculous speedup in pretty much everything - 100-1000x.

We had slowly but surely made our way to a standard `Index` class API that let us collect, select, and search on large piles of sketches.

In particular, we'd started to invest in *selectors*, that let us specify features (like k-mer size, or molecule type) that we wanted our collection limited to.

### Round 1 (sourmash 4.1)

For [sourmash v4.1.0](https://github.com/sourmash-bio/sourmash/releases/tag/v4.1.0), two months later, we evolved things more.

We had a lazy selection `Index` class that deferred running the selectors until the actual sketches themselves were requested.  Getting the class to work properly and supporting it fully throughout the code base (and testing the bejeezus out of it) forced us to regularize the class API some more, which opened up many more opportunities.

We also added *generic* support for retrieval of sketches by random access into a collection, through our use of .zip collections and `ZipFileLinearIndex`. This was an expansion of the lazy loading and on-disk storage that SBTs had enjoyed since v3.2, but without the same overhead cost of the data structures. So, now it was possible to package really large collections of sketch in a compressed format *and retrieve individual sketches directly*, with minimal overhead. Not so incidentally, this was also our first random-access/on-disk mechanism that could store _incompatible_ sketches - so it was much more flexible than what we'd been doing before.

The internal (and command-line) support for the streaming `prefetch` functionality was also a watershed moment.  Prior to `prefetch`, all of our database search methods did a search and then sorted all of the results to present a nice summary to the user. While useful, this meant that if you had lots of matches, you had to store them all in memory so you could sort them later. This could be ...prohibitive in terms of memory, and we already had specific examples where we knew it wouldn't work. `prefetch` was a new feature that was *explicitly* streaming and was meant to search Databases of Unusual Size: so, it simply output matches as it found them, with no sorting.

Last but by no means least, once we had streaming _input_ we needed streaming _output_, so we implemented a general sketch saving method that supported several standard output methods (to directories and zipfiles, in particular) to offload sketches directly to disk.

Together, what this all meant was that we could finally:

* take an arbitrarily large collection of on-disk sketches,
* select just the ones we wanted without necessarily loading them all,
* walk across those sketches one by one, storing no more than a small number of them in memory,
* find matches and offload those matches to disk as we went.

There were still some suboptimal constraints that had to be obeyed, but they were in the implementation, not in the API, so we "just" needed to iterate on the implementation :).

This was the first crack in the dam of database building (one of our motivating use cases): once we had zipfile collections implemented, we could first build zipfile collections and then use those zipfile collections as our source build for all the other database types that supported fast search. (And, indeed, we now have [a snakemake workflow](https://github.com/sourmash-bio/sourmash/issues/1511#issuecomment-867759491) that does exactly that!.)

### Round 2 (sourmash 4.2)

Between v4.1 and v4.2, we had several minor releases that cleaned things up and improved edge case efficiency. 

For [sourmash v4.2.0](https://github.com/sourmash-bio/sourmash/releases/tag/v4.2.0) in early July 2021, however, we doubled down on the "working with large collections" theme.

First, we introduced ["picklists"](https://sourmash.readthedocs.io/en/latest/command-line.html?highlight=picklist#using-picklists-to-subset-large-collections-of-signatures), which give command-line and API-level support for selecting sketches based on their metadata features (not their content). The initial implementation was slooooooow on large data sets, but this was an important declarative mechanism (that immediately saw extension in unexpected directions, too!)

This was followed (in the same release) by database *manifests*, a feature that is not user-facing at all (and doesn't show up in the docs, either - oops!). Manifests are simply a spreadsheet-style catalog of the metadata for all the sketches in a particular database, and they can be calculated *once* and then included in zipfiles. They support direct retrieval of sketches by id, as well as rapid intersection with picklists.

These two features were relatively minor in terms of new user-facing functionality - although they do support some cool stuff! - but were massive in terms of internal improvements.

For example, it was now virtually instant to take a zipfile collection of 260,000 sketches and pick out the three sketches you were interested in, based on whatever criteria you wanted.

So, as a not so random example, you could run `prefetch` on a big database (low memory, streaming...) and save only the CSV with match names, and then *just use that CSV* as a picklist to run further operations on the database - search, gather, etc. There's no need for intermediate collections of sketches in workflows! (This has saved us literally 100s of GBs of disk space already!)

As another not-so-random example, you could load a manifest from a Zipfile collection, run your sketch selection (ksize, molecule type, identifier, etc.) on the manifest in memory, and then go back to load _only_ the relevant sketches from disk as you needed them.

Again, the internal implementation is leading the user-facing features here, and there are still some performance issues, but the API support is there and seems flexible enough to support a wide range of optimizations.

### Round 3 (sourmash 4.2.1, maybe?)

The next release will add some internal support for more/better manifest stuff. In particular, I've been experimenting with a *generic* lazy loading index class, which lets us do clever things like load a manifest, do selection and filtering on it, and only actually go to the disk to load the index object when we're ready - previous approaches always worked on the loaded index, which is suboptimal when you have thousands of them.

With this new class, we can apply the manifest directly as a picklist and subset down to just the sketches we care about.  (As with all of these things, I've been [playing around](https://github.com/sourmash-bio/sourmash/pull/1619) with different implementations and throwing different use cases at them, and it's been  "interesting" to watch various  solutions fall apart under the burden of really large collections!)

One thing this has let me do is (finally!) re-engineer database releases around manifests, using (tada) [manifests of manifests](https://github.com/ctb/2021-sourmash-mom). With this we do the following -

* load many manifests from many collections into a single SQLite database;
* run our metadata selection (k-mer size, molecule type, picklists, etc.) on this database, using SQL primitives;
* and then go grab precisely those sketches we care about, for further downstream processing.

In _practice_ this lets us do things like cut a new database release for GTDB quickly and easily - it takes [only a minute](https://github.com/sourmash-bio/sourmash/issues/1652#issuecomment-877647611) to verify that we have all of the necessary sketches and return their locations. (And like everything else, it can probably be optimized dramatically.)

### What's next? (sourmash 4.3 or later)

We've been [somewhat fixated](https://github.com/sourmash-bio/sourmash/issues/1350) on trying to provide good user experience (fast, performant, communicative) around searching Extremely Large Collections.

We have a prototype solution for near-realtime search of 50k+ sketches (see [sourmash#1226](https://github.com/sourmash-bio/sourmash/issues/1226) and [sourmash#1641](https://github.com/sourmash-bio/sourmash/issues/1641)) and at some point that will make it into the codebase. At that point we will be closer to fully exploiting CPU and disk capabilities; right now our speed is mostly bound by our lack of parallelism.

Somewhere down the road we're going to expand our persistent storage options. We support file storage, zipfiles, Redis, and IPFS for SBTs already (thanks again Luiz!) but want to support these for more collection types. Not hard now, just ...work.

And, as a nice cherry on top of the sundae, after all of the `Index` API refactoring we did back in 4.0 and 4.1, we can now easily support client/server mechanisms via remote procedure calls using only the standard interface - see [sourmash#1484](https://github.com/sourmash-bio/sourmash/issues/1484). This opens the door to using larger in-memory database types, which have been hampered thus far by the loading time.

## Some concluding thoughts

Why are we putting so much effort into all of this? There are a couple of reasons:

* sourmash is underpinning a lot of different work in our lab, and these kinds of efficiency enhancements really make a difference when amortized over 5 projects!
* routine lightweight search of all public data will unlock a lot of use cases that we can only see dimly right now. But our experience has been that *actually building* stepping stones towards this dimly-seen future set of use cases is the best way to make them happen (or to figure out why they can't or shouldn't happen).
* it's fun! This has been a labor of love during some rough pandemic times, and it's been nice to actually make visible progress on something over the last 18 months...

That all having been said, it's been a lot of work to solve the engineering challenges, with only fuzzy use cases to motivate us. Moreover, a lot of the work we describe above is not directly publishable. It's not entirely clear how we'll roll this out in a way that supports people's careers. So it's a bit of a gamble, but hey, that's what tenure's for, right?

(There's definitely some more to discuss here about the tension between grant writing and a focus on slow, careful, and iterative engineering of new capabilities - my tagline in lab for this is "boring in theory, transformative in practice" - but that's another blog post.)

Some other thoughts -

**Abstractions sure are convenient!** Figuring out the right APIs internally has led to a renaissance in our internal code, although I think we need to step up our code docs game, too, so that someone other than the core developers can make use of these features :(.

**Declarative approaches are awesome.** It's been really nice to redefine our APIs in terms of what we want to have happen, and then implement differently performing classes (storage, search, selection) that we can mix and match depending on our requirements.

**Automated testing has been key!** We embarked upon the v4 journey with a codebase at about 85% code coverage, and having those solid building blocks has been critical. We continue to discover API edge cases that need to be resolved, and then we *immediately* lock them down with more tests. Without these tests, the massive-scale refactoring we've been doing would never have worked. (A `diff --stat v3.5.1` shows virtually every source file changed, with 17738 lines added, and 3546 removed, in a codebase with only 50,000 lines of code and tests!)

**Python is awesome**. The language supports really nice abstraction layers, provides good language primitives for streaming and lazy evaluation (generators in particular!), and has both a massive stdlib and straightforward installation system that means that adding new capabilities to software built in Python is quite easy.

**Rust is awesome**.  We're really liking Rust as a high-performance layer under Python. The boundaries are still being negotiated - who owns what objects is a persistent theme, for example, and we're still working on fleshing out Rust support for new storage types - but Python is challenging for compute-focused multithreading while Rust supports it very straightforwardly (and way, way better than C++).

Last but not least, **sqlite3 continues to be amazing**. I'm not even that good at tuning it, and it's already incredibly efficient; if we put time and effort into better schema, we'll probably get an order of magnitude improvement out of it with only a few hours of work. We just don't need that yet :).

--t
