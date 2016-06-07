A review of "Large-Scale Search of Transcriptomic Read Sets with Sequence Bloom Trees"
######################################################################################

:authors: C\. Titus Brown, Luiz Irber, Qingpeng Zhang
:tags: Bloom filters,reviews
:date: 2015-06-25
:slug: 2015-review-bloomtree
:category: science

(This is a review of `Large-Scale Search of Transcriptomic Read Sets
with Sequence Bloom Trees
<http://biorxiv.org/content/early/2015/03/26/017087>`__, Solomon and
Kingsford, 2015.)

In this paper, Solomon and Kingsford present Sequence Bloom Trees (SBTs).
SBT provides an efficient method for indexing multiple sequencing
datasets and finding in which datasets a query sequence is present.

The new method is based on using multiple Bloom filters and organizing
them in a binary tree, where leaves represent specific datasets and
internal nodes contain all the k-mers present in their subtrees.  A
query starts by breaking the sequence into a set of k-mers and
checking if they are present in the node Bloom filter at a specific
threshold. If yes then the query is repeated for children nodes, but
if it isn't the subtree is pruned and search proceeds on other
nodes. If all searches are pruned before reaching a leaf then the
sequence is not present in any dataset.  They prove the false positive
rate for a k-mer can be quite higher than traditional applications of
Bloom filters, since they are interested in finding if the whole set
of k-mers is over a threshold. This leads to very small data
structures that remain capable of approximating the correct answer.

Compared to alternative software (like SRA-BLAST or STAR) it has both
decreased runtime and memory consumption, and it also can be used as a
filter to make these tools faster.

Overall review
--------------

The paper is well written, clear, mostly expert in the area (but see below),
and lays out the approach and tool well.

The approach is novel within bioinformatics, as far as we know.  More,
we think it's a tremendously important approach; it's by far the most
succinct representation of large data sets we've seen (and Bloom
filters are notoriously efficient), and it permits efficient indexing,
storage of indices, and queries of indices.

A strange omission is the work that has been done by our group and
others with Bloom filters.  Pell et al., 2012 (`pmid 22847406 <http://www.ncbi.nlm.nih.gov/pubmed/22847406>`__), showed
that implicit De Bruijn graphs could be stored in Bloom filters in
exactly the way the authors are doing here; work by Chikhi and Rizk,
2013 (`pmid 24040893 <http://www.ncbi.nlm.nih.gov/pubmed/24040893>`__) implemented exact De Bruijn graphs efficiently
using Bloom filters; and Salikhov et al, 2014 (`pmid 24565280 <http://www.ncbi.nlm.nih.gov/pubmed/24565280>`__) further
used Cascading Bloom filters.  Our group has also used the median
k-mer abundance (which, in a Bloom filter, equals median k-mer
presence) to estimate read presence and coverage in a very similar way
to Solomon and Kingsford (Brown et al., 2012, "digital
normalization"). We also showed experimentally that this is very
robust to high false positive rates (Zhang et al., 2014, `pmid
25062443 <http://www.ncbi.nlm.nih.gov/pubmed/25062443>`__, buried in the back).

There are three points to make here --

1. Previous work has been done connecting Bloom filters and k-mer storage,
   in ways that seem to be ignored by this paper; the authors should
   cite some of this literature.  Given citation space limitations,
   this doesn't need to be exhaustive, but either Salikhov or Pell seems
   particularly relevant.

2. The connection between Bloom filters and implicit De Bruijn graphs
   should be explicitly made in the paper, as it's a powerful theoretical
   connection.

3. All of our previous result support the conclusions reached in this paper,
   and this paper makes the false-positive robustness argument much more
   strongly, which is a nice conclusion!

---

We have found that users are often very confused about how to pick the
size of Bloom filters.  My sense here is that the RRR compression
means that very large Bloom filters will be stored efficiently, so you
might as well start big, because there's no way to do progressive size
increases on the Bloom filter; do the authors agree with that
conclusion, or am I missing something?

One possible writing improvement is to add another level under the
leaves in Supp Fig 1 to make it clear that traditional alignment or
other alternatives are required, since SBT only finds if the query is
present in the dataset (but not where).  The speed comparisons in the
paper could be qualified a bit more to make it clear that this is only
for basic search, although some of us think it's already clear enough
so it's advice, not a requested or required change.

However, there is a solid point to be made that (in our opinion) the
true value of the SBT approach is not necessarily in speeding up the
overall process (3.5x speedup) but in doing the search in very low
memory across an index that can be distributed independently of the
data.

page 16, Theorem 2 says the probability that ... is nearly 0 when FPR
is << theta, fraction threshold.  But next in the example, theta is
0.5 and FPR is also 0.5, so here the FPR is NOT << theta, as in
Theorem 2.  How to conclude that "by Theorem 2, we will be unlikely to
observe > theta fraction of false positive kmers in the filter."?

Software and tool publication
-----------------------------

Bioinformatics paper checklist (http://ivory.idyll.org/blog/blog-review-criteria-for-bioinfo.html):

The software is directly available for download:
Yes, https://github.com/Kingsford-Group/bloomtree

The software license lets readers download and run it:
The license is not specified; this needs to be fixed.  But 'bloomtree'
makes use of several GPL toolkits.

The software source code is available to readers:
Yes, https://github.com/Kingsford-Group/bloomtree

We successfully downloaded and ran the software.

The data for replication is available for download:
Yes, public data from SRA; it's listed on supp materials, but could
be added to the tool site too.

The data format is either standard, or straightforward, or documented.
Yes

Other comments:

* we reimplemented SBT within the khmer package here:
  https://github.com/ctb/2015-khmer-sequence-bloom-trees.  It's clean and
  easy to reimplement, which speaks well to its likely impact.

* we compiled the software from scratch, built some test data sets,
  and verified that it worked as expected:
  https://github.com/ctb/2015-sbt-demo

Recommendations:

* we strongly recommend that a lab-independent URL be used as the
  official URL for the software (e.g. the github page, instead of the
  CMU page).  Lab Web sites tend to fall out of date or otherwise
  decay.

* One of the big drawbacks to Bloom filters is that they are fixed in
  size. Guidance on choosing Bloom filter size would be welcome.  One
  way to do this is to use an efficient method to calculate
  cardinality, and khmer has a BSD- licensed implementation of the
  HyperLogLog cardinality counter that they'd be welcome to copy
  wholesale.

Signed,

\C. Titus Brown

Luiz Irber

Qingpeng Zhang
