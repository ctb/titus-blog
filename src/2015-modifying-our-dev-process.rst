Modifications to our development process
########################################

:author: C\. Titus Brown
:tags: khmer
:date: 2015-05-14
:slug: 2015-modifying-our-dev-process
:category: science

After a fair amount of time thinking about software's place in science
(see blog posts `1
<http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__,
`2
<http://ivory.idyll.org/blog/2015-on-sustainable-scientific-software.html>`__,
`3
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html>`__,
and `4 <http://ivory.idyll.org/blog/2015-more-on-software.html>`__),
and thinking about `khmer's <http://github.com/ged-lab/khmer>`__
short- and long-term future, we're making some changes to our development
process.

**Semantic versioning**: The first change, and most visible one, is
that we are going to start bumping version numbers a lot faster.  One
of the first things Michael Crusoe put in place was `semantic
versioning <http://en.wikipedia.org/wiki/Software_versioning>`__,
which places certain compatibility guarantees on version numbers used.
These compatibility guarantees (on the command line API only, for
khmer) are starting to hold us back from sanding down the corners.
Moving forward, we're going to bump version numbers as quickly as
needed for the code we've merged, rather than holding off on cleanup.

Michael `just released khmer v1.4
<https://github.com/ged-lab/khmer/releases/tag/v1.4>`__; my guess is
that 2.0 will follow soon after.  We'll try to batch major versions a
little bit, but when in doubt we'll push forward rather than holding
back, I think.  We'll see how it goes.

**Improving the command-line user experience.** At the same time,
we're going to be focusing more on user experience issues; see `#988
for an example <https://github.com/ged-lab/khmer/issues/988>`__.
`Tamer Mansour <https://twitter.com/DrTamerMansour>`__, one of my new
postdocs at Davis, took a fresh look at the command line and argued
strenuously for a number of changes, and this aligns pretty well with
our interests.

**Giving more people explicit merge authority.** 'til now, it was mostly
Michael and myself doing merges; we've asked `Luiz Irber
<https://twitter.com/luizirber>`__ and `Camille Scott
<https://twitter.com/camille_codon>`__ to step up and do not only code
review but merges on their own recognizance.  This should free up
Michael to focus more on coding, as well as speeding up response times
when Michael and I are both busy or traveling.  I'm also asking
mergers to fix minor formatting issues and update the ChangeLog for
pull requests that are otherwise good - this will accelerate the pace
of change and decrease frustration around quick fixes.

This is part of my long-term plan to involve more of the lab in
software engineering.  Most experimental labs have lab duties for grad
students and postdocs; I'd like to try out the model where the grad
students and postdocs have software engineering duties, independent
of their research.

**Deferring long-term plans and deprecating sprint/training efforts.**
We will `defer our roadmap
<http://khmer.readthedocs.org/en/v1.4/roadmap.html>`__ and decrease
`our sprint and training interactions
<http://figshare.com/articles/Channeling_community_contributions_to_scientific_software_a_hackathon_experience/1112541>`__.
As a small project trying to get more funding, we can't afford the
diversion of energy at this point.  That having been said, both the
roadmap planning and the sprints thus far were tremendously valuable
for thinking ahead and making `our contribution process
<http://khmer.readthedocs.org/en/v1.4/dev/getting-started.html>`__
more robust, and we hope to pursue both in the future.

**Paying technical debt maintenance fees, instead of decreasing
debt.** We still have lots of issues that are burdening the codebase,
especially at the Python and C++ interface levels, but we're going to
ignore them for now and focus instead on adding new features
(hopefully without *increasing* technical debt, note - we're keeping
the code review and continuous integration and test coverage and ...).
Again, we're a small project trying to get more funding... hard
choices must be made.

----

I'm writing a grant now to ask for sustained funding on a ~5 year time
scale, for about 3 employees - probably a software engineer /
community manager, a super-postdoc/software engineer, and a grad
student.  If we can get another round of funding, we will reactivate
the roadmap and think about how best to tackle technical debt.

Comments welcome!

--titus

p.s. Special thanks to Ethan White, Greg Wilson, and Neil Chue Hong
for their input!
