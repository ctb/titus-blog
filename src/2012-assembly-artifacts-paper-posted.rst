Assembly artifacts paper posted
###############################

:author: C\. Titus Brown
:tags: ngs,python,assembly
:date: 2012-12-1
:slug: 2012-assembly-artifacts-paper-posted
:category: science


We just posted another pre-submission paper to arXiv.org:

**Illumina Sequencing Artifacts Revealed by Connectivity Analysis of Metagenomic Datasets**

Authors: Adina Chuang Howe, Jason Pell, Rosangela Canino-Koning, Rachel
Mackelprang, Susannah Tringe, Janet Jansson, James M. Tiedje, and C.
Titus Brown

`arXiv link <http://arxiv.org/abs/1212.0159>`__

`Paper repository on github <https://github.com/ged-lab/2012-assembly-artifacts>`__

Abstract:

   Sequencing errors and biases in metagenomic datasets affect
   coverage-based assemblies and are often ignored during
   analysis. Here, we analyze read connectivity in metagenomes and
   identify the presence of problematic and likely a-biological
   connectivity within metagenome assembly graphs. Specifically, we
   identify highly connected sequences which join a large proportion
   of reads within each real metagenome. These sequences show
   position-specific bias in shotgun reads, suggestive of sequencing
   artifacts, and are only minimally incorporated into contigs by
   assembly. The removal of these sequences prior to assembly results
   in similar assembly content for most metagenomes and enables the
   use of graph partitioning to decrease assembly memory and time
   requirements.

---

This paper extends our `partitioning paper (Pell et al, PNAS, 2012)
<http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__ and
describes the effect of removing sequencing artifacts and highly
conserved sequences from read data sets prior to partitioning large
environmental metagenomes.

More anon...

--titus
