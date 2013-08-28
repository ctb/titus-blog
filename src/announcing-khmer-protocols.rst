Announcing the khmer-protocols project
######################################

@@ add leigh's stuff

:author: C\. Titus Brown
:tags: assembly,eel pond,kalamazoo,assembly
:date: 2013-08-20
:slug: announcing-khmer-protocols
:category: science
:status: draft

(with Chris Welcher, Michael Crusoe, and Leigh Sheneman.)

This summer, `I spent a lot of time writing up computational protocols
<../2013-summer-vacation.html>`__ for both mRNAseq and metagenome
assembly in the Amazon cloud.

I'm happy to announce that they are now available!  `Here's the link. https://khmer-protocols.readthedocs.org/>`__.

Both protocols rely heavily on `khmer
<http://khmer.readthedocs.org/en/latest/>`__, and use both
`partitioning
<http://www.pnas.org/content/early/2012/07/25/1121464109.abstract>`__
and `digital normalization <http://arxiv.org/abs/1203.4802>`__.

The Eel Pond mRNAseq Assembly Protocol
--------------------------------------

This protocol, named after the harbor in Woods Hole surrounded by
the Marine Biological Lab, is a lightweight mRNAseq assembly pipeline
that, for 50-100m reads, should take 1-3 days on a single m1.xlarge
AWS machine (see `Leigh Shemenan's blog post for more information <http://leighasheneman.com/blog/2013/8/21/x0lwr5nekf4sogplrsopekpu55os7z>`__).  It walks the user through:

* adapter trimming with Trimmomatic
* quality filtering with fastx
* digital normalization with khmer
* assembly with the Trinity pipeline
* setting up a little personal BLAST server in the cloud
* annotating the sequences against the mouse proteome

Soon, we will be adding differential expression analysis with RSEM.

Note, we would particularly like to thank Josh Rosenthal of the UPR for
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

The metagenome protocol is a bit less mature than the mRNAseq protocol,
but should still be useful.

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

A. Part of it is that the Trinity pipeline is heavier-weight than our
   protocol, and will require more computational resources; another
   part of it is that I don't want to have to coordinate with them as
   we evolve our protocol (and I would imagine the same is true in
   reverse); a third is that we are using some of our own special
   sauce, and want the leisure to explore and evolve our own protocol.

Q. Someone else claims they have a better protocol than yours.  Why should
   I use yours?

A. You shouldn't!  But please use *someone's* rather than inventing your own,
   until you have a good reason otherwise.  Thanks in advance.

Q. So then why did you invent your own?

A. Umm... we don't know of any good lightweight protocols for the
   cloud, honestly.  Plus we think very highly of our special sauce.

Q. Why are you releasing these as protocols, rather than as pipelines?
   I'd rather not have to type out all that stuff!

A. There are lots of reasons, but the simplest is that it's actually
   quite hard to write a robust pipeline that anyone can run.  Plus,
   the protocols are kind of easy to remix, because it's clear what
   data goes on to the next step at each point; this is not so true of
   pipelines, which are large, opaque bodies of code.  So if you want
   to try out a different trimmer, or avoid digital normalization,
   it's easy!

Q. I used your protocol and got sucky results. Your protocol sucks and I
   hate you.

A. I'm sorry to hear that! ...could you share your sucky results so that we
   can improve our protocol? Thanks!

Q. I ignored your advice and modified your protocol and got *way* better
   results.  Your protocol sucks.  Ha ha!

A. Great! ...could you share your improvements? Thanks!  We'd be happy
   to give you credit in both the protocol and subsequent publications.

Q. Your protocol isn't as good as it could be.  I invented a nifty piece
   of software that solves a bunch of problems and is way cool.

A. Great! ...could you share? Thanks! We'd be happy to give you credit
   in both the protocol and subsequent publications.

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

0. It's remarkably difficult to find a detailed HOWTO on how to deal
   with raw reads all the way through annotation and differential
   expression analysis.  Hopefully this can have a clarifying effect
   for people who want to gain a better understanding of some of the
   possible steps.

1. Imagine a world where it's copy-and-paste, and $50 of compute resources,
   to assemble and annotate a transcriptome!  Wouldn't that be neat?

2. We are planning to instrument the protocols with all sorts of
   performance metrics and diagnostic outputs, so that we can
   understand where the bottlenecks are. (See Leigh's `initial blog
   post
   <http://leighasheneman.com/blog/2013/8/21/x0lwr5nekf4sogplrsopekpu55os7z>`__
   on this.)

3. Right now there's no good way to investigate the impact of different
   primer trimming and quality filtering programs, much less different
   assemblers.

4. We'd like to set up comparative metrics, both on the computational
   side and on the performance side (think Assemblathon 2, but for
   transcriptomes and metagenomes).  This will help us evaluate our
   own future work, as well as serve as one possible platform for
   evaluating and reviewing new assemblers.

5. Hopefully people will get angry with us for being so naive about
   transcriptome and metagenome assembly and demonstrate to us why
   we are wrong. Then we will fix our protocols accordingly.

6. Some time soon we plan to start offering to run your assemblies for you,
   using these protocols.
   `Read more here <http://ivory.idyll.org/blog/crowdsourced-analysis-with-data-privacy-sunset.html>`__.

7. These protocols can also serve as substrates for the development,
   testing, and integration of new technology, like error correction.

8. Did I mention everything's `on github
<https://github.com/ged-lab/khmer-protocols>`__?  It's also under CC0,
like almost everything else we do.  This means that

     - you can copy, adapt, modify, and remix the protocols;

     - you can contribute openly, with credit, to them, via a well-understood
       process (again, see `github flow <http://scottchacon.com/2011/08/31/github-flow.html>`__;

     - and, of course, you can do whatever else you want to do with them.

@@cit