What's a good Python code base?
###############################

:author: C\. Titus Brown
:tags: python
:date: 2009-01-07
:slug: lazyweb-good-code-bases
:category: python


A friend asks, ::

  i'm going to be recoding <x> from scratch starting next week, in python.
  what codebase would you recommend as good to model after?

Any thoughts on a well-formed, reasonably sized (yet not huge), and simple
Python code base?

There have to be some examples somewhere!  I'd suggest something in the stdlib,
but nothing is coming to mind right now -- and there are some real stinkers in
there, too.

For now, I've pointed my friend towards PEP 8 and the Python Cookbook.  Very
unsatisfying.

--titus


----

**Legacy Comments**


Posted by Greg Wilson on 2009-01-07 at 15:54. 

::

   If you find one, please let me know --- my students would want to see
   it too.


Posted by Joseph Lisee on 2009-01-07 at 17:03. 

::

   Trac: <a href="http://trac.edgewall.org/browser/trunk/trac">http://tra
   c.edgewall.org/browser/trunk/trac</a>    Its on the bigger size, but
   they use a very neat extension point and plugin system which makes
   modifying and expanding Trac very easy and powerful.  I built a
   similar plugin/extension point system myself based on some of the
   "magic" Trac uses to make there's work.  Trac also has decent package
   organization and testing.


Posted by Brett on 2009-01-07 at 17:13. 

::

   Typically the newer modules in the standard library that were
   specifically for the stdlib and not imported from external use tend to
   be very good. I remember thinking at one point that the heapq module
   was of high quality, for instance.


Posted by Jonathan Ellis on 2009-01-07 at 17:18. 

::

   I guess your objection to the Cookbook (dead trees version) is that
   the projects are too small?  Other than that I thought the commentary
   was quite good.


Posted by Titus Brown on 2009-01-07 at 17:31. 

::

   Jonathan -- exactly.    Joseph, Trac is big enough that I worry it's
   got its whole own set of conventions.  It's definitely hard to grok.
   I guess I'm looking for something in the "sweet spot" between a single
   module and a large-ish program: small enough to understand, big enough
   to have to confront some real problems.    I'd offer up twill, but
   it's just a wrapper around mechanize, really.


Posted by hads on 2009-01-07 at 17:35. 

::

   Check out Zine; <a
   href="http://zine.pocoo.org/">http://zine.pocoo.org/</a> - it's a
   pretty new project but the guys behind it write nice code in my
   opinion.


Posted by Rene Dudfield on 2009-01-07 at 17:47. 

::

   hi,    great question.    I wouldn't recommend the stdlib modules...
   often they are only written for the latest version of python - and are
   made for distribution with python - not for external distribution.
   There are ***many*** things you need to do for high quality external
   packages that you don't need to do with stdlib modules.    Good python
   modules often need to work with older releases of python.    You'll
   probably need to make heaps of hacks/extensions to distutils, have
   automated bots building and testing it all the time, plus all sorts of
   other things.    You need to have it packagable for the various OS
   distributions, like debian, freebsd, macports, windows installers, mac
   OSX installers etc etc.  Not to mention setting it up in pypi,
   easy_install, and buildout.    A good small software needs to have it
   all in one file with tests and all :)  Then people can just copy that
   file into their project and they are done.    Then there is building a
   community around the project... which is often very important.  So
   there are lots of examples available, and posts about how to do
   things.  Can people easily contribute?  Can people test the software
   on their platform easily?    There is also promotion -- where to
   announce the project?  Documentation about why the software is useful,
   it's pros and cons.    Also, applications have many different
   requirements compared to frameworks, or libraries.    I guess it
   really depends on the type, and size of the software, and the
   distribution needs.    For big projects, I'd look at cherrypy,
   twisted, pygame, moinmoin, trac, and numpy.  Each project has
   different requirements and needs.  I'd call each of these projects
   good for their requirements.      ... anyway, there's some rambling
   thoughts on the matter for you... I'm very interested in what others
   have to say about the question.


Posted by Giulio Piancastelli on 2009-01-07 at 19:35. 

::

   I'm in a similar position as your friend. I had a look at html5lib
   (http://code.google.com/p/html5lib/): I found some inspiring bits, but
   I am really a newbie at Python coding and code base structuring, so
   I'm not in the best position to judge html5lib's quality.    If you
   look at it, I'd be interested in reading your thoughts.


Posted by Ben on 2009-01-08 at 07:03. 

::

   web.py


Posted by Tom on 2009-01-08 at 19:55. 

::

   It is by no means small, but one of the best I've seen is Twisted.
   Religious about TDD, automated builds, etc. The codebase is pretty
   enormous, but you could probably showcase any individual module for a
   smaller slice.    <a
   href="http://twistedmatrix.com">http://twistedmatrix.com</a>


Posted by Chris Perkins on 2009-01-09 at 19:15. 

::

   I think the sqlalchemy codebase is a work of art.    Twisted codebase
   is good, but it does not follow pep-8.    The Pylons codebase is nice,
   as are Formencode, and PasteScript.


Posted by Yi Qiang on 2009-01-10 at 23:38. 

::

   Another vote for Twisted, some of the best code I've had a chance to
   work with yet.


Posted by Yi Qiang on 2009-01-10 at 23:38. 

::

   Another vote for Twisted, some of the best code I've had a chance to
   work with yet.

