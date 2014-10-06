What are our requirements for working with other software projects?
###################################################################

:author: C\. Titus Brown
:tags: software,dddd,ddd
:date: 2014-10-06
:slug: 2014-software-process-requirements
:category: science

As part of my `Moore-funded work
<http://ivory.idyll.org/blog/2014-moore-ddd-talk.html>`__, we expect
to be embarking on some software integration (more about that later).
This means working with other people's software packages at or beneath
their command-line API.  More importantly, we'll be auditioning
packages that will receive the, ahem, benefit of our contributions --
any serious integration project will necessarily lead to evolution on
both sides of any partnership, and in the standard open source way,
we'd expect to facilitate that with pull requests or patches.

So... what should we look for in a dance partner?

The strong position is this: we look for a reasonably stable,
well-developed project.  Here, Michael Crusoe suggested looking
through the `Software Sustainability Institute Criteria Based
Assessment <http://www.software.ac.uk/software-evaluation-guide>`__.
So something like the following criteria might be good criteria:

* your test coverage is measured regularly and is high (~80-90%);

* you use a version control system, and it is publicly readable;

* there's an official and reasonably well-used support channel;

* there's a reasonably active user community;

* there's a release checklist;

In practice, this is likely to be pretty limiting.  I don't know how many
bioinformatics projects could meet every item on this checklist, but it's
probably not more than a handful.

A weaker starting position might be:

* you have a versioning policy, and at least one of the major public
  interfaces is under semantic versioning@;

* you have a patch & contributor policy and a functioning code review workflow to merge in contributions;

* you have automated tests that others can run successfully;

Other things to consider, for academic projects:

* there's either an active multi-lab developer community, or the project
  has 2+ years of funding remaining;

* there's an end of life plan that doesn't depend on continued
  funding;

But why?
--------

Here we are coming in and saying we'd love to make use of your nice
software, but we have the following requirements first. Isn't this
being rather demanding of us?!

Probably.  But flip the perspective.

First of all, most of the requirements above are basic requirements
for actually functioning code -- go see `my post on software reuse
<http://ivory.idyll.org/blog/research-software-reuse.html>`__, section
"Bad code is often wrong code."  If you aren't meeting the minimal
requirements of version control, testing, and some version stability,
your code is likely to be broken already.

Second, we're not talking about just using these other projects, we're
talking about *integrating* with them.  Meeting the process
requirements above means that you actually *have* a minimally sane
development process.  If we must patch your software, and you have no
way to give us feedback and help us reconcile with your own
development plans, then we are going to end up forking (and
supporting) some version of your software; I don't want to get
into that game.

Third, if your project is virtually guaranteed to vanish in a year
(e.g.  with your funding), I think it would be a bad idea to build on it.

[ ... ] something pithy here.

--titus
