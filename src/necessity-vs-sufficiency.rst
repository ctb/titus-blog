Good code coverage: Necessity vs Sufficiency
############################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2009-02-19
:slug: necessity-vs-sufficiency
:category: python


I get really frustrated with posts that claim `your unit tests lie to
you
<http://agilesoftwaredevelopment.com/blog/janusz-gorycki/your-unit-tests-are-useless>`__
or `100% code coverage is fallacious
<http://binstock.blogspot.com/2007/11/fallacy-of-100-code-coverage.html>`__
or `there are flaws in coverage measurement
<http://nedbatchelder.com/blog/200710/flaws_in_coverage_measurement.html>`__.
These are sensationalist headlines that encourage bad behavior, by
confusing new or inexperienced or argumentative or lazy developers:
"well, we all know test coverage isn't that important..."

There is a fundamental confusion here between *necessary* and
*sufficient*.  In plain English, things that are *necessary* are,
well, necessary for a process; things that are *sufficient* are,
collectively, sufficient.

One does not imply the other.  Tires are *necessary* but not
*sufficient* for a car.

Why do I bring this up?  Because near-100% code coverage is basically
*necessary* for a complete automated test suite, but not sufficient.

If you do not have near-100% code coverage, then some portion of your
code is not being executed by your tests.  That means that code is
untested.  It can't possibly be tested if you aren't executing it!

(As a corollary, `no test that adds to code coverage is useless <http://binstock.blogspot.com/2007/11/fallacy-of-100-code-coverage.html>`__.  It may not be
as useful as it could be, but it is still running code that is otherwise
untested.  Room for improvement does not equal uselessness!)

OTOH, there are many reasons that 100% code coverage isn't sufficient to
make your test suite good.  For one, code coverage isn't branch coverage.
For another, code coverage can't tell you if your feature set meets your
client's needs or is in fact functional -- all it can do is tell you that
your feature set meets your expectations at the moment.

So, let me suggest this simple pair of statements:

1. High (statement) code coverage in your tests is *important*.
2. High code coverage doesn't guarantee that your tests are complete.

I feel like high code coverage is actually a pretty low bar for a
project.  Whether or not you're using TDD, if you don't have high code
coverage numbers, you're not really testing very thoroughly; it's
generally pretty easy to amp up your code coverage numbers quickly,
although writing the test fixtures can be a problem.  I'll talk a bit
about this in my PyCon talk.

Regardless of your tests suite, `your project will probably fail in a boring and project-specific
way
<http://geeksinboston.com/2009/01/07/you-will-probably-fail-in-a-boring-and-project-specific-way/>`__.

--titus

P.S. `Many people do get it, which is nice. <http://coverclock.blogspot.com/2008/10/while-code-coverage-is-necessary-but.html>`__


----

**Legacy Comments**


Posted by Paddy3118 on 2009-02-19 at 06:56. 

::

   Is their ever a reason to **defend** non 100% statement coverage? The
   only psudo defence I can think of is that those missing statements are
   tested in a way that does not give results that can be collated in the
   same way.    - Paddy.


Posted by Titus Brown on 2009-02-19 at 10:11. 

::

   Paddy,    in practice I've found one or two situations.    Multi-
   platform coverage reports can be difficult to integrate -- e.g. one
   request I've had from Python-Dev is to provide an integrated view of
   code coverage from Windows, Mac OS X, and Linux.  But that's just a
   tools question.    The more real concern is that sometimes there are
   things that are **very** hard to test any way but manually.  Again,
   this can be thought of as a limitation of the test framework
   technology... but (for example) an aviation company writing code to
   send data to a flight box might not be able to test that interaction
   easily without hacking hardware.  Yes, you can mock the interaction --
   but then you're not doing proper integration testing that includes the
   hardware, are you...    So in practice I usually suggest &gt; 90% as a
   good baseline target.  Past that I find that increasing code coverage
   yields lower returns than regression tests or other such things.
   YMMV; I mostly work on FLOSS projects, so I (frankly) have a slightly
   lower commitment to 100% quality than I think a company should have ;)
   --titus


Posted by manuelg on 2009-02-19 at 13:53. 

::

   Titus:    &gt; ... So in practice I usually suggest &gt; 90% as a good
   baseline target.  Past that I find that increasing code coverage
   yields lower returns than regression tests or other such things.
   This is an excellent point.  This comment, plus your post make an
   excellent starting point for understanding where test coverage fits
   into sound software engineering.


Posted by Michael Foord on 2009-02-19 at 16:31. 

::

   Too right. Too often "testing is no silver bullet" is used as an
   excuse not to test.


Posted by Andrew Dalke on 2009-02-20 at 06:10. 

::

   I had a discussion about this recently with Glyph. He posted that 100%
   coverage was essential. My response and various followups at <a
   href="http://glyph.twistedmatrix.com/2009/02/joel-un-
   test.html">http://glyph.twistedmatrix.com/2009/02/joel-un-
   test.html</a> . Part of it is my assertion that coverage is not part
   of TDD, because of how refactoring works. Refactored code only needs
   to pass the suite, and code coverage isn't typically discussed as part
   of this step.    @Paddy: my defense for non-100% coverage by the test
   suite was that manual testing covered the 1% of the cases I couldn't
   easily test without a day or two of extra programming. Manual testing
   takes about 15 minutes. As it was, 99% coverage took 1 day over a
   project lifetime of 9 days. (It's ongoing, so my numbers are larger
   than I mentioned in Glyph's comments.)    I also give an example of
   auto-generated code, like a decision tree implemented in C. Failure in
   the code generation are likely correlated with failures in the test
   code generation. Of course you could hide things in a state table, but
   you still won't cover all of state space, which is the real goal.
   SQLite strives for 100% coverage. That task, and the story behind it,
   is something I would like to hear more about. Even with tool
   development specifically meant to support that, they haven't yet
   achieved it. They are at 99.37% statement coverage and 95.16% branch
   coverage, says <a href="http://www.sqlite.org/testing.html">http://www
   .sqlite.org/testing.html</a> .    Their consortium agreement at <a hre
   f="http://www.sqlite.org/consortium_agreement-20071201.html">http://ww
   w.sqlite.org/consortium_agreement-20071201.html</a> calls for 95%
   coverage. Try that clause in your next collaboration agreement. ;)


Posted by Chris Perkins on 2009-02-20 at 13:05. 

::

   I could not agree with your sentiments more.  I have had the argument
   with other developers so many times whether or not coverage is
   important.  I can tell you that I have worked on projects that had no
   notion of coverage, and projects that did.  The projects with coverage
   were easier to maintain, were easier to refactor and were more robust
   in their functionality.  I can't count the number of times I find bugs
   while finishing that last 10% of coverage.    Here are my
   recommendations for coverage percentages:    85% bottom bar for heavy-
   handed development (read: sprinting)  90% for alpha-quality code.  95%
   beta release is practical.  100% formal release.    Let's face it, TDD
   is only practical to some extent, so you are going to spend a certain
   amount of time writing tests after you have something "working".  If
   you look at this time as part of the maintenance of the project, and
   set goals for release that include coverage gateways, your product
   will be more stable.  I use this principle for www.sprox.org, and it
   has served me well, very few bug reports have come in.    I agree
   absolutely that branch coverage is more important than coverage, but
   that is not to say that coverage should be ignored.  Coverage provides
   a nice metric and a good starting point.  One question I have is:
   Does Python provide a good branch coverage tool?    cheers.  -chris


Posted by Andrew Dalke on 2009-02-20 at 14:13. 

::

   Can anyone point me to a non-trivial package (10K SLOC or more) which
   has 100% code coverage in the unit tests? And which counts as having a
   "formal release"?    I hear the advocacy for it, but I again point to
   SQLite which has put a lot of work getting to **nearly** 100%, and
   hopes to get the rest of the way some time this year.    I want to
   know how I should test for malloc/new failures, how to test for
   network hiccups, how to handle failures with the file system. The only
   thing I can come up with is having mock objects for everything, or a
   shared library shim, which can insert failures in the right locations.
   But writing  full isolation layer for anything involving the outside
   world seems like a lot of work, and fragile in the face of code
   changes. I want to see what people have done for this.    @Chris? Is
   any of your code available for me to look at?


Posted by Ned Batchelder on 2009-02-20 at 20:57. 

::

   Hey! Why did I get lumped in with the Eeyores?  I started my post with
   "Coverage testing is a great way to find out what parts of your code
   are not tested by your test suite."  I was just trying to point out
   the same thing you are: even with 100% coverage, you have a lot to
   learn about what your code does.


Posted by Titus Brown on 2009-02-20 at 23:46. 

::

   Andrew, beautiful discussion with Glyph.  Thanks for the pointer!  The
   sqlite stuff is also awesome and something I hadn't seen before.
   Ned, I object to your headline, not your article.  I **know** you're
   into coverage ;)    --titus

