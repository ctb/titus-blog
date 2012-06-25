LLNL Course: Done!
##################

:author: C\. Titus Brown
:tags: python,teaching
:date: 2007-06-24
:slug: llnl-course-done
:category: teaching


On Tuesday (June 12), Wednesday, and Thursday I taught the course
"Intermediate and Advanced Software Carpentry in Python" at Lawrence
Livermore National Labs.  This was intended to be an extension of some
of the ideas from the `Software Carpentry course
<http://www.swc.scipy.org/>`__.

The pre-course course `advert
<http://ivory.idyll.org/blog/apr-07/class-blurb.html>`__, the handouts
distributed at the course (`day 1
<http://teckla.idyll.org/~t/transfer/public/day1.pdf>`__, `day 2
<http://teckla.idyll.org/~t/transfer/public/day2.pdf>`__, and `day 3
<http://teckla.idyll.org/~t/transfer/public/day3.pdf>`__), the
`corrected and revised handouts
<http://ivory.idyll.org/articles/advanced-swc/>`__, and `associated
source code
<http://ivory.idyll.org/articles/advanced-swc/code.tar.gz>`__ are all
available for your perusal and use.

As you can see from the outline and handouts, I took a rather
fast-paced and shallow approach to teaching this class.  This was by
direction and intent; because this was an *intermediate* class, I
assumed basic familiarity with most things Python, and gave a tour of
various features rather than an in-depth tutorial.  It's by no means a
complete exploration of the topics, and it's not intended to be!  In
particular, I felt free to offer up really stupid examples rather than
justifying each Python feature, because I assumed that people would
fit features to their needs.  (This is why there are a lot of stupid
examples!)

A few thoughts:

There are a lot of people that use Python at LLNL!  Alas, very few
of them are biologists, who mostly use Perl.

After a slightly rough first day, I switched to introducing and
demoing features rather than requesting some hands-on work.
Apparently it is difficult for most people to switch from listening
to coding on short notice!  My (badly planned) exercises were kinda
bogging the class down, and someone pointed out that these people
were going to take what I taught and use it immediately anyway, and
that I should just point them in the right direction rather than
making them do exercises.

As I saw with my `PyCon'07 talk
<http://ivory.idyll.org/blog/mar-07/pycon-talk-source>`__, demoing
coding in front of people conveys more of a sense of the process
*and* content than having prepackaged demos.

Teaching smart, motivated people is a joy.  I don't know how this will
compare to teaching undergrads at MSU, but my guess is that motivation
will generally be lower!

Talking all day, every day, for three days, is bloody exhausting.
Really, really, really, really exhausting.

I generated over 75 pages of text (no images, and not counting the
code that I wrote but did not insert into the text).  Doctests
rock.  So does ReStructured Text.  Combining them is synergistic.
  
Doctests in tutorials keep me honest.

subprocess rocks.  I would generalize and say that os.system is one
of the big failure points in people's use of Python, and subprocess
can solve the simple problems really easily.  Unfortunately the
current subprocess module documentation sucks.  I have been
inspired.

My discussion of multiprocessing was, I think, a hit.  It was easy
to make fun of Python's default "you don't need threading that
much!"  in front of a crowd of people that work on massively
parallel CPU intensive applications!  I explained how and why the
Python approach was actually pretty good, and went through actually
converting one of my library functions into a threadsafe &
threadaware Python function.

parallelpython is neat although I find that the example code chafes
my sense of aesthetics.

pyrex rocks.  ctypes rocks.  SWIG is a tad obsolete and buggy (at
least for Python) when you have SIP and Boost!

I was introduced briefly to `Babel
<http://www.llnl.gov/CASC/components/babel.html>`__, a
cross-language interoperability system buil at LLNL.

`pyMPI <http://pympi.sf.net/>`__ is also built at LLNL, and they use it
fairly extensively.

I didn't get to talk about a few things in my original outline,
either because I forgot, or couldn't fit it in.  The biggest lack
was the planned discussion of data presentation via the Web and
data storage via databases.  I think this technique is
underutilized in scientific circles.

I tried to push testing, testing, testing.  I don't know how
successful I was.

--titus


----

**Legacy Comments**


Posted by Greg on 2007-06-24 at 15:11. 

::

   Sounds interesting, here are a few follow up questions if you don't
   mind:    1. What is LLNL?  2. Why do doctests in tutorials keep you
   honest?  3. You wrote:  subprocess rocks. I would generalize and say
   that os.system is one of the big failure points in people's use of
   Python, and subprocess can solve the simple problems really easily.
   Unfortunately the current subprocess module documentation sucks. I
   have been inspired.    Would you mind expanding on that idea a bit?
   I'm still a heavy user of os.system :-(


Posted by Titus Brown on 2007-06-24 at 16:02. 

::

   Greg,    LLNL is "Lawrence Livermore National Labs".    doctests in
   tutorials make it easy to check that the code you're writing does what
   you think it does.  You're sure, the students are sure, and you can't
   just make stuff up completely!    subprocess completely replaces
   os.system and lets you do things like capture stdout/stderr and write
   via stdin, things that are tricky or downright impossible with
   os.system.  It also has sensible return codes on Windows.  subprocess
   is actually much more powerful than just that, but that's the pocket
   summary ;)    --titus


Posted by Matt Doar on 2007-06-26 at 13:06. 

::

   "subprocess rocks. I would generalize and say that os.system is one of
   the big failure points in people's use of Python, ... Unfortunately
   the current subprocess module documentation sucks. I have been
   inspired."    I could not agree more. subprocess means that I can
   finally replace bash scripts with python and is my biggest reason for
   moving to python 2.4. But yes, the documentation really needs lots
   more examples, ideally for Windows and Unix commands, and more
   explanation about running in a shell or not.


Posted by Alex on 2007-07-02 at 10:38. 

::

   "Unfortunately the current subprocess module documentation sucks. I
   have been inspired."    I look forward to the results of your
   inspiration.  One thing that would be good would by side-by-side "if
   you'd have done it this way before, do it like so with subprocess"
   examples.  (I found this page by googling on (python subprocess write
   examples), in the hope of figuring out the subprocess idiom I could
   use as a drop-in replacement for       gp = os.popen('gnuplot', 'w')
   No luck so far.)


Posted by Dave Rogers on 2007-07-03 at 14:16. 

::

   Which "MSU" are you teaching at?    Thanks, Dave


Posted by Titus Brown on 2007-07-03 at 14:27. 

::

   Michigan State U.


Posted by Dave Rogers on 2007-07-03 at 22:37. 

::

   Titus,    I'm good friends with Chuck Esterbrook and I met you back in
   2001 at the Python Conference in Long Beach, CA.  Yes, its okay if you
   don't remember me.    I happen to live right next to Michigan State.
   I'm a graduate of their Computer Science program as well.      If you
   aren't already familiar with the East Lansing area, I can give you
   some pointers.    Good luck,  Dave

