DART and buildbot
#################

:author: C\. Titus Brown
:tags: python,programming,testing
:date: 2007-02-02
:slug: comparing-DART-and-buildbot-anyone
:category: python


Dear lazyweb,

does anyone know of any comparisons of `DART <http://public.kitware.com/Dart/HTML/Index.shtml>`__ with `buildbot <http://buildbot.sf.net/>`__?

thanks!

--titus


----

**Legacy Comments**


Posted by Grig Gheorghiu on 2007-02-02 at 17:36. 

::

   Never heard of DART, but I used something called STAF/STAX in the
   past, and I had to struggle with tests defined in XML syntax. That's
   why I shuddered when I saw this on the DART page:    "Dart has several
   powerful features. These include:      * Client/Server model for
   testing and reporting    * Separation of data from presentation using
   XML and XSLT"    XML and XSLT...that way lies madness.      Grig


Posted by Kumar McMillan on 2007-02-05 at 10:45. 

::

   I haven't used DART either but I can say that a coder on my team was
   able to implement all the custom logic needed to port our home-grown,
   legacy "buildbot" to the real buildbot by creating a custom
   fileIsImportant callable.  In other words, buildbot seems very
   flexible to use.  It was perfect as a continuous integration tool for
   our multiple test suites/projects shared in a single subversion
   repository but looks like it can accomodate many other scenarios too.


Posted by Titus Brown on 2007-02-05 at 11:11. 

::

   Will Schroeder of Kitware pointed me towards DART2,    <a
   href="http://www.na-mic.org/Wiki/index.php/Dart2Summary">http://www
   .na-mic.org/Wiki/index.php/Dart2Summary</a>    and the DART manual is
   apparently available here:    <a href="http://svn.na-
   mic.org:8000/svn/Dart/trunk/Documentation/Manual/Dart.pdf">http://svn
   .na-mic.org:8000/svn/Dart/trunk/Documentation/Manual/Dart.pdf</a>
   Kumar, thanks for your comment!  Like Grig, I dislike XML on principle
   and I do appreciate the extensibility of Python software in general --
   I had a similar experience with nose.

