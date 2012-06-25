Some interesting discussions on the testing-in-python list
##########################################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2007-03-20
:slug: tip-list
:category: python


For my own future reference, as well as to attract people to the
fairly high signal `testing-in-python mailing list <http://lists.idyll.org/listinfo/testing-in-python>`__, here are some particularly interesting
posts to the TIP list.

Raphael Marvie `implements <http://lists.idyll.org/pipermail/testing-in-python/2007-March/000230.html>`__ a simple textual specification -> test suite generator.

Kumar McMillan `makes some nice suggestions <http://lists.idyll.org/pipermail/testing-in-python/2007-March/000210.html>`__ for Michal's "spec" nose plugin.

Benji York `outlines <http://lists.idyll.org/pipermail/testing-in-python/2007-March/000180.html>`__ a "Testing in Zope 3" case study (originally asked for by Grig).

Sebastien Douche `discusses <http://lists.idyll.org/pipermail/testing-in-python/2007-March/000174.html>`__ the reason he likes to use Trac to manage projects.

Kumar McMillan `talks about the nosetrim plugin <http://lists.idyll.org/pipermail/testing-in-python/2007-March/000043.html>`__ for suppressing duplicate errors in your nose output.

And last but not least, Grig `starts a loooong discussion
<http://lists.idyll.org/pipermail/testing-in-python/2007-March/000050.html>`__
on "Doctest or unitest?" that has some really excellent responses; see
especially `Jim Fulton discusses doctests with setup/teardown in
footnotes
<http://lists.idyll.org/pipermail/testing-in-python/2007-March/000142.html>`__,
`Benji York posts the Platonic Ideal of doctests
<http://svn.zope.org/zc.queue/trunk/src/zc/queue/queue.txt?rev=67933&view=markup>`__,
and `Benji York makes the case for good APIs (and zope.testbrowser and
twill, too
<http://lists.idyll.org/pipermail/testing-in-python/2007-March/000147.html>`__.

One less pleasant surprise was finding out that `unittest is being
rewritten
<http://lists.idyll.org/pipermail/testing-in-python/2007-March/000198.html>`__
for Py3K, and Collin is going with something that is both a
significant rewrite *and* neither nose or py.test.  The mind boggles.

Why are we extending a module based on an ugly paradigm (the unittest
module is great, but it's got a lot of unnecessary syntactic sugar
compared to nose/py.test), creating Yet Another unittest system,
breaking people's old unittest extensions, and skipping past two
fairly popular testing frameworks?  Apparently this route is easier
than either letting things be or convincing the nose/py.test people to
"donate".  I don't have anything against Collin, but is he really
going to develop something that's significantly better than what's out
there already?  I'm particularly unhappy that it's going to be dropped
into Py3K; I'm still not sure why this is happening.  (Can anyone
point me to a discussion?)

My preference would be to leave unittest as-is if we can't appropriate
nose or py.test.

Anyway, I argued my point on the list, and no one else seems to be
worried about it (or, rather, they don't have a solution ;).

--titus


----

**Legacy Comments**


Posted by Ian Bicking on 2007-03-20 at 14:04. 

::

   Yeah, the arguments for a reimplementation are very weak.  Yes, having
   external libraries isn't great.  So... maybe the answer is to adapt
   one of those libraries; that's certainly not a justification for
   writing a new one.  nose would be much easier in these terms, as
   py.test integrates with lots of stuff in the py-lib that isn't really
   stdlib-ready.      Rewriting **again** would be silly.  And I don't
   think the nose author is so territorial that changes to make it
   appropriate for the stdlib would be a problem.    Of course, then
   there's the question of release cycles and the stdlib and how any of
   that fits together.  But reimplementation doesn't solve anything there
   either.


Posted by Mike Verdone on 2007-03-20 at 19:15. 

::

   I haven't heard anything lately about the rewrite on the Py3k list.
   Maybe they forgot about it? :)    Generally I've found the unittest
   module as-is is good enough. The hard part is convincing the
   developers to write the tests. I don't really care too much which
   framework is "best". I hope the old unittest module lives on in Py3k
   somehow.    One strong point of unittest is that it looks a lot like
   JUnit. Less of a learning code if you've already learned to handle
   that beast.


Posted by Titus Brown on 2007-03-20 at 19:22. 

::

   I agree with both of you ;)

