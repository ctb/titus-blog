Is software a primary product of science?
#########################################

:author: C\. Titus Brown
:tags: sustainability, software citation
:date: 2015-04-22
:slug: 2015-software-as-a-primary-product-of-science
:category: science

**Update** - I've written Yet Another blog post, `More on scientific
software <http://ivory.idyll.org/blog/2015-more-on-software.html>`__
on this topic.  I think this blog post is a mess so you should read
that one first ;).

----

This blog post was spurred by `a simple question from Pauline Barmby
on Twitter <https://twitter.com/PBarmby/status/590850156804833281>`__.
My response didn't, ahem, quite fit in 144 characters :).

----

First, a little story.  (To paraphrase Greg Wilson, "I tell a lot of
stories.  Some of them aren't true. But this one is!")

When we were done writing `Best Practices for Scientific Computing
<http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745>`__,
we tried submitting it to a different high-profile journal than the
one that ultimately accepted it (PLoS Biology, where it went on to
become `the most highly read article of 2014 in PLoS Biology
<http://blogs.plos.org/biologue/2015/03/02/metrics-and-impact-looking-beyond-research-articles/>`__).
The response from the editor went something like this: "We recognize
the importance of good engineering, but we regard writing software as
equivalent to building a telescope - it's important to do it right,
but we don't regard a process paper on how to build telescopes better
as an intellectual contribution."  (Disclaimer: I can't find the
actual response, so this is a paraphrase, but it was definitely a "no"
and for about that reason.)

Is scientific software like instrumentation?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When I think about scientific software as a part of science, I
inevitably start with its similarities to building scientific
instruments.  New instrumentation and methods are absolutely essential
to scientific progress, and it is clear that good engineering and
methods development skills are incredibly helpful in research.

So, why did the editors at High Profile Journal bounce our paper?  
I infer that they drew exactly this parallel and thought no further.

But scientific software is only somewhat like new methods or
instrumentation.

First, software can spread *much* faster and be used much more like a
black box than most methods, and instrumentation inevitably involves
either construction or companies that act as middlemen.  With
software, it's like you're shipping *kits* or plans for 3-D printing -
something that is as close to immediately usable as it comes.  If
you're going to hand someone an immediately usable black box (and
pitch it as such), I would argue that you should take a bit more
care in building said black box.

Second, complexity in software scales *much* faster than in hardware
(citation needed).  This is partly due to human nature & a failure to
think long-term, and partly due to the nature of software - software
can quickly have many more moving parts than hardware, and at much
less (short term) cost.  Frankly, most software stacks resemble
massive `Rube Goldberg machines
<http://dtrace.org/blogs/wesolows/2014/12/29/fin/>`__ (read that
link!)  This means that different processes are needed here.

Third, at least in my field (biology), we are undergoing a transition
to data intensive research, and software methods are becoming ever
more important.  There's no question that software is going to eat
biology just like `it's eating the rest of the world
<http://www.wired.com/2012/04/ff_andreessen/5/>`__, and an
increasingly large part of our primary scientific output in biology is
going to hinge directly on computation (think: annotations. 'nuff
said).

If we're going to build massively complex black boxes that under-pin
all of our science, surely that means that the *process* is worth
studying intellectually?

Is scientific software a primary intellectual output of science?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No.

I think concluding that it is is an example of the logical fallacy
`"affirming the consequent"
<http://en.wikipedia.org/wiki/Affirming_the_consequent>`__ - or,
"confusion of necessity and sufficiency".  I'm not a logician, but I
would phrase it like this (better phrasing welcome!) --

   Good software is necessary for good science. Good science is an
   intellectual contribution.  Therefore good software is an intellectual
   contribution.

Hopefully when phrased that way it's clear that it's nonsense.

I'm naming this "the fallacy of grad student hackers", because
I feel like it's a common failure mode of grad students that are good
at programming.  I actually think it's a tremendously dangerous idea
that is confounding a lot of the discussion around software contributions
in science.

To illustrate this, I'll draw the analog to experimental labs: you may
have people who are tremendously good at doing certain kinds of
experiments (e.g. expert cloners, or PCR wizards, or micro-injection
aficionados, or WMISH bravados) and with whom you can collaborate to
rapidly advance your research.  They can do things that you can't, and
they can do them quickly and well!  But these people often face dead
ends in academia and end up as `eterna-postdocs
<http://www.nature.com/news/wanted-staff-scientist-positions-for-postdocs-1.17303>`__,
because (for better or for worse) what is valued for first authorship
and career progression is intellectual contribution, and doing
experiments well is not sufficient to demonstrate an intellectual
contribution.  Very few people get career advancement in science by
simply being very good at a technique, and I believe that this is OK.

Back to software - writing software may become necessary for much of
science but I don't think it should ever be sufficient as a primary
contribution.  Worse, it can become (often becomes?) an engine of
procrastination. Admittedly, that procrastination `leads to things
like IPython Notebook
<http://blog.fperez.org/2012/01/ipython-notebook-historical.html>`__,
so I don't want to ding it, but neither are all (or even most ;) grad
students like Fernando Perez, either.

Let's admit it, I'm just confused
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This leaves us with a conundrum.

Software is clearly a force multiplier - `"better software, better
research!
<http://www.software.ac.uk/blog/2014-01-23-spread-word-better-software-better-research?mpw>`__.

However, I don't think it can be considered a primary output of
science.  Dan Katz said, `"Nobel prizes have been given for inventing
instruments. I'm eagerly awaiting for one for inventing software
[sic]" <https://twitter.com/danielskatz/status/590855359033651200>`__
-- but I think he's wrong. Nobels have been given because of the
insight enabled by inventing instruments, not for inventing
instruments. (Corrections welcome!)  So while I, too, eagerly await
the explicit recognition that software can push scientific insight
forward in biology, I am not holding my breath - I think it's going to
look much more like `the 2013 Chemistry Nobel
<http://www.nobelprize.org/nobel_prizes/chemistry/laureates/2013/press.html>`__,
which is about general computational methodology.  (My money here
would be on a Nobel in Medicine for genome assembly methods, which
should follow on separately from massively parallel sequencing methods
and shotgun sequencing - maybe Venter, Church, and Myers/Pevzner
deserve three different Nobels?)

Despite that, we do need to incentivize it, especially in biology but
also more generally.  Sean Eddy wrote `AN AWESOME BLOG POST ON THIS
TOPIC <http://selab.janelia.org/people/eddys/blog/?p=313>`__ in 2010
(all caps because IT'S AWESOME AND WHY HAVEN'T WE MOVED FURTHER ON
THIS <sob>).  This is where DOIs for software usually come into play -
hey, maybe we can make an analogy between software and papers! But I
worry that this is a flawed analogy (for reasons outlined above) and
will simply support the wrong idea that doing good hacking is
sufficient for good science.

We also have a new problem - the so-called `Big Data Brain Drain
<https://jakevdp.github.io/blog/2013/10/26/big-data-brain-drain/>`__,
in which it turns out that the skills that are needed for advancing
science are also tremendously valuable in much more highly paid jobs
-- much like physics number crunchers moving to finance, research
professors in biology face a future where all our grad students go on
to make more than us in tech.  (Admittedly, this is only a problem if
we think that more people clicking on ads is more important than basic
research.) Jake Vanderplas (the author of the Big Data Brain Drain
post) addressed potential solutions to this in `Hacking Academia
<https://jakevdp.github.io/blog/2014/08/22/hacking-academia/>`__,
about which I have mixed feelings. While I love both Jake
and his blog post (platonically), there's a bit too much magical
thinking in that post -- I don't see (m)any of those solutions getting
much traction in academia.

The bottom line for me is that we need to figure it out, but I'm a bit
stuck on practical suggestions.  Natural selection may apply --
whoever figures this out in biology (basic research institutions
and/or funding bodies) will have quite an edge in advancing
biomedicine -- but natural selection works across multiple
generations, and I could wish for something a bit faster.  But I don't
know.  Maybe I'll bring it up at SciFoo this year - "Q: how can we
kill off the old academic system faster?" :)

I'll leave you with two little stories.

The problem, illustrated
~~~~~~~~~~~~~~~~~~~~~~~~

In 2009, we started working on what would ultimately become `Pell et
al., 2012 <http://www.pnas.org/content/109/33/13272.full>`__.  We
developed a metric shit-ton of software (that's a scientific measure,
folks) that included some pretty awesomely scalable sparse graph
labeling approaches.  The software worked OK for our problem, but was
pretty brittle; I'm not sure whether or not our implementation of this
partitioning approach is being used by anyone else, nor am I sure if it
should be :).

However, the paper has been a pretty big hit by traditional scientific
metrics!  We got it into PNAS by talking about the data structure
properties and linking physics, computer science, and biology
together.  It helped lead directly to `Chikhi and Rizk (2013)
<http://www.almob.org/content/8/1/22>`__, and it has been cited a
whole bunch of times for (I think) its theoretical contributions.  Yay!

Nonetheless, the incredibly important and tricky details of scalably
partitioning 10 bn node graphs were lost from that paper, and the
software was not a big player, either.  Meanwhile, Dr. Pell left
academia and moved on to a big software company where (on his first
day) he was earning quite a bit more than me (good on him! I'd like a
5% tithe, though, in the future :) :).  Trust me when I say that this
is a net loss to academia.

Summary: good theory, useful ideas, lousy software. Traditional success.
Lousy outcomes.

A contrapositive
~~~~~~~~~~~~~~~~

In 2011, we figured out that linear compression ratios for sequence
data simply weren't going to cut it in the face of the continued rate
of data generation, and we developed `digital normalization
<http://arxiv.org/abs/1203.4802>`__, a deceptively simple idea that
hasn't really been picked up by the theoreticians.  Unlike the Pell
work above, it's not theoretically well studied at all. Nonetheless,
the preprint has a few dozen citations (because it's so darn useful)
and the work `is proving to be a good foundation for further research
for our lab <https://peerj.com/preprints/890/>`__.  Perhaps the truest
measure of its memetic success is that it's been reimplemented by at
least three different sequencing centers.

The software is highly used, I think, and many of our efforts on the
`khmer software <http://github.com/ged-lab/khmer>`__ have been aimed
at making diginorm and downstream concepts more robust.

Summary: lousy theory, useful ideas, good software. Nontraditional
success. Awesome outcomes.

Ways forward?
~~~~~~~~~~~~~

I simply don't know how to chart a course forward.  My current
instinct (see below) is to shift our current focus much more to theory
and ideas and further away from software, largely because I simply
don't see how to publish or fund "boring" things like software
development.  (Josh Bloom has `an excellent blog post that relates to
this particular issue: Novelty Squared
<https://medium.com/@profjsb/novelty-squared-dd88857f662>`__)

I've been obsessing over these topics of software and scientific focus
recently (see `The three porridge bowls of scientific software
development
<http://ivory.idyll.org/blog/2015-on-sustainable-scientific-software.html>`__
and `Please destroy this software after publication. kthxbye
<http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__)
because I'm starting to write a renewal for `khmer's funding
<http://ivory.idyll.org/blog/the-future-of-khmer-2013-version.html>`__.
My preliminary specific aims look something like this:

Aim 1: Expand low memory and streaming approaches for biological sequence analysis.

Aim 2: Develop graph-based approaches for analyzing genomic variation.

Aim 3: Optimize and extend a general purpose graph analysis library

Importantly, **everything to do with software maintenance, support,
and optimization is in Aim 3** and is in fact only a part of that aim.
I'm not actually saddened by that, because I believe that software is
only interesting because of the new science it enables.  So I need to
sell *that* to the NIH, and there software quality is (at best) a
secondary consideration.

On the flip side, by my estimate **75% of our khmer funding is going
to software maintenance**, most significantly in paying down `our
technical debt <http://en.wikipedia.org/wiki/Technical_debt>`__.  (In
the grant I am proposing to decrease this to ~50%.)

I'm having trouble justifying this dichotomy mentally myself, and I can
only imagine what the reviewers might think (although hopefully they
will only glance at the budget ;).

So this highlights one conundrum: given my estimates and my
priorities, how would you suggest I square these stated priorities
with my funding allocations?  And, in these matters, have I been wrong
to focus on software quality, or should I have focused instead on
accruing technical debt in the service of novel ideas and
functionality?  Inquiring minds want to know.

--titus
