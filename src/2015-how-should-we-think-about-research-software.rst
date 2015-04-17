Please destroy this software after publication. kthxbye.
########################################################

:author: C\. Titus Brown
:tags: software, sustainability
:date: 2015-04-17
:slug: 2015-how-should-we-think-about-research-software
:category: science

tl;dr? A while back `I wrote that there are three uses of research
software
<http://ivory.idyll.org/blog/research-software-reuse.html>`__:
replication, reproduction, and reuse. The world of computational
science would be better off if people clearly delineated whether or not
they wanted anyone else to reuse their software, and I think it's a
massive mistake to expect that everyone's software should be reusable.

----

A few months back, I reviewed a pretty exciting paper - one I will
probably highlight on my blog, when it comes out.  The paper outlined
a fairly simple concept for comparing sequences and then used that to
develop some new ultra-scalable functionality.  The theory seemed novel,
the computational results were pretty good, and I recommended acceptance
(or minor revisions).  This was in spite of the fact that the authors
stated quite clearly that they had produced largely unusable software.

Other reviewers were not quite so forgiving, however -- one reviewer
declined to review the paper until they could run the software on
their own data.

This got me thinking - I think I have a reputation as wanting people
to release their software in a useful manner, but I've actually shied
away from requiring it on several occasions.  Here was a situation
that was a pretty direct conflict: neat result, with software that was
not intended for reuse.  Interestingly, I've drawn this line before,
although without much personal comment.  In `my blog post on review
criteria for bioinformatics papers
<http://ivory.idyll.org/blog/blog-review-criteria-for-bioinfo.html>`__,
there's nothing there about whether or not the software is *reusable*
- it must just be legally readable and executable.  But I'm also
pretty loud-mouthed about wanting *good quality* (or at least *better
quality*) software out there in the bioinformatics world!

So what gives?  I felt that the new *technique* looked pretty awesome,
and would be tremendously useful, while the implementation was (as
stated) unlikely to be something I (or others) used.

I think this highlights that there are two *different* possible goals
for bioinformatics papers.  One goal is the standard scientific goal:
to demonstrate a new method or technique, whether it be mathematical
or computational.  The other goal is different, and in some ways much
harder: to provide a functioning tool for use and reuse. These should
have different review standards, and that maybe the authors should be
given the opportunity to distinguish clearly between the two goals.

There's actually a lot of commonality between what I would request of
the software from either kind of paper, a technique paper or a tool paper.

* Both need to be accessible for download and viewing - otherwise, how
  can I understand the details of the implementation?

* Both types of software need to be usable enough to reproduce the
  results in the paper, in theory (e.g. *given sufficient access to
  compute infrastructure*).

* Both should be in a publicly accessible and archived format, to
  avoid `loss of the software
  <http://www.davelunt.net/evophylo/2013/03/software-persistence/>`__
  from personal Web sites, etc.

* Both should show evidence of decent principles of basic software
  engineering, including the use of version control, some form of
  testing (albeit unit testing or functional testing or even just
  defined input with known good output), release/version information,
  installation/dependency information, and the like.

However, there are some interesting differences.  Off the top of my head,
I'm thinking that:

* Crucially, the software from the technique paper would not need to
  be open source - by the `OSI definition
  <http://opensource.org/licenses>`__, the technique code would not
  need to be freely modifiable or re-sharable.

  (To be clear, I know of neither any formal (journal) requirements
  nor ethical requirements that a particular implementation be
  modifiable or redistributable.)

* Nor need the software from the technique paper be written in a
  general way (e.g. to robustly process different formats), or for
  broader re-use.  In particular, this means that documentation and
  unit/functional tests might be minimal - enough to support replication
  but no more.

* The software from the technique paper should be accessible to basic
  review, but should not be subject to code review on style or
  implementation - correctness only.

* Software from a "tools" paper, by contrast, should be held to much
  higher standards, and be subject to code review (in parts) and
  examination for documentation and installation and ... oh, heck,
  just start with the `sustainability evaluation checklist
  <http://www.software.ac.uk/online-sustainability-evaluation>`__ at
  the SSI!

I'm aware that by having such relaxed constraints on technique
publication I'm more or less directly contradicting myself in `my
earlier blog post on automated testing and research software
<http://ivory.idyll.org/blog/automated-testing-and-research-software.html>`__
- all of that *definitely* holds for software that you hope to be
reused.

I'm not sure how or where to draw the line here, exactly.  It's
certainly reasonable to say that software that doesn't have unit tests
is likely to be wrong, and therefore unit tests should be required -
but, in science, we should never rely on a single study to prove
something anyway, so I'm not sure why it matters if software is wrong
in some details.  This is where the `difference between
"replicability" and "reproducibility"
<http://ivory.idyll.org/blog/research-software-reuse.html>`__ becomes
important.  If I can't replicate your computation (at least in theory)
then you have no business publishing it; but *reproducing* it is
something that is a much larger task, outside the scope of any given
paper.

I want to quote David States, `who wrote a comment two years ago on my blog <http://ivory.idyll.org/blog/research-software-reuse.html#comment-772560142>`__:

   Too often, developers work in isolation, and this creates a high
   risk for code errors and science errors. Good code needs to be
   accessible and this includes not just sharing of the source code
   itself but also use of effective style, inclusion of tests and
   validation procedures and appropriate documentation.

I think I agree - but what's the minimum, here, for a technique paper
that is meant to be a demonstration of a technique and no more?

One final point: in all of this we should recognize that the current
situation is quite poor, in that `quite a bit of software is simply
inaccessible for replication purposes
<http://reproducibility.cs.arizona.edu/v2/RepeatabilityTR.pdf>`__.
(This mirrors my personal experiences in bioinformatics review, too.)

Improving this situation is important, but I think we need to be
precise about what the minimim is.  I don't think we're going to get
very far by insisting that all code be held to high standards; that's
a generational exercise (and part of why I'm so bullish on `Software
Carpentry <http://software-carpentry.org/>`__).

So: what's the minimum necessary for decent science?

--titus

p.s. In case anyone is wondering, I don't think `our software
<http://github.com/ged-lab/khmer>`__ really meets my own criteria for
tool publication, although it's getting closer.

p.p.s. Drawing this distinction leads in some very good directions for
publishers and funding bodies to think about, too.  More on that in
another blog post, if I get the chance.

p.p.p.s. My 2004 paper (Brown and Callan) has a table that's wrong due
to a fencepost error.  But it's not seriously wrong.  *shrug*
