New findings from our paper, "These are not the k-mers you are looking for"
###########################################################################

:author: C\. Titus Brown
:tags: khmer, k-mer counting, reviews
:date: 2014-05-15
:slug: 2014-more-on-khmer-counting
:category: science

Earlier today, `I posted
<http://ivory.idyll.org/blog/2014-response-to-reviewers-khmer-counting.html>`__
our response to `the reviewers' comments
<http://ivory.idyll.org/blog/khmer-counting-reviews.html>`__ on our
`k-mer counting paper, "These are not the k-mers you are looking for:
efficient online k-mer counting using a probabilistic data structure
<http://ivory.idyll.org/blog/2013-khmer-counting-paper.html>`__.

A side note -- I was wondering how many public examples there are of
the whole paper submission/review/responses to reviewer/revised paper
submission cycle?  And how many of them weren't legally compelled?
(Thanks to our reviewers for letting us post their reviews publicly!)

As you can see, our reviewers were *very* thorough and we put in a lot
of work in the response; the paper is now dramatically better and
considerably more solid.  In the process we discovered a few new things.

---

New factoids from the paper
---------------------------

1. Digital normalization is remarkably refractory to high k-mer counting
   false positive rates.

   At the request of the reviewers, we got down to the point where we
   were running digital normalization on an E. coli data set at a
   false-positive rate of 98.8%, in 20 MB of RAM, before we saw any
   ill effects of low-memory diginorm.  (See output at tab 111 in `our
   IPython Notebook
   <http://nbviewer.ipython.org/github/ged-lab/2013-khmer-counting/blob/36a8a0c5254412225ca343cd7bf5559b4a792e8d/notebook/khmer-counting.ipynb#Tables>`__
   for details.)

2. k-mer abundance trimming is incredibly effective at getting rid of
   errors.  See output at tab 109 in `our IPython Notebook
   <http://nbviewer.ipython.org/github/ged-lab/2013-khmer-counting/blob/36a8a0c5254412225ca343cd7bf5559b4a792e8d/notebook/khmer-counting.ipynb#Tables>`__;
   filtering by quality scores leaves at least 1000x more unique
   k-mers in a high coverage data set (and yes, these are certain to
   be errors).  Now that fairly low-memory k-mer trimming approaches
   are available, we may switch our protocols over to k-mer trimming
   only (and avoid quality score trimming altogether).

3. `Turtle <http://www.ncbi.nlm.nih.gov/pubmed/24618471>`__ is remarkably fast, and `KAnalyze <http://www.ncbi.nlm.nih.gov/pubmed/24642064>`__ is not very fast in our hands.

   You can read the details in our paper, but in our hands, KAnalyze
   was slower than everything but Tallymer; counter to the claims in
   their paper, Jellyfish and DSK (as well as KMC, BFCounter, Turtle,
   and khmer) all beat KAnalyze. `See the figure in our IPython
   Notebook
   <http://nbviewer.ipython.org/github/ged-lab/2013-khmer-counting/blob/36a8a0c5254412225ca343cd7bf5559b4a792e8d/notebook/khmer-counting.ipynb#Figure-1---time-usage-of-different-k-mer-counting-tools>`__.

   Now, before anyone argues with us about the details, I'd like to
   point out that our analysis is **completely open** and remarkably
   **reproducible**.  We ran everything in the Amazon cloud, with open
   source and open data, and you can run it too, if you like -- `see
   our tutorial
   <https://github.com/ged-lab/2013-khmer-counting/blob/36a8a0c5254412225ca343cd7bf5559b4a792e8d/tutorial.rst>`__. If
   you get different results, let us know, m'kay?

   In any case, we believe (but have not verified) that the source of
   the speed discrepancy in the KAnalyze paper is caused by their use
   of custom parsing scripts to rewrite other k-mer counters' output
   into their format.  Regardless, our paper *almost* directly refutes
   their claims (we'd have to do the benchmarks on their data to
   refute directly).  Any thoughts on what to do about this?

--titus
