MinHash signatures as ways to find samples, and collaborators?
##############################################################

:author: C\. Titus Brown
:tags: minhash,sourmash,ddd
:date: 2015-04-11
:slug: 2016-sourmash-signatures
:category: science

`As I wrote last week
<http://ivory.idyll.org/blog/2016-sourmash.html>`__ my latest
enthusiasm is MinHash sketches, applied (for the moment) to RNAseq
data sets.  Briefly, these are small "signatures" of data sets that
can be used to compare data sets quickly.  In the previous blog post,
I talked a bit about their effectiveness and showed that (at least in
my hands, and on a small data set of ~200 samples) I could use them to
cluster RNAseq data sets by species.

What I didn't highlight in that blog post is that they could
potentially be used to find samples of interest as well as (maybe)
collaborators.

Finding samples of interest
===========================

The "samples of interest" idea is pretty clear - supposed we had a
collection of signatures from all the RNAseq in the the Sequence Read
Archive? Then we could search the entire SRA for data sets that were
"close" to ours, and then just use those to do transcriptome studies.
It's not yet clear how well this might work for finding RNAseq data
sets with similar expression patterns, but if you're working with
non-model species, then it might be a good way to pick out all the
data sets that you should use to generate a de novo assembly.

More generally, as we get more and more data, finding relevant samples
may get harder and harder.  This kind of approach lets you search on
sequence content, not annotations or metadata, which may be incomplete
or inaccurate for all sorts of reasons.

In support of this general idea, I have `defined a provisional file
format (in YAML)
<https://github.com/dib-lab/sourmash/blob/master/urchin/abyssicola-SRR3217899.sig>`__
that can be used to transport around these signatures.  It's rather
minimal and fairly human readable - we would need to augment it with
additional metadata fields for any serious use in databases(but see
below for more discussion on that).  Each record (and there can
currently only be one record per signature file) can contain multiple
different sketches, corresponding to different k-mer sizes used in
generating the sketch.  (For different sized sketches with the same
k-mers, you just store the biggest one, because we're using bottom
sketches so the bigger sketches properly include the smaller
sketches.)

If you want to play with some signatures, you can -- `here's an
executable binder <http://mybinder.org/repo/dib-lab/sourmash/>`__ with
some examples of generating distance matrices between signatures, and
plotting them.  Note that by far the most time is spent in loading the
signatures - the comparisons are super quick, and in any case could be
sped up a lot by moving them from pure Python over to C.

I've got a pile of all echinoderm SRA signatures already built, for
those who are interested in looking at a collection -- `look here
<https://github.com/dib-lab/sourmash/tree/2016-apr-blog/urchin>`__.

Finding collaborators
=====================

Searching public databases is all well and good, and is a pretty cool
application to enable with a few dozen lines of code.  But I'm also
interested in enabling the search of *pre-publication* data and doing
matchmaking between potential collaborators. How could this work?

Well, the interesting thing about these signatures is that they are
irreversible signatures with a one-sided error (a match means
something; no match means very little).  This means that you can't
learn much of anything about the original sample from the signature
unless you have a matching sample, and even then all you know is the
species and maybe something about the tissue/stage being sequenced.

In turn, this means that it might be possible to convince people to
publicly post signatures of pre-publication mRNAseq data sets.

Why would they do this??

An underappreciated challenge in the non-model organism world is that
building reference transcriptomes requires a lot of samples.  Sure,
you can go sequence just the tissues *you're* interested in, but you
have to sequence deeply and broadly in order to generate good enough
data to produce a good reference transcriptome so that you can
interpret your own mRNAseq.  In part because of this (as well as many
other reasons), people are slow to publish on their mRNAseq - and,
generally, data isn't made available pre-publication.

What if you could go fishing for collaborators on building a reference
transcriptome? Very few people are excited about just publishing a
transcriptome (with some reason, `when you see papers that publish 300
<http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889>`__),
but those are really valuable building blocks for the field as a
whole.

So, suppose you had some RNAseq, and you wanted to find other people
with RNAseq from the same organism, and there was this service where
you could post your RNAseq signature and get notified when similar
signatures were posted?  You wouldn't need to do anything more than
supply an e-mail address along with your signature, and if you're
worried about leaking information about who you are, it's easy enough
to make new e-mail addresses.

I dunno. Seems interesting.  Could work. Right?

One fun point is that this could be a distributed service.  The signatures
are small enough (~1-2 kb) that you can post them on places like github,
and then have aggregators that collect them.  The only "centralized" service
involved would be in searching all of them, and that's pretty lightweight
in practice.

Another fun point is that we already have a good way to communicate
RNAseq for the limited purpose of transcrpiptome assembly -- `diginorm
<http://ivory.idyll.org/blog/what-is-diginorm.html>`__.
Abundance-normalized RNAseq is useless for doing expression analysis,
and if you normalize a bunch of samples together you can't even figure
out what the original tissue was.  So, if you're worried about other
people having access to your expression levels, you can simply
normalize the data all together before handing it over.

Further thoughts
================

As I said in the `first post
<http://ivory.idyll.org/blog/2016-sourmash.html>`__, this was all
nucleated by reading the `mash
<http://biorxiv.org/content/early/2015/10/26/029827>`__ and
`MetaPalette <http://biorxiv.org/content/early/2016/02/17/039909>`__
papers.  In my review for MetaPalette, I suggested that they look at
mash to see if MinHash signatures could be used to dramatically reduce
their database size, and now that I actually understand MinHash a bit
more, I think the answer is clearly yes.

Which leads to another question - the Mash folk are clearly planning
to use MinHash & mash to search assembled genomes, with a side helping
of unassembled short and long reads.  **If** we can all agree on an
interchange format or three, why couldn't we just start generating
public signatures of all the things, mRNAseq and genomic and
metagenomic all?  I see many, many uses, all somewhat dimly...  (Lest
anyone think I believe this to be a novel observation, clearly the
Mash folk are well ahead of me here -- they undersold it in their
paper, so I didn't notice until I re-read it with this in mind, but
it's there :).

Anyway, it seems like a great idea and we should totally do it.  Who's
in? What are the use cases? What do we need to do? Where is it going
to break?

--titus

p.s. Thanks to Luiz Irber for some helpful discussion about YAML formats!
