(Some) Principles of Computational Science
##########################################

:author: C\. Titus Brown
:tags: science,teaching
:date: 2010-12-10
:slug: principles-of-computational-science
:category: teaching


I'm just finishing up my `Computational Science for Evolutionary Biologists <http://ged.msu.edu/courses/2010-fall-cse-891/>`__ course,
and I'm finding it tricky to come up with a good high-level summary of
what I would like them to take away.  As you can see from `the class
notes <http://ged.msu.edu/angus/beacon/>`__ they've done some
reasonably neat stuff with Digital Life and (separately!) next-gen
sequence analysis, but the class has been somewhat random in its
topics and train of thought.

Anyway, for the final class I decided I'd go slide by slide through
a number of principles that they should apply if and when they find
themselves doing computational science.  In each case I can point to
class exercises and homeworks that illustrate the points, which I think
means I haven't totally failed... ;)

Anyway, here's what I have so far:

----

13 Principles of Computational Science:

1) Computational science is just like any other science: don't trust it if
you don't understand it.

  Seriously.  Computers aren't magic, and computational jargon isn't any
  more meaningful than any other jargon.

2) The entire chain of evidence matters.

  Keep close track of the raw data; the analysis source code; and the
  parameters used at each stage of data generation, processing and
  summarization.

  Corollary: Make your raw data available.  To do otherwise is just silly.

3) If it's not automated, `it's crrrrrap <http://snl.itgo.com/sounds/scotcrap.wav>`__

  As soon as there's some manual step in your pipeline, you've lost track of
  what you're doing.  You may do it differently, or not at all, or incorrectly.
  And you'll never know.  You'll just get different results.  Sometimes.

4) Use version control.

  If it's neither raw data (backed up!) nor generated data, put it in version
  control.

5) Using other people's software to do science is hard.

  They probably had some other use in mind that doesn't fit your needs, but
  you're going to try to adapt it anyway, aren't you?  Good luck with that.

  Corollary: using your own software to do science, 2 years after you wrote it,
  is hard -- because you're not you any more.  (Remember, you can never
  step in the same stream twice.)

6) No software is trustworthy.

  Until you understand your software stack intuitively, have obsessed over
  parameter choices, and have locked down your software behavior with automated
  tests, don't trust it.  After that, you can grudgingly extend some minimal
  trust to it, at least until the next version is released.

7) Computation is not science.

  Science is science.  Computation may be one of the ways in which you do
  science.

8) Hypotheses are good.

  It's virtually impossible to analyze data without some kind of hypothesis
  in mind.

  Corollary: Each hypothesis is only a starting point.  It's probably wrong,
  so don't get too attached to it.

9) More data is not necessarily less confusing.

  The more data you have, the harder it can be to get a clean signal.
  Statistics help here, unless of course you have an unknown systematic
  bias in your data.

  Corollary: You have an unknown systematic bias in your data.

10) Interdisciplinary research is hard.

  You need to be an expert in multiple fields, each with its own special
  techniques, lingo, and "commonly understood" shibboleths.  Proper hypothesis
  testing involves mastering the first two; publication may depend on avoiding
  the latter.

  Corollary: computational science is implicitly interdisciplinary, hence
  hard.  (If it were easy, we wouldn't need smart people like you to do it,
  right?)

11) A lot of computing is just details.

  There's very little magical about computing.  An awful lot of it is just
  more details to remember.  Running software, gathering the results,
  processing them, plotting them, tweaking parameters, etc.

12) Look at your data.

  Look at your data, and your results, in as many ways as possible.  You'll
  often be surprised by what's actually in there.

13) Above all, tell a story.

  Nobody is interested in just graphs.  If you don't have an interesting
  story, dig deeper.

----

I know, somewhat scattered.  Any more thoughts, or pointers to similar lists?

thanks,

--titus

p.s. I plan to finish up with my (IMO very underappreciated) principles
of `How to be a Successful Computational Scientist
<http://ged.msu.edu/angus/files/how-to-be-successful-computational-scientist.pdf>`__,
summarized here:

1. Never show them your data.

2. Do not, under any circumstances, communicate clearly.

3. Never release your source code, either.

4. Judge computational science by results, not quality.

5. Use as much data as possible.

Then they get to fill out evaluations.  Whee!



----

**Legacy Comments**


Posted by Michael R. Bernstein on 2010-12-10 at 11:50. 

::

   Consider moving #3 to after #9, and adding a corollary: "Even if you,
   magically, always do things the same way, you should probably consider
   your involvement an unknown systematic bias".    Further, there is
   probably something missing about making the entire software stack
   reproducible if at all possible. It could be considered a corollary
   of #1-6 inclusive (except #5, it's actually a corollary to the
   corollary). Perhaps make a point about using virtual machines and
   backing up their images.


Posted by Noah Spies on 2010-12-20 at 11:10. 

::

   "Look at your data.  Look at your data, and your results, in as many
   ways as possible. You'll often be surprised by what's actually in
   there."    I find people tend not to fully understand this--looking at
   data in different ways to them means testing as many hypotheses as
   possible by calculating lots of p-values. Before you get down to that
   level, it's always helpful to get a feel for the raw data. A human eye
   can spot patterns incredibly quickly, and, for example, a little time
   spent browsing next-gen sequencing results in the ucsc genome browser
   can guide you to ask the right questions.

