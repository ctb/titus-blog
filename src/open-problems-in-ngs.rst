Open problems in next-gen sequence analysis
###########################################

:author: C\. Titus Brown
:tags: ngs,bioinformatics
:date: 2012-06-25
:slug: open-problems-in-ngs
:category: science

At our `2012 course on Analyzing Next-Generation Sequencing Data
<http://bioinformatics.msu.edu/ngs-summer-course-2012>`__, we talked
quite a bit about future sequencing technologies, as well as about
what analyses are reasonably cookbook (and which ones aren't).

Here are my thoughts -- yours welcome!

Sequencing tech
---------------

The basic conclusions about sequencing tech were these:

1. Illumina is by far the "best" current technology in terms of
   breadth and depth of applications.  454 is waning in utility and
   it's simply not cost effective; PacBio is too error prone for
   widespread use; and Nanopore technologies are not yet available,
   much less proven.  Illumina MiSeq looks particularly beguiling,
   with fast turnaround and long reads.  One surprise to me was that
   the Ion Torrent was billed as being error prone and currently
   rather expensive.

2. Illumina is likely to remain "it" as far as RNAseq and shotgun
   metagenomics goes: depth of sampling is critical for these
   applications, and no other technology has anything like the
   deep sampling provided by Illumina.

Given the speakers and attendees we had this year, I think these are
pretty robust conclusions for what's available today.  3 months from
now?  Who knows!?  The sequencing field is moving awfully fast...

Bioinformatics needs
--------------------

For me, of course, the bioinformatics needs ware just as interesting,
if not more so.  Bench biologists seem to finally be getting the idea
that data generation isn't very interesting if you can't do a good
analysis of the data (and those "good analyses" also need good
downstream hypothesis generation & validation, but that's a separate
point...)

My perspective (informed by both discussions with course faculty as
well as results from my own research program -- yarr, these be forward
looking statements, me matey!) is that several NGS problems have been
essentially solved, modulo some important finer details.  These
include reference-free transcriptome assembly, isoform
detection/extraction/analysis, and resequencing analysis of
individuals.  Good software exists for these tasks, and while I'm sure
speedups and enhancements to software and algorithms will come, I
doubt that these areas will be fruitful for serious, novel
bioinformatics work.  I also personally believe that *efficient*
assembly of genomes, transcriptomes, and metagenomes (with one caveat
-- see below) is solved by digital normalization, although *quality*
of assembly will remain an issue for a while.

So... what's left?  What's still really hard?

1. **Differential gene expression.** The biggest surprise from the
   course was that none of the faculty had good recommendations for a
   protocol or pipeline for determining differentially expressed
   *genes*.  RSEM and other EM-based algorithms were mentioned but it
   turns out that head-to-head comparisons of these algorithms show
   poor agreement between them.  All wrong?  All right?  Who knows??
   We had a wide ranging discussion about this that led me to some
   thoughts about a possible solution, which is always nice...

   (In contrast, differential *exon* expression is much easier...)

2. **Assembly of non-model genomes.** There's a dark cloud hanging
   over genome assembly: polymorphism, thy name is mud.  Repeats and
   polymorphism (aka heterozygosity and strain variation) are hard for
   current assemblers to resolve, and I have experienced the horrors of
   these problems myself in several projects.

3. **Combining 454, Illumina, and other read technologies.** It kind
   of baffles me that this is true, but as far as I can tell there is
   no good way to combine multiple read technologies for genome or
   transcriptome assembly.  I can find lots of ad hoc protocols, of course,
   but everyone always seems to end with "...so this is what we use, and
   it kind of sucks."  References to better solutions are welcome...

4. **Recovery or inference of haplotypes.** Short-insert data isn't
   good for the haplotype phasing problem, alas.  Still very challenging.

5. **Metagenome assembly of diverse environments.** Digital
   normalization makes most assembly scaling challenges go away, by
   shifting the problem to one that scales with the diversity of your
   sample; I see no reason you can't do contig assembly of pretty much
   anything on a commodity machine with 512 GB-1 TB of RAM.  The
   problem here is that soil and marine environments seem to have
   nigh-infinite diversity.  This is where `partitioning
   <http://arxiv.org/abs/1112.4193>`__ comes in handy, but we think we
   can only complete an assembly of about 1-2 Tbp of data with current
   holistic approaches.

6. **Efficient error correction.** Error correction of Illumina reads,
   PacBio, 454, etc. is a growth area -- especially *efficient* error
   correction.

7. **Population sequencing.** People insist on feeding mixed populations
   into sequencers, for both good and bad reasons.  This is bioinformatically
   challenging to resolve in terms of recovering variants and distinguishing
   them from errors.

So, anyway, that's my 2 cents.  I'm actually working on all seven of
these, and I am pretty sure we can provide significant leverage on #2,
#3, #5, and #6.  Stay tuned!

I'd love to hear other thoughts on these weighty issues.

--titus
