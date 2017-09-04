Title: Comparing genome sets extracted from metagenomes (Sunday Morning Bioinformatics).
Date: 2017-09-03
Category: science
Tags: bioinformatics, tara, minhash, ngs, metagenomics, smb
Slug: 2017-comparing-genomes-from-metagenomes
Authors: C. Titus Brown
Summary: Two different binning procedures, on different data, produce somewhat different bins. Duh.

(Because I'm a nerd who loves my research, I frequently do short-form bioinformatics analyses on weekends. I may start posting more of them.  But an important note is that these will necessarily be incomplete and speculative because I put a hard limit on the time spent doing them - e.g. the below excursion took me about 2.5 hours total, starting from having the signatures calculated. Most of the 2 hours was before the kids woke up :)

----

I’ve been watching the metagenome-assembled genomics community for a while with some envy.  The lure of extracting single genomes from the messy complex mixture of stuff in a metagenome is seductive! But the environment with which I have the most experience, agricultural soil, doesn’t lend itself to this process (because coverage is almost always too low, and complexity is too high), so I've been relegated to the sidelines (<sob>).

I've also been a bit wary of binning. First, almost all binning approaches operate post-assembly, and I generally think all metagenome assemblies are wrong (although of course some are useful!) Second, many binning approaches involve examining the clusters and applying cutoffs chosen by eyeball, which lends a potential degree of variability to things that I'm concerned by. And third, we just posted [a paper](http://www.biorxiv.org/content/early/2017/07/03/155358) suggesting that strain variation (which is almost certainly present to massive degree in any sufficiently deep sequencing data) really gets in the way of metagenome assembly. This suggests that most metagenome assemblies are going to be somewhat incomplete.

But I'm always happy to take advantage of other people's work and so I've been on the lookout for good binned data sets to play with.
   
Conveniently, two different groups recently applied their binning approaches to the Tara ocean data set ([Sunagawa et al., 2015](https://www.ncbi.nlm.nih.gov/pubmed/25999513)), and I thought I'd take the opportunity to compare 'em.  While a comparison won't necessarily say anything about the completeness of the binning, it might help characterize variability in the approaches.

The two approaches were posted to bioRxiv as [Tully et al., 2017](http://www.biorxiv.org/content/early/2017/07/13/162503) and [Delmont et al., 2017](http://www.biorxiv.org/content/early/2017/04/23/129791). Below, I will refer to them as 'Tully' and 'Delmont'.

## Tara Oceans: the bacterial fraction

(These stats are mostly taken from Tully et al., 2017)

Tara Oceans generated metagenomic sequencing data from 234 samples, size-filtered to enrich for "prokaryotic" (bacterial + archaeal) organisms.  This ended up being a ~terabase data set containing 102 billion paired-end reads.

## The Tully data

Tully et al. produced 2631 genomes, and estimated that  1491 were more than 70% complete and 603 were more than 90% complete. (Wow!)

The process used was (roughly) as follows --

1. Assemble each of 234 samples with MEGAHIT, yielding 562m contigs.
2. After length filtering the contigs at 2kb, use CD-HIT to eliminate contigs that are more than 99% similar.
3. Co-assemble contigs from each of the 61 stations (geographical locations) with MINIMUS2, yielding 7.2m contigs.
4. Apply BinSanity to cluster these contigs into genome bins, and use CheckM to evaluate completeness.

## The Delmont data

Delmont et al. produced 957 genomes from 93 samples (presumably a subset of the 234 samples above?), using this [very well documented approach](http://merenlab.org/data/2017_Delmont_et_al_HBDs/) - briefly,

1. Co-assemble samples from 12 geographical regions with MEGAHIT.
2. Bin results with CONCOCT.
3. Manually refine CONCOCT results using a'n'vio'.
4. Extract bins with > 70% completion or 2 Mbp of contigs into 1077 genome bins.
5. Collapse redundant genomes from across the different regions into 957 bins based on average nucleotide identity (> 98% ANI).

## Some initial thoughts

Quite different approaches were taken here: in particular, Tully et al. assembled each of 234 samples individually, then co-assembled the resulting assembly by each of 61 stations; while Delmont et al. divided 93 samples into 12 based on geographical location, and co-assembled those 12.

Both studies used MEGAHIT to assemble the primary contigs.  It would be interesting to compare these initial assemblies directly, as this would place  bounds on the similarity of the eventual binning outcomes.

## Getting to the data

I downloaded both full sets of binned genomes, and then ran the following [sourmash](https://github.com/dib-lab/sourmash/) command to compute sourmash signatures from the data:

```
sourmash compute -k 21,31,51 \
                         --scaled 2000 \
                         --track-abundance
```

This took about an hour for the Tully collection, and less for the Delmont collection.

You can download the data sets from [the Open Science Framework](https://osf.io/9876b/) if you'd like to follow along --

```
curl -L https://osf.io/vngdz/download -o delmont-genome-sigs.tar.gz
curl -L https://osf.io/28r6m/download -o tully-genome-sigs.tar.gz
```

The first file is about 30 MB, the second file is about 90 MB.

I then unpacked the two collections on my laptop,

```
tar xzf delmont-genome-sigs.tar.gz 
tar xzf tully-genome-sigs.tar.gz 
```

and built search trees (SBTs) for each of them at k=31 --

```
sourmash index -k 31 delmont31 --traverse-directory delmont-genome-sigs
sourmash index -k 31 tully31 --traverse-directory tully-genome-sigs
```

## Comparing binned genomes directly

I wrote a [custom script](https://github.com/ctb/2017-tara-binning/blob/master/compare-two-directories.py) that computed matches between genomes in one directory vs genomes in the other directory.

Here, 'similarity' is Jaccard similarity, 'identity' is more than 80% Jaccard similarity, and 'containment' is more than 95% of a genome's signature included in the other.

```
% ./compare-two-directories.py delmont-genome-sigs delmont31.sbt.json tully-genome-sigs tully31.sbt.json 
```

After lots of detailed output, you get the following summary:
```
thresholds:
min Jaccard similarity for any match: 0.05
to score as identical, similarity must be >= 0.8
to score as contained, containment must be >= 0.95
----
delmont-genome-sigs vs tully-genome-sigs: 957 signatures
identical count: 22
containment count: 66
matches: 591
no match: 366
no contain: 891
----
tully-genome-sigs vs delmont-genome-sigs: 2631 signatures
identical count: 27
containment count: 54
matches: 850
no match: 1781
no contain: 2577
```

Some initial thoughts here:

* the tully genomes probably have more "redundancy" in this context because of the way Delmont et al. removed redundancy.
* the data sets are strikingly different!

## Getting overall stats for overlap/disjointness

After all this, I got to wondering about the overall similarity of the genomes.  So, I wrote [another custom script](https://github.com/ctb/2017-tara-binning/blob/master/compare-two-directories-hashvals.py), `compare-two-directories-hashvals.py`, to compare the k-mer composition of tully and delmont directly.  (For those of you familiar with MinHash, no, you cannot do this normally based on MinHash signatures; but we're using super-special opensauce in sourmash that lets us do this. Trust us.)

```
% ./compare-two-directories-hashvals.py delmont-genome-sigs tully-genome-sigs 
loading all signatures: delmont-genome-sigs
loading from cache: delmont-genome-sigs.pickle
...loaded 957 signatures at k=31
loading all signatures: tully-genome-sigs
loading from cache: tully-genome-sigs.pickle
...loaded 2631 signatures at k=31
total hashvals: 2837161
both: 17.2%
unique to delmont-genome-sigs: 22.1%
unique to tully-genome-sigs: 60.7%
```

Here we estimate that the binned genomes, in aggregate, share about 17.2% of the union, while Delmont et al. has about 22.1% of the unique content, and Tully has about 60.7% of the unique content.

This is probably largely due to the extra data that was taken into account by Tully et al. (234 samples in tully vs 93 samples in delmont.)

It is reassuring that some genomes (~20) are identical between the data sets, albeit at a low threshold of 80%; and that some genomes from one are mostly contained in bins from the other (~50-60 in each direction).

## Concluding thoughts

It is not surprising that two different binning procedures run on different
subsamples produce different results :).

I must admit that it is not immediately obvious to me  where I go from here. What stats or distributions should I be looking at? How do people compare the output of different binning procedures when they're working on the same samples?  Thoughts welcome!

If you want to play with the data yourself, you should be able to repeat my entire analysis on your own laptop in ~30 minutes, starting from [a basic sourmash install](https://sourmash.readthedocs.io/en/latest/tutorials.html) and using the commands above.  You'll need to clone [the repo](https://github.com/ctb/2017-tara-binning), of course.

--titus
