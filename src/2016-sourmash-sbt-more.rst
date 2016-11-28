Quickly searching all the microbial genomes, mark 2 - now with archaea, phage, fungi, and protists!
###################################################################################################

:author: C\. Titus Brown
:tags: minhash,sourmash,ddd, Bloom filters
:date: 2016-11-27
:slug: 2016-sourmash-sbt-more
:category: science

This is an update to last week's blog post, `"Efficiently searching
MinHash Sketch collections"
<http://ivory.idyll.org/blog/2016-sourmash-sbt.html>`__.

----

Last week, Thanksgiving travel and post-turkey somnolescence gave me
some time to work more with `our combined MinHash/SBT implementation
<http://ivory.idyll.org/blog/2016-sourmash-sbt.html>`__.  One of the main
things the last post contained was a collection of MinHash signatures of
all of the bacterial genomes, together with a Sequence Bloom Tree index
of them that enabled fast searching.

Working with the index from last week, a few problems emerged:

* I hadn't done all the microbes, just the bacteria!

* The MinHashes I'd calculated contained only the filenames of
  the genome assemblies, and didn't contain the name or accession
  numbers of the microbes.  This made them really annoying to use.

  (See the new ``--name-from-first`` argument to sourmash compute.)

* In my initial index calculation, I'd ignored non-bacterial
  microbes.  Conveniently my colleague Dr. Jiarong (Jaron) Guo had
  already downloaded the viral, archaeal, and protist genomes from
  NCBI for me.

* We guessed that we wanted more sensitive MinHash sketches for all the
  things, which would involve re-calculating the sketches with more
  hashes. (The default is 500, which gives you one hash per 10,000
  k-mers for a 5 Mbp genome.)

* We also decided that we wanted more k-mer sizes; the sourmash
  default is 31, which is pretty specific and could limit the
  sensitivity of genome search. k=21 would enable more sensitivity,
  k=51 would enable more stringency.

* I also came up with some simple ideas for using MinHash for taxonomy
  breakdown of metagenome samples, but I needed the number of k-mers
  in each hashed genome to do a good job of this. (More on this later.)

  (See the new ``--with-cardinality`` argument to sourmash compute.)

Unfortunately this meant I had to recalculate MinHashes for 52,000
genomes, and calculate them for 8,000 new genomes.  And it wasn't going
to take only 36 hours this time, because I was calculating approximately
6 times as much stuff...

Fortunately, 6 x 36 hrs *still* isn't very long, especially when
you're dealing with pleasantly parallel low-memory computations.  So I
set it up to run on Friday, and ran six processes at the same time,
and it finished in about 36 hours.

Indexing the MinHash signatures also took much longer than the first batch,
probably because the signature files were much larger and hence took longer
to load. For k=21, it took about 5 1/2 hours, and 6.5 GB of RAM, to index
the 60,000 signatures.  The end index -- which includes the signatures
themselves -- is around 3.2 GB for each k-mer size.
(Clearly if we're going to do this for the entire
SRA we'll have to optimize things a bit.)

On the search side, though, searching takes roughly the same amount of
time as before, because the *indexed* part of the signatures aren't
much larger, and the Bloom filter internal nodes are the same size as
before.  But we can now search at k=21, and get better named results
than before, too.

For example, go grab the Shewanella MR-1 genome::

  curl ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/165/GCF_000146165.2_ASM14616v2/GCF_000146165.2_ASM14616v2_genomic.fna.gz > shewanella.fna.gz

Next, convert it into a signature::

  sourmash compute -k 21,31 -f --name-from-first shewanella.fna.gz

and search! ::
  
  sourmash sbt_search -k 21 microbes shewanella.fna.gz.sig

This yields::
  
  # running sourmash subcommand: sbt_search
  1.00 NC_004347.2 Shewanella oneidensis MR-1 chromosome, complete genome
  0.16 NZ_JGVI01000001.1 Shewanella xiamenensis strain BC01 contig1, whole genome shotgun sequence
  0.16 NZ_LGYY01000235.1 Shewanella sp. Sh95 contig_1, whole genome shotgun sequence
  0.15 NZ_AKZL01000001.1 Shewanella sp. POL2 contig00001, whole genome shotgun sequence
  0.15 NZ_JTLE01000001.1 Shewanella sp. ZOR0012 L976_1, whole genome shotgun sequence
  0.09 NZ_AXZL01000001.1 Shewanella decolorationis S12 Contig1, whole genome shotgun sequence
  0.09 NC_008577.1 Shewanella sp. ANA-3 chromosome 1, complete sequence
  0.08 NC_008322.1 Shewanella sp. MR-7, complete genome

The updated MinHash signatures & indices are available!
-------------------------------------------------------

Our MinHash signature collection now contains:

1. 53865 bacteria genomes
2. 5463 viral genomes
3. 475 archaeal genomes
4. 177 fungal genomes
5. 72 protist genomes

for a total of 60,052 genomes.

You can download the various file collections here:

* All 60,052 genomic signatures: `microbe-sigs-2016-11-27.tar.gz <http://spacegraphcats.ucdavis.edu.s3.amazonaws.com/microbe-sigs-2016-11-27.tar.gz>`__  (1.4 GB)
* k=21 SBT index: `microbe-sbt-k21-2016-11-27.tar.gz <http://spacegraphcats.ucdavis.edu.s3.amazonaws.com/microbe-sbt-k21-2016-11-27.tar.gz>`__ - SBT name is 'microbes'. (1.4 GB)
* 

Hope these are useful!  If there are features you want, please go ahead
and `file an issue <https://github.com/dib-lab/sourmash/issues>`__; or,
post a comment below.

--titus

----

Index building cost for k=21::
  
   Command being timed: "/home/ubuntu/sourmash/sourmash sbt_index microbes -k 21 --traverse-directory microbe-sigs-2016-11-27/"
        User time (seconds): 18815.48
        System time (seconds): 80.81
        Percent of CPU this job got: 99%
        Elapsed (wall clock) time (h:mm:ss or m:ss): 5:15:09
        Average shared text size (kbytes): 0
        Average unshared data size (kbytes): 0
        Average stack size (kbytes): 0
        Average total size (kbytes): 0
        Maximum resident set size (kbytes): 6484264
        Average resident set size (kbytes): 0
        Major (requiring I/O) page faults: 7
        Minor (reclaiming a frame) page faults: 94887308
        Voluntary context switches: 5650
        Involuntary context switches: 27059
        Swaps: 0
        File system inputs: 150624
        File system outputs: 10366408
        Socket messages sent: 0
        Socket messages received: 0
        Signals delivered: 0
        Page size (bytes): 4096
        Exit status: 0

