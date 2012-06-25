Some Google Summer of Code Project Ideas
########################################

:author: C\. Titus Brown
:tags: python,gsoc
:date: 2009-03-20
:slug: gsoc-projects
:category: python


`'tis the season
<http://wiki.python.org/moin/SummerOfCode/2009?action=show&redirect=SummerOfCode>`__,
and so it's time for me to post my list of accumulated project ideas.
I'll transfer these over to the wiki tomorrow, after I track down some
references.  I'm willing to mentor any or many of these but I'd prefer
to find someone to be the primary mentor for most of 'em.  The ideas
are not isolated to a single project; there are some potential
overlaps in the testing stuf, especially.
 
1. Improve subprocess

I and others (mainly others) have talked about cleaning up & improving
the subprocess module and associated documentation.  This project
would involve gathering a bunch of features, integrating them, testing
them out on multiple platforms (most especially Windows), documenting
them, submitting them to the Python core, and working through at least the
first round of critiques.

2. Core Python testing infrastructure/nose compatibility

Work on the Python 2.x/3.x test running infrastructure to build a
`nose compatibility layer
<http://somethingaboutorange.com/mrl/projects/nose/>`__, so that
developers can run the Python tests with nose.  This would then enable
tag-based execution, code coverage analysis, and all sorts of other
nice features.  The goal would be to produce a nose plugin that was
core-Python-specific, so no changes would need to be made to the core
Python code.

3. Analyze code coverage and improve test coverage, for Python core.

The CPython and stdlib code coverage is not terribly great, ranging
from 99% to ~50% for some stdlib modules.  Measure the C code coverage,
integrate it with the Python code coverage, and provide a convenient
integrated report.  Make it easy to run & generate code coverage.  Do
so for Mac OS X, Windows, and Linux.  Improve code coverage by adding
tests.

4. Integrate of Pyrex and C code coverage into figleaf reporting

Right now, figleaf (my code coverage analysis tool) measures and
reports on Python code coverage.  Add integration hooks to allow it to
import and generate reports on C/C++ and Pyrex/Cython code coverage.

5. Port figleaf to Python 3.0.

Code coverage analysis is an important component of testing, especially
when refactoring legacy projects.  Make figleaf 3.0 compatible, probably
in a separate branch.

6. Implement branch coverage measurement and reporting for CPython.

'nuff said.  (This is a tough project that would be more research than
implementation, I think.)

7. Extend a simple continuous build system for Python projects.

Work on a simple buildbot replacement that allows simple, flexible
reporting and remote push of results.  (This is also part of the
snakebite project.)  More in a bit.

8. GridRepublic/BOINC Python

Distributed Python: Borrow or invent a notation for master/slave
execution in Python. Develop a system that implements this on BOINC,
i.e., creates WUs and applications, and harvests the results. See the
`BOINC dev projects
<http://boinc.berkeley.edu/trac/wiki/DevProjects>`__ generally and the
`Python app design document
<http://boinc.berkeley.edu/trac/wiki/PythonAppDev>`__ specifically.

--titus

p.s. Oh, yeah, and a `pygr <http://code.google.com/p/pygr>`__-related project
would be good, too.


----

**Legacy Comments**


Posted by Jesse Noller on 2009-03-20 at 10:49. 

::

   +1 to point 1,2,3, on point 4, look at further integration with ned's
   coverage tool, +1 to 6,7 - hadn't seen 8 before, need to take a look.
   I'm actually +1000 on adding nose-capabilities into core. I know it's
   a bit of a bikeshed, but given I work on tests all day long, I see the
   benefit


Posted by Al Snow on 2009-03-22 at 14:30. 

::

   Question: Are there other Python-based projects (mozilla, etc) that
   are participating in GSOC that you could partner with?


Posted by Titus Brown on 2009-03-22 at 15:37. 

::

   Al, yes, of course.  Just go look at the GSoC page.  But it's not
   clear what "partnering" means...?  We tend not to support "just
   programming in Python" as a project ;)


Posted by vikas on 2009-03-24 at 07:11. 

::

   hi......    i want to talk you this nose integration to python core,do
   you available at irc ?


Posted by vikas on 2009-03-24 at 07:11. 

::

   hi......    i want to talk you this nose integration to python core,do
   you available at irc ?


Posted by Titus Brown on 2009-03-24 at 07:23. 

::

   vikas, no, I don't use IRC ;).  Could you drop me a note at
   titus@idyll.org?

