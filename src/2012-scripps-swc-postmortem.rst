Software Carpentry at Scripps - Nov 2012 - postmortem
#####################################################

:author: C\. Titus Brown
:tags: python,teaching
:date: 2012-09-24
:slug: 2012-scripps-swc-postmortem
:category: science

I am just returning from a trip to Southern California that included,
among other things, the teaching of a two day Software Carpentry
workshop at `The Scripps Research Institute
<http://www.scripps.edu>`__.  There were two instructors, myself and
Tracy Teal, a research scientist at MSU; and two external TAs,
Qingpeng Zhang (one of my graduate students) and Cait Pickens (an MSU
grad student studying computational learning).  Andrew Su, the hosting
faculty member, helped out quite a bit.

Justin Kitzes, a postdoc from Berkeley, was supposed to come but fell
ill at the last minute :(.

Note that Cait `has
<http://michigancomputes.wordpress.com/2012/11/18/software-carpentry-the-preparation/>`__
`posted
<http://michigancomputes.wordpress.com/2012/11/24/software-carpentry-day-1-part-1/>`__
two reports on it as well; I like how touchingly naive she is about my
preparation, where she thinks that I was only preparing things at the
last minute because Justin fell ill ;).

Venue
~~~~~

The venue was pretty good, although we crammed 40 people into a room
that was a bit small, and the screen was too small to be clearly
seen from some positions in the room. There was a kitchen next door
where the Scripps folk kept coffee and pastries all day, as well
as bagels for breakfast and sandwiches for lunch - win!

One thing we had that I would have liked at other venues was a plethora
of nearby conference rooms.  This let me go to another room when I was
preparing or modifying tutorials.  It was also a good place to meet with
the TAs to plan things.

One minor obstacle was that the "guest" network (which was all that
was available to us as visitors) didn't initially have ssh enabled!
This blocked us from ready access to some of our materials and demos.
Andrew quickly got that changed, which was fantastic (lightning
fast sysadmin response!); but then, later
on, it proved to be impossible for me to get to non-canonical Web
sites, which blocked me from easily setting up a multi-user Amazon
machine running multiple ipython notebooks.

**Recommendation**: In addition to a main room, ask to have a
nearby conference or breakout room where instructors can meet with
students and with each other.

**Recommendation**: Make sure that the local network is open to both ssh
and http/s for visitors; non-canonical ports (8000+?) would be a bonus.
Best of all would be to enable login accounts for the instructors on the
same network that the students are using.

Social hacking
~~~~~~~~~~~~~~

It's always difficult to manage workshops, both in terms of short-term
pacing and long-term retention.  Cait and Tracy tried some new
approaches out for this workshop: research paragraphs, minute cards,
pairing into groups, and a formal concept roundup at the end.

I think the biggest win for me was the minute card concept.  At the
end of every session (before each break) we asked everyone to take a
minute to write down one thing they had learned, and one thing they
were confused about.  They then turned these in to us (anonymously).
This ended up being an *excellent* barometer of the session, and both
let us pace lessons better and identify & address general points of
confusion.  Highly recommended.

At the beginning, we also asked everyone to email us research
paragraphs, identifying a specific problem that they wanted to solve
using what they learned in the workshop (this came from the discovery
that a 15-minute writing exercise `did cool things <http://blogs.discovermagazine.com/notrocketscience/2010/11/25/15-minute-writing-exercise-closes-the-gender-gap-in-university-level-physics/>`__). This was when
we realized that virtually every biologist in the room was hoping we
could help them out with sequence analysis :).  The only negative was
that for this (and other evaluation mechanisms) we forgot to ask for
explicit permission to share their paragraphs with the local
professor, and so will only be able to give summaries to Andrew.

We asked everyone to go through a formal concept roundup at the end.
Cait wrote down a bunch of concepts that we'd taught, and asked people
to build a map showing which concepts connected to each other.  (I
don't know how this turned out, as I was decompressing.)

On the second day, we also asked people to sit in pairs, next to
people they knew or saw regularly.  Greg Wilson (via Tracy) had said
that research showed that concepts were retained better when they had
a friendly person nearby to discuss stuff with, and to connect with
after the workshop.  I'm not sure how this went but I did see a lot
more useful on-topic chatter the second day.

**Recommendation**: Use minute cards!  Before every break, ask everyone
to write down one thing they learned and one thing they were confused about,
and hand them in.

**Recommendation**: Ask everyone for research paragraphs at the beginning
of the workshop.

**Recommendation**: Identify what student information and documents
you want to share with the workshop host *before* starting the
workshop, and get explicit permission to do so from the students.
(To share them without permission is unethical.)

Topics
~~~~~~

We covered: the shell; automating tasks; basic Python, including
graphing and parsing; basic Python data structures; installing and
using some Python packages, including a BLAST parser and a sequence
parser; some useful UNIX tools (grep and find); and, at the end, 
a whirlwind tour of testing, version control, and analysis pipelines.

The main problem we faced up front was that we were teaching
biologists, who generally do not encounter computation anywhere in
their coursework.  That had at least two direct consequences: we had
to start at a *very* basic level, and we had to motivate people to pay
attention to us, which in turn required that we speak their language.
Luckily (well, ok, partly by design ;) Tracy and I are both
biologists, and Qingpeng is in my lab, so we were familiar with the
lingo and domain-specific problems.

We knew, going in, that the level of the students was going to be a
problem -- we'd done a pre-workshop survey.  But we still went
into the workshop with material that was systematically too high
level for the students.  So we had to adapt on the fly.

I think we really need three "levels" of Software Carpentry material:
a beginner level, an intermediate level, and an advanced level.  I
think most of the current SWC stuff focuses on the intermediate level
of stuff that physicists and engineers need to know but never really
get taught -- testing, version control, and automation.  The beginner
level should focus on issues like correctness, beginning automation,
pipelines, and introduce testing and version control as concepts.  The
advanced level can focus on optimization, C/C++ integration, detailed
testing advice, etc. -- stuff that only people deep into Python really
get into -- if indeed we want to offer it at all.  (See my `Intermediate
and Advanced Software Carpentry material <http://intermediate-and-advanced-software-carpentry.readthedocs.org/>`__ for an example.)

A number of people came up to us after the workshop and said that we'd
provided a great intro to and overview of computational concepts, and
they were much clearer on where UNIX and programming could fit into
their science.  I think that's about as much as we can realistically
hope for from a beginner workshop -- but that's already way more than
we do in most biology training, and I think it's really worth it.

**Recommendation**: Make sure workshops are taught by domain experts,
and motivate students with close-to-real-world examples from their
domain.

**Recommendation**: Develop "libraries" of beginner, intermediate, and
advanced topics that we can reuse as we move forward with Software
Carpentry.

Teaching testing
~~~~~~~~~~~~~~~~

I used IPython Notebook to implement a simple set of unit tests and
regression tests -- you can `see the notebook here <https://raw.github.com/swcarpentry/2012-11-scripps/master/python/testing-with-nose.ipynb>`__.

The unit tests I developed by writing a function that calculated G/C
content for a DNA sequence, and then working through issues like Ns,
lower case letters, and null strings.  I think everyone got the point,
which was neat.

For the regression tests, I tried to motivate this by talking about
the software lifecycle, specifically in research, and discussed how
nice it was to be able to keep software *consistent* in terms of
results.  I then implemented a simple regression test that compared a
"saved" output for a script to the current output.  I don't know how
successful I was, but I gather the more advanced users in the audience
appreciated seeing some testing in action.

Teaching version control
~~~~~~~~~~~~~~~~~~~~~~~~

We ended up not having time to teach command line git, although we did
use it to distribute data (which worked really well, BTW).  In some cases where
git wasn't installed properly, we had to use the download button on the
github project to grab a zip file, but that worked fine once we figured
it out.

For people that haven't seen (distributed) version control before, the
github workflow (fork, edit, send pull request) seems to make sense.
At least, I felt very comfortable teaching it, and everyone completed
a full pull request set.

I'd love to see how this interfaces with a follow-on command line git
tutorial; next time!

**Recommendation**: Use git and github to distribute data for workshops.
You can use either the repository or the 'download zip' button.

**Something to try next time**: Teach the github workflow as an intro
to distributed version control.

Software installs
~~~~~~~~~~~~~~~~~

Software installation was, as usual, horrible.  We squared several
things away fairly quickly by settling on `Anaconda CE
<http://continuum.io/>`__ for Mac OS X and telling everyone else to
just use VirtualBox to run a virtual machine, but this left behind a
bunch of people with old Windows machines (Anaconda CE just didn't
work on Windows, at least not for me; and VirtualBox is a bit of a
resource hog).  There was also a fair bit of confusion about how to
use Anaconda properly, aided and abetted by the fact that none of the
tutors had any experience with it either.

BTW, even if we could have gotten Anaconda CE working on Windows, none
of our pipeline examples would have worked, because they included
shell commands.  Windows really is just different.

What's the solution here?

From my experience in running a number of workshops, I give you the following
set of points to consider.

1. Cloud computing always just works, 'cause it's their business model to
   make things "just work". 

2. Windows is horrible and strange for most of what we want to teach, which is
   standard computational science practice -- which in turn generally involves
   UNIX.

3. Software installs on Windows machines are always kind of weird anyway.

4. VirtualBox works pretty well in general, but seems to fail (due to
   compute resource requirements) on some small number of machines.

5. The less computationally experienced a person is, the more likely they
   are to have a weird/non-standard or resource-limited system that makes
   it impossible to install something we need.

So the question is, what do we want to be teaching people?  If we want
to teach people how to use their own laptops to do stuff, we're
basically doomed; every laptop is different and we spend all our time
debugging environments.

But.

If we want to give people in-depth exposure to ideas and good
computational practice, I think we're basically ok: some people will
be able to install all the stuff just fine, while others will have to
use a VM, and an unlucky few will have to resort to a cloud machine.
But everyone will be able to follow along.  If students can follow
along with the course materials and are properly motivated, they
should be able to go to their local computer support later on and get
the software installed -- i.e. after the workshop, when it's not a
melee situation.

We can definitely help future workshop tutors by providing up-to-date
installation instructions, annotated by instructors based on
experience, and also providing up-to-date VirtualBox and Amazon
images.  This would let instructors get on with the business of
teaching as quickly as possible. And, more generally, *other* 
(non-Software Carpentry) courses could make use of our images for
*their* classes - a total win.

So here are my recommendations:

**Recommendation**: Rely on Anaconda (for Mac OS X), virtual machines
(for Windows), and cloud machines (for situations where neither work).

**Recommendation**: Keep an up-to-date Virtual Machine ready for workshop
attendees to download.  (The one we used had an out-of-date IPython Notebook
install, for example.)

**Recommendation**: Develop a multi-user Amazon image that lets people
use the shell and run IPython Notebook.  (This requires some scut work but
nothing terribly difficult.)  If we base this off of `StarCluster <http://starcluster.mit.edu>`__ then
instructors can (optionally) do a StarCluster lesson, too.

**Recommendation**: Provide Anaconda, virtualenv, and virtual machine
instructions for each software install.

**Recommendation**: Provide video tutorials of the Anaconda and VM install,
so that people can tell if they've done it properly.

And now it's time for a rant.  *We all suck.* The fact that we, as
computer people, put up with all of this hard to install software is
incredibly depressing.  Even worse, it's not for a good reason -- it's
because computer people are lazy when writing software and happy to
spend the time on the back end to figure out its complexities.  We
should stop using packages that are hard to install, or yell more
loudly at the people building such packages.  It's incredibly
frustrating and infuriating, and it's holding us up as a society,
at this point.

Hosting and editing workshop materials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Software Carpentry tutors list continues go have "robust"
conversations on how best to host and edit workshop materials,
especially in a collaborative setting.

This was the first workshop where we tried out `github's online
editing capability of the ReadTheDocs-hosted site
<http://ivory.idyll.org/blog/rtd-comments-and-editing.html>`__.  It
went OK -- the online editing was less important for the teachers than
was the automatic updating of the course Web site (see
http://swc-scripps.idyll.org).  Tracy kept on wanting to use the
github site, which natively rendered the reStructuredText documents,
instead of the Sphinx-based ReadTheDocs site.  I personally think the
extra structured offered by Sphinx is nice but don't have any real
evidence of that ;).

Our workflow for the online materials was to outline our proposed
tutorial sections, adapting existing materials as possible or writing
new ones as needed, and then post those to the site in preparation.
I used IPython Notebooks a fair bit for introducing Python code and
shell commands, and added those to the online materials after each
tutorial section.

This all worked pretty well but required a significant effort on
post-session Web site cleanup and editing.

My takeaway from this was that, like anything else worthwhile, there
is still a significant barrier to entry in reStructuredText, and
because of this (as well as the general time and attention required to
maintain things) that you need to have someone pretty dedicated to
the site.

I still like the online editing but it wasn't as useful as I'd hoped.
This might be because we didn't introduce people to github until
late in the second day, though.  I still hold out hope!

**Recommendation**: have someone whose job it is to keep the Web site
updated and sane.

**Recommendation**: have a static site that is *auto-updated* from
github; ReadTheDocs can do this for Sphinx/reStructuredText sites.
(Q: can gh pages do this for Jekyll sites?)

**Recommendation**: use reStructuredText and Sphinx, or Jekyll and
Markdown, to build full sites.  Don't use individual pages.  Students
like having a single Web site to go to, and github just confuses
them.

**Recommendation**: provide a simple alias for the Web site.  We used
http://scripps-swc.idyll.org/ (a domain that I own).  Make it easy to
remember and type in, so that students can do it even if they don't
have access to e-mail.  Software Carpentry should buy a simple domain
for this purpose.  (I'm happy to donate the swc.idyll.org
namespace...)

**Something to try next time**: introduce Web site editing earlier!

In-class interaction
~~~~~~~~~~~~~~~~~~~~

One of the problems I've always had during my shorter workshops is
getting significant feedback and interaction during the workshop.  For
longer workshops, students and TAs get to know each other quite well,
but during the shorter ones the stranger-danger and intimidation
factor seem to block many of the students from grabbing us and asking
questions.  This is important for a successful workshop: I like to
adapt my materials and presentations to what the students actually need
and are concerned with, and pacing presentations correctly is much
easier with feedback.  It's also nice to get feedback on the various
pages, e.g. "I couldn't follow these instructions, but this tweak
helped."

As part of the ReadTheDocs site, I'd provided disqus commenting; for
`our two-week summer next-gen sequence analysis course <http://bioinformatics.msu.edu/ngs-summer-course-2012>`__, this
was successful in terms of garnering topic-specific feedback during
and after the course.  I'd hoped that the zero-entry disqus system
would encourage people to do that during shorter course.  That turned
out not to work at all for this course, or at least it wasn't used
at all :).

The surprise success was `hipchat <http://www.hipchat.com/>`__, a
realtime online discussion forum.  As you can see `from
<http://swc-scripps.idyll.org/en/latest/_static/14.html>`__ `the
<http://swc-scripps.idyll.org/en/latest/_static/15.html>`__
`transcripts
<http://swc-scripps.idyll.org/en/latest/_static/16.html>`__, we
started to get increasingly many comments and questions this way as
the course progressed, and it was nice to see.  I also took to posting
bits of code from the IPython Notebooks to hipchat so that people
could monitor the forum to grab code instead of typing it in from the
screen.

I've tried things like hipchat before (there was a Python-related one,
convore, a few years back that I used) and never found them all that
useful.  What was different this time?

I think the success of hipchat rested on Andrew's initial enthusiasm
for it, and Cait's continued use of it to answer questions and post
links.  You really need someone monitoring this kind of forum full
time, and Cait used it effectively to debug people's problems and
(failing remote intervention) to get them to raise their hand so
she could go help them in person.

I would definitely use hipchat (or something similar) again.

**Recommendation**: Use an online realtime discussion forum, but
expect to need to have someone really focused on answering questions
on it.

Real world applications
~~~~~~~~~~~~~~~~~~~~~~~

I implemented a "real" end-to-end example of a pipeline combining
shell and Python on the first day, and Tracy wrote a full Python data
munging script for a student's problem on the second day.  I think
this helped motivate the students to realize that this was both very
useful stuff, and that while "complexity" awaited in every direction,
it was nonetheless manageable.

**Recommendation**: embrace some real world complexity, if only to show
the students what it looks like.

Miscellaneous points and problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Paths are always a big sticking point. People just don't get
paths. Everyone is on a different computer, running software from a
different install, and no one can ever figure out what directory
they're in or where the software they need to run is.  It's not clear
if we need more instruction up front, or if this is something that
just takes time.

Speaking of things that just take time: don't bother trying to teach
people who don't have any programming experience to program in a
workshop!  It takes weeks or months to do that.  If they know some
Perl or Ruby or Matlab, then I bet that you can usefully throw some
Python at them.

I got my first really strong recommendations for OpenCourseWare (the
MIT lectures) and the Khan Academy from a student in the workshop who
said he'd learned to program from them -- never heard that before.  He
wanted to know why we weren't recommending them, or at least providing
the links.  I asked some CS profs and got answers that, on reflection,
seemed somewhat strange; something to expand on later.  My current
take is that I'll recommend them for people who want to learn more
Python, but not over taking a class or finding a good book.

Outcomes
~~~~~~~~

There were a few really useful outcomes, apart from the generally positive
comments from students.

First, most of the students in the class laughed at the `'sudo make me
a sandwich' comic <http://xkcd.com/149/>`__.  That's real progress,
folks -- more people being inculcated into nerd culture++.

Second, I got the sense that people came out of the class with some
very specific requests for TSRI's computing infrastructure (like:
provide UNIX workstations, running IPython Notebook).  This kind of
thing is good to see, especially when the requests and comments are
coming from the field that's the ignored step-child of scientific
computing, biology.

Third, Andrew seemed to get a lot of out of hosting the workshop.
Maybe he'll host more!  This one filled up in about 4 hours, and the
class plus wait list had over 90 people on it.  This is clear evidence
of demand!  (Warning, Andrew -- our rates will triple for the next
one! ;)

Fourth, someone from the Salk Institute sat in and will be pitching SWC
to the Salk.

Fifth, Tracy and Qingpeng and Cait all got to see what running a workshop
was like, and seem to have thoroughly enjoyed it.  So now they can
run workshops all on their own!

.. @@DOI
