Exhibiting aggressive competence
################################

:author: C\. Titus Brown
:tags: python,oss,education
:date: 2009-12-18
:slug: aggressive-competence
:category: teaching


This last term I facilitated the participation of five MSU students in
the `Undergraduate Capstone Open Source Projects (UCOSP)
<http://ucosp.wordpress.com/>`__ program, in which students do
distributed open source software development and receive home
institution credit.  UCOSP was managed out of U Toronto by Greg
Wilson, and I was (and am) enthusiastic to participate as it's clearly
a good way bring open source into education.

However, I was less thrilled to see that the majority of the MSU
students received, ahem, "less than passing" grades from their project
leaders.  I knew about the problems in one particular project from
having met with the students on a regular basis, but the other results
caught me by surprise.  I would love to kick and scream and complain
that I should have been made more aware of what was going on -- and
where I had constructive things to suggest, I did -- but the **more
important failure may have been a mismatch between the MSU students'
approach to these projects, and project expectations**.

The students variously had a number of problems, ranging from team
miscommunication & poor conduct to an inability to get the software to
compile.  This meant that for several students, **no visible work got
done** -- for example, in one project, it regularly happened that
person X was working on a patch, and person Y committed an overlapping
patch first.  Or on another project, person Z spent two months trying
to get the basic project infrastructure compiled, and was reduced (at
the very end) to submitting code fixes without testing them in the
full project context.  Or several times, person A spent a week working
out how to refactor a test into something reliable, and resulted in
what looked like (and maybe was) a trivial code change.

All of these situations may result (and **did** result) in low
evaluations.  This is understandable: **no visible work got done**, so
how is an evaluator supposed to grade them!?  Yet, all of the
situations are legitimate issues that block progress.  What is a
student to do?

The answer won't be too hard to guess for anyone who has worked on
real-world team projects: **make your struggles visible**.

Someone steps on your patch?  Fine -- submit *your* patch too, and
explain why it's better (or worse) than the first patch.  Code review
the other patch, while you're at it: who better to do the review
than someone who really understands the issues?  Then when you get
poor marks for not having contributed code, point at your patch.
(You *are* using version control, right?)

Can't compile the software?  Fine -- write down what's going wrong,
and post it publicly.  Document your fix attempts.  Ask for help.
Bash your head against the wall repeatedly.  Either fix the problem,
or document the problem thoroughly.  Either someone will help you, or
you'll figure it out, or you'll leave an audit trail so that others
won't have to do all that fail work.  Then when you get poor marks for
not having contributed any patches, point out that the project has
technical issues and either no one could help you (project FAIL) or
you spent all your time fixing them.

Trying to debug niggling details that turn out (in the end) not to
involve big impressive code changes?  Submitting too many unimpressive
patches that no one seems to value?  Write down why your contributions
are valuable.  At the end of the day the evaluation may (rightly or
wrongly) be "not too smart, but sure did work hard" -- but that's
better than "no evidence of any work having been done".

Note how a lot of this seems to involve **communication**?  Right --
that.  For team projects, being an effective communicator is more
important than being a kick-ass programmer.

At the end of the day, there are things you *can* control, and things
you *can't* control.  You can't control what other people think of
you, and you can't control how other people (including project leaders
and professors) evaluate you.  But you *can* visibly work hard, and
defend yourself based upon that evidence.

I call the general approach of throwing energy at a project
**"aggressive competence"**, and I think it's a necessary component of
effective team software development.  Everyone has days, or weeks, or
even months where they look incompetent or ineffective; often that's
because outsiders don't understand or appreciate the work that you've
done.  Tough on you, but I don't think it's reasonable to expect your
boss, or colleagues, to look hard at your work to find reasons to
praise you.  Fundamentally, it's your responsibility to "manage up"
and communicate your progress to others effectively.

In open source projects (and elective college courses) the immediate
ramifications of a poor evaluation may not be clear -- I'll leave you,
dear reader, to figure out the longer term consequences.  But I think
the ramifications of a poor evaluation are immediately obvious in the
context of a capstone course, or a paying job.

Incidentally, this illuminates one of the reasons why I'm such a big
fan of UCOSP: it *is* reality.  You're working on an existing project,
with other developers, at a distance; and it's not anyone else's
responsibility to frame the problem for you.  It's your responsibility
to make progress.

This is where I think there were mismatched expectations.  The
students expected that they were going to be managed, helped, and
given clear expectations.  They weren't.  So they got bad evaluations.

What do I plan to do?  Well, assuming that UCOSP + MSU goes forward
next term, I will be communicating *my* expectations quite clearly to
the students.  And I will be asking for regular progress reports,
sent to me and CCed to the project leaders.  And I'll be sending them
this blog post.  And I'll be failing the ones that don't listen.

I'll end with a paraphrase of one of my favorite sci-fi authors:
"every new developer has problems on a new project.  The extent of our
sympathy for those problems, however, will be dictated by the efforts
made to overcome them."

--titus

p.s. It's also a good way to figure what projects you don't want to
work on: I once got dinged for working too hard in a company; I was
told that I was "rowing too fast and the boat was going around in
circles."  My response (that perhaps others might consider rowing
faster) was not received well.  That's the kind of job situation you
can leave without guilt (as I did).

p.p.s.  Code reviews can be an extraordinarily effective
passive-aggressive way to correctively interact with jerks on a
project, too.


----

**Legacy Comments**


Posted by manuelg on 2009-12-18 at 19:59. 

::

   Everything you say is true, and very well put.  I will point people
   who deserve sound counsel to your blog post as well.    But the truth
   is that "aggressive competence" is hard for many people, and it is not
   unusual for a student to leave school without ever practicing this
   particular skill.  I would imagine a healthy majority of students
   would do whatever they could to avoid having to practice "aggressive
   competence" in their careers.    I will stress this skill to my own
   daughter, because I feel responsible to help prepare her for the world
   as it actually exists.  But I can easily imagine computer science
   majors avoiding the career of software development just to avoid the
   need for "aggressive competence", and into careers with far less
   demand for assertiveness, even if those careers are less
   intellectually rewarding and less lucrative.  (Because, as you put it,
   clear specifications and clear direction are so often lacking in
   software development.)    So we have students that could love
   programming, and will avoid careers in software development.  And I
   would be a liar if I said I knew how to repair that.


Posted by holger krekel on 2009-12-21 at 03:52. 

::

   Hi Titus, good post and thanks for taking the time to write down your
   insights, advise and conclusions.  Also, i am often wondering why
   universities don't try harder to involve CS students in Open Source
   projects and am happy to see that you are seriously trying to foster
   that.   cheers, holger


Posted by Paul Hildebrandt on 2009-12-23 at 19:01. 

::

   I think "aggressive competence" is really important in the work place.
   We work in small teams and every morning we have a stand up meeting to
   tell people what we are working on and if we have any problems.  This
   15 min meeting helps everyone get an idea of where the project is
   going.  it's also a great time to ask for help. Even better we sit
   close to each other and when someone has a problem they just call out
   "Hey I'm stuck can I get another set of eyes on this problem"  It's
   normally solved pretty quick and we keep making progress.  Time is
   money and the company doesn't care if you have help solving the
   problem they just want it solved, and the quicker the better.


Posted by Titus Brown on 2009-12-24 at 13:34. 

::

   Hey all, thanks for the kind words.    Holger, most professor-level
   academics just don't have much experience with open source!  That, and
   it's hard to fit it into a course in the right way.  You might be
   interested in this:    <a href="http://teachingopensource.org/index.ph
   p/TeachingOpenSource_Mailing_List">http://teachingopensource.org/index
   .php/TeachingOpenSource_Mailing_List</a>    Anyway, UCOSP is the best
   opportunity I've seen yet for introducing OSS in an effective way.
   We'll see how it shakes out next term, when I will be more heavily
   involved.


Posted by Ann on 2009-12-25 at 05:05. 

::

   Thank you for a great post!


Posted by Ann on 2009-12-25 at 05:06. 

::

   Thank you for a great post!


Posted by Doug Hellmann on 2010-01-03 at 13:42. 

::

   It sounds like you're giving your students excellent real-world
   experience.  The part of my college education with the highest pay off
   in the end was the time I spent as a graduate assistant working on a
   team building software for a bunch of geologists.  They were perfect
   customers: They weren't computer experts, so had no idea what we could
   make the software do or how long it would take.  That meant we had to
   work with them to establish requirements and schedules, and then go
   meet them on our own without a lot of help.  Stakes were lower,
   because deadlines were very flexible, but otherwise it was a great
   training ground for a "real" job.    For transparency at work, we rely
   heavily on a ticketing system for all significant tasks.
   Communication isn't really happening unless it's recorded in trac (in
   our case).  Notes from hallway conversations, meetings, etc. are all
   entered as comments on the appropriate ticket (giving us a historical
   record as well as a chance to clarify or correct the understanding of
   whoever makes the notes).  Writing everything down is our way of
   establishing an institutional memory, which has come in handy quite a
   few times in the 8+ years I've been on this project when no one could
   remember the origin of a feature or design decision.     Progress is
   reported in terms of closed tickets, rather than code written.
   Requirements become obsolete or change and not every task in support
   of a release requires development of a new feature, fixing a bug, or
   writing docs.  Code reviews, doc reviews, and sysadmin work are all
   relevant, too.


Posted by Mark Sienkiewicz on 2010-01-07 at 14:58. 

::

   From your description, it looks like the real problem is not the
   students -- it is incompetent management.    Why didn't the manager
   coordinate assignments, so that people do not waste their time writing
   conflicting patches?  That is the job of the manager.    How did the
   manager fail to notice that a worker could not compile the software
   for * 2 months * ?  How did the manager fail to offer any help?  That
   is the job of the manager.    If it is anything like most open source
   projects that I have contact with, it is because there IS NO manager.
   Many open source projects expect you will download their code, reverse
   engineer it (because there is no documentation), figure out what you
   need to know, and then find a way to aggressively contribute.  People
   who thrive in that environment will contribute; those that don't will
   quietly go away.    From the goals page on UCOSP's web page, I would
   expect the project to give extensive and explicit instruction in how
   to work in the open source environment.  From your description,
   though, it sounds like the project really let the students down.  It
   threw them into a situation that they were totally unprepared for,
   gave them no guidance, and then was disappointed when they were not
   successful.    Am I being too harsh?  Maybe, because I only know what
   you wrote in this blog post.  But the fact of the matter is that your
   idea of "Aggressive Competence" is just a tiny hint of what those
   students need to know.    Aggressive Competence is a useful technique.
   Even in the business world, where it costs real money to waste your
   programmer's time, you can still find bad management.  AC shares a lot
   with CYA (Cover Your Ass), where you document that you did the best
   that you could in the circumstances.    The part I find depressing is
   this:  It would be even better if you could tell the students how to
   succeed, rather than just documenting their reasons for failure.  I
   don't know what to tell them, though, because I have never found a
   recipe for a project to succeed in the face of bad management.    I
   think your idea of asking for regular progress reports is a good one.
   You will be acting in place of the manager; when you see the report,
   you will be in a position to take corrective action.  When you don't
   see the report, you will be in a position to ask "Hey, where is your
   report?"  (They're still learning; they need to be reminded.)    And
   you'll be in a position to suggest what the student should have done
   -- not as a criticism, but as a way to show them what works and what
   doesn't.  Wouldn't hurt to tell them about the differences between
   free-software and commercial development when the opportunity arises.
   When I got my degree, I knew all kinds of things about computers, but
   nearly nothing about how to apply that knowledge in a group.  I
   graduated, got a job, and then started learning to be a professional
   programmer.  It would be great if you could give the kids coming along
   now a head start on that.    Mark S.    p.s.  I assume you'll also be
   sharing this blog post and the comments with UCOSP?


Posted by pengar roulette on 2010-01-08 at 16:44. 

::

   Hey, ok, I get it, I guess - but does this really work?

