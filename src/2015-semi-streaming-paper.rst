A new preprint on semi-streaming analysis of large data sets
############################################################

:author: C\. Titus Brown
:tags: khmer,streaming
:date: 2015-03-27
:slug: 2015-semi-streaming-paper
:category: science

We just posted a new preprint (well, ok, `a few weeks back
<https://peerj.com/preprints/890/>`__)! The preprint title is
"Crossing the streams: a framework for streaming analysis of short DNA
sequencing reads", by Qingpeng Zhang, Sherine Awad, and myself.  Note
that like our other recent papers, this paper is 100% reproducible,
with `all source code in github
<https://github.com/ged-lab/2014-streaming/>`__.  we haven't finished
writing up the instructions yet, but happy to share (see `AWS.md
<https://github.com/ged-lab/2014-streaming/blob/master/AWS.md>`__ for
notes).

This paper's major point is that you can use the massive redundancy of
deep short-read sequencing to analyze data as it comes in, and that
this could easily be integrated into existing k-mer based error
correctors and variant callers.  Conveniently the algorithm doesn't
care what you're sequencing - no assumptions are made about uniformity
of coverage, so you can apply the same ol' spectral approaches you use
for genomes to transcriptomes, metagenomes, and probably single-cell
data.  Which is, and let's be frank here, super awesome.

The paper also provides two useful tools, both implemented as part of
`khmer <http://github.com/ged-lab/khmer>`__: one is an efficient
approach to k-mer-abundance-based error trimming of short reads, and
the other is a streaming approach to looking at per-position error
profiles of short-read sequencing experiments.

A colleague, Erich Schwarz, suggested that I more strongly make the
point that is really behind this work: we're in for more data. Scads
and scads of it.  Coming it with ways of efficiently dealing with it
at an algorithmic level is important.  (We didn't strengthen this point
in the posted preprint - the feedback came too late -- but we will hopefully
get a chance to stick it in in the revisions.)

The really surprising thing for me is that the general semi-streaming
approach has virtually no drawbacks - the results are very similar to
the full two-pass offline approaches used currently for error
correction etc.  Without implementing a huge amount of stuff we had to
make this argument transitively, but I think it's solid.

For entertainment, take a look at the error profile in Figure 6.  That's
from a real data set, published in Nature something or other...

And, finally, dear prospective reviewers: the biggest flaws that I see
are these:

* we chose to make most of our arguments by analyzing real data, and
  we didn't spend any time developing theory.  This is a choice that
  our lab frequently makes -- to implement effective methods rather
  than developing the underlying theory -- but it leaves us open for
  `a certain type of criticism
  <https://liorpachter.wordpress.com/2014/09/11/digital-normalization-revealed/>`__.

* to extend the previous point, the algorithmic performance depends
  critically on details of the data set.  We didn't know how to
  discuss this and so the discussion is maybe a bit weak.  We'd love
  reviewers to ask pointed questions that we can address in order to
  shore it up.

* Repeats! How does all this stuff work with repeats!? I did a lot of
  work simulating repetitive sequences and couldn't find any place
  where repeats actually caused problems.  My intuition now tells me
  that repeats are not actually a problem for methods that interrogate
  De Bruijn graphs using entire reads as an index into the graph, but
  I'd welcome someone telling me I'm wrong and either telling me
  where to look, or asking concrete questions that illuminate better
  directions to take it.

--titus
