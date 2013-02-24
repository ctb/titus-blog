Assemblathon 2 review, round 1, parts thereof
#############################################

:author: C\. Titus Brown
:tags: science,assembly
:date: 2013-02-24
:slug: 2013-assemblathon-review-i
:category: science

**Note: this is the general part of the submitted review; I left out
the things that I expect might change if revisions are made.**

Also see `Thoughts on the Assemblathon 2 paper
<thoughts-on-assemblathon-2.html>`__.

The review, minus specific remedies
-----------------------------------

Re `the Assemblathon 2 paper <http://arxiv.org/abs/1301.5406>`,

Bradnam et al. systematically evaluate and compare 43 de novo genome
assemblies of 3 organisms from 21 teams.  My lab and I set out to
evaluate the paper.

First, reviewing this paper thoroughly is effectively impossible; it's
huge and complicated!  So apologies for any mistakes below...

At a high level, this paper is a tour de force, analyzing the results
of applying a dozen or more different de novo assembly pipelines to
three different data sets, and ranking the results by a variety of
different metrics.  The three genomes chosen, fish, snake, and bird,
are all vertebrate genomes, so they're large and repeat-ridden, and in
some cases highly polymorphic, which makes this an extra challenging
(but realistic) set of assembly problems.  The major problem to be
overcome by this paper is that we are evaluating fuzzy heuristic-laden
software against fuzzy error-prone data in a situation where we don't
know the answer, and I think given these constraints the authors do as
good a job as is reasonably possible.

The resulting paper does an excellent job of broadly presenting the
challenges of assembly, providing a good if rather high level
discussion of the various ranking metrics they used.  Their broad
conclusions were well supported: assemblers do very different things
to the same data, and you need to pick an approach and a set of
parameters that maximize the sensitivity and specificity for your
project goals; and repeats and heterozygosity will kill you.

From a scientific perspective, I was dismayed by their failure to make
use of external data such as synteny and gene model concordance to
evaluate the assemblies.  The CEGMA scores were probably the closest
to this but the numbers were surprisingly low to me, so either CEGMA
doesn't work that well on vertebrate genomes or the assemblies are
actually worse than the paper made clear. The fosmid and optical map
analyses were not that convincing, because while they spoke to some
sort of basic agreement with orthogonal data, they didn't have the
breadth (fosmid) or resolution (optical map) to provide really solid
independent evidence of the quality.  When I am evaluating assemblies
I look for "surprises" in terms of missing gene models and odd
rearrangements compared to neighbors, and I feel like there are some
reasonably straightforward things that could have been done here.
Nonetheless, the analyses that were done were done well and discussed
well and led to clearly defensible conclusions.

A major missing component of the paper was *computational cost*.  As
someone who works primarily on how to achieve assemblies on low-cost
hardware, I can assure assembler authors that very few people can
easily run multiple assemblies on large amounts of data using their
assemblers.  This (and ease of use, documentation, and community) is
honestly going to drive choice of assembly pipelines far more so than
notional correctness.  This is especially true since a conclusion of
the paper was "try lots of assemblers because they all do differently
weird things on different data", which would lead me to the
time-saving argument that a 60% accurate easily achievable assembly is
considerably better than an 80% assembly that cannot readily be
computed.  Perhaps assemblathon 3 can be more tuned towards the
question of whether or not anyone other than the authors can run these
things and achieve good results!

While I'm talking about what I wish could have been done, it would
have been nice to have something like RNAseq for the organisms.
RNAseq can be used to look at completeness as well, by looking at the
intersection between conserved genes and genes that map to the
assembly, and I think it would have been invaluable.  Internally
focused statistical analyses are great, but there's nothing like
orthogonal data (as with the fosmids and the optical map) for real
evaluation.

I also could not figure out how much of the input data was used for
each assembly, and it didn't look like any of the analyses took this
into account -- REAPR is the only one that I would have expected to do
so, but that paper doesn't seem to be available.  How many of the
input reads actually map to the genome (or how many of the
high-abundance k-mers are present) would have been an interesting
metric, although I recognize that repeats and het make this a
difficult metric to analyze.

Finally, I think the fact that experts (in many cases the authors of
the assembler) are running the assemblers should be mentioned more
clearly: these results are presumably the best possible from those
software packages, and 3rd-party users are unlikely to do as well.

---

--titus
