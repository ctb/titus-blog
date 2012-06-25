The SciPy 2007 Testing BoF
##########################

:author: C\. Titus Brown
:tags: python,testing,scipy
:date: 2007-08-20
:slug: scipy-testing-bof
:category: python


Thanks to a kind invitation by Fernando Perez, I was alerted to a BoF
on Python/testing at SciPy.  He made the mistake of introducing me as
"the resident expert" so I felt even less inhibited than normal, which
was hopefully not too problematic...

Gael Varoquaux `took notes <http://www.scipy.org/SciPy2007_testing_notes>`__.

Basically, this was a lot of fun.  I can't compare with previous
years, but I feel like testing in Python is really being emphasized.
Fernando shared some of his personal reasons for getting so
interested, which was interesting in itself.  Most people in the room
seemed interested in getting started if they weren't already testing
(well, duh, it was a BoF, but still...)

A few comments/thoughts/anecdotes.

I need to publicize `the testing-in-python mailing list
<http://lists.idyll.org/listinfo/testing-in-python>`__ some more.
It's quite low bandwidth and the signal-to-noise ratio has been
essentially infinite (no noise!).  Join!

`nose
<http://www.somethingaboutorange.com/mrl/projects/nose/>`__ is
becoming *very* popular.  Three or four of the people there (out of 20
or so) were using nose already, and had nothing but good things to say
about it.  I think extending my `nose Introduction
<http://ivory.idyll.org/articles/nose-intro.html>`__ would be very
relevant to the community.

Fernando really wanted to work within the stdlib, but several people
tried to convince him that nose was worth the extra install.

There were a lot of very good requests for testing functionality that
doesn't yet exist (see the wiki notes).  There are some pretty good
master's projects in there, actually...

The most interesting suggestion came from several people: people would
like to be able to tie test results (performance, regression, code
coverage) to specific code revisions and then query for results across
revisions.  I think something like the `Test Anything Protocol
<http://en.wikipedia.org/wiki/Test_Anything_Protocol>`__ might fit the
bill, although it may be too simple.... Anyway, someone should develop
this.  Since I believe svn stores diffs, it could be as simple as appending
the latest test results to a file, although this could be really stupid
for a big project ;).

I recommend that people interested in GUI testing look at QT and
`KWWidgets <http://www.kwwidgets.org/>`__. These are both toolkits
with test hooks built in.  KWWidgets is not well known, but it seems
deserving of further attention.

Nobody else knows how to do multiprocessing code tests, either.

There's clearly enough interest out
there to support a few simple "intro" guides to testing in Python...

All in all, a really fun time -- thanks for organizing this, Fernando!

--titus
