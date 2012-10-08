Teaching with ipython notebooks -- a progress report
####################################################

:author: C\. Titus Brown
:tags: python,ipynb,ngs
:date: 2012-10-07
:slug: teaching-with-ipynb-2
:category: science

The `IPython Notebook
<http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html>`__
(or 'ipynb' for short) is one of the most exciting technologies for
teaching and research that I've seen in recent years.  It is a
completely open source, well architected, and fairly stable system
for scientific computing and data exploration.

I've now been `using it for teaching <teaching-with-ipynb.html>`__ for
about 5 months; I first tried it out for our summer course on next-gen
sequence analysis, and then used it briefly in a Software Carpentry
workshop.  I've been an unabashed advocate of it ever since Wes
McKinney demoed it for me on a train ride from Seattle to Portland,
and we've started to use it in our research, both `for paper writing
<http://ivory.idyll.org/blog/replication-i.html>`__ and, more
regularly, for interactive data exploration.

Most recently, I've been using it for the second reboot of my intro
grad course, `Computational Science for Evolutionary Biologists
<http://ged.msu.edu/angus/beacon-2012/>`__, which is an introduction
to programming, UNIX command line usage, data analysis (de novo
sequence assembly), and evolutionary modeling (with Avida).  We've put
the students through beginning Python using IPython Notebook running
on Amazon EC2; the screencasts and in-class coding demos run on
notebooks, the homework assignments are given out in notebooks, and
students are handing in their homeworks on github gists.

What's my verdict after all of this experience?

**The bottom line is that the IPython Notebook is (still) the best
thing I've ever used for teaching.**

Recently, several of the Software Carpentry (SWC) folk, including Matt
Davis and Ethan White, `wrote a post
<http://software-carpentry.org/2012/10/transitioning-to-the-ipython-notebook/>`__
talking about how we're transitioning some or all of the SWC materials
over to ipynb.  I thought I'd expand on that post a bit and give some
of my own opinions and experiences, below.

What's the bad news?
--------------------

There are still a few places where the ipython notebook is either not ready
or simply not a good solution.

**UNIX state and ipynb state can differ**: Over the summer I found that
people new to UNIX and programming got very easily confused by the
fact that ipynbs were distinct from the underlying state of the machine.
Experienced computer folk would automatically understand that if
three notebooks were running on a single machine, then file changes in
one would be visible to other notebooks.  The notebook interface,
however, masks this underlying change.  I think this is unavoidable.

**Underlying ipynb state isn't linear in the notebook**: A related
problem is that ipynb state doesn't progress "down" the notebook,
because you can always jump around in the cells.  I think this is
unavoidable, too.

**Installation problems**: Unless you buy into the `Enthought Python
Distribution <http://www.enthought.com/products/epd.php>`__, IPython
Notebook and its "useful" dependencies, which include matplotlib,
are basically impossible to install.  Even when you *do* use the EPD,
about a quarter of the installations don't work properly right off the
bat, and I have generally not been able to debug things in the time
available to me.  This is the main reason I'm using EC2, and why I'm
going to encourage people in my class to switch to VMs in the future;
installation is easier that way.

**Long-running jobs**: IPython Notebook doesn't effectively run in a
headless mode, and excepts you to be more or less tethered to the same
Internet connection.  This makes it hard to execute long-running jobs
in ipynb, because you can't close up your laptop and come back later
very easily.  There are exceptions to this but not very comfortable
ones.  As a general rule, I do all of my long-running compute at
the command line.  (Note, Fernando says they have plans to improve upon
this aspect of the notebook.)

**Writing serious code**: I don't think the ipynb is going to replace
my serious editor (emacs) for writing modules and bigger programs
(more about this later).  It's meant for interactive data exploration.

**It gets in the way if you already kinda know UNIX**: One of the most
common complaints I got at the summer course was that people who
already knew some UNIX didn't like IPython Notebook for anything but
plotting.  They *already* knew how to drive the operating system and
didn't need a journal-like thingy to help them.

I'm pretty ambivalent about counting this last one as a negative -- I
suspect that at these students become more familiar with UNIX they
will be able to more easily navigate between ipynb and UNIX, but at an
early-intermediate stage of knowledge it gets in the way.  More
generally, I think that we *should* be teaching scientists to use this
kind of journal-like thinking when they do computation.  But that
doesn't necessarily make it easer on them when they're learning it!

Now, what's the good news?
--------------------------

**Ease of use**: I think the best news is that the IPython Notebook is
easy to use and easy to understand at a basic level.  No more remote
command lines, remote editors, and file transfer -- you can learn
Python to a basic level without all that stuff.  My experience has
been that, in biology, throwing all of that at people with no prior
computing experience is just too much.  I've been positively impressed
with how quickly my students have been picking up the programming side
of things, and I honestly expect the command line stuff to be much
more straightforward.  (We'll see how the next few weeks go!)

**Very easy for demos**: I've been using it in screencasts and
in-class demos for my graduate course, and some colleagues here at MSU
have been using it for in-class demos for their intro programming course.
Thumbs up.  We can pass the code around, or post static views of notebooks,
or whatever.  Overall, the ability to give the students exactly the code
I worked up in class is golden.

**Good data exploration**: I'm increasingly starting to use it to whip
together graphs and figures for talks; we've already used it for
publications, of course (`here
<http://ivory.idyll.org/blog/replication-i.html>`__), but it's a great
way to interactively explore data sets.

**nbviewer is awesome**: One of my gripes in the original `teaching
post <teaching-with-ipynb.html>`__ was that it was hard to post static
notebooks.  No longer!  The `nbviewer.ipython.org
<http://nbviewer.ipython.org>`__ site lets you transform raw .ipynb
files (from github gists or any URL at all) into nicely rendered HTML
notebooks.

**IPython Notebook is not a sandbox**: In my experience, you can go
quite far in data exploration with cell-level functions and scripting.
Until you become reasonably expert at those, you probably don't need
to write much in the way of your own modules.  Moreover, even once
you do start writing modules, ipynb lets you work with those via
the standard Python systems.

More broadly, IPython Notebook is a fantastic user interface on top of
the increasingly broad and deep Python ecosystem for scientific
computing and data analysis.  It is not, in any way, a sandbox that
limits you or prevents you from making full use of what other people
are doing.  And that, from the perspective of teaching the actual
practice of scientific computing and data analysis to students, is
what I find most important.

How am I actually using it?
---------------------------

**In my intro computational science course**: In the first few weeks,
students learn how to `start up an EC2 instance (YouTube)
<http://www.youtube.com/watch?v=JMedTCa5lec&feature=youtu.be>`__,
`connect to IPython Notebook (YouTube)
<http://www.youtube.com/watch?v=pDyaUUmvWvk&feature=youtu.be>`__, `do
basic Python commands
<http://ged.msu.edu/angus/beacon-2012/week1.html>`__, `upload their
homework to github gists as IPython Notebooks (YouTube)
<http://www.youtube.com/watch?v=YY0Bff5PoKI>`__, and do many useful
things like `plot (YouTube) <http://youtu.be/YSK3CboAOvU>`__.  I
post the homework sets as ipynbs, too -- see, for example, `the Monty
Hall problem
<http://nbviewer.ipython.org/urls/raw.github.com/beacon-center/intro-computational-science/master/hw-week4-monty-hall.ipynb>`__.

**For the summer course on next-gen sequence analysis**: I post a
bunch of notebooks through `github
<https://github.com/ngs-docs/ngs-notebooks>`__ that show students how
to `update their notebook repositories
<http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/renderedr/ngs-00-update-notebooks.ipynb>`__,
`install software
<http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/rendered/ngs-02-install-screed.ipynb>`__,
`run BLAST
<http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/rendered/ngs-10-blast.ipynb>`__,
`plot data
<http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/rendered/ngs-11-python-and-graphing.ipynb>`__,
`plot k-mer distributions
<http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/rendered/ngs-44-kmer-distributions.ipynb>`__,
`access sequence collections programmatically
<http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/rendered/ngs-62-screed-database-as-dict.ipynb>`__,
and even `play with digital normalization
<http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/rendered/ngs-5x-digital-normalization.ipynb>`__.  Next year I plan to put in more
info on what's going on in the notebooks -- this year, I talked through
them interactively in front of the class.

It's important to note that teaching all this stuff is still the primary
challenge, and the IPython Notebook is merely one tool that we can use.
Still, it's a pretty awesome tool, given the craptitude we have in terms
of legacy development environments, and the reviews have been pretty positive
so far from the students.

This next year at PyCon we've proposed a panel to talk about
the ipynb for teaching, and I think I'll be pimping it at a pre-PyCon
teaching workshop, too.

What does the future hold?
--------------------------

When I talk to the IPython team, I find them to be incredibly
ambitious.  They basically view the IPython Notebook as a general
computing platform for seamlessly connecting a Python interpreter to
dynamic HTML/JavaScript, and they are hell-bent on the awesome.  I
confidently expect to see generic JavaScript widgets, spread-sheet
like computing, collaboration within an ipynb, slide shows, and
recording/playback to make an appearance within the notebook over the
next year or two.
