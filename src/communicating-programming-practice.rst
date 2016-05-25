Communicating programming practice with screencasts
###################################################

:author: C\. Titus Brown
:tags: python,teaching
:date: 2013-02-12
:slug: communicating-programming-practice
:category: python

One of the things that I have struggled with over the years is how to
teach people how to *actually* program -- by this I mean the
minute-to-minute process and techniques of generating code, more so
than syntax and data structures and algorithms.  This is generally not
taught explicitly in college: most undergraduate students pick it up
in the process of doing homeworks, by working with other people,
observing TAs, and evolving their own practice.  Most science graduate
students never take a formal course in programming or software
development, as far as I can tell, so they pick it up haphazardly from
their colleagues.  Open source hackers may get their practice from
sprints, but usually by the time you get to a sprint you are already
wedged fairly far into your own set of habits.

Despite this lack of explicit teaching, I think it's clear that
programming practice is really important.  I and the other Linux/UNIX
geeks I know all have a fairly small set of basic approaches --
command-line driven, mostly emacs or vi, with lots of automation at
the shell -- that we apply to all of our problems, and it is all
pretty optimized for the tools and tasks we have.  I would be hard
pressed to imagine a significantly more efficient and effective
set of practices (which just tells me that there is probably
something much better, but it's far away from my current practices :).

Now that I'm a professional educator, I'd like to teach this, because
what I see students doing is so darned inefficient by comparison. I
regularly watch students struggle with the mouse to switch between
windows, copy and paste by selecting or dragging, and otherwise
completely fail to make use of keyboard shortcuts.  I see a lot of
code being built from scratch by guess-work, without lots of Google-fu
or copy/pasting and editing.  Version control isn't integrated into
their minute-by-minute process.  Testing?  Hah.  We don't even *teach*
automated testing here at MSU. It's an understatement to say that
using all of these techniques together is a conceptual leap that many
students seem ill-prepared to make.

Last term I co-taught an `intro graduate course in computation for
evolutionary biologists
<http://ged.msu.edu/courses/2012-fall-cse-891/>`__ using IPython
Notebook running in the cloud, and I made extensive use of screencasts
as a way to show the students how I worked and how I thought.  It went
pretty well -- several students told me that they really appreciated
being able to see what I was doing and hear why I was doing it, and
being able to pause and rewind was very helpful when they ran into
trouble.

So this term, for my database-backed Web development course, I decided
to post videos of the homework solutions for `the second homework
<http://msu-web-dev.readthedocs.org/en/latest/hw2.html>`__, which is
part of a whole-term class project to build a distributed peer-to-peer
liquor cabinet and party planning Web site.  (Hey, you gotta teach 'em
somehow, right?)

I posted the example solutions as `a github branch
<https://github.com/ctb/cse491-drinkz/tree/hw2-solutions>`__ as well
as videos showing me solving each of the sub problems in real time,
with discussion:

  HW 2.1 -- http://www.youtube.com/watch?v=2img0wKdokA

  HW 2.2 -- http://www.youtube.com/watch?v=eQU4qImY9VM

  HW 2.3 -- http://www.youtube.com/watch?v=YqL18Ip2wws

  HW 2.4 -- http://www.youtube.com/watch?v=7iOITFHrqmA

  HW 2.5 -- http://www.youtube.com/watch?v=0Ea5yxRCKKw

  HW 2.6 -- http://www.youtube.com/watch?v=6k8pnl2SgVI

I think the videos are decent screencasts, and by breaking them down
this way I made it possible for students to look only at the section
they had questions about.  Each screencasts is 5-10 minutes
total, and now I can use them for other classes, too.

So far so good, and I doubt many students have spent much time looking
at them, but maybe some will.  We'll have to see if my contentment
in having produced them matches their actual utility in the class :).

But then something entertaining happened.  Greg Wilson is always
bugging us (where "us" means pretty much anyone whose e-mail inbox he
has access to) about developing hands-on examples that we can use in
`Software Carpentry <http://software-carpentry.org>`__, so I sent
these videos to the SWC 'tutors' mailing list with a note that I'd
love help writing better homeworks.  And within an hour or so, I got
back two nice polite e-mails from other members of the list, offering
better *solutions*.  One was about `HW 2.1
<http://ged.msu.edu/courses/2012-fall-cse-891/>`__ --

  It might be safer to .lstrip() the line before checking for comments
  (to allow indented comments). Also, not line[0].strip() doesn't test
  for lines with only white space. it tests for lines that have white
  space as the first character.  'not line.strip()[0]' would be all
  white space... That would also make 'not line' redundant.

I also got a more general offer from someone else to peer review my
homework solutions, and chastising me for using ::

  fp = open(filename)
  try:
    ... do stuff ...
  finally:
    fp.close()

instead of ::

  with open(filename) as fp:
     ... do stuff

heh.

I find this little episode very entertaining. I love the notion that
other people (at least one is another professor) had the spare time to
watch the videos and then critique what I'd done and then send me the
critique; I also like the point that the quest for perfect code is
ongoing.  I am particularly entertained by the fact that they are both
right, and that my explanation of my code was in some cases facile,
shallow, and somewhat wrong (although not significantly enough to make
me redo the videos -- the perfect is the enemy of the good enough!)

And, finally, although no feedback spoke directly to this, I am in
love with the notion that we can convey effective practice through
video.  I think this episode is a great indication that if we could
get students to record themselves working through problems, we could
learn how they are responding to our instruction and start to develop
a deeper understanding of the traps for the novice that lie within our
current programming processes.

--titus
