The future of khmer (2013 version)
##################################

:author: C\. Titus Brown
:tags: science,khmer,assembly,ngs
:date: 2013-05-14
:slug: the-future-of-khmer-2013-version
:category: science

.. @why excited? sole grant

So, I got this grant.  And, um, it looks like khmer has a future, which
means... so does my lab.

Some background
~~~~~~~~~~~~~~~

What is khmer?

khmer is my lab's software for doing various things to
sequencing data, and is largely focused on providing good demo
implementations of low-memory data structures and efficient -- often
streaming, single-pass -- algorithms relating to de novo assembly.

khmer has been fairly successful in some ways, starting with `my
posting of it as a low-memory way to scalably count k-mers
<http://ivory.idyll.org/blog/kmer-filtering.html>`__, followed by the
publication of `a paper on how to build de Bruijn graphs on Bloom
filters
<http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__, aka 'partitioning', and
continuing with the posting of a preprint on `efficient streaming
lossy compression of shotgun sequencing data sets
<http://arxiv.org/abs/1203.4802>`__, aka 'digital normalization'.  In addition to having a user
population somewhere in the dozens to the hundreds (note: we don't
really have any way to keep track accurately, so this is anecdotal),
people have incorporated ideas from khmer & our pubs into the `Minia
genome assembler <http://minia.genouest.org/>`__, the `Trinity mRNAseq
assembly pipeline
<http://www.ncbi.nlm.nih.gov/pubmed/23845962>`__
and the `Mira assembler
<http://mira-assembler.sourceforge.net/docs-dev/DefinitiveGuideToMIRA.html#sect_ref_data_reduction>`__. A
number of papers have come out that use khmer in various ways, mostly
taking advantage of the diginorm stuff.

For me, the biggest change has been that many previously unachievable
assembly problems are now relatively simple and straightforward.  I
think our most technically *impressive* paper to date is our paper on
`assembling previously unassemblable metagenomes
<http://arxiv.org/abs/1212.2832>`__.  However, digital normalization
(and `its derivative, in silico normalization <http://trinityrnaseq.sourceforge.net/trinity_insilico_normalization.html>`__) has probably
been most widely used for mRNAseq, where it can convert a previously
intractable *de novo* assembly task into something quite do-able.

All in all, not bad for five years, starting from 0 (knowing nothing
about assembly) and going to about 50 (being able to assemble just
about anything *but* soil).  We can do `contig assembly of
ridiculously large metagenome data sets
<http://ivory.idyll.org/blog/jgr-assembling-the-amazon.html>`__ but
ultimately this is an `infinite assembly problem
<http://ivory.idyll.org/blog/crowdsourcing-my-research.html>`__, and
my grants for that keep on getting rejected; still, I have hope.

What's the goal of khmer?
~~~~~~~~~~~~~~~~~~~~~~~~~

I nominally "direct" my lab, which really means fund, lead, and lead
astray -- I consider myself kind of a `chaos monkey
<http://techblog.netflix.com/2012/07/chaos-monkey-released-into-wild.html>`__
in lab meetings, for better or for worse.  I take a similar approach
to software development, albeit with a bit more of a direction.
So it can be a bit hard to define a goal.

One thing that khmer is: it's a test bed for trying to implement good
software development practices in an academic setting.  Not sure how
successful I've been at that -- I talk a good game, but we still don't
do (for one example) continuous integration.  The first software
engineer I hired for khmer, specifically, had experience working on
large projects in physics and elsewhere; it's pretty clear that khmer
was far below his standards for a project!

I'm also trying to use khmer as a test case to show that a core
library of reusable code can be used to more effectively do
computational science: better science through superior software!  That
has been amply validated thus far, and new and additional results will
be emerging over the next months and years as we expand khmer with
additional functionality.

khmer is also a test bed for development of new algorithms and data
structures, and demo implementations of these algorithms.  Diginorm
itself is about a 5 line Python program, once you have an online k-mer
counter; partitioning is, in theory, not much more complicated until
you hit large-scale problems.  Some of our new code is going to be a
bit more complex than diginorm, but we really are trying to KISS and
provide software that implements a scalable and usable version of our
core theoretical and computational ideas.

khmer is definitely *not* intended to be the one true software
implementation of our ideas.  There are two reasons for this: first, I
believe both `ideas <http://ivory.idyll.org/blog/w4s-overview.html>`__
and `software
<http://ivory.idyll.org/blog/research-software-reuse.html>`__ should
be remixable and remixed in order to advance science better; and
second, we don't have the funding to support its broad use.  I do get
a bit testy with people that implement our ideas *more poorly* than the
khmer implementation, but I understand why they do it; especially for
stuff like diginorm, importing the whole khmer codebase is silly.  (If
you've written an assembler, diginorm is, literally, 5 lines of code
on top of that code.)

What's the future of khmer?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

As I indicated in my `post on the new multithreaded read parsing
coming to khmer
<http://ivory.idyll.org/blog/multithreaded-read-parsing-in-khmer.html>`__,
at the moment we don't have much energy or focus to spend on
optimizations, incremental improvements, and sanding down the corners
of the software.  We're instead focusing on "shooting for the moon",
expanding khmer to do things like `streaming error correction
<http://ged.msu.edu/downloads/2012-bigdata-nsf.pdf>`__, `variant
calling <http://ged.msu.edu/downloads/2012-bigdata-nsf.pdf>`__, and
`infinite assembly
<http://ged.msu.edu/downloads/2012-career-nsf-final.pdf>`__.

There are two reasons for this focus on big projects and advances.

First, I'm an *academic*, running a *research lab*.  My output is
*supposed* to be focused on high-impact, go-for-broke stuff.  Mind
you, I am expected to do this while carefully limiting myself to safe
grant-fundable projects that are unlikely to fail; writing incremental
papers that I can get easily published; and graduating students -- but
that tension is just part of the fun academic game, amiright?

Second, we don't have the funding.  To really make our approaches a
viable option for many people, we'd have to expand our focus to
include a much wider range of things, such as: user interfaces; better
documentation; integration with existing pipelines; more fiddly
features that people need (or think they need); collaborations with
large groups; etc.  This requires attention and focus and effort, by
highly trained personnel that aren't emphasizing cutting edge
research.  This requires money.  Moolah.  Cash.  Cabbage.

We don't have it.

Oh, wait.  That's the news!

We've got money!
~~~~~~~~~~~~~~~~

The big news is this: our BIG DATA grant proposal, `Low memory
Streaming Prefilters for Biological Sequencing Data
<http://ged.msu.edu/downloads/2012-bigdata-nsf.pdf>`__, has been
funded as a 3-year NIH R01.  And yes, this is the grant where the
reviewers `specifically recognized open source, blogging, and
community engagement as a positive
<http://ivory.idyll.org/blog/openness-and-online-reputation-recognized-in-grant-reviews.html>`__.

I would also like to claim the extra bonus points for receiving this
grant during the `sciquester
<http://news.sciencemag.org/sciencenow/sciquester/>`__ ;).

Of the grants I wrote last year, this was probably the biggest shot in
the dark.  The `BIG DATA competition
<http://www.nsf.gov/news/news_summ.jsp?cntn_id=123607>`__ was very
visible and highly competitive, and very cross domain -- so I had to
write the grant in such a way as to convince non-biologists that this
was an important issue.  When I heard that my reviews were positive,
I was completely floored; when I read them, I was even more surprised.

So what does this funding mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I quote from above:

   To really make our approaches a viable option for many people, we'd
   have to expand our focus to include a much wider range of things,
   such as: user interfaces; better documentation; integration with
   existing pipelines; more fiddly features that people need (or think
   they need); collaborations with large groups; etc.

That.  That is what this funding means.

More specifically,

1. New features.  We've already got prototype code working for a lot
   of the aims of this grant, including: streaming reference-free
   mapping of reads; streaming error correction of genomic,
   metagenomic, and mRNASeq data; and streaming variant calling.  But
   the code isn't efficient, well-tested in isolation (esp on real
   data), or integrated into pipelines that other people might use.
   That is going to require a lot of effort.

   I also want to play around with dynamically sized bloom filters,
   reasonably efficient but non-probabilistic graph representations,
   and mechanisms for distributed implementations of the streaming
   algorithms.

2. Cloud computing. We also want to benchmark the heck out of it in
   realistic situations, so that we can examine the tradeoffs
   and understand what will happen on crummy hardware, limited memory,
   bad I/O, etc.  I'm personally less interested in *specialized*
   hardware than in *commodity* or *rental* compute, which is (sorta by
   definition) what everyone actually has.

3. Integration with user interfaces.  While not part of *this* grant,
   a lot of khmer was developed with the ultimate goal of connecting
   with end-users.  I'd like to engage with Galaxy, KBase, and
   (especially) iPlant to see if we can better integrate with their
   workflows and UIs.

A big part of my focus going forward is going to be *theory*.  There
is are massive distinctions between a good idea ("hey, I bet diginorm
could work!"), an implementation ("hey, diginorm works on this real
data set!"), and a solid *understanding* ("hey, diginorm will always
work under this range of conditions/data sets/etc.").  The latter is
most valuable, but trickiest.  If we really want to produce a solid set
of widely usable data structures and algorithms, we need to be able to
define when they are and aren't usable or worthwhile.

What else does this funding mean?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's just say that an R01 helps my tenure case at MSU more than `my
klout score
<http://ivory.idyll.org/blog/i-got-tenure-via-klout.html>`__ ever
will.

What hasn't been funded?
~~~~~~~~~~~~~~~~~~~~~~~~

Oh, lots of things.  The one I'm most frustrated by is `my NSF CAREER
proposal <http://ged.msu.edu/downloads/2012-career-nsf-final.pdf>`__,
which was rejected a few weeks back.  I think it's a bit ironic that
the one kind of work that has *never* been funded in my lab is the
metagenome assembly work, which is `the only place we've published
<http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__, and
probably where I'm best known and the work is most needed.  Sigh.

Still, this funding is a great start, and a good sign for the future!

--titus
