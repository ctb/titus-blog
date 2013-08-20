Announcing the khmer-protocols project
######################################

:author: C\. Titus Brown
:tags: assembly,eel pond,kalamazoo,assembly
:date: 2013-08-20
:slug: announcing-khmer-protocols
:category: science
:status: draft

This summer, `I spent a lot of time writing up computational protocols
<../2013-summer-vacation.html>`__ for both mRNAseq and metagenome
assembly.

I'm happy to announce that they are now available!

The Eel Pond mRNAseq Assembly Protocol
--------------------------------------

This protocol, named after the harbor in Woods Hole that the Marine
Biological Lab surrounds, is a lightweight mRNAseq assembly pipeline
that, for 50-100m reads, should take 1-3 days on a single m1.xlarge
AWS machine.  It walks the user through:

* adapter trimming with Trimmomatic
* quality filtering with fastx
* digital normalization with khmer
* assembly with the Trinity pipeline
* setting up a little personal BLAST server in the cloud
* annotating the sequences against the mouse proteome

@@link

Soon, we will be adding differential expression analysis with RSEM.

Note, I'd particularly like to thank Josh Rosenthal of the UPR for
helping out with testing this protocol.

The Kalamazoo Metagenome Assembly Protocol
------------------------------------------

This protocol, named after the funniest-sounding city in Michigan,
is a reasonably lightweight metagenome assembly pipeline.  For most
metagenomes it should be executable on moderate to high-end cloud
resources.  It walks the user through:

* adapter trimming with Trimmomatic
* quality filtering with fastx
* digital normalization with khmer
* assembly with Velvet
* setting up a little personal BLAST server in the cloud

Basic Information
-----------------

If you need help, or are interested in discussing, helping out, or
otherwise kibbitzing, `sign up for the "protocols" mailing list
<http://lists.idyll.org/listinfo/protocols>`__.

The khmer-protocols source is `here
<https://github.com/ged-lab/khmer-protocols>`__ on github.  There is
`an issue tracker
<https://github.com/ged-lab/khmer-protocols/issues>`__ as well; dump
unresolved questions there.

Pre-Answered Questions
----------------------

Q. Why aren't you just using the Trinity pipeline (for mRNAseq assembly)?

A. Part of it is that I believe the Trinity pipeline is heavier-weight
   than ours, and will require more computational resources; another
   part of it is that I don't want to have to coordinate with them as
   we evolve our pipeline (and I would imagine the same is true in
   reverse); a third is that we are using some of our own special
   sauce, and want the leisure to explore and evolve our own pipeline.

Q. Someone else claims they have a better protocol than yours.  Why should
   I use yours?

A. You shouldn't!  But please use *someone's* rather than inventing your own,
   until you have a good reason otherwise.  Thanks in advance.

Q. Why are you releasing these as protocols, rather than as pipelines?
   I'd rather not have to type out all that stuff!

A. There are lots of reasons, but the simplest is that it's actually quite
   hard to write a robust pipeline.  Plus, these protocols are kind of easy
   to remix, because it's clear what data goes on to the next step at each
   point.  So if you want to try out a different trimmer, or avoid
   digital normalization, it's easy!

Q. I used your protocol and got sucky results. Your protocol sucks and I
   hate you.

A. I'm sorry to hear that! ...could you share your sucky results so that we
   can improve our protocol? Thanks!

Q. I ignored your advice and modified your protocol and got *way* better
   results.  Your protocol sucks.  Ha ha!

A. Great! ...could you share your improvements? Thanks!

Q. Your protocol isn't as good as it could be.  I invented a nifty piece
   of software that solves a bunch of problems and is way cool.

A. Great! ...could you share? Thanks!

Q. I have 454, Ion Torrent, or PacBio data.  Can we integrate this?

A. Not sure how to do that yet. Sorry!

Q. I'd like to contribute; how can I?

A. Discuss on the mailing list, and/or submit pull requests (see
   `github flow <http://scottchacon.com/2011/08/31/github-flow.html>`__
   for more info on pull requests).

Q. This is awesome! I have money to give you!

A. Great! We take donations in unmarked $20s and $50s.

Longer-term hopes
-----------------

1. Imagine a world where it's copy-and-paste, and $50 of compute resources,
   to assemble and annotate a transcriptome!  Wouldn't that be neat?

2. We are planning to instrument the protocols with all sorts of
   performance metrics and diagnostic outputs, so that we can understand
   where the bottlenecks are.

3. Some time soon we plan to start offering to run your assemblies for you,
   using these protocols.
   `Read more here <http://ivory.idyll.org/blog/crowdsourced-analysis-with-data-privacy-sunset.html>`__.

4. We'd like to set up comparative performance metrics, both on the
   computational side and on the performance side (think Assemblathon 2,
   but for transcriptomes and metagenomes).  This will help us evaluate
   our own future work, as well as serve as one possible platform for
   evaluating and reviewing new assemblers.

5. Hopefully people will get angry with us for being so naive about
   transcriptome and metagenome assembly and demonstrate to us why
   we are wrong. Then we will fix our protocols accordingly.
