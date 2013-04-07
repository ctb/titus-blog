Multithreaded read parsing coming to khmer
##########################################

:author: C\. Titus Brown
:tags: science
:date: 2013-04-06
:slug: multithreaded-read-parsing-in-khmer
:category: science

Is khmer evolving?

The `khmer project <http://khmer.readthedocs.org>`__ is our software
package to work with short reads, and it enables a lot of things like
k-mer counting and de Bruijn graph exploration and modification.  As
data volume grows, interest in `partitioning <@@>`__ and `digital
normalization <@@>`__ is also growing.  But we haven't really talked
much about new features in khmer.

So, you might wonder, is the project stagnant?  The answer: No.

As `more and more people start to use khmer
<http://biomickwatson.wordpress.com/2013/03/14/shouting-at-my-data-in-the-cloud/>`__,
we are faced with the question of whether or not to improve it
incrementally, or to `shoot for the moon
<http://www.wired.com/opinion/2013/02/moonshots-matter-heres-how-to-make-them-happen/>`__.
These are not entirely orthogonal, but my lab doesn't have the
humanpower to help people use khmer, AND fix rough corners, AND
optimize it, AND do research.  While we've been trying to balance
these needs, we've mostly been focusing on our research, 'cause that's
where our incentives are.

But while our research is, indeed, going to be awesome, it doesn't
really help users in the short term.

However, our software engineer, Eric, has been bravely bucking this
trend and working to provide the next set of really cool optimizations.
His latest set of nifty refactoring just hit the `bleeding edge branch
<https://github.com/ged-lab/khmer/tree/bleeding-edge>`__ and it is
truly awesome to behold.

Briefly, Eric has implemented multithreaded read parsing in C++, and
**provided a Python iterator interface to it**.  This is further along
the path of some of his earlier work to make our core data structures
threadsafe, and improve read parsing performance dramatically
(described in some detail in `our chapter on Working with Big Data in
Bioinformatics <http://arxiv.org/abs/1303.2223>`__).  The big thing for
me, to reiterate, is that we now have a Python API to access multithreaded
read parsing!  This makes it quite generally useful, as well as flexible
and usable for prototyping new khmer code.

How does it work?
-----------------

I put together a script to try it out; you can see `the entire
functioning script as a gist on github
<https://gist.github.com/ctb/5328016>`__ if you're interested in
trying it out yourself.

How does it work?  I would argue "as you would expect" :).

Let's suppose you are dealing with a large read data set, and you want
to do some mildly expensive computation on each read.  Below,
I wrote a simple function to simulate a mildly expensive operation
by sleeping for 2 tenths of a second for every 1000 reads, while
adding the read names into a set::

    s = set()

    def read_names(rparser):
        for n, read in enumerate(rparser):
            s.add(read.name)

            if n % 1000 == 0:
                print 'sleeping', n
                time.sleep(0.2)

Now, rather than running this function in a normal serial way, you
note that hey, perhaps you could speed things up by running it in
parallel!  How would you do that?

First, instantiate a ReadParser::

    rparser = khmer.ReadParser(filename, n_threads)

and then ... you're done.  Simply start up that many Python threads,
and use 'read_names' as the target of a threading.Thread. ::

    print 'starting threads'
    threads = []

    # start n_threads threads
    for tnum in xrange(n_threads):
        t = threading.Thread(target=read_names, args=(rparser,))
        threads.append(t)
        t.start()

Then, wait for the threads to exit. ::

    # wait until all threads have exited
    for t in threads:
        t.join()

    print 'done; loaded %s sequences' % len(s)

A not-so-scientific trial shows the basic speedup -- with 1 thread,
'time' reports ::

   real    0m5.191s   <-- 5.2 seconds of walltime
   user    0m0.138s
   sys     0m0.015s

with 2 threads, ::

   real    0m2.789s   <-- 2.8 seconds of wall time
   user    0m0.178s
   sys     0m0.081s

with 4 threads, ::

   real    0m1.794s   <-- 1.8 seconds of walltime
   user    0m1.234s
   sys     0m0.115s

and with 8 threads::

   real    0m1.418s   <-- 1.4 seconds of walltime
   user    0m2.453s
   sys     0m0.074s

----

(Since this is a fairly small set of sequences, and there is overhead
to setting up the threading, the times are not going to be linear with
the number of threads used.  But for larger files and real processing,
Eric's shown that we can get nearly linear speedups of 0.9x for each
thread added.  You can `read the book chapter
<http://arxiv.org/abs/1303.2223>`__ if you want more performance
and design details.)

Also note that Eric has also added paired-end reading, which makes
sure that each thread gets both ends.

Overall, I think this is really exciting.  Eric's put in a lot of work
to make the code threadsafe and to refactor the read parsing code to
have a consistent set of APIs, and it's bearing fruit.  While there is
more work to be done, it's nearing the point where it's going to
simply be the bedrock on which we can drive future optimizations and
scaling.

To get the latest bleeding edge, do ::

   git clone https://github.com/ged-lab/khmer.git -b bleeding-edge

Whither the future?
-------------------

Factoring out this multithreaded read stuff into its own set of
Python- accessible APIs does make it immediately useful to other
programmers.  I'm not sure how far we want to go down the path of
becoming a general library for things like read parsing in Python and
C++, but it should be possible to swipe the code (BSD license!)
for those who are interested in doing so.  We could probably put it
into screed if we wanted... hmmmm....

Also, I should point out that most of the features in khmer master so
far are completely serial -- the only exception is some aspects of
partitioning, 'cause that's so slow.  That means that people using
diginorm on 3 billion reads are doing so in a single thread so far!
Since the diginorm algorithm is single pass, they don't yell at me too
much, but it does take a fair amount of time.  But, good news -- those
people should see significant improvements in speed with the next
version of khmer...

As for the broader future of khmer, it's on hold until we receive good
(or bad) news about funding.  I've got a bunch of students looking to
graduate, a bunch of collaborators who want to finish off their
analyses, and not much money to pursue things like good software
engineering.  Hopefully that will change, and if or when it does, I'll
blog about my thoughts on the future of khmer.

--titus
