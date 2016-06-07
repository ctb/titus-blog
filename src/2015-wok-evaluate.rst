Comparing and evaluating assembly with graph alignment
######################################################

:authors: \C. Titus Brown, Camille Scott, Michael R. Crusoe
:tags: khmer,wok,graphalign,evaluation
:date: 2015-05-22
:slug: 2015-wok-evaluate
:category: science

One of our long-term interests has been in figuring out what the
!$!$!#!#%!  assemblers actually do to real data, given all their
heuristics.  A continuing challenge in this space is that short-read
assemblers deal with *really* large amounts of noisy data, and it can
be extremely hard to look at assembly results without running into
this noise head-on.  It turns out that `being able to label De Bruijn
graphs efficiently
<http://ivory.idyll.org/blog/2015-wok-labelhash.html>`__ and `align
reads to graphs
<http://ivory.idyll.org/blog/2015-wok-error-correction.html>`__ can
help us explore assemblies in a variety of ways.

The two basic challenges are *noisy data* and *lots of data*.  When
(for example) looking at what fraction of reads has been incorporated
into an assembly, noise causes problems because a read may have been
corrected during assembly.  This is where graph alignment comes in
handy, because we can use it to align reads to the full graph and get
rid of much of this noise.  Lots of data complicates things because
it's very hard to look at reads individually - you need to treat them
in aggregate, and it's much easier just to look at the reads that
match to your assembly than to investigate the oddball reads that
don't assemble.  And this is where the combination of graph alignment
and labeling helps, because it's easy to count and extract reads based
on overlaps with labels, as well as to summarize those overlaps.

The main question we will be asking below is: can we measure overlaps
and disjoint components in *graph extents*, that is, in unique
portions of assembly graphs?  We will be doing this using our `sparse
graph <http://ivory.idyll.org/blog/2015-wok-labelhash.html>`__ instead
of counting nodes or k-mers, for two reasons: first, the covering is
largely independent of *coverage*, and second, the number of sparse
nodes is a lot smaller than the total number of k-mers.

The underlying approach is straightforward:

* load contigs or reads from A into the graph, tagging sparse nodes as we go;
* load contigs or reads from B into the graph, tagging sparse nodes as we go;
* count the number of tagged nodes that are unique to A, unique to B, and
  in the overlap;
* optionally do graph alignment as you load in reads, to ignore errors.

Some basics
-----------

Let's start with simulations, as usual.  We'll set up two randomly
generated chromosomes, a and b, of equal size, both in ``genomes.fa``,
and look at ``genome-a`` extent within the context of both (target
'fake_a' in `Makefile
<https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/Makefile>`__)::

   ./compare-graphs.py genomes.fa genome-b.fa
   all tags: 52
   n tags in A: 52
   n tags in B: 26
   tags in A but not in B 26
   tags in B but not in A 0

So far so good -- there's a 50% overlap between one of the chromosomes
and the total.

If we now generate reads from genome-b.fa and do the graph comparison
with the reads, we get silly results (target 'fake_b' in `Makefile
<https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/Makefile>`__)::

   ./compare-graphs.py genomes.fa reads-b.fa
   all tags: 135
   n tags in A: 109
   n tags in B: 107
   tags in A but not in B 28
   tags in B but not in A 26

Despite *knowing* by construction that all of the reads came from
genome-b, we're getting results that there's a lot of tags in the
reads that aren't in the genome.  This is because of errors in the
reads, which introduce many spurious branches in the graph.

This is now where the read aligner comes in; we can do the same
comparison, but this time we can ask that the reads be aligned to the
genome, thus eliminating most of the errors in the comparison::

   ./compare-graphs.py genomes.fa reads-b.fa --align-b
   all tags: 99
   n tags in A: 99
   n tags in B: 72
   tags in A but not in B 27
   tags in B but not in A 0

At this point we can go in and look at the original tags in A that aren't
covered in B (there are 52) and note that B is missing approximately half
of the graph extent in A.

Trying it out on some real data
-------------------------------

Let's try evaluating a reference against some low-coverage reads.
Using the same mouse reference transcriptome & subset of reads that
we've been using `in previous blog posts
<http://ivory.idyll.org/blog/2015-wok-labelhash.html>`__, we can ask
"how many sparse nodes are unaccounted for in the mouse transcriptome
when we look at the reads?"  (Note, the mouse transcriptome was not
generated from this data set; this is the reference transcriptome.)

The answer (target `rna-compare-noalign.txt
<https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/rna-compare-noalign.txt>`__
in the `Makefile
<https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/Makefile>`__)
is::

   all tags: 1959121
   n tags in A: 1878475
   n tags in B: 644963
   tags in A but not in B 1314158
   tags in B but not in A 80646

About 12.5% of the reads in (B; 80646 / 644963) don't pick up tags in
the official reference transcriptome (A).

Interestingly, the results with alignment are essentially the same
(target `rna-compare-align.txt <https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/rna-compare-align.txt>`__)::

   all tags: 1958219
   n tags in A: 1877685
   n tags in B: 643655
   tags in A but not in B 1314564
   tags in B but not in A 80534

suggesting that, by and large, these reads are disjoint from the
existing assembly, and not mere sequencing errors.  (This may be
because we require that the entire read be mappable to the graph in
order to count it, though.)

Evaluating trimming
-------------------

One of the interesting questions that's somewhat hard to investigate
in terms of transcriptome assembly is, `how beneficial is read
trimming to the assembly?
<http://genomebio.org/is-trimming-is-beneficial-in-rna-seq/>`__ The
intuition here (that I agree with) is that generally sequence trimming
lowers the effective coverage for assembly, and hence loses you
assembled sequence.  Typically this is measured by running an
assembler against the reads, which is slightly problematic because the
assembler could have all sorts of strange interactions with the
trimming.

So, can we look at the effect of trimming in terms of sparse nodes?
Sure!

Suppose we do a stringent round of trimming on our RNAseq (Trimmomatic
SLIDINGWINDOW:4:30) - what do we lose?

On this low coverage data set, where A is the graph formed from the
trimmed reads and B is the graph from the raw reads, we see (target
`rseq-hardtrim-ba-noalign.txt
<https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/rseq-hardtrim-ba-noalign.txt>`__)::

   all tags: 588615
   n tags in A: 518980
   n tags in B: 588615
   tags in A but not in B 0
   tags in B but not in A 69635

we see about 12% of the sparse nodes missing from the trimmed data.

If we run the read aligner with a low coverage cutoff (target
`rseq-hardtrim-ba-align1.txt
<https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/rseq-hardtrim-ba-align1.txt>`__),
we see::

   all tags: 569280
   n tags in A: 519396
   n tags in B: 561757
   tags in A but not in B 7523
   tags in B but not in A 49884

Basically, we recover about 20,000 tags in B (69,635 - 49,884) with
alignment vs exact matches, so a few percent; but we also lose about
half that (7,500) for reasons that we don't entirely understand
(wiggle in the graph aligner?)

We have no firm conclusions here, except to say that this should be a
way to evaluate the effect of different trimming on graph extent, which
*should* be more reliable than looking at the effect on assemblies.

Notes and miscellany
--------------------

* There is no inherent coverage model embedded here, so as long as we can
  correct for the density of tags, we can apply these approaches to
  genomes, metagenomes, and transcriptomes.

* It's actually very easy to extract the reads that do or don't match,
  but our current scripts don't let us do so based on labels.

* We aren't really using the labeling here, just the tagging - but
  labeling can enable n-way comparisons between e.g. different
  assemblies and different treatments, because it lets us examine
  which tags show up in different combinations of data sets.

Appendix: Running this code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The computational results in this blog post are Rather Reproducible
(TM).  Please see
https://github.com/dib-lab/2015-khmer-wok5-eval/blob/master/README.rst
for instructions on replicating the results on a virtual machine or
using a Docker container.
