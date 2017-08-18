My Salmon review
################

:author: C\. Titus Brown
:tags: salmon,review
:date: 2017-08-16
:slug: 2016-review-salmon
:category: science

I was one of the reviewers of the Salmon paper by Patro et al., 2017,
`Salmon provides fast and bias-aware quantification of transcript
expression
<https://www.nature.com/nmeth/journal/v14/n4/abs/nmeth.4197.html>`__.
I was asked to review the paper on September 14, 2016, and submitted
my review (or at least stopped getting reminders :) soon after October
20th.

The review request stated,

   ... I would be grateful for your views on both the technical merits of this work and its interest to a broad readership.

   Please try the tool and report your experience. Let me know if you have issues with access.

   Brief Communications are intended to report concise studies of high quality and broad interest but are expected to be less substantial than Articles. Typically, a Brief Communication will describe a significant improvement to a tried-and-tested technique, its adaptation for a new application, or an important new tool of interest to the scientific community.

and I reviewed the paper as requested.

Below is the full text of my review as I submitted it.  (Note that I
have not been posting my reviews lately because I've been busy, and I
don't have a simple automated system for doing it.  In this case the
review seems like it might be of general interest.)

----

The authors present salmon, a new RNAseq quantification tool that uses
pseudoalignment and is highly performant.  The significant factors
recommending salmon over other tools include speed, high sensitivity,
correction for technical biases in sequencing, an open source license,
and a robust implementation that is straightforward to use.  The paper
makes the argument that salmon is the premier tool for RNAseq
quantification.

The paper is well written, if unavoidably dense due to the nonsensical
space constraints of this journal.  The supporting and supplemental
material is well written and seems comprehensive.  The comparisons
with kallisto and express seem fine to me although I note that the x
axes of the various figures are zoomed into a slightly absurd extent;
nontheless, the comparisons support the conclusions reached in the paper.

There are some interesting gems buried deep within the paper.  For
example, I was struck by the observation that apparent isoform
switching may be caused by technical artifacts (supp fig 5).  While
the format and journal chosen by the authors doesn't permit proper
exploration of this, I suspect that the technical bias correction is
going to be a very important aspect of this software.

I should also say that various versions of the preprint and software
have been out for well over a year, and we and others have been using
it since very early on.  Others have done independent benchmarks that
agree with the conclusions reached in the paper.

Requested changes:

* the authors should provide an archival location for salmon, and include
  a DOI to the specific version used in this paper. This can be easily
  accomplished with e.g. zenodo/github integration.

* as the authors are putting this forward for general use, I would
  like at least a brief discussion of how they do software testing and
  validation.  In particular, this can answer the important question
  of how users and developers can know that future versions of salmon
  will produce results at least as correct as the results in this
  paper.

Requested additions:

* optional but recommended: the documentation should be expanded to include
  a "getting started" tutorial. Right now a naive user would have no idea
  where to star.

Typos/corrections:

p3, at the same false discovery rate than those => as those

probabilistic is mis-spelled on p5

p7, reference 5 has "page" in it inappropriately.
