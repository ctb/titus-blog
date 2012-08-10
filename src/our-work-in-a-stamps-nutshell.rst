Our work in a nutshell (STAMPS metagenome version)
##################################################

:author: C\. Titus Brown
:tags: assembly,metagenomics
:date: 2012-08-09
:slug: our-work-in-a-stamps-nutshell
:category: science

Mixed community assembly
------------------------

Suppose you have a community that has two organisms in it, at widely
varying abundances.  What can you do?

.. image:: http://ivory.idyll.org/permanent/stamps-reads.png
   :width: 40%

Partitioning
------------

Partitioning takes this mixed distribution and, based on graph connectivity,
splits the reads into two bins.  Thus, you go from this:

.. image:: http://ivory.idyll.org/permanent/stamps-reads.png
   :width: 40%

to this:

.. image:: http://ivory.idyll.org/permanent/stamps-part2.png
   :width: 40%

where the reads are split into two bins, the green bin and the blue bin.

Digital normalization
---------------------

Digital normalization takes this mixed distribution and downsamples both
peaks so that they have the same abundance.  In doing so it discards
the vast majority of the data as well as the vast majority of the errors.

.. image:: http://ivory.idyll.org/permanent/stamps-reads.png
   :width: 40%

.. image:: http://ivory.idyll.org/permanent/stamps-dn.png
   :width: 40%

---

For more info as well as parameters to run these things, check out the
`STAMPS tutorial
<http://ged.msu.edu/angus/stamps-2012/basic-partitioning-and-diginorm.html>`__.
I'll post the raw files soon.

--titus
