Title: sourmash 4.1.0 released!!
Date: 2021-05-17
Category: science
Tags: sourmash, software, release
Slug: 2021-sourmash-v4.1.0-released
Authors: C. Titus Brown
Summary: sourmash v4.1.0 is here!

We are pleased to announce that sourmash v4.1 is now out! As usual [it can be installed via conda or pip](https://sourmash.readthedocs.io/en/latest/#installing-sourmash). You can [read the release notes here](https://github.com/dib-lab/sourmash/releases/tag/v4.1.0) for details, or just read on here for the highlights!

## One big new command-line feature - zipfile collections.

One command-line feature that opens up a lot of new opportunities down the line is support for zipfile collections.

Zipfile collections provide a way for sourmash to take in potentially *very* large collections of signatures. Briefly, you can take a directory hierarchy of signatures and zip them all up, and sourmash can now load the signatures directly from the zip file - so you can distribute collections of signatures, search and gather and compare on them, and so on.

Now, back in v3.3.0, Luiz [added .zip as a storage format for Sequence Bloom Trees](http://ivory.idyll.org/blog/2020-sourmash-databases-as-zip-files.html), indexed databases of signatures. These are fantastic, but because of the nature of SBT indices, they came with some restrictions - they had to be compatible signatures, and big SBTs consumed a lot of disk space and memory. While we're working on fixing that separately, zipfile collections offer an alternative that is not faster but does offer some more conveniences.

In particular, unlike SBTs, zipfile collections can store incompatible signatures, and they don't consume any extra memory, and they don't require any ancillary files. This lets us (not so hypothetically...) store k=21, k=31, and k=51 signatures for [all 300k+  GTDB genomes](https://osf.io/wxf9z/files/) in a fairly small (~8.5 GB) zipfile. You can also get the GTDB representatives in even smaller files (1.5 GB) and we built SBTs for them, too (2.8 GB each).

The remaining problem is that zipfile collections aren't indexed, and so searching 300k+ signatures is not really that fast because you're doing it linearly. While `search` can handle it, iterative approaches like `gather` cannot. To that end, we added interim support via `prefetch`. Read on!

## Another nifty command line feature: `prefetch`.

`sourmash prefetch` is a command that basically does a `sourmash search --containment`. It only works on scaled signatures (more about that soon, promise), and it's meant as a prefilter for `sourmash gather`. The idea is, you run `prefetch` with a metagenome query, and `prefetch` finds all of the potentially relevant signatures, and then saves them for you. Then, you run `sourmash gather` on the saved signatures, which winnows them down to the smallest possible list of genomes relevant to your metagenome.

Why implement `prefetch`? A couple of reasons -

* we already had code in some other projects that did this and was quite useful.
* it was an easy feature to implement that led to massive speedups when doing certain kinds of parameter exploration.
* it's explicitly streaming compatible, because it doesn't need to hold anything in memory long-term - it's meant to walk across whatever (potentially very, very large...) databases and collections you give it, and output any relevant matches. As we're approaching a million genomes in Genbank, this feature seemed ...relevant.
* last but not least, _internal_ support for prefetch goes with some excellent internal primitives that can now be further optimized. More about THAT in some future releases :).
* prefetch also lets us support some other features, such as reporting ties in `sourmash gather`. We don't do that yet, but we can do so _much_ more easily now.

So how would you use prefetch? You don't need to, really - it now underpins gather, so `sourmash gather` on a zipfile containing all 300k+ GTDB genomes will actually run much, much faster than it ever would have before, despite using a linear search underneath.

For some speed comparisons of the new features, see [sourmash issue #1530](https://github.com/dib-lab/sourmash/issues/1530) - here's the summary, for searching approximately 45,000 signatures from GTDB with a fake metagenome built from 4 genomes -

|          | Time (s) | Memory (mb)|
| -------- | -------- | -----------|
| 1. index, prefetch     | 10s     | 215mb       |
| 2. index, no prefetch     | 22s     | 214mb       |
| 3. no index, prefetch     | 207s     | 81mb       |
| 4. no index, no prefetch     | 811s     | 87mb       |

So obviously you want to use an index if you have the memory, but if you don't, you definitely want to use prefetch! Happy to discuss the scaling behavior in the comments or over at the github issue, too - the short version is that the time for rows (2) and (4) should scale with the diversity of the metagenome.

Important note: before sourmash 4.1, row (2) above was the only behavior supported. :) All of the behaviors above can be toggled at the command line.

## Last but by no means least: flexible and online output formats for saving signatures

As we were implementing all this, it turned out to be easy to refactor in some more flexible output formats.  You can now specify that `sketch`, `search`, `gather`, and `prefetch`, as well as many of the `sourmash sig` manipulation commands, should put their output signatures in a directory (`output/`), a Zip file (`output.zip`), or a compressed sig file (`output.sig.gz`). These are also streaming compatible - the zipfile and directory output saves matches "as you go", without holding them in memory. And, since all of these can be passed into sourmash as collections to search and manipulate, we have a pleasingly complete set of storage formats!

## Other features

The [release notes](https://github.com/dib-lab/sourmash/releases/tag/v4.1.0) should be pretty comprehensive, and they do contain links into the pull requests (and from there, into the issues) that we addressed for this release. In particular, note that as our user base expands we're getting a wider range of issues submitted. Many of these are straightforward to fix - so this release addresses a fair number of those user requests, too.

In particular, this release should address a number of Windows issues around encodings and newlines; we don't yet provide wheels for Windows, but we're getting a lot closer!

## Internal improvements and enhanced flexibility

For me the really exciting thing is the internal refactoring that under-pin the features above. We've significantly reworked the internals to consolidate code, make new features easier to add, better support streaming of large signature collections, and permit many more optimizations. Coincidentally (we swear!) the refactoring also sped up some of our core operations - `sourmash gather`, in particular, is twice as fast and consumes 80-90% less memory on SBTs! Maybe that's the sign of a good refactoring? Or maybe we just got lucky...

sketchily yours,
--titus
