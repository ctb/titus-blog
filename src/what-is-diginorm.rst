What is digital normalization, anyway?
######################################

:author: C\. Titus Brown
:tags: ngs,python,diginorm
:date: 2012-04-06
:slug: what-is-diginorm
:category: science


I'm out at a `Cloud Computing for the Human Microbiome Workshop <http://chem.colorado.edu/knightgroup/index.php?option=com_flexicontent&view=items&id=254:cloud-computing-for-the-microbiome-workshop->`__ and I've been trying to convince people of the importance of digital normalization.  When `I posted the paper <http://ivory.idyll.org/blog/mar-12/diginorm-paper-posted>`__ the reaction was reasonably positive, but I haven't had much luck explaining why it's so awesome.

At the workshop, people were still confused.  So I
tried something new.

I first made a simulated metagenome by taking three genomes worth of
data from the Chitsaz et al. (2011) paper (see
http://bix.ucsd.edu/projects/singlecell/) and shuffling them together.
I combined the sequences in a ratio of 10:25:50 for the E. coli
sequences, the Staph sequences, and the SAR sequences, respectively;
the latter two were single-cell MDA genomic DNA.  I took the first 10m
reads of this mix and then estimated the coverage.

You can see the coverage of these genomic data sets estimated by using
the known reference sequences in the first figure.  E. coli looks nice
and Gaussian; Staph is smeared from here to heck; and much of the SAR
sequence is low coverage.  This reflects the realities of single cell
sequencing: you get really weird copy number biases out of multiple
displacement amplification.

Then I applied three-pass digital normalization (see `the paper
<http://ivory.idyll.org/blog/mar-12/diginorm-paper-posted.html>`__) and
plotted the new abundances.  As a reminder, **this operates without
knowing the reference in advance**; we're just using the known reference
here to check the effects.

.. figure:: http://ivory.idyll.org/permanent/raw-coverage.png
   :width: 400px

   Coverage of genome read mix, calculated by mapping the mixed reads
   onto the known reference genomes.

.. figure:: http://ivory.idyll.org/permanent/norm-coverage.png
   :width: 400px

   Coverage post-digital-normalization, again calculated by mapping
   the mixed reads onto the known reference genomes.

As you can see, digital normalization literally "normalizes" the data
to the best of its ability.  That is, it cannot create higher coverage
where high coverage doesn't exist (for the SAR), but it can convert
the existing high coverage into nice, Gaussian distributions centered
around a much lower number.  You also discard quite a bit of data (look
at the X axes -- about 85% of the reads were discarded in downsampling
the coverage like this).

When you assemble this, you get as good or better results than
assembling the unnormalized data, despite having discarded so much
data.  This is because no low-coverage data is discarded, so you still
retain as much overall covered bases -- just in fewer reads.  To boot,
it works pretty generically for single genomes, MDA genomes,
transcriptomes, and metagenomes.

And, as a reminder? Digital normalization does this in fixed, low
memory; in a single pass; and without any reference sequence needed.

Pretty neat.

--titus



----

**Legacy Comments**


Posted by Mick Watson on 2012-04-11 at 04:31. 

::

   It's a cool idea :)    Quick questions:     1) how does it scale to
   samples with 300 organisms?  2) how does it compare to existing
   methods which partition de bruijn graphs based on coverage?    Cheers!


Posted by Titus Brown on 2012-04-11 at 08:49. 

::

   We've applied it to samples where we estimate we end up with about 700
   microbial genomes worth of genomic DNA, based on assembly and single-
   copy gene #; for that we've used a big hash table (I think 128gb).
   There should be 10,000-1m species in the sample, though, so we have
   further to go.    As far as we can tell (some qualifications may
   apply), for microbial genomes, diginorm + assembly gives essentially a
   superset of what other approaches yield.  We cannot show this yet for
   really complex situations where strain variation and sequencing
   artifacts may be messing with us.

