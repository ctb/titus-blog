Notes from "How to grow a sustainable software development process (for scientific software)"
#############################################################################################

:author: C\. Titus Brown
:tags: science
:date: 2015-06-12
:slug: 2015-growing-sustainable-software-development-process
:category: science

I gave a presentation at the BEACON Center's coding group this past
Monday; here are my notes and followup links.  Thanks to Luiz Irber
for scribing!

----

My short slideshow: `here
<http://www.slideshare.net/c.titus.brown/2015-msucodereview>`__

The `khmer project <https://github.com/dib-lab/khmer>`__ is on github,
and `we have a tutorial for people who want to try out our development
process
<http://khmer.readthedocs.org/en/latest/dev/getting-started.html>`__.
khmer has ~5-10 active developers and has had ~60 contributors overall.

Growing a development process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

How can you grow a process that meets your needs?

* use version control and develop on branches;
* create a checklist to use when merging branches into master;
* follow the checklist!

(For more checklist motivation, see `The Checklist Manifesto
<http://www.amazon.com/The-Checklist-Manifesto-Things-Right/dp/0312430000>`__
by Atul Gawande.)

We do the above as part of our `GitHub flow-based development approach <https://guides.github.com/introduction/flow/>`__.

**tl;dr? Grow your checklist slowly, but make everyone adhere to it.**

What goes on your checklist?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ideas for things that could go on your checklist:

* I ran the tests and they passed!
* Someone else ran the tests and they passed!
* A computer ran the tests automatically and they passed! `(Continuous Integration) <https://en.wikipedia.org/wiki/Continuous_integration>`__
* The code formatting guidelines are met.  (> 2 people with different coding styles? CHAOS.)
* The code coverage guidelines are met.
* A spellchecker was run.
* Changes were described in a `ChangeLog <https://en.wikipedia.org/wiki/Changelog>`__.
* Commit messages make sense.
* Code coverage didn't decrease.
* Checks on specific types of features ("Script parameters should be documented").

I also strongly suggest a two-person merge rule (the primary developer
of a feature *can not* merge that feature); this helps ensure the
checklist is followed :)

You can see our checklist for khmer `here
<http://khmer.readthedocs.org/en/latest/dev/coding-guidelines-and-review.html>`__.

---

It's important to make the checklist as lightweight as possible, and
making sure it addresses useful "pain points" in your developer
process; there's a line where people start ignoring the checklist
because there's less direct value.

There's no reason to start heavy; you can grow your checklist slowly,
as your project accrues experience and developers turn over.

---

Development process goals
~~~~~~~~~~~~~~~~~~~~~~~~~

Add features quickly (by using branches) while keeping technical debt
manageable!

The concept of `technical debt
<https://en.wikipedia.org/wiki/Technical_debt>`__ is key - if you let
cruft accrue in your codebase, eventually your entire codebase will become
unmaintainable and unmanageable.

Other useful links:

* the `Software Sustainability Institute's evaluation checklist
  <http://www.software.ac.uk/online-sustainability-evaluation>`__ can
  be a helpful way to assess your project.

* There are several sites for hosting documentation that
  automatically update from your version control repo; we use
  `ReadTheDocs <http://www.readthedocs.org>`__.

* Targeting code to test is easily done by first looking for
  code that is not executed by your tests, using `code coverage <https://en.wikipedia.org/wiki/Code_coverage>`__.

* The `Bus factor <https://en.wikipedia.org/wiki/Bus_factor>`__ is a measure
  of how well documented your various processes are.

* The paper `Best practices for scientific computing
  <http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745>`__
  is a good overview of things to think about.

* A good overview of our rationale for and experience with adopting these
  techniques is `here
  <http://files.figshare.com/1209108/wssspe13_ged.pdf>`__.

* We continually self-assess the value of our development process and
  modify it accordingly; see, for example, `some recent modifications
  <http://ivory.idyll.org/blog/2015-modifying-our-dev-process.html>`__.

--titus
