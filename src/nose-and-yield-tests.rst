Nifty Nose Functionality
########################

:author: C\. Titus Brown
:tags: python,programming,figleaf
:date: 2007-02-07
:slug: nose-and-yield-tests
:category: python


I just put the finishing touches on some automated regression tests for
`figleaf <http://darcs.idyll.org/~t/projects/figleaf/README.html>`__, my
simple code coverage analysis program.  In the process I found a nice
use for `nose's  <http://somethingaboutorange.com/mrl/projects/nose/>`__
``yield`` test constructor.

Briefly, nose lets you write code like this: ::

   def test()
      for i in range(0, 10):
         yield check_num, i, 2*i

   def check_num(i, j):
      assert 2*i == j

This defines a set of 10 tests, each of which are executed and counted
independently.

(I think this behavior is based on py.test but I could be wrong.)

I hadn't had any use for this kind of test before, but when
considering how to write the figleaf tests, I realized that this would
be a really neat way of basing regressions tests on individual files.

Suppose I have a directory full of .py files together with coverage
information, and I want to execute each .py file and check the
coverage results against the previously recorded coverage information.
Easy!  Here's the code: ::

   def test():
      for filename in os.listdir(testdir):
          if filename.startswith('tst') and filename.endswith('.py'):
              yield compare_coverage, filename, filename + '.cover'

where ``compare_coverage(pyfile, cover_file)`` is a function that
executes the given filename and compares current coverage data with
the pre-recorded stuff.

This saves me having to do something silly like write an individual
test loader for each .py file, which would be cumbersome and perhaps
brittle.

--titus


----

**Legacy Comments**


Posted by Eduardo Padoan on 2007-02-07 at 06:30. 

::

   &gt; (I think this behavior is based on py.test but I could be wrong.)
   Yes, it is. It is called Generative test.  <a
   href="http://codespeak.net/py/current/doc/test.html#generative-tests-
   yielding-more-tests">http://codespeak.net/py/current/doc/test.html
   #generative-tests-yielding-more-tests</a>


Posted by Jay Parlar on 2007-02-07 at 07:56. 

::

   It is in fact based on py.test. I asked Jason Pellerin to add this
   functionallity last year, after I switched from py.test to nose for a
   project and needed this kind of generation.


Posted by Terry Peppers on 2007-02-08 at 07:56. 

::

   I have a full suite of tests that are built on this very behavior.
   Handy when you have a base test that you want to run with different
   test values or in my case a single test against multiple web sites.

