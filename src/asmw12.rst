Argonne Soil Metagenomics Workshop 2012 - my talk
#################################################

:author: C\. Titus Brown
:tags: khmer,assembly,metagenomics,soil
:date: 2012-10-05
:slug: asmw12
:category: science

These talk notes are for my talk at the `2012 Argonne Soil Metagenomics
Workshop <http://press.mcs.anl.gov/asmw12/>`__.

..  @@slideshare.

Slide 1 - title
---------------

I'm going to be talking about our assembly pipeline for soil metagenomes.

Slide 2 - acks
--------------

Much of this work was done by a talented former postdoc of mine, Adina
Howe, who has now moved on to Argonne National Lab.  Other students and
postdocs contributed significantly, including most especially Jason Pell
who has been involved with many of the underlying computational work.
I have some excellent collaborators, including Jim Tiedje and Janet
Jansson.

Slide 3 -- kids
---------------

Folker should feel free to call my sequencing data ugly, but even he has
to admit that my daughteres are very attractive.  They take after their
mother, who bears the burden of me being gone from home to talk here.

Slide 4 -- open science
-----------------------

Everything I'm discussing here is available online!

Slide 5 -- a polemic position
-----------------------------

I don't see any alternatives to short-read sequencing and assembly in
soil metagenomics.  We need deep sampling and total bases, not fewer
but longer reads.  Isolation and enrichment approaches are excellent
complements to whole metagenome sequencing, but with the vast diversity
present in agricultural soil, they won't give you everything anytime
soon.  Whole metagenome sequencing lets you study the nucleic acid
content of communities in situ, which is one of the things we really
want to do!

I would also like to point out that assemblies are computationally
convenient: they represent a summary of the short read data, and often
a *much* smaller summary.

Slide 6 -- holy heck that's a lot of diversity!
-----------------------------------------------

Even in this crowd, I rarely see an appreciation for just how diverse
soil really is.

To sequence the things that we can reproducibly see in OTUs, we will
need a minimum of about 50 Tbp of sequencing -- roughly 100 full
Illumina HiSeq runs -- to sample it thoroughly.  (That's whether or not
you're doing assembly!)

Alternatively, if you guess that there are about 100,000 species in a soil
sample, that's approximately 100x the genomic complexity of a haploid
human genome.

We can do this sequencing, and it's becoming progressively easier.  But
current assembly and analysis approaches simply cannot handle this data!

Slide 7 -- coverage is essential.
---------------------------------

To robustly assemble things, you *really* need high coverage.  This is
a graph of fraction of things recovered in 300 bp or 1kb contigs from
the Human Microbiome Project mock community -- real sequencing of a fake
community -- showing that you need at least 10x coverage, on average,
to retrieve about 95% of genome content in 1kb contigs.  That's where
the 50 Tbp number comes from in the last slide.

The main reason you're not getting assemblies is because usually most
of the microbes in your soil metagenomes have not reached this threshold.

Slide 8 -- scaling challenges
-----------------------------

We've spent a lot of time figuring out how to analyze this essentially
infinite amount of data.  Our goal is to make metagenome assembly
straightforward, and to develop evaluation techniques so that you can
tell when your assembly is good.

Slide 9 -- DOE grand challenge data set
---------------------------------------

The data set that really motivated this work came from the JGI via
Janet Jansson and Jim Tiedje.  This is a two terabasepair Illumina
data set from 9 different midwestern soil samples, including an Iowa
cornfield and Iowa prairie.  They took small, ~1g samples of soil
and subjected them to both 16s and Illumina sequencing.  It's one
of the largest soil metagenome data sets around.

Today I'll be talking about our assemblies of the Iowa corn and Iowa prairie
data sets, which are each on the order of 300 Gbp, or 3 billion reads each.

Slide 10 -- digital normalization
---------------------------------

The first technique we developed for dealing with this data is a
computational version of cDNA library normalization, in which we
preferentially downsample high abundance components of the data for
the purpose of assembly.  This is predicated on the observation that
in mixed samples, much of the data is essentially redundant -- by
the time you robustly sample the low-abundance genomes that are in
your data, you've seen the high abundance stuff quite a bit!  This
data consumes disk space and memory.

.. @@

Slide 11 -- data partitioning
-----------------------------

The second technique we developed is a computational version of
cell sorting, in which we use read-to-read connectivity to split
reads into bins.  These bins turn out to correspond really well
to source genomes -- that is, reads that bin together tend to
come from the same species.  I'll show you an example of that
later.

We can do this partitioning very efficiently due to some nifty
computational techniques we've developed.

Slide 12 -- our computational strategy
--------------------------------------

So, our overall computational strategy is this: develop computational
approaches as needed, critically evaluate them on test data sets,
especially including those where we already know the answer, and see
what we see!  Our general experience and those of labs using our
software is that our stuff works pretty well, especially for scaling.
The digital normalization stuff Just Works, but relatively few people
are using the partitioning.

Slide 13 -- partitioning on real data
-------------------------------------

When we look at the mock community data with partitioning, what we can see
is that the vast majority of partitions, or bins of reads, contain reads
from only one genome (in blue).  A few reads, those from highly conserved
genes in different species, tend to group together (green), but it's less
than 2-3%.

When we do a computational spike-in of a single E. coli, we find that
we can group all those reads together into a separate set of partitions.

When we do this with 5 different E. coli strains, we do get partitions
that contain reads from all of those strains, and those reads do assemble
together.  This is essentially unavoidable, but we can detect it very
easily.

Slide 14 -- assembling soil
---------------------------

So when we assemble soil, what do we actually get?  A lot.

We recover approximately 3 Gbp of sequence in contigs > 300 bp,
containing millions of contigs and genes.  Overall we assemble only
about 20% of the reads from the highest abundance critters, indicative
of the ridiculous diversity lurking just below the coverage threshold.

Slide 15 -- contigs are low coverage
------------------------------------

After assembling contigs we can go back and count them, by mapping raw
reads back to them.  Basically we see that, as expected, most of our
contigs end up being low coverage; the corn is slightly small so we
have, overall, less coverage.

Slide 16 -- even abundance distributions
----------------------------------------

When we line contigs up on a rank/abundance distribution, we see that
after a bit of high abundance stuff, there is a long slow plateau
that represents the underlying evenness of the microbial population.
Essentially we see that it is very hard to pick off the highest abundance
critters to any degree because there's *so many* that are all at similar
abundance.

Slides 17 and 18 -- preliminary taxonomy
----------------------------------------

These represent the taxonomy of individual contigs, without accounting
for abundance.  So, for example, phage contigs are counted only once
even though they may be very high abundance.  This is something
that the MG-RAST folk will be adding for assemblies.

Slide 19 -- strain variation
----------------------------

Another thing that we can do is assess the degree to which strain variation
or polymorphism shows up, by mapping reads back to the assembled contigs.
This graph represents one particular contig, with the top two alleles
plotted for each position; at the ends, we see higher variation because
of repeat content that tends to end contigs, while in the middle you 
can see more reliable variants.  Here you can see that there's only one
position with a minor allele present in > 5% abundance.

Overall, when we look at the 5000 most abundant contigs, only 1 of
them has an average polymorphism rate of above 5%.  This is less than
some animal genomes, and tells us that we should expect to get decent
non-chimeric assemblies of these regions.

So, for our samples -- which represent very small, localized soil
samples -- we haven't yet seen much in the way of strain variation.
We think that we can assemble what we do see, with the caveat that
you may get chimeric assemblies that we can pick out later.


Slide 20 -- technology conclusion
---------------------------------

Basically, we can assemble stuff.

We want you to be able to assemble stuff.

We have good ways to assemble lots more stuff, and are working on them.

Slide 21 -- assembly conclusion
-------------------------------

The main message I want to convey is that, one way or another, we will
be able to extract decent quality metagenomes from shotgun metagenomics.

Depending on sample, you may not need to worry a lot about strain variation.
Either way, we can generate assemblies and figure out if they're chimeric.

Your job?  To make sense of all of this :)
