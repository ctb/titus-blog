Writing (Python) Code that Doesn't Suck, v2
###########################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2007-09-26
:slug: not-sucking-v2
:category: python


My `last post on this subject <http://ivory.idyll.org/blog/sep-07/not-sucking>`__ got a number of good comments, both here and on the `biology-in-python mailing list <http://lists.idyll.org/listinfo/biology-in-python>`__, so I've amended and updated it.  (Note that Brandon King is now listed as a contributor.)

I would particularly appreciate comments on the licensing section and
the conclusions.  Also, I'll reply to one or two comments in another post.

cheers,

--titus

---------

==============================
Writing Code That Doesn't Suck
==============================

Here are some prescriptions for writing Python code that other Python
programmers will find more usable and readable than it might otherwise
have been (i.e. code that "doesn't obviously suck").  This advice is
intended for people writing anything more advanced than isolated code
snippets: anything that you might eventually want to release, for
example, or share with other people.

Follow coding conventions
=========================

Follow the suggested Python style guide, PEP 8
(http://www.python.org/dev/peps/pep-0008/).  Also read the docstring
style guide, PEP 257 (http://www.python.org/dev/peps/pep-0257/).

If you follow these style guides, then other people will be able to
read your code more easily.

Also, try not to override built-in Python objects, e.g. ``str = 5`` or
``id = myOwnObject``.

Organize your code
==================

Be systematic in the way you organize your code.  I tend to use the
following conventions (see
http://ivory.idyll.org/articles/advanced-swc/#modules-and-scripts for
my motivation):

 - module filenames must be valid Python identifiers, but scripts
   should use '-' instead of '_' (which renders them non-importable).

 - use shallow package hierarchies for naming, e.g.

	import pkg.fasta_io

   instead of

            import pkg.seq.readers.file_readers.fasta

   The latter one may seem better organized, but no one will ever
   remember the whole package name!  Note that you can always organize
   your actual files in as deep a hierarchy as you want, while keeping
   the public API shallow and easy to use.

 - modules, when executed from the command line, should either run
   tests or do nothing.

 - provide README.txt, lib/, bin/, doc/, and setup.py.  Everyone knows
   what each of those files/directories contains.

Use setup.py and Distutils
==========================

Provide a setup.py file (see docs.python.org, distutils
documentation), even if it's incomplete.  This will let people install
your code in the standard Pythonic way.

Even better, post your code to the Python Package Index and make sure
that it can be installed with easy_install.  This makes it really
trivial to get the latest "official" version of your package.

Provide Automated Tests
=======================

Python has some excellent built-in testing frameworks, including
unittest and doctest.  Use them to provide at least some simple
automated tests.

Even simple unit tests are really important, and they don't take much
time to write.  Put big/complicated functional tests under tests/; put
smaller/simpler unit tests with the code they're testing.

One very useful technique is to write examples in doctest format:
write a text or reStructuredText document that contains discussion
interspersed with executable code, in the form of commands and their
expected output.  Then run them with doctest, which will tell you if
any of your commands produce unexpected output.  This will keep you
honest and make sure that your examples are always up-to-date.

Provide a simple, obvious and/or standard way to run all of your
automated tests.  Test discovery frameworks like nose or py.test may
help with this.  If you want to provide flexibility in which tests to
run, that's great, but make sure that the default command runs a fast
and useful set of tests.

More advanced advice: use code coverage (look up coverage.py or
figleaf) to determine which sections of your code aren't covered by
your current tests; use continuous integration (buildbot) to run your
tests nightly on several different platforms.

Provide API Documentation
=========================

Put in docstrings; they're a fundamental part of Python.  Adhere to
the docstring "coding standard", PEP 257
(http://www.python.org/dev/peps/pep-0257/).

There are several tools for extracting docstrings and module/package
information and building Web pages out of them; I personally like
epydoc, but there are several other choices out there.  Use one, and
update your HTML docs nightly or weekly as your code changes.

Write some examples.  Was there a particular problem that motivated
you to write your code?  If so, describe how you solved it, in simple
language, with really simple code.

If you have users and you change the API, be sure to tell them, e.g. use
a ChangeLog.

Making Releases
===============

Provide regular zip and/or .tar.gz files of your entire distribution,
with docs and generated files.  Make them available via HTTP and/or
FTP.

Name and number your releases systematically, preferably either by
date (if you haven't formally released the package yet!) or number.
Use something that will stay in approximate lexical order, e.g. ::

   myproject-0.1
   myproject-0.2
   myproject-0.3
   myproject-1.0

Don't go over the number 10, e.g. ``project-0.10`` looks too much like
``project-0.1`` for comfort, both by eye and to the computer.

Don't use ``-latest`` except for snapshots, e.g. if you use
``project-latest.tar.gz`` it should be an automatically generated
snapshot.

Don't use ``-current`` unless it's a symbolic link to the latest
release.  (Preferably, keep old releases in a separate location, like
``OLD/``, and only have one obvious release -- the latest one -- on
the main page or in the main download directory.)

**Always** have a file named ``project-x.y.tar.gz`` unpack into
``project-x.y/``.  Never have it unpack into the current directory,
or into another directory name where it may conflict with an
older/different version of your software.

Release fairly regularly.  It's (much!) better to have a release with
some known bugs than it is to never release anything at all.

Use version control and provide public access
=============================================

Use CVS or Subversion to store and publish your code; everyone has
clients for them and everyone knows how to use them.  If you use darcs
or bazaar-ng or git, that's great -- but provide a nightly snapshot of
your latest source code, so that I don't have to install something in
order to get your latest version.

Copyright and license your code
===============================

Copyright holders are the people who own the code, and they can
license it for use, modification, and redistribution by others.  Make
this information explicit if you want others to use your code!

Provide an explicit copyright notice, so people know who the author is
and when the code was written.  (Make sure you know who actually owns
your code: it may be your employer, not you!)

Provide an explicit license -- we suggest either the BSD, the GPL, or
the LGPL.  (Do your best to avoid writing a new license; it will
confuse people.)  The BSD releases your software for use,
modification, and redistribution by anyone, while the LGPL and GPL
place certain requirements on redistribution.

Conclusions
===========

People often start out programming with their own conventions, or
their teacher's conventions.  In Python, there is really One Right
Way to Do It -- see PEP 8.

Not interested in conforming?  Well, I know you're brilliant and
idiosyncratic and your personal naming conventions, or spacing choice,
or homegrown test framework, are important signs of your
individuality and creativity -- but unfortunately they're likely to
get in my way when I try to use your code.  What I'm really interested
in is the creativity of your approach and algorithms.  After all, the
point of sharing code is to share your code and your solutions, not
your idiosyncratic approach to programming!  So, if you follow the
above conventions, you have a better chance of providing code that
other people will want to use.

If you need help with getting any of the above things to work, please
just ask.  The Python community is always quite happy to help people
work through issues related to making your code look better, behave
better, and play more nicely with other code.

Contributors
============

C. Titus Brown wrote the first draft.  Brandon King submitted detailed
comments that were incorporated into the second draft.  We welcome
comments or diffs!

(sep25/2007 draft.)


----

**Legacy Comments**


Posted by Kumar McMillan on 2007-09-26 at 19:39. 

::

   very nicely put.  two comments:    1. An ammendment (IMHO) to release
   often: Do not perpetuate a "dev" release.  That is, if you have to
   tell people to easy_install my_module==dev,&gt;=r2151 then just cut a
   release!      2. I strongly feel that "tests" should be a submodule of
   your module.  I.e. my_module.tests.  Some people disagree with this so
   here are my arguments:  I want to run your tests on my production
   server to, uh, be sure that it still works over there.  No matter how
   many times your tests pass for **you** it doesn't mean they will pass
   for me.  I want to easy_install your release and if I find a bug I
   want to also submit a test so you don't break it again!  Lastly, it's
   easy.  Is it 1977?  Are you trying to save disk space? :)


Posted by Titus Brown on 2007-09-26 at 20:28. 

::

   Hey Kumar,    while less specific, I feel that this advice:    Provide
   a simple, obvious and/or standard way to run all of your automated
   tests.    covers your point -- I don't care **where** your tests are,
   I just want to run 'em!    --titus


Posted by Titus Brown on 2007-09-26 at 20:31. 

::

   Also note:    <a href="http://use.perl.org/~chromatic/journal/34552?fr
   om=rss">http://use.perl.org/~chromatic/journal/34552?from=rss</a>
   Even Perl folk agree! ;)    (and, chromatic -- in response, note the
   "obviously"  in 'code that "doesn't obviously suck"'.  Of course
   there's a lot more to writing good code than these rules, but these
   are good guidelines for packaging, IMO.)

