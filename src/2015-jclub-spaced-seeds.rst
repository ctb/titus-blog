DIB jclub: Spaced Seed Data Structures for De Novo Assembly
===========================================================

:author: Camille Scott, Michael Crusoe, Jiarong Guo, Qingpeng Zhang, \C. Titus Brown
:tags: De Bruijn graphs, assembly
:date: 2015-05-27
:slug: 2015-jclub-spaced-seeds
:category: science

**Note:** at the `Lab for Data Intensive Biology
<http://ivory.idyll.org/lab/>`__, We're trying out a new journal club
format where we summarize our thoughts on the paper in a blog post.
For this blog post, Camille wrote the majority of the text and the
rest of us added questions and comments.

----

Inanç Birol, Justin Chu, Hamid Mohamadi, et al., “Spaced Seed Data
Structures for De Novo Assembly,” International Journal of Genomics,
Article ID 196591, in press.

The paper:

* URL: http://www.hindawi.com/journals/ijg/aa/196591/ref/

* `PDF download <http://scholar.google.com/scholar_url?url=http://downloads.hindawi.com/journals/ijg/aip/196591.pdf&hl=en&sa=X&scisig=AAGBfm3nVOYRe1p93foiJjWgq6T6UUWnJQ&nossl=1&oi=scholaralrt>`__

Some relevant background:

* `PathSet Paper <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3619201/pdf/cmb.2012.0098.pdf>`__
* `Spaced Seeds <http://bioinformatics.oxfordjournals.org/content/27/17/2433.full.pdf>`__

Summary
-------

The authors describe several data structures for integrating a special
case of spaced seeds into de Bruijn Graphs. Traditionally, a spaced
seed is a mask that's applied to an indexing sequence, increasing the
sensitivity of seeding approaches. For example, we could use 110110110
to mask out the 3rd base in each codon of our seed, thus allowing for
a wider range of matches given the high variability of that position
in protein coding regions. The special case here has the mask follow
the form 1..1..0..0..0..1..1, where the left and right pass regions
are k-mers, and the mask in the middle is of length Δ; or in other
words, given a region of length 2k+Δ, the seed comprises the prefix
and suffix k-mers.

Three data structures are introduced. The first is a naive hash table formulated in the same manner as the current ABySS implementation, which stores:

* The concatenated seeds as a bit string, represented with the notation [ k : k ]
* The extensions of both k-mers in the seed pair, stored as a 16-bit string
* Observation frequencies for the two strands of the seeds
* Bookkeeping junk

The second is a “spaced seeds bloom filter,” which as one might expect, stores the seeds in a bloom filter. The novelty here is the way they hash the seeds. Given a string of length 2k representing the concatenated k-mers of the seed, they hash:

* The left k-mer (i.e., the first k bases)
* The right k-mer (i.e., the last k bases)
* The string formed from pulling out every other base starting at position 0 (i.e., the “odd” bases)
* The string formed from pulling out every other base starting at position 1 (i.e., the “even” bases)
* For each of the four described values, they actually hash the XOR of the forward and revcomp’d 2-bit encodings

One immediately useful application of this method is in its ability to
infer the existence of single-base errors. For example, if we check a
seed and find that our filter already contains the “left” and “odd”
k-mers, but not the “right” and “even” ones, there’s a good chance
that our query seed just has a single base error in one of the “right”
and “even” positions (see Table 3 for complete listing).

Finally, they describe a “spaced seeds counting bloom filter” which,
you guessed it, stores seeds in a counting bloom filter. This is a
particularly nifty implementation, as it uses the minifloat standard
to exactly count up to 15, and probabilistically count values from
15-~128,000. They use the bloom filter to first count existence, and
then fall over to the counting filter when a seed is observed multiple
times. The usefulness of a better counting bloom filter should be
obvious to our group.

Broadly, we care about this because:

1. The seeding methodology allows for dBG’s to be scaled up to longer,
   error prone reads - a very important advancement to make if we want to
   dBG’s to continue to be relevant. The question remains as to whether
   we ought to be piling more and more duct tape on to dBG's to keep them
   in use.

2. The seeding also allows more accurate resolution of complex graph
   regions by retaining longer range correlations from within reads.

3. The aforementioned error identification. The hashing method allows
   one to quickly restrict the set of possible/likely erroneous k-mers in
   a read, which should speed up spectral error correction.

4. Generally, spaced seeds have better fault tolerance and uniqueness
   than long k-mers. Fig. 1 shows that spaced seeds of length 16 with
   Δ>100 have better uniqueness than k-mers of length 64, and are
   obviously less prone to single base errors because they are composed
   of less sequence.

Other notes
-----------

Interesting, they routinely use a k size of 120 when assembling 150 bp
reads.

The staged Bloom filter reminds us of the BFCounter implementation,
which uses exact counting for k-mers seen two or more times.

For Illumina reads (100 - 150 bp long), the middle part of each read
are ignored if delta is big like 100 bp. So, were the y axis in figure
1 changed to absolute number, unique 2k-mers should be much higher in
number than unique spaced seeds.

A generally question we have is which one is the most memory efficient
data structure for DBG, `sDBG
<http://alexbowe.com/succinct-debruijn-graphs/>`__ or bloom filters?

Spaced seeds let you take advantage of longer reads; the alternative,
using longer k, would reduce coverage dramatically, be sensitive to
errors as well, and consume more memory.

Confusions
----------

* The authors claim that this is better than the method used in the
  PathSet paper because spaced seeds “allow” for fixed distance
  between seed pairs. This is confusing to us, because the variable
  distance used in PathSet seems to be described as a *feature* — yet
  these authors posit that variable-distance seeds are sensitive to
  “read coverage fluctuations” for reasons. No justification was given
  for this statement.

* We don't see how spaced seeds are useful with the higher error rate of
  uncorrected long 'pore reads; granted the error correction for both
  nanopore and pacbio has gotten a lot better lately.

  More specifically, this seems targeted at long, erroneous
  reads. What effect do indels etc have from pac bio?  Do you need error
  corrected reads? If you have error corrected long reads aren't you
  already mostly done assembling and no longer need to use DBG?  And
  what's the effect of indels vs effect of high substitution, especially
  given the spaced seeds with fixed spacing?
