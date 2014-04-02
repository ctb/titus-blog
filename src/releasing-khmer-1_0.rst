Announcing khmer 1.0
####################

:author: C\. Titus Brown
:tags: software,release,khmer
:date: 2014-04-01
:slug: releasing-khmer-1_0
:category: science

The khmer team is pleased to announce the release of khmer version 1.0.
khmer is our software for working efficiently with fixed length DNA
words, or k-mers, for research and work in computational biology.

Links:

* `khmer documentation <http://khmer.readthedocs.org/en/v1.0/>`__
* `PyPI link <https://pypi.python.org/pypi/khmer/1.0>`__
* `Announcement <https://github.com/ged-lab/khmer/releases/tag/v1.0>`__
* `ChangeLog <https://github.com/ged-lab/khmer/blob/v1.0/ChangeLog>`__
* `Citation handle <http://figshare.com/articles/The_khmer_software_package_enabling_efficient_sequence_analysis/979190>`__

khmer v1.0 is the culmination of about 9 months of development work by
Michael Crusoe (@biocrusoe).  Michael is the software engineer I hired
on `our NIH BIG DATA grant
<http://ivory.idyll.org/blog/the-future-of-khmer-2013-version.html>`__,
and he's spent at least half his time since being hired wrangling the
project into submission.

What is new?
~~~~~~~~~~~~

The last nine months has been a process+code extravaganza.  Here are
some of the things we did for 1.0, with an emphasis on the parts of
the *process* we changed:

1. Added continuous integration.  Thanks in part to a Rackspace VM,
   pull requests on github trigger builds and unit tests via Jenkins!

2. Moved to a `pull request model <http://scottchacon.com/2011/08/31/github-flow.html>`__ for development.

3. Instituted code reviews and `a development checklist <http://khmer.readthedocs.org/en/v0.8/development.html#checklist>`__.

4. Made khmer pip-installable.

5. Moved to a unified cross-platform build system.

6. Normalized our command line arguments and made the CLI documentation
   be auto-generated from the code.

7. Moved to `semantic versioning <http://semver.org/>`__.

8. Built a `Galaxy <http://galaxyproject.org/>`__ interface.

9. Added code coverage analysis of both C++ and Python code to our continuous integration system.

10. Introduced a `CITATION file <https://github.com/ged-lab/khmer/blob/master/CITATION>`__ and modified the scripts to output citation information.

11. Wrote a `citation handle <http://figshare.com/articles/The_khmer_software_package_enabling_efficient_sequence_analysis/979190>`__ for the software.

12. Built better user-focused documentation.

13. Starting using parts of `the khmer protocols <bttp://khmer-protocols.readthedocs.org>`__ for acceptance testing.

Why did we do all this work!?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The short answer is, we like it when our software works.  khmer is
becoming increasingly broadly used, and it would be good if the
software were to continue working.

A slightly longer answer is that we are continuing to improve khmer --
we're making it faster, stronger, and better -- while we're *also* doing
research with it.  We want to make sure that the old stuff keeps working
even as we add new stuff.

But it's not just that.  There are now about five people working on
fixing, improving, and extending khmer -- several of them are graduate
students, working on kick-ass new functionality as part of their PhDs.
By having testing infrastructure that better ensures the stability and
reliability of our software, each graduate student can work out on their
own long branch of functionality, and -- when they're ready -- they can
merge their functionality back into the stable core, and we can all take
advantage of it.

Actually, it's even more.  **We're building an edifice here, and we
need to have a stable foundation**.  One very important addition that
just came last weekend was the addition of khmer `acceptance testing
<http://en.wikipedia.org/wiki/Acceptance_testing>`__ -- making sure
that khmer not only works as we expect it to, but integrates with
other tools.  For this, we turned to `the khmer protocols
<http://ivory.idyll.org/blog/announcing-khmer-protocols.html>`__, our
nascent effort to build open, integrated pipelines for certain kinds of
sequence analysis.

Our acceptance testing consists of running from raw data through the
assembly stage of the Eel Pond mRNAseq assembly protocol, albeit with
a carefully chosen data subset.  This takes less than an hour to
run, but in that hour it tests some of the core functionality of
khmer *at the command line*, *on real data*.  We hope to extend this
into the majority of our functionality over time -- for now we're
mostly just testing digital normalization and read manipulation.

Having passing acceptance tests before a major release is both
extraordinarily reassuring and quite useful: in fact, it caught
several last minute bugs that we'd missed because of either incomplete
unit and functional tests, OR because they were bugs at the integration
level and not at the unit/functional level.

And one interesting side note -- our acceptance tests encompass Trimmomatic,
fastx, and Trinity.  That's right, we're passively-aggressively testing other
people's software in our acceptance tests, too ;).

Better Science Through Superior Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ultimately, this improved infrastructure and process lets us confidently
move forward with new features in khmer, lets my group work in concert
on orthogonal new features, enables larger processes and pipelines
with less fear, uncertainty, and doubt, and -- ultimately -- should
result in significant time savings as extend our research program.  My
firm belief is that this will allow us to do better science as we move
forward.

Watch This Space.  We'll let you know how it goes.

--titus
