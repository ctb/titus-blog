Categorizing 400,000 microbial genome shotgun data sets from the SRA
####################################################################

:author: C\. Titus Brown
:tags: minhash,sourmash,ddd,sra
:date: 2017-01-18
:slug: 2017-sourmash-sra-microbial-wgs
:category: science

This is another blog post on MinHash sketches; see also:

    * `Applying MinHash to cluster RNAseq samples <http://ivory.idyll.org/blog/2016-sourmash.html>`__
    * `MinHash signatures as ways to find samples, and collaborators? <http://ivory.idyll.org/blog/2016-sourmash-signatures.html>`__
    * `Efficiently searching MinHash Sketch collections <http://ivory.idyll.org/blog/2016-sourmash-sbt.html>`__
    * `Quickly searching all the microbial genomes, mark 2 - now with archaea, phage, fungi, and protists! <http://ivory.idyll.org/blog/2016-sourmash-sbt-more.html>`__
    * `What metadata should we put in MinHash Sketch signatures? <http://ivory.idyll.org/blog/2016-sourmash-signatures-metadata.html>`__

----

A few months ago I was at the Woods Hole MBL `Microbial Diversity
course <http://ivory.idyll.org/blog/2016-summer-vacation.html>`__, and
I ran across Mihai Pop, who was teaching at the STAMPS Microbial
Ecology course.  Mihai is an old friend who shares my interest in
microbial genomes and assembly and other such stuff, and during our
conversation he pointed out that there were many unassembled microbial
genomes sitting in the `Sequence Read Archive
<https://www.ncbi.nlm.nih.gov/sra>`__.

The NCBI Sequence Read Archive is one of the primary archives for
biological sequencing data, but it generally holds only the raw
sequencing data; assemblies and analysis products go elsewhere.  It's
also largely unsearchable by sequence: you can search an individual
data set with BLAST, I think, but you can't search multiple data sets
(because each data set is large, and the search functionality to
handle it doesn't really exist).  There have been some attempts to
make it searchable, including most notably `Brad Solomon and Carl
Kingsford's Sequence Bloom Tree paper
<http://www.nature.com/nbt/journal/v34/n3/full/nbt.3442.html>`__ (also
on `biorxiv <http://biorxiv.org/content/early/2015/03/26/017087>`__,
and see `my review
<http://ivory.idyll.org/blog/2015-review-bloomtree.html>`__), but it's
still not straightforward.

Back to Mihai - Mihai told me that there were several hundred thousand
microbial WGS samples in the SRA for which assemblies were not readily
available.  That got me kind of interested, and -- combined with
`my interest in indexing all the microbial genomes for MinHash searching <http://ivory.idyll.org/blog/2016-sourmash-sbt-more.html>`__ -- led to... well,
read on!

How do you dance lightly across the surface of 400,000 data sets?
-----------------------------------------------------------------

tl;dr? We're sipping from the beginning of each SRA data set only.

The main problem we faced in looking at the SRA is that whole genome
shotgun data sets are individually rather large (typically at least
500 MB to 1 GB), and we have no special access to the SRA, so we were
looking at a 200-400 PB download.  Luiz Irber found that NCBI seems to
throttle downloads to about 100 Mbps, so we calculated that grabbing
the 400k samples would significantly extend his PhD.

But, not only is the data volume quite large, the samples themselves
are mildly problematic: they're not assembled or error trimmed, so we
had to develop a way to error trim them in order to minimize spurious
k-mer presence.

We tackled these problems in several ways:

* Luiz implemented a distributed system to grab SRA samples and compute MinHash sketch signatures on them with sourmash; he then ran this 50x across Rackspace, Google Compute Engine, and the MSU High Performance Compute cluster `(see blog post) <http://blog.luizirber.org/2016/12/28/soursigs-arch-1/>`__;

  To quote, "Just to keep track: we are posting Celery tasks from a
  Rackspace server to Amazon SQS, running workers inside Docker
  managed by Kubernetes on GCP, putting results on Amazon S3 and
  finally reading the results on Rackspace and then posting it to
  IPFS."

  This meant we were no longer dependent on a single node, or even on
  a single compute solution. w00t!

* We needed a way to quickly and efficiently error trim the WGS samples.
  In MinHash land, this means walking through reads and finding "true"
  k-mers based on their abundance in the read data set.
  
  Now, thanks to `khmer <https://khmer.readthedocs.io>`__, we have ways
  of doing this on a low-memory streaming basis, so we started with that
  (using ``trim-low-abund.py``).

* Because whole-genome shotgun data is generally pretty high coverage,
  we guessed that we could get away with computing signatures on only
  a small subset of the data.  After all, if you have 100x coverage
  sample, and you only need 5x coverage to build a MinHash signature,
  then you only need to look at 5% of the data!

  The ``fastq-dump`` program has a streaming output mode, and both
  khmer and sourmash support streaming I/O, so we could do all this
  computing progressively.  The question was, how do we know when to
  stop?

  Our first attempt `was to grab the first million reads from each
  sample, and then abundance-trim them, and MinHash them
  <https://github.com/dib-lab/soursigs/blob/master/soursigs/tasks.py#L16>`__.
  Luiz calculated that (with about 50 workers going over the holiday break)
  this would take about 3 weeks to run on the 400,000 samples.

  Fortunately, due to a bug in my categorization code, we thought that
  this approach wasn't working.  I say "fortunately" because in attempting
  to fix the wrong problem, we came across a much better solution :).

  For mark 2 of streaming, some basic experimentation suggested that
  we could get a decent match when searching a sample against known
  microbial genomes with only about 20% of the genome.  For E. coli,
  this is about 1m bases, which is about 1m k-mers.

  So I whipped together a program called `syrah
  <https://github.com/dib-lab/syrah>`__ that reads FASTA/FASTQ
  sequences and outputs high-abundance regions of the sequences until
  it has seen 1m k-mers.  Then it exits, terminating the stream.

  This is nice and simple to use with fastq-dump and sourmash -- ::

     fastq-dump -A {sra_id} -Z | syrah | \
        sourmash compute -k 21 --dna - -o {output} --name {sra_id}

  and when Luiz tested it out we found that it was 3-4x faster than
  our previous approach.  `(See the final command here.)
  <https://github.com/dib-lab/soursigs/blob/master/soursigs/tasks.py#L40>`__

At this point we were down to an estimated 5 days for computing about
400,000 sourmash signatures on the microbial genomes section of the SRA.
That was fast enough even for grad students in a hurry :).

Categorizing 400,000 sourmash signatures... quickly!
----------------------------------------------------

tl; dr? We sped up the sourmash Sequence Bloom Tree search functionality, like, a lot.

Now we had the signatures! Done, right?  We just categorize 'em all! How long can that take!?

Well, no.  It turns out when operating at this scale even the small things
take too much time!

We knew from browsing the SRA metadata that most of the samples were
likely to be strain variants of human pathogens, which are very well
represented in the microbial RefSeq.  Conveniently, `we already had
prepared those for search
<http://ivory.idyll.org/blog/2016-sourmash-sbt-more.html>`__. So my
initial approach to looking at the signatures was to compare them to
the 52,000 microbial RefSeq genomes, and screen out those that could
be identified at k=21 as something known.  This would leave us with the
cool and interesting unknown/unidentifiable SRA samples.

I implemented a new sourmash subcommand, ``categorize``, that took in
a list (or a directory) full of sourmash signatures and searched them
individually against a Sequence Bloom Tree of signatures.  The output
was a CSV file of categorized signatures, with each entry containing
the best match to a given signature against the entire SBT.

It worked great! It took about 1-3 seconds per genome.  For 400,000
signatures that would take... 14 days.  Sigh.  Even if we parallelized
that it was annoyingly slow.

So I dug into the source code and found that the problem was our YAML
signature format, which was `slow as a dog <https://github.com/dib-lab/sourmash/issues/70>`__.  When searching the SBT, each leaf node was stored in YAML
and loading this was consuming something like 80% of the time.

My first solution was to `cache all the signatures <https://github.com/dib-lab/sourmash/pull/94>`__, which worked great but consumed about a GB of RAM.
Now we could search each signature in about half a second.

In the meantime, Laurent Gautier had discovered the same problem in
his work and he came along and `reimplemented signature storage in
JSON <https://github.com/dib-lab/sourmash/pull/71>`__, which was
10-20x faster and was a way better permanent solution.  So now we have
JSON as the default sourmash signature format, huzzah!

At this point I could categorize about 200,000 signatures in 1 day on
an AWS m4.xlarge, when running 8 categorize tasks in parallel (on a
single machine).  That was fast enough for me.

It's worth noting that we explicitly opted for separating the
signature creation from the categorization, because (a) the signatures
themselves are valuable, and (b) we were sure the signature generation
code was reasonably bug free but we didn't know how much iteration we
would have to do on the categorization code.  If you're interested in
calculating and categorizing signatures directly from streaming FASTQ,
see ``sourmash watch``.  But Buyer Beware ;).

Results! What are the results?!
-------------------------------

For 361,077 SRA samples, we cannot identify 8707 against the 52,000
RefSeq microbial genomes.  That's about 2.4%.

From the 8707, I randomly chose and downloaded 34 entire samples.  I
ran them all through the MEGAHIT assembler, and 27 of them assembled
(the rest looked like PacBio, which MEGAHIT doesn't assemble).  Of the
27, 20 could not be identified against the RefSeq genomes.  This
suggests that about 60% of the 8707 samples are samples that are (a)
Illumina sequence, (b) assemble-able, and (c) not identifiable.

You can download the signatures @@here.

You can get the CSV of categorized samples `here <https://s3-us-west-1.amazonaws.com/spacegraphcats.ucdavis.edu/sra-bacteria-wgs-360k.categories.csv.gz>`__ (it's about 5 MB, .csv.gz).

What next?
----------

Well, there are a few directions --

* we have about 350,000 SRA samples identified based on sequence content now.
  We should cross-check that against the SRA metadata to see where the metadata
  is wrong or incomplete.

* we could do bulk strain analyses of a variety of human pathogens at
  this point, if we wanted.

* we can pursue the uncategorized/uncategorizable samples too, of
  course!  There are a few strategies we can try here but I think the
  best strategy boils down to assembling them, annotating them, and
  then using protein-based comparisons to identify nearest known
  microbes.  (See `Twitter conversation 1
  <https://twitter.com/ctitusbrown/status/817117068554182656>`__ and
  `Twitter conversation 2
  <https://twitter.com/ctitusbrown/status/817395590174679040>`__.)

* we should cross-compare uncategorized samples!

At this point I'm not 100% sure what we'll do - we have some other fish to
fry in the sourmash project first, I think - but we'll see. Suggestions
welcome!

A few points based partly on reactions to the Twitter
conversation about what to do --

* mash/MinHash comparisons aren't going to give us anything interesting,
  most likely; that's what's leading to our list of uncategorizables.

* I'm skeptical that nucleotide level comparisons of any kind (except perhaps
  of SSU/16s genes) will get us anywhere.

* functional analysis seems secondary to figuring out what branch of
  bacteria they are, but maybe I'm just guilty of name-ism here.

Backing up -- why would you want to do this?
--------------------------------------------

No, I'm not into doing this just for the sake of doing it ;).

* It would be nice to make the SRA content searchable.  This is particularly
  important for non-model genomic/transcriptomic/metagenomic folk.

* I think a bunch of the tooling we're building around sourmash is going
  to be broadly useful for lots of people.

* Being able to scale sourmash to hundreds of thousands (and millions and
  eventually billions) of samples is going to be, like, super useful.

* More generally, this is infrastructure to support data-intensive biology.
  We have funding to develop that.

* I'm hoping I can tempt the grey databases into indexing their
  (meta)genomes and transcriptomes and making the signatures available
  for search.  See e.g. `"MinHash signatures as ways to find samples,
  and collaborators?"
  <http://ivory.idyll.org/blog/2016-sourmash-signatures.html>`__.

--titus
