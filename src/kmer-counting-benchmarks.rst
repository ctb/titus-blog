Counting k-mers on EC2 - huh?
#############################

:author: C\. Titus Brown
:tags: python,ngs,khmer,wtf
:date: 2013-07-03
:slug: kmer-counting-benchmarks
:category: science

(This blog post was mightily helped by Qingpeng Zhang, the first
author of the paper; he wrote the pipeline.  I just ran it a bunch :)

We have been benchmarking k-mer counters in a variety of ways, in
preparation for an upcoming paper.  As with `the diginorm paper
<http://ivory.idyll.org/blog/replication-i.html>`__ we are automating
everything, so I thought heck, why not try running it on a bunch of
different EC2 machines to see how variable their performance is?
Then, I ruined that idea by varying the machine configuration instead of
using identical machines :).

The overall pipeline takes about 30 hours to run, and for this blog
post I am focusing in on one particular benchmark -- the length of
time it takes the various programs to generate and count the
abundance distribution of the 22-mers present in 48.7 m short
reads, or about 5 GB of data.  We used `Jellyfish <http://www.cbcb.umd.edu/software/jellyfish/>`__, `DSK <http://bioinformatics.oxfordjournals.org/content/early/2013/01/16/bioinformatics.btt020>`__, `khmer <http://khmer.readthedocs.org/en/latest/>`__, and `Tallymer <http://www.zbh.uni-hamburg.de/?id=211>`__; we're planning to try out KMC, also, but didn't get to it for this post.

I ran the counting four machines: our local server, which is your
standard reasonably high performance Linux box; two m2.2xlarge Amazon
EC2 instances (34 GB RAM), one with the default setup and one with a 1
TB EBS disk with 100 IOPS configuration; and an m2.4xlarge Amazon EC2
instance, with 68 GB RAM.  I chose different zones for all three EC2
machines.  The max memory required was about 24 GB, I think.

I analyzed everything within an IPython Notebook, which is available
`here
<http://nbviewer.ipython.org/urls/raw.github.com/ged-lab/2013-khmer-counting/master/notebook/khmer-counting-compare.ipynb>`__.
If you want to play with the data, grab the master branch of
https://github.com/ged-lab/2013-khmer-counting.git, go to the
notebooks/ subdirectory, run the ipython notebook server, and open the
'khmer-counting-compare' notebook.  All the data necessary to run the
notebook is there.

The results are a bit weird!

First, let's look at the overall walltime it took to count (Figure 1).
Jellyfish did a really nice job, outperforming everything else handily.
Tallymer (the oldest of the programs) was by far the slowest; DSK and
khmer were in the middle, depending on machine configuration.

.. figure:: ../static/images/khmer-benchmarks/time.png
   :width: 500px
   :alt: walltime graph

   Fig 1. The time (in seconds) to count the k-mers and generate a
   k-mer abundance histogram for 48.7m short reads from a soil
   metagenome, using several different k-mer counting packages.

A few points about Figure 1 --

1. Why no errorbars? Time is money, baby -- this already cost quite
   enough, thankyouverymuch.

2. Doesn't this mean Jellyfish is just plain better?  Well, read on (this
   and other blog posts).

3. Why did everything perform worse on the IOPS configured EC2 instance?
   Heck if I know.  Note that khmer has the *least* disk access of
   anything, which suggests that disk performance just downright sucked
   on the IOPS instance.

----

Now let's take a look at how efficiently the programs were using compute.
Figure 2 shows the ratio of user time (which is approximately seconds
spent by each core, summed, minus time spent in the OS critical sections)
to walltime (how long the whole process took).

.. figure:: ../static/images/khmer-benchmarks/usertime_ratio.png
   :width: 500px
   :alt: usertime ratio graph

   Fig 2. The ratio of user time (seconds x cores, omitting system
   time) to walltime (seconds) when generating the k-mer abundance
   histogram for 48.7m reads.  Note that Jellyfish and khmer were both
   run with 8 threads, while Tallymer is unthreaded and DSK was run
   with 1 thread by mistake.

A few points about figure 2:

4. Wowsers! We ran both Jellyfish (red) and khmer (blue) with 8
   threads, and the results suggest that they both used them very
   efficiently on our own server -- a factor of about 8 suggests that
   they were merrily blasting along doing computing, hindered little
   if at all by disk access!  Since our local server has great I/O (I
   guess?), that probably accounts for it.  Note: I think this also
   means our locking and multithreading implementations are really
   good (read `this
   <http://ivory.idyll.org/blog/multithreaded-read-parsing-in-khmer.html>`__
   and `this <http://arxiv.org/abs/1303.2223>`__ for more information;
   this is a general threaded API for sequence reading, hint hint).

5. DSK and Tallymer both did a poor job of using multiple CPUs.  Well, to
   be fair, Tallymer doesn't support threads.  And while DSK does, we forgot
   to run it with 8 threads.  Oops.  Betcha performance increases!

6. If I/O is what matters here, m2.4xlarge has what appears to be the
   next best I/O -- khmer got up to a ratio of 7.09.  Even on the
   IOPS system, khmer did OK.

   In general, I think these benchmarks show that I/O is the Achilles
   heel of the various k-mer counting systems.  I don't know why the
   IOPS configuration would be worse for that, though.

----

Finally, let's look at system time.  Figure 3 shows total system time
(in seconds) for each program/machine configuration.  System time includes
all disk access, but not, I think, cache invalidation or other things
like that.

.. figure:: ../static/images/khmer-benchmarks/system_time.png
   :width: 500px
   :alt: system time graph

   Fig 3. System time (primarily disk access) for generating the
   k-mer abundance histogram for 48.7m reads.

Thoughts:

7. This more or less confirms what we inferred from the other graphs:
   I/O is a bottleneck.  Jellyfish, for whatever reason, disagrees with
   that statement, so they must be doing something clever :)

----

Some concluding thoughts for this initial blog post --

8. Don't go around claiming that one k-mer counter is better, based
   on this!  We omitted at least one good lookin' published k-mer
   counter (`KMC <http://www.biomedcentral.com/1471-2105/14/160>`__)
   and may go take a look at `BFCounter
   <http://www.biomedcentral.com/1471-2105/12/333>`__ and `Turtle
   <http://arxiv.org/abs/1305.1861>`__ too.  Plus, we screwed up
   our DSK benchmarking.

9. Note we've said nothing about memory or disk usage here.  Indeed.

10. At the end of the day, I don't understand what's going on with the
    IOPS-optimized EBS instances.  Did I choose too low a number? (100 IOPS).
    Did I pick too big a hard drive? Is our access pattern lousy? Or what?

    Note that `this post from Garantia Data <http://garantiadata.com/blog/is-amazon-piops-really-better-than-standard-ebs#.UdTGzTGWXAA>`__
    ended up with similar questions :).

    Here, I think there are probably a variety of access patterns, but
    the basic thing that's going on is (a) reading a steady stream of
    data sequentially, and (b) for most of the programs, writing stuff
    to disk steadily.  (khmer does not do any disk access beyond reading
    in the sequence file here.)

----

Anyway, that's the first of what will probably be several blog posts on
k-mer counting performance.  This is a real data set, and a real set of
well-used programs, so I think it's a pretty good benchmark; let me know
if you disagree and want to see something else...

--titus
