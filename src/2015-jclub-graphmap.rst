DIB jclub: Fast and sensitive mapping of error-prone nanopore sequencing reads with GraphMap
============================================================================================

:date: 2015-07-22
:authors: Luiz Irber, Sherine Awad, Camille Scott, Lisa Cohen, Tamer Mansour, \C. Titus Brown
:tags: read mapping, jclub
:slug: 2015-jclub-graphmap
:category: science

**Note:** at the `Lab for Data Intensive Biology
<http://ivory.idyll.org/lab/>`__, we're trying out a new journal club
format where we summarize our thoughts on the paper in a blog post.
For this blog post, Luiz wrote the majority of the text and the rest
of us added questions and comments.

----

The paper:

Fast and sensitive mapping of error-prone nanopore sequencing reads with
GraphMap.

* URL: http://biorxiv.org/content/early/2015/06/10/020719
* Hough transform: https://en.wikipedia.org/wiki/Hough_transform

Relevant background:

* `Gapped k-mer filters <https://www.cs.helsinki.fi/u/tpkarkka/publications/cpm02.pdf>`__


Summary
-------

This paper presents a new read mapper, GraphMap.

The method is described as a five-stage read funneling approach, which
successively reduces the number and complexity of the decisions that
need to be made

Stage 1: Region selection
#########################

Gapped spaced seeds are not the same as our `last journal club
<http://ivory.idyll.org/blog/2015-jclub-spaced-seeds.html>`__, but
it's an interesting strategy for selecting seeds to extend alignments.

Based on `Levenshtein distance
<https://en.wikipedia.org/wiki/Levenshtein_distance>`__, it uses gaps
inside k-mers to consider mismatches and indels.  Three shapes are
used, with one or two positions being DC ("don't care") bases:

- 1110111: DC base can be either a match or mismatch
- 111111: one deletion at the specified position (?)
- 11100111: DC base and following base are skipped.
  At most one insertion and one match/mismatch.

(Can we use longer shapes?
These one are for fairly small _k_,
if we can extend the idea to arbitrary _k_ it might be useful for seeding on graphalign).

Hough transforms are used in a clever way to bin seeds into viable regions,
but it depends on reference coordinates (so it is not so useful for us
in the absence of a decent reference).

Stage 2: Graph-based vertex-centric construction of anchors
###########################################################

The 'graph' part of GraphMap comes from the next step,
where the seeds are processed to construct alignment anchors.
Given a target and a query,
a "kmer mapping graph" (a DAG) is built for the target.
In a "kmer mapping graph" distinct nodes can represent the same k-mer.
For example,
the first step in constructing a 2-mer mapping graph for *CTAATATC* would be
CT -> TA -> AA -> AT -> TA -> AT -> TC
(note nodes TA, AT appearing twice).
Then, for each vertex an edge is added for every successor until the last node is reached.

These graphs are small,
since target and query are a read sequence and a single region of the reference
(for memory consumption purposes,
read sequence are usually smaller and so used as target).
A new index is constructed for the target on the fly,
with a much smaller seed size (defaults to k=6).
For k < 10 perfect hashing is used,
for k >= 10 a suffix array.

After the graph is ready,
the mapping works by walking along target and query simultaneously.
The query is processed as a sliding window,
and an edge is followed to extend the walk each step in the target,
while keeping track of all walks corresponding to potential mapping sites.

There are similarities to how `partial order alignment
<https://simpsonlab.github.io/2015/05/01/understanding-poa/>`__ works,
but how is this stage any different than just doing DP?

Stage 3: Extending anchors into alignments using LCS
####################################################

(nothing here)

Stage 4: Refining alignments using $L_1$ linear regression / Stage 5: Construction of final alignment
#####################################################################################################

Just summary of stages 4 and 5: After we have extended anchors in
stage 3, we will have a set of points representing the alignments from
LCSK, mixed with a set of noise; (indels, sequence errors, etc). To
refine these alignments, we need to draw a line that best fits these
points. This is done by using linear regression, which is used to fit
the alignment's "predictive model" from among these observed points
"list of anchors".

The points that lie on given dl1 from either sides of the line,
represents our best alignments - those points who deviates should
be discarded.

Then the std deviation of anchors from this line, no. of exact kmers
covered by anchors around the line, length of query that matched the
target, no. of bases covered by anchors (normalized) and the read
length are used to compute an f score.  The region with highest f
score are picked for final alignment.

(I think the reference coordinates c can be estimated from the position on the read and the position of the hit, so we still can use Hough Transform?)

Stages 4 and 5 seem heavyweight.

----

Questions and comments:

* we are unclear on how index would be constructed in the absence of a
  reference in the case of a de novo assembly. Last paragraph of
  Discussion states: "GraphMap’s sensitivity and specificity as a
  mapper could thus serve as the basis for fast computation of overlap
  alignments and de novo assemblies in the future." But algorithm from
  Figure 1b and Methods Stage I: region selection seems to be based on
  seed finding between query and reference. What is used as reference
  in the absence of a reference?

* GraphMap showed improved runtime (Suppl Table 2) compared to "gold
  standard" BLAST alignment. In Figure 2 with synthetic data, data
  platform type made the biggest difference in GraphMap performance
  compared to "gold-standard" BLAST aligner. Oxford Nanopore 2D data
  (double-stranded) had consistently among the highest precision
  relative to other platforms, although PacBio was close behind in
  both C. elegans and H. sapiens sets. Interesting that genome size
  (from 2.2 Mbp = N. meningitidis to 198 Mbp = H. sapiens ch3) didn't
  make much difference in precision (mapped location on read; seed
  hit, k-point) or recall (alignment)
  (https://en.wikipedia.org/wiki/Precision_and_recall). Recall was
  much lower in all ONT data regardless of species.

* Impressed with figure 3a, difference between GraphMap and LAST
  mapping tool with difference in consensus sequences (colored = low
  confidence, grey = higher confidence). Would liked to have seen
  their BWA-MEM and BLASR results, although Figure 3b suggests LAST
  was closer to GraphMap with higher coverage.

* Interesting applications outline in Results. Benefit of GraphMap to
  reduce pipeline resources required for ONP data? Mick Watson
  suggests BLAST
  (https://biomickwatson.wordpress.com/2015/06/01/analysing-minion-data-with-no-bioinformatics-expertise-nor-infrastructure/).

* Reasons for why we care include new ONP technology in field
  applications, e.g. identifying pathogens in remote location with
  local install. Species predictions in Table 3, F1 (mean of precision
  and recall) higher for GraphMap. Need for more testing with real ONP
  data (just 3 species were tested in this paper) and with higher
  complexity, e.g. pathogenic microbial eukaryotes?

* We were a bit surprised that longest-common-subsequence works so
  well with ONT, but that's why they did it with only the subsequences
  extracted after the graph approach.

* "Our comparisons with BLAST suggest that reads that cannot be mapped
  by GraphMap may essentially be unmappable." Did they characterize
  these reads at all?

* What's the memory usage? Largely or entirely unmentioned.

* We were confused by the gapped qspaced seeds/gapped q-gram filter
  stuff. (p10)

* We do not think they tested for genome scaling appropriately. They
  need to show an example for may be a whole human genome. As Lisa
  noticed there is no change in precision with their bigger genomes.

* The clinical application is very interesting. They did not compare
  precision of other mappers using strain specific sequence.
 
