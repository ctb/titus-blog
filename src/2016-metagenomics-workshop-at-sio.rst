A shotgun metagenome workshop at the Scripps Institute of Oceanography
######################################################################

:author: C\. Titus Brown
:tags: metagenomics,ngs,workshop
:date: 2016-10-14
:slug: 2016-metagenomics-workshop-at-sio
:category: teaching

We just finished teaching a two day workshop at the Scripps Institute
of Oceanography down at UC San Diego.  `Dr. Harriet Alexander <http://twitter.com/nekton4plankton>`__, a postdoc
in my lab, and I spent two days going through
`cloud computing <https://2016-metagenomics-sio.readthedocs.io/en/latest/aws/index.html>`__,
`short read quality <https://2016-metagenomics-sio.readthedocs.io/en/latest/quality.html>`__
and
`k-mer trimming <https://2016-metagenomics-sio.readthedocs.io/en/latest/kmer_trimming.html>`__,
`metagenome assembly <https://2016-metagenomics-sio.readthedocs.io/en/latest/assemble.html>`__,
`quantification of gene abundance <https://2016-metagenomics-sio.readthedocs.io/en/latest/salmon_tutorial.html>`__,
`mapping of reads against the assembly <https://2016-metagenomics-sio.readthedocs.io/en/latest/mapping.html>`__,
`making CIRCOS plots <https://2016-metagenomics-sio.readthedocs.io/en/latest/circos_tutorial.html>`__,
and `workflow strategies for reproducible and open science <https://2016-metagenomics-sio.readthedocs.io/en/latest/workflow.html>`__.
We skipped the `slicing and dicing data sets with k-mers <https://2016-metagenomics-sio.readthedocs.io/en/latest/slice.html>`__, though -- not enough time.

Whew, I'm tired just writing all of that!

The workshop was delivered "Software Carpentry" style - interactive hands-on
walk throughs of the tutorials, with plenty of room for questions and
discussion and whiteboarding.

Did I mention we recorded? Yep. We recorded it. You can watch it on
YouTube, in four acts: `day 1, morning <https://www.youtube.com/watch?v=h3XBXTLmM8k>`__, `day 1, afternoon <https://www.youtube.com/watch?v=pGEVHPh9q6A>`__,
`day 2, morning <https://www.youtube.com/watch?v=F-Pj4YAWzcA>`__, and 
`day 2, afternoon <https://www.youtube.com/watch?v=uGVHi9EUA1I>`__.

Great thanks to Jessica Blanton and Tessa Pierce for inviting us down and
wrangling everything to make it work out!

The bad
-------

A few things didn't work out that well.

The materials weren't great
~~~~~~~~~~~~~~~~~~~~~~~~~~~

This was a first run of these materials, most of which were developed the
week of the workshop.  While most of the materials worked, there were
hiccups from the last minute nature of things.

Amazon f-ups
~~~~~~~~~~~~

Somewhat more frustrating, Amazon continues to institute checks that
prevent new users from spinning up EC2 instances.  It used to be that
new users could sign up a bit in advance of the class and be able to
start EC2 instances.  Now, it seems like there's an additional verification
that needs to be done AFTER the first phone verification and AFTER the first
attempt to start an EC2 instance.

The workshop went something like this:

Me: "OK, now press launch, and we can wait for the machines to start up."

Student 1: "It didn't work for me. It says awaiting verification."

Student 2: "Me neither."

Chorus of students: "Me neither."

So I went and spun up 17 instances on my account and distributed the
host names to all of the students via our EtherPad.  Equanimity in
the face of adversity...?

We didn't get to the really interesting stuff that I wanted to teach
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There was a host of stuff - genome binning, taxonomic annotation,
functional annotation - that I wanted to teach but that we basically
ended up not having time to write up into tutorials (and we wouldn't
have had time to present, either).

The good
--------

The audience interaction was great. We got tons of good questions, we
explored corners of metagenomics and assembly and sequencing and biology
that needed to be explored, and everyone was super nice and friendly!

We wrote up the materials, so now we have them! We'll run more of
these and when we do, the current materials will be there and waiting
and we can write new and exciting materials!

The location was amazing, too ;). Our second day was in a little classroom
overlooking the Pacific Ocean.  For the whole second part of the day you
could hear the waves crashing against the beach below!

The unknown
-----------

One of the reasons that we didn't write up anything on taxonomy, or
binning, or functional annotation, was that we don't really run these
programs ourselves all that much.  We did get some recommendations
from the Interwebs, and I need to explore those, but now is the time
to tell us --

* what's your favorite genome binning tool? We've had
  `DESMAN <https://github.com/chrisquince/DESMAN>`__ and
  `multi-metagenome <https://madsalbertsen.github.io/multi-metagenome/>`__
  recommended to us; any others?

* functional annotation of assemblies: what do you use? I was hoping
  to use `ShotMap <https://github.com/sharpton/shotmap/>`__.  I had
  previously balked at using ShotMap on assembled data, for several
  reasons, including its design for use on raw reads. But, after
  Harriet pointed out that we could `quantify the Prokka-annotated
  genes from contigs
  <https://2016-metagenomics-sio.readthedocs.io/en/latest/salmon_tutorial.html>`__,
  I may give ShotMap a try with that approach.  I still have to figure
  out how to feed the gene abundance into ShotMap, though.

* What should I use for taxonomic assignment?  Sheila Podell, the
  creator of `DarkHorse <http://darkhorse.ucsd.edu/index.html>`__, was
  in the audience and we got to talk a bit, and I was impressed with the
  approach, so I may give DarkHorse a try.  There are also k-mer
  based approaches like MetaPalette that I want to try, but my
  experience so far has been that they are extremely database
  intensive and somewhat fragile.  I'd also like to try marker gene
  approaches like `PhyloSift <https://peerj.com/articles/243/>`__.
  What tools are people using? Any strong personal recommendations?
  
* What tool(s) do people use to do abundance calculations for genes in their
  metagenome? I can think of a few basic types of approaches --

  * count raw reads that map to a particular gene sequence;

  * use `Salmon to quantify genes annotated on an
    assembly
    <https://2016-metagenomics-sio.readthedocs.io/en/latest/salmon_tutorial.html>`__,
    which is an extension of the above for when you didn't have the
    known set of genes;

  * translate reads and search against proteins;

...but I'm at a loss for specific software to use.
Any help appreciated - just leave a comment or `e-mail me at titus@idyll.org <mailto:titus@idyll.org>`__.

--titus
