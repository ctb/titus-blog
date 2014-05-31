Some myths of reproducible computational research
#################################################

:author: C\. Titus Brown
:tags: reproducibility,rants
:date: 2014-05-31
:slug: 2014-myths-of-computational-reproducibility
:category: science

About 10 days ago, I gave a talk in Manchester to Carole Goble's
group, hosted by Aleksandra Pawlik.  The talk title was "Six ways to
Sunday: Approaches to computational reproducibility in non-model
sequence analysis."  I've posted the slides `(here)
<http://www.slideshare.net/c.titus.brown/2014-manchesterreproducibility>`__.

For the talk, I put together a list of five things that I felt were "myths" of
reproducible computational research: attitudes that wrongly
discouraged people from actually *doing* computational research
reproducibly.  I thought it was worth reproducing them below with a bit
of discussion.

Myth 1: Partial reproducibility is hard
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Some people seem wary of the mountain of work that any true attempt at
reproducible computational science must entail, and so they don't want
any part of it.

Bah!

Start small; it's easy. Let me tell you: *anything* you do --
providing the raw data, posting any small scripts, detailing the
versions of programs you used together with their parameters -- will
be tremendously welcome to anyone trying to validate or build off your
paper.  This includes you yourself, in 2 years.

Myth 2: Incomplete reproducibility is useless
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

20% or 50% or 60% or 80% is all better than 0%.  Sure, 100% is better
than 80%, but it might be a lot more work to get to 100% rather than
80%, so why not start small and target something that seems achievable
first?  (It's OK, I give you permission!)

In practice, *anything you do* will be useful.  (See #1.)

Myth 3: We need new platforms for reproducible computational science
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Engineers like building stuff. It sure is easier (and hence more fun,
at least in the short term) than doing science.  But what we need
right now is *scientists actually using stuff that already exists*, not
*engineers building new stuff that no one will ever use.*

Every year at PyCon there's a fresh, new batch of eager young
programmers who are interested in Open Science.  Awesome!  But they
seem to spend a lot of time talking about how new software is needed.
My message to them? However glamorous it may seem at first to build
something new, you're wasting your time.  Go help some scientists use
existing software, instead.

Also: to a first approximation, IPython Notebook and knitr have won.
Sure, they may not be everything you want or feel is needed, but
they've hardly got any market penetration in science yet.  I submit
that you are more likely to make a difference by actually _using_
something imperfect than you are by trying to build something perfect.
If, after you publish a paper or two and have some use cases that
aren't met by existing tools, I will enthusiastically endorse you
writing a new tool :).

Myth 4: Virtual machines solve the reproducibility problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Maybe they do, but not usefully so.

Look, VMs are just giant black boxes.  Your VM could be a giant lookup
table that doesn't implement any actual methods but just regurgitates
already calculated results.  No one would be able to tell -- you're
just providing an interface to something, right?  But is that really useful
in helping people understand what it is you did, replicating it on their
own, or reusing and remixing it?  No, not at all.

And yes, I've made this argument `before
<http://ivory.idyll.org/blog/vms-considered-harmful.html>`__.  Bill
even says that he sorta agrees with me now.

Myth 5: GUIs are the way to go, because scientists might actually *use* easy-to-use software.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bioinformaticians like the idea of Galaxy (just to pick on one that I
actually kinda like ;) because they think that it will make it easy for
biologists to do computation.  And hey, look, you get reproducibility for
free!

Unfortunately, at least in the area of bioinformatics I work in, things
change so rapidly that the GUIs don't keep up.  By the time it's in a GUI,
it's rarely still very cutting edge, which doesn't fit well with most
research that I see being done.

But there's a bigger problem: almost all data analysis steps take
place in a larger pipeline.  The GUI has to wrap the *entire* pipeline,
or else be scriptable in order to fit in; otherwise, it actually
presents an *obstacle* to reproducibility, because you have to capture
its parameters somewhere else.

Galaxy is a decent compromise: it is a GUI, that provides access to
cloud resources; it wraps command lines, so you can pretty quickly
integrate the latest thing; and reproducibility comes "for free".
But (like all the other GUIs I've seen) it's pretty limiting in terms
of what you can wrap with it.


Less talk, more work
~~~~~~~~~~~~~~~~~~~~

At the end of the day, my lab's experience is this: you don't need
much in the way of "magic sauce" to get started doing things
reproducibly.  You need a little bit of experience or training (cue
`Software Carpentry <http://software-carpentry.org>`__), and a little
bit of elbow grease the first time around, but it's just not that hard
to get started and make your research life better.

Fundamentally, my lab now does this stuff 'cause it makes everything
easier.  Automation reduces our maintenance burden; explicit workflows
built for extensibility make paper revisions much easier; explicit
instructions are good for training students.  At this point I feel
like we're moving clearly into the "virtuous cycle" stage, where the
positive feedback of doing everything like this turns us into
unstoppable borg-like computational scientists.  We'll let you know
how that goes.

--titus
