Thoughts on bioinformatics training suites
##########################################

:author: C\. Titus Brown
:tags: teaching,cloud computing
:date: 2013-12-3
:slug: bioinformatics-training-suites
:category: teaching

I've started to think more broadly about bioinformatics training, and
after some conversations with Vicky Schneider-Gricar at TGAC, Terri
Atwood at GOBLET, and others, I thought I'd write down some thoughts
on bioinformatics classrooms. In particular, what kind of compute
infrastructure is needed?

Before I get started, my assumptions and interests are as follows:

1. Many students will be fairly low-tech.  (Practically speaking, it's
   a fair assumption that even some of those who claim to be awesome
   superhackers will be missing some essential skill, so setting the
   base technical expectations fairly low is the safe way to go.)

2. The audience will generally be mostly bio-, not comp-.  (That's
   just who I teach.)

3. Technology is the devil.  Anything that requires the teacher to
   jump through hoops while teaching, remember to press buttons, or
   otherwise debug and adjust while standing in front of 15 or more
   people while trying desperately to evince high IQ, is FAIL.
   (If you haven't taught in a hi tech environment, you don't have the
   right to tell anyone how easy it is to just remember to fribable
   the bibpop every 5 minutes.)

So, what are the options?

Option 1: Participants bring their own computers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

One approach for training is that participants simply bring their own
computers to the classroom.  Students install the necessary software
and follow along with the workshops materials.  (This is how Software
Carpentry workshops are designed, so I've taught ~5-6 workshops this
way.)

The upsides are that students can immediately use whatever they learn
in the course, and there's little or no investment needed to set up
or maintain the computers in this workshop environment.

The downsides, however, are many:

* Necessary software needs to be installed on many different laptops.
  This can be difficult, depending on what needs to be installed and
  what OS the laptop is running.

  (Many of my worst bootcamp teaching experiences come from this.)

* Students must usually have reasonably up-to-date laptops, OR be able to
  run virtual machines.

  (Software Carpentry has had reasonably good luck with VirtualBox, but
  it's still a foreign environment for most; it seems like a poor
  compromise.)

* Depending on the tasks being demonstrated in the workshop, student
  computers may need to have more memory, disk space, or compute than
  most biologists will have.

  (For the `NGS course
  <http://bioinformatics.msu.edu/ngs-summer-course-2014>`__ we run de
  novo assembly software, which may require 8-16 GB of RAM.  Most
  laptops don't have that much RAM.)

* Some of the instructors or TAs need to be able to work on multiple platforms,
  so that they can fix install problems.

  (A typical problem in Software Carpentry is that many of the instructors
  have Macs or Linux machines, and aren't necessarily very good at
  debugging Windows installs.)

* Most cutting edge bioinformatics software runs primarily or best on Linux,
  and may not run on Mac OS or (especially) Windows.

  (This leads to two concerns: first, you might have to choose demo
  software that is particularly portable, rather than the software you
  would prefer to teach; second, you're handicapping students in the long
  term by not teaching them that, for better or for worse, Linux is
  actually where most bioinformatics is done.)

* Workshop materials must be generic enough to work on multiple platforms,
  with different path layouts, OS versions, etc.

  (Writing workshop materials is an immense amount of work.  Having to
  make them flexible in this way, and testing them and keeping them
  working on multiple platforms, is even more work.)

Option 2: Pre-installed machines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another approach for training is to use pre-installed machines (and/or
virtual machines running on existing hardware).  There's a classroom
with a bunch of hardware; the instructor
specifies software to be installed; someone (IT support, or the
instructor) installs it; students come to the classroom and use
machines that have been pre-loaded with the software needed for the
course.

On the surface, this seems like a great idea.  The machine can be configured
as needed, the software is guaranteed to work, the environments are uniform,
and life is good.   I've run several workshops this way and it can work
OK.

But, again, there are actually quite a few problems.

* You'll need some form of dedicated IT support to configure, maintain,
  and support the machines.

  (This can range from merely an additional task on top of a standard
  computing environment, as with MSU's Computer Science classrooms,
  where we have our regular sysadmins maintain a standard set of
  computers across many different classrooms; to a periodically scheduled
  support request whenever a workshop is run.  No matter what this can
  be a significant extra burden.)

* The machines and environments are unfamiliar to the students.

  (Whatever you run will be unfamiliar to 20% or more of the students,
  and even on the fairly standard Mac OS X environment, there are
  so many ways to customize it that native users will inevitably struggle
  with the differences.)

* The students generally won't be able to take what they've learned back
  "home" with them.

  (Even when students are at the same institution as the workshop, they
  often won't have access to the training suite or environment afterwards.
  This is especially true if the environment was custom-installed for the
  instructor.)

* Most places won't want to provide substantial compute capacity for the
  instructional lab.  This either limits what can be taught, OR means
  that students will also have to gain access to a local compute cluster,
  which complicates things further.

  (Most compute clusters are not thrilled at the idea of setting up specialized
  access for workshop attendees, either, in my experience.)

* The instructor needs to come up with specialized install
  instructions for the software they need installed on whatever
  environment the workshop will use.

  (This can be a significant additional burden on the
  instructor. Moreover, since the IT support will generally not be
  expert in whatever the instructor needs installed, the instructor
  will also need to verify the installs.)

Option 3: Cloud computing
~~~~~~~~~~~~~~~~~~~~~~~~~

A third option is to use remote-hosted virtual machines (aka cloud
computing).  The idea here is that the instructor specifies some
cloud service (Amazon, Rackspace, iPlant) to which all students
can have access; s/he provides a customized virtual machine with
some or all of the necessary software installed; and students use
the virtual machines remotely via either their laptop or provided
workstations.

It will come as no surprise to readers of my blog that this is my
favorite option.  It has much to recommend it: participants can use
their own computers, their own Web browser, and whatever SSH program
they like (Windows is the only OS that doesn't come with SSH
natively).  Graphic interaction can be supported either via X Windows
(ugh) or IPython Notebook or knitr.  Students can bring home their
expertise, assuming the cloud platform is still available to them at
home; alternatively, if their home institution provides hosted VMs,
they can use that.  Compute can be scaled up, or down, as needed for
whatever is being taught -- Amazon now rents machines with over 200 GB
of RAM, for example.

I've now taught over a dozen workshops this way, with a high degree
of success (at least in terms of the technical side.)

Problems, nonetheless, abound:

* Some institutions, labs, and funding agencies don't want to use remote
  computers for legal or other reasons (think HIPAA).

  (I haven't run into this myself; but, following my life goal of
  minimizing face time with lawyers, working out the legalities an be
  problematic.  Do note that the NSA uses Amazon Web Services for some
  things, so it's a little hard to believe that something couldn't be
  worked out for medical or other sensitive data.)

* Sharing files between local and remote is a perennial problem

  (I usually use Dropbox, which provides a command-line installable
  client.)

* Few people are prepared to edit files remotely.

  (Well, frankly, few people are prepared to edit text files at all.
  I use either IPython Notebook or pico remotely, OR encourage people
  to edit things in Dropbox or on github.)

* You need reliable network access and decent servers for the material
  and the data you're using.

  (In practice this is a must for most classrooms these days, but it
  can still be an problem when 30 people are clicking on the same link
  to download the same 50 MB file.)

* Cloud computing frequently costs money.

  (Amazon and Rackspace both charge money; iPlant could be free, but is
  still only dipping its toes into this area.  Grants can usually be
  obtained to help with the costs during the workshop, but what to students
  do when they get home?  Our local HPC has taken some of our cloud
  instructions and used that to install the software locally, which is a
  pretty neat idea and something we're pursuing more generally.)

* The tech competencies needed to set up and work with cloud machines
  is a bit more specialized than local sysadminning.

  (Some reasonably significant expertise, or at least time investment,
  is needed to get familiar with setting everything up.  It's, uhh,
  fairly easy when you've spent several years doing it ... ;))

My perfect bioinformatics training suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Of the three, then, I really prefer the cloud computing option.

My perfect bioinformatics training suite looks something like this:

* Lots of tables for group work, facing a common screen. Monitors and keyboards
  are available at the tables so that students can have multiple screens
  if they want.

* People mostly bring their own laptops, but there are a few available for
  when the inevitable tech problem happens (no power cord; machine crashes;
  corporate laptops too locked down to install software; etc.)

  An alternative would be to provide nice but cheap workstations with a
  Web browser and a shell, in serried ranks; but I bet most people would
  prefer to use their laptops if possible.

* Instructors maintain material for a fairly generic cloud environment
  (Ubuntu, Debian, Redhat, whatever) and configure virtual machines
  as needed for each course.  Some local IT support is on call for helping
  instructors with technical issues, but the expectation is that most of
  the installation will be done by the instructor or the students, and only
  particularly weird tech problems would need support.

Some additional fillips and thoughts:

* Classrooms could provide teleconferencing support for remote viewing,
  multiple classes, etc.  Screen sharing is still a bit technically
  tricky, so it can be hard to debug things remotely; local tech support
  would be needed for remotely taught courses.

  (We are currently exploring the use of Google Glasses as an alternative
  to screen sharing.)

* iPlant and other free academic clouds are starting to offer general
  cloud computing services that may be utilized in and out of the
  classroom.

  (Key word: "starting." Don't be the first adopter.)

* If enough people bought into the idea, we could establish shared
  training and support resources around a common VM model.  Then
  instructors could use whatever cloud they liked, but be working off
  of a common OS model and base software install.

  (Hmm, what a great idea.)

Conclusions
~~~~~~~~~~~

There are no panaceas.

I like the cloud.  It's served me well.

What did I miss?

--titus
