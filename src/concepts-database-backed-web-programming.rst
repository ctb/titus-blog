Concepts in Database-backed Web Programming - a Post-Mortem
###########################################################

:author: C\. Titus Brown
:tags: python,teaching
:date: 2008-12-27
:slug: concepts-database-backed-web-programming
:category: teaching


(This blog post is a long, rambling retrospective on my recent
undergrad comp-sci course at Michigan State U., newly renamed to
"Concepts in Database-backed Web Programming".)

I set out this term to teach a CS class in the way I would have wanted
it taught when I was an undergrad.  The class was `CSE 491:
Introduction to Database Backed Web Development
<http://ged.msu.edu/courses/2008-fall-cse-491/>`__, the place was
`Michigan State University <http://www.msu.edu/>`__, and the audience
for the class was a group of 30-odd undergraduates, with a few
graduate students mixed in.  The range of prior experience with
programming, Python, HTML, JavaScript, SQL, etc. was pretty broad:
some students were crackerjack PHP Web programmers; others had never
seen Python and had no experience with Web programming whatsoever.

You can read about how I pitched the class on the `course Web site
<http://ged.msu.edu/courses/2008-fall-cse-491/>`__, but what I planned
to do was throw the students into the deep end by introducing them to
a range of new technologies and approaches, all in the context of
developing a database-backed Web site.  Michael Carter (`the Orbited
guy <http://cometdaily.com/people/michael_carter/>`__) convinced me at
PyCon '08 that I should teach the technology more or less from
scratch, by taking them through network programming, building their
own Web server, and writing a Web app.  So this is what I did.

I was in a bit of an odd situation, having been hired for a Computer
Science faculty position with no degree in CS and scarcely any CS
background.  (My BA is in Math and my PhD is in Developmental
Biology.)  Why was I hired, you might ask?? Well, I've been working as
a computational scientist for `over 15 years
<http://en.wikipedia.org/wiki/Avida>`__, I'm firmly embedded in the
open source world, I luuuuve agility (note, `small a
<http://steve-yegge.blogspot.com/2006/09/good-agile-bad-agile_27.html>`__),
and I do a certain amount of `bioinformatics research
<http://ged.msu.edu/>`__, so I managed to convince the CS department
that (in addition to my amazingly buzzwordy and sexy research
interests) I could bring some useful skills to the CS department.  It
didn't hurt that MSU had already decided to try out Python for its
intro programming course for majors, either.

Now, as `any
<http://www.codinghorror.com/blog/archives/001035.html#_jmp0_>`__
`programming
<http://leahculver.com/2007/05/30/a-computer-science-degree-doesnt-hurt-much/>`__
`wonk <http://www.joelonsoftware.com/items/2007/12/03.html>`__ `knows
<http://steve-yegge.blogspot.com/2006/07/wizard-school.html>`__, us
actual *programmers* know how to teach programming far better than
those ivory tower academics do.  And since I regard programming as
necessary, if not sufficient, for a Computer Science undergrad degree,
I decided to focus on teaching programming.  So I discarded my ivory
tower academician status & set out to do a better job of teaching it.
(That's only partly sarcastic, BTW; I don't know many CS professors
who think we do a stellar job of teaching programming.  Of course, I'm
equally sure that people like Yegge and Spolsky don't have the answers
either!)

My goals were simple, if not easy: teach students about programming a
real app, while introducing modern methods and iterative development.
If they happened to learn something about Web programming on the way,
so much the better.

Now, my *plan* was to discard as much unnecessary cruft as possible
and teach the young 'uns how to actually *program*, in some modern
useful language, while throwing as many new concepts as possible at
them and encouraging them to scavenge online.  Specifically,

 - no prior Python experience was required;
 - Subversion use was mandatory;
 - homework could be collaboratively done, or not: all I cared was
   that the students could explain their work upon request;
 - code could be taken from anywhere and anyone, as long as students
   understood the code they'd used;
 - the class was programming-heavy, with weekly assignments;
 - attendance was left to the students, i.e. no mandatory attendance;
 - all my notes were (and are) open;
 - my notes were *intentionally* incomplete, with the idea that students
   should have to use other resources (e.g. the Web) to find answers;
 - my primary concern was that their code run to my specs, and I provided
   automated tests for that purpose;
 - the central class project was a continuing one, and I would dock
   points for things that hadn't been fixed from the last homework;

I should mention that this was my first solo course, and I was
developing it from scratch, while setting up a new lab and research
program, moving into a new house, and helping take care of my 1 yro
daughter.  So it was a tad overambitious to develop a new course, with
a new approach, as my first ever professorial experience.  (The next
time so many people tell me I'm being insane, I may listen.)

The bottom line is I think I did an OK job, with some notable
failures, and (time will tell) hopefully some successes.  Since I
regard `failure as "good"
<http://weblog.raganwald.com/2005/01/what-ive-learned-from-failure.html>`__,
in that mindset, I offer the following `retrospective
<http://jamesshore.com/Agile-Book/retrospectives.html>`__.  All of
these issues below were surprising to me. Some, in retrospect, should
have been obvious & were the results of insufficient planning; others
were simply surprising and I don't think I could have anticipated
them.  And then there's the issues the students themselves had to
point out to me in the end-of-class survey...

1. **There was very little duplicate homework, as far as I could tell.**

One surprise was that almost everyone handed in homework they wrote themselves
(or, their attempts at obfuscating their duplication worked :).  Since I
didn't require independent work I was expecting more duplication.

Occasionally I got two people who had made exactly the same mistake,
because they were *working* together.  But their logic was similar,
not their code.

2. **People rarely took advantage of last week's solutions.**

Students really wanted to do the work themselves, and even when I
handed out solutions to the previous homework they built on their own
code almost exclusively.

This also led to some entertaining situations where people programmed
themselves into a corner, but that's called "gaining valuable
experience", right?

3. **Students don't like to ask for help.**

My homework assignments varied widely in their difficulty, but students
rarely asked for help, especially towards the end of the course.  I like
to think this is because they got better at doing the work but I was told
that "they figured me out", which seems to mean that they got used to the
way I asked questions and what kinds of things I wanted them to do.

4. **Students generally do all their work at the last minute.**

The majority of students almost invariably did the homework the night
before.  This meant that when I handed out a more difficult or
time-consuming homework, there were more complaints and less good work
than when I handed out easy homework -- even when I *told* them that
it was going to be a lot of work this week.  This was intensely
frustrating to me, but completely understandable.

5. **Even though I broke down the problems, they were still big.**

If you look through the homeworks, you'll see that I broke down the
problems into pretty manageable chunks.  (One of my friends taking the
course pointed out that all the hard work of abstraction was already
done in the assignments!)  At least at first, students had trouble
digesting these chunks.

I trace this difficulty back to two root causes: first, I did not
always hand out self-contained homework assignments, so students had
to put in a bit of work to figure out extra components were needed.
This is in contrast to what I think is the typical undergrad CS
assignment, where the problem domain is completely covered in class
and if you're smart (and the professor doesn't make mistakes!) you can
do the HW without going beyond the handouts and the book.  Second,
students are relatively unused to pure programming assignments: most
classes ask for something conceptually difficult, and I don't think
much of the HW for this class was difficult.  In contrast, I assigned
a fair bit of programming and problem-solving and I got the impression
that students -- especially the less experienced ones -- had trouble
with sizeable programming problems.

6. **Writing consistent homework assignments is tough.**

My homework assignments were all over the map in difficulty, for reasons
that seem clear in hindsight but were not so obvious when I was writing
up the syllabus!

7. **Students improved dramatically over the term.**

I started out with what I thought were simple assignments, and
students said they were too hard (and did poorly on them).  I lowered
the level a bit, which left them them challenging and significant but
not as difficult.  Towards the end of the term, though, most students
started acing every homework; they'd actually learned something during
the term, you see... and I didn't adjust!

I'm pretty sure about half the class was bored for most of the second
part of the term.

8. **Properly introducing automated testing in a course is hard.**

I wanted one of the big novelties in this course to be automated testing.
Students aren't formally exposed to any kind of automated testing in
the normal CSE curriculum, and since I'm test-infected I thought it'd
be fun to introduce them to unit & functional tests.

I think I did an OK job with the functional tests.  We used twill to test
the basic Web stuff, and Selenium to test some of the JavaScript; I didn't
introduce the Selenium IDE until the last lab, for some reason, but other
than that I think the students got the idea at least.

Unit tests were much more problematic, though.  I couldn't figure out
how to require them to write unit tests on their own, and looking back
on the term I still don't know how I'd have done it.  So what I did
was supply unit tests as part of the homework.  The problem then was
that they regarded the unit tests as a metric to pass, and rather than
coding to the intent they coded to the letter of the tests.  It got to
the point where I had to choose between becoming a complete test
fascist and really specifying every jot & tittle in a test, OR giving
up and using the unit tests as **a** guide rather than **the** guide.
I chose the latter, and that's when I started pushing more on
functional tests, arguing to myself that we really cared about the
functionality...

I'll probably write more about this later, but I've come to the
reluctant conclusion that it's hard to teach real unit testing to
people who are relatively new to programming.  They simply don't have
the paranoid mindset that they need to have in order to properly write
tests.  This may have implications for poorer-quality programmers,
too.

9. **Subversion was a disaster (but it was probably my fault).**

By the end of the course, there were three or four people who had
irretrievably messed up their Subversion working repository, and a
dozen more who were still having problems periodically.

This was because I'm an idiot.

I made students hand stuff in through per-student private svn
repositories: homework #1 would go in homework1/, homework #2 in
homework2/, etc.  However, homeworks 4 through 13 were all related --
building a Web server -- and more and more files became reused from HW
to HW as the course went on.  So, students would drag & drop
subfolders from one HW to another HW... contaminating their next HW
with .svn directories from the previous homework.  This basically
wedged svn.

I don't know what I was thinking.

What I *should* have done was have them all work off of a trunk and
then use svn copy to make branches for each handed-in HW.  This is what
I'll do next year.

However, I have to say that TortoiseSVN shares some of the blame.  It
does not interoperate well with command-line svn, so students who were
primarily using Windows to work with their homework could not switch
to using command-line svn.  Grr.

10. **Making the homework gradeable is hard.**

It turns out it's not enough to assign homework that's targetted at an
appropriate problem and at an appropriate level.  Someone also has to
grade it!  And with 30-odd students, at 10 minutes a homework you're
going to need 5 hours to grade it... so it behooves you to make
homeworks that are easy to test at a functional level!

I started out by writing automated scripts to run through and test
various behavior.  This was great when everything worked, but sucked
for broken homework -- that homework had to be graded individually.

My first grading innovation was to print out each homework assignment
and look at it.  I could usually scan for common mistakes and mark
points of interest within 30 seconds; once I'd finished scanning all
the printouts, I could run automated tests to verify that everything
worked, and when it didn't, my visual scan had usually given me a
pretty good idea of what was wrong.  Printing out the homework worked
until the homework got too long -- by the end, the average homework
was well over 400 lines of code.

My next grading innovation was to write a fairly thorough set of functional
tests at the Web server level, using both twill and Selenium.  This worked
great once the basic networking functionality was complete, and also
highlighted a number of places where my unit tests had passed the homework
but the HW was broken at a higher level.

Towards the end, though, I simply had to run their Web server and test
it in my own Web browser.  Since I had introduced Selenium by around
week 10, I could require that they hand in Selenium tests, and I could
also swap in my own Selenium tests for automated testing purposes.  It
still took hours and hours and hours, but it was easier.

Next year I'll probably include more specific hooks in each homework --
"the file must be named this, must be importable, and must have a function
called x that does y and z".  I'll also introduce functional testing
at an even earlier stage.

Overall, though, grading homework was a huge time suck.  I'm going to
have to think about how to write more gradeable HW assignments next
year.  Of course, next year my TA will be doing the first pass
grading...

11. **If you only care that the code works, the students will hand in
crappy code that works.**

Any student of metrics will tell you that if you measure people's performance
in a few specific ways, they will game the metric.

In general, students didn't pay much attention to code clarity and
maintainability. A colleague of mind has named this typical CS HW
mentality the "dung beetle" model: students pile on more and more code
until it works, and then repeat the next week.  This had the expected
effect of tripping them up at various times, because they were
building on their previous HW!  But it still got ugly.

My favorite example of bad code was what students handed in when I was
trying to get them to call sock.recv in a loop, until they received
the specified number of bytes for a POST.  Reading just the right
amount here is critical, because their servers were blocking servers,
and so sock.recv would block once the client was sending no more.  To
require the correct behavior, I wrote a stub socket object that 
raised an Exception (rather than blocking), used dependency injection
to insert it into their code, and then checked for the right behavior.

The right code was something like this: ::
 
   while remaining > 0:
      data += sock.recv(expected)
      remaining -= len(data)

Now, many people had a fencepost error, ::

   while remaining >= 0:
      data += sock.recv(expected)
      remaining -= len(data)

and when I added the stub & exception, their code morphed overnight into
this: ::

   while remaining >= 0:
      try:
         data += sock.recv(expected)
      except:
         break
      remaining -= len(data)

This code passed my tests by waiting for the assertion raised by my
dummy sock.recv, and also worked fine for small POST requests -- but
it hung indefinitely on *real* data.  They'd seen the exception being
raised by sock.recv and rather than trying to understand the root
cause, they'd just ... handled it!

Bleargh.

Still, there were a number of students who seemed to just understand
that they should go through their code a few times and clean it up.
Reading their code was always a pleasure.

12. **Preparing properly for a course is a huge amount of work.**

I truly didn't realize how much work it was creating a lecture outline,
writing up lectures notes, creating a lab, writing up lab notes, creating
homework, and grading homework.  Good god.  I must have spent 20-30 hrs
a week on the course, and the quality of my work was not always high;
next year I might spend as much again, just getting everything up to
snuff.  After that I'll just have to tweak it, thank goodness.

13. **We don't teach simple troubleshooting logic well at MSU.**

Students simply don't know how to troubleshoot code -- it turns out
it's not an intuitive skill.  Who knew?

The number of times I made students go back and put in print statements
to figure out *exactly* what was going on ... <shakes head>

I will devote a lab or two to basic debugging and troubleshooting
skills next year.

14. **The language doesn't much matter (tho Python still rocks).**

About half the class started out with no Python background, but by the
fourth homework, everyone could use Python equally well.  The main
differences that emerged were between people who expressed themselves
clearly in their code, and those who didn't.  Python helped primarily
by eliminating a lot of the syntactic cruft that would have confused
matters.

15. **Knowing a subject well doesn't mean you can teach it well.**

I know basic network programming as well as most anyone, and I certainly
know my Python.  But explaining my programming and design choices to
students turned out to be quite difficult.  I knew all sorts of reasons
why the statelessness of the basic HTTP protocol was really great for
programmers, but I sure couldn't expound on them in front of a class
of people.

Being an expert is different from knowing how to teach the material!
And standing in front of a chalkboard lowers your IQ by at least 20 points.

---

So I have a lot of food for thought.  In addition to the systemic
improvements, for next year, I'm probably going to bump up the level
of the course.  I'd like to make it more of a "project" course; I'm
thinking of something like a three-way division:

 - 5 weeks of Python, network programming, HTTP, and building a Web
    server.

 - 5 weeks of SQL, JavaScript, CSS, AJAX.

 - 5 weeks of bashing on a real site, with a real framework.

--titus


----

**Legacy Comments**


Posted by Greg Wilson on 2008-12-29 at 17:32. 

::

   I'm impressed it went as well as it did --- my first time out with a
   new course has almost always been a disaster :-)  A couple of
   thoughts:    - If you can figure out how to teach debugging, please
   let the rest of us know.  In particular, if you figure out how to
   **assess** debugging skills, I'd like to hear about it.    - Have the
   students create tests for assignment N+1 as part of assignment N.
   I've had them doing something like this (writing specs for the next
   assignment as part of this one) for a couple of terms now, and it's
   worked pretty well --- I'll bet they "get" the purpose of unit tests
   quicker this way.    Happy Hogswatchnight,  G


Posted by Brett on 2008-12-29 at 18:12. 

::

   Thanks for writing this, Titus! My supervisor typically teaches
   software engineering and he runs into similar problems with his
   students.    As a student who has taken some CS courses (but honestly
   not that many as my bachelors is in philosophy and I only snuck in
   four CSE courses in my undergrad), teaching unit testing is damn hard.
   I always understood the overall benefit, but I always felt that I was
   under so much of a time crunch that they were not worth it. And even
   building on previous code didn't matter to me as I figured that once
   it worked it would continue to work. That was obviously false most of
   the time. =) Greg's suggestion sounds like a good idea, especially for
   when you potentially shift the spec for only a part of the code but
   not all of it.    As for the use of svn, I have never seen VCS usage
   taught properly ever. At Cal there was a shell script that simply
   copied your files to a class account into a directory for you and that
   assignment. About the only way I can think of having something for svn
   is to use tags since you can then simply check out their code with a
   common tag across all students.    Otherwise it sounds like you did
   what I wished more of my professors had done.


Posted by John Taber on 2008-12-29 at 21:08. 

::

   Titus,  great honest assessment.  Yeah, I think those of us coming in
   from outside have a more dynamic and different outlook to teaching.
   I've found very similar experiences as you have.  One answer I think
   is to really simplify and break work down to really small problems -
   making it more doable and have students gain confidence in small
   successes (kind of similar to agile programming).      It would be
   really cool to have a inter-campus project so students can learn
   collaborating on work with others they don't know and are distant. It
   could be fun for the students.      ps: I'm also interested in
   creating an open source teaching repository or wiki or something - let
   me know if there's some interest.


Posted by Daniel on 2008-12-29 at 21:09. 

::

   Posted by Greg Wilson:  &gt; - If you can figure out how to teach
   debugging,  &gt; please let the rest of us know.  In particular,  &gt;
   if you figure out how to assess debugging skills,  &gt; I'd like to
   hear about it.    Maybe some simple, fixed bugs could be lifted from a
   couple of interesting bug trackers, then ask the students to jot down
   every step taken to diagnose and fix it? Perhaps using a bug tracker,
   and having students help each other.     ISTM it's more about the
   process than the results, so practice and feedback are very important.
   Having them fix/contribute to two realworld (easy) bugs in any open
   bug tracker would be a cool GHOP-ish exam ;)    On a more general
   note:    One of my English teachers used the "grade your peer's work"
   trick, and IMHO it makes you pay more attention to shortcomings and
   abilities (i.e., you focus on developing a skill set instead of gaming
   the metric). It also lets students know their classmates' goals, who
   works hard, who is talented, etc.


Posted by Jonathan Ellis on 2008-12-29 at 21:55. 

::

   Hey Titus,    I agree with Greg -- sounds like it went about as well
   as could be expected.  That's a useful postmortem, too!  (I'm probably
   done with teaching, but you never know.)    A couple comments:    -
   I'm surprised to hear about interop problems between Tortoise and
   cmdline svn.  I used Tortoise for years and never had any problems
   switching between that and Eclipse or IDEA or other svn
   implementations.  I'm pretty sure Tortoise uses the "official" tigris
   libraries, too.  I suspect a PEBCAK. :)    - Networked program
   troubleshooting is especially hard for students.  Not only do you have
   to make sure that the internals are correct, but that the
   communications layer is, too.  It's quite a difficulty multiplier.
   One thing that Python is missing that can help (in some situations) is
   a good remote debugging solution.  Embedding a Python shell can also
   help, but probably not for what your students are doing.  (Several
   IDEs provide a stub you can add to your code to listen for a remote
   connection from their debugger, but that's a lot of effort compared to
   the JVM "it just works," not to mention that AFAIK none of the options
   there are free.)  SoC project?


Posted by cariaso on 2008-12-29 at 22:58. 

::

   Academic theory be damned, the print statement is still the basis of
   debugging.


Posted by Doug Hellmann on 2008-12-30 at 09:47. 

::

   When I was an undergrad, we had an operating systems course where we
   were handed the code for an OS simulator (this was before Linux was
   widely respected/available/etc.) and we had to change it in specific
   ways (to use different priority schemes to switch between processes or
   manage memory).  Maybe you can use some of the code from this semester
   as training material for those debugging labs next time?  Hand them
   the code and the tests that are failing, and tell them to fix it and
   "show their work".


Posted by Titus Brown on 2008-12-30 at 15:17. 

::

   Greg -- the N/N+1 idea is a good one!  Err, how do you specify what
   the tests should test, and how do you evaluate the quality of the
   tests, though?  (See?  I'm learning... :)    Brett, re VCS teaching, a
   number of students say they "saw the light" when I taught them svn
   copy... so I'll put that in earlier next year.    John T., keep in
   touch... actually, if you could drop me an e-mail so I have your info,
   that'd be great!    Daniel, the problem with things like bug trackers
   and so on is that the assignments are just too small.  I don't feel
   like this class, at this level, is sufficient to motivate the use of
   anything much beyond version control -- certainly not bug tracking
   etc.  I like the "peer grading" idea... have to think about how to
   work that in!    Jonathan, bite they tongue :).  PEBKAC indeed!  The
   problem seems to be in TortoiseSVN **not** respecting svn's official
   backwards compatibility policy.  I never took the time to really track
   it down, though.  Perhaps I will do so next term...    Introducing
   more tools must be done carefully.  Would introducing a remote
   debugger help, or it would it just contribute more intellectual "load"
   to the course?    Doug, that's a great idea!  Now that I know some of
   the problems they're going to have, I can make lab "problems" where
   they have to debug code from this year.  Great idea.    And yes, I
   mostly use 'print' myself...    --titus


Posted by Sheila on 2008-12-31 at 12:42. 

::

   To work peer-grading in, think of it as teaching code reviews, and the
   students could use a code review checklist when ranking a peer. For
   every assignment, you could rotate students in groups of three so that
   you have more peer review data to work with.    here's some ideas for
   a checklist    * correctness    * completeness    * clarity    *
   efficiency    * test coverage    * unit test cases coverage    * style
   * security?    * usability?    * common defects    * pick a review
   perspective: test, design, client, person on call at 4 am


Posted by Sheila on 2008-12-31 at 12:53. 

::

   Is there a way for 30 people to review changes before approving them
   for trunk? Maybe you could break the class into groups of 5 - 8, and
   then rotate people so that they have to work on another groups code
   for the next release -- since the majority of time in life one ends up
   working on legacy code and performing software archaeology.    Also,
   did you find that they understood continuous integration? I've
   suggested it to some students and got baffled responses.    I've also
   noticed a lack of understanding of dependency handling. This was for a
   java project -- They wanted to check all of the libraries into the
   repository. When I suggested using an artifact server I got baffled
   responses again.    and, they did not use build scripts, but did
   things by hand in eclipse.


Posted by Nes on 2008-12-31 at 13:52. 

::

   Wow. That brought back some memories. Especially point 10. For my
   Masters degree I went the TA route to fund my tuition. I had to teach
   an intro class plus tutor and grade some programming classes. One of
   the classes I had to grade was weekly homework assignments for
   assembly programming for a class of 40. The first couple homework
   assignments were not too bad, you could look over them at a glance. By
   the fourth week programs were getting past 100 lines and it only got
   worse from there. Holly mother of Moses, I would come into lab Sunday
   8am get out at 10pm to grade just one assignment! I doing automated
   testing and plainly giving 75% to the programs that seemed to work
   properly to save some time. But deciding on that other 25% of the
   grade and figuring out how much the students actually accomplished for
   the programs that didn't work was crazy. I would look at some programs
   and think that they were for the wrong assignment and discover that
   they somehow had been bent into shape to work for the new one. Fun
   times.


Posted by Titus Brown on 2008-12-31 at 14:18. 

::

   Sheila, thanks -- that sounds like a great way to start.    I was
   thinking about how to get the students to work on other people's code,
   but discarded it as too unwieldy for this last term.  I may try to fit
   it in next term.    I didn't even try to fit in continuous
   integration, mainly because the tools that are out there are very
   annoying to set up, and I believe in live demos.  Hopefully that will
   change by next year.    tnx,  --titus


Posted by Michael Carter on 2009-01-03 at 06:12. 

::

   Great post Titus.    We never did finish our conversation; I
   distinctly remember being sad because I realized this on my plane trip
   home from pycon, and I wasn't certain I'd convinced you that starting
   with network programming was the right idea. I'm glad that you gave it
   a try though, and I can't wait to talk to you about it this year at
   Pycon!    As for grading, you could take a purely functional approach
   where you run everyone's homework through a set of acceptance tests,
   and they get a grade based on how many they pass. If this is to steep,
   you can always grade on a curve in the end.    You could even give
   your students the option of having access to run your acceptance tests
   against their current code, so they know what there final grade will
   be at any point. But take 10 points off their score for not writing
   their own test suite.    Incidentally, if you are interested in
   working to create an "Open Source" version of this course, I'd love to
   help you out! I would be very excited to be involved in future
   iterations of this class.


Posted by Noah Gift on 2009-01-04 at 02:31. 

::

   Titus,    I still haven't reached the magic formula for explaining why
   someone should write tests, but it might make sense to make it like
   real life.    When you get bitten by not testing is when a program
   goes from being a toy program to a production program, and you have to
   change it or fix something thought was working.  Maybe a test could
   involve changing a homework assignment that would be very difficult if
   they didn't write unit tests.


Posted by Minhajuddin on 2009-01-04 at 12:32. 

::

   Wow, I didn't know that People teach how to create web servers in Grad
   courses.


Posted by Krishnan on 2009-01-04 at 13:39. 

::

   I would love to have an open source version of the course :)


Posted by Titus Brown on 2009-01-04 at 13:41. 

::

   Minhajuddin, it's an undergrad course.


Posted by Titus Brown on 2009-01-04 at 16:36. 

::

   Also see:    <a href="http://cs193h.stevesouders.com/">http://cs193h.s
   tevesouders.com/</a>


Posted by Dan Carroll on 2009-01-04 at 17:40. 

::

   Very interesting read.  This course seems like something I would have
   loved to take in college.  I look forward to reading through the notes
   on the course website, since I'm always looking for some fun side
   projects to work on.    A suggestion for grading homework assignments
   next time around: how about setting up an online code review system?
   The could hook into the SVN repositories, and allow you to easily log
   on and browse each student's submission.  You could annotate the code
   right there and provide a convenient way to give feedback (rather than
   manually printing out code and so forth).


Posted by David Mercer on 2009-01-04 at 22:32. 

::

   The college CS course I took that introduced unit testing was heavy on
   the Test Driven Design style of development.  You were given a
   somewhat small number of tests for the weeks HW that your prog had to
   pass, and you had to write your own for other cases/inputs, as you saw
   fit.  Of course there were additional tests used for grading various
   edge cases and such that you didn't see ahead of time.  Better hope
   you got those!  Of course some students wrote their tests after the
   fact :-). Points also were generally deducted for an insufficient
   number of tests.  Readability and style usually only came into play if
   you didn't pass all tests, in which case they might give you some
   points back for good looking code.    This was a large intro
   programming class, and eclipse and junit were used.  They had a custom
   grading server where you ftp'd in you files with pre-dtermined file
   names, and they were automatically run against the test suite.


Posted by Edward Waller on 2009-01-05 at 00:47. 

::

   I like the idea of working in groups a lot.  No other course really
   does much with group projects except capstone, which I haven't done
   yet.  But most real world work is done in groups it seems.  I also
   think this would help explain the usefulness of SCM, instead of
   students complaining about it all the time, and even suggesting handin
   (where you can only hand in one file at a time).  Anyway, I wanted to
   say that I really enjoyed the class overall.  It's my favorite CSE
   class so far, and I just wish it could have been a lot more
   challenging; maybe a separate class or something.  Hope it goes even
   better next time :).    P.S. If you used git you wouldn't have all
   those .svn folders everywhere causing problems =P.


Posted by picsiq on 2009-01-05 at 11:50. 

::

   Monique, a Leaf fan, originate this plumb persistent to believe. Now,
   let me core out that this was in no way an undertake to glory one pair
   is more wisely than the other. It was upright a core to official two
   things.


Posted by Jan Van lent on 2009-01-06 at 13:55. 

::

   A related blog post by Chris Okasaki:    <a
   href="http://okasaki.blogspot.com/2008/03/program-testing-for-sake-of-
   learning.html">http://okasaki.blogspot.com/2008/03/program-testing-
   for-sake-of-learning.html</a>    Some ideas:     - Allow people to
   submit/test there code at any time and return the number of tests
   passed.     - If you return only a percentage of tests passed students
   have to work out themselves a good number of tests to implement.     -
   Closer to the deadline the actual results of the tests and the tests
   can be returned as well.     - Would it be possible to write tests for
   unit tests? Or maybe tests for the properties that should be tested by
   the unit tests.     - It may be nice to have a system that easily
   allows students to use tests written by other students.    All of this
   of course requires that the interfaces are well specified up front.


Posted by Doug Hellmann on 2009-01-07 at 20:08. 

::

   You could use buildbot to automate test runs.  Students could initiate
   tests through the web interface, or you could trigger the tests based
   on commits.  Each time the tests are run, the results could include
   tests they write on their own and tests you provide for basic
   coverage.


Posted by Sheila on 2009-01-08 at 14:21. 

::

   good logistics suggestion    &gt; A suggestion for grading homework
   &gt; assignments next time around: how about  &gt; setting up an
   online code review system?  &gt; The could hook into the SVN    Google
   code uses svn, and you get a review app cooked in. If you don't want
   to use google code, you could still use svn and check out reviewboard.
   also, if someone wants to use git instead, I've seen lots of talk
   about using git **with** svn. lots of freedom. there


Posted by Ted Pollari on 2009-01-09 at 01:08. 

::

   Going off of the ideas put forward by Jan Van lent -- if you allowed
   them access to the results of the tests you would put their code
   through, what about giving /more/ information earlier on and reducing
   how much help or info any of your tools gave as the deadline got
   closer?  That might help encourage them to start on the assignment
   earlier rather than just before it were due -- particularly if they
   were the ones who knew they might need help.

