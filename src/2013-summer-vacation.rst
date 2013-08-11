What I did on my summer vacation (2013)
#######################################

:author: C\. Titus Brown
:tags: mbl,pipelines,stamps,teaching
:date: 2013-08-10
:slug: 2013-summer-vacation
:category: science

I'm writing this as I travel to NY from Woods Hole, MA, where I spent
much of the last 6 weeks.  I was in Woods Hole to work and teach
at the Marine Biological Lab, one of two major research institutions
that call Woods Hole home.

I was at MBL for two reasons: first, I had received a summer
fellowship from the MBL to work on non-model transcriptomics in
general, and lamprey regeneration in particular; and second, I was
teaching a section on metagenome assembly at the `2013 Course on
Strategies and Techniques for Analyzing Microbial Population Structure
<http://hermes.mbl.edu/education/courses/special_topics/stamps.html>`__,
or STAMPS 2013.  (The summer fellowship was generously funded by the
Burr and Susie Steinbach Award and the Laura and Arthur Colwin Endowed
Summer Research Fellowship Fund, and covered my housing for the month
of July.)

So, what did I actually accomplish?  Two big things.

First, I put together a few presentations on metagenome assembly, as well
as a pretty detailed tutorial and some labs.  Specifically,

- `An Intro to Metagenome Assembly <http://www.slideshare.net/c.titus.brown/2013-stampsintroassembly-25057638>`__;

- `A Not So Practical Guide to Assembling Metagenomes <http://athyra.idyll.org/~t/2013-stamps-assembly-methods.pptx>`__;

- A repeat of my `pipelines lecture <http://athyra.idyll.org/~t/lecture5-pipelines.pptx>`__ from NGS 2013;

- A presentation on `k-mers and assembly <http://athyra.idyll.org/~t/2013-stamps-lab-1.pptx>`__ and four associated IPython Notebooks: `calculating kmer-abundances <http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/stamps13-render/01-kmer-abundance.ipynb>`__, `assembling E. coli with Velvet <http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/stamps13-render/02-assembly.ipynb>`__, `partitioning <http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/stamps13-render/03-partitioning.ipynb>`__, and `digital normalization <http://nbviewer.ipython.org/urls/raw.github.com/ngs-docs/ngs-notebooks/stamps13-render/04-diginorm.ipynb>`__;

- and a `detailed metagenome assembly protocol <http://ged.msu.edu/angus/2013-stamps/>`__.

The Not So Practical Guide presentation was a particularly challenging
presentation to put together, but one reason I value these teaching
opportunities so much is that they force me to explain myself to fairly
advanced scientific practitioners -- good for the soul.

Second, I wrote a detailed protocol on non-model transcriptome assembly
in the cloud, and worked with Josh Rosenthal at University of Puerto
Rico to make it correct and fairly robust.  I'll be running it by
some beta testers soon -- more on that in the next few weeks.

The truly excellent thing about this detailed protocol is that I think
it's nearing a point where we can do non-model transcriptomes in the
cloud for about $50 of compute time.  This would enable us to do a
pilot of a `crowdsourced transcriptomic pipeline for non-model
organisms
<http://ivory.idyll.org/blog/crowdsourced-analysis-with-data-privacy-sunset.html>`__;
if you're interested in this, drop me a note.

In the process of all of this work, I cleaned up a bunch of khmer
functionality; introduced (and then found and fixed) an annoying bug
in the development branch of khmer; discovered a few new ways to
measure and look at metagenomics; and generally had a pretty good
time.

A good summer "vacation"!

--titus
