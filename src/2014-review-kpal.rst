My review of "Determining the quality and complexity of NGS..."
###############################################################

:author: C\. Titus Brown
:tags: reviews, k-mers, ngs
:date: 2014-12-18
:slug: 2014-review-kpal
:category: science

I was a reviewer on `Determining the quality and complexity of
next-generation sequencing data without a reference genome <http://www.ncbi.nlm.nih.gov/pubmed/25514851>`__ by
Anvar et al., `PDF here
<http://genomebiology.com/content/pdf/s13059-014-0555-3.pdf>`__.
Here is the top bit of my review.

One interesting side note - the authors originally named their tool
`kMer <https://pypi.python.org/simple/kmer/>`__ and I complained about
it in my review.  And they renamed it to `kPal
<https://pypi.python.org/simple/kpal/>`__!  Which is much less confusing.

----


The authors show that a specific set of low-k k-mer profile analysis
tools can identify biases and errors in sequencing samples as well as
determine sample distances between metagenomic samples.  All of this
is done *independently* of reference genomes/transcriptomes, which is
very important.

The paper is well written and quite clear.  I found it easy to read
and easy to understand.  The work is also novel, I believe.

Highlights of the paper for me included a solid discussion of k-mer
size selection, a thorough exploration of how to compare various
k-mer-based statistics, the excellent quality evaluation bit (Figure 3),

I was a bit surprised by the shift from quality assessment to metagenomic
analysis, but there is an underlying continuity in the approach that makes
this a reasonable transition.  There might be a way to update the text to
make this transition easier for the non-bioinformatic reader.

It's hard to pick out one particularly important result; the two
biggest results are (a) k-mer based and reference free quality
evaluation works quite well, and (b) k-mer analysis does a great job
of grouping metagenome samples.  The theory work on transitioning
between k-mer sizes is potentially of great technical interest as well.
