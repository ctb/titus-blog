How we make our papers replicable, v0.8 (beta)
##############################################

:author: C\. Titus Brown
:tags: replication
:date: 2014-07-15
:slug: 2014-our-paper-process
:category: science

----

0. Create a github repository named something like '2014-paper-xxxx'.
   Ask me for name suggestions.

   In that github repo, do the following:

1. Write a Makefile or some other automated way of generating all
   results from data - see

      https://github.com/ged-lab/2013-khmer-counting/blob/master/pipeline/Makefile

   or ask Camille (`@camille_codon
   <https://twitter.com/camille_codon>`__) what she is using.  The
   goal here is to go from raw data to directly interpretable data in
   as automated a fashion as possible.

   If queue submission or other scripts are involved, they should run
   the commands in the Makefile.  That is, all commands should (as
   much as possible) be in *one* place, and how they are executed is a
   bit less important.

2. Write a README explaining the above.  For example, see:

      https://github.com/ged-lab/2013-khmer-counting/blob/master/README.rst

   this README should describe versions of software and (as much as
   possible) give instructions that will work on Ubuntu 14.04.  It's
   OK if not all the commands will run on any given amazon machine
   (e.g. because of memory limitations); what's important is to have
   them all specified for a specific OS version, not whatever
   bastardized version of Linux (e.g.) our HPC uses.

3. Write an IPython Notebook that generates all the figures - see

      http://nbviewer.ipython.org/github/ged-lab/2013-khmer-counting/blob/master/notebook/khmer-counting.ipynb

   for an example.  This should take all of the data from the pipeline
   makefile (#1, above) and turn it into the production ready figures
   that go into the paper.

4. Write the paper in LaTeX, if at all possible, and write a Makefile
   to generate the final output file.  This is what we will submit to
   arXiv, submit to review, etc.

   See

      https://github.com/ged-lab/2013-khmer-counting/blob/master/Makefile

   for an example here.

----


Specific examples:

Pell et al., PNAS, 2012: https://github.com/ged-lab/2012-paper-kmer-percolation

Brown et al., arXiv, 2012: https://github.com/ged-lab/2012-paper-diginorm

Zhang et al., PLoS One, 2014: https://github.com/ged-lab/2013-khmer-counting

Feel free to deviate from the above but expect questions.  Tough questions.

--titus

