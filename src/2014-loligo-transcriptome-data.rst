Loligo pealeii (squid) data dump
################################

:author: C\. Titus Brown
:tags: open data,f-yeah
:date: 2014-02-17
:slug: 2014-loligo-transcriptome-data
:category: science

A few months back, I announced `the khmer protocols project
<http://ivory.idyll.org/blog/announcing-khmer-protocols.html>`__, an
effort to write down an explicit, open protocol for transcriptome and
metagenome assembly.  This project was started `during the summer of
2013 at the Woods Hole Marine Biological Lab
<http://ivory.idyll.org/blog/2013-summer-vacation.html>`__, in
collaboration with `Joshua Rosenthal
<http://neuro.rcm.upr.edu/research/investigators/dr.-j.-rosenthal>`__.
I'd met Josh at the `CephSeq meeting
<http://ivory.idyll.org/blog/cephseq-cephalopod-genomics.html>`__ the
year before, and we reconnected at MBL in 2013; there, motivated in
part by discussions at CephSeq, I started writing the eel-pond
protocol.

During the summer, Josh and I found that we were both incredibly
frustrated by the general failure of researchers to share data pre-pub, and so
we started to chat seriously about some ideas we'd independently had
about incentivizing the opening of transcriptome data.  This
eventually led to `the Open Marine Transcriptome project
<http://ivory.idyll.org/blog/open-transcriptome-project-thoughts.html>`__,
which is still in its formative stages.

However, in the meantime I am happy to report that Josh assembled a
bunch of squid transcriptomes and is willing to make them available to
all.  In addition, Josh did some skim Illumina sequencing (~40x
coverage) of the squid genome, and my lab assembled it; we are making
a really basic draft genome available as well.  (Here, by squid, we
mean Loligo pealeii, or the `Longfin inshore squid
<http://en.wikipedia.org/wiki/Longfin_inshore_squid>`__ -- "loligo"
for short.  It is also sometimes called "Doryteuthis pealeii".)

It should be noted that one of the transcriptomes was made from
carefully dissected Giant Fiber Lobe neurons. These are the cell
bodies for the well-studied squid giant axon. Thus this transcriptome
should provide "molecular support" for all the cell biology and
neurophysiology that has focused on this most famous of preps.

We are pleased to announce the availability of this data, in two formats.

First, you can download the assembled and annotated transcriptome data
in FASTA format:

* `Loligo pealeii buccal ganglion transcriptome (v1.0) <https://s3.amazonaws.com/public.ged.msu.edu/oompa/LPealei.Buccalganglion.Annotated.transcriptome.v1.0.fasta.gz>`__

* `Loligo pealeii giant fiber lobe (v1.0) <https://s3.amazonaws.com/public.ged.msu.edu/oompa/LPealei.GFL.Annotated.transcriptome.v1.0.fasta.gz>`__

* `Loligo pealeii optic lobe (v1.0) <https://s3.amazonaws.com/public.ged.msu.edu/oompa/LPealei.OL.Annotated.transcriptome.v1.0.fasta.gz>`__

* `Loligo pealeii stellate ganglion (without giant fiber lobe) (v1.0) <https://s3.amazonaws.com/public.ged.msu.edu/oompa/LPealei.SG.Annotated.transcriptome.v1.0.fasta.gz>`__

* `Loligo pealeii vertical lobe (v1.0) <https://s3.amazonaws.com/public.ged.msu.edu/oompa/LPealei.VerticalLobe.Annotated.Transcriptome.v1.0.fasta.gz>`__

as well as the (unannotated) genome assembly: `Loligo pealeii genomic
data (v0.2)
<https://s3.amazonaws.com/public.ged.msu.edu/oompa/loligo-pealeii-gmc-v0.2.fa.gz>`__

Second, we have *also* made available a `public BLAST server <http://athyra.idyll.org/~t/blast/ceph/>`__ where you can search the individual transcriptomes, a database of the concatenated transcriptomes, and the genomic sequence.  (The BLAST server is not on a particularly powerful machine so I may turn it off if thousands of squid enthusiasts start pounding on it ;)

.. @@update ceph blast with backlink

----

Methods
~~~~~~~

The various tissues were dissected by Josh Rosenthal and sequenced
using an Illumina HiSeq.  Raw data and details will be made available as
part of a data paper.  Assembly and annotation was done per
`the khmer protocols v0.8.4 <https://khmer-protocols.readthedocs.org/en/v0.8.4/>`__, with the exception of using the uniprot database for annotation instead
of mouse.

The genomic data was similarly sequenced with a HiSeq and was then
subjected to a variant of the `Kalamazoo metagenome protocol
<https://khmer-protocols.readthedocs.org/en/v0.8.4/>`__: specifically,
we did three-pass digital normalization and then assembled with
Velvet.  This will be described in more detail in the data paper.

Answers
~~~~~~~

**Why are you making these data available?**

We love cephalopods (see `this great writeup of why <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3570802/>`__, and we think that making this data available will
accelerate cephalopod research.  You can read more about our general
thoughts `here
<http://ivory.idyll.org/blog/open-transcriptome-project-thoughts.html>`__.

**How should I use them?**

Heck if we know.  Impress us!

**How should I cite them?**

We will post a citation handle to `figshare <http://figshare.com>`__
shortly.  If you desperately need to cite us, please contact us a few
days in advance of when you need to cite ;).

**What if the transcripts or contigs are wrong?**

Every assembly is at least a little bit wrong, but we're reasonably
confident that our assembly approaches work OK.  We've also tried to
maximize sensitivity of the genome assembly, at the expense of contig
length; we believe this means that misassemblies are also somewhat
unlikely.

That having been said, it is your responsibility to validate your
own analyses.  Caveat emptor.

You may, of course, also pretend that the data is not available and then
not use it for anything.

**What data sharing license are these data under?**

We're releasing these data under `Creative Commons 0
<https://creativecommons.org/publicdomain/zero/1.0/>`__, the most
liberal of the Creative Commons licenses.  This is a public domain
dedication: do with the data what you will.  If you publish something
based on this data, it is standard academic practice to cite us (see
above).

**Hey, can I repost these on my own site?**

Sure thing.  Just remember that standard academic practice is to cite
the *origin* of the data, so even if you do something super cool in
terms of remixing the data with other data sets, we'd appreciate a
link and guidance for users of your data set to cite us.

**Why aren't you trying to get a Science or Nature paper out of all this?
Aren't your reputations going to suffer for doing all this work without
trying to milk the data for all it's worth?**

We're pretty sure our reputations won't suffer from making a bunch of
useful data available.  Heck, we're pretty sure *your* reputation
wouldn't suffer from making a bunch of useful data available (hint).

**The genome is, like, completely useless!? The N50 is about 250 bases!**

Yep.  Sorry!  If you give us $200k we will give you a better genome in
~6 months (annotations not included).  In the meantime, we think that
this genome is extremely useful for determining exon structure and
avoiding degenerate PCR at all costs.  In fact, this genome shows
near-complete coverage of the ORFs from a handful of cDNAs cloned
Back When.

I'm serious about the $200k.  And that's direct, not direct+indirect.

**Do you want to collaborate? I have a bunch of analyses that you can do
for me -- Science/Nature paper guaranteed!**

Nope, sorry, too busy.  I am, however, happy to *not* collaborate --
see `the open marine transcriptome project
<http://ivory.idyll.org/blog/open-transcriptome-project-thoughts.html>`__.
Send us your tired, your poor, your huddled transcriptomes...

Questions
~~~~~~~~~

We'd love your thoughts on these questions of ours in the comments
below.

* Is this a good way for us to post the data?  Is there a better way?

* How important is raw data (raw reads) to you? Should we accelerate
  the posting of the raw data?  (You can have it now for all we care, but
  we don't have a good place to post really big files.)

We'd also love any other feedback, but I reserve the right to publicly
post negative feedback that is particularly entertaining.

Enjoy!

--titus
