Running code coverage on the CPython trunk
##########################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2007-12-17
:slug: coverage-on-python-trunk
:category: python


Brett Cannon notes that `GHOP is working out well
<http://sayspy.blogspot.com/2007/12/ghop-is-working-out-well-and-i-need-to.html>`__,
and muses about the future of the CPython test infrastructure (among
other things).  This is something I'm interested in as well (guess
where all those testing tasks in GHOP came from? ;) and I've been confused,
if not frustrated, by the apparent complexity of the CPython test suite.

One of the techniques I set up a year or so ago, after I first wrote
figleaf, was to run code coverage analysis on the trunk tests.  This
was more trouble than it should have been: the test runner itself
needed to be patched.  This is because code coverage analysis relies
on setting the trace function with ``sys.settrace``, and a number of
tests delete the system trace function, either with ``sys.settrace``
or with internall calls.

Tonight, inspired both by Brett's post and some cleanup work I'm doing
on figleaf, I tracked down all of the modules responsible for deleting
the trace function and excluded them from my test run.  The result?  A
(fairly simple) command-line code coverage analysis run that I think
could easily meet Brett's request for a nightly coverage analysis.

To run this yourself, you need to grab the `latest version <http://darcs.idyll.org/~t/projects/figleaf-latest.tar.gz>`__ of figleaf, unpack it somewhere, and then run the following command in your build directory: ::

  % ./python /path/to/bin/figleaf Lib/test/regrtest.py `cat traceless`
  % ./python /path/to/bin/figleaf2html

(See the bottom of this post for the contents of the ``traceless`` file.)

This runs figleaf with the dev version of Python and excludes all of the
modules that set the trace function, directly or indirectly.

The results can be seen `here
<http://iorich.caltech.edu/~t/transfer/python/>`__ for a short while.

It would be easy to get this running on Windows as well, if only there
were a nice way to tell regrtest to exclude those modules without
having a really long command line...

--titus

Here's the 'traceless' file: ::

-x test_trace
-x test_scope
-x test_doctest
-x test_asynchat
-x test_asyncore
-x test_capi
-x test_decimal
-x test_docxmlrpc
-x test_ftplib
-x test_logging
-x test_poplib
-x test_queue
-x test_smtplib
-x test_sys
-x test_telnetlib
-x test_threaded_import
-x test_threadedtempfile
-x test_threading
-x test_threading_local
-x test_urllib2_localnet
-x test_xmlrpc
-x test_builtin
-x test_hotshot
-x test_exceptions
-x test_coercion
-x test_richcmp


----

**Legacy Comments**


Posted by Brett on 2007-12-17 at 13:57. 

::

   Yeah, the CPython test suite is more complicated than it needs to be.
   Problem is that the whole thing has grown organically with no set
   testing rules in place.  This is why I want to write up a doc that
   explicitly states what a test needs to do (coverage, separate whitebox
   from blackbox, make the tests re-entrant, etc.).    And this organic
   nature is also why there is a bunch of random stuff in
   test.test_support.    But the biggest reason is no one has cared
   enough to try to rectify the issue.  All of the core developers know
   what to do to get the tests they need written, so we just deal with
   it.  But I am sure it is a bigger pain for non-committers.  This is
   why I have publicly stated I want to fix this.    I will hopefully vet
   stuff through TIP to make sure that I am doing reasonable stuff and to
   possibly get help in applying any decisions made.


Posted by Jerry on 2008-03-17 at 16:39. 

::

   Your directions confused me a bit. :)  With regrtest.py, apparently
   command line arguments are interpreted as names of classes to run.
   The -x flag turns changes the meaning of all arguments to be those to
   exclude.    eg: You probably want to do:  regrtest.py -x test_trace
   test_scope test_...    Your "traceless" file doesn't need the -x
   switch repeated for each class.

