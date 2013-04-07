Arizona, Software Carpentry, and Software Installation
######################################################

:author: C\. Titus Brown
:tags: python,teaching
:date: 2013-04-07
:slug: 2013-swc-arizona
:category: science

Software installation is a real problem.

I'm writing this as I return from my fourth Software Carpentry
workshop, or -- if you count the one I ran at LLNL almost a decade ago
-- my fifth one.  This workshop was taught with Karen Cranston and
Rich Enbody, both of them very experienced teachers.  The workshop was
at University of Arizona, co-sponsored by iPlant, and organized by
Julie Messier.  Darren Boss, Katie Cunningham, and Chas Leichner
helped out as TAs, along with one or two others whose names I missed
(sorry!)

I think it was a success, in that we covered `a fair amount of useful
material <http://2013-swc-az.readthedocs.org>`__ ranging from basic
Python programming to automating data analysis.  We had about 90%
attendance on the second day (which is at least a sign that we duped
them into thinking that it would be valuable based on the first day's
content ;).

The only total disaster was software installation.  (Oh, installation,
my old enemy!)  Unlike the UW workshop, I spent more time working with
students to debug problems, and so I can assure you with some
confidence that installing Anaconda on Windows is just a complete
nightmare.  Our problems ranged from IPython Notebook not starting up,
to it not running any Python code, to it not emitting any output when
Python code was run.  Some people could *only* run it from Git Bash,
others *couldn't* run it from Git Bash, but cmd worked fine.  Which
was which seemed to depend on Windows version, 64- vs 32-bit, and the
alignment of the heavens at that very moment.

Problems also occurred with software installation via pip (do I need
to run anaconda pip, or what? Where is my Python install? Do I have
admin privileges? etc.) and running Python scripts at the command
line.

So it was a mess.

Naturally, when the instructors got together at the end of the day
at 1702, the over-beer conversation turned to INSTALLATION.  What
were we going to do about it for the next workshops??

This is more than a merely academic question.  I now have some money
to fling at these kinds of problems.  So how best to spend it?  Here
are our thoughts, equally contributed from Karen, Rich, Darren, Katie,
Chas, and myself.

Karen made the point that the first two hours are critical -- that's
when people are awake, energetic, and optimistic.  We mostly spend
the first two hours debugging install, which means that (a) people
who got it working are bored, and (b) people who don't have it working
are scrambling with incomprehensible technical problems.  So we need
to address it in some way that doesn't make the first two hours SUCK.

Options!
~~~~~~~~

FIRST, we could send out a specialized "installation TA" to meet with
students to install and document install problems, and also to
coordinate with local Python groups to come help out with
troubleshooting.  Eventually we'd saturate the set of common problems
and we could provide either automated workarounds, or specific install
protocols to diagnose and fix the common problems.

The main problem I see with this is that it's manpower intensive, and
we need to find a fairly well-trained person to fly around a lot.

SECOND, we could work with Continuum and Enthought to make their
installs work better.  This could include building a little Web
or binary installer (for Anaconda), and maybe some nice launchers.
Remember, most of the time we're dealing with people who don't
have any experience with the command line, so anything that involves
more than typing one or two completely stereotyped command lines
is FAIL.

I would be mildly unhappy to spend money making their software better,
but since we're already using it... I guess my main fear is
that at some point Continuum or Enthought would cease to offer their
free/academic version and our work would disappear.

THIRD, we could provide expected install results in some form, so
that people could know when they had installed things properly
in advance.  For example, "you should be able to run ipython
notebook, type 'print "hello, world"', and hit shift-enter, and
get "hello, world"."  But in video form or something.

We should definitely do this.

FOURTH, we could just tell Windows people to use VirtualBox and
provide a VM.  It flies in the face of trying to get the students to
be able to use this stuff on their own computer, but perhaps we can
motivate them with the workshop and they can go get help installing
this stuff on their own, later; or, during the workshop, but with less
urgency.

I'm going to do this for my future workshops, I think.  Should it be
Software Carpentry standard policy?

FIFTH, we could compute entirely in the cloud, as I do with a number
of my other courses.  For my other courses, we tend to be analyzing
large amounts of data, so running it on the local laptop is generally
impossible.  It has worked out great.  On the flip side, it doesn't
help students to actually use this stuff on their own (see above)...

This costs money but I bet we could get one or two of the big cloud
providers to spring for it.  Or we could work with the iPlant folk.

SIXTH, we could compute in the cloud for the FIRST day, and then have
an install fest at the end of the first day, or the beginning or end
of the second.

This has the advantage of motivating people by showing them how good
the world *could* be, if only they spent the time... plus, the installs
could still fail without huge harm to the workshop.

SEVENTH, we could use some general installation system that actually
works, like on Linux.  My concern with this is that the more "meta" we
go (like, "install this piece of software so that we can more easily
install *any* piece of software! it's cool, trust me!") the more
quickly we lose students and the more things can actually go wrong.

I don't see anything like this in the cards.  Easy installation is
simply not a forte of the open source crowd.

EIGHTH, we could fix Windows.  Hahahaha, no, not really.

What am I missing?

thanks,

--titus
