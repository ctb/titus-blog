The One True Testing Approach: There's No Such Thing
####################################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2008-12-02
:slug: the-one-true-testing-approach
:category: python


The ongoing debate about doctests (`here
<http://faassen.n--tree.net/blog/view/weblog/2008/12/01/0>`__, and links
therein) seems to me to be somewhat silly.

doctests should be assessed by their utility to you and your project, in
whatever role you happen to be using them.  I personally find them to be
very useful in API documentation, where they can help show the API in
use while documenting it in a verifiably correct way.  I've also found
them to be useful in teaching, where both you and your students can
rely on your code examples to be correct, or at least to run properly.

Obviously you still have to write *good* API documentation, and *good* examples
for teaching; simply having a doctest isn't a guarantee of quality docs, just
like simply having tests doesn't guarantee that your code is tested.  I
personally find functional tests to "fit my brain" much better for actual
testing, and unit tests are often the second approach I use.  But I like to
write doctests, too, and I think they have their place.

So why is everyone talking about whether or not doctests are good?  I think too
many people are after the One True Testing Approach, an approach that they can
use, without thought and to the exclusion of all others, for their testing.

For example, Andrew (?) complains that `doctests are
narrative, and unit tests are less good when they're narrative
<http://andrew.puzzling.org/diary/2008/October/23/narrative-tests>`__. OK, so
you think people are misusing doctests... but maybe they have a place in
narrative tests, like API documentation or functional tests?

Before I mischaracterize Andrew's position too much, I should say that he
thinks unit tests should make up the bulk of automated tests.  While I don't
fundamentally disagree, I do think that's an extreme position that depends on
what it is, exactly, that you're writing.  Libraries are going to have
different needs than database-intensive apps, which in turn will be
different from AJAX-heavy Web GUIs, which will be different from
scientific apps.

In Andrew's `second post <http://andrew.puzzling.org/diary/2008/October/24/more-doctest-problems>`__, he complains that doctests have a number of drawbacks.
Hey, I agree with most of what he says -- but I think he's wrong, again, in
phrasing doctests as an *alternative* to xUnit-style unit tests.  I think
they're complementary.

Ned Batchelder chimes in with `more doctest problems
<http://andrew.puzzling.org/diary/2008/October/24/more-doctest-problems>`__,
which basically reiterate Andrew's complaints that doctests don't work as your
only (or even your primary) set of tests.  Again, I agree completely.  So, umm,
why not use doctests where they're appropriate, like in API example
documentation, and use unit tests for the rest?  Why should I choose to use
only one tool?

Martijn `wrote a nice post
<http://faassen.n--tree.net/blog/view/weblog/2008/12/01/0>`__ pointing out some
of the good things about doctests, and my experience with doctests echoes his,
frankly.  I think they're great for keeping basic API information up-to-date,
and I really like having executable documentation.  They also force you to
think in certain ways about your APIs, which can make the APIs better.

In sum, I'm saying that you should pick the kind of testing approach that gives
you the most bang for your buck (where "buck" is measured in time, or money, or
whatever).  That means that the testing approach of choice is going to be
context dependent, and that context includes things like the project itself,
the team, the language(s) being used, and your ultimate goals.  This may seem
like useless advice, but I think it's at the heart of productive testing: using
the most effective tools for the job.

A corollary to that view is that there is no **One True Testing Approach**;
there are just a lot of complementary approaches.  Figuring out which is
good for what purpose is part of the learning process!

I'd rather see the conversation shift to what doctests are good for, and in
that vein I encourage people to read all of the comments on `Martijn's post
<http://faassen.n--tree.net/blog/view/weblog/2008/12/01/0>`__.

--titus

p.s. If you comment, please drop me a note at t@idyll.org.


----

**Legacy Comments**


Posted by Rene Dudfield on 2008-12-02 at 23:31. 

::

   Hello!    Part of what makes xUnit good is that it is a standardised
   way across multiple languages to write tests.    This is what made
   testing so popular... along with all the X hype :)  All the
   information(blog posts, articles, books etc) could be used across
   multiple languages.  Just download phpunit, junit, pyunit, and start
   testing!    So it's not the one true way, but it is still going to be
   the most popular way.  Since you can use the basic idea for testing in
   multiple languages.    Note, that many C programs use a doc test like
   approach to testing.  They run some stuff, stuff gets printed out, and
   that printed output is then placed into a test file of expected
   results.    It's interesting reading the original paper on SUnit:  <a 
   href="http://www.xprogramming.com/testfram.htm">http://www.xprogrammin
   g.com/testfram.htm</a>    There's a few gems of wisdom missing from
   many xUnit frameworks... like each class returning a test suite when
   it receives a test message :)  Go package.object.test()!!    ...
   anyway... I like your points, and agree that it's good to use a couple
   of different methods for testing... and use doctests &amp; unittests
   myself.      cu!


Posted by Martijn Faassen on 2008-12-03 at 08:20. 

::

   Titus, thanks for this post. I agree with you. Doctests aren't a
   panacea, but neither is unittest. I hadn't considered that a "one true
   way" attitude might be influencing this discussion - that's an
   interesting analysis.    What prompted my posting was me getting
   annoyed seeing people heap negativity on doctests. It didn't really
   start out right: I was told I abuse them and I was told to stop!
   Anyway, I'm glad I decided to stay positive in my posting, as the
   discussion in the comments has remained at a high level.    Indeed:
   let's use the right tool for the job and the right tool for the people
   involved, and let's talk about what that means.


Posted by Noah Gift on 2008-12-04 at 05:16. 

::

   One of the other good things about doctest that I didn't hear anyone
   mention is that it is a great beginners testing framework.  If for
   that reason alone it should be given more respect.  Setting up
   impossible standards is a sure fire way to make sure people never
   write tests.  With doctests, it is so easy to write at least something
   basic, that there is no excuse for a beginner.


Posted by Titus Brown on 2009-01-05 at 05:07. 

::

   Also see:    <a href="http://paddy3118.blogspot.com/2008/12/yet-
   another-blog-entry-on-
   doctests.html">http://paddy3118.blogspot.com/2008/12/yet-another-blog-
   entry-on-doctests.html</a>

