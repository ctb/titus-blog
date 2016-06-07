Graph alignment and variant calling
###################################

:authors: \C. Titus Brown, Michael R. Crusoe, Jordan Fish, Jason Pell.
:tags: khmer,wok,graphalign,variants
:date: 2015-05-19
:slug: 2015-wok-variant-calling
:category: science

There's an interesting and intuitive connection between `error
correction
<http://ivory.idyll.org/blog/2015-wok-error-correction.html>`__ and
variant calling - if you can do one well, it lets you do (parts of)
the other well.  In `the previous blog post
<http://ivory.idyll.org/blog/2015-wok-error-correction.html>`__ on
some new features in khmer, we introduced our new "graphalign"
functionality, that lets us align short sequences to De Bruijn graphs,
and we discussed how we use it for error correction.  Now, let's try
it out for some simple variant calling!

Graphalign can potentially be used for variant calling in a few
different ways - by mapping reads to the reference graph and then
using a pileup approach, or by error correcting reads against the
graph with a tunable threshold for errors and then looking to see
where all the reads disagree - but I've become enamored of an approach
based on the concept of reference-guided assembly.

The essential idea is to build a graph that contains the information
in the reads, and then "assemble" a path through the graph using a
reference sequence as a guide.  This has the advantage of looking at
the reads only once (to build a DBG, which can be done in a single
pass), and also potentially being amenable to a variety of heuristics.
(Like almost all variant calling, it *is* limited by the quality of
the reference, although we think there are probably some ways around
that.)

Basic graph-based variant calling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Implementing this took a little bit of extra effort beyond the basic
read aligner, because we want to align past gaps in the graph.  The
way we implemented this was to break the reference up into a bunch of
local alignments, each aligned independently, then stitched together.

Again, we tried to keep the API simple. After creating a ReadAligner object, ::

    aligner = khmer.ReadAligner(graph, trusted_cutoff, bits_theta)

there's a single function that takes in the graph and the sequence (potentially
genome/chr sized) to align::

    score, alignment = align_long(graph, aligner, sequence)

What is returned is a score and an alignment object that gives us access
to the raw alignment, some basic stats, and "variant calling" functionality -
essentially, reporting of where the alignments are not identical.  This is
pretty simple to implement::

     for n, (a, b) in enumerate(zip(graph_alignment, read_alignment)):
         if a != b:
            yield n, a, b

The current implementation of the variant caller does nothing beyond
reporting where an aligned sequence differs from the graph; this is
kind of like guided assembly. In the future, the plan is to extend it
with reference-free assembly.

To see this in action for a simulated data set, look at the file
`sim.align.out
<https://github.com/ctb/2015-khmer-wok2-vc/blob/master/sim.align.out>`__
-- we get alignments like this, highlighting mismatches::

   ATTTTGTAAGTGCTCTATCCGTTGTAGGAAGTGAAAGATGACGTTGCGGCCGTCGCTGTT
   |||||||||||||||||||| |||||||||||||||||||||||||||||||||||||||
   ATTTTGTAAGTGCTCTATCCCTTGTAGGAAGTGAAAGATGACGTTGCGGCCGTCGCTGTT

(Note that the full alignment shows there's a bug in the read aligner
at the ends of graphs. :)

It works OK for whole-genome bacterial stuff, too.  If we take an
E. coli data set (the same one we used `in the semi-streaming paper
<https://peerj.com/preprints/890/>`__) and just run the reads against
the known reference genome, we'll get 74 differences between the graph
and the reference genome, out of 4639680 positions -- an identity of
99.998% (`variants-ecoli.txt
<https://github.com/ctb/2015-khmer-wok2-vc/blob/master/variants-ecoli.txt>`__).
On the one hand, this is not that great (consider that for something
the size of the human genome, with this error rate we'd be seeing
50,000 false positives!); on the other hand, as with error correction,
the whole analysis stack is surprisingly simple, and we haven't spent
any time tuning it yet.

Simulated variants, and targeted variant calling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With simulated variants in the E. coli genome, it does pretty well.
Here, rather than changing up the genome and generating synthetic
reads, we went with the same real reads as before, and instead changed
the reference genome we are aligning to the reads.  This was done with
the `patch-ecoli.py script
<https://github.com/ctb/2015-khmer-wok2-vc/blob/master/patch-ecoli.py>`__,
which changes an A to a C at position 500,000, removes two bases at
position 2m, and adds two bases at position 3m.

When we align the "patched" E. coli genome against the read graph, we
indeed recover all three alignments (see `variants-patched.txt
<https://github.com/ctb/2015-khmer-wok2-vc/blob/master/variants-patched.txt>`__)
in the background of the same false positives we saw in the unaltered
genome.  So that's kind of nice.

What's even neater is that we can do *targeted* variant calling
directly against the graph -- suppose, for example, that we're
interested in just a few regions of the reference.  With the normal
mapping-based variant calling, you need to map all the reads first
before querying for variants by location, because mapping requires the
use of the entire reference.  Here, you are already looking at all the
reads in the graph form, so you can query just the regions you're
interested in.

So, for example, here you can align just the patched regions (in
ecoli-patched-segments.fa) against the read graph and get the same
answer you got when aligning the entire reference (target
`ecoli-patched-segments.align.out
<https://github.com/ctb/2015-khmer-wok2-vc/blob/master/ecoli-patched-segments.align.out>`__).
This works in part because we're stitching together local alignments,
so there are some caveats in cases where different overlapping query
sequences might lead to different optimal alignments - further
research needed.

Speed considerations
~~~~~~~~~~~~~~~~~~~~

Once you've created the graph (which is linear time with respect to
the number of reads), things are pretty fast.  For the E. coli data
set, it takes about 25 seconds to do a full reference-to-graph
alignment on my Mac laptop.  Much of the code is still written in
Python so we hope to get this under 5 seconds.

In the future, we expect to get much faster.  Since the alignment is
guided and piecewise, it should be capable of aligning through highly
repetitive repeats and is also massively parallelizable. We think that
the main bottleneck is going to be loading in the reads.  We're
working on optimizing the loading separately, but we're hoping to get
down to about 8 hours for a full ~50x human genome variant calling
with this method on a single CPU.

Memory considerations
~~~~~~~~~~~~~~~~~~~~~

The memory is dominated by graph size, which in turn is dominated by
the errors in short-read Illumina data.  We have `efficient ways of
trimming some of these errors <https://peerj.com/preprints/890/>`__,
and/or compressing down the data, even if we don't just correct them;
the right approach will depend on details of the data (haploid?
diploid? polyploid?) and will have to be studied.

For E. coli, we do the above variant calling in under 400 MB of RAM.
We should be able to get that down to under 100 MB of RAM easily
enough, but we will have to look into exactly what happens as we
compress our graph down.

From the `Minia paper <http://minia.genouest.org/>`__, we can place
some expectations on the memory usage for diploid human genome
assembly.  (We don't use *cascading* Bloom filters, but our approaches
are approximately equivalent.)  We believe we can get down to under 10
GB of RAM here.

Additional thoughts
~~~~~~~~~~~~~~~~~~~

As with most of our methods, this approach should work directly for
variant calling on RNAseq and metagenomic data with little alteration.
We have a variety of graph preparation methods (straight-up graph
loading as well as digital normalization and `abundance slicing
<http://khmer-recipes.readthedocs.org/en/latest/001-extract-reads-by-coverage/index.html>`__)
that can be applied to align to everything while favoring
high-coverage reads, or only to high coverage, or to error-trimmed
reads, or...

In effect, what we're doing is (rather boring) reference-guided
assembly.  Wouldn't it be nice if we extended it to longer indels, as
in `Holtgrewe et al., 2015
<http://www.ncbi.nlm.nih.gov/pubmed/25649620>`__?  Yes, it would. Then
we could ask for an assembly to be done between two points...  This
would enable the kinds of approaches that (e.g.) `Rimmer et al., 2014
<http://www.nature.com/ng/journal/v46/n8/full/ng.3036.html>`__
describe.

One big problem with this approach is that we're only returning
positions in the reference where the graph has *no* agreement - this
will cause problems when querying diploid data sets with a single
reference, where we really want to know *all* variants, including
heterozygous ones where the reference contains one of the two.  We can
think of several approaches to resolving this, but haven't implemented
them yet.

A related drawback of this approach so far is that we have (so far)
presented no way of representing multiple data sets in the same graph;
this means that you can't align to many different data sets all at
once.  You also can't take advantage of things like the contiguity
granted by long reads in many useful ways, nor can you do haplotyping
with the long reads. Stay tuned...

References and previous work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A number of people have done previous work on graph-based variant calling --

* Zam Iqbal and Mario Caccamo's `Cortex
  <http://cortexassembler.sourceforge.net/>`__ is the first article
  that introduced me to this area.  Since then, Zam's work as well as
  some of the work that Jared Simpson is doing on FM indices has been
  a source of inspiration.

  (See especially `Zam's very nice comment
  <http://ivory.idyll.org/blog/2015-wok-error-correction.html#comment-2033226348>`__
  on our error correction post!)

* Heng Li's `FermiKit <http://arxiv.org/abs/1504.06574>`__ does
  something very similar to what we're proposing to do, although it
  seems like he effectively does an assembly before calling variants.
  This has some positives and some negatives that we'll have to
  explore.

* `Kimura and Koike (2015)
  <http://bioinformatics.oxfordjournals.org/content/early/2015/01/19/bioinformatics.btv024.short>`__
  do variant calling on a Burrows- Wheeler transform of short-read
  data, which is very similar to what we're doing.

* Using k-mers to find variation is nothing new.  Two articles that
  caught my eye -- `BreaKmer (Abo et al, 2015)
  <http://www.ncbi.nlm.nih.gov/pubmed/25428359>`__ and `kSNP3 (Gardner
  et al., 2015)
  <http://bioinformatics.oxfordjournals.org/content/early/2015/04/25/bioinformatics.btv271.abstract>`__
  both do this to great effect.

* the GA4GH is working on graph-based variant calling, primarily for
  human.  So far it seems like they are planning to rely on well
  curated genomes and variants; I'm going to be working with (much)
  poorer quality genomes, which may account for some differences in
  how we're thinking about things.

Appendix: Running this code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The computational results in this blog post are Rather Reproducible
(TM).  Please see
https://github.com/dib-lab/2015-khmer-wok2-vc/blob/master/README.rst
for instructions on replicating the results on a virtual machine or
using a Docker container.
