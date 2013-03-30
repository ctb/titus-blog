How do sequencing errors modify de Bruijn graph connectivity?
#############################################################

:author: C\. Titus Brown
:tags: science,de Bruijn graphs,k-mers
:date: 2013-03-26
:slug: how-do-errors-modify-dbg-connectivity
:category: science

Are our reviewers correct or incorrect?

About two months ago we got back reviews for our `assembly artifacts
<http://arxiv.org/abs/1212.0159>`__ paper, in which we showed that
there was a strong 3' bias in the reads towards higher graph
connectivity.  Since shotgun sequencing is supposed to be random, we
asserted that this 3' bias was likely due to some sort of systematic
bias towards particular sequences being produced by the sequencing
machinery at the 3' end of reads.

Several of our reviewers disagreed.  The gist of the arguments was,
I think, that (a) everyone already knows that random error rates are
higher towards the 3' end of reads; (b) random errors cause
graph complexification by introducing new branches; and (c) these
random errors were sufficient to explain the results we saw.

Good point.  Our intuition was different (read on), but since we're
all scientists here, this question should not be settled by wild
guessing, but by exchanging data analysis at 50 paces.  And, as the
authors, it's our responsibility to make the argument.

Graph density
~~~~~~~~~~~~~

At the heart of our paper is this calculation of graph density.
In graph theory, there is a term "degree", which means "number
of edges connected to a node".  High-degree nodes are highly
connected, low-degree nodes are not.  If we wanted to investigate
graph connectivity in assembly graphs, why not simply use
'degree' and go from there?

Well, in DNA de Bruijn graphs, there are only a maximum of 8 edges for
any node (all possible combinations of A/T/C/G for the prefix and
suffix).  And there are quite a few nodes that have all 8 edges.  It's
not a particularly useful measure because of this.

So instead we developed a simple new measure which we call "graph
density" (I'm sure it isn't novel, it's just "new" in our heads).
This measure can be thought of as graph volume -- to calculate it, you
specify a radius and a starting node, and then walk in all directions
through the graph for 'radius' steps.  The density is then the
average number of new nodes per step.

If the graph is a linear graph with no branching, then each step will
bring you to at most two new nodes.  If the graph is highly
connected, then you can reach thousands or millions of nodes within a
short distance.

For the assembly artifacts paper, we showed that if you chose a radius
of 10 and started at the 3' end of a read, you would see a much higher
graph density -- indicating a much more highly connected graph --
than if you started walking the graph at the 5' end of the read.

Simulation results
~~~~~~~~~~~~~~~~~~

The question we wanted to investigate was, to what extent do
single-base sequencing errors affect our graph density calculation?
Our reviewers believed that random errors would lead to higher graph
density (model A); our intuition from our percolation paper was that
random errors would not connect the graph aberrantly (model B).

To answer this, I built a random genome and then sampled 100-base
reads from it with error, using as a base the script from the
`diginorm paper <http://arxiv.org/abs/1203.4802>`__.  I had three
error models: first, a random-uniform error model, in which errors
were assigned to reads `uniformly <https://github.com/ctb/dbg-graph-null/blob/master/make-reads.py>`__; second, a `3'-end-biased random
error model <https://github.com/ctb/dbg-graph-null/blob/master/make-reads-biased-random.py>`__, with the same overall per-base error rate as the
first model, but with twice the likelihood of errors past the midpoint
of a read; and third, `a systematic-bias error model <https://github.com/ctb/dbg-graph-null/blob/master/make-reads-biased-nonrandom.py>`__, a combination of
the random-uniform (#1) with the placement of a specific 32-base k-mer
at the end of the read for every 10k reads.

I generated a bunch of reads from the same random genome, loaded
them into a de Bruijn graph, and calculated the density of the first
100k reads.  I then plotted the density of the graph by starting position
in the read.

If model A is correct, then the 3'-end biased errors would lead to
a higher graph density towards the end of the read.  If model B is
correct, then the graph density towards the end of the read would
go down, because errors would make it less likely for the read to
connect to the rest of the graph.

In either case, we would expect to see lots of connectivity resulting
from the placement of a common sequence at the end of reads.

The results are below.

.. figure:: ../static/images/db-errors-bias.png
   :width: 400px

   Fig 1: Effects of errors on assembly graph density at radius=10.

Within the parameters of the simulation, it's clear that model B
holds: random errors cause decreases in graph connectivity. The
question is, why? And if we add more complexity to the simulation, by,
for example, adding repetitive sequences characteristic of real
genomes, will we get different results?

The intuition that I think explains the results is this: random errors
do introduce more graph complexity, but only in a very local sense.
That is, random errors introduce new branches to the assembly graph,
but these branches are "sterile" -- they do not connect to any other
parts of the graph.  This is directly connected to the percolation
results we observed in our `PNAS paper <http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__, where we showed that below a
certain level of occupancy in an implicit de Bruijn graph, random
long-distance connections do not form spontaneously.

Another way to put this is that the fastest way to increase graph
complexity is by introducing spurious connections between real
components, rather than adding new nodes.  You can see this quite
clearly with the 1-in-10,000 connections formed by the red line.

OK, so why shouldn't you believe me?

1. This was done for a high-coverage graph, not a low-coverage graph.
   (You can see this by looking at the Y axis above.)  Things could
   be very different for a low-coverage graph.

2. The error rates may not be representative.  We used a fixed error
   rate of 1%; maybe higher error rates would have different effects.

3. Repeats! It's not clear what effect repeats will have in combination
   with these error rates.

In the first two cases, I believe that we can be guided by the de
Bruijn graph percolation paper, which suggests that it is solely the
occupancy of the graph that matters.  So I may not pursue this avenue
further; I think intuition, theory, and simulation agree.

For repeats, simulations are the next step, I think.

What happens with repeats?
~~~~~~~~~~~~~~~~~~~~~~~~~~

To figure out the effect of repeats on local graph density,
`I made a genome with repeats <https://github.com/ctb/dbg-graph-null/blob/master/make-random-genome-with-repeats.py>`__.  This is a 10% repetitive genome,
with a 1kb repeat spread uniformly throughout the genome.

.. figure:: ../static/images/db-errors-bias-rep.png
   :width: 400px

   Fig 3: Effects of errors on assembly graph density when repeats
   are present in the genome.

While the overall graph density goes up with repeats, the trend towards
lower graph density with errors continues.

How dependent is graph density on radius?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another interesting question is, what does the graph density look like
for different values of the radius?  I looked at the 3' biased random
errors for r=1, r=3, r=5, and r=10.

.. figure:: ../static/images/db-errors-bias-radii.png
   :width: 400px

   Fig 3: Effects of errors on assembly graph density at radius=10,
   for 3' biased random errors.

Somewhat to my surprise, random errors cause a decrease in graph
density even for very small radii.  What?

At this point I rechecked my simulation script.  It seems to work --
there were 2 times as many errors in the second half of the reads
as in the first -- see Figure 4.

.. figure:: ../static/images/db-errors-bias-errorcount.png
   :width: 400px

   Fig 4: Positions of random errors.

I don't understand the result in Fig 3.  I would have expected small
radiuses (r=1, or r=3) to increase in graph density with random errors.
But I see the same trend as for larger radiuses.  Must think more.

Concluding thoughts
~~~~~~~~~~~~~~~~~~~

All of this bolsters our conclusion that the increase in
local graph density seen in our Illumina data sets at the 3' end of
reads is due to something other than random errors.

The next step is to experiment with different coverage levels, as in a
diverse metagenome.  I don't expect that to change things, but might
as well check it out!

I don't know that simulations are going to settle this completely, but
I hope we can reach an agreement with the reviewers that the situation
is more complicated than they thought.  (We will probably soften the
language on systematic bias, too ;).  I do have to say that I really
like this feature of science: the reviewers had one particular intuition,
we had another, and we failed to argue properly in the paper for ours.
They correctly called us on it, and we are responding with data! and
simulations! showing that our intuition is at least not completely
wrong.  Science FTW!

One thing that we saw at some distant point in the past was that you
might be able to split the sequences into two bins -- those with high
graph connectivity, and those without.  It might be time to revisit
that in the context of our simulations above: for the red line, do we
see that there are some sequences with extremely high connectivity
that contribute to almost all of the graph complexity, and many others
without high connectivity?  That would let us get a much better
handle on which sequences are contributing to this.

If you want to play with the code, go visit the source code for the simulations
`here on github <https://github.com/ctb/dbg-graph-null>`__.  You'll also
need the `'ctb' version of khmer <http://github.com/ctb/khmer/>`__.
You can check out the IPython Notebook for graphing `here <http://nbviewer.ipython.org/urls/raw.github.com/ctb/dbg-graph-null/master/dens.ipynb>`__.

--titus


.. why default graph density so high?
.. 2 phase - low connect, high connect.
