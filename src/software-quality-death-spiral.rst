The (Lack of) Testing Death Spiral
##################################

:author: C\. Titus Brown
:tags: python,testing,pycon
:date: 2008-03-25
:slug: software-quality-death-spiral
:category: python


At PyCon '08, I gave a talk on `testing and the OLPC project
<http://us.pycon.org/2008/conference/schedule/event/83/>`__ where I
referred to the "Testing Death Spiral".  My accompanying slide, which
aimed to be simple rather than comprehensive, had this scenario:

1. Write a bunch of code & manually test it.
   
   (Good so far.)

2. Start adding features over *here*.

3. Watch code break over *there*.

4. Rinse, lather, repeat

   (Where do *you* think this ends?)

----

OK, so that format doesn't really work in a blog post, but hopefully
you get the gist of the scenario.  This is a scenario I see a lot: a
project gets hacked together & works well enough that people start
using it; then the project starts to expand. Many new features are
added.  However, as these new (and presumably solid) features are
being added, the old code becomes increasingly ignored, uncovered by
manual testing, and fragile.

This is a simple consequence of an inescapable fact: the amount of
testing needed to detect `regressions
<http://www.answers.com/regressions>`__ scales with the number of
features.  Forget about finding *new* bugs in the code you just wrote
-- I'm talking about breaking *existing* code.

I have seen people attempt to escape this scenario in a number of
ways: improve the architecture and reduce internal linkages; open
source it; release early, release often; alpha- and beta-test it; stop
adding new features; and probably many more.  These are all good
thoughts, but they are all doomed to failure [#]_.  Nonetheless, I
wish you well.

The only solution I have found is this: write automated tests.

Before I continue, let me say: automated tests are not a panacea.
Writing good code is hard, getting your project "out there" is
important, exploratory testing is *mandatory*, and writing appropriate
automated tests is hard; there's a lot more to building software than
writing good, automated tests.  I stress that every time I talk about
test automation.  I just think automated tests are *necessary* [#]_.

Let us suppose, for the sake of argument, that you have some software
that is actively evolving.  Furthermore, this software has no
automated tests.  Every time you add a feature, you test the bejeezus
out of that feature in order to satisfy yourself that it works.  You
do this for every new feature that is added, and thus consider your
software to be solid.

I now have two questions to ask:

 - are you adding features in isolation from each other?  that is, is
   your architecture such that each new features only uses
   non-state-changing code from elsewhere in your project?

   (if the answer is yes -- are you **sure**?)  

 - do you completely control the packages, libraries, compiler,
   operating system, and hardware that your software runs on?

   (if the answer is yes, do you plan to never, ever, change any of
   those components?  and have you discussed these plans with anyone
   outside your development team? and do you *believe* your managers?)

I like to summarize these questions this way: **are you feeling lucky, punk?**

If the answer is "yes" to all of the above, then congratulations --
you are Apple, stuck at one point in time, and never planning to
release a new piece of software or hardware :).  Hopefully you'll do
better than Apple did *before* they decided to change and adapt...

If the answer is "no" to any of the above, I encourage you to read on.

I assert that even with a perfectly decoupled architecture, brilliant
software engineers, and nigh-complete control over the software and
hardware that you use -- in itself a dream software development
situation -- you will eventually need to add features that crosscut
that architecture, and you will also need to upgrade the compiler,
libraries, language version, operating system, and hardware.  In order
to make sure that your software still works, *each time* you add a
feature or change a component, you will have to retest every feature
and every piece of code.  And, if you have no automated tests, you
will have to do this manually.  Every time.

If you have automated tests, however, your development process could
look something like this:

1. change code
2. run tests
3. commit
4. test manually, do exploratory testing
5. find bugs, write automated tests to reduce bugs
6. goto 1

Even if you don't add any new features, this process applies to
library, compiler, platform, and hardware changes.  At the least, you
will be able to quickly determine if you've broken something that
you're testing for; at the best, you will be able to quickly and
confidently release new versions of your software.

.. ugly transition @CTB

Fundamentally, then, automated testing is important for *software
maintenance*.  And since the cost of software maintenance is a
significant portion of the cost of developing the software in the
first place [#]_, it behooves you to pay attention to anything that
will reduce the cost of software maintenance.  This is without even
considering other aspects of test utility, like increased developer
velocity, ease of refactoring, increased confidence in your software,
etc.

This maintenance situation is the scenario that led me into testing
(or, if you prefer, "illuminated me as to the importance of automated
tests by whacking me over the head with a clue bat".)

Let me assure you that this maintenance situation doesn't *just* apply
to large bodies of code, either.  I maintain a number of small
projects and having automated tests means that I simply don't release
code with regressions.  Moreover, when my small projects "grow up"
into bigger ones -- or, more frequently, are used in larger projects
-- I'm not stuck in a situation where I suddenly have to write a bunch
of tests to achieve stability.  I *always* try to grow my test
framework organically with the project, because I will *never* have
the time to put into writing tests from scratch for my bigger
projects.

----

So, automated tests are important for maintenance, and they are
critical for making sure that your old code still works while you
focus on new code.  Without automated tests, you will be doomed to
releasing increasingly buggy software as your body of code increases
and the *average* level of testing decreases.

Does this actually happen?

----

This is precisely the scenario that led to our consulting work with
`ARINC
<http://us.pycon.org/zope/talks/2007/sun/track1/084/talkDetails2>`__,
which went well.  (As in, they're adding new features with great
confidence after we helped them adopt automation tools and practices.)

----

This is also the scenario that leads to what Jamie Zawinski named `the
Cascade of Attention Deficit Teenagers
<http://www.jwz.org/doc/cadt.html>`__.  Open Source projects, facing a
continually increasing number of bugs, often opt to completely rewrite
their components in the expectation that *this* time, they'll get it
right.  This completely ignores our experience with software rewrites,
which suggests that (barring brilliance and luck) any rewrite will
contain as many bugs as the original software -- they'll just be
*different* bugs.  (As JWZ points out, though, it's more fun to write
*new* code than to fix the crud someone else wrote before...)

----

And, finally, it is also the scenario faced by the One Laptop Per
Child project, which has built a tower of cards on open source
software.  Their build system pulls in about fifty distinct packages
*live from the Internet*, compiles them all, and then layers the Sugar
user interface on top of them.

There is no automated testing in place.

----

OK, back to the Software Testing Death Spiral.   What happens to
projects that lack both automated tests and an exponentially increasing
team of testers?  Starting somewhere in the middle of the process:

1. They manually test the new features and bug fixes that they've just added.

2. They release their software.

3. Their software breaks in unexpected locations, bug reports are
   filed, and (optimistically) those bugs are fixed.  Go to #1.

The inevitable consequence is a death spiral, barring only a complete
rewrite (which will possibly fail, or likely lead to a product that's
just as buggy, but with unknown bugs), trashing of the project, OR
-- and this is an optimistic scenario -- the adoption of automated
testing.

----

Here are a few straw men, with moderately snarky replies:

**"We don't test, and we don't use version control.  Which is more
important?"** Version control.  But you're doomed, anyway.

**"We don't have time to test."** Why do you have time to write
software, but not time to make sure it works?

**"We don't have the expertise to build good tests, and/or we can't
afford the tools, and/or we don't know how to use them."** This is a
pretty realistic scenario, actually.  May I suggest: hire consultants,
or read some good books, or dedicate your young new hire to learning
the tools?

**"We don't like to test."** Well, at least you're honest ;).  I would
summarize your choices like this: either you can write crappy
software, or you can learn to like testing.  The former will most
likely doom you to the rubbish bin of history.  The latter gives you a
better chance of "making it".

**"We really do plan to rewrite our software in two years."** Points
for honesty, again!  I think you're rolling the dice -- many software
projects fail, but maybe you'll do better.  Might I suggest an
incremental rewrite rather than a complete rewrite?  (For that you'll
need testing, though...)

**"We wrote a bunch of automated tests.  They didn't help us.** Ahh, a
problem based in actual experience!  I would like to suggest -- with
no background in your particular problem -- that you try out several
different kinds of tests, like functional tests or regression tests,
and see what *does* help you.

**"How do I test, if I don't know what the right answer is, anyway?"**
How do you know you *got* the right answer, then?  If your customers
don't care if you're right, then you've stumbled into a gold mine, but
I daresay it will end badly.  (This straw man was actually sighted at
PyCon -- sorry, MC.)  I hear this a lot in research, actually, but
it's still nonsense.  Perhaps another blog post in there...

**"I can't convince my boss/team leader/PI that it's important to
spend the time to write tests.  (I even sent him/her your blog
post.)"** You could go one of three ways: try harder, integrate
testing into your personal development strategy and view this
situation as an opportunity to "manage up", or quit.  The middle
option is the interesting one: you can quietly start
writing automated tests to "fence in" your own code, and explain to
your boss that this is just how you code -- it's like using emacs
instead of vi -- and you're not insisting that anyone else follow
suit.  Hopefully your productivity will not decrease much, while
your reliability will increase.  Good fellow programmers may follow suit
and at some point your manager might realize that you've all evaded
his dictat.  Or not.  But it beats working on untested code!

**"I am but one lone programmer, and I can't convince my team to
write/use tests.  (I even sent them your blog post.)"** See previous
question/answer: you will find that most worthwhile programmers are in
favor of anything that increases their productivity and reliability.

**"There's so many other things to straighten out on my project before
I can even think about what tests to write."** I sympathize, I really
do, but if your project is so undirected that you can't even figure
out what it's *supposed* to do (and write tests for it) then you have
far bigger problems than bad code to worry about.

**"I took your advice and wrote tests.  Then we changed a bunch of
stuff, and now all the tests break, and I don't have time to fix them.
What do I do now?"** Hmm, this is a common complaint. First, try to
separate out a subset of the tests that are of *immediate* use to you
(as in, they pass and/or they exercise a lot of your code).  Keep that
subset working.  Second, don't be afraid to simply *delete your old
tests*.  Tests should not be a maintenance headache; if you like and
use tests, but don't see the point of maintaining a bunch of your
broken tests, get rid of them!  Then put new ones back in as
necessary.

----

There really are a bunch of other reasons to write automated tests, too.
For example, consider:

 - cross-platform development is dramatically simplified when you have
   a moderately thorough test suite.  In particular, you can develop
   on your favorite machine, in your favorite programming environment,
   and let the continuous integration boxes run and test your code on
   all the other machines.

 - setting up new development environments and development machines is
   much easier when you can simply ... run the tests to figure out if it's
   all working.

 - integrating new people into the development team is much easier when
   they can run tests to figure out if they just broke something.

 - releasing "a quick bugfix" is a lot easier when you can be fairly
   confident that your quick new release is no more broken than your
   last release.

If these aren't enough to make you think seriously about testing, then
I give up!

----

There's no real conclusion to this :).  I'll talk more about the OLPC
stuff later.

Don't get me wrong: testing is *hard*.  Testing effectively is even
harder.  There are ways around this, but the best way to start may be
to simply power through: write a bunch of tests, and ruthlessly
discard those that don't help.  Then refine your method over time.  I
have some advice to offer here, too, but that's for another blog
post...

And remember... `Darth Vader recommends testing!
<http://www.flickr.com/photos/sebastian_bergmann/2282734669/>`__

--titus

p.s. Thanks to Tracy Teal, Lisa Crispin, Alex Gouaillard, Kumar
McMillan, Shannon -jj Behrens, and Doug Hellmann for comments!

.. [#] E-mail me if you think I should write about why :)

.. [#] I can blog about "necessity" vs "sufficiency", too.  Let me know.

.. [#] I've heard estimates of 80-90% of the total cost of development
   for a successful software project, i.e. initial feature development
   is 10-20%, maintenance is 80-90%, but I have no good references for
   this.


----

**Legacy Comments**


Posted by Peter Bengtsson on 2008-03-25 at 10:06. 

::

   The one thing that gets me hooked on automated testing is that they're
   for **you**, the developer. Not anybody else. And re-running the tests
   gives you quick feedback on your development.     That was one of the
   best arguments you articulated at the PyCon tutorial.


Posted by Louis DMeglio on 2008-03-25 at 14:29. 

::

   Great post.  As the one that's been running QA for my company for
   about a year I can tell you you've hit the nail right on the head.  At
   various times in the last year I've wanted to use every one of your
   straw men at least once.  Luckily, we pushed through and accomplished
   the level of testing we had to.  Thanks for verbalizing the pain of QA
   so well.


Posted by Jesse on 2008-03-25 at 16:16. 

::

   I come from a QA background, and helped build out an entire team of
   Automated testers where I work that are solely dedicated to writing an
   maintaining a suite of regression tests defined by QA, and reviewed by
   development.    A many times within the history here, we've been close
   to a 1:1 ratio of Automators to Developers - we actually carved out a
   role solely for test engineering ( like the google title more than
   ours ). the test code is in some cases, more complex than the product
   code due to the nature of the test we have to perform.    Testing is a
   critical, critical thing - for all software. It's like a good chef,
   you know the Chef cares about what he's cooking for you, because he is
   tasting it regularly to ensure it's not crap.    Bad chefs are the
   ones who can't, or won't taste their food as they are cooking it.
   The same applies to QA and Automated testing. QA, as a discipline,
   needs to accept Automation as a role and function within the greater
   testing Arena (and ditch the "manual or slightly above manual
   mentality) and Developers need to embrace it as a "proof" of what they
   have done.    I love this post.    I was also, unfortunately, the
   crazy guy who whooped when you had the picture of your kid in google
   garb at pycon :)


Posted by tomvale13 on 2008-03-25 at 17:51. 

::

   Coming from a tester, cheers.    I may use this post as leverage for
   that payrise I'm hunting for.    thanks again,    keep up the good
   work.    Tom


Posted by Ted Henry on 2008-03-25 at 18:46. 

::

   "How do I test, if I don't know what the right answer is, anyway?"
   When I am doing exploratory programming or prototyping (the prototype
   does end up being the product) for the first 50-75% of a project there
   is no way I can justify writing tests. I've tried writing tests in
   this phase and it is ridiculously wasteful. I end up writing at least
   5-8 times the software because I have to rewrite the tests at least
   4-7 times. I literally don't know what I'm programming because my
   client doesn't know what he wants and changes his mind every time I
   show him a demo. The prototype and demos are the spec writing process.
   I think testing is great but to invest time in writing tests
   (sometimes very difficult to write certain tests) I want to be
   reasonably sure that the tests will survive to the end of the project.


Posted by Titus Brown on 2008-03-25 at 20:34. 

::

   Hi Ted, I suspect we program in the same way, but I may start testing
   a bit earlier than you :).  I find functional tests (that test the
   external API more than the internal functions) can be really useful
   for making sure that important stuff stays working.    I am skeptical
   that you can't or don't solidify a project until it's 50-75% done.
   Maybe we have different definitions of "done"?  At the point where
   you're half done with a project, you shouldn't be changing core
   interfaces that much!    TDDers would say that you can do a better job
   of laying out the project (and avoiding rewriting) by writing the
   tests first, but YMMV.    Anyway, regardless of definitions and
   percentages and types of testing, there **is** a term for what you say
   you do: it's called "incurring technical debt".  The idea is that when
   doing exploratory or prototype programming, you ignore good software
   practices and focus on figuring out what the right direction is.
   Then, after you have figured that out, you can start improving the
   quality of the code and doing things like testing.  I like this term
   because it implies a balance sheet, where each additional bit of
   untested code you write incurs a "testing" debt.    Personally I have
   found that the sooner I integrate testing into a project the easier it
   is, but again, YMMV.    --titus


Posted by Topher on 2008-03-26 at 02:46. 

::

   No wonder you had problems.  It's "Lather, rinse, repeat".  Yeesh.


Posted by Titus Brown on 2008-03-26 at 03:26. 

::

   :)    I usually do like to get my hair wet first...


Posted by Titus Brown on 2008-03-26 at 03:36. 

::

   :)    I usually do like to get my hair wet first...


Posted by Peter Kehl on 2008-03-26 at 08:23. 

::

   hi Titus,    good article. Please, would you write something on
   "necessity" vs "sufficiency"? As to what else is important to prevent
   death of a SW project.    thx


Posted by Peter Kehl on 2008-03-26 at 08:29. 

::

   hi Titus,    I can't find RSS feeds for your blog. Does it have any?
   If not, are you thinking of some, or do you know whethere there's any
   external web service that generates RSS out of a web url?


Posted by hans on 2008-03-26 at 11:25. 

::

   <a href="http://us.pycon.org/zope/talks/2007/sun/track1/084/talkDetail
   s2">http://us.pycon.org/zope/talks/2007/sun/track1/084/talkDetails2</a
   >    "Item(s): Release Form not on File"


Posted by Blog Hatah on 2008-03-26 at 16:56. 

::

   You can't test everything. Also are you spending your time
   economically?


Posted by Titus Brown on 2008-03-26 at 17:56. 

::

   Peter -- see "atom" over on the left.  Those are equivalent to RSS
   feeds, I think.    Blog Hatah, it's true that you can't test
   everything, of course!  Nor should you try in my opinion.  The
   question is, do you test **at all**?  If you don't test at all, you
   don't have a chance of testing **enough**.    The question of
   economics is of course an issue, but I think I give some pretty strong
   reasons why testing gives good value for effort.


Posted by cariaso on 2008-03-27 at 19:04. 

::

   Ted,   I think you and I come from similar environments. Testing is
   great, but it is also the fad du jour. Should we be doing more
   *testing? yes!   *protyping? yes!   *design? yes!   *HCI testing? yes!
   *formal proofs? ugh, if you're into that.  *    Tests are only one
   tool in the developer's bag of tricks, and they aren't appropriate for
   every job.    Titus,  <a href="http://suicyte.wordpress.com/2008/03/27
   /strange-paper-i/">http://suicyte.wordpress.com/2008/03/27/strange-
   paper-i/</a>  made me curious for your take. This has been 'broken'
   forever, and when corrected it doesn't seem to help anything. This is
   one of the pillars bioinformatics.     What is a testing advocate's
   take on this?    Scenarios like this make me feel like updating the
   legacy tests could be the hardest part of the correction. Would you be
   willing to update a large number of legacy test cases to correct for
   this?


Posted by Titus Brown on 2008-03-29 at 11:43. 

::

   Hey Mike,    I can't think of any real situation where testing isn't
   useful; I can think of lots of places where prototyping, HCI testing,
   and formal proofs aren't.  Have you ever written a piece of code that
   you haven't run?  Isn't that a test, of sorts?    The BLOSUM stuff is
   interesting.    The only practice that I could see really having
   caught that bug up front is doing TDD or BDD, where you figure out
   ahead of time what the answer should be for a specific situation and
   then assert that that IS the computed answer.  But it's tough: the
   more complicated the algorithm, the less likely it is that you'll be
   able to write code that way.  (My conception of testing isn't that
   you're supposed to catch all the bugs up front -- that's basically
   impossible for any real piece of software.)    Re fixing the legacy
   tests, most of my tests for BLAST and BLOSUM would have little or
   nothing to do with the BLAST algorithm per se; they'd have to do with
   file loading, string handling, alignment building, etc.  And, as I
   advocate in the article above, if so many tests were "broken" by
   fixing the BLAST code that they weren't useful any more, I'd delete
   them.  Useless tests are just that: useless.    --titus


Posted by cariaso on 2008-03-30 at 19:22. 

::

   "I can't think of any situation where testing isn't useful"    Last
   week I wanted to color code a score from 0 to 1. A score close to 1
   should be very visually emphasized, a score close to 0 should belend
   into the white background. What was unclear was just how intense a
   score of .95 should be, and how musted a .15 should be. In the end I
   chose to take score**4 as producing a visually pleasing balance. To me
   this code seems not worth testing. There is no right answer, only
   current behavior. Some variations from current behavior are likely as
   I refine the code. But any surprise changes are certainly a bug.
   Testing could help me, but not enough to be worth the effort.
   Have I ever written a piece of code that I've never run? frequently.
   I write behavior for rare conditional branches. I usually have no test
   data for these 'corner cases' and as long as I log a message saying
   'doing X at <em>_FILE_</em>,<em>_LINE_</em>' I often don't feel the
   need to actually test. If I were landing a man on the moon that
   wouldn't be cool. If I was color coding a report its perfect.    But I
   don't actually follow what you were suggesting when you asked the
   question  "Have you ever written a piece of code that you've never
   run?"        All of the test harnesses I've looked at add some work
   extra work. Its not that I don't see the value of tests, its that for
   some of my tasks they are more trouble than value. And there is no
   reason they can't be written next week. If they help you think about
   the problem you're going to solve, great. But sometimes I want unit
   tests. Sometimes I want a whiteboard. and sometimes I just want to get
   in there and see what I can make it do easily.    import eztesting  My
   dream testing library, silently instruments my code. It records inputs
   and outputs just like a memoize. It notices when the same input
   produce different outputs. It builds a profile of specific input
   output pairs, and notices general rules for code which isn't <a href="
   http://en.wikipedia.org/wiki/Referential_transparency_%28computer_scie
   nce%29">referentially transparent</a>. It builds up something akin to
   a profiler log, but it extends over multiple runs and even months
   worth. Periodically it flags functions which have been run for a long
   time with specific input/output behaviors. And these are offered to me
   a good candidate regression tests, and perhaps exported into a new
   regressiontests.py file which I can 'svn add'. These tests are also
   small enough in scope that I think they can make good unit tests as
   well. And it monitors for when behavior on any of these tests suddenly
   changes. This is run on a smoke testing machine after each commit. It
   doesn't need to do anything more than some extra auditing during
   typical runs.     It doesn't seem all that hard to build something
   like that. It doesn't need to test everything, it just needs to add
   some new capability without getting in my way.


Posted by cariaso on 2008-03-30 at 19:33. 

::

   and re:"I can think of lots of places where prototyping, HCI testing,
   and formal proofs aren't."    really? Lets make sure we're speaking
   the same language.     When I say HCI I mean very end-user oriented
   testing. Does the user know what will be achieved, what inputs are
   necessary, what the outputs mean, and how to produce them? Is the
   significance of all data returned intuitive?     I've seen too many
   developers take their code to the level of believing that it is
   correct, and whether or not the actual users understood the results
   was secondary. Anything after the compilation step was considered
   stupid user error. This is sort of thing where I think the BLOSUM
   example shines. End users matter more than right and wrong.


Posted by Titus Brown on 2008-04-01 at 14:33. 

::

   Mike, I think that you're generalizing from some very specific
   situations (I can't write tests for the right shade of color!
   Therefore testing isn't worth it!) to the general statement that
   automated tests aren't useful for the majority of your code.
   Obviously I disagree and I think I give some pretty good reasons
   above.    It may indeed be that you're writing one-off pieces of code
   every day, but that has its own dangers: my own experience has shown
   that every piece of code I write has bugs in it, and the more I work
   with that code the more bugs I find.  That suggests that if I write
   code that I only use once and I don't find any bugs in it that once,
   then I'm just missing the bugs :)    I've only found one or two bugs
   that were **serious** in the sense that they altered published
   results, but I suspect more lurk :(.  Plus, we're both probably pretty
   good programmers in general; think back to your typical starting grad
   students and shudder appropriately!    The questions about code that
   you've never run were to point out that execution is, at its base, a
   form of testing (as long as it completes to your satisfaction, of
   course!)  **Everyone** tests code to that level (smoke and/or
   exploratory testing).  Automated tests help with regression detection,
   and many other things, but they're not good at finding **new** bugs.
   "End users matter more than right or wrong"... that's clearly wrong,
   at least if you're trying to do science.  I think you're confusing
   necessary (end users have to understand and care about the results!)
   with sufficient (it is NOT sufficient that end users understand and
   care about the results, those results must also be correct!)    As for
   eztesting, I'm working on something with Disney Animation that
   intersects with those ideas -- we think alike :).  I'm not sure how
   useful blind recording -&gt; test generation will be, but I'll let you
   know.    --titus

