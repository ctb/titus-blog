The Dead Sea Scrolls and an Open Marine Transcriptome Project
#############################################################

:author: C\. Titus Brown
:tags: open science, assembly
:date: 2014-01-15
:slug: open-transcriptome-project-thoughts
:category: science

In 1947 a Bedouin shepherd found a bunch of ancient scrolls in a cave
near the Dead Sea.  These scrolls, now known as `the Dead Sea scrolls
<http://en.wikipedia.org/wiki/Dead_Sea_Scrolls>`__, included some of
the oldest known Biblical texts as well as other Jewish religious
writing. Over the next few decades, these scrolls - of immense
historical importance -- remained in the possession of a small team of
scholars, largely unpublished.

`In 1991, the Huntington Library made available a complete microfilm
copy of the Scrolls <http://gnosis.org/library/dss/dss.htm>`__, thus
dramatically opening up research in this area.  Cool! A story of open
data and open research!

What the heck does this have to do with transcriptomes?

With the advent of `ridiculously inexpensive deep sequencing
<http://www.genome.gov/sequencingcosts/>`__, many labs, big and small,
have been sequencing lots and lots of transcriptomes.  Transcriptomes
are, generally speaking, fairly inexpensive to sequence ($1000/sample,
using a HiSeq); much easier to assemble than genomes; and quite useful
in their own right, in terms of enabling downstream research.

Unfortunately, many of these transcriptomes remain immured behind lab
walls, often for lack of bioinformatics (human) resources.  Even
worse, for non-model organisms, the transcriptomes are most useful in
context -- as we discussed in `the Cephalopod Sequencing Consortium
white paper
<http://www.standardsingenomics.org/index.php/sigen/article/view/sigs.3136559>`__,
an isolated transcriptome from a deeply divergent critter is only
useful inasmuch as you can annotate the transcripts by homology.  So
these transcriptomes are subject to a classic `network effect
<http://en.wikipedia.org/wiki/Network_effect>`__ where individually
they are not as useful as they would be collectively.

In other words, there's a lot of potential for accelerating biology if
we can only figure out how to get people to open up their data. (Just
like the Dead Sea Scrolls! Sort of.)

Hmm.  I wonder if offering to do the analysis for them would help?

So let's try that, shall we?

The basic idea
~~~~~~~~~~~~~~

A while back I suggested `crowdsourcing -omic analysis
<http://ivory.idyll.org/blog/crowdsourced-analysis-with-data-privacy-sunset.html>`__.
I think we are going to try out a related idea on marine transcriptomes.

The bare-bones details go something like this:

1. We would solicit (say) 100 marine animal mRNAseq data sets,
   ~50-100m reads each (for two+ conditions, if you have 'em), from
   anyone.

2. We would take each data set and pass them through our
   transcriptomics pipeline (open, versioned, etc).  Estimated cost to
   run on Amazon? ~$100-200.

3. We would then provide an annotated transcriptome for download, a
   BLAST server, spreadsheets of the annotations, and spreadsheets of
   differential expression information, to the owners of the data.

4. One year after the data was given to us, we would put make the data
   and analysis publicly available under a CC-BY or CC0 license (on
   figshare? SRA? Amazon?) and provide a citation handle for the
   data+analysis (e.g. on figshare).

Potential embellishments include the idea of finding money to sequence
~20 or more samples as part of this.

A collaborator and I are planning to post ~5-10 such data sets already,
and the protocols for doing the analysis are getting closer to complete
(`see them here <https://khmer-protocols.readthedocs.org/>`__).

What's in it for you?
~~~~~~~~~~~~~~~~~~~~~

If you're the proud provider of an mRNAseq data set, what's in it for you?

1. You'll get an initial transcriptome analysis that will help you
   drive your biology.

2. We'll give you some tools to explore the transcriptome data
   (although they might be just a BLAST server, assembly download,
   and spreadsheet download at first).

3. We'll also automatically compute appropriate diagnostic outputs and
   cross-checks to reassure you that your results are OK.

4. We'll manage submission of your raw data to an archival server, sufficient
   for publication purposes.

5. There will be an easy citation for the first part of the methods
   section of your mRNAseq analysis.

6. Free and decent bioinformatics analysis.  Consulting fees for this
   kind of thing range from $50/hr to $200/hr; if someone hired me to
   run this kind of transcriptome assembly for them, I'd charge ~$1000
   per 100m reads.  But you can't beat free :)

What's in it for us?
~~~~~~~~~~~~~~~~~~~~

Why on earth would we do this?

0. I did my graduate work in evo devo & have a lot of friends in this field;
   I can't think of many cheaper ways to accelerate invertebrate research
   within the Bilateria than to help people analyze their data.

1. We really do believe in open source, open science, and open data, and
   think this would be a great demo project.  

2. We get to study the computation as well as the bioinformatics of
   many different mRNAseq assemblies (which has got to be
   fascinating!) and thoroughly test our assembly pipeline on a lot of
   data. Having a chance to assemble many different transcriptomes
   would help us understand when it does and doesn't work, and
   help us (and, later on, others) improve assembly.

3. We expect to develop lots of new assembly comparison tools as part of
   figuring out whether or not our approaches worked!

4. Citations of our work, increased impact, and collaborations on hard
   research problems are sure to follow.

5. I think this would upset people who are
   currently hoarding genomic and transcriptomic data of great interest,
   and I like being disruptive.

Tough decisions and our proposals to address them
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**What license would we publicly release the data and analysis under?**
Probably either CC-BY or CC 0, which would adhere to normal academic
requirements of "I used this so I should cite it."

**For the data & analysis citation handle, what would be the
authorship?** My proposal is 1/2 and 1/2: my lab gets either first or
last, your lab gets the other one, and we do the rest alphabetically.

**Who would have access to the data during the embargo period?**
We're thinking of offering three options: (1) the data becomes available
immediately upon the analysis being completed; (2) the data can be used
for aggregate analysis by my lab and specifically named collaborators
during the 1-yr embargo period; or (3) the data can only be used by
my lab to do the analysis, and not for anything else by anyone other than
the original authors, until the 1-yr embargo is up.

The last option, (3), would potentially limit our ability to improve
your assembly and would certainly reduce the quality of the
annotations, but would be the most conservative and acceptable for
some.

**What license would the software and pipeline be under?** Oh, that's
actually easy. BSD/CC0: free for all to use, reuse, and abuse.

Where can you sign up?
~~~~~~~~~~~~~~~~~~~~~~

If you're potentially interested, `fill out this short form
<https://docs.google.com/forms/d/1db8vjraoeR3J5n0amdBAsvfssQqIu5tV-qtXacx0cEM/viewform>`__
and we'll let you know when we have all our ducks in a row.

Anything else you want to say, Titus?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Yep, two things:

First, we're looking for partners in crime.  If anyone wants to work
with us on this, we're game.  `Drop me a note
<mailto:titus@idyll.org>`__.

Second, this would be a sunlight operation: everything we did would be
freely and openly visible, excepting only the specifics of the data
where appropriate.  We have a really annoying culture of inside dealing
and data hoarding in evo devo, and I don't want to play that game.

I'd love your comments and thoughts.

--titus

p.s. Thanks to Andy Cameron for the Dead Sea Scrolls story!

.. @@ add MBL
.. @@ Moore effort
.. afterparty

.. include other people's transcriptomes that are already open 

.. Figshare or iplant; data cite pub if they pay.