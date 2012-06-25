Testing is hard.
################

:author: C\. Titus Brown
:tags: python, testing
:date: 2006-11-19
:slug: testing-is-hard
:category: python


I spent the better part of today refitting `Cartwheel
<http://cartwheel.idyll.org/>`__ for testing.  Cartwheel is a
bioinformatics framework that is used by a few hundred people; it's
mostly a database-backed Web site, with a compute server queueing
system tacked on.

Cartwheel is one of the two sites that got me interested in automated
Web testing: various parts of the Web site kept on breaking when I
added features.  So I started writing PBP tests for it, and that
ultimately led to `twill <http://twill.idyll.org/>`__.  twill,
testing, and my thesis side tracked me from Cartwheel.  Now I'm
finally back to working on Cartwheel.

The somewhat surprising fact is that retrofitting it for testing was
quite difficult.  It's particularly surprising given that I know
Cartwheel, twill, and nose inside out -- so I hadn't expected to have
too many problems adding twill testing into the Cartwheel Web server
inside of a nose-executable test suite.

I had to solve any number of silly problems, ranging from a lack of
test hooks in the database configuration to crosstalk between sys.argv
and cgi.py (!!)  as well as crosstalk between nose and Quixote 1.2.
There are times when I get really frustrated at tools -- mostly when
they screw me over by having deeply buried references to Python-wide
instance variables ;).

At any rate, I now have some automated tests running, and the way
is cleared for me to add some more with hopefully less trouble.

I also came across another reason to use `wsgi_intercept
<http://darcs.idyll.org/~t/projects/wsgi_intercept/README.html>`__ to test Web
sites in-process: you can test REMOTE_ADDR-based access restrictions
by twiddling the environment variable directly.  By resetting
REMOTE_ADDR to IP addresses of sites that should (and shouldn't) have
access, you can test access restrictions without using those remote
sites.

--titus


----

**Legacy Comments**


Posted by Ian Bicking on 2006-11-19 at 13:45. 

::

   Notably paste.lint/wsgiref.validate will check for that sys.argv/cgi
   conflict and warn you about it (happens whenever you don't set
   QUERY_STRING).  Have you tried wrapping wsgi_intercept to test for
   such problems?


Posted by Max Ischenko on 2006-11-20 at 01:15. 

::

   Testing is hard largely because tools (twill, Python web frameworks,
   etc.) are not very good. There is a lot of "accidental complexity"
   when you do automated web testing.


Posted by Titus Brown on 2006-11-20 at 01:26. 

::

   Ian, yep, I finally figured it out ;).  I probably should use
   wsgiref/paste.lint to check out wsgi_intercept.    Max, I **sort of**
   agree with your statement (see my comments on tool immaturity in my
   `pythonthreads interview &lt;<a
   href="http://www.pythonthreads.com/articles/interviews/python-
   community-is-extremely-active-in-building-agile-testing-
   tools..html">http://www.pythonthreads.com/articles/interviews/python-
   community-is-extremely-active-in-building-agile-testing-
   tools..html</a>&gt;`__  I would say the tools are definitely
   **immature**, but  to say that they aren't **good** requires a
   standard for **good**, and I haven't seen anything significantly
   better that can serve as that standard.  The comment about accidental
   complexity hits home perfectly.    --titus

