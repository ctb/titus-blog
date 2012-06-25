GUI Testing
###########

:author: C\. Titus Brown
:tags: python,testing
:date: 2008-03-21
:slug: gui-testing
:category: python


Kumar MacMillan pointed me towards `GUITAR
<http://www.cs.umd.edu/~atif/GUITARWeb/>`__, a framework built by
`Atif Memon <http://www.cs.umd.edu/~atif/newsite/index.htm>`__ and
others.  There's a `YouTube video
<http://www.youtube.com/watch?v=OiE9zRPD6ps>`__ of him and Adam Porter
talking at the Google Test Automation Conference (2007).

Looks and sounds interesting.  Also nice to note that `GUITAR is being
open-sourced <http://sourceforge.net/projects/guitar>`__...

--titus


----

**Legacy Comments**


Posted by Kumar McMillan on 2008-03-24 at 10:44. 

::

   Roughly, it uses introspection to analyze all the possible inputs to
   GUI components (Java only, currently) and traces the path to other
   components they connect to.  Then it throws all that into a "reactor"
   that generates runnable functional tests for each possible input
   combination.  He has applied it to 3 popular apps from sourceforge and
   already discovered legitimate bugs.  Cool idea!    (It is hard to
   understand this by glancing at the site description.)

