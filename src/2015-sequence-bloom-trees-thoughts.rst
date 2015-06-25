Thoughts on Sequence Bloom Trees
################################

:author: C\. Titus Brown
:tags: Bloom filters
:date: 2015-06-25
:slug: 2015-sequence-bloom-trees-thoughts
:category: science

We just submitted `our review
<http://ivory.idyll.org/blog/2015-review-bloomtree.html>`__ of the
paper `Large-Scale Search of Transcriptomic Read Sets with Sequence
Bloom Trees. <http://biorxiv.org/content/early/2015/03/26/017087>`__,
by Brad Solomon and Carl Kingsford.

The paper outlines a fairly simple and straightforward way to query
massive amounts of sequence data (5 TB of mRNAseq!) in very small disk
(~70 GB) and memory (~under a GB), fairly quickly (~2.5 days).

The short version is that I think this is an incredibly powerful
approach that I am now planning to build on `for our own Moore DDD
project
<http://ivory.idyll.org/blog/2014-moore-ddd-stmt-of-work.html>`__.

The review was a lot of fun; it's right up our alley, and we've
thought a lot about related (but somewhat distinct) issues.  Here are
some extended comments that I thought were probably not appropriate
for the official review because they're somewhat forward looking.

----

First, we did the review in approved Open Science style.  Since Brad
and Carl did us the favor of using GitHub (source code) and bioRxiv
(preprint), and I sign my reviews, there need be no mystery in this
process.  Therefore I am posting our review publicly with only minor
edits.  Moreover, I filed three issues on GitHub (`#1
<https://github.com/Kingsford-Group/bloomtree/issues/1>`__, `#2
<https://github.com/Kingsford-Group/bloomtree/issues/2>`__, and `#4
<https://github.com/Kingsford-Group/bloomtree/issues/4>`__) and
submitted two pull requests (`#3
<https://github.com/Kingsford-Group/bloomtree/pull/3>`__ and `#5
<https://github.com/Kingsford-Group/bloomtree/pull/5>`__), both of
which were merged.

Second, because we work in this area and are very interested in it, I
put together both a demo of their software (see `2015-sbt-demo
<https://github.com/ctb/2015-sbt-demo>`__) and also did a simple
reimplementation in khmer (see `2015-khmer-sequence-bloom-trees
<https://github.com/ctb/2015-khmer-sequence-bloom-trees/blob/master/README.md>`__)
to make sure that their software worked, and that I thoroughly
understood the basic issues involved.

Note that we are unable to use their implementation as licensed, as it
is under the GPL and would contaminate our source tree, which is under
BSD :(.

Third, I have a lot of suggestions and thoughts! For example,

* The use of RRR compression is awesome and is something we should
  look into for khmer (`dib-lab/khmer#1074
  <https://github.com/dib-lab/khmer/issues/1074>`__).

* We get a 20% performance increase from a simple optimization applied to
  our k-mer lookups that could apply to SBTs -- see just-merged
  `dib-lab/khmer#862 <https://github.com/dib-lab/khmer/pull/862>`__,
  by Camille Scott.

* The authors might also be interested in making use of our HyperLogLog
  implementation for k-mer cardinality counting, which could help
  users choose the right size for their Bloom filters.

* Streaming diginorm/semi-streaming in general (see `Crossing the
  streams <https://peerj.com/preprints/890/>`__) could be a very
  useful pre-filter for building SBTs.  My guess is that with k-mer
  prefiltering a la digital normalization, there would be no loss to
  sensitivity but a substantial decrease in memory requirements.

* It would be really interesting to brainstorm about how far this can
  be taken.  We have reasonably strong evidence & intuition that you
  can do `straight abundance estimation
  <http://ivory.idyll.org/blog/2015-wok-counting.html>`__ directly off
  of counting Bloom filters, and it doesn't seem like a stretch to
  say, "hey, let's store EVERYTHING in an sequence Bloom tree analog
  and do comparative expression analysis that way!"  We don't have an
  immediate use case for this ourselves, but I'm sure one will present
  itself...

* Qingpeng Zhang and I immediately started talking about how to apply
  this to metagenomics, and the main worry is that the method seems to
  depend on low diversity of true k-mers.  This can partly be mitigated
  by diginorm and/or semi-streaming k-mer abundance trimming, but ultimately
  things are going to scale at best with the true size of the De Bruijn
  graph.  It will be interesting to see how this plays out.

--titus
