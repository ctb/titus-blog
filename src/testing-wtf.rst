A Testing WTF
#############

:author: C\. Titus Brown
:tags: python, testing
:date: 2007-08-22
:slug: testing-wtf
:category: python


I'm in the process of writing up a "when and how to test" screed, and
I discovered this:

Karl Fogel's book, `Producing Open Source Software
<http://producingoss.com/>`__, has precisely two keyword hits to
testing in the ToC.

WTF?

--titus


----

**Legacy Comments**


Posted by Ricardo Niederberger Cabral on 2007-08-22 at 17:00. 

::

   I counted three. But really, is there any real technical difference
   between testing OSS projects versus commercial ones (which the author
   probably assumed as something already extensively covered elsewhere)?


Posted by Rams on 2007-08-23 at 00:17. 

::

   All non-trivial SVN patches require a test to be submitted; the whole
   test suite is in python. The "HACKING" doc has the details.     But
   you are right though, the book doesn't emphasize testing - many
   hackers like the author do not have testing (as a topic worthy of
   attention by itself) on their radar. I am far more concerned about
   "Committers" are gods attitude in the book. It doesn't talk about how
   to detect and eliminate cliques and cabals. Why does SVN have a
   private committers only mailing list ? What are the exact criteria for
   for becoming a committer - Why is it so difficult to set it down in
   black and white ?


Posted by Titus Brown on 2007-08-23 at 10:53. 

::

   Rams -- what project are you talking about?    Ricardo -- I think
   there are differences in testing OSS projects, just like there are
   differences in communication structure, responsibilities, code
   writing, etc... Testing is actually a huge force multiplier when
   working on a collaborative project, **especially** one where most
   people are, in theory, equal contributors.    --titus


Posted by Rams on 2007-08-24 at 15:55. 

::

   Titus Brown,  I meant the SVN project itself, since that project is
   used throughout the book as the primary example.  Here is the HACKING
   doc:<a href="http://subversion.tigris.org/hacking.html">http://subvers
   ion.tigris.org/hacking.html</a>

