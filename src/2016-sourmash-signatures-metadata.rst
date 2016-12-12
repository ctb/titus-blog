What metadata should we put in MinHash Sketch signatures?
#########################################################

:author: C\. Titus Brown
:tags: sourmash
:date: 2016-12-12
:slug: 2016-sourmash-signatures-metadata
:category: science

One of the uses that we are most interested in MinHash sketches for is
the indexing and search of large public, semi-public, and private
databases.  There are many specific use cases for this, but the basic
goal is to be able to find data sets by content queries, using
sequence as the "bait".  Think "find me data sets that overlap with my
metagenome", or "what should I co-assemble with?"  One particularly
interesting feature of MinHash sketches for this purpose is that you
`can provide indices on closed or private data sets without revealing
the actual data
<http://ivory.idyll.org/blog/2016-sourmash-signatures.html>`__ - while
I'd prefer that most data be open to all, I figure "findable" is at
least an advantage over the current situation.

As we start to plan the indexing of larger databases, a couple of
other features of MinHash sketches also start to become important.
One feature is that they are *very small*, and they are also *very
quick to search*.  For 60,000 microbial genomes the compressed data
set of sourmash sketches is under a few GB, and that's with an overly
verbose and unoptimized storage format.  These 60,000 genomes `can be
searched in under a few seconds and in less than a GB of RAM
<http://ivory.idyll.org/blog/2016-sourmash-sbt-more.html>`__; because
of the wonder of n-ary trees, it is unlikely that search of much
larger databases will be significantly slower.  A third feature (well
explored in `the mash paper
<http://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0997-x>`__)
is that MinHash sketches with large k are both very *specific* and
very *sensitive* to single genomes, in that you usually recover the
right match, and it is rare to recover irrelevant matches.

One consequence of the speed and small footprint of MinHash sketches
is that we can easily provide the individual sketches as well as the
aggregated Sequence Bloom Tree databases for download and use.
Another consequence is that people can search and filter on these
databases quite quickly and without a lot of hardware - pretty much
everything can be done on laptop-scale hardware.  Moreover the
sketches (once calculated) don't really need to be updated - the
sketch will change very little even if an assembly is updated.  So
while people might be interested in building custom MinHash databases
for searching subsets of archives, it seems reasonable to maintain a
single database of *all the sketches* that can be downloaded and searched
by anyone.

This opinion informed my response to Michael Barton, who is interested
in `building custom databases for several reasons
<https://github.com/marbl/Mash/issues/27#issuecomment-266089271>`__ -
my guess is that this will be a somewhat specialized (though perhaps
reasonably frequent) use case, compared to simply downloading and using
a pre-constructed database.  More important to me is the
interoperability of different tools, which basically boils down to
choosing the same hash functions and (eventually) figuring out what
k-mer size and number of MinHash values to store per data.

Something that I'm more focused on at the moment is *another* question
`that Michael asked
<http://ivory.idyll.org/blog/2016-sourmash-sbt-more.html#comment-3044395517>`__,
which is about metadata.  Right now our individual signature files can
contain multiple sketches per sample, with different k-mer sizes and
molecule types (DNA/protein).  These are kept in YAML.  Because of
this, the format is easily extensible to include a variety of
metadata, but I have put very little thought into what metadata to
store.

Thinking out loud,

* there will be a few pieces of metadata that every sketch should have;
  for public data, for example, the URL and an unambiguous database
  specific identifier should be there.

* each source database will have its own metadata records; if we index
  data sets from the Assembly database at NCBI, there will be
  different fields available than from the SRA database at NCBI, vs
  the MG-RAST metagenome collection, vs the IMG/M database.  I'm not
  aware of any metadata standards here (but I wouldn't know, either).

  This means that trying to come up with a single standard is an
  idea that is doomed to fail.

* we should try to include enough information that there is something
  human readable and useful, if possible;

* I'm not sure how much information we need to include beyond database
  identity and database record ID; it seems like dipping our toes into
  (e.g.) taxonomy and phylogeny would be a dangerous game, and that
  information could be pulled out of the databases for whatever
  specific use case.

* I'm comfortable with the idea of a developing out the details over
  time as we add new data sets, and perhaps updating old records with
  more complete metadata as we develop new use cases and more robust
  handling code.

Some examples
-------------

For example, looking at `Shewanella oneidensis MR-1 <https://www.ncbi.nlm.nih.gov/assembly/GCF_000146165.2>`__, the assembly record has the following info::

   ASM14616v2
   Organism name: Shewanella oneidensis MR-1 (g-proteobacteria)
   Infraspecific name: Strain: MR-1
   BioSample: SAMN02604014
   Submitter: TIGR
   Date: 2012/11/02
   Assembly level: Complete Genome
   Genome representation: full
   RefSeq category: reference genome
   Relation to type material: assembly from type material
   GenBank assembly accession: GCA_000146165.2 (latest)
   RefSeq assembly accession: GCF_000146165.2 (latest)
   RefSeq assembly and GenBank assembly identical: yes

Clearly we want to store 'organism name' and probably the strain, and
the accession information; and we probably want to include assembly
level and genome representation.  I'd probably also add the URL to
download the .fna.gz file. But I don't think we want statistics
(included at the bottom of the page), or any of the other information
on `the Genome page <https://www.ncbi.nlm.nih.gov/genome/?term=txid70863[orgn]>`__, because we'd end up having to update that regularly for many samples.

----

Looking at `the SRA record for a metagenome from Hu et al., 2016 <http://www.ebi.ac.uk/ena/data/view/SRX997544>`__, I'd probably want to include:

* the fact that it is metagenomic FASTQ;
* the description at the top "Illumina MiSeq paired end sequencing; metagenome SB1 from not soured petroleum reservoir, Schrader bluffer formation, Alaska North Slope"
* whatever error trimming/correction commands I used before minhashing it;
* a link to the ENA FASTQ files for download;

and that's about it.

----

Other records would presumably vary in similar ways, ranging from
really minimal information ("this kind of sample, this kind of
sequencing, have fun") to much more fleshed out metadata.

Your thoughts on how to go about this?

--titus
