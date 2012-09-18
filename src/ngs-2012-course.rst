Analyzing Next Generation Sequencing Data - 2012 Course
#######################################################

:author: C\. Titus Brown
:tags: science,ngs,teaching
:date: 2012-09-17
:slug: ngs-2012-course
:category: science

We held the `2012 workshop on Analyzing Next Generation Sequencing Data <http://bioinformatics.msu.edu/ngs-summer-course-2012>`__
from June 4 to June 15, at the Kellogg Biological Station in western
Michigan, about 30 minutes north of Kalamazoo.

(This is a long delayed blog post. :)

The goal of the workshop is to take biologists with little in the way
of computational knowledge and bring them up to speed on doing
bioinformatics data analysis of next-gen data.  We don't want to turn
them into practicing computer science researchers, but rather we want
to get them to the point where they can run their own analyses using
other tools and some small amount of scripting.  It's a tricky thing
to manage!

This year the course was sponsored by NIH (`through an R25 grant <http://ged.msu.edu/downloads/2010-ngs-course-nih-r25.pdf>`__),
which let us expand our set of invited faculty.  The faculty this year
included Ian Dworkin from MSU, Istvan Albert from PSU, Corbin Jones
from UNC, Erich Schwarz from Caltech & Cornell, and Julian Catchen
from Oregon State.

We also had 4 TAs from my lab: Adina Howe, Qingpeng Zhang, Jaron Guo,
and Likit Preeyanon.  Many people came up to me and told me what a
great job they'd done, which is always nice to hear; no heads need
roll.

Applicants
----------

We received a total of 168 applications from researchers.  110
researchers were from the US; 25% of US applicants come from Michigan,
with the remaining 75% split across 35 other states, including 12 from
California, 8 applicants from Arizona, 6 from Wisconsin and North
Carolina, and 5 or fewer from each of the other 31 states.  We also
had over three dozen international applicants, including applicants
from Germany, Norway, Brazil, Slovenia, Portugal, Spain, Australia,
New Zealand, and France.

Most notably, we had over 22 tenure-line faculty apply to the
workshop!

We used biological system of choice, data sets already available,
bioinformatics approaches needed, and existing knowledge/background to
choose a broad range of students that included vertebrate,
invertebrate, microbial, and plant researchers.

We admitted 8 graduate students, 10 postdocs, 4 tenure-line faculty,
and 3 industry or independent researchers.  The workshop participants
are spread across the US and the world, with 4 from Michigan, 2 from
Pennsylvania, and participants from several other states including CA,
OH, KA, NH, IL.  International participants included people working in
Mexico, Canada, France, Spain, and Switzerland.

Workshop
--------

We spent between 6 and 10 hours each day on lectures, tutorials, and
free working time.  (We also included plenty of time for frisbee,
volleyball, swimming, napping, and running -- think summer camp for
scientists!)  Several people told us that they really liked the
balance of activities, which let them stay sharp and alert during the
lessons without getting bored by too much instruction.

Course Materials
----------------

As always, the `majority of the course materials are available online
<http://ged.msu.edu/angus/tutorials-2012/>`__ under a CC-BY-SA
license.  This year we put the disqus commenting system in place,
which let students ask questions and provide feedback that was
recorded.  (Seemed to work well!)

One big shift this year was in using the ipython notebook.  Some
people found it distracting (it's one more thing to learn, on top of
the shell and some minimal programming and a bunch of tools!) while
others found it super-awesome; either way, we produced `a bunch of
notebooks <https://github.com/ngs-docs/ngs-notebooks>`__ that
illustrate how to run BLASTs, use khmer and screed, etc.  (You can see
video introductions to the ipython notebook `here
<http://ged.msu.edu/angus/beacon-2012/week1.html>`__, under my current
fall course.)

Another big shift this year was that I had personal research content
to introduce.  While I didn't want to make the course all about our
stuff, which is still in the process of being published, every third
student had a problem that could be addressed with digital
normalization.  So, I introduced digital normalization early in the
second week, and had the TAs talk about their research then as well.
(It went better than expected.)

Critiques
---------

Every year, at the end of the course we do a post-mortem, where people
are supposed to say mostly negative things.  As in previous years,
most of the critiques were about how we handled basic UNIX and
programming knowledge; we try to walk the line between motivating the
UNIX shell, Python, etc., and actually teaching them about it.  It's
tough!  But nothing terribly serious other than the usual "more stuff/
better taught"...

Evaluation
----------

This is the first year where we had a formal external evaluation done
for us.  As I've mentioned before, `I think assessment and evaluation
are critical
<http://ivory.idyll.org/blog/ngs-course-where-next.html>`__: they let
us determine whether or not the students are learning what we want to
teach them, and helps us target future efforts more precisely.

The evaluation results came in a week or two ago -- and, I quote:

   A pre-workshop evaluation of the NGS Summer Workshop 2012 -
   Analyzing Next-Generation Sequencing Data was conducted on June 4,
   with a post-workshop evaluation occurring June 15, 2012. Observations
   were also conducted at the start, middle, and end of the workshop. In
   all, 25 participants completed the pre-survey and 23 completed both
   the pre- and post-surveys.

   **EXECUTIVE SUMMARY OF RESULTS**

   We summarize
   evaluation results below. [ ... ]

   In summary, we found that:
   
   1. Scores on the Perception of Computational Ability scale were
      calculated for both the pre- and post-workshop surveys. Results from
      the Wilcoxon Signed Ranks Test indicate that pre- and post-workshop
      results are statistically different (Z = -4.116, p <= 0.001), with
      higher post-workshop scores. This indicates that participants
      perceived greater computational ability after engagement in the
      workshop.

   2. Scores on the Computational Understanding - Sequencing
      Data scale were calculated for both the pre- and post-workshop
      surveys. Results from the Wilcoxon Signed Ranks Test indicate that
      pre- and post-workshop results are statistically different (Z =
      -4.111, p <= 0.001), with higher post-workshop scores. This indicates
      that participants perceived greater understanding after engagement in
      the workshop.

   3. Scores on the Python Coding Ability scale were
      calculated for both the pre- and post- workshop surveys. Results from
      the Wilcoxon Signed Ranks Test indicate that pre- and post-workshop
      results are statistically different (Z = -4.374, p <= 0.001), with
      higher post- workshop scores. This indicates that participants
      perceived greater coding ability after engagement in the workshop.

   4. Participants were generally very satisfied with the workshop. On
      average, participants rated the workshop components as Good-Very Good.

   5. Participants generally felt the workshop met their needs and would
      overwhelmingly recommend it to others.

   6. Participants were generally
      positive about the workshop in their open-ended comments. Suggestions
      for improvement include: more time on RNA sequencing and differential
      expression/data, less focus on why tools are not good, more focus on
      basics of programming, scripts and/or UNIX early on, and more details
      about daily activities.

The informal summary by our evaluator was "you nailed it" - always nice
to hear!  The above results are slightly squishy because they are based
on self-perception; we are hoping to get more objectively quantifiable
results out of the free form essays.  However, I think we can be reasonably
certain that if the students hated the course, they would not be learning
very much, so ... so far, so good.

We are currently working on coding the free-form essays in preparation
for a publication on educating advanced biologists in computation;
I'll post those results when I can.

2013 and Beyond
---------------

The course is funded for one more year, through 2013.  I've done some
`hand-wringing
<http://ivory.idyll.org/blog/ngs-course-where-next.html>`__ about
whether or not I should run the course in the future.  There are lots
of reasons *not* to run the course: it's not strongly valued by MSU,
it doesn't bring in much money, it consumes a big chunk of my summer
time, and frankly it's a lot of work!  But... in many ways it's
strongly affected my research program for the better.  I understood de
Bruijn graph assembly because I had to learn it to teach the 2010
course, for example; and now I'm publishing in the area, two years
later.  Each year I get a dose of opinion about what is holding people
back, and this lets me target and refine my bioinformatics research.
This year, I figured out how to apply digital normalization to 454
data (or, rather, how to evaluate it ON such data, which is more
important); and I developed some potentially great ideas on how to do
better mRNAseq quantitation.  Teaching is good for research!  (There's
also `evidence that graduate students' teaching improves their
research, too
<http://www.sciencemag.org/content/333/6045/1037.abstract>`__.)

It also serves as a great networking tool, of course -- I've been
invited to give 4 or 5 talks by previous students so far -- and this
year we had some really excellent sequencing center folk who could
give me the skinny on the various platforms, which was valuable.
Admitting senior faculty has its pluses as well; one of the attending
full professors offered to write me a tenure evaluation letter based
on the high quality of the course (!).

So, largely because of these research impacts, I've decided to apply
again to the NIH to run the course in the future, and I may also be
trying to figure out a Research Coordination Network (NSF) of some
kind to expand our efforts.  I'm trying to figure out how to continue
bringing in new ideas and tools to the course; one idea is run an
additional "advanced tools" discussion breakout at something like
Plant & Animal Genome, where we could get some candid opinions on
tools and figure out what tools are good/better/best.

...suggestions welcome.

Anyhoo, the application is due next Tuesday.  Wish me luck!

--titus
