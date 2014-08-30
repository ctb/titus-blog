Estimating (meta)genome size from shotgun data
##############################################

:author: C\. Titus Brown
:tags: khmer
:date: 2014-08-28
:slug: 2014-estimate-genome-size-shotgun
:category: science

This is a recipe that provides a time- and memory- efficient way to
loosely estimate the likely size of your assembled genome or
metagenome from the raw reads alone.  It does so by using digital
normalization to assess the size of the coverage-saturated de Bruijn
assembly graph given the reads provided by you.  It *does* take into
account coverage, so you need to specify a desired assembly coverage -
we recommend starting with a coverage of 20.

Uses for this recipe include estimating the amount of memory required
to achieve an assembly and providing a lower bound for metagenome
assembly size and single-copy genome diversity.

This recipe will provide inaccurate estimates on transcriptomes (where
splice variants will end up confusing the issue - this looks at
single-copy sequence only) or for metagenomes with high levels of
strain variation (where the assembler may collapse strain variants
that this estimate will split).

----

Note: at the moment, the khmer script ``normalize-by-median.py`` needs
to be updated from the master branch of `khmer
<https://github.com/ged-lab/khmer>`__ to run this code properly.  Once
we've cut a new release, we'll remove this note and simply specify the
khmer release required.

.. shell start

.. ::

   . ~/dev/ipy7/bin/activate
   
   # make a 500 bp repeat
   python ~/dev/dbg-graph-null/make-random-genome.py -l 500 -s 10 > repeat.fa
   
   # create a genome with 5kb unique sequence interspersed with 5x 500 bp
   # repeats.
   echo '>genome' > genome.fa
   cat repeat.fa | grep -v ^'>' >> genome.fa
   python ~/dev/dbg-graph-null/make-random-genome.py -l 1000 -s 1 | grep -v ^'>' >> genome.fa
   cat repeat.fa | grep -v ^'>' >> genome.fa
   python ~/dev/dbg-graph-null/make-random-genome.py -l 1000 -s 2 | grep -v ^'>' >> genome.fa
   cat repeat.fa | grep -v ^'>' >> genome.fa
   python ~/dev/dbg-graph-null/make-random-genome.py -l 1000 -s 3 | grep -v ^'>' >> genome.fa
   cat repeat.fa | grep -v ^'>' >> genome.fa
   python ~/dev/dbg-graph-null/make-random-genome.py -l 1000 -s 4 | grep -v ^'>' >> genome.fa
   cat repeat.fa | grep -v ^'>' >> genome.fa
   python ~/dev/dbg-graph-null/make-random-genome.py -l 1000 -s 5 | grep -v ^'>' >> genome.fa
   
   # build a read set
   python ~/dev/dbg-graph-null/make-reads.py -C 150 genome.fa > reads.fa

Let's assume you have a simple genome with some 5x repeats, and you've
done some shotgun sequencing to a coverage of 150 or higher.  If your reads are
in ``reads.fa``, you can get an estimate of the single-copy genome size
(here known to be 5500 bp) by running ``normalize-by-median.py``
::
   
   ~/dev/khmer/scripts/normalize-by-median.py -x 1e8 -k 20 -C 20 -R report.txt reads.fa 
   ./estimate-genome-size.py -C 20 -k 20 reads.fa.keep report.txt

This yields the output::

   Estimated (meta)genome size is: 8727 bp

This is off by about 50% for reasons that we don't completely
understand.  Note that you can get more accurate estimates for this
data set by increasing C and decreasing k, but 20/20 should work
about this well for most data sets. (For an E. coli data set, it
returns 6.5 Mbp, which is only about 25% off.)


Resources and Links
~~~~~~~~~~~~~~~~~~~

`This recipe
<https://github.com/ged-lab/khmer-recipes/tree/master/003-estimate-genome-size>`__
is hosted in the khmer-recipes repository,
https://github.com/ged-lab/khmer-recipes/.

It requires the `khmer software <http://khmer.readthedocs.org>`__.

--titus

