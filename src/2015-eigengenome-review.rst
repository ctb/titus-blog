Our review of the eigengenome partitioning paper
################################################

:author: C\. Titus Brown and Camille Scott
:tags: assembly, partitioning
:date: 2015-09-22
:slug: 2015-eigengenome-review
:category: science

Below is our first review of the paper `Detection of low-abundance bacterial
strains in metagenomic datasets by eigengenome partitioning
<http://www.ncbi.nlm.nih.gov/pubmed/?term=26368049>`__ by Brian Cleary
et al., recently published in Nature Biotech.

All in all, this is one of the most technically interesting papers
we've read in a while.

A few interesting tidbits of background info --

* this is the paper that I talked about at the top of `Please destroy
  this software after publication. kthxbye
  <http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__.  (The software appears to be more usable now that it was when
  we first reviewed the paper.)

* after signing the review, I engaged in separate conversations about
  the paper with the two other reviewers, the editor, and the authors
  ;).

* I would guess that the authors lost at least a dozen citations by
  not publishing this as a preprint.  I consciously avoided mentioning
  the approach, using the software, or developing on top of the method
  while it was in review, because it wasn't publicly available yet and
  I didn't know how long it would take to come out.  Maybe this isn't
  a big deal in the larger scheme of things, but I think it's a very
  clear example of science being slowed down by publishing delays.

* one of the other reviewers suggested that they look to our own work
  on partitioning (`Pell et al., 2012
  <http://www.pnas.org/content/109/33/13272.full>`__) and do a
  comparison.  I think I sent an e-mail to the authors saying that
  this would be a silly comparison because their method should work
  way better than ours, and they could quote me on that ;). (I gave
  more details in the e-mail, but, basically, graph partitioning as-is
  doesn't work that well on large samples.)

-----

In this paper, Cleary et al devise a clever (dare I say
"groundbreaking?") approach to raw-read partitioning of metagenomic
data.  This approach addresses a variety of problems in shotgun
metagenome analysis.  In short, the approach is entirely novel, the
scaling potential is amazing, the results seem quite good to us, and
the practical need for such an approach is great.

We divide our review into three parts -- the results & discussion; the
methods; and the software.  Details below.

Given the novelty of the approach and the strength of the results, we
personally don't think it's reasonable to require that the software be
made more usable, but this may be a requirement of NBT.  We do think a
small test data set that can be run on a single machine should be made
available for reviewers and readers to try out; this shouldn't be
particularly burdensome or time consuming.

The authors should consider posting this as a preprint so we can cite
this in forthcoming reviews while waiting for the no doubt lengthy
review process to complete...

Revisions that should, in our view, be required, are marked with '\*\*'.

----

Results and discussion:

The authors develop a partitioning approach that splits up raw reads
into different bins, or partitions, based on an eigengenome clustering
approach.  The goal is to separate reads by source genome based on
abundance covariation, so that they can be assembled or analyzed by
donwstream approaches.  A key part of the approach is to do this
partitioning scalably, so that extremely large data sets can be
partitioned and then analyzed with more intensive approaches later on.

To validate this approach, the authors apply their partitioning
approach to several large data sets and generate what, to those of us
who have invested in raw-read partitioning, are excellent results with
the normal drawbacks.  Specifically, the partitioning seems to do a
great job of separating out reads that should belong together, with
the caveat that separating highly similar sequences (core conserved
regions in strains) is effectively impossible.

The first paragraph is a general intro that's a little unsatisfying:
first, metagenomic researchers frequently sequence billions of bases
because otherwise \_they don't sample the diversity\_, not because of
the challenges they face with assembly pipelines! And second, it's not
at all clear that genomic content can be "identified through popular
alignment-based metagenomic analysis."  Sure, that's what's used,
because they have no choice, but it doesn't work very well except for
SSU analyses.

The rest of the introduction is very well done - technically sophisticated
and pretty comprehensive.  I'm a little leary of the strength of the
statement that "In this scheme, short reads which originate on the same
physical fragment of DNA are likely to partition together..." - isn't
that difficult to conclusively demonstrate??  Maybe "should" would be
better than "are likely"?

The data sets chosen are good test sets.  The application to a
multiple TB data set (!!) is amazing.  The Sharon data set is a
perfect application of this approach and the results look good to me.

I can't find a place where the authors say this outright, although
they imply it in their discussion -- they should point out that MORE
SAMPLES gives you MUCH MORE RESOLUTION with this approach, which is a
key feature in the sample-heavy future.

The authors are (in my opinion) quite right that their approach is a
dramatic improvement over assembling first and then binning later;
this approach leaves open the option of applying different assemblers
or parameters for each bin, which could be quite important, and is
also likely to be much more scalable than any assembly-based approach.

----

Methods:

The methods are (or at least seem to be, to us) pretty groundbreaking,
and more broadly applicable than metagenomics.  We do not think that
using document vectors/latent semantic indexing for unassembled
sequence analysis has been done before -- this is enabled by their use
of the complex-simplex hashing function.  We believe this to be novel
(or at least we would be using it if we had ever seen it before.)

The authors effectively construct a (sample x k-mer abundance) matrix
that they then cluster.  However, this on its own is not scalable, so
they invest in a nice hyperplane clustering approach, relying on a
complex-space hashing approach that places close k-mers near to each
other in k-space.  These k-mers are assigned to the same column in the
matrix, which effectively decreases the size of the matrix to
something much more manageable.  This matrix is then clustered using
SVD.  Reads are then assigned back to these k-mer clusters.

For each sample the number of columns must scale ~with the diversity
of the sample; this seems likely to be the major memory bottleneck.

It seems to me that the resolution could be increased iteratively, by
some sort of adaptive splitting of columns in tandem with the SVD.
This is probably part of their future work.

An important feature of the SVD implementation is that it is
streaming!

We think the complex-simplex approach and clustering could easily be
applied to many parts of sequence analysis, including mRNAseq
analysis, error correction, and graph building.

In any case, this all makes sense to us and we think it's novel.

----

Software:

The software is available on github, good!

\*\* No license is specified; this needs to be addressed.

\*\* No copyright is specified; this needs to be addressed.

\*\* The specific version (git hash? branch tag?) used to generate the
   results in this paper should be specified somewhere and placed in
   the paper.

The software is clearly not intended for direct reuse.  There are stern
warnings about how it's going to be hard to use in any particular
environment, and it's a mess o' scripts.

\*\* Space limitations in NBT prevent replication details (detailed
   parameters, etc.) from being provided in the text.  Fine, but please
   provide them somewhere (github?) and point at them!

----

[ ... typo commentary redacted ... ]

Signed,

\C. Titus Brown, MSU

Camille Scott, MSU
