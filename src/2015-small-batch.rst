Small batch, artisanal, hand-crafted bioinformatics training
############################################################

:author: C\. Titus Brown
:tags: ngs-course,ngs,swc
:date: 2015-08-31
:slug: 2015-small-batch
:category: teaching

On June 11th, 2010, I remember dropping the last workshop attendee off
at the Kalamazoo train station, turning the car towards home, and
nearly sobbing in relief that workshop was over and done and I could
finally get some sleep now.  `That workshop
<http://bioinformatics.msu.edu/ngs-summer-course-2010>`__ was the
first of a series of now `six summer workshops
<http://bioinformatics.msu.edu/ngs-summer-course-2015>`__ that I've
coordinated over the last 6 years, and, as much as anything else,
they've defined my academic career.

The third and final week of our sixth go, the `2015 workshop on
Analyzing Next-Generation Sequencing Data
<http://bioinformatics.msu.edu/ngs-summer-course-2015>`__, just
finished, and (as far as I can tell) it went great.  This year we
essentially ran `two consecutive workshops
<http://ivory.idyll.org/blog/2015-summer-course-NGS.html>`__ - the
first two weeks was our "standard" `zero-entry from-scratch
bioinformatics workshop <http://angus.readthedocs.org/en/2015/>`__,
and the third week was an almost entirely different workshop.  During
the third week, we had a bunch of instructors come and give advanced
tutorials to alumni and other more advanced bioinformaticians.

Why did
we do the third week?

The third week
--------------

The `third week <http://angus.readthedocs.org/en/2015/week3.html>`__
was an attempt to answer the question, "what next?" for people who
already had some basic computing background and wanted to fill out
their knowledge and experience base.  As of last year, we have about
125 alumni - now up to 150 (!) - of the first two weeks, and I
thought that some of them might be interested in getting together for
...more.  I'd tried to do a third week last year but it fell apart
in the face of bad organization (my fault) and too few attendees.

This year, I tried recruiting a bunch of external instructors.  I
wanted to find a bunch of enthusiastic and experienced trainers who
could deliver bioinformatics-relevant material at a high level.  So,
in late March, I put out an open call on the Software Carpentry
instructors mailing list::

   Hi all,

   see http://ivory.idyll.org/blog/2015-summer-course-NGS.html.

   “””
   For this third week, we are also looking for a few
   instructors/lecturers; travel and lodging would be covered. Drop me
   an e-mail if you are a trained Software Carpentry or Data Carpentry
   instructor and are interested in coming and hanging out with us for
   a week to develop materials and approaches!
   “”"

   If there are SWC instructors interested in trialing their own
   genomics material on a captive audience, investigating
   reproducibility awesomeness, or otherwise coming and hanging out to
   teach and train and develop, please respond privately to this
   e-mail.  The location is quite nice, and the people are great!

and... this worked! Astonishingly well!  After applying stringent
selection criteria (I accepted everyone who responded), and after
sorting out all the travel, we ended up with eight instructors and
myself.  They were joined by approximately 10 students, along with our
crack TA/organizing team, Amanda Charbonneau and Jessica Mizzi.

You can see the `detailed schedule here <http://angus.readthedocs.org/en/2015/week3.html>`__, but essentially I just divvied the week up into three hour
chunks and gave the instructors the following guidelines:

* please plan your presentations to be interactive, copy-paste, and
  cloud-based.  They should be in Markdown or reST, and under a
  permissive CC license (I suggest CC0).

* ideally they would run on Amazon EC2.  Happy to help you get that
  working. If they don’t work on EC2 and work on individual laptops,
  make sure to allow LOTS of time for installation!

* I would like to have them on the ANGUS web site, on github here:
  https://github.com/ngs-docs/angus.  Please submit PRs!  I suggest
  putting them under week3/. I am happy to organize/link into the
  schedule.

* I’m reserving about 3 hours on the schedule for each one, which (by
  typical software carpentry etc experience) means an even mix of
  talking, running things, and troubleshooting/debugging.

* finishing early and allowing time for during- and after- discussions
  is fine and frankly recommended :)

* please introduce yourself at your tutorial - give a brief background
  of you and your research and your interests.

* you can see what we taught this year, here:
  http://angus.readthedocs.org/en/2015/ - gives you some sense of a
  style that we have found works well in this kind of workshop.

At this point let me digress a bit and say this: Software Carpentry is
effin' magical.  I don't know of another group of people to whom I
could have sent **an open invitation to come present**, gotten back a
bunch of replies from people I didn't know and invited them **without
screening them in any way**, sent a bunch of vague instructions like
the above, and then had them **all show up** and **give great
presentations.**

So, yeah, the week3 stuff went really well.  Completely apart from the
student learning, several different instructors independently told me
that they'd learned something from every presentation.

Here is the menu:

* Ryan Williams (Iowa State) gave a **tutorial on multivariate stats**
  that started out a bit slow and then all of a sudden we were like
  HOLY COW HOW DID WE WAIT I DIDN'T KNOW OK THAT'S COOL.  `(Lisa's notes) <https://monsterbashseq.wordpress.com/2015/08/25/multivariate-tests-with-ngs-data-and-visualization-in-r-week-3-ngs-2015/>`__

* Lex Nederbragt (University of Oslo) did an **interactive tutorial on
  assembly** where he demoed two teaching techniques using Google Docs
  - ask questions poll for answers, discuss, repoll; and collaborative
  graphing, where we all added points to a Google Spreadsheet based on
  computing we did individually.  Super neat.  (See `Lex's blog post
  <https://flxlexblog.wordpress.com/2015/08/31/active-learning-strategies-for-bioinformatics-teaching-2/>`__
  for more on active learning, and `Lisa's notes on assembly <https://monsterbashseq.wordpress.com/2015/08/25/genome-assembly-week-3-ngs-2015/>`__)

* Marian Schmidt (University of Michigan) powered through into the
  evening with a thorough introduction to **RMarkdown, Git, and RStudio**.
  While I missed most of this due to a phone call, I got to experience
  the "power pose" -- a way to pump up everyone's energy level before
  sitting back down at RStudio.  Great quote from Lex: "Wow, this R
  stuff is really cool!"  `(Lisa's notes <https://monsterbashseq.wordpress.com/2015/08/25/reproducible-research-using-rmarkdown-ngs2015-week-3/>`__)

* Meeta Mistry (Harvard) gave an excellent three-way comparison of
  **DEseq 2, Limma, and edgeR** for differential expression analysis on an
  example RNAseq data set.  (I will be using this tutorial in three weeks!)
  `(Lisa's notes <https://monsterbashseq.wordpress.com/2015/08/26/rnaseq-differential-expression-analysis-ngs2015/>`__)

* Asela Wijeratne (Ohio State University) gave a *very* well received
  tutorial on **pathway analysis in RNAseq**.  Sadly I missed most of this
  due to a migraine (bad weather + too much caffeine + too little sleep ;(
  but I got many positive reviews.  I'm going to have to go through this
  on my own.  `(Lisa's notes <https://monsterbashseq.wordpress.com/2015/08/26/pathway-analysis-for-rnaseq-data-ngs2015/>`__)

* Tiffany Timbers (Simon Fraser University) showed us all how to do
  **Genome Wide Association Studies**.  Her tutorial was a masterclass on
  data munging - she had us pipe data through about 6 different programs,
  and I think we ended up transforming the data using R, sed, grep and cut,
  multiple times.  There was an entertaining moment when Lex figured out
  that she was presenting technical questions from her own research,
  in effect using us as pre-reviewers for her paper ;).  `(Lisa's notes <https://monsterbashseq.wordpress.com/2015/08/26/gwas-for-ngs-data-ngs2015/>`__)

* Leigh Sheneman (Michigan State University) gave an excellent
  presentation on **using AMIs and snapshots on Amazon Web Services**, for
  reproducibility purposes.  People were incredibly thankful to have
  all this explained and I got several very positive reviews
  afterwards. `(Lisa's notes <https://monsterbashseq.wordpress.com/2015/08/27/reproducibility-with-aws-ngs2015/>`__)

* Chris Hamm (University of Kentucky) talked about **detecting sex-linked
  differential expression via dosage compensation**.  Two highlights of
  his talk: (1) we all realized how insanely into butterflies he is
  (see: `@butterflyology <https://twitter.com/butterflyology>`__); (2)
  he managed to produce some figures so beautiful that we spontaneously
  applauded. `(Lisa's notes <https://monsterbashseq.wordpress.com/2015/08/27/differential-expression-and-dosage-compensation-in-rnaseq-ngs2015/>`__)

* I gave two tutorials, one on Docker and one on GitHub pull requests &
  collaborative documentation editing.  People seemed to find them both
  interesting, although Docker confused people the most of all the topics
  in the workshop.  (See `Lisa's notes on Docker <https://monsterbashseq.wordpress.com/2015/08/24/ngs-2015-week-3-docker-tutorial/>`__ and `Lisa's notes on GitHub/PRs <https://monsterbashseq.wordpress.com/2015/08/28/github-pull-requests-and-readthedocs-ngs2015/>`__.)

Throughout all of this, the instructors and students were very
engaged.  It was kind of hilarious to have 1:1 ratio of instructors
and students, when we were also using `the sticky system
<https://dynamicecology.wordpress.com/2015/01/13/sticky-notes-as-a-teaching-and-lab-meeting-tool/>`__
-- no sooner would a pink sticky go up (indicating trouble) then would
three different instructors converge on the pink sticky and work to
solve the problem.  Amazing to watch.

For me (and many instructors), the third week was also awesome in a
different way.  I had seen *most* of the subject material before, so
while the details were interesting, I don't know that they would have
held my attention in all cases.  But, not only were the materials
interesting, the instructors were *awesome* and each had their own bag
of tricks.  Most of them weren't something that I could write down,
apart from the technical stuff mentioned above, but everyone had their
own style and energy and approach for holding the attention of the
audience, and it was a privilege to experience so many teaching styles.

Here's the feedback:

.. figure:: ../static/images/ngs-2015-week3-whiteboard.jpg
   :width: 80%

and here are `Lisa's notes on the whole week <https://monsterbashseq.wordpress.com/2015/08/28/week-3-ngs2015/>`__.

Why did we all do the third week?
---------------------------------

A week is ... a lot of time.  Why did everyone show up and what did
people get out of it?  I have a few thoughts.

* We selected students who already had a reasonably strong exposure
  (alumni from previous workshops, or people with significant
  practical experience).  This meant that we had 10x less in the way
  of problems with software installs and copy/paste/typing issues (which
  is what dominates the first week of the two-week course).  This led
  in turn to a much faster pace, which I think was fun for everyone involved.

* Researchers are hungry for advanced materials. I had a lot of
  trouble figuring out how to pitch this, which is one reason why the
  3rd week in 2014 failed, and why I worked extra hard this year to
  bring in students; people weren't willing to put in a week on the
  vague hope that it would be interesting: they wanted specifics.  If
  and when we do this again, though, the pitch is easy: "Come learn
  the cutting edge of bioinformatics practice."

* Everyone was a great teacher - energetic, engaged, passionate.  That's
  actually kind of rare in workshops :).

* Software Carpentry instructors rarely get a chance to learn en masse
  from other Software Carpentry instructors.

* Socializing and networking.  The NGS workshop has always had a
  significant component of hanging out, because, well, that's fun.
  It's also productive for careers.  This socializing is aided by
  things like trips to breweries, a lot of volleyball (with no
  expectations of expertise), a beautiful environment, and lots of
  downtime for relaxation and interaction.
  similar to Gordon Conferences.)

* Everyone likes to know what they know, especially if they learned it
  in isolation.  Comments from the students, in particular, tended to
  mention that they had *seen* lots of this stuff, but hadn't necessarily
  put it all together or filled in the gaps in their knowledge.  Finding out
  that you actually *do* know a lot is great; rounding it out with experience
  and more information is even better.

* Material development was an explicit goal of mine.  We got a lot of
  good (open) material out of this, and I'm already planning on reusing
  a bunch of it!

Having run this once, I honestly don't anticipate a problem in "selling" it
going forward.

Are you going to run it again?
------------------------------

tl;dr? Probably, but probably some other time/place.

This was an awesome experience for everyone I talked to.

But it was also three weeks, and the people who really stuck it out
the *entire* time had our brains turned into mush by it.  So I think
we probably won't run three weeks again.

But there's really no reason to tie the third week to the first
two-week workshop.  So maybe we can do that elsewhere and elsewhen.

It cost (I estimate) $2500 for me to run.  If I ran it "cold" (not
tied to the two-week workshop) it would probably be about $5000.  I
have enough money to do that again, perhaps even a few times.  (Most
of the costs are in instructor travel/room/board.)

We could probably run a bunch on more specific topics like "RNAseq",
"environmental metagenomics", etc, although I'd want to keep many of
the technical things (Amazon, Docker, workflows, reproducibility,
etc.) as those were well received.

This sounded great! How are you going to scale it so I can come?
----------------------------------------------------------------

I *don't* want to scale it up much.  I think it would actually be a
huge mistake to scale this beyond ~30-40 people, total.  Good learning
at this level (and maybe at any level) simply doesn't happen with mass
teaching, or with low instructor-student ratios.

I'd *love* to see other people run things like this, though. I think
the answer to scaling is "run more" not "run bigger", and it seems to
be easy to sucker Software Carpentry instructors into advanced
teaching in nice places.

With that in mind, I have an offer: if you want to run something like
this in the area of data-intensive biology, let's chat.  I have money
and organizational capacity, and if you can supply a remote location
with decent lodging and good weather, maybe we can work something out.
There are a few strong requirements on my side (keep it cheap for
students; all materials posted CC0 or CC-BY; you host, we run; we need
tech advanced biology students; and probably a few more things to
ensure a good experience for all concerned) but I'd love to see how
far we can take this.

--titus
