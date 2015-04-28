Popping the open source/open science bubble.
############################################

:author: C\. Titus Brown
:tags: open source, open science
:date: 2015-04-27
:slug: 2015-we-live-in-a-bubble
:category: science

One of the things that became clear to me over the last two weeks is
just how much of a open source/open science bubble my blog and Twitter
commenters live in.  Don't take that as a negative -- I'm in here with
you, and it's a great place to live :).  But it's still a bubble.

Two specific points brought this home to me.

First, a lot of the Twitter and blog commentary on `Please destroy
this software after
publication. kthxbye. <http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__
expressed shock and dismay that I would be OK with non-OSS software
being published.  (Read `Mick Watson's blog post
<https://biomickwatson.wordpress.com/2015/04/21/on-publishing-software/>`__
and `Kai Blin's comment
<http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html#comment-1977208787>`__.)
Many *really* good reasons why I was wrong were brought up, and, well,
I have to say it was terrifically convincing and I'm going to change
my own policy as a reviewer.  So far, so good.  But it `turns out
<https://twitter.com/ctitusbrown/status/590130439421087744>`__ that
only a few journals require an actual `open source
<http://opensource.org/licenses>`__ license (`Journal of Open
Research Software
<http://openresearchsoftware.metajnl.com/about/editorialPolicies#custom-1>`__
and `Journal of Statistical Software
<http://www.jstatsoft.org/instructions>`__).  So there is a
**massive** disparity between what some of my tweeps (and now me)
believe, and what is codified practice.

Second, many eloquent points were made about software as a major
product and enabler of research -- see especially the comments on
"software as communication" and "software as experimental design" by
others (linked to `here
<http://ivory.idyll.org/blog/2015-more-on-software.html>`__ - see
"Software as..." section).  These points were very convincing as well,
although I'm still trying to figure out how exactly to evolve my own
views.  And yet here again I think we can be quite clear that most
biologists and perhaps even some bioinformaticians would have either
no considered opinion on software, or be outright dismissive of the
idea that software itself is intellectual output.  Again, very
different from what the people on Twitter and my blog think.

I was already pretty surprised with how strong the case was for open
source software as a requirement (go read the links above).  I was even
more surprised with how eloquently and expansively people defended the
role of software in research.  Many, many strong arguments were put
forth.

So, how do we evolve current practice??

But first...

If software is so important, software is fair game for peer review
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I promise this wasn't a stealth goal of my `original blog post
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html>`__
but people realize that an obvious conclusion here is that software is
fully fair game for in depth `peer review
<http://www.nature.com/news/rule-rewrite-aims-to-clean-up-scientific-software-1.17323>`__, right? (Never mind that `most scientists probably aren't capable
of doing good peer review of code
<http://software-carpentry.org/blog/2015/04/quality-is-free-getting-there-isnt.html>`__,
or that `any reasonably strong code review requirements
<http://www.mozillascience.org/effective-code-review-for-journals>`__
would mean that `virtually no more software would be published
<https://twitter.com/billdoesphysics/status/590279027606179842>`__ -
an effective but rather punitive way to ensure only good software is
published in science :)

A few weeks back I received a response to my review of an application
note, and the senior author objected strenuously to my reviewing their
actual *software* in any way.  It really pissed me off, frankly -- I
was pretty positive about their packaged software and made some
suggestions for how they could improve its presentation to others, and
basically got back a punch to the nose asking how dare I make such
suggestions.  As part of my own rather intemperate response, I said:

   This is an *application note*.  The application itself is certainly
   fair game for review...

How much angrier would this person have been if I'd rejected the paper
because I actually had comments on edge cases in the source code??

Two years ago now we had another `big eruption
<http://ivory.idyll.org/blog/on-code-review-of-scientific-code.html>`__
("big" in the Twitter sense, at least) around code review.  A year
even before *that* `I proposed optional review criteria for
bioinformatics papers
<http://ivory.idyll.org/blog/blog-review-criteria-for-bioinfo.html>`__
that my students, at least, have started to use to do reviews.

In all that time very little has changed.  There are three objections
that I've heard in these last three years that bear up over time --

First, scientists neither know how to `review code
<http://ivory.idyll.org/blog/blog-review-criteria-for-bioinfo.html>`__
nor how to `write reasonable code
<http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745>`__;
this would lead at best to inconsistency in reviews, or at worst simply
lead to a massive waste of time.

Second, I am not aware of any code review guidelines or standards for
scientific code.  Code review in industry has at least some basic good
practices; `code review in science is a different beast
<http://arxiv.org/abs/1407.5648>`__.

Third, `code review can be used to unfairly block publication
<http://simplystatistics.org/2013/09/26/how-could-code-review-discourage-code-disclosure-reviewers-with-motivation/>`__.
This came up again `recently
<http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html#comment-1973345421>`__
(READ THAT COMMENT) and I think it's a great reason to worry about
code review as a way to *block* publication.  I still don't know how to deal
with this but we need some guidelines for editors.

The bottom line is that if software is fair game for peer review, then
we need a trained and educated body of reviewers - just as we do for
molecular methods, biological sequencing, and statistics.  This will
inevitably involve the evolution of the community of practice around
both software generation (s...l...o...w...l...y... happening) *and*
software peer review (<envision birds chirping in the absence of
conversation>).

(One solution I think I'm going to try is this: I'm going to ask the
Software Carpentry community for a volunteer to do code review for
every computational paper I edit, and I will provide suggested
(optional) guidelines. Evil? Maybe so. Effective? I hope so.)

We need some guidelines and position papers.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of the discussion around computation as a primary research product,
Dan Katz `asked
<https://twitter.com/danielskatz/status/591360494042251266>`__,

   "I wonder if a collaborative paper on this would find a home somewhere?"

Yes. To break out of the bubble, I think we need a *bunch* of position
papers and guidelines on this sort of thing, frankly.  It's clear to
me that the online community has a tremendous amount of wisdom to
offer, but we *are* living in a bubble, and we need to communicate
outside of that -- just as the open access and open data folk are.

One important note: we need simple, clear, minimum requirements, with
broadly relevant justifications.  Otherwise we will fail to convince
or be useful to anyone, including our own community.

A few ideas:

* We need a clear, concise, big-tent writeup of "why software is important,
  and why it should be OSS and reviewed when published";

* We need to discuss good minimum requirements in the near term for
  code review, and figure out what some end goals are;

* We need some definitions of what "responsible conduct of
  computational research" looks like (Responsible Conduct of Research
  is a `big thing
  <http://grants.nih.gov/training/responsibleconduct.htm>`__ in the
  US, now; I think it's a useful concept to employ here).

* We need some `assessment metrics
  <https://twitter.com/kaythaney/status/590205234661621760>`__ (via
  @kaythaney) that disentangle "responsible conduct of research" (a
  concept that nobody should disagree with) from "open science" (which
  some people disagree with :).

and probably a bunch of other things... what else do we need, and how
should we move forward?

--titus
