How good is MEGAHIT?
####################

A few weeks back, Nick Loman (via Manoj Samanta) brought MEGAHIT to
our attention via `Twitter
<https://twitter.com/pathogenomenick/status/515390848230760448>`__.
MEGAHIT promised to be "an ultra-fast single-node solution for large
and complex metagenome assembly" and they provided a `a preprint
<http://arxiv.org/abs/1409.7208>`__ and some `open source software
<https://github.com/voutcn/megahit>`__.  This is a topic near and dear
to my heart (see `Pell et
al. <http://www.ncbi.nlm.nih.gov/pubmed/22847406>`__ and `Howe et al.,
2014 <http://www.ncbi.nlm.nih.gov/pubmed/24632729>`__), so I was
immediately interested - especially since the paper used our Howe et
al.  data set to prove out their results.  The twitterati also pointed
out that the preprint engaged in some bashing of this previous work,
presumably to egg me on.

So I thought, heck! Let's take it for a spin!  So my postdoc Sherine
Awad and I tried it out.

tl; dr? MEGAHIT seems pretty awesome to me, although IDBA and SPADes
seem to have it beat by a bit.

We ran into some `small compilation problems
<https://github.com/voutcn/megahit/pull/2>`__ but got it working on an
Ubuntu 12.04 system easily enough.

Running it was also a snap.  It took a few minutes to work through the
required options, and voila, we got it running and producing results.
(You can see some example command lines `here
<https://github.com/ctb/2014-megahit-evaluation/blob/master/Makefile>`__.)

First question -- 

How does it do on E. coli?
--------------------------

One of the claims made in the paper is that this approach performs
well on low-coverage data.  To evaluate this, I took a 5m read subset
from the E. coli MG1655 dataset (see `Chitsaz et al., 2011
<http://www.ncbi.nlm.nih.gov/pubmed/21926975>`__) and further
subsetted it to 1m reads and 500k reads, to get (roughly) 100x, 20x,
and 10x data sets.  I then ran MEGAHIT with default parameters,
specifying 1 GB of memory, and limiting only the upper k size used
(because otherwise it crashed) -- again, `see the Makefile
<https://github.com/ctb/2014-megahit-evaluation/blob/master/Makefile>`__.

After it was done assembling, I ran QUAST on the results.

======================    =======      ======     ======
Measure                   100x         20x        10x
======================    =======      ======     ======
N50                       73736        52352      9067
Largest alignment         221k         177k       31k
bp in contigs > 1kb       4.5mb        4.5mb      4.46mb
Genome fraction           98.0%        98.0%      97.4%
Misassembled length       2kb          40.8kb     81.3kb
======================    =======      ======     ======

In summary, it does pretty well - with even pretty low coverage,
you're getting 97.4% of the genome in contigs > 500bp (QUAST's default
cutoff).  Misassemblies grow significantly at low coverage, but you're
still only at 2% in misassembled contigs.

Next question -

How well does it do on on a metagenomic data set?
-------------------------------------------------

Sherine has been running benchmarks for Velvet, SPAdes, and IDBA on
the data set from `Shakya et al, 2013
<http://scholar.google.com/citations?view_op=view_citation&hl=en&user=YJoYY7oAAAAJ&sortby=pubdate&citation_for_view=YJoYY7oAAAAJ:yD5IFk8b50cC>`__,
a mock community data set.  So I asked her to add some MEGAHIT
results.  She did quality trimming as specified in `Kalamazoo
<http://khmer-protocols.readthedocs.org/en/v0.8.4/metagenomics/1-quality.html>`__,
and then ran MEGAHIT with 10 GB of RAM.  She then used QUAST to evaluate
the results against the known good genomes.

======================    =======      =======     ======
Measure                   MEGAHIT      SPAdes      IDBA
======================    =======      =======     ======
# contigs > 1kb           19,982       16,387      16,191
length in contigs >       190.7mb      192.5mb     194.8
# misassemblies           698          894         1223
Bp in misassemblies       12.7mb       28.2mb      21.8mb
Metagenome fraction       89.96%       90.42%      90.97%
======================    =======      =======     ======

Again, the answer is "MEGAHIT works pretty well".  Fewer
misassemblies, but also more contigs and a bit less coverage of the
known genome.

Third question --

How fast and memory efficient was MEGAHIT?
------------------------------------------

Very.  We didn't actually measure it carefully, but, like, really
fast.  And low memory, also.  We're doing systematic benchmarking
on this front for our own paper, and we'll provide details as we
get them.

So, what are your conclusions?
------------------------------

So far, +1.  Highly recommended to people who are good at command line
stuff and general all-around UNIX-y folk.  I'd want to play around
with it a bit more before strongly recommending it to anyone who
wasn't a seasoned bioinformatician.  It's rough around the edges, and
I haven't looked at the code much yet.  It also breaks in various edge
cases, but at least it's pretty robust when you just hand it a straight
up FASTQ file!

That having been said, it works shockingly well and is quite fast and
memory efficient.  If you're having trouble achieving an assembly any
other way I would definitely recommend investing the time to try out
MEGAHIT.

--titus

TODO: run on untrimmed, should perform better.
