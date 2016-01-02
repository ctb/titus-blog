Sustaining the development of research-focused software
#######################################################

:author: C\. Titus Brown
:tags:
:date: 2016-01-02
:slug: 2016-sustaining-research-software-development
:category: science

Recently I was asked by someone at a funding organization about the
term "hardening software"; I wrote a blog post@@ asking others what
they thought, and this got a number of great comments (as well as
spurring Dan Katz to write a blog post of his own@@).  I'd already
written an initial response to my friend at the funder (which I'll
publish separately), but the comments I got from the blogosphere made
me think more broadly about how researchers mentally model software
development.

I see two pretty divergent ways of thinking about software development
in my research community.  The first I would call "consumer product",
and the second, "community project". [0]

In "consumer product" software, a company or research group builds
some software and releases it for the wider world to use, often
through a publication or a preprint.  The goal of the developers is to
allow other people to use the software. They may be quite passionate
about this, providing good documentation and test data sets along with
help forums. However, there will generally be little to no developer
documentation available: the goal is to recruit *users*, not
developers.

In "community project" software, a company or research group builds
some software, and (as above) releases it to the wider world to use.
Here, the producers usually want to let people use the software
directly, but there is an additional emphasis on the software being
something malleable - something that others can work on and with, and
mold or adapt themselves to fit their needs.

With both kinds of projects, the software can be more or less mature,
and can be targeted at novice or expert users, and can have a broad or
a narrow technical vision, etc etc.  The key question is whether the
*software* is the product, or the software *project* is the product.

It's not hard to find consumer product-type software in the
bioinformatics world.  Most assemblers and mappers are essentially
opaque blobs of software that users interact with via the command
line, and bugs, issues, and feature requests are communicated to a
core set of developers, who then deal (or not) with them.

It's quite a bit harder to find full community projects in
bioinformatics; while I'm sure I'll think of many the moment I hit
"post", I don't have a shining exemplar in mind, although velvet and
samtools come close.  This may be due to a lack of developers, but is
perhaps also because of the way academic funding works. I'll talk more
about this below.

Sustainability and software needs - why do we care, and what do we want?
------------------------------------------------------------------------

Software is fast becoming a sine qua non in research, and researchers
and funding agencies have been trying to figure out how to support
sustainable software development.  There's a `whole NSF program
devoted to sustainable research software
<http://www.nsf.gov/pubs/2014/nsf14520/nsf14520.htm>`__, and I think
it's fair to say that one of the main subsurface goals of the `BD2K
program <https://datascience.nih.gov/bd2k>`__ is to tackle the
question of software (PSA: data isn't much use without software). The
USDA and bio bits of DOE are also running smack into the problem that
the research programs they fund are utterly dependent on software yet
investments in software are often secondary and rarely yield software
that is usable past the end of the grant.  It turns out that software
development for research is a surprisingly intransigent beast.

Fundamentally, stable research software is a way of accelerating
research.  I believe there to be a lot of interest in & need for the
domain-specific software set - software that is more specific than
(say) Linux, Python and R, or RStudio and IPython/Project Jupyter, or
the various major R and Python packages for data analysis. These have
large user bases and are generically quite useful, so while supporting
them is still a challenge, their support options become more
varied. Conveniently, the `Moore, Sloan, and Helmsley Foundations
<http://blog.jupyter.org/2015/07/07/jupyter-funding-2015/>`__ have
been stepping up here as well. But what about software closer to the
domain?

It's been very hard to meet the tremendous need for sustained
development of domain-specific software - for example, in
bioinformatics, I understand that very few mappers or assemblers or
parsing libraries are actively supported by funding agencies for more
than one round. When they are, it's almost always for new methods
development, not for supporting and sustaining the software; these
goals are somewhat at odds, to say the least.  (See `The three
porridge bowls of sustainable scientific software development
<http://ivory.idyll.org/blog/2015-on-sustainable-scientific-software.html>`__
for more on this conundrum.) The software that *is* supported directly
usually is a "best of breed" software package that wins because it's
first-to-market, and/or because of existing user bases, and/or because
it's useful for biomedically-relevant missions; moreover, it's often
produced by a few groups at well-known institutions. While these tools
are often quite good in and of themselves, I don't think this approach
serves tool and algorithm diversity. We need an ecosystem of tools,
not just one tool in each domain that is "owned" by one or two actors.

So, to rephrase the question more specifically: how can we build and
sustain an *ecosystem* of research-focused software to support and
accelerate inquiry with flexible domain-specific computational tools?

The lesson I take from the open source world is that, in the absence
of a business model, only "community project" software is sustainable
in the long term.

When I write that, it seems almost tautological - of *course* if a
project doesn't have a business model, the project won't be
sustainable without a larger community! But there is essentially *no*
business model behind *most* research software. (The most common
approach seems to be assume that anything important will continue to
be funded - a dangerous assumption in these days of 10% funding lines;
the next most common approach is to build software to be at the core
of a research program, and then get funding for the surrounding
research program. Both of these approaches have obvious failure
modes.) And so I think that we should be focusing on community project
software.

In support of this thesis, I would point out that all of the more
general packages I mentioned above (Linux, Python, R, RStudio,
IPython/Project Jupyter, and things like scikit-learn) are full open
source community projects, with a robust contribution process, a wide
body of regular and part-time developers, and open and ongoing
conversations about future directions.  All of these packages have
demonstrated long-term sustainability. I'm can't conclude that this is
a causal relationship, but I would bet that it is.

Shoving software out into the community is no guarantee, but it's easier now than it used to be.
------------------------------------------------------------------------------------------------

Lest people think that slapping a contributor process on software is
enough to make it "community supported", let me just say that it's
much more complicated than that. In addition to all the skills you had
to have to write the software in the first place (the technical and
algorithmic skills, the scientific background, and at least some
software engineering knowledge) you also need to engage with the
community online, solicit feedback and improvements, manage
contributions and bug reports, and otherwise be responsive.

The transition to a successful community project seems challenging to
me. From tracking this in the open source world (mostly in
retrospect), it seems like you need some combination of luck, skill,
and robust community-facing efforts.  In the scientific world, I'm not
sure how to guide funding towards projects where this transition is
likely to be successful.  My first thought would be to go with the NSF
structure of SSE/SSI - fund new projects to get them started off, then
provide transition grants to see if they can engage with a larger
community, and then fund them as part of the community.  One problem I
see is that the time scale is so long - it's 5-10 years to take a
project from nothing to something - and maintaining funding across
that period is fraught with challenges.

One piece of good news is that it's become a lot easier to manage the
technical infrastructure. GitHub or BitBucket can host your code, make
it easy for people to work off the latest version, and provide tools
to manage patch contributions and code review; ReadTheDocs and github
and other sites can host your documentation; Travis-CI and other
continuous integration platforms can run your tests, there are lots of
places to host mailing lists, Twitter and blogs can help you gather
your community 'round, and teleconferencing can help you coordinate
developers.

The bad news is that the new skills that are required are community
building and social interaction skills - something that many faculty
are unprepared for, and probably won't have time for, and so they need
to outsource them (just like most software engineering, or
experimental work).  This leads to a problem: community projects are
bigger.

Community software projects are bigger, and therefore harder to fund
--------------------------------------------------------------------

From the funding perspective, another problem is that community
software projects are just... bigger, and hence more expensive. You
need to pay attention not just to the research aspect of things, but
also the community and the software quality. This probably means that
you need at least two full time efforts for even a small project - a
community manager/release manager/testing manager, and technical lead
to drive the project's software engineering forward.  (This is in
addition to whatever science you're doing, too ;).

From the applying-to-funder perspective, this makes life a bit of a
nightmare. You have to successfully navigate continued software
development, the building out of a community, and scientific progress,
and then justify this all in an "ask" to a funding body, with a pretty
low chance of making it.  Add in the fact that very few programs will
fund software development directly, and the ask gets larger.

I don't think anyone in industry is going to be surprised by the
notion that you have to deliver value (here, "innovation") while
building robust software.  The contrast here is really that
researchers often toss "grad ware" out the door as if it's good,
robust, usable software, and we often have no funding plan beyond
"publish it and then apply for a bunch of grants." This isn't
sustainable, we shouldn't view it as sustainable, and the only
surprise is that anyone thinks it *is* sustainable.  But the corollary
may be that we need to figure out how to engage with a larger
community around developing individual research software packages,
rather than trying to productize it.

But if that engagement costs more, it's going to be even harder for
program managers to fund.

Focusing on community software projects solves a lot of problems
----------------------------------------------------------------

It's always difficult to figure out if software is actually useful
when people are asking for grant support for it. My guess? If there's
a broad, robust community associated with it, it's probably useful. (I
don't really know how to measure the size and quality of the
community, though.)

We probably need fewer community projects overall. Maybe grad students
could write extensions to existing software, instead of writing a
whole new package; I gather this is what happens in the VTK world.

Community projects will inevitably have less tolerance for crap
software, at least on average.  (I haven't thought through this
thoroughly, but (a) no one wants to join your software project if they
can't get it to run, and (b) your project will die if every release
has more new bugs in it than were fixed.) So the poor quality, lousy
adherence to community standards, and miserable packaging that
afflicts many current bioinformatics projects would probably just go
away in a model where only community-backed projects were given
continued funding.

Community projects also have a built-in succession mechanism - when a
principle investigator loses interest in a particular project, or
retires, or lapses in funding, there is a decent chance that other PIs
will be able to pick up the project and move forward with it.

Communities also channel software development in specific ways that
are more democratic.  If the project leads aren't responsible for
implementing everything but have to rely on the community to implement
and support features, then they are less likely to add useless
features.

A more fundamental point is that I often think that we don't really
know how to set our goals in software development. Something that open
source excels at is channeling the needs of its users into functioning
software. Explicitly acknowledging the community's role in deciding
the future of a software project means that the project is committed
to meeting the needs of its users, which I think probably fits with
many goals of funders.

What does this all mean?
------------------------

In sum, I think one way - perhaps the best way - to sustainably
develop research software is to build a community around its
development

One way for funders to do this might be to provide support for
software making the transition from a small project to a community
project.

While funding might still be needed to maintain the core of the
project (I think a full-time developer and a full-time community
manager are minimal requirements) this funding would be leveraged
better by supporting a full-on community of developers, rather than
supporting a small team.

A corollary might be that software grants should be reviewed equally
on their community engagement plan, not just on their innovation in
methods.

This goes some way towards formalizing the notion that some research
software isn't meant for further use, by providing some direction for
research software that IS meant for further use (see `Please destroy
this software after
publication. kthxbye. <http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__
for my thoughts on the rest ;).

Some problems with this perspective
-----------------------------------

I do worry a lot that we don't have the robust community of developers
in biology to support the necessary software development.  If all you have
is users, who in the community develops the software?

Open source is hardly a panacea, and open source processes aren't
bulletproof. Lots of open source software is really bad. I do think
that the ones that attract a community are likely to be less bad,
though ;).

Community coalescence may be more strongly related to star power and
social media savviness than technical excellence.

Scientists (at least in biology) don't get rewarded for community
involvement and community development.  On the flip side, maybe
getting grants explicitly for doing that would provide a mechanism of
reward.

Researchers still need to figure out how to do good software
engineering, which is hard.

----

.. Need core dev, support, AND community. AND/OR, ecosystem.

   bioinformatics middle class; trinity. command-line binaries vs.

   - avida and decadal software development.
   - funding agencies don't really fund community development.

   sloan and moore and helmsely and arnold seem to get it.
   review criteria
   fernando chapter

   training!

[0] (I'm ignoring "burner" software - software that serves to
demonstrate or explore an algorithm, but isn't intended for use or
extension - see my post `Please destroy this software after
publication. kthxbye. <http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__,
and the "No success without quality" section of `Gael Varoquaux's post
<http://gael-varoquaux.info/programming/software-for-reproducible-science-lets-not-have-a-misunderstanding.html>`__
for discussions on that.  I'm also going to ignore platforms which try
to support other software rather than offering research functionality
directly on their own; these fall into infrastructure more than
research-pointy software.
