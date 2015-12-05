jclub: Bloom Filter Trie - a data structure for pan-genome storage 
##################################################################

:author: Sherine Awad, Lisa Cohen, Jiarong Guo, and C. Titus Brown
:tags: bloom filters, data structures, De Bruijn graphs, jclub
:date: 2015-07-27
:slug: 2015-jclub-bloom-filter-trie
:category: science

**Note:** this is a blog post from the `DIB Lab
<http://ivory.idyll.org/lab/>`__ journal club.

Jump to `Questions and Comments:`_.

----

The paper:

http://www.techfak.uni-bielefeld.de/~stoye/dropbox/wabi2015final.pdf

"Bloom Filter Trie: a data structure for pan-genome storage."

by Guillaume Holley, Roland Wittler, and Jens Stoye.

Background 
===========

- Pan Genome: Represents genes in a clade that comprises
  hundreds/thousands of strains that share large sequence parts but
  differ by individual mutations from one another.

- Colored De Bruijn Graph (C-DBG) - A directed graph where each vertex
  represents a kmer and is associated with a color that represents the
  genome where the kmer occurs.  An edge between vertex x and vertex y
  exists if x[2..k] = y[1..k-1]

Existing pan-genome Data structures
-----------------------------------

- Burrows-Wheeler Transform (BWT) that rearranges the input data to
  enable better compression by aggregating characters with similar
  context.

- FM-Index count and locate the occurrence of substring in BWT.

- Bloom Filter BF - A bit array of n elements initialized with zeros,
  and it uses a set of hash functions for look-up and insertion in a
  constant time.

- Sequence Bloom Filter (SBT) is a binary tree with BFs as vertices.
  A query sequence is broken into a set of kmers then checked if they
  exist in the vertex bloom filter. If yes, search is repeated on
  children if not existing the proceeds on other vertices.
 

Paper Scope: New pan-genome Data Structure 
===========================================

Proposes a new data structure for indexing and compressing a
pan-genome as a C-DBG, the Bloom Filter Trie (BFT). The trie stores
kmers and their colors. The new representation allows for compressing
and indexing shared substrings.  It also allows quick checking for the
existence of a given substring. It is incremental, alignment and
reference free, and allows for any format.

How BFT Works? 
==============

Colors Representation Before Compression 
----------------------------------------

Colors are represented by a bit array initialized with 0s.  Each color
has an index i_color: color_x [i_color] =1 means kmer x has color
i_color.


Colors Representation After Compression 
---------------------------------------

If we can put each color set in a specific position in an array such
that this position encodes into a number less than the color set size,
then we can store the color set in the BFT using less space.  Color
set size is the number of kmers sharing a color multiplied by its
size. So basically, they sort colors in a list based on the color set
size in a decreasing order then they add each color set to an external
array incrementally (if : integer encoding the position of the color in
the array < size of the color). Finally, each color is replaced in the
BFT by its position in the external array

Uncompressed Container 
-----------------------

A set of tuples of capacity ``c <s, color_ps>`` where:
``x = ps`` and ``x is the path from root to v``.

When number of suffixes exceeds c the container is burst. 

In bursting process, each suffix s is split into a suffix s_suff and prefix s_pref

Prefixes are stored in a new compressed container.  

Suffixes and their colors are stored in a new uncompressed containers.
 
Compressed Container and  Bursting Procedure
----------------------------------------------

An uncompressed container is replaced by a compressed one that stores
q prefixes of suffix with links to children containing the suffix.

- quer is a BF represented as m bit array and has f hash functions to
  record and filter the presence of q prefixes of suffix.

- The q prefixes of suffix are stored in a bloom filter BF.  q
  suffixes are stored in an array suf in lexicographic order of the
  prefixes of those suffixes.

- pref[𝛂] =1 if a prefix a exists with 𝛂 as its binary representation.

- clust is an array of q bits one per suffix of array suf. A cluster is a list of consecutive suffixes in array suf that has the same prefix. 


BFT Operations 
==============

Look up 
-------

To check if a Spref ab with 𝛂𝜷 representation exist in a compressed
container cc, the BF quer is checked and the prefix a existence is
verified in the array pref. Remember that suffix prefixes are stored
in quer during bursting process.

if a exist, then its hamming weight is computed which is the index of
the cluster in which suffix b is likely located where i is the start
position of the cluster. Remember that a cluster is a list of
consecutive suffixes that has the same prefix, so b is compared to
suffixes in that cluster.

To check of a kmer x exists in a BFT t, the look-up process traverses
t and for each vertex v it checks its containers one after
one. Remember that suffix and their colors are stored in uncompressed
container during burst process, hence a vertex now either represent a
suffix from an uncompressed container or a suffix rooted from its
compressed container.

- For the first case, and as the uncompressed container has no childs,
  a match indicates the presence of the kmer.

- For the second case, the quer is checked for the x_suff[1..l]. If it
  is found, traverse is continued recursively to the corresponding
  children.  The absence of of x_suff[1..l] means the absence of the kmer
  as it can’t be located in another container of vertex v.  Remember
  that k is a multiple of l so kmer =k/l equal substrings.

Insertion
----------

If the kmer already exist, its set of colors is only
modified. Otherwise, a lookup process is continued till:

* The prefix of the searched suffix does not exist
* The  kmer suffix does not exist 

Then the kmer is inserted. Insertion is simple if the container is
uncompressed.  If the container is compressed, the insertion of of
s_pref =ab is pretty complicated:

Remember in the look up process, the ‘a’ prefix existence is verified
by checking pref array.  If it does not exist: it is a FP, and we can
insert now by setting pref[𝛂] to 1. So, in next look up, the
verification will lead to a TP index and start position of cluster pos
are recomputed and updated. How?  if it does exist: Then the suffix b
is to be inserted into suf[pos]

Evaluation
============ 

Experiments presented in the paper show that BFT is faster than SBT
while utilizing less memory.

- KmerGenie was used to get optimal k size and mininal kmer count

- Data insertion (loading) and kmer query was compared between SBT and
  BFT. Traversal time is also evaluated on BFT.

- BFT was multiple times faster than the SBT on the building time
  while using about 1.5 times less memory. The BFT was about 30 times
  faster than the SBT for querying a k-mer.

Questions and Comments:
=======================

- Essentially, a nice fast data structure for querying for k-mers and
  retrieving their colors.  I guess this is for pangenomes, among
  other things.

- They essentially use compressed nodes in the tree to efficiently
  store prefixes for large sections of the tree.

- We worry about the peak mem usage diagram. It seems like a fair
  amount of memory is used in the making.  How does this compare to
  the SBT? Do they compare peak memory usage or merely compressed
  memory usage?

- It seems like one advantage that the SBT has is that with the BFT
  you cannot store/query for presence in individual data sets.  So,
  for example, if you wanted to build indices for data sets spread
  across many different machines, you would have to do it by gathering
  all of the data sets in one place.

- Both SBT and BFT get the compression mainly from bloom filter. The
  author did not discuss about why there is difference in compression
  ratio. Bloom filter size? The FP rate of bloom filters in used in
  SBT was mentioned as 7.2%, but FP rate of bloom filters in BFT were
  not mentioned in paper.

- Another catch in the evaluation is that 1) loading cpu time
  difference in Table 1 of SBT and BFT may be from kmer counting
  (Jellyfish vs. CMK2); 2) When comparing the unique kmer query time,
  unique kmer were divided into subsets due to memory limit. Not sure
  whether this was a fair comparison.

- How does false positive rate of all bloom filters (on all nodes)
  affect overall error rate, e.g. If BFT is converted back to k-mers,
  how many sequence error are there? (None, we think)

- PanCake (alignment based) and RCSI (Reference based) were mentioned
  but not included in evaluation, which gave us the impression that
  they are not as efficient. Do they have any advantage?

- BFT or SBT vs. khmer? (mentioned in intro but not discussed)

- Pan genome (and transcriptome, proteome!) storage is super
  cool. (might not be relevant question here, but I am wondering:) How
  are genomes defined as "highly similar", as the authors restricted
  their test data sets to. At what point do species diverge to become
  too distant to analyze in this manner? e.g. how close is close, and
  what is too far?

  (CTB answer: it has something to do with how many k-mers they share,
  but I don't know that this has been really quantified.  Kostas
  Konstantinidis et al's latest work on species defn might be good
  reading
  (http://nar.oxfordjournals.org/content/early/2015/07/06/nar.gkv657.full)
  as well as his Average Nucleotide Identity metric.)

- Wondering how might BFT scale? Authors only tested prokaryotic
  sequences, 473 clinical isolates of Pseudomonas aeruginosa from 34
  patients = 844.37 GB. Simulated data were 6 million reads of 100 b
  length for 31 GB. In comparison, MMETSP data are transcriptomic data
  from 678 cultured samples of 306 marine eukaryotic species
  representing more than 40 phyla (see Figure 2, Keeling et al. 2014)
  Not sure how large the entire MMETSP data set is, but probably on
  order of TB?
  http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889
  http://www.ncbi.nlm.nih.gov/nuccore?term=231566%5BBioProject%5D

- Although they discussed SBT as existing data structure, and
  graphalign in khmer, it wasn't clear until end that one of the main
  goals of the paper, besides describing BFT, was to compare their BFT
  to SBT (Soloman and Kingsford 2015
  http://biorxiv.org/content/biorxiv/early/2015/03/26/017087.full.pdf)
  I feel this should have been noted in the Abstract.

- speed can partly come from being able to abort searches for k-mers partway
  through.

- BFT is really specialized for the pangenome situation, where many k-mers are
  in common. The cluster approach will break down if the genomes aren't mostly
  the same?

- we would have liked a more visual representation of the data structure
  to help build intuition.

Points for clarification or discussion:
=======================================

-  c is defined as capacity, but this is not well-described. What is capacity? 

-  BFT to khmer graphalign comparison? 
