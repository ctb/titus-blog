Top 12 reasons you know you are a Big Data biologist
####################################################

:author: C\. Titus Brown
:tags: big-data,ngs,python
:date: 2012-03-07
:slug: big-data-biology
:category: python


A few people have recently asked me what this "Big Data" thing is in
biology.  It's not an easy question to answer, though, because
biology's a bit peculiar, and a lot of Big Data researchers are not
working in bio.  While I was thinking about this I kept on coming up
with anecdotes -- and, well, that turned into this: the Top 12 Reasons
You Know You Are a Big Data Biologist.

---

0. You no longer get enthused by the prospect of more data.

I was at a conference a few months back, and an Brit colleague of mine
rushed up to me and said, "Hey!  We just got an Illumina HiSeq! Do you
have anything you want sequenced?"  My immediate, visceral response
was "Hell no!  We can't even deal with a 10th of the sequence we've
already got!  PLEASE don't send me any more! Can I PAY you to not send
me any more?"

1. Analysis is the bottleneck.

I'm dangerously close to `genomics bingo <https://docs.google.com/spreadsheet/ccc?key=0AkNPpmDaw5GhdFUyRFJ5TDd2b2l6Wlg3TnJKTl9ySGc#gid=0>`__ here, but:

I was chatting with a colleague in the hallway here at MSU, pitching
some ideas about microbiome work, and he said, "What a good idea!  I
have some samples here that I'd like to sequence that could help with
that."  I responded, "How about we stop producing data and think about
the analysis?"  He seemed only mildly offended -- I have a rep, you
see -- but biology, as a field, is wholly unprepared to go from
data to an analyses.

My lab has finally turned the corner from "hey, let's generate more
data!"  to "cool, data that we can analyze and build hypotheses from!"
-- yeah, we're probably late bloomers, but after about 3 years of tech
development, there's very little we *can't* do at a basic sequence
level.  Analysis at that level is no longer the bottleneck.  Next
step?  Trying to do some actual biology!  But we are working in a few
very specific areas, and I think the whole field needs to undergo this
kind of shift.

2. You've finally learned that 'for' loops aren't all they're cracked up to be.

This was one of my early lessons.  Someone had dumped a few 10s of
millions of reads on me -- a mere gigabyte or so of data -- and I was
looking for patterns in the reads.  I sat down to write my usual
opening lines of Python to look at the data: "for sequence in
dataset:" and ... just stopped.  The data was just too big to do
iteration in a scripting language with it!  Cleverness of some sort
needed to be applied.

Corollary: not just Excel, but BLAST, start to look like Really
Bad Ideas That Don't Scale.  Sean Eddy's HMMER 3 FTW...

3. Addressing small questions just isn't that interesting.

Let's face it, if you've just spent a few $k generating dozens of
gigabytes amounts of hypothesis-neutral data on gene expression from
(say) chick, the end goal of generating a list of genes that are
differentially regulated is just not that exciting.  (Frankly, you
probably could have done it with qPCR, if you didn't want that cachet
of "mRNAseq!")  What more can you do with the data?

(This point comes courtesy of Jim Tiedje, who says (I paraphrase):
"The problem for assistant professors these days is that many of may
not be thinking big enough."  Also see: `Don't be afraid of failure:
really go for it
<http://www.cccblog.org/2012/02/28/darpa-director-dont-be-afraid-of-failure-really-go-for-it/>`__)

The biggest training challenge (in my opinion) is going to be training
people in how to push past the obvious analysis of the data and go for
deeper integrative insight.  This will require training not just in
biology but in data analysis, computational thinking, significant
amounts of informed skepticism, etc. (See `our course <http://bioinformatics.msu.edu/ngs-summer-course-2012>`__.) I think about it
like this: generating hypotheses from large amounts of data isn't that
interesting -- I can do that with publicly available data sets without
spending any money!  *Constraining* the space of hypotheses with big
data sets is far more interesting, because it gives you the space of
hypotheses that aren't ruled out; and its putting your data to good
use.  I'll, uh, let you know if I ever figure out how to do this
myself...

I think there are plenty of people that can learn to do this, but as
Greg Wilson correctly points out, there has to be a tradeoff: what
do you take out of existing training curricula, to be replaced with
training in data analysis?  I wish I knew.

4. Transferring data around is getting more than a bit tedious.

For some recent papers, I had to copy some big files from EC2 over to
my lab computer, and from there to our HPC system.  It was Slow, in
the "time for lunch" sense.  And these were small test data sets,
compressed.  Transferring our big data sets around is getting tedious.
Luckily we have a lot of them, so I can usually work on analysis of
one while another is transferring.

5. Your sysadmin/HPC administrator yells at you on a regular basis about your
disk usage.

We regularly get nastygrams from our local sysadmins accusing of using
too many terabytes of disk space.  This is in contrast to the good ol'
days of physics (which is where I got my sysadmin chops), where your
sysadmin would yell at you for using too much CPU...

6. You regularly crash big memory machines.

My favorite quote of the year so far is from the `GAGE paper
<http://www.ncbi.nlm.nih.gov/pubmed?term=gage%20salzberg>`__), in
which Salzberg et al (2012) say "For larger genomes, the choice of
assemblers is often limited to those that will run without crashing."
Basically, they took a reasonably big computer, threw some big data at
various assembly packages, and watched the computer melt down.  Repeatedly.

Someone recently sent me an e-mail saying "hey, we did it!  we took 3
Gb of sequence data from soil and assembled it in only 1 week in 3 TB
of RAM!"  Pretty cool stuff -- but consider that at least four to six
runs would need to be done (parameter sweep!), and it takes only about
1 week and $10k to generate twice that data.  In the long run, this
does not seem cost effective.  (It currently takes us 1-2 months to
analyze this data in 300 GB of RAM.  I'm not saying we have the
answer. ;)

7. Throwing away data looks better and better.

I made a kind of offhanded comment to a NY Times reporter once (hint: don't do
this) about how at some point we're going to need to start throwing away data.
He put it as the ultimate quote in his article.  People laughed at me for it.
(BUT I WAS RIGHT!  HISTORY WILL SHOW!)

But seriously, if someone came up to you and said "we can get rid of
90% of your data for you and give you an answer that's just as good",
many biologists would have an instant negative response.  But I think
there's a ground truth in there: a lot of Big Data is *noise*.  If you
can figure out how to get rid of it... why wouldn't you?  This is an
interesting shift in thinking from the "every data point is precious
and special" that you adopt when it takes you a !#%!#$ week to
generate each data point.

I attended a talk that David Haussler gave at Caltech recently.  He
was talking about how eventually we would need to resequence millions
of individual cancer cells to look for linked sets of mutations.  At
50-300 Gb of sequence per cell, that's a lot of data.  But most of
that data is going to be uninteresting -- wouldn't it be great if we
could pick out the interesting people and then throw the rest away?
It would certainly help with data archiving and analysis...

8. Big computer companies call you because they're curious about why
you're buying such big computers.

True story: a Big Computer Company called up our local HPC to ask why
we were buying so many bigmem machines.  They said "It's the damned
biologists -- they keep on wanting more memory.  Why?  We don't know -
we suspect the software's badly written, but can't tell.  Why don't
you talk to Titus?  He pretends to understand this stuff."  I don't
think it's weird to get calls trying to sell me stuff -- but it *is* a
bit weird to have our local HPC's buying habits be so out of
character, due to work that I and others are doing, that Big Computer
Companies notice.

(Note: the software's not mine, and it's not badly written, either.)

9. Your choice must increasingly be "improve algorithms" rather than "buy
bigger computers"

I've been banging this drum `for a while <http://ivory.idyll.org/blog/aug-11/cloud-not-the-solution.html>`__.  Sequencing
capacity is outpacing Moore's Law, and so we need to rethink
algorithms.  An algorithm that was nlogn used to be good enough; now,
if analysis requires a supra-linear algorithm, we need to figure out
how to make it linear.  (Sublinear would be better.)

Anecdote: we developed a nifty data structure for attacking metagenome assembly
(see: http://arxiv.org/abs/1112.4193).  It scaled (scales) assembly by a factor
of about 20x, which got us pretty excited -- that meant we could in theory
assemble things like `MetaHIT <http://www.nature.com/nature/journal/v464/n7285/full/nature08821.html>`__ and `rumen <http://www.sciencemag.org/content/331/6016/463.abstract>`__ on commodity hardware without doing
abundance filtering.  Literally the day that we told our collaborators we
had it working, they dumped 10x more data on us and told that they could send
us more any time we wanted.  (...and that, boys and girls, was our introduction
to the HiSeq!)  20x wasn't enough.  Sigh.

The MG-RAST folk have told me a similar story.  They did some
awesomely cool engineering and got their pipeline running about 100x
faster.  That'll hold them for a year or so against the tidalwave of
data.

Corollary: don't waste your time with 2% improvements in sensitivity and
specificity unless you also deliver 10x in compute performance.

10. You spend a lot of time worrying about biased noise, cross-validation, and
the incorrect statistical models used.

We were delayed in some of our research by about a year, because of
some systematic biases being placed in our sequencing data by
Illumina.  Figuring out that these non-biological features were there
took about two months; figuring out how to remove them robustly took
another 6 months; and then making sure that removing didn't screw up
the actual biological signal took another four months.

This is a fairly typical story from people who do a lot of data analysis.
We developed a variety of cross-validation techniques and ways of intuiting
whether or not something was "real" or "noise", and we spent a certain
amount of time discussing what statistical approaches to use to assess
significance.  In the end we more or less gave up and pointed out that
on simulated data what we were doing didn't screw things up.

11. Silicon Valley wants to hire your students to go work on non-biology problems.

Hey, it's all Big Data, right?

---

So: what is Big Data in biology?

First, I've talked mostly about DNA sequence analysis, because that's
what I work on.  But I know that proteomics and image analysis people
are facing similar dilemmas.  So it's not just sequence data.

Second, compute technology is constantly improving.  So I think we
need moving definitions.

Here are some more serious points that I think bear on what, exactly,
problems for Big Data in biology.  (They're not all specific to biology,
but I can defend them on my home ground more easily, you see.)

1. You have archival issues on a large scale.

You have lots of homogeneously formatted data that probably contains
answers you don't know you're looking for yet, so you need to save it,
metadata it, and catalog it.  For a long time.

2. The rate at which data is arriving is itself increasing.

You aren't just getting one data set.  You're getting dozens (or hundreds)
this year.  And you'll get more than that next year.

One implication of this is that you'd better have a largely automated
analysis pipeline, or else you will need an increasing number of people
just to work with the data, much less do anything interesting.  Another
implication is that software reuse becomes increasingly important: if
you're building custom software for each data set, you will fall behind.
A third implication is that you need a long-term plan for scaling your
compute capacity.

3. Data structure and algorithm research is increasingly needed.

You cannot rely on many heavyweight iterations over your data, or
simple data structures for lookup: the data is just too big and
existing algorithms are tailored to smaller data.  For example, BLAST
works fine for a few gigabytes of data; past that, it becomes
prohibitively slow.

4. Infrastructure designers are needed.

Issues of straightforward data transfer, network partitioning, and
bus bandwidth start to come to the forefront.  Bottleneck analysis
needs to be done regularly.  In the past, you could get away with
"good enough", but as throughput continues to increase, bottlenecks
will need to be tackled on a regular basis.  For this, you need
a person who is immersed in your problems on a regular basis; they
are hard to find and hard to keep.

One interesting implication here is for cloud computing, where
smart people set up a menu of infrastructure options and you can
tailor your software to those options.  So far I like the idea,
but I'm told by aficionados that (for example) Amazon still falls
short.

5. You have specialized hardware needs.

Sort of a corollary of the above: what kind of analyses do you need to
do?  And what's the hardware bottleneck?  That's where you'll get the
most benefit from focused hardware investment.

6. Hardware, infrastructure design, and algorithms all need to work together.

Again, a corollary of the above, but: if your bottleneck is memory, focus
on memory improvements.  If your bottleneck is disk I/O, focus on hardware
speed and caching.  If your bottleneck is data transfer, try to bring your
compute to your data.

7. Software needs to change to be reusable and portable.

Robust, reusable software platforms are needed, with good execution
guarantees; that way you have a foundation to build on.  This software
needs to be flexible (practically speaking, scriptable in a language
like Python or Ruby or Perl), well developed and tested, and should
fade into the background so that you can focus on more interesting
things like your actual analysis.  It should also be portable so that
you can "scale out" -- bring the compute to your data, rather than
vice versa.  This is where Hadoop and Pig and other such approaches fit
now, and where we seriously need to build software infrastructure in
biology.

8. Analysis thinking needs to change.

Comprehensively analyzing your data sets is tough when your data sets
are really big and noisy.  Extracting significant signals from them is
potentially much easier, and some approaches and algorithms for doing
this in biology exist or are being developed (see especially
Lior Pachter's `eXpress <http://bio.math.berkeley.edu/eXpress/>`__).
But this is a real shift in algorithmic thinking, and it's also a real
shift in scientific thinking, because you're no longer trying do
understand the entire data set -- you're trying to focus on the bits
that might be interesting.

9. Analyses are increasingly integrative.

It's hard to make sense of lots of data on its own: you need to link it in
to other data sets.  Data standards and software interoperability and
"standard" software pipelines are incredibly important for doing this.

10. The interesting problems are still discipline-specific.

There are many people working on Big Data, and there is big business
in generic solutions.  There's lots of Open Source stuff going on,
too.  Don't reinvent those wheels; figure out how to connect them to
your biology, and then focus on the bits that are interesting to you
and important for your science.

11. New machine learning, data mining, and statistical models need to be
developed for data-intensive biological science.

As data volume increases, and integrative hypothesis development
proceeds, we need to figure out how to assess the quality and
significance of hypotheses.  Right now, a lot of people throw their
data at several programs, pick their favorite answer, and then recite
the result as if it's correct.  Since often they will have tried out
many programs, this presents an obvious multiple testing problem.
And, since users are generally putting in data that violates
one or more of the precepts of the program developers, the results
may not be applicable.

12. A lack of fear of computational approaches is a competitive advantage.

The ability to approach computational analyses as just another black
box upon which controls must be placed is essential.  Even if you can
open up the black box and understand what's inside, it needs to be
evaluated not on what you *think* it's doing but on what it's
*actually* doing at the black box level.  If there's one thing I try
to teach to students, it's to engage with the unknown without fear,
so that they can think critically about new approaches.

---

Well, that's it for now.  I'd be interested in hearing about what
other people think I've missed.  And, while I'm at it, a hat tip to
Erich Schwarz, Greg Wilson, and Adina Howe for reading and commenting
on a draft.

--titus


----

**Legacy Comments**


Posted by joe on 2012-03-06 at 21:23. 

::

   Hey!  I work in software, and your big data problems sound really
   familiar!    If you have students looking for work, please shoot an
   email my way....


Posted by Diane Trout on 2012-03-06 at 21:40. 

::

   Slightly off topic, but it reminded me of a semi-serious joke I made
   about our disk space usage.    My boss wants us to save all of the
   custom tracks loaded on our UCSC mirror because she might want to re-
   use an old analysis. But we're perpetually running out of disk, so the
   obvious solution was scan her mailbox for links to the tracks, and
   garbage collect the ones that have no references.    Also "Analyses
   are increasingly integrative." is why I'm interested in the
   RDF/Semantic Web stack. It started with me wanting a way to tack semi-
   structured metadata to my samples. And then I discovered that unlike
   serving up random JSON name/value pairs, I can use the URLness of an
   RDF attribute to make the metadata attributes globally unique -- which
   makes merging multiple data sources simpler.    E.g. I make a fake
   ontology for the various submitting agency to track the metadata they
   came up with for my samples.    Diane


Posted by Tshepang Lekhonkhobe on 2012-03-07 at 08:39. 

::

   'for a while' links is broken: <a
   href="http://ivory.idyll.org/blog/mar-12/ivory.idyll.org/blog/aug-11
   /cloud-not-the-solution.html">http://ivory.idyll.org/blog/mar-12/ivory
   .idyll.org/blog/aug-11/cloud-not-the-solution.html</a>


Posted by Titus Brown on 2012-03-07 at 10:34. 

::

   Tshepang -- thanks, fixed!  Diane, awesome comment...


Posted by Mick Watson on 2012-03-07 at 10:44. 

::

   I do wonder whether there is just a bit too much hand wringing about
   "big data".    For e.g., the rumen metagenomic data you mentioned
   above, I can assemble using MetaVelvet on our server in less than a
   day (admittedly it has 512Gb of RAM, but doesn't everyone?).  I can
   count the 17mers in it using Jellyfish in a few hours.    So I just
   set the processes running, two days later, I have my analysis.  What's
   the problem?  Does it matter that you can do it quicker?      Big data
   doesn't really worry me.      We're generating lots of metagenomic
   data of a similar size to the rumen data, but that's part of a 2 year
   project, so we'll just crank it through the server and still have
   plenty of time to spare.    What happens if we get a "V4" HiSeq
   upgrade that gives us 10x the data again?  Well, I could just go and
   use a 6Tb RAM machine down in Norwich (http://www.tgac.ac.uk/news/6/68
   /Record-breaking-data-centre-for-genome-sequencing-opened-in-Norwich/)
   I know I am being flippant, but really to me the challenge isn't the
   data, it's the biology.  I don't care if it takes 2 hours, 2 days or 2
   weeks to process the data.      Improve your computing efficiency by
   100x, I don't care; improve your ability to extract biological
   information by 100x, then I'm interested :)


Posted by steve williams on 2012-03-07 at 14:28. 

::

   how many sequential passes occur through the data copying it hither
   and yon before you copy it into ram so you can do a sequential pass
   through the data? if only those copy processes had a little bit of
   intelligence. . .


Posted by Fabien Campagne on 2012-03-08 at 20:57. 

::

   Very good points. I can't help but wonder at the gap between the skill
   set needed to solve these problems rigorously and the typical
   backgrounds of bioinformaticians (who often come from various
   backgrounds, but rarely from computer science). I personally trained
   in chemistry, and appreciate the challenges in learning three new
   fields at once (CS, stats and biology).    Another point would be to
   encourage people interested in reusable software and efficient
   algorithms to collaborate through contributions to open-source
   projects. Using a tool is great, but if you find that a small
   modification can help you push the enveloppe and help you get the job
   done more efficiently, contributing these changes/suggestions back to
   the project will help others benefit as well. I have contributed code
   to several tools over the years (sometimes crossing disciplines, e.g.,
   contributions to MG4J), or just reported bugs (often with patches, so
   it is easier on the busy developer) and found the process most
   rewarding (at both the intellectual and personal level). Since
   collaborations on software works well by email and electronic
   communication, it is easier to assemble like-minded team members with
   complementary expertise across academia and/or industry.


Posted by Jan Strube on 2012-03-09 at 00:12. 

::

   Hi Titus,    This problem is something the LHC experiments are
   intricately familiar with. The data rates are far too large to store
   everything on disk, so we have rather involved trigger systems that
   disregard everything that looks like like garbage. Even something
   we've already measured in previous experiments several years ago is
   being dropped if it occurs at too high a rate.


Posted by Titus Brown on 2012-03-11 at 22:39. 

::

   Jan, Fabien -- very good points, and I'm pushing in all those
   directions :).

