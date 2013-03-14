The challenges of mRNAseq analysis
##################################

:author: C\. Titus Brown
:tags: science,mRNAseq,assembly
:date: 2013-3-13
:slug: the-challenges-of-mrnaseq-analysis
:category: science

I'm worried about our current mRNAseq analysis strategies.

I recently posted a draft paper of ours to arXiv entitled `RNA-Seq
Mapping Errors When Using Incomplete Reference Transcriptomes of
Vertebrates
<http://haldanessieve.org/2013/03/12/rna-seq-mapping-errors-when-using-incomplete-reference-transcriptomes-of-vertebrates/>`__;
the link is to the Haldane's Sieve discussion of the paper.  Graham
Coop said I should write something quick, and so I am (sort of -- I mean
to write this post a few days ago, but teaching. family. etc.)

I decided to post the paper -- although we haven't submitted it
yet -- because I wanted to solicit feedback and gauge where the
disagreements or misunderstandings were likely to pop up.  I suspect
reviewers are going to have a hate-hate relationship with this paper,
too, so I want to get rid of any obvious mistakes by crowdsourcing
some early reviews ;).

Before I talk about the paper, let me mention a few related factoids
that crossed my 'net firehose and that tie into the paper; I'll weave
them into the paper discussion below.

A. Dan Zerbino (one of the `Assembly Gods? <http://www.homolog.us/blogs/2013/02/20/the-mapping-god-speaketh/>`__) wrote a `good e-mail about how Oases can't really leverage
   coverage information when reconstructing transcripts
   <http://listserver.ebi.ac.uk/pipermail/oases-users/2013-March/000301.html>`__
   on the oases-users mailing list.

B. I read and reviewed the `SASeq paper on mRNAseq quantification
   <http://arxiv.org/abs/1208.3619>`__, which talks about how
   many of our transcript models are almost certainly not expressed.

C. `The lamprey genome paper came out
   <http://ivory.idyll.org/blog/the-lamprey-genome.html>`__, pointing out
   that the genome is probably missing ~20-30% of the germline content.

D. `A paper on evaluating mRNAseq expression analysis software hit arXiv
   <http://arxiv.org/pdf/1301.5277v2.pdf>`__.

OK, so what did our paper say?

The paper's genesis is this: for years I'd been explaining to
collaborators that mRNAseq was unreliable on any organism without a
pretty good reference transcriptome, and that constructing the
reference transcriptome relied on either good mRNAseq assembly tools
OR on having a good reference genome.  So that was what my lab was
working on doing with their data.

Since we tend to work on weird organisms like chick (which has an
incomplete genome and a notoriously poor gene annotation), lamprey
(see above -- missing 20-30% of its genome), and Molgulid ascidians
(for which we are constructing the genome), we needed to go the de
novo mRNAseq assembly route.

However, we also quickly realized that there were a few problems with
de novo mRNAseq assembly and expression evaluation: lots of mRNAseq
needed to be crunched in order to get good reconstruction, which was
computationally intensive (see: diginorm); splice variants would
confuse mapping (see: this paper); we were uncertain of how well
splice variants could be assembled with or without a reference (see:
this paper); and we weren't sure how to evaluate mapping tools.

When a new postdoc (Alexis Black Pyrkosz, the first author) joined the
lab and wanted a fairly simple project to get started, I suggested
that she evaluate the extent to which an incomplete reference transcriptome
would screw things up, and perhaps try out a few different mappers.  This
took her about a year to work through, in addition to all of her other
projects.  She built a straightforward simulation system, tried it out
on chick and mouse, and got some purely computational results that place
(in my view) fundamental limits on what you can accomplish with certainty
using current mRNAseq technology.

Incidentally, one piece of feedback she got at GLBio from a prof was
(paraphrased) "I hope this isn't your real project, because it's not
very interesting."

The results, in short, are:

1. What mapper you use doesn't really matter, except to within a few percent;
   they all perform fine, and they all degrade fairly fast with sequencing
   errors.

2. Incomplete reference transcriptomes matter, a lot.  There are two
   entirely obvious reasons: if you have a splice variant A that is in
   your reference but not present in your mRNAseq, and a splice
   variant B that is not in your reference but is actually transcribed
   and in your mRNAseq, the reads for B will get mapped to the wrong
   transcript; and (the even more obvious one) you can't measure the
   expression of something that's not in your reference via mapping.

   The SASeq paper does a nice job of pointing out that there's something
   rather seriously wrong with current mRNAseq references, even in mouse,
   and they provide a way to minimize misestimation in the context of the
   reference.

3. Direct splice variant reconstruction and measurement is, technically,
   impossible for about 30% of the transcripts in mouse.  For standard
   paired-end sequencing, it turns out that you cannot claim that
   exon A and exon Z are present in the same isoform for about 30% of
   the isoforms.

4. The slightly surprising conclusion that we reached from this is
   that mRNAseq assembly is also, generally speaking, impossible: you
   cannot unambiguously construct a reasonably large proportion of
   observed isoforms via assembly, since the information to connect
   the exons is not there.

   Until recently, I had held out a forlorn hope that Clever Things
   were being done with coverage. Then I saw Dan Zerbino's e-mail,
   point A, above.

And yet, judging by the Oases and Trinity publications, assembly
works!  What's up?

There's something a bit weird going on. Tools like Oases and
Trinity can clearly construct a fair proportion of previously observed
transcripts, even though the information to do so from direct
observation isn't there and they can't necessarily use coverage
inference reliably.  My guess (see paper D, above) is that this is
because biology is mostly cooperating with us by giving us one
dominant isoform in many or most circumstances; this matches what Joe
Pickrell et al. observed in their *truly excellent* `noisy splicing
paper <http://www.ncbi.nlm.nih.gov/pubmed/21151575>`__.  But I'd be
interested in hearing alternate theories.

At this point, my friend and colleague Erich Schwarz tends to get
unhappy with me and say "what would you have me do with my mRNAseq,
then? Ignore it until you come up with a solution, which you claim is
impossible anyway?"  Good question!  My answer is (a) "explore the
extent to which we can place error bars or uncertainty on isoform
abundance calculations", (b) "figure out where interesting isoform
misestimation is likely to lie in the data sets", and (c) "look at
exon-exon junctions and exon presence/absence instead of whole isoform
abundance."  But the tools to do this are still rather immature, I
think, and people mostly ignore the issue or hope it doesn't bugger up
their results.  (Please correct me if I'm wrong - I'd love pointers!)

In my lab, we are starting to explore ways to determine what mis- or
un-assembled isoforms there might be in a given transcriptome.  We're
also looking at non-reference-based ways of doing mRNAseq
quantification and differential expression (technically, graph-based
methods for mRNAseq).  We are also deeply skeptical of many of the
normalization approaches being used, largely because every time we
evaluate them in the context of our actual data, our data seems to
violate a number of their assumptions...  Watch This Space.

Paper reactions
---------------

What's the reaction to the paper been, so far?

Well, on Twitter, I've been getting a fair bit of "ahh, a good
reference genome will solve your problems!" But I think points #3 and
#4 above stand.  Plus, invoking solving `a harder and more expensive
problem
<http://ivory.idyll.org/blog/thoughts-on-assemblathon-2.html>`__ to
solve what you think is a simpler problem is an interesting approach
:).  And since we don't have good references (and won't for a while)
it's not really a solution for us.

I've also been getting "this is a well known problem and not worth
publishing!" from a few people. Well, OK, fair enough.  I've been
skimming papers with an eye to this for a while, but it's entirely
possible I've missed this part of the literature.  I'd love to read
and cite such a paper in this one (and even rely on it to make our
points, if it truly has significant overlap).  Please post links in
the comments, I'd really appreciate it!

It is clear that the paper needs some reshaping in light of some of
the comments, and I'd like to especially thank Mick Watson for his
open comments.

Concluding thoughts
-------------------

If our results are right, then our current approaches to mRNAseq have
some potentially serious problems, especially in the area of isoform
expression analysis.  Worse, these problems aren't readily addressible
by doing qPCR confirmation or replicate sequencing.  I'm not entirely
sure what the ramifications are but it seems like a worthwhile thing
that someone should point out.

--titus

p.s. Our simulations are fairly simple, BTW.  We'll put the code out
there soon for you to play with.

p.p.s. Likit Preeyanon, a graduate student in my lab, was one of the
first people in my lab to look really critically at mRNAseq.  Watch
for his paper soon.
