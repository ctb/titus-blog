Error detection for metagenomic and mRNAseq short-read data sets
################################################################

:author: C\. Titus Brown
:tags: assembly,metagenomics
:date: 2012-08-11
:slug: error-detection-for-metagenome-and-mrnaseq
:category: science

One of the biggest problems with basic sequence analysis -- some would say
*the* biggest problem -- is the error rate.  If our sequencing reads were
error-free, both assembly and mapping would be much, much easier.  Alas,
Illumina reads have a 0.1-1% error rate per base, and PacBio has an error
rate in the 15-30% range.

A good error detection technique can help a lot -- you can either
remove erroneous sequences if you have large volumes of data, or, if
your data is precious, you can try to correct them.  But it all starts
with robust *detection* of errors!

A wide range of error detection techniques have arisen for genomic
samples (see `Quake <http://www.ncbi.nlm.nih.gov/pubmed/21114842>`__ for a
good set of references). All of these error detection techniques use
some form of coverage information to figure out whether or not a
particular base is erroneous; this relies on the fundamental point
that random sequencing errors generate sequence that is random, hence
not present in the actual genomic sample, and therefore unlikely to be
seen more than once or twice.  So if you see rare sequence in a
high-coverage sample, then you can guess that it's an error.

Quite a bit of work has been done on what constitutes "rare" and "high
coverage", and how to distinguish undersampled (but real) sequence
from erroneous (but nonetheless higher coverage) sequence.  (I really
like the discussion in the `Quake paper
<http://www.ncbi.nlm.nih.gov/pubmed/21114842>`__ about this, if you're
interested.)

Despite all this work, there are a bunch of problems with error
detection.  The main one that's been causing me grief is that
the above techniques only work on genomic samples, and not on mRNAseq
or metagenomic sequence.  This is because metagenomes and mRNAseq
don't really have a single "coverage" per se -- there are high
abundance and low-abundance components in mixed populations, and
so you can't easily look at a k-mer in a sequence and decide that
it's good or bad by looking at all the other k-mers in the sample.
In particular, if you get rid of rare sequences (as a number
of published metagenome assemblies did) then you get rid of both
errors in high coverage sequence AND real low-coverage sequence.

This bit us in the `digital normalization paper
<ivory.idyll.org/blog/diginorm-paper-posted.html>`__.  For genomic
samples, we recommend a 3-pass digital normalization approach -
normalize coverage, eliminate low-abundance k-mers, and then normalize
coverage again.  (There is a somewhat confusing technical reason for
doing this in three passes that you can read in the diginorm paper.)
However, for mRNAseq and metagenomes, this approach of eliminating
low-abundance k-mers doesn't work well, in fact ends up trashing a bunch
of real -- but low-coverage -- data.  So for mRNAseq and metagenomics
data we don't yet recommend low-abundance k-mer removal.

It turns out, though, that this problem is easily solved by using an
approach derived from digital normalization.  Digital normalization is
based on the observation that you can estimate the per-locus coverage
of reads in various ways; all you have to do is couple that to a
second step that looks for low-abundance k-mers in high-coverage
reads.  (An alternate way of saying it is that we can look for
low-coverage nodes adjacent to high-coverage graph components.)

As part of my `grant-a-palooza <http://ged.msu.edu/interests.html>`__
this summer I worked through how to actually do this, and wrote a
simple reference implementation.  The essential idea is in the
following figure:

.. image:: http://ivory.idyll.org/permanent/error-detection.png
   :width: 60%

It's pretty simple: you collect reads for each locus until you reach a
saturation point for that locus (say, an average coverage of 20); then
you stop collecting reads, and instead start running error detection
on them.  At the end, you go back through all of the collected reads
and run error detection on them, to.  If there are low-coverage
loci, then you never do any error correction on reads belonging to them
and hence don't eliminate any genuinely low abundance sequences.

Unlike digital normalization, this is not a single-pass approach,
because you have to look at the collected reads more than once.  But
it is a few-pass approach: for high-coverage data sets, you touch most
reads only once.  (My estimate is that for 100x coverage genomic data
set and a coverage saturation point of 20x, you would look at only 20%
of the reads twice -- so it would be a 1.2x pass approach.)  This is
already substantially better than most error correction programs,
which require at least two passes across the data.  Moreover, with
use of Counting Bloom Filters as in our `khmer
<http://github.com/ged-lab/khmer/>`__ software, the approach can be
done in fixed and relatively low memory.

Sooooo, does it work?  On simulated data sets, the answer is "yes!"
but I wanted to try it out on some real data.  So I took advantage of
my time at the `STAMPS <http://stamps.mbl.edu/>`__ course to run it on
the `HMP mock community data sets <http://hmpdacc.org/HMMC/>`__.
Conveniently, for these data sets, we know the "ground truth" -- the
true genomes from which the reads came -- and so I can cross-validate
against that.

The results are below.  The figure shows a graph of error location
within reads, for both k-mer-based approaches (no reference needed)
and a reference based analysis.  The k-mer based approach is in blue,
and the reference-based analysis is in green.  I used a k of 20, so in
the k-mer based approach errors in the first 20 positions are all
aggregated at the first position.  Note that absolute
numbers of errors have been adjusted by a factor of 10 to overlap;
the error detection script only detects the first error in a read,
and not any of the following errors, while the reference-based
analysis finds all of the mismatches in the read, so they do not
have the same y scale.

.. image:: http://ivory.idyll.org/permanent/mock-error-profile.png
   :width: 60%

Note that the shape of the curve is the same, and the peaks are at the
same place.  It works!  Remember, for the blue curve, *we didn't use
the reference sequence*.  Also remember this is for *metagenomic*
sequence, not genomic sequence!  (Although it will work just fine
on genomic sequence, too.)

So, as far as I can tell, our approach is a conceptual solution to
error detection (and, soon, error *correction*) for mRNAseq and
metagenomic data sets.  Pretty neat.

The scripts to do all of this are in the khmer repository; see
`trim-low-abund
<https://github.com/ged-lab/khmer/blob/master/sandbox/trim-low-abund.py>`_
and `dn-identify-errors
<https://github.com/ged-lab/khmer/blob/master/sandbox/dn-identify-errors.py>`__.
They're pretty ugly and largely untested, so I wouldn't recommend
using them out of the box; we have lots of work to do on them before
they're ship-ready.  But the concept seems to work!

--titus

p.s. There are a number of tricky issues to work out, of course --
repeats are a chief concern, for example; for mRNAseq, splice variants
would be dropped, too.  We're working on ways to deal with that.

p.pp.s. Incidentally, digital normalization may be a good way to
preprocess Illumina reads prior to using the `new PacBio read
correction approaches <http://www.ncbi.nlm.nih.gov/pubmed/22750884>`__
- thanks to Lex Nederbragt for pointing this out.

