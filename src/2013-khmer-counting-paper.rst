New paper posted -- "These are not the k-mers you are looking for"
##################################################################

:author: C\. Titus Brown
:tags: khmer, k-mer counting, ngs
:date: 2013-09-12
:slug: 2013-khmer-counting-paper
:category: science

We've just posted a new paper to arXiv: `"These are not the k-mers you
are looking for: efficient online k-mer counting using a probabilistic
data structure." <http://arxiv.org/abs/1309.2975>`__ We'll be
submitting it to PLoS One after we wait a few days for comments from
the Twittersphere and/or on `Haldane's Sieve <http://haldanessieve.org>`__.

The paper discusses our `CountMin Sketch
<http://en.wikipedia.org/wiki/Count%E2%80%93min_sketch>`__
implementation of a memory-efficient k-mer counting system, which
we've been using for a long time now (`first post: July 2010!
<http://ivory.idyll.org/blog/kmer-filtering.html>`__).  The software
is called khmer, and between when we started working on the khmer
software and this submission, k-mer counting has exploded in
popularity, with `Jellyfish
<http://bioinformatics.oxfordjournals.org/content/27/6/764>`__,
`BF-Counter <http://www.biomedcentral.com/1471-2105/12/333>`__, `DSK
<http://www.ncbi.nlm.nih.gov/pubmed/23325618>`__, `KMC
<http://www.biomedcentral.com/1471-2105/14/160>`__, and `Turtle
<http://figshare.com/articles/Turtle_Identifying_frequent_k_mers_with_cache_efficient_algorithms/791581>`__
all joining the venerable `Tallymer
<http://www.ncbi.nlm.nih.gov/pubmed/18976482>`__ software in this
space.  As you might expect, we got a little bit worried that we were
going to be late to the party.  ...this paper is us bringing the
dessert, or at least refreshing the punchbowl :).

I think the paper is interesting for a few different reasons.

First, the approach, and the software we built around it (`khmer
<http://github.com/ged-lab/khmer/>`__, are at the core of our
research: `partitioning
<http://www.pnas.org/content/early/2012/07/25/1121464109.abstract>`__
and `digital normalization <http://arxiv.org/abs/1203.4802>`__ were
built on top of this approach.  This paper is a long-awaited addition
to those.

Second, it turns out that khmer is one of the few k-mer counting
libraries to support online k-mer counting: many of the other
libraries are built to read through all the data once, and then answer
questions about the data.  (BF-Counter is the only published k-mer
counter that does this at scale, but the current version is quite
slow.)  This was very important for us because streaming approaches
like digital normalization depend on having immediate updated access
to k-mer counts; for example, single-pass diginorm requires online
k-mer counting (which might help explain why Trinity, which uses
Jellyfish for their normalization approach, `uses an offline algorithm instead <http://ivory.idyll.org/blog/trinity-in-silico-normalize.html>`__).

To put it another way, khmer gives circumstantial evidence that **API
is destiny**.  I don't think we would have developed diginorm if we'd
developed an offline API.  As a programmer, this is a deeply pleasing
observation: good (flexible) APIs lead to more flexible research.  Or,
to put it yet another way, "Better Science through Superior Software!"
While this is mostly applied to people focused on sustainable
software, it also applies to situations where good API design can open
up new research directions.

Third, we show that probabilistic approaches are the bomb for k-mer
analysis.  Approaches like the CountMin Sketch and the Bloom filter
(as used in BF-Counter) rely on left-skewed probability distributions
for efficiency. As this paper shows in detail, that perfectly
describes k-mer abundance distributions in shotgun Illumina datasets;
hence the use of a CountMin Sketch is not only appropriate but
actually works extremely well.

Fourth, we show that khmer scales about as well as other "good" k-mer
counters like Jellyfish and DSK.  I'm not sure we did a fantastic job
of discussing the tradeoffs but it's clear that we now have an
excellent range of good choices for k-mer counters, and khmer is
one of them.

Fifth, as with several of our other papers -- most notably `the
diginorm paper <http://ivory.idyll.org/blog/replication-i.html>`__ --
this is a **completely reproducible paper**.  (In fact, I think this
one is *better* than the diginorm paper, because more of it is
automated.  See `our tutorial
<https://github.com/ged-lab/2013-khmer-counting/blob/master/tutorial.rst>`__
for running this on Amazon.)

And let me just say... it's not that hard to make papers reproducible,
even with gobs of data.  It took a certain amount of work for Qingpeng
to figure it all out, but that was because I hadn't been pushing him
enough from the beginning.  If we'd started earlier the whole
reproducibility & automated pipeline approach would have been no
sweat.

Sixth, we now have a nice standard benchmarking pipeline for k-mer
counters.  So, coming up soon: `understanding computational
bottlenecks for various things
<http://ivory.idyll.org/blog/pycon14-sub.html>`__, and, of course, see
my `older blog post on this
<http://ivory.idyll.org/blog/kmer-counting-benchmarks.html>`__.
Moreover, we (and others!) can now quickly spot-check and
cross-compare the performance of new k-mer counters using this
pipeline.

One minor regret is that it's not *that* easy to add something to the
pipeline.  We focused far more on getting the paper out than on making
the pipeline easy to modify.

Seventh, and the sleeper surprise -- diginorm is really efficient at
high false positive rates!  Richard Smith bugged me about a snarky
comment we had in the diginorm source code (see `github issue
<https://github.com/ged-lab/khmer/issues/157>`__) where we warned
people not to change the max threshold for diginorm false positive
rate.  This was because, until recently, we had no idea what a good FP
rate was!  It turns out that for diginorm you can get by with an 80%
false positive rate without suffering much, at least in terms of the
E. coli genome assembly; this is because the median k-mer abundance
used by diginorm is very refractory to high FP rates.

Eighth, I think the title is really awesome. Dr. Tracy Teal gets credit
for that one, even if we can't get it past reviewers.  (*My* best idea
was "Count me maybe: ...")

Enjoy!

--titus

