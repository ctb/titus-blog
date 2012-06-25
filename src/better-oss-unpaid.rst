Better Open Source Code with Just Volunteers?
#############################################

:author: C\. Titus Brown
:tags: python,oss,olpc
:date: 2009-02-14
:slug: better-oss-unpaid
:category: python


Over at `OLPC News <http://www.olpcnews.com/>`__, Wayan Vota `asks
<http://www.olpcnews.com/people/negroponte/better_open_source_code_just_w.html>`__:
"Do you get better FOSS code ...  if the developers are paid or
unpaid?"

----

Interesting question, especially as considered in light of the OLPC
code base.

As of about a year ago, virtually everybody I talked to was shocked
and stunned at the poor quality of the OLPC code base.  My personal
encounters with the code left me frustrated at the poor Python style,
angry at the simultaneously over- and under-engineered build process,
livid at the poor quality control, and blue about the long-term
prospects of the OLPC software.  I was not alone, although most people
were polite enough not to `be a jerk about it like me
<http://ivory.idyll.org/blog/mar-08/software-quality-death-spiral.html>`__.
(Looking back, perhaps if more people had been jerks earlier, things
could have improved.  Or not.)

At the time I felt that the OLPC code, which might have been a triumph
for the OLPC project, a gem of Python code, and a win for the open
source community, had turned into a cesspool of code and a potentially
infinite time sink for people working on it.

I haven't revisited the project since then, and I know that community
enthusiasm has waned for the OLPC.  I don't think the poor quality of
the code was a huge factor in this decline, but it certainly decreased
the interest that serious hackers had in getting involved in the
project -- at least, it did for everyone I talked with.

----

So, let's get back to the original question: in an OSS project, is it
better to let the community write your code for you, or should you
have a core development team?

Let me rephrase that another way, actually: if your business practices
drive you to write crappy, hurried code, with no attention to any form
of reasonable software development processes (agile or otherwise), no
automated testing, and very little QA of any kind, are you better off
turning software development over to the community?

The answer becomes less difficult then: **yes**, if it's an option,
you should jettison your software development efforts.  If you can't
do things competently, you should remove yourself from the
responsibility of doing it.  Abdicating responsibility is the
responsible thing to do in these circumstances, *if* you can make it
work.

But... what went wrong, anyway?  I don't know.  I'd guess that the
OLPC software development team was overmatched from the beginning:
responsibility of developing new software for a novel mix of hardware,
together with a novel GUI interface, in an environment of much
enthusiasm and relatively little funding, is hard. Add to this the
enthusiastic but not very disciplined-sounding roadmap, as well as the
unrealistic deadlines set due to PR and political considerations, and
it's a recipe for disaster.  When you also throw in an overwhelmed
OLPC management team, I don't think you can expect anything **but**
disaster.

So, looking back, I think the OLPC was probably headed into a mess
from day 1, and while the fubar'ed software development process didn't
help, it was at least partly driven by circumstances outside the
control of the software developers.  The software developers were
hamstrung from the get go.  And in that environment, turning the
majority of your software development over to someone else -- someone
**not under your direct control** -- may in fact be the best option.

I think that's actually a much more interesting question: at what
point should an organization realize that they are so incompetent at
managing and doing "in-house" software development that they should
try to outsource it?  What metrics should they look at, and how should
the decision be made?

--titus

p.s. `The general question of whether to go for paid or unpaid
development is silly, of
course <http://github.com/raganwald/homoiconic/blob/master/2009-02-12/a_question.md#readme>`__.
The answer is, "it depends."  Duh.  The interesting question is what questions
you need to ask to figure it out!

p.p.s. Disclaimer: the individual OLPC people I know, up to and
including lower management, are smart, enthusiastic, and good people.
I place the majority of the blame squarely at the top.


----

**Legacy Comments**


Posted by Steve Holden on 2009-02-15 at 05:52. 

::

   """Disclaimer: the individual OLPC people I know, up to and including
   lower management, are smart, enthusiastic, and good people. I place
   the majority of the blame squarely at the top."""    Hear, hear. This
   disastrous proof that egotistical academics do not in general make
   good managers or production engineers has cost the open source
   community a lot in terms of credibility. Then, after all that, a
   complete about-face will have the damned things running Windows XP.
   Groan.    The OLPC project appears to have suffered from the naive
   belief that goodwill and intellectual capacity alone are required to
   make a project succeed. It was indeed a disastrous failure of senior
   management, and wasted a lot of capable programmers' time. Great idea,
   terrific cause, lousy execution.


Posted by Wayan @ OLPC News on 2009-02-15 at 06:25. 

::

   Titus,    This is a great answer to my question.  Might you mention it
   in the comments on that post?  Or would you be up for a Guest Post
   responding to my question on OLPC News?


Posted by Titus Brown on 2009-02-15 at 16:47. 

::

   Steve, please don't tar us egotistical academics with such a broad
   brush ;)    Wayan, posted.


Posted by Rene Dudfield on 2009-02-15 at 21:19. 

::

   hi,    a few thoughts on this subject...    "Do you get better FOSS
   code ... if the developers are paid or unpaid?"    Code quality is
   very subjective.    If you need to get code out there at the start of
   a project -- to meet a deadline -- then the code quality needs to be
   worse.    However, code which is not working automatically is worse
   when you have deadlines.  Deadlines are why crap code is often better
   than quality code.      People not working to deadlines, and not
   following a budget can make better quality code in some ways.  Since
   it doesn't matter if they spend four months perfecting two functions.
   However being paid to work on a FOSS project allows you to tackle
   greater sized projects.  Some times you need to sit down for 3 months
   full time to do some projects(or even 10 years!!!).  It can be
   impossible to do some types of work at 1 hour a week spread between 10
   people.    Without considering the goals of a project - you can not
   judge the output.  It's a very common mistake people make when
   critiquing design and art.  This is why I think your analysis of OLPC
   code quality is wrong.  Since you judge it based on a different
   criteria.  Their goal was not to make high quality code -- they had
   other goals... like shipping a laptop(amongst many other changing
   goals).        cheers,


Posted by Martin on 2009-02-22 at 15:18. 

::

   What code in particular did you think was bad.  I'm not an OLPC
   developer, but I have hacked on plenty of the code.  I agree there're
   non-pythonic code blocks around, but that's not the same as low-
   quality.  I'm interested in what you found.


Posted by Titus Brown on 2009-02-24 at 20:41. 

::

   The build system was severely hacked and failed regularly.    The base
   sugar code was spaghetti-ish.    None of the code was commented.

