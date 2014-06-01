A khmer mini-Hackathon: Introducing scientists to testing and code review
#########################################################################

:author: C\. Titus Brown
:tags: khmer, open science
:date: 2014-06-01
:slug: 2014-khmer-hackathon
:category: science

As part of the 2-day `Mozilla Science Labs hackathon
<http://software-carpentry.org/blog/2014/05/multisite-sprint-in-july.html>`__
in late July, the `khmer project <http://github.com/ged-lab/khmer/>`__
will be providing a "mentored open source contributathon" experience.
This will provide an opportunity for people interested in trying out
our instance of the `"github flow"
<http://scottchacon.com/2011/08/31/github-flow.html>`__ model, in
which contributions are submitted for review using a pull request.
Since our project has lots of unit tests and fairly high code
coverage, people can also see how testing and code coverage interact
with software development in practice.

The basic idea is this:

1. We will provide a list of low-hanging fruit in the khmer issues
   list `(so far, 21 issues, but we will expand)
   <https://github.com/ged-lab/khmer/issues?direction=desc&labels=low-hanging-fruit&page=1&sort=updated&state=open>`__).

2. Interested parties will come, pick an issue, claim it on the issue
   tracker, create a pull request (PR) on github, make the changes, and
   go through our development process.

3. Once the PR is ready for review, we will review it according to our
   `development guidelines
   <http://khmer.readthedocs.org/en/v1.0.1/development.html>`__ and
   make sure it passes the various style checks, code coverage
   analysis, multi-platform continuous integration, and all the rest.

4. If it doesn't, we will pass it back to the contributor for revision.
   If it does, we will merge into our master branch.

5. Throughout this period, I and other people from the team will be
   available for one-on-one Skype/Hangout/IRC to help steer
   people through the contribution workflow.

For the two days of the hackathon, we will be focused on providing
quick turn around times on review and helping people work through
technical and conceptual problems.

How do I participate?
~~~~~~~~~~~~~~~~~~~~~

Go to https://github.com/ged-lab/khmer/issues/446 and click on
'subscribe' (lower right, under Notifications) -- as the time
gets closer, we'll put new information there.

Why would I want to do this?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mentored open source software development experiences are a bit hard to
come by, especially if you're a scientist who doesn't have time to do
a Google Summer of Code.  We're scientists, we're programmers, and
we're friendly; come play!

More specifically, there are a lot of minor technical bits to doing
software development on a project.  We'd love to help you past them.

Oh, and if you successfully get merged into khmer, we'll put you down
as a contributor and make you an author on the next khmer software paper.
So, uh, fame?

What do I need to know in order to participate?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You should have been through a Software Carpentry bootcamp, and/or
know some basic git.  You'll need to be able to log in to a Linux box
with ssh; if you don't have a Linux account, we can provide one.
You'll need to know a little bit of programming, and be able to figure
out a bit more (although I expect many of our low hanging fruit issues
will be documentation and testing).

What's in it for the khmer team?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A bunch of things! We like teaching and training. Contributions are
always welcome. Maybe we can do some good. And we ourselves will get a
chance to focus on khmer a bit, too.

I think one very specific outcome will be a much improved (battle
tested!) contributor's guide to our project, which will be welcome.

We'll be running a local version at MSU for people in the lab and down
the hall, which is probably good for training.

--titus
