Digital normalization of short-read shotgun data
################################################

:author: C\. Titus Brown
:tags: ngs,python,diginorm
:date: 2012-03-21
:slug: diginorm-paper-posted
:category: science


We just posted a pre-submission paper to arXiv.org:

**A single pass approach to reducing sampling variation, removing
errors, and scaling de novo assembly of shotgun sequences**

Authors: C. Titus Brown, Adina Howe, Qingpeng Zhang, Alexis B. Pyrkosz,
and Timothy H. Brom

`arXiv link <http://arxiv.org/abs/1203.4802>`__

`Paper Web site, with source code and tutorials <http://ged.msu.edu/papers/2012-diginorm/>`__

Abstract:

   Deep shotgun sequencing and analysis of genomes, transcriptomes,
   amplified single-cell genomes, and metagenomes enable the sensitive
   investigation of a wide range of biological phenomena. However, it is
   increasingly difficult to deal with the volume of data emerging from
   deep short-read sequencers, in part because of random and systematic
   sampling variation as well as a high sequencing error rate.  These
   challenges have led to the development of entire new classes of
   short-read mapping tools, as well as new *de novo* assemblers.
   Even newer assembly strategies for dealing with transcriptomes,
   single-cell genomes, and metagenomes have also emerged.  Despite these
   advances, algorithms and compute capacity continue to be challenged by
   the continued improvements in sequencing technology throughput.  We
   here describe an approach we term digital normalization, a single-pass
   computational algorithm that discards redundant data and both sampling
   variation and the number of errors present in deep sequencing data
   sets. Digital normalization substantially reduces the size of data
   sets and accordingly decreases the memory and time requirements for
   *de novo* sequence assembly, all without significantly impacting
   content of the generated contigs.  In doing so, it converts high
   random coverage to low systematic coverage.  Digital normalization is
   an effective and efficient approach to normalizing coverage, removing
   errors, and reducing data set size for shotgun sequencing data sets.
   It is particularly useful for reducing the compute requirements for
   *de novo* sequence assembly.  We demonstrate this for the assembly
   of microbial genomes, amplified single-cell genomic data, and
   transcriptomic data.  The software is freely available for use and
   modification.

---

I'll blog more about this stuff over the next few days, but, briefly,
this paper presents a single pass, fixed-memory approach to
downsampling sequencing data (yeah, the `stuff I've been talking about
for a while now
<http://ivory.idyll.org/blog/mar-12/big-data-biology>`__).  This
approach is called "digital normalization", or "diginorm" for sure.
It eliminates lots of data, evens out coverage, and removes errors
from shotgun sequencing data sets.  The net effect is an often massive
amount of data reduction combined with significant scaling of *de
novo* assembly.

Or, to put it another way, it's a streaming lossy compression
algorithm that primarily "loses" errors in sequencing data.

We've implemented it as a preprocessing filter that should work on any
data set you want to assemble, with potentially any assembler.  It's
written in C++, with a Python wrapper, as part of `khmer
<http://github.com/ctb/khmer/>`__.  And, of course, it's freely
available for use, re-use, modification, and redistribution under the
BSD license, 'cause why the heck not?

If you want to try it out, we've linked to some tutorials for running
microbial genome assemblies with Velvet, as well as eukaryotic
transcriptome assemblies with Oases and Trinity, on the
`paper Web site <http://ged.msu.edu/papers/2012-diginorm/>`__

We'll submit this paper to PNAS on Friday; I'm still waiting for some
final proofreading.

Together with `our other paper <http://arxiv.org/abs/1112.4193>`__,
which is currently under revision for resubmission to PNAS, these two
papers form the theoretical basis for our attack on soil metagenome
assembly.  (Our plan is sheer elegance in its simplicity!)

--titus


----

**Legacy Comments**


Posted by Mick on 2012-03-22 at 04:40. 

::

   How does this differ from other error correction tools eg Quake?


Posted by Titus Brown on 2012-03-22 at 08:26. 

::

   Mick, it's more efficient than any algorithm I know of (single pass,
   fixed memory) and works on many kinds of Illumina shotgun data
   (genome, MDA, transcriptome, metagenome).  The result is often a
   factor of 10x or more improvement in memory usage and CPU time; see
   tables 3 and 4.  It also leads to dramatically improved assemblies in
   a broader variety of circumstances than any other tool or approach;
   diginorm does a lot more than error correction.  (We don't discuss the
   better assemblies in this paper, because we focused on describing the
   basic approach.)    --t


Posted by Mads Albertsen on 2012-03-23 at 01:06. 

::

   Thanks for putting the code and paper out in the open. I've been
   playing with khmer on semi-large datasets (100-500 Gb metagenomes and
   SC genomes) and I usually see "better" assemblies by just normalizing
   on one PE read and then extracting the 2nd PE read using the
   normalized 1st PE reads. Is there any theoretical concerns in using
   this low tech solution to retain the maximum number of PE reads?
   rgds  Mads


Posted by Mads Albertsen on 2012-03-23 at 01:09. 

::

   Thanks for putting the code and paper out in the open. I've been
   playing with khmer on semi-large datasets (100-500 Gb metagenomes and
   SC genomes) and I usually see "better" assemblies by just normalizing
   on one PE read and then extracting the 2nd PE read using the
   normalized 1st PE reads. Is there any theoretical concerns in using
   this low tech solution to retain the maximum number of PE reads?
   rgds  Mads


Posted by Titus Brown on 2012-03-23 at 10:17. 

::

   Mads, sounds fine to me!  We've been doing the opposite --
   interleaving, diginorm, then extracting paired sequences and orphans
   and assembling separately -- see the tutorial.  But this is guesswork
   &amp; intuition and not based on empirical evidence of any sort.  Let
   me know if you end up doing a comparison and find evidence one way or
   the other :)    --titus


Posted by Nathaniel Street on 2012-03-28 at 05:43. 

::

   Would you say it is safe to apply this to heterozygous species?


Posted by Titus Brown on 2012-03-29 at 13:25. 

::

   Hi Nathaniel,    it's not going to screw up your assembly any more
   than the assembler will... heterozygosity is a problem for pretty much
   all assemblers :)    We have used it with apparent success ourselves,
   yes.    -titus


Posted by Mircea Podar on 2012-04-04 at 08:50. 

::

   Thanks for the updates, very useful. I was looking at the output from
   the different scripts and it appears that the low-abundance filtering
   doesn't get rid of the entire read but chops out the culprit k-mer.
   This leaves a bunch of much shorter reads that often times dont pass
   the k size in velvet. Is there a particular reason why  maintaining
   fragmented reads as opposed to getting rid of them?  best,  mp


Posted by Titus Brown on 2012-04-04 at 17:30. 

::

   Mircea, you may want to assemble with different k-mer values in Velvet
   (or others) so our philosophy is to simply leave it all in.  We should
   eliminate reads that are shorter than the filtering k.

