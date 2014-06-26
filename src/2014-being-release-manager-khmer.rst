Being a release manager for khmer
#################################

:author: C\. Titus Brown
:tags: khmer
:date: 2014-06-17
:slug: 2014-being-release-manager-khmer
:category: science

We just released `khmer v1.1
<https://github.com/ged-lab/khmer/releases/tag/v1.1>`__, a minor
version update from `khmer v1.0.1
<https://github.com/ged-lab/khmer/releases/tag/v1.0.1>`__ (minor
version update: `220 commits, 370 files changed
<https://github.com/ged-lab/khmer/compare/v1.0.1-docsupdate...v1.1>`__).

Cancel that -- _I_ just released khmer, because I'm the release
manager for v1.1!

As part of an effort to find holes in our documentation, "surface" any
problematic assumptions we're making, and generally increase the `bus
factor <http://en.wikipedia.org/wiki/Bus_factor>`__ of the khmer
project, we have been switching up the release manager for every 1.0+
release.  The first release manager (for v1.0) was Michael Crusoe
(`@biocrusoe <https://twitter.com/biocrusoe>`__); the second (for
v1.0.1) was (`@luizirber <https://twitter.com/luizirber>`__); and I'm
the third, for v1.1.

Each time through, we make our `release process docs
<http://khmer.readthedocs.org/en/v1.1/release.html>`__ more explicit
and more correct.  There's really no better way to do it; each RM
comes with a different background and a different skillset, so by the
time four or five people have cut a release, we should have ironed out
any wrinkles.

Roughly speaking, our release process consists of:

#. Building a release candidate

#. Testing the release candidate in multiple ways using virtualenvs on
   a Linux box.

#. Pushing to the `test PyPI server
   <https://wiki.python.org/moin/TestPyPI>`__ and doing install tests in a
   virtualenv.

#. Doing multi-system tests on `the BaTLab <https://www.batlab.org>`__, and
   running our acceptance tests on Amazon Web Services.

#. If that all passes for a release candidate, cutting the final release!

There are about a dozen steps in all, with 40-50 command line
steps. It's a bit complicated but it's all codified in a `somewhat
cockamamie semi-automated copy-and-paste doc
<http://khmer.readthedocs.org/en/v1.1/release.html>`__ that actually
works pretty well.

For me, the big challenge was getting the `BaTLab
<https://www.batlab.org/>`__ multi-platform install tests to run; this
required about 30 minutes of handholding by Michael.  Once they ran we
discovered a few problems, the biggest of which was a breakage of
Python 2.6 compatibility -- which we simply wouldn't have found otherwise.


For the next release manager, the challenge will be to get through the
acceptance tests; for v1.1, we added acceptance tests based on our
metagenome protocol, so we now test about 90% of our software's
command line interface on *real data* before releasing it.  But since
I'm the person in charge of the acceptance testing system, there are a
few tricks and tips that I haven't completely codified, so I'll have
to work on pushing those out the door.

The main lesson I've learned from all of this is that you catch *a
lot* more bugs with all this testing than you would any other way.  It
will hopefully result in a more pleasant user experience as people
find fewer and fewer "dumb" bugs, and it certainly is giving us more
confidence in our software processes' robustness as we contemplate
some bigger changes to khmer down the line.

Something that's also rather exciting is that we have three people who
aren't part of the lab contributing code -- `@chuckpr
<http://github.com/chuckpr>`__, `@accaldwell
<http://github.com/accaldwell>`__, and `@znruss
<http://github.com/znruss>`__.  As our process becomes more explicit,
I think we're attracting people who want to contribute but (6 months
ago) wouldn't have known how.

What's up next on the khmer timeline?  We're participating in `the
July Mozilla Science Labs hackathon
<http://software-carpentry.org/blog/2014/06/update-on-sprint-plans.html>`__
by offering a `khmer contributathon
<http://ivory.idyll.org/blog/2014-khmer-hackathon.html>`__ so people
can try out our workflow, and we're `going to revamp the docs for that
<https://github.com/ged-lab/khmer/issues/440>`__.  We'll let you know
how it goes.

--titus
