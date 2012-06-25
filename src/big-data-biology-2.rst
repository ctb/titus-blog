Big Data Biology - why efficiency matters
#########################################

:author: C\. Titus Brown
:tags: ngs,python,diginorm
:date: 2012-04-06
:slug: big-data-biology-2
:category: science


I'm going to pick on Mick Watson today.  (It's OK.  He's just a foil for
this discussion, and I hope he doesn't take it too personally.)

Mick made the following comment on my earlier `Big Data Biology blog post <http://ivory.idyll.org/blog/mar-12/big-data-biology>`__:

   I do wonder whether there is just a bit too much hand wringing
   about "big data".

   For e.g., the rumen metagenomic data you mentioned above, I can
   assemble using MetaVelvet on our server in less than a day
   (admittedly it has 512Gb of RAM, but doesn't everyone?).  I can
   count the 17mers in it using Jellyfish in a few hours.

   So I just set the processes running, two days later, I have my
   analysis.  What's the problem?  Does it matter that you can do it
   quicker?


   Big data doesn't really worry me.  

   ...

   I know I am being flippant, but really to me the challenge isn't
   the data, it's the biology.  I don't care if it takes 2 hours, 2
   days or 2 weeks to process the data.

   Improve your computing efficiency by 100x, I don't care; improve
   your ability to extract biological information by 100x, then I'm
   interested :)

He makes one very, very, very good point -- who cares if you can run
an analysis (whatever it is) and it doesn't provide any value?  The
end goal of *my* sequencing analysis is to provide insight into
biological processes; I might as well just delete the data (an O(1)
"analysis" operation, if one with a big constant in front of it..)  if
the analysis isn't going to yield useful information.

But he also seems to think that speed and efficiency of analyses
doesn't matter for science.  And I don't just *think* he's dead wrong,
I *know* he's dead wrong.

This is both an academic point and a practical point.  And, in fact,
an algorithmic point.

The academic reason why efficient computation is good for science
-----------------------------------------------------------------

The academic point is simple: our ability to do thorough exploratory
analysis of a large sequencing data set is limited by at least four
things.  These four things are:

  1. Our ability to do initial processing on the data - error trimming
     and correction, and data summary (mapping and assembly, basically).

  2. The information available for cross-reference.  Most (99.9%) of
     our bioinformatic analyses rely on homology (for inference of
     function) and annotation.

     (This is why Open Access of data is so freakin' important to us
     bioinformaticians.  If you hide your database from us, it might
     as well not exist for all we care.)

  3. Statistics.  We do a lot of sensitive signal analysis and
     multiple testing, and we are really quite bad at computing FDRs
     and other statistical properties.  Each statistical advance is
     greeted with joy.

  4. The ability to complete computations on (1), (2), and (3).

Every 100gb data set takes a day to process.  Mapping and assembly can
take hours to days to weeks.  Each database search costs time and
effort (in part because the annotations are all in different formats).
Each MCMC simulation or background calculation takes significant time,
even if it's automated.

**Inefficient computation thus translates to an economic penalty on
science (in time, effort, and attention span).** This, in turn, leads
directly to science that is not as good as it could be (as do `poor
computational science skills
<http://ivory.idyll.org/blog/jun-11/ngs-2011>`__, `badly written
software
<http://ivory.idyll.org/blog/jan-12/top-ten-things-i-hate-about-bioinfo-software>`__,
`inflexible workflows
<http://ivory.idyll.org/blog/dec-11/data-intensive-science-and-workflows>`__,
`opaque pipelines
<http://ivory.idyll.org/blog/dec-11/four-reasons-i-wont-use-your-data-analysis-pipeline>`__,
and `too quick a rush to hypotheses
<http://ivory.idyll.org/blog/dec-11/is-discovery-science-really-bogus>`__
-- hey, look, a central theme to my blog posts!)

Anecdote: someone recently e-mailed us to tell us about how they could
assemble a comparable soil data set to ours in a mere week and 3 TB of
memory.  Our internal estimates suggest that for full sensitivity, we
need to do 5-10 assemblies of that data set (each with different
parameters) followed by a similarly expensive post-assembly merging --
so, minimally, 6 weeks of compute requiring 3 TB of memory, full-time,
on as many cores as possible.  You've gotta imagine that there's going
to be a lot of internal pressure to get results in less time (surely
we can get away with only 1 assembly?) with less parameter searching
(what, you think we can tell you which parameters are going to work?)
and this pressure is going to translate to doing less in the way of
data set exploration.  (Never mind the *actual* economics -- since
this data set would take about 1 week of sequencer time, and $10,000
or so, to generate today, I think they don't make sense either.)

I can point you to at least three big metagenome Illumina assembly
papers where I *know* these computational limitations truncated their
exploration of the data set.  (Wait, you say there are only three?
Well, I'm not going to tell you which three they are.)

The practical reason why efficient computation is good for science
------------------------------------------------------------------

This one's a bit more obvious, but, interestingly, Mick *also* treads
all over it.  He says "...I can assemble using MetaVelvet on our server
in less than a day (admittedly it has 512 Gb of RAM, but doesn't everyone?"

Well, no, they don't.

*We* didn't have access to such a big server until recently.  We had plenty
of offers for occasional access, but when we explained that we needed them
for a few weeks of dedicated compute (for parameter exploration -- see above)
and also that no, we weren't willing to sign copyright or license for our
software over to a national lab for that access, somewhat oddly a lot of
the offers came to naught.

It turns out *most* people don't have access to such bigmem computers, or
even big compute clusters; and when they do, those computers and clusters
aren't configured for biologists to use.

Democratization of sequencing should mean democratization of analysis,
too.  Every year `our next-gen sequence analysis course
<http://ivory.idyll.org/blog/mar-12/ngs-course-where-next.html>`__
gets tons of applicants from small colleges and universities where the
compute infrastructure is small and what does exist is overwhelmed by
Monte Carlo calculations.  Our course explicitly teaches them to use
Amazon to do their compute -- with that, they can take that knowledge
home, and spend small amounts of money to buy IaaS, or apply for an
AWS education grant to do their analysis.  We feel for them because
we were *in* their situation until recently.

**Expensive compute translates to a penalty on the very ability of
many scientists and teachers to access computational science.**
*(Insert snide comment on similar limitations in practical access to
US education, health care, and justice).*

The algorithmic reason why efficient computation is good for science
--------------------------------------------------------------------

Assemblers kinda suck.  Everyone knows it, and recent contests &
papers have done a pretty good job of highlighting the limitations
(see `GAGE <http://gage.cbcb.umd.edu/index.html>`__ and `Assemblathon
<http://assemblathon.org/>`__).  This is not because the field is full
of stupid people, but rather because assembly is a really, really hard
problem (see `Nagarajan & Pop
<http://trinity.engr.uconn.edu/~vamsik/Fragment%20Assembly/NagarajanPopJCB09.pdf>`__)
-- so hard that really smart people have worked for decades on it.
(In many ways, the fact that it works at all is a tribute to their
brilliance.)

Advances in assembly algorithms have led to our current crop of
assemblers, but assemblers are still relatively slow and relatively
memory consumptive.  Our `diginorm paper <http://ivory.idyll.org/blog/apr-12/what-is-diginorm.html>`__ benchmarks Trinity as
requiring 38 hours in 42gb of RAM for 100m mouse mRNAseq reads; genome
and metagenome assemblers require similar size resources, although the
variance depends on the sample, of course.  `SGA
<http://www.ncbi.nlm.nih.gov/pubmed?term=22156294>`__ and `Cortex
<http://www.ncbi.nlm.nih.gov/pubmed?term=22231483>`__ seem
unreasonably memory efficient to me :), but I understand that they perform
less well on things other than single genomes (like, say, metagenomic
data) -- in part because the underlying data structures are
targeted at specific features of their data.

What's the plan for the future, in which we will be applying next-gen
sequencing to non-model organisms, evolutionary experiments, and
entire populations of novel critters?  These sequencing data sets will
have different features from the ones we are used to tackling with
current tech -- including higher heterozygosity and strong GC-rich
biases.

I personally think the next big advances in assembly will come through
the systematic application of sample- or sub-sample specific,
compute-expensive algorithms like `EMIRGE
<http://www.ncbi.nlm.nih.gov/pubmed?term=21595876>`__ to our data
sets.  While perfect assembly may be a pipe dream, significant and
useful incremental advances seem very achievable, especially if the
practical cost of current assembly algorithms drops.

Not so parenthetically, this is one of the reasons I'm so excited
about `digital normalization <http://ivory.idyll.org/blog/apr-12/what-is-diginorm.html>`__ (the general concept, not only our
implementation) --

I bet more algorithmically expensive solutions would be investigated,
implemented, and applied if memory and time requirements dropped,
don't you?

Or if the data could be made less error-prone and simpler?

Or if the volume of data could be reduced without losing much
information?

I will take one side of that bet...

---

Of course, I'm more than a wee bit biased on this whole topic.  A big
focus of my group has been in spending the last three years fighting
the trend of "just use a bigger computer and it will all be OK".
`Diginorm <http://ivory.idyll.org/blog/mar-12/diginorm-paper-posted.html>`__ and `partitioning <http://ivory.idyll.org/blog/dec-11/kmer-percolation-posted.html>`__ are two of the results, and a
few more will be emerging soon.  I happen to think it's incredibly
important; I would have done something else with my time, energy,
and money if not.  Hopefully you can agree that it's important, even
if you're interested in other things.

So: yes, computational efficiency is not the only thing.  And it's a
surprisingly convenient moving target; frequently, you yourself can
just wait a few months or buy a bigger computer, and achieve similar
results.  But sometimes that attitude masks the fact that efficient
computation can bring better, cheaper, and broader science.  We need
to pay attention to that, too.

And, Mick?  I don't think I can improve your ability to extract
biological information by 100x.  On metagenomes, would 2-10x be a good
enough start?

--titus


----

**Legacy Comments**


Posted by Deepak Singh on 2012-04-06 at 10:49. 

::

   Ever since I was a grad student, I have always been unhappy about two
   things in scientific research    1. Job queues  2. A lack of
   appreciation of the importance of efficient computing    Later on, as
   I had to deal with a lot of academic code, this only got amplified.
   My conclusions for why    - Labor is cheap.  Grad student time is not
   valued.  It's perfectly acceptable to have computation run longer and
   inefficiently.  - The end goal is the paper, and not the long term, so
   code is always written with those insights.    My very biased $0.02


Posted by Mick Watson on 2012-04-10 at 05:07. 

::

   I can't believe you posted this on a bank holiday weekend.  I was on
   holiday, and had to wait days to respond!    Well, I guess this serves
   me right for writing a flippant post on your blog ;)    I stand by my
   major point:  there is too much hand-wringing about "big data" in
   biology.  In my first job we worried about GenBank being too big; in
   my second job, downloading the human trace archive caused problems as
   our ISP cut-off the connection before we were finished; in my last
   job, I sat in a room with a well-known biologist as he told everyone
   that MAGE-ML would be too big and would break the internet.  I'm
   really glad there are smart people out there worrying about "big
   data", but my experience tells me it's always been a problem, and we
   have always solved it.  It looks to me like you're one of those smart
   people interested in solving those problems, which is great :)
   Just as your focus has been 'fighting the trend of "just use a bigger
   computer and it will all be OK"', what I want to promote is that we we
   put the "bio" back in "BIOinformatics", and the biology back in
   "computational BIOLOGY".  Please understand that I'm not aiming this
   at you;  I'm aiming this at the possibly 1000s of young
   bioinformaticians who might be reading your blog.  If you've done
   nothing but write java code for the last 3 years, well, I'd encourage
   you to stop.  Test a hypothesis.  Push back some biological
   boundaries, rather then technical boundaries.  Try it, it's fun :)
   Clearly, we need scientists who push back both technical and
   biological boundaries;  You make very good points above, and you
   clearly are someone who wants to do both, which is fantastic.  Your
   research is clearly relevant and innovative.  It should be published
   and funded (subject to rigorous peer-review of course).  And if
   getting from A to B 100x quicker enables you to get to C, I
   congratulate you for it.  But not everyone is you.  Somewhere, out
   there, is a PhD student writing a new short-read aligner in the hope
   of making it faster than Bowtie; in a different lab is a post-doc
   writing yet another De Bruijn graph assembler hoping to make it
   quicker than SOAPdenovo, or ABySS.  In my opinion, as a branch of
   biology, bioinformatics does not concentrate enough on the "bio" :)
   And finally: can you make good on that promise of 2-10x better
   metagenomic assemblies?


Posted by Titus Brown on 2012-04-10 at 09:46. 

::

   Thanks, Mick!  A very good counterpoint.    I think some (many?) of
   the boundaries that need pushing will require better (=&gt; more
   relevant) bioinformatics, as well as good (=&gt; high quality, deep,
   etc.) biology.    And I'm pretty sure we can make good on the 2-10x
   better metagenomic assemblies, but you're going to have to wait a bit
   for us to prove it to you... we have lots of circumstantial evidence
   but are still pulling it together for pub!

