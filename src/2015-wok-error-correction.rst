Read-to-graph alignment and error correction
############################################

:author: Jordan Fish, Jason Pell, Michael R. Crusoe, and C\. Titus Brown
:tags: khmer,wok,graphalign,errcorr
:date: 2015-05-18
:slug: 2015-wok-error-correction
:category: science

One of the newer features in khmer that we're pretty excited about is
the read-to-graph aligner, which gives us a way to align sequences to
a De Bruijn graph; our nickname for it is "graphalign."

Briefly, graphalign uses a pair-HMM to align a sequence to a k-mer
graph (aka De Bruijn graph) allowing both mismatches and indels, and
taking into account coverage using a binary model (trusted and
untrusted k-mers).  The core code was written by Jordan Fish when he
was a graduate student in the lab, based on ideas stemming from Jason
Pell's thesis work on error correction.  It was then refactored by
Michael Crusoe.

Graphalign actually lets us do lots of things, including align both
short and long sequences to DBG graphs, error correct, and call
variants.  We've got a simple Python API built into khmer, and we're
working to extend it.

----

The core graphalign API is based around the concept of a ReadAligner object::

    aligner = khmer.ReadAligner(graph, trusted_cov, bits_theta)

where 'graph' is a De Bruijn graph (implemented as a counting table in
khmer), 'trusted_cov' defines what the trusted k-mer coverage is, and
'bits_theta' adjusts a scoring parameter used to extend alignments.

The 'aligner' object can be used to align short sequences to the graph::

     score, graph_alignment, read_alignment, truncated = \
         aligner.align(read)

Here, 'graph_alignment' and 'read_alignment' are strings; if
'truncated' is false, then they are of the same length, and constitute
a full gapped alignment of the DNA sequence in 'read' to the graph.

The approach used by 'align' is to seed an alignment at the first trusted
k-mer, and then extend the alignment along the graph in both directions.
Thus, it's effectively a local aligner.

Error correction
~~~~~~~~~~~~~~~~

Our initial motivation for graphalign was to use it to do error
correction, with specific application to short-read sequences.  There
was (and to some extent still is) a dearth of error correction
approaches that can be used for metagenome and transcriptome data
sets, and since that kind of data is what our lab works on, we needed
an error correction approach for those data.  We also wanted something
a bit more programmable than the existing error correctors, which were
primarily command-line tools; we've found a lot of value in building
libraries, and wanted to use that approach here, too.

The basic idea is this: we build a graph from our short-read data,
and then go back through and align each short read to the graph.  A
successful alignment is then the corrected read.  The basic code looks
like this::

    graph = build_graph(dataset)

    aligner = khmer.ReadAligner(graph, trusted_cov, bits_theta)

    for read in dataset:
        score, graph_align, read_align, is_truncated = aligner.align(read)
        corrected_read = graph_align

In conjunction with `our work on semi-streaming algorithms
<https://peerj.com/preprints/890/>`__, we can directly convert this
into a semi-streaming algorithm that works on genomes, metagenomes,
and transcriptomes.  This is implemented in the `correct-reads script
<https://github.com/dib-lab/khmer/blob/2015-wok/sandbox/correct-reads.py>`__.

Some results
~~~~~~~~~~~~

If we try this out on a simulated data set (random genome, randomly
chosen reads - see target ``compare-sim.txt`` in `Makefile
<https://github.com/dib-lab/2015-khmer-wok1-ec/blob/master/Makefile>`__),
it takes the simulated data from an error rate of around 1% to about
0.1%; see `compare-sim.txt
<https://github.com/dib-lab/2015-khmer-wok1-ec/blob/master/compare-sim.txt>`__.

Applying this to a ~7m read subset of mRNAseq that we tackled in the
semi-streaming paper (the data itself is from the `Trinity paper,
Grabherr et al, 2011
<http://www.ncbi.nlm.nih.gov/pubmed/21572440>`__), we take the data
from an error rate of about 1.59% to 0.98% (see target
``rseq-compare.txt`` in `Makefile
<https://github.com/dib-lab/2015-khmer-wok1-ec/blob/master/Makefile>`__).
There are several reasons why this misses so many errors - first,
error correction depends on high coverage, and much of this RNAseq
data set is low coverage; second, this data set has a lot of errors;
and third, RNAseq may have a broader k-mer abundance distribution than
genomic sequencing.

One important side note: we use exactly the same script for error
correcting RNAseq data as we do for genomic data.

How good is the error correction?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tl; dr? It's pretty good but still worse than current methods.  When
we compare to Quake results on an E. coli data set (target
`compare-ecoli.txt
<https://github.com/dib-lab/2015-khmer-wok1-ec/blob/master/compare-ecoli.txt>`__
in `the Makefile
<https://github.com/dib-lab/2015-khmer-wok1-ec/blob/master/Makefile>`__),
we see:

============  ==========
Data set      Error rate
============  ==========
Uncorrected   1.587%
Quake         0.009%
khmer         0.013%
============  ==========

This isn't too bad - two orders of magnitude decrease in error rate! -
but we'd like to at least be able to beat Quake :).

(Note that here we do a fair comparison by looking only at errors on
sequences that Quake doesn't discard; to get comparable results on
your data with khmer, you'd also have to trim your reads.  We are also
making use of the approach developed in the streaming paper where we
digitally normalize the graph in advance, in order to decrease the
number of errors and the size of the graph.)

Concluding thoughts
~~~~~~~~~~~~~~~~~~~

What attracts us to this approach is that it's really *simple*.  The
basic error correction is `a few lines
<https://github.com/dib-lab/khmer/blob/2015-wok/sandbox/correct-reads.py#L39>`__,
although it's surrounded by a bunch of machinery for doing
semi-streaming analysis and keeping pairing intact.  (The
`two-pass/offline script for error correction
<https://github.com/dib-lab/khmer/blob/2015-wok/sandbox/error-correct-pass2.py>`__
is much cleaner, because it omits all of this machinery.)

It's also nice that this applies to all shotgun sequencing, not just
genomic; that's a trivial extension of `our semi-streaming paper
<https://peerj.com/preprints/890/>`__.

We also suspect that this approach is quite tunable, although we are just
beginning to investigate the proper way to build parameters for the
pair-HMM, and we haven't nailed down the right coverage/cutoff parameters
for error correction either.  More work to be done!

In any case, there's also more than error correction to be done with
the graphalign approach -- stay tuned!

References and previous work
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is by no means novel - we're building on a lot of ideas from a
lot of people.  Our interest is in bridging from theory to practice,
and providing a decent tunable implementation in an open-source
package, so that we can explore these ideas more widely.

Here is short summary of previous work, surely incomplete --

* Much of this was proximally inspired by Jordan's work on `Xander
  <https://github.com/rdpstaff/Xander-HMMgs>`__, software to do
  HMM-guided gene assembly from metagenomic data.  (An accompanying
  paper has been accepted for publication; will blog about that when
  it hits.)

* More generally, my MSU colleague `Yanni Sun
  <https://sites.google.com/site/yannisun/>`__ has had several PhD
  students that have worked on HMMs and graph alignment, and she and
  her students have been great sources of ideas!  (She co-advised
  Jordan.)

* `BlastGraph <http://alcovna.genouest.org/blastgraph/>`__, like
  Xander, built on the idea of graph alignment.  It is the earliest
  reference I know of to graph alignment, but I haven't looked very hard.

* `Yuzhen Ye <http://mendel.informatics.indiana.edu/~yye/lab/>`__ and
  `Haixu Tang <http://www.informatics.indiana.edu/hatang/>`__ at
  Indiana have developed very similar functionality that I became
  aware of when reviewing `their nice paper on graph alignment for
  metatranscriptomics
  <https://scholar.google.com/citations?view_op=view_citation&hl=en&user=4Hywr5UAAAAJ&sortby=pubdate&citation_for_view=4Hywr5UAAAAJ:LI9QrySNdTsC>`__.

* Jared Simpson has been `doing nice work
  <http://simpsonlab.github.io/2015/04/08/eventalign/>`__ on aligning
  Nanopore reads to a reference sequence.  My guess is that the
  multiple sequence alignment approach described in `Jonathan Dursi's
  blog post
  <http://simpsonlab.github.io/2015/05/01/understanding-poa/>`__ is
  going to prove relevant to us.

* The error corrector Coral `(Salmela and Schroder, 2011)
  <http://www.ncbi.nlm.nih.gov/pubmed/21471014>`__ bears a strong
  philosophical resemblance to graphalign in its approach to error
  correction, if you think of a De Bruijn graph as a kind of
  multiple-sequence alignment.

If you know of more, please add references below, in the comments -
much appreciated!

Appendix: Running this code
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The computational results in this blog post are Rather Reproducible
(TM).  Please see
https://github.com/dib-lab/2015-khmer-wok1-ec/blob/master/README.rst
for instructions on replicating the results on a virtual machine or
using a Docker container.
