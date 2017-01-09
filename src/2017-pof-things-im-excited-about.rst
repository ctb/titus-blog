Topics and concepts I'm excited about (Paper of the Future)
###########################################################

:author: C\. Titus Brown
:tags: futurepaper, futureshock
:date: 2017-01-09
:slug: 2017-pof-things-im-excited-abuot
:category: science

Note: This is the third post in a mini-series of blog posts inspired
by the workshop `Envisioning the Scientific Paper of the Future
<http://caltech.stacksdiscovery.org/scientific-paper-future>`__.

----

I've been struggling to put together an interesting talk for the
workshop, and last night Gail Clement (our host, `@Repositorian
<https://twitter.com/Repositorian>`__) and Justin Bois helped me
convinced myself (using red wine) that I should do something
other than present my vision for #futurepaper.

So, instead, here is a set of things that I'm pretty excited about in the
world of scholarly communication!

I've definitely left off a few, and I'd welcome pointers and commentary
to things I've missed; please comment!

----

1. The wonderful ongoing discussion around significance and reproducibility.
----------------------------------------------------------------------------

In addition to Victoria Stodden, Brian Nosek and John Ioannidis have
been leaders in banging various drums (and executing various research
agenda) that are showing us that we're not thinking very clearly about
issues fundamental to science.

For me, the blog post that really blew my mind was Dorothy Bishop's
`summary of the situation in psychology. <https://deevybee.blogspot.com/2016/03/there-is-reproducibility-crisis-in.html>`__ To quote:

   Nosek et al have demonstrated that much work in psychology is not
   reproducible in the everyday sense that if I try to repeat your
   experiment I can be confident of getting the same effect. Implicit
   in the critique by Gilbert et al is the notion that many studies
   are focused on effects that are both small and fragile, and so it
   is to be expected they will be hard to reproduce. They may well be
   right, but if so, the solution is not to deny we have a problem,
   but to recognize that under those circumstances there is an urgent
   need for our field to tackle the methodological issues of
   inadequate power and p-hacking, so we can distinguish genuine
   effects from false positives.

Read the whole thing. It's worth it.

Relevance to #futurepaper: detailed methods and exact repeatability is
a prerequisite for conversations about what we really care about, which
is: "is this effect real?"

2. Blogging as a way to explore issues without prior approval from Top People.
------------------------------------------------------------------------------

I've always hated authority ever since I noticed the propensity for
authorities to protect their position over seeking truth.  This
manifests in many ways, one of which through control over peer review
and scientific publishing processes.

With that in mind, it's worth reading up on Susan Fiske's
`"methodological terrorism" draft
<https://www.dropbox.com/s/9zubbn9fyi1xjcu/Fiske%20presidential%20guest%20column_APS%20Observer_copy-edited.pdf>`__,
in which Fiske, a professor at Princeton and an editor at PNAS,
"publicly compares some of her colleagues to terrorists" `(ref)
<http://nymag.com/scienceofus/2016/10/inside-psychologys-methodological-terrorism-debate.html>`__.
Fiske is basically upset that people are daring to critique published
papers via social media.

There are a bunch of great responses; I'll highlight just one,
by `Chris Chambers <https://neurochambers.blogspot.com/2016/09/methodological-terrorism-and-other-myths.html>`__:

   So what’s really going on here? The truth is that we are in the midst
   of a power struggle, and it’s not between Fiske’s “destructo-critics”
   and their victims, but between reformers who are trying desperately to
   improve science and a vanguard of traditionalists who, every so often,
   look down from their thrones to throw a log in the road. As the body
   count of failed replications continues to climb, a new generation want
   a different kind of science and they want it now. They're demanding
   greater transparency in research practices. They want to be rewarded
   for doing high quality research regardless of the results. They want
   researchers to be accountable for the quality of the work they produce
   and for the choices they make as public professionals. It's all very
   sensible, constructive, and in the public interest.

Yeah!

The long and short of it is that I'm really excited about how science
and the scientific process are being discussed openly via blogs and
Twitter.  (You can also read my `"Top 10 reasons why blog posts are
better than scientific papers
<http://ivory.idyll.org/blog/2017-top-ten-reasons-blog-posts.html>`__.)

Relevance to #futurepaper: there are many alternate "publishing" models
that offer advantages over our current publishing and dissemination system.
They also offer potential disadvantages, of course.

3. Open source as a model for open science.
-------------------------------------------

Two or three times every year I come back to `this wonderful chapter
by K. Jarrod Millman and Fernando Perez
<http://www.jarrodmillman.com/publications/millman2014developing.pdf>`__
entitled "Developing open source scientific practice."
This wonderful chapter breaks down all the ways in which current
computational science practice falls short of the mark and could learn
from standard open source software development practices.

For one quote (although the chapter offers far more!),

   Asking about reproducibility by the time a manuscript is ready for
   submission to a journal is too late: this problem must be tackled
   from the start, not as an afterthought tacked-on at publication
   time. We must therefore look for approaches that allow researchers
   to fluidly move back and forth between the above stages and that
   integrate naturally into their everyday practices of research,
   collaboration, and publishing, so that we can simultaneously
   address the technical and social aspects of this issue.

Please, go read it!

Relevance to #futurepaper: tools and processes prior to publication matter!

4. Computational narratives as the engine of collaborative data science.
------------------------------------------------------------------------

That's the title of `the most recent Project Jupyter grant application
<https://blog.jupyter.org/2015/07/07/project-jupyter-computational-narratives-as-the-engine-of-collaborative-data-science/>`__, authored by Fernando Perez
and Brian Granger (and `funded! <https://blog.jupyter.org/2015/07/07/jupyter-funding-2015/>`__).

It's hard to explain to people who haven't seen it, but the Jupyter
Notebook is the single most impactful thing to happen to the science
side of the data science ecosystem in the last decade.  Not content
with that, Fernando and Brian lay out a stunning vision for the future
of Jupyter Notebook and the software ecosystem around it.

Quote:

   the core problem we are trying to solve is the
   collaborative creation of reproducible computational narratives that can
   be used across a wide range of audiences and contexts.

The bit that grabs me the most in this grant proposal is the bit on
collaboration, but your mileage may vary - the whole thing is a great read!

Relevance to #futurepaper: hopefully obvious.

5. mybinder: deploy running Jupyter Notebooks from GitHub repos in Docker containers
------------------------------------------------------------------------------------

Another thing that I'm super excited about are the opportunities provided by
lightweight composition of many different services.  If you haven't seen
`binder (mybinder.org) <http://mybinder.org>`__, you should go play with it!

What binder does is let you spin up running Jupyter Notebooks based on the
contents of GitHub repositories.  Even cooler, you can install and configure
the execution environment however you want using Dockerfiles.

If this all sounds like gobbledygook to you, check out `this link
<http://mybinder.org/repo/minrk/ligo-binder/notebooks/GW150914_tutorial.ipynb>`__
to a binder for exploring the LIGO data.  Set up by Min Ragan-Kelly,
this link spools up an executable environment (in a Jupyter Notebook)
for exploring the LIGO data.  Single click, no fuss, no muss.

I find this exciting because binder is one example (of several!) where
people are building a new publication service by composing several
well-supported software packages.

Relevance to #futurepaper: ever wanted to give people a chance to play
with your publication's analysis pipeline as well as your data? Here
you go.

6. Overlay journals.
--------------------

As preprints grow, the question of "why do we have journals anyway?"
looms.  The trend of `overlay journals
<http://www.nature.com/news/open-journals-that-piggyback-on-arxiv-gather-momentum-1.19102>`__
provides a natural mixing point between preprints and more traditional
(and expensive) publishing.

An overlay journal is a journal that sits on top of a preprint server. To quote,

   “The only objection to just putting things on arXiv is that it’s
   not peer reviewed, so why not have a community-based effort that
   provides a peer-review service for the arXiv?" [Peter Coles] says —
   pointing out that academics already carry out peer review for
   scientific publishers, usually at no cost.

Relevance to #futurepaper: many publishers offer very little in the way of
services beyond this, so why pay them for it when the preprint server already
exists?

7. Bjorn Brembs.
----------------

Bjorn is one of these people that, if he were less nice, I'd find irritating
in his awesomeness.  He researches flies or something, and he consistently
pushes the boundaries of process in his publications.

Two examples -- `living figures
<http://www.nature.com/news/living-figures-make-their-debut-1.17382>`__
that integrate data from outside scientists, and `systematic openness
<http://bjoern.brembs.net/2016/12/why-did-the-moth-fly-into-the-flame/?utm_content=bufferaaac1&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer>`__ -
to `quote from Lenny Teytelman
<https://www.protocols.io/groups/protocolsio/news/a-shining-example-of-science-communication>`__,

   The paper was posted as a preprint prior to submission and all previous versions of the article are available as biorxiv preprints.
   The published research paper is open access.
   The raw data are available at figshare.
   All authors were listed with their ORCID IDs and all materials referenced with RRIDs.
   All methods are detailed with DOIs on  protocols.io.
   The blog post gives the history and context of the work. It's a fascinating and accessible read for non-fly scientists and non-scientists alike.
   Beautiful!

Bjorn also has a `wonderful paper <http://journal.frontiersin.org/article/10.3389/fnhum.2013.00291/full>`__ on just how bad the Impact Factor and journal status-seeking system is, and `his blog post on what a modern scholarly infrastructure should look like <http://bjoern.brembs.net/2015/04/what-should-a-modern-scientific-infrastructure-look-like/>`__ is worth reading.

Relevance to #futurepaper: hopefully obvious.

8. Idea futures or prediction markets.
--------------------------------------

There are other ways of reaching consensus than peer review, and `idea
futures <https://mason.gmu.edu/~rhanson/ideafutures.html>`__ are one
of the most fascinating.  To quote,

   Our policy-makers and media rely too much on the "expert"
   advice of a self-interested insider's club of pundits and big-shot
   academics. These pundits are rewarded too much for telling good
   stories, and for supporting each other, rather than for being
   "right". Instead, let us create betting markets on most
   controversial questions, and treat the current market odds as our
   best expert consensus. The real experts (maybe you), would then be
   rewarded for their contributions, while clueless pundits would
   learn to stay away. You should have a free-speech right to bet on
   political questions in policy markets, and we could even base a new
   form of government on idea futures.

Balaji Srinivasan `points out that the bitcoin blockchain is another
way of reaching consensus
<https://twitter.com/balajis/status/813393779142979584>`__, and I
think that's worth reading, too.

Relevance to #futurepaper: there are other ways of doing peer review and
reaching consensus than blocking publication until you agree with the paper.

9. Open peer review by a selected papers network.
-------------------------------------------------

`This proposal <http://journal.frontiersin.org/article/10.3389/fncom.2012.00001/full>`__ by Chris Lee, a friend and colleague at UCLA, outlines how to do peer review via (essentially) a blog chain. To quote,

   A selected-papers (SP) network is a network in which researchers
   who read, write, and review articles subscribe to each other based
   on common interests. Instead of reviewing a manuscript in secret
   for the Editor of a journal, each reviewer simply publishes his
   review (typically of a paper he wishes to recommend) to his SP
   network subscribers. Once the SP network reviewers complete their
   review decisions, the authors can invite any journal editor they
   want to consider these reviews and initial audience size, and make
   a publication decision. Since all impact assessment, reviews, and
   revisions are complete, this decision process should be short. I
   show how the SP network can provide a new way of measuring impact,
   catalyze the emergence of new subfields, and accelerate discovery
   in existing fields, by providing each reader a fine-grained filter
   for high-impact.

I think this is a nice concrete example of an alternate way to do peer
review that should actually work.

There's a lot of things that could tie into this, including trust
metrics; cryptographic signing of papers, reviews, and decisions so
that they are verifiable; verifiable computing a la `worldmake
<http://worldmake.org>`__; etc.

Relevance to #futurepaper? Whether or not you believe this could work,
figuring out why you think what you think is a good way to explore what
the publishing landscape *could* look like.

10. A call to arms: make outbreak research open access.
-------------------------------------------------------

What would you call a publishing ecosystem that actively encourages
withholding of information that could save lives, all in the name of
reputation building and job security?

Inhumane? Unethical? Just plain wrong?

All of that.

Read Yowziak, Schaffner, and Sabeti's article, `"Data sharing: make outbreak research open access. <http://www.nature.com/news/data-sharing-make-outbreak-research-open-access-1.16966>`__

There are horror stories galore about what bad data sharing does, but
one of the most affecting is in this `New Yorker article <http://www.newyorker.com/magazine/2014/07/21/one-of-a-kind-2>`__ by Seth Mnookin, in which he quotes `Daniel MacArthur <https://macarthurlab.org/people/>`__;

   The current academic publication system does patients an enormous disservice.

The larger context is that our failure to have and use good mechanisms
of data publication is killing people.  Maybe we should fix that?

Relevance to #futurepaper: open access to papers and data `and
software <ivory.idyll.org/blog/2017-data-implies-software.html>`__ is
critical to society.

----

Anyway, so that's what's on the tip of my brain this fine morning.

--titus
