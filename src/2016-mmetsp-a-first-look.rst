Bashing on monstrous sequencing collections
###########################################

:author: C\. Titus Brown
:tags: mmetsp, khmer-protocols, rnaseq
:date: 2016-04-08
:slug: 2016-mmetsp-a-first-look
:category: science

So, there's this fairly large collection of about 700 RNAseq samples,
from 300 species in 40 or so phyla.  It's called the Marine Microbial
Eukaryotic Transcriptome Sequencing Project (MMETSP), and was funded
by the Moore Foundation as a truly field-wide collaboration to improve
our reference collection for genes (and more).  Back When, it was
sequenced and assembled by the `National Center for Genome Resources
<http://ncgr.org/>`__, and published in PLOS Biology `(Keeling et
al., 2014)
<http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001889>`__.

Partly because we think assembly has improved in the last few years,
partly as an educational exercise, partly as an infrastructure
exercise, partly as a demo, and partly just because we can, Lisa Cohen
in my lab `is starting to reassemble all of the data - starting with
about 10%
<https://monsterbashseq.wordpress.com/2016/04/07/marine-microbes-what-to-do-with-all-the-data/>`__.
She has some of the basic evaluations (mostly via `transrate
<http://hibberdlab.com/transrate/>`__) posted, and before we pull the
trigger on the rest of the assemblies, we're pausing to reflect and to
think about what metrics to use, and what kinds of resources we plan
to produce.  (We are not lacking in ideas, but we might be lacking in
*good* ideas, if you know what I mean.)

In particular, this exercise raises some interesting questions that we
hope to dig into:

* what does a good transcriptome look like, and how could having 700
  assemblies help us figure that out? (hint: distributions)
  
* what is a good canonical set of analyses for characterizing transcriptome
  assemblies?
  
* what products should we be making available for each assembly?

* what kind of data formatting makes it easiest for other bioinformaticians
  to build off of the compute we're doing?

* how should we distribute the workflow components? (Lisa really likes shell
  scripts but I've been lobbying for something more structured. 'make' doesn't
  really fit the bill here, though.)

* how do we "alert" the community if and when we come up with better
  assemblies? How do we merge assemblies between programs and efforts,
  and properly credit everyone involved?
  
Anyway, feedback welcome, here or on `Lisa's post
<https://monsterbashseq.wordpress.com/2016/04/07/marine-microbes-what-to-do-with-all-the-data/>`__!
We are happy to share methods, data, analyses, results, etc. etc.

--titus

p.s. Yes, that's right. I ask new grad students to start by
  assemblying 700 transcriptomes. So? :)
