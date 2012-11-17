How much sequencing is needed for...?
#####################################

:author: C\. Titus Brown
:tags: science,ngs,metagenomics,assembly
:date: 2012-11-17
:slug: how-much-sequencing-is-needed
:category: science

I gave a talk last Wednesday at U. Michigan in the `DCMB program
<http://www.ccmb.med.umich.edu/>`__ where I included a slide
estimating how much DNA sequencing (in base pairs) was needed for good
de novo assembly of sequences from various biological environments or
problems.  The slide was there to motivate the challenges of soil
metagenomics.

As you can see, you need about the same amount of sequencing for
a soil or a marine metagenome as you do for a human genome.  Or E. coli.

.. figure:: ../static/images/how-much-seq-1.png
   :width: 500px

   Fig 1. How much sequencing is needed for de novo assembly (from
   Illumina short reads)?

Wait, what?  The E. coli genome is about 3 orders of magnitude smaller
than the human genome -- they shouldn't compare!

Oh, sorry, the Y axis on that figure is in log format.  Sorry, rookie
mistake.  Here's the figure with a linear Y axis.

.. figure:: ../static/images/how-much-seq-2.png
   :width: 500px

   Fig 2. How much sequencing is needed for de novo assembly (from
   Illumina short reads) -- non-log-Y version.

Hmm.  How did I say I got these numbers, again?

The basic calculations are on `this Google Docs spreadsheet
<https://docs.google.com/spreadsheet/ccc?key=0ArcOEBWnXSBidHhubFpWTzQ5akJsLWg0d3FWS2R3SFE#gid=0>`__.  For de novo assembly from Illumina reads, I estimated
a requirement of 100x coverage (you can lower that to 20x if you want; it
doesn't change the results all that much ;).  The effective genome sizes are calculated as follows:

*  for E. coli and the human genome, the numbers are well known: 5 Mbp for
   E. coli, and 3 Gbp for a (haploid) human genome.

*  for the transcriptome, I adlibbed some numbers from `this excellent
   blog post by Anthony Fejes <http://blog.fejes.ca/?p=607>`__.
   Briefly, I calculated that we needed about 100m reads, 100bp in
   length, per RNAseq sample; and that we would want to sample about
   50 tissues to get a reasonably complete transcriptome.

* for the metagenomes, I calculated the dilution factor of the rarest
  species we wanted to see -- 1 in 200 for human gut, 1 in 1e3 for
  marine, and 1 in 1e6 for agricultural soil.  The first number is
  from the MetaHIT papers and is probably wrong. The second number
  comes from Greg Dick at U. Michigan, who works on marine
  environments.  The third number comes from Tracy Teal, who works on
  soil. The soil number is actually quite a bit lower than the
  estimate I cite in my papers, which is from `Gans, Wolinsky, and
  Dunbar (Science, 2005)
  <http://www.sciencemag.org/content/309/5739/1387>`__.  That paper
  claims a million *distinct* bacterial genomes in each gram of soil.

  I then multiplied this dilution factor by the estimated genome
  size for most bacteria (5e6 -- again, you can change this
  number down to 2.5e6, a good lower bound on the average, without
  much effect).  I then multiplied *that* by 100x coverage for
  assembly from Illumina.

  The basic logic is that in order to assemble each metagenome (or
  transcriptome) "completely", we need to get sufficient shotgun
  coverage of the *rarest* genome in the metagenome (or transcript in
  the transcriptome) in order to assemble it.

  (This is absent considerations of noise, etc. -- read this
  `excellent paper from @joe_pickrell et al., Noisy Splicing Drives
  mRNA Isoform Diversity in Human Cells
  <http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1001236>`__.
  But I would argue you want to see the noise, then discard it as
  noise, rather than *ignore* it because you think you know it's
  noise.)

Feel free to tweak the numbers in `the spreadsheet
<https://docs.google.com/spreadsheet/ccc?key=0ArcOEBWnXSBidDhqczZzX016NUJkdzBWbXl6Wk5QcFE>`__
if you disagree with the assumptions made above, of course.

A few things to mention.

These are *per individual*.  If you want a single bacterial or human
genome, or a transcriptome for a single human (or vertebrate), or a
complete metagenome from a single gut, marine, or soil sample, these
numbers apply.  It is an interesting question as to whether you can do
shallower sequencing across multiple samples to detect rare
transcripts (in transcriptomes) and rare genomes (in metagenomes), but
I do not think we know the answer yet.

The numbers will be ~10x lower for detection, assuming you trust
your reference genome/transcriptome/metagenome (hint: I wouldn't).

Second, yes, soil does seem to be that ridiculously diverse.  In fact,
it's probably more diverse; these estimates are from 16s, and probably
ignore archaea and eukaryotes.  They certainly ignore phage.  Given
that phage are likely to be high abundance even if they're rare (which
we think we are seeing in some of our soil data) the above calculations
are almost certainly an underestimate.  This may be balanced by my
failure to account for rRNA copy number in the bacteria, though, which
would make my estimates a bit of an *over*-estimate, by maybe a factor
of 5-10.

I'll talk more about soil in the future, as we start to post some of
our ag soil papers.  Soon, I promise!

Third, these calculations are an inescapable fact of shotgun
sequencing, which samples randomly from the population of molecules.
Sample enrichment approaches will certainly help lower this number, if
you can target low abundance molecules in some way -- think library
normalization, or cell sorting.  On the other hand, they may also
increase bias in your sampling... I tend to argue that, as sequencing
costs continue to drop, you might as well just shove it all into a
sequencer and use bioinformatics to sort it out.

Fourth, would increased read lengths help?  Well, for de novo assembly,
you can probably get away with 5-10x coverage with PacBio, if you
assume that their error rate is going to decrease.  That's in the
graph below.

.. figure:: ../static/images/how-much-seq-3.png
   :width: 500px

   Fig 3. How much sequencing is needed for de novo assembly from
   PacBio reads - 10x coverage.

And the answer is, you still need to generate 10s of billions of reads
for many of these samples.  I do not yet have a clear cost estimate on
PacBio or Nanopore reads -- I'd welcome a followup blog post or
correct numbers! -- but I suspect that Illumina is still the only game
in town for complex non-genomic samples, and will remain so for some
time.  (Also see this excellent blog post from EdgeBio: `MiSeq 2x250
-- Does Length Really Matter?
<http://www.edgebio.com/miseq-2x250-%E2%80%93-does-length-really-matter>`__)

----

So, for our soil samples, we really do think we need about 50 Tbp or
more (that's 50e12) per sample.  And that's why we are working on
`scaling de novo assembly
<http://ivory.idyll.org/blog/an-assembly-handbook-for-khmer.html>`__
:).

Comments welcome!

--titus
