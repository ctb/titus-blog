Paper draft: Scaling metagenome sequence assembly with probabilistic de Bruijn graphs
#####################################################################################

:author: C\. Titus Brown
:tags: ngs,kmers,bioinformatics,metagenomics
:date: 2011-12-20
:slug: kmer-percolation-posted
:category: science


(updated to point to http://arxiv.org/).

Authors: Jason Pell, Arend Hintze, Rosangela Canino-Koning, Adina Howe, James M. Tiedje, C. Titus Brown

Abstract:

    The memory requirements for de novo assembly of short-read shotgun
    sequencing data from complex microbial populations are an
    increasingly large practical barrier to environmental
    studies. Here we introduce a memory-efficient graph representation
    with which we can analyze the k-mer connectivity of metagenomic
    samples, allowing us to reduce the size of the de novo assembly
    process for metagenomes with a "divide and conquer"
    algorithm. This graph representation is based on a probabilistic
    data structure, a Bloom filter, that allows us to store assembly
    graphs in as little as 4 bits per k-mer. We use this approach to
    achieve a 20-fold decrease in memory for the assembly of a soil
    metagenome sample.

The paper is available on arXiv here: http://arxiv.org/abs/1112.4193.
Comments are welcome!  We're planning to submit it to PNAS later this
week.

I'll write a longer blog post about it soon.

--titus
