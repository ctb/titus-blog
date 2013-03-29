How do sequencing errors modify de Bruijn graph connectivity? (Part II)
#######################################################################

:author: C\. Titus Brown
:tags: science,de Bruijn graphs,k-mers
:date: 2013-03-28
:slug: how-do-errors-modify-dbg-connectivity-ii
:category: science

Continuing in the saga of "what do sequencing errors do to our de Bruijn
graph density measure" (`read the first post here <http://ivory.idyll.org/blog/how-do-errors-modify-dbg-connectivity.html>`__), I have some new results.

The conclusion of the first post was that on random (non-real)
genomes, both with and without repeats, we see that de Bruijn graph
connectivity is *decreased* by random sequencing errors.  Zam Iqbal
and I had a reasonably robust discussion in the comments, and he
suggested trying a real genome.  (Yes, it was on my list.  But he
upped the ante by saying he didn't believe my results were relevant
because they weren't real genomes. Fair 'nuff!)

So I applied the `make-reads.py
<https://github.com/ctb/dbg-graph-null/blob/master/make-reads.py>`__
and `make-reads-biased-random.py
<https://github.com/ctb/dbg-graph-null/blob/master/make-reads-biased-random.py>`__
scripts to E. coli MG1655, and --

The results are in!

.. figure:: ../static/images/db-errors-ecoli.png
   :width: 400px

   Fig 1: Effects of errors on assembly graph density at radius=10 for E. coli MG1655.

Basically, we see the same effect as with Fig 1 in the `last post
<http://ivory.idyll.org/blog/how-do-errors-modify-dbg-connectivity.html>`__:
when there are more errors in the second half of the read, the average
local graph connectivity is lower.  Also note that (comparing the Y
axis levels in Fig 3 from the last post to Fig 1 above) E. coli isn't
very repetitive at all, which we kind of knew.

So, what could be going on?

1. E. coli isn't repetitive enough to give us a real test.  But I think it
   does directly address Zam's concern that the polymorphisms in IS elements
   and other repeats would lead to inadvertent connectivity -- it appears
   it's not *quite* that simple.

2. What we really need are metagenome-like abundances, which is to say
   multiple somewhat overlapping genomes with different abundances;
   this will then supply the necessary graph density increase in the
   face of random errors.  I'll be testing that next.

3. Aliens.  Some explanation we haven't thought of.

4. Our original explanation in the `assembly artifacts
   <http://arxiv.org/abs/1212.0159>`__ paper: the sequencer is sticking gunk
   on the end.

Obviously it's going to be hard to rule out #3, but I think we lay out
a pretty strong argument for #4 in the paper, at least once we can
rule out #2 and previous.

--titus
