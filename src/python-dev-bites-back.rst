python-dev Bites Back!
######################

:author: C\. Titus Brown
:tags: python
:date: 2007-03-05
:slug: python-dev-bites-back
:category: python


OK, this is one thing I *love* about Python -- in my entry on `"five
things I hate about Python"
<http://ivory.idyll.org/blog/mar-07/five-things-I-hate-about-python.html>`__
(which achieved "entry worth bashing" status on reddit; go provocative
titles!), I complained about the difficulty in getting patches submitted.

AMK read this and `posted about it <http://mail.python.org/pipermail/python-dev/2007-March/071495.html>`__ to the python-dev mailing list, starting a
discussion.  One outcome of the discussion is that Python will soon be
available via a distributed VCS, like git.  (I can't claim any credit
for anything other than being loudmouthed: this idea came up during the
python-dev panel, and people brought it up as a possible solution to
my complaint.)

So I really like the fact that rather than dismissing me as a complete
blowhard (which I *am*) the -dev community actually discussed it and
is taking some action.

I think the action is a technical solution to a social problem, but then
again I'm prone to that as well ;).

My suggestions:

I would personally like to make it possible for someone to
"test-submit" a code patch to Python and then see if it breaks an
existing test.  Perhaps we could even maintain a "non-breaking applied
patches" branch of Python.  And then run that against the pybots
community service to see what breaks.  That'd be neat, right?
(Actually, I could probably award a masters degree for setting up such
a project, if anyone was willing to come to Michigan for two
years... let me know ;)

There's an even more important social change I'd like to see.  Before
writing or applying patches, developers should write at least one new
test that fails BEFORE the patch is applied and succeeds only AFTER
the patch is applied.  This will serve several goals: patches will
apply to precisely identified problems; test coverage will gradually
increase; and world peace will be achieved.

This idea fits in with some of the other ideas that I discussed
briefly with Brett Cannon for refitting the existing test suite a bit.
The real question is, of course, Where Will Titus Find The Time?

(Anyone need/want a Masters? ;)

--titus


----

**Legacy Comments**


Posted by michele on 2007-03-06 at 04:16. 

::

   Great news! :-)    I hope they will go with Mercurial, I've switched
   to it from Bazaar 4 months ago and I've never looked back.    It's
   fast (as much as GIT), it's conceptually very simple and clean, it's
   multi platform (GIT is linux only) and IT'S PYTHON. ;-)    Quoting
   James Gosling:    "So one of the big changes over the last year has
   been that there's a new source-code management tool called Mercurial,
   and that's made everyone in engineering very happy."    <a href="http:
   //java.sun.com/developer/technicalArticles/Interviews/gosling_os1_qa.h
   tml">http://java.sun.com/developer/technicalArticles/Interviews/goslin
   g_os1_qa.html</a>


Posted by glenn on 2007-03-07 at 20:54. 

::

   Test-first patching?  Awesome!  Test first development always feels so
   right when you do it, but it is still so easy to just dive into the
   solution; formalizing it as part of the open source process is an
   incredible technical solution to a social problem that would likely
   bleed over in to all sorts of other projects.  ( Time for some commit
   triggers and nosetests )


Posted by Diane Trout on 2007-03-09 at 17:53. 

::

   Ooh ooh, a masters for improving python? That sounds like fun.
   Also the mercurial cvs import tool is much more robust than the
   equivalent tool for git. So far it looks like I've gotten through 1998
   for the 3.4 GiB mozilla cvs repository. (I tried 4 different paths for
   importing the mozilla repository into git and they all failed).

