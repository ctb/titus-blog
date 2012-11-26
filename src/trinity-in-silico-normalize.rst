What does Trinity's In Silico normalization do?
###############################################

:author: C\. Titus Brown
:tags: science,diginorm,khmer,assembly
:date: 2012-11-26
:slug: trinity-in-silico-normalize
:category: science
:status: draft

For a few months, the Trinity list was awash with discussions about
how to use `digital normalization
<http://ivory.idyll.org/blog/what-is-diginorm.html>`__ to lower the
memory and compute requirements for mRNASeq assembly.  At some point a
Trinity developer contacted me and said that they were going to
provide their own in silico normalization approach as part of Trinity,
because their benchmarks showed that diginorm as implemented in khmer
didn't work too well with Trinity.  The Trinity approach has since
emerged `here
<http://trinityrnaseq.sourceforge.net/trinity_insilico_normalization.html>`__,

The observation that diginorm performed as a prefilter for Trinity
concerned me, obviously, because we have `a preprint
<http://arxiv.org/abs/1203.4802>`__ saying that it works quite well
:).  I couldn't get enough specifics for me to replicate their bad
results with diginorm, and they seemed happy to go their own route, so
I left it there, provisionally.

At the time, I took a quick look at their normalization approach and
couldn't quite figure out precisely what it would do, but also couldn't
take the time to understand it in depth.  That was a few months ago,
and the issue has been a persistent itch in the back of my mind since
then, but I finally got around to banging on it today.  Below are the
results.

The Trinity in silico normalization algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The master script, ``util/normalize_by_kmer_coverage.pl``, masterminds
the conversion of FASTQ to FASTA and sets various parameters.  The
parameters of interest used below are a k-mer size K of 25 and a
default coverage C of 20.

Briefly, ``util/normalize_by_kmer_coverage.pl`` converts everything to
FASTA and runs Jellyfish, a ridiculously fast k-mer counter, on all
the files.  Jellyfish reads in all the FASTA sequences and outputs a
file ``normalized_reads/jellyfish.25.kmers.fa`` containing each
25-mer and its count.

Then, ``fastaToKmerCoverageStats`` (source:
``Inchworm/src/fastaToKmerCoverageStats.cpp``)

- loads in all of the k-mer counts from the k-mer FASTA file, ``normalized_reads/jellyfish.25.kmers.fa``.

- for each read, computes the median, average, stdev, and percentage stdev, and outputs them to ``<seqfile>.K25.stats``.

Next, ``util/nbkc_normalize.pl`` goes through each of the
``<seqfile>.K25.stats`` files and, after some error analysis, checks to
see if a random number between 0 and 1 (excluding 1) matches is less
than the ratio of the desired coverage and the median coverage.  If it
is, the sequence name is output to a file
``<seqfile>.C20.pctSD100.accs``.

See ``util/nbkc_normalize.pl``, line 26, for the decision point::

        if (rand(1) <= $max_cov/$med_cov) {
            print "$core_acc\n";
        }

To see how this if statement works out, consider:

If the desired coverage is 20, and the median coverage is 10,
the ratio is greater than 2 and the read is always kept.

If the desired coverage is 20, and the median coverage is 40,
the ratio is 0.5 and the read is kept roughly half the time.

Finally, the function ``make_normalized_reads_file`` in
``util/normalize_by_kmer_coverage.pl`` loads in all the names in each
``<seqfile>.C20.pctSD100.accs`` file into an index and then goes
through each ``<seqfile>`` and extracts the kept sequences into a
final ``<seqfile>>.normalized_K25_C20_pctSD100.fa`` file.

This last file is then assembled.

A few basic observations
~~~~~~~~~~~~~~~~~~~~~~~~

Assuming your file is in FASTA format to begin with, this algorithm
reads each sequence 4 times: once for Jellyfish, once for
fastaToKmerCoverageStats, once for nbkc_normalize (since each sequence
has a stat line), and once again to make the final normalized reads
file.  Each 25-mer in the data set is also written and read once, and
as there are generally more total k-mers than total sequences, this
algorithm's runtime scales with a factor of approximately 5 times the
input data set size.

In terms of memory usage, Jellyfish and Inchworm (the first two steps)
both count all k-mers (although it looks like there is an option to
discount k-mers that only show up once -- I think this must only apply
to the fastaToKmerCoverageStats step, not the original Jellyfish
step).  Thus the memory requirements for Trinity's in silico
normalization scales with the number of distinct k-mers in the data
set -- again, this can be quite large.

What happens when you run it on simulated data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From the diginorm paper, I have a convenient simulated test data set
for exploring normalization approaches.  The data set is described in
the `diginorm paper <http://arxiv.org/abs/1203.4802>`__; basically
it's just a bunch of reads simulated from short transcripts across
three different orders of magnitude (see `make-random-transcriptome
<https://github.com/ged-lab/2012-paper-diginorm/blob/master/pipeline/make-random-transcriptome.py>`__
and `make-biased-reads
<https://github.com/ged-lab/2012-paper-diginorm/blob/master/pipeline/make-biased-reads.py>`__).

I generated the simulated data, and then ran diginorm (k=25, C=20) and
Trinity norm (k=25, C=20).

I started with 1m reads; diginorm kept 91,029, while Trinity norm kept
13,245.

I assayed a few different metrics on these files.

First, I asked how many total k-mers were left in each data set.  This is
an estimate of the amount of memory needed to assemble the data with a
de Bruijn graph assembler::

   Unnormalized data: 3,163,778 total k-mers
   diginorm normalization: 1,976,319 total k-mers remaining
   Trinity normalization: 190,815 total k-mers remaining

Next, I plotted k-mer abundance histograms; a closeup of the comparison
is shown in Figure 1.

.. figure:: ../static/images/normhistzoom.png
   :width: 500px

   Fig 1. k-mer abundance plots of raw and normalized data.

The main takeaway here is that both diginorm and Trinity norm are
shifting the k-mer abundance plot as they're supposed to, and making
it "normal".  Diginorm is underestimating the k-mer coverage (hence
the green curve is not centered on 20) while Trinity is bang on --
this is due to the retention of more erroneous sequences by diginorm,
I think.

Third, I looked at how many "true" k-mers were lost; since this is
simulated data, I know exactly what should be there. ::

   Missing 96.0 true k-mers in the sequence reads
   Missing 103.0 true k-mers in the diginorm reads
   Missing 363.0 true k-mers in the Trinity norm reads

Due to random sequence sampling, errors, and low coverage of some
transcripts, we're missing 96 k-mers of 47,600 in the raw reads --
these are completely unrecoverable by assembly, of course!

But what do the filters do?

Diginorm drops an additional 7 k-mers, and Trinity normalization drops
267 k-mers.  This isn't bad -- 267 looks a lot larger than 7, but it's
still only 0.6% of the total k-mers.

From this little study, we can see that Trinity normalization decreases
the total number of k-mers by 94% as opposed to only 38% by diginorm;
and Trinity normalization discards about 98% of the reads, as opposed
to only 90% by diginorm.  In exchange, Trinity discards about 40 times
as many true k-mers as diginorm, or 0.6% of the recoverable k-mers
(Trinity) vs 0.01% of the recoverable k-mers (diginorm).  Not too shabby!

Reproducing it with khmer.
~~~~~~~~~~~~~~~~~~~~~~~~~~

`khmer <https://github.com/ged-lab/khmer>`__ conveniently provides me
with all I need to reimplement Trinity's basic normalization
algorithm.  So `I did <https://github.com/ctb/khmer/blob/trinity/sandbox/filter-median.py>`__, implementing the removal of sequences
via the median count across the entire data set -- basically a
conversion of the diginorm algorithm into a non-streaming algorithm --
with this code:: 

      med, avg, dev = ht.get_median_count(seq)
      if random.randint(1, med) > args.coverage:
            # discard sequence
      else:
            # else, keep sequence

The results kinda sucked -- I kept about 87k sequences as compared to 91k
with diginorm, and 13k with Trinity.  Huh?

Whoops.

Turns out the Trinity normalization procedure has *another* important
if statement -- see ``util/nbkc_normalize.pl``, line 15::

        if ($pct_dev > $max_pct_stdev) { next; } # discard sequence

Here, the per-read pct_dev is defined as the deviation in k-mer
coverage divided by the average k-mer coverage, times 100 (to make it
a percent).  If the deviation is high, that indicates that the read is
likely to contain many errors, since high-coverage reads with
low-coverage k-mers shouldn't happen.  Trinity sets a cutoff of 100:
if the deviation is as big as the average, the read should go away

Sure enough, when I implement that in khmer::

        med, avg, dev = ht.get_median_count(seq)
        pct = dev / avg * 100

        if random.randint(1, med) > args.coverage or pct > 100:
            return None, None

I keep approximately 13k reads -- pretty much what I get with
the Trinity normalization script.

You can see the final two scripts here: `filter-median.py
<https://github.com/ctb/khmer/blob/trinity/sandbox/filter-median.py>`__
and `filter-median-and-pct.py
<https://github.com/ctb/khmer/blob/trinity/sandbox/filter-median-and-pct.py>`__.

Can I make it more efficient?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Trinity implementation goes over the data 5x, while my
implementation goes over the data twice (the minimum needed by the
approach).  Both read in all the k-mers in order to count them,
which balloons the required memory horrendously.  Is there a way to
get back to the streaming goodness of diginorm, which looks at each
sequence only once?

It turns out there is, at least approximately.  The following code does the trick::

                med, avg, dev = ht.get_median_count(seq)

                pct = 0.
                if avg:
                    pct = dev / avg * 100

                if med < DESIRED_COVERAGE and pct < 100:
                    ht.consume(seq)
                    passed_filter = True

Here, 'get_median_count' is counting the k-mers in the sequence only
in the context of the k-mers already seen, not all of the k-mers in
the data set -- that is, this is an **online** implementation of
the algorithm that only looks at each piece of data once.  Only once a
sequence passes the criterion are its k-mers deemed worthy of
being counted.

Note that we can only do this because shotgun sequencing reads are
essentially in random order; because this is true, the above is an
approximation of the random choice made in the previous scripts
(modulo the choice of pct deviation cutoff, which I haven't thought
about).  I followed this same logic chain in making the original
digital normalization a streaming algorithm :).

This new extra-efficient streaming approach (implemented in
`normalize-by-median-pct.py
<https://github.com/ctb/khmer/blob/trinity/sandbox/normalize-by-median-pct.py>`__)
keeps a total of 17,889 reads (as compared to 13,245 from Trinity) and
279,672 k-mers (as compared to 190,815 from the Trinity normalization
procedure).  The extra reads and k-mers kept seem to be the price we
pay for converting the algorithm from 2-pass to a streaming algorithm.
In partial repayment we lose only 162 "real" k-mers in our streaming
approach, as compared to 267 k-mers in the Trinity multipass approach.

it may be possible to tweak the parameters to get better agreement
with Trinity, but I would argue that the improvement is already
dramatic enough.  Unlike the original algorithm, this one looks at
each read once, and consumes far less memory than the original
algorithm, because most k-mers are never counted.  The positive impact
of this on runtime and memory is substantial (see `the diginorm paper
<http://arxiv.org/abs/1203.4802>`__).

Conclusions
~~~~~~~~~~~

First, I understand the Trinity normalization algorithm well
enough to reproduce it in a completely different language and software
stack.  Yay!

Second, I can convert the Trinity multipass algorithm into a streaming
online single-pass algorithm, with substantial decrease in running
time, disk access -- the streaming algorithm is entirely in-memory --
and total memory required.  Combine this with khmer's general memory
efficiency and it's a big win overall. (Spoiler alert: we can count
k-mers about 5-10x more memory efficiently than Jellyfish.)

I don't see any easy way that Trinity can incorporate this into their
script-based workflow -- they'd have to hook into Jellyfish's library
code -- but it would probably be worth it.

Third, I now understand why the Trinity algorithm discards so much
more data than digital normalization: it uses a pretty hard-core
heuristic guess about what relative k-mer abundances within a read
should look like, and discards reads that look bad.  We are already
doing this with diginorm implicitly by using the median, but this is
way more stringent.  I'm still not sure how much this added stringency
will matter for things like sensitivity to splice junctions.  That,
however, is something I'll leave for future inquiry... because I'm
done for tonight ;).

Over and out!

--titus

p.s. You can see some of the ancillary changes I made to the diginorm
pipeline for this blog post `here
<https://github.com/ctb/2012-paper-diginorm/commit/94ba2c1f8bda2e779285bfc47c6d5d0a08acbad5>`__;
note especially `the IPython Notebook calculations
<http://nbviewer.ipython.org/urls/raw.github.com/ctb/2012-paper-diginorm/trinity/pipeline/abundance-hists.ipynb>`__.
Drop me a note or ask in comments if you want to play with it
yourself.

p.p.s. If the Trinity team implements this, I expect them to cite this blog post :).  I'll `even provide a figshare DOI for them... <http://ivory.idyll.org/blog/posting-blog-entries-to-figshare.html>`__