Title: A quick read of _The genomic and proteomic landscape of the rumen microbiome_
Date: 2018-12-08
Category: research
Tags: rumen, metagenome assembly
Slug: 2018-rumen-metagenome-in-brief
Authors: C. Titus Brown
Summary: Using short and long reads to assemble genomes from metagenomes!

Today, I woke up to several tweets about the preprint of a new paper from Mick
Watson et al.,
[The genomic and proteomic landscape of the rumen microbiome revealed by comprehensive genome-resolved metagenomics](https://twitter.com/BioMickWatson/status/1071443060914032640). A few things about the tweets caught my eye:

* "Complete single contig microbial genomes from nanopore long reads"
* "MinION + rumen DNA + Dr. Amanda Warr = circular contigs of novel rumen bacteria"
* "You want complete, circular bacterial chromosomes assembled from a complex microbiome? It's here!"

and I wanted to dig into the results!

**This is my hot take on the paper**, written while desperately
avoiding my inbox, sitting at a coffee shop across from my 8 yro
daughter (who is playing The Room) while waiting for my 11 yro
daughter to finish her viola lesson.  I welcome corrections and
questions!

I feel compelled to mention that Mick and I have a complicated
relationship: for example, in a uniquely British microaggression, he
once tweeted my Norwich breakfast order line by line, while sitting at
nearby table. Our relationship in no way affects this blog post, which
will seek to understand the paper's methods without snark. ;)

The preprint is
[here](https://www.biorxiv.org/content/early/2018/12/08/489443) and it
is very straightforward and readable!

A brief outline of the results from a methods-oriented perspective:

* They generated 6.5 Tbp of sequence data from rumen, all Illumina.
* From this, they generated approximately 5000 metagenome-assembled genomes, all 80% or more complete; 4,000 of these are novel.
* They also used a Nanopore MinION to sequence the one of the samples, and generated 11.4 Gbp of data with a read N50 of 11kb and mean read length of 6kb.
* A Canu assembly of the Nanopore data led to 178 Mbp of contigs greater than 1kb in length, with an N50 of 268kb.
* Five of these contigs are bigger than 3 Mbp in length, and 31 of the contigs are predicted to be circular (i.e. closed genomes!)
* Two *Prevotella copri* genomes were extracted: one was generated by Nanopore and one was generated by Illumina. They are very, very similar.

It's hard to describe how exciting these results are! While rumen
communities are still a far cry in complexity from soil and sediment
communities, they are much more complex than acid mine drainage and
hot spring communities, and here we are getting thousands and
thousands of genomes from them! WOW!

## Questions and comments

The questions and comments I had are all related to generalizability
of the techniques used in this paper.

### Q: How were the Illumina genomes assembled?

Each of 282 rumen samples were sequenced fairly shallowly with
Illumina (~24-140m 2x150bp reads). Then
each sample was assembled and binned independently. In addition,
six "batches" of samples were assembled together, in order to recover
lower-abundance genomes.

In the first version of this blog post, I had not see the co-assembly
step & Mick corrected me on twitter; see comments.  Mick also said (in
another tweet linked in the comments) that they were unable to
assemble all 282 samples together, due to limitations in MEGAHIT.

### Q: How were the Nanopore assembled genomes affected by the shallower coverage of the Nanopore data?

One of the samples was sequenced with both Illumina and a Nanopore MinION.
The MinION generated 11.4 Gbp of data with a read N50 of
11kb and mean read length of 6kb. The amount of data generated for that
sample with Illumina was not directly stated in the text of the paper, but 
it's probably in the 30 Gbp range (100m 2x150 bp reads).

What I can't tell from my first read of the paper is exactly how the
Illumina and Nanopore data compared in terms of overlap.

So, while the Nanopore assembled contigs are (much) longer than the
Illumina assembled contigs, I would bet that the Illumina data covers
most of the Nanopore data and also recovers a lot more sequence,
including strain variation in the Nanopore genomes. I'd love to
understand this better!

(Which actually points to the interesting thought that maybe polishing
metagenome-assembled microbial genomes will need new strain-aware
methods!)

### Q: When can we stop using Illumina and start using Nanopore data alone??

I didn't reach a good understanding here, but as I understand it from
my first read, Illumina data is (much) more cost effective
and is also quite important for correcting the Nanopore data.

Two specific points that I took from this paper:

* the raw Canu assemblies of the Nanopore data were quite inaccurate on per-base level and had to be corrected with Illumina data;
* Each Illumina sample probably cost about $500, while the MinION
  sample probably cost about $2000-3000 (and was not as easy to
  multiplex, so, probably needed increased labor costs too).

So my hot take answer is: we're not quite at the point where you can
generate scads of Nanopore data for the same cost as Illumina
(especially including handling & prep costs), but we're probably within
an order of magnitude in cost. Exciting!

But the likely medium-term answer is that we will need both kinds of
data for the foreseeable future: Nanopore to generate long contigs,
Illumina to get high quality base calls.

--titus
