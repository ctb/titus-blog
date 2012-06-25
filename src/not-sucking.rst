Writing Code That Doesn't Suck
##############################

:author: C\. Titus Brown
:tags: python,testing
:date: 2007-09-24
:slug: not-sucking
:category: python


*Note: this is ultimately intended for the biology-in-python Wiki at
http://bio.scipy.org/.  I will release it under a CC license, so please
feel free to use it for your own site!  --titus*

Here are some prescriptions for writing Python code that other Python
programmers will find more usable and readable than it might otherwise
have been.  This advice is intended for people writing anything more
advanced than isolated code snippets: anything that you might
eventually want to release, for example, or share with other people.

Follow coding conventions
=========================

Follow the suggested Python style guide, PEP 8
(http://www.python.org/dev/peps/pep-0008/).  Also read the docstring
style guide, PEP 257 (http://www.python.org/dev/peps/pep-0257/).

If you follow these style guides, then other people will be able to
read your code more easily.

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

Provide Automatic API Documentation
===================================

There are several tools for extracting docstrings and module/package
information and building Web pages out of them; I personally like
epydoc, but there are several other choices out there.  Use one, and
update your HTML docs nightly or weekly as your code changes.

Use version control and provide public access
=============================================

Use CVS or Subversion to store and publish your code; everyone has
clients for them and everyone knows how to use them.  If you use darcs
or bazaar-ng or git, that's great -- but provide a nightly snapshot of
your latest source code, so that I don't have to install something in
order to get your latest version.

Conclusions
===========

Yes, I know you're brilliant and idiosyncratic and your personal
naming conventions, or spacing choice, or homegrown test framework,
are a important signs of your individuality and creativity.  I don't
care.  I just want to use your software.  Don't try to surprise me,
because if you do surprise me I will probably be so shocked and
dismayed that I'll forget all about your software and instead write a
blogrant.  Do you really want me to waste that much time!?

More seriously, the point of sharing code is to share your code and
your solutions, not your idiosyncratic approach to programming.  If
you follow the above conventions, you have a better chance of
providing code that other people will be able to use.

If you need help with getting any of the above things to work, please
just ask.  The Python community is always quite happy to help people
work through issues related to making your code look better, behave
better, and play more nicely with other code.

I'm sure I'm forgetting plenty of things.  E-mail `me <mailto:titus@idyll.org>`__  and I'll add them.


----

**Legacy Comments**


Posted by Titus Brown on 2007-09-24 at 14:54. 

::

   whoops.  Forgot a licensing/copyright discussion.    Add a
   LICENSE.txt.  Put copyright notices somewhere, even if not in all the
   code files.  Choose BSD or GPL.


Posted by rgz on 2007-09-24 at 15:11. 

::

   "Yes, I know you're brilliant [...] and creativity. I don't care."
   I always try to follow the style guide lines and **even I** find that
   slightly offensive, "But think about me" sells better than "I don't
   care".    Not the smartest way to communicate with brilliant and
   idiosyncratic people.


Posted by Titus Brown on 2007-09-24 at 15:28. 

::

   One of us is either sarcasm impaired or offensive ;).    I'll see what
   I can do to amend the language to imply that brilliance, creativity,
   and idiosyncracy belong in your algorithms, not in your programming
   style.  I think the point does need to be made strongly, though,
   because young scientists tend to be serious offenders.    --titus


Posted by John M. Camara on 2007-09-24 at 17:03. 

::

   On the license issue you should add MIT. You may also want to state
   that a larger number of developers are more likely to contribute under
   an MIT style license over GPL.  I can't tell you how many times I have
   come across a module that was licensed under GPL that I would have
   like to use and would have contributed code but couldn't due to the
   license.    Anyway, another good practice is to use pylint [1] to
   discover bugs and bad coding practices.    [1] <a href="http://www.log
   ilab.org/project/pylint">http://www.logilab.org/project/pylint</a>


Posted by John Dawson on 2007-09-25 at 09:52. 

::

   In the article, you said:  "Note that you can always organize your
   actual files in as deep a hierarchy as you want, while keeping the
   public API shallow and easy to use."    How is this technique best
   accomplished?


Posted by Titus Brown on 2007-09-26 at 14:27. 

::

   See replies to comments at    <a
   href="http://ivory.idyll.org/blog/sep-07/code-layout-and-version-
   control.html">http://ivory.idyll.org/blog/sep-07/code-layout-and-
   version-control.html</a>

