Scientific software engineering, Jan 2017 version
#################################################

:author: C\. Titus Brown
:tags: khmer, software sustainability
:date: 2017-01-25
:slug: 2017-scientific-software-egr-kill-me-now
:category: science

As part of my `Moore Foundation Data Driven Discovery grant
<http://ivory.idyll.org/blog/2014-moore-ddd-stmt-of-work.html>`__, I
have to put together annual reports each year.  (This is more or less
standard for grants. ;)  You can read my `annual report narrative, here <https://github.com/ctb/2017-moore-ddd-annual-report/blob/master/narrative.md>`__, and my (ancillary, not required) `breakdown of projects in the lab, here <https://github.com/ctb/2017-moore-ddd-annual-report/blob/master/projects.md>`__.

Software development is hard
----------------------------

In the project breakdown, I `discussed our software development efforts <https://github.com/ctb/2017-moore-ddd-annual-report/blob/master/projects.md#continued-development-of-khmer-and-screed>`__ since the move to UC Davis and
Michael Crusoe's departure.  I say,

   khmer remains central to the lab and, a well as a suite of useful
   exploratory tools, is now maturing into a robust platform that
   several projects in the lab are relying on. Despite this I am still
   somewhat alarmed (at a strategic level) regarding the level of
   resources required to achieve even a minimally responsible level of
   scientific software development.

A bit further on, I make the point,

   ...we continue to find minor and not-so-minor bugs in khmer. This
   suggests to me that plain ol' software bugs are likely to have a
   significant contribution to the
   repeatability/replication/reproducibility crisis.

This point isn't new -- see Soergel, 2015, `"Rampant software errors
may undermine scientific results"
<https://f1000research.com/articles/3-303/v2>`__ -- but I wanted to mention
it again :).

Interestingly, we find the major value of our "exhaustive (and
exhausting)" testing regime to be less in *finding* new bugs, and more
in allowing us to fearlessly refactor and adapt the code base to new
projects as needed.  Daniel Standage and I have had several
discussions on this about khmer, as he was new to the experience; and
I'm watching it work again in the sourmash project as well.  (I should
say that this is all probably obvious to industry folk, but it seems
not to be obvious to academics!)

In sum, even for a little bitsy project like khmer, sustained software
development is hard.  We're taking the attitude that correctness is
critical, but I have a lot of sympathy with folk who conclude out of
expediency that maybe it's too hard for their project.
See: `Please destroy this software after publication. kthxbye. <http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__

Contracting out bits of software development may be an effective strategy
-------------------------------------------------------------------------

After (literally) years of trying to figure out how to move software
engineering forward in a sustainable way, I've reached a solution that
I'm happy with.  The solution:

1. Run the project as an open source project, with the testing, and the code
   review, and the issue tracker.

2. Contract out to someone from the open source community to help with code
   reviews, optimization, and issue whacking.

3. Task people within the lab with leading their scientific efforts
   and integrating it into the software as they go.

In this case I've got Daniel to keep an overall eye on the science
aspects of the project, and I've contracted with Tim Head (`@betatim
<http://github.com/betatim>`__) to do open source-y stuff.

There's a lot that goes into this, but I'll say that in the past I've
had a lot of trouble balancing the software engineering against
progressing the science.  One of the mismatches - especially for a
small lab like mine - was between the effort a full-time software
engineer could put in, and what grad students and postdocs found
possible given their projects.  This led to lopsided investment in
software engeering vs research. The tension remains, of course, but
it's much reduced.

A few points --

* "For our lab, a ratio of 1 half-time software engineer to 2-3 active
  grad/postdoc developers seems to work ok."

* I think this can scale in either direction.  I promised Tim a minimum
  number of hours over a 3 month period, but can reduce or increase that
  as needed over longer periods.  And, if we suddenly get an influx of money
  or project-related work, it seems like there are a fair number of
  PhD-level open source hackers out there that are available for hire.

  If I can ever do all the paperwork, I'd be happy to hire current
  grad students and postdocs as contractors, too.  (I was about halfway
  down that road with Upwork when Tim came along, and the paperwork
  was much easier this way :).)

* I'd like to think I'm paying Tim a reasonable amount (although I'm
  definitely not hiring him at Silicon Valley rates).  In return, he
  gets super-flexible working hours, the ability to put the work on
  his C.V. as part of an open portfolio, some occasionally interesting
  problems, and interaction with a new problem domain (he's a
  physicist by training, and while they *are* automatically expert at
  everything, there are niggling details about biology that he's still
  learning).

* It is very useful to run this project like a community-based open
  source project, even if we have relatively little in the way out
  regular outside contributors; it means that people can come and go,
  and catch up on project history, and so on, and it enables
  asynchronous work in an excellent way. (We're not nearly at `dat
  scale async <https://github.com/maxogden/async-team>`__ but I'm
  heading in that direction. :)

Refactoring vs software architecture redesign: Small moves, Ellie.
------------------------------------------------------------------

About every 6 months to a year, the question of investing in *real*
software design comes up.  Yesterday, `Daniel jumped
in. <https://github.com/dib-lab/khmer/issues/1592>`__.

It's clear from my response on that issue that I'm gunshy about large
scale architecture redesign :).

On the flip side, small scale changes and incremental refactoring are
messy, confusing, and slow; `our latest effort
<https://github.com/dib-lab/khmer/issues/1541#issuecomment-274828660>`__
to consolidate and de-obfuscate our sequence reading code is a tangled
mess of issues that is almost impossible to understand.  I have to sit
down and reset my brain and read the issues for 10 minutes before each
comment. (SOON THIS DRAGON WILL BE SLAIN, however.)

Flipping the flip, I'm pretty happy with how the `last big code
reorganization effort turned out
<https://github.com/dib-lab/khmer/pull/1504>`__.  And the current
effort is revealing `some lapses in our test suite
<https://github.com/dib-lab/khmer/pull/1590#issuecomment-274839945>`__ -
the last line of that comment is me saying "oh shit! that shouldn't
have worked!" - and moreover this is an area where `we've fixed some
bugs <https://github.com/dib-lab/khmer/issues/1434>`__ and `identified
some others <https://github.com/dib-lab/khmer/issues/1540>`__.

And for a last reversal, I'll just say that our current collection of
k-mer processing code is a crazy nightmare of functionality that is
only barely kept under control by our testing infrastructure.
(THIS DRAGON SLEEPS, ALBEIT FITFULLY.)

So:

* there may be a place for rethinking architecture, but I've never
  seen large scale architecture change work out well in practice.
  See: Perl 6.

* small scale changes yield messy interim code but seem to wind up yielding
  ok results.  See: Python 3.

* this really needs to be a constant effort on code bases; your code base
  is either "living" or "dead", and living code needs constant maintenance.
  But maybe it beats the alternative?

--titus
