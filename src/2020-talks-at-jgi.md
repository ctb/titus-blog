Title: Two talks at JGI in May: sourmash, spacegraphcats, and disease associations in the human microbiome.
Date: 2020-02-17
Category: science
Tags: sourmash, metagenomics, ibd, spacegraphcats
Slug: 2020-talks-at-jgi
Authors: C. Titus Brown
Summary: Using k-mers and taxonomy to find contamination in metagenomes

Hello all! I'm giving two metagenomics talks - a tech talk and a bio
talk - at the Joint Genome Institute on May 7, 2020. The abstracts are
below.

The JGI just moved to a new building at LBNL, so these talks are much
more accessible to the UC Berkeley and LBNL communities than they
would have been a year ago. I hope interested people can make it!

The talks will be in the afternoon on May 7th at the
[Integrative Genomics Building](https://www.lbl.gov/community/integrative-genomics-building/),
LBNL Bldg 91-310. I've put the tentative times down. I'll update this
post with final times and contact information for security + parking
passes closer to the day.

## Bio talk: Novel approaches to metagenome analysis reveal microbial signatures of IBD

(This will be the Science and Technology seminar, 3-4pm on May 7.)

Inflammatory bowel disease (IBD) is a spectrum of diseases
characterized by chronic inflammation of the intestines; it is likely
caused by host-mediated inflammatory responses at least in part
elicited by microorganisms. As of 2015, 1.3% of US adults have been
diagnosed with IBD. To date, although significant microbial
associations have been uncovered, no causative or consistent microbial
signature has been associated with IBD.

In a metaanalysis of six IBD cohorts comprising 2290 gut microbiome
shotgun metagenomes, we sought to uncover microbial signatures of
IBD. We developed a k-mer-based analysis approach based on sourmash
scaled signatures that comprehensively characterizes each metagenome
sample. We demonstrate that this approach explains substantial PCoA
variation across samples, and that patient, study, and diagnosis
account for the majority of variation. We then built an accurate
random forest classifier to predict IBD subtype. This classifier is
built on approximately 14,000 predictive k-mers and outperforms all
previously published work for characterization of IBD subtype. We next
sought to uncover the biological signal of the predictive k-mers. To
determine the origin of the predictive k-mers, we used sourmash gather
to search 400,000 microbial genomes from GenBank as well as recent
human metagenome reanalysis efforts.

We found that 69% of predictive k-mers were contained in 129 genomes,
many of which match known IBD correlates. We reasoned that many
additional predictive k-mers were likely in the pangenomes of these
129 predictive genomes, so we next used spacegraphcats to query
neighborhoods in compact de Bruijn graphs and extract sequences that
were near our predictive genomes in graph space. This increased the
annotated fraction of predictive k-mers to 85%.

This suggests that ~16% of predictive k-mers originate from
strain-variable or accessory components of pangenomes, and that this
variation is hidden from referenced-based approaches but is important
for determining IBD subtypes. Interestingly, the fraction of
predictive k-mers associated with the 129 genomes changed
substantially after spacegraphcats queries. For example, a genome from
the genus Bacteroides increased from owning 2.1% to 10.7% of
predictive k-mers, surpassing the genome that was most predictive
prior to spacegraphcats queries (Clostridiales bacterium, 2.9% to
7.4%). We are now working to bioinformatically characterize the genes
associated with the pangenomes.

Our pipeline is lightweight and open source, extensible to similar
comparative metagenomic studies, and has the potential to improve
diagnostic criteria for IBD subtype.

## Tech talk: No k-mer left behind.

(This is part of the Compute Next Generation talk series at JGI, 2-3pm
on May 7.)

Here at the DIB Lab @ UC Davis, we've developed and implemented a few
techniques that might be of interest to microbiology and metagenomics
computational researchers. In this tech talk, will dig into the theory
and implementation of our approaches, and discuss some of our current
and future use cases. While there may be some extreme speculation
involved, I will be sure to highlight it as such :).

The first technique is DensityHash, an extension and simplification of
the modulo hash technique proposed as an alternative to MinHash by
Broder (1997). Briefly, we massively downsample k-mers by intersecting
with a subset of hash space. This permits efficient and accurate
estimation of Jaccard similarity and containment on large sequencing
data sets. We have implemented this technique in sourmash
(github.com/dib-lab/sourmash), which offers a pleasant user experience
for comparing samples, searching large databases (e.g. all of
GenBank), estimating the composition of metagenomes, and discovering
contaminated MAGs, among others. We also have a taxonomic module that
slices and dices arbitrary taxonomies, and associates them with hashes
for fun and profit.

The second technique is neighborhood query into large compact De
Bruijn graphs, using dominating sets. Briefly, we implement a
practically efficient linear-time neighborhood clustering on
metagenome compact De Bruijn graphs, and then use this to query and
characterize neighborhoods. This is implemented in spacegraphcats
(github.com/spacegraphcats/spacegraphcats/). Spacegraphcats permits
recovery of accessory elements and strain variation from metagenomes,
for additional fun and profit.

All of our software is open source under the BSD license, developed
openly on GitHub, and implemented in a combination of Python and
Rust. We use automated tests, continuous integration, code coverage
analysis, and pull request review in our development processes.

References:

sourmash: [Pierce at al., 2019](https://f1000research.com/articles/8-1006)

spacegraphcats: [Brown et al., 2020](https://www.biorxiv.org/content/10.1101/462788v3)

----

Hope to see you there!

--titus
