PyCon 2015 talk notes for "How to interpret your own genome"
############################################################

:author: C\. Titus Brown
:tags: python,pycon,genomics,human genetics
:date: 2015-04-10
:slug: 2015-pycon-talk
:category: science

Here are talk notes and links for `my PyCon 2015 talk <https://us.pycon.org/2015/schedule/presentation/410/>`__.

The talk slides are `up on SlideShare <http://www.slideshare.net/c.titus.brown/2015-pycontalk>`__.

----

General background
==================

You should definitely check out `Mike Lin's great blog posts on "Blogging my genome" <http://blog.mlin.net/p/blogging-my-genome.html>`__.

I found `SNPedia <http://snpedia.com>`__ through this wonderful blog post on
`how to use 23andMe irresponsibly <http://slatestarcodex.com/2014/11/12/how-to-use-23andme-irresponsibly/>`__, on Slate Star Codex.

My introduction to bcbio came from `Brad Chapman's excellent blog post <http://bcb.io/2013/05/06/framework-for-evaluating-variant-detection-methods-comparison-of-aligners-and-callers/>`__ on evaluating and comparing variant detection methods.

There are several openly available `benchmarking data sets <http://gatkforums.broadinstitute.org/discussion/1292/which-datasets-should-i-use-for-reviewing-or-benchmarking-purposes>`__ for human genetics/genomics.  The Ashkenazim data set
I used for my talk `is here <https://sites.stanford.edu/abms/content/giab-reference-materials-and-data>`__, and you can see the `Personal Genome Project profile for the son, here <https://my.pgp-hms.org/profile_public?hex=huAA53E0>`__.
The raw data is `available here <ftp://ftp-trace.ncbi.nih.gov/giab/ftp/technical/NISTAshkenazimTrio/>`__, and you can see the `resequencing report for the son, here <ftp://ftp-trace.ncbi.nih.gov/giab/ftp/technical/NISTAshkenazimTrio/HG-002_Homogeneity-10953946/HG002Run01-11419412/HG002run1_S1.report.html>`__.

`The Personal Genome Project <http://www.personalgenomes.org/>`__ is something
worth checking out.

More and more of human genetics and genomics is "open" -- check out the
Variant Call Format (VCF) spec, `now on github <https://github.com/samtools/hts-specs>`__.

Follow-on links
===============

If you're interested in keeping up with human genomics, Twitter is a
pretty good place to go.  I asked who to follow and got a great list
-- `go here
<https://twitter.com/ctitusbrown/status/586537235723366401>`__.

----

Pipeline
========

To run the bcbio variant calling pipeline I discuss in the talk, or
examine the SNPs in the Ashkenazim trio with Gemini, take a look at
`my pipeline notes
<https://github.com/ctb/2015-pycon-talk/blob/master/AWS.rst>`__.
The Gemini part will let you examine SNPs for the three individuals
in the Ashkenazi trio, starting from the VCF files.

.. Slide notes

How to get involved
===================

I asked the `bcbio <https://github.com/chapmanb/bcbio-nextgen>`__ and
`gemini <https://github.com/arq5x/gemini/>`__ folk if there were any
opportunities for Python folk to get involved in their work.

Here are some of their thoughts:

* fixing the slowness of bigwig parsing in bx-python would be a great
  project. See my last comment here which
  pinpoints the bottleneck:

    https://bitbucket.org/james_taylor/bx-python/issue/38/read-a-bigwig-file-is-slow

* another good "open" project is the SQLite to PostgreSQL conversion to help
  provide improved speed for larger input files. There is some in-progress
  work from Aaron Quinlan on this branch:

     https://github.com/arq5x/gemini/tree/postgresql

* From the bcbio side, the biggest help we could use from non-biology
  technical folks is improving the use and cleanliness of the Cloud port:

     https://bcbio-nextgen.readthedocs.org/en/latest/contents/cloud.html

  and in moving to use the common workflow language (CWL) as a backend for
  running computations:

     https://github.com/common-workflow-language/common-workflow-language

  For folks with workflow/distributed experience, there is a reference
  implementation in Python that needs extension and parallelization:

     https://github.com/common-workflow-language/common-workflow-language/tree/master/reference

----


