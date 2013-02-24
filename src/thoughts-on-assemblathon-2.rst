Thoughts on the Assemblathon 2 paper
####################################

:author: C\. Titus Brown
:tags: science,assembly
:date: 2013-02-23
:slug: thoughts-on-assemblathon-2
:category: science

(Also see `Assemblathon 2 review, round 1, parts thereof <../2013-assemblathon-review-i.html>`__)

I just finished reviewing the `Assemblathon 2 paper
<http://arxiv.org/abs/1301.5406>`__, in which many of the extant de
novo genome assembly pipelines were evaluated against three different
organismal data sets.  (I'll post the review when I can.)  Good paper.

To me, the biggest outcome of the Assemblathon 2 paper can be stated
quite simply: we're doing it all wrong, in bioinformatics.  The paper
is, in some ways, an indictment of de novo assembly, and, more broadly
of all of sequence-based bioinformatics, and even more broadly, of all
of computational biology.

What the paper shows *unambiguously* is that on any reasonably
challenging genome, and with a reasonable amount of sequencing,
assemblers neither perform all that well nor do they perform
*consistently*.  You can accurately read that statement any way you
want: assemblers are sensitive to parameters (they produced different
results on the same data with small parameter tweaks); different
assemblers perform quite differently on the same data; the same
assembler with the same parameters performs differently on different
data sets.  This is all clearly stated in the Assemblathon paper, if
not always dwelled upon :).

What's my beef, exactly?

The paper accurately points out that different assemblers address
different goals, as Keith Bradnam says on `Haldane's Sieve
<http://haldanessieve.org/2013/01/28/our-paper-making-pizzas-and-genome-assemblies/>`__:

   "the best genome assembler is the one that ... best addresses what
   you want to get out of a genome assembly (bigger overall assembly,
   more genes, most accuracy, longer scaffolds, most resolution of
   haplotypes, most tolerant of repeats, etc.)

but we have been told, through a succession of papers in high profile
journals and with all of the various genome browsers, that here is THE
genome of mouse, here is THE assembly of zebrafish.  As a result, the
unwary biologist (which is many of them) will unwittingly trust the
assembly we have.  It is of course an open secret that some assemblies
are worse than others (just talk to a chick developmental biologist
about the chick genome sometime - stand back a bit first, though).
But as a field, we have pretended that genome assembly is a reliable
exercise and that the results can be trusted; the Assemblathon 2 paper
shows that that's wrong.

So, my first beef is that we have not done a good job of communicating
this uncertainty.

My second beef is that we have not done a good job of *managing* this
uncertainty.  If there's one group that should be eyeing the
Assemblathon 2 paper with concern, it's the sequencing and informatics
centers, who are increasingly trying to be a one-stop shop for genome
analysis.  The Assemblathon 2 paper basically points out that you
can't trust what they produce to be what you want, and (from personal
experience) I can tell you that very rarely do sequencing centers put
significant thought into your specific genome: it tends to be a
production pipeline using (shock! surprise!) what they already know
how to use, with a minimum of parameter sweeps.  When you connect this
to the Assemblathon 2 paper, what you get is a near-certain statement
that your genome assembly is worse -- perhaps *considerably* worse --
than it could be.  But nobody recognizes this explicitly, and our sequencing
centers are paid to produce sequence, not assemblies, much less *good*
assemblies, so the incentive isn't there to change.

So, what should we be doing?  Two things.

First, we should be building better, more automatic assemblers.
Sebastian Boisvert (@sebhtml) said something really smart about this:
something like, "Assemblers should take in your data and automatically
do the best possible job with it."  (I can't track down the reference,
though.)  YES, exactly.  For any new data set, we should automatically
run a bunch of assemblers and figure out which assemblies look best
according to a wide variety of metrics -- and we should work towards
making that decision more automatic.

Which brings me to the second thing we should be doing.  We should be
making sure that these assemblers can be run quickly, and efficiently,
on any given set of data.  This would let us actually *run* them and
*do* parameter sweeps, as opposed to now, where you need to have serious
computational infrastructure to run a lot of these assemblers.

Above, I made the claim that this paper is an indictment of much of
computational biology.  How so?

Because everything I say above is completely and entirely obvious to
anyone who has worked in computational science *outside* of biology.
I was trained on doing biology research with physicists and open
source programmers, who both have the perspective that all software is
wrong , although some of it is useful, and all results are
approximate.  This perspective is rare in computational biology
[#fyb]_.  And I think it needs to be far more common.

We need to recognize that different heuristic decisions in different
assemblers lead to different results.  We need to clearly state that
each assembly is a computational hypothesis, developed from noisy data
using approximate computation, and that this assembly must be treated
with skepticism.  And we need to stop treating the output of programs
published in peer-reviewed articles as if they are tablets handed down
from on high, correct until proven wrong -- they worked *once*, for
*one group*, but that hardly means they're robust or even particularly
correct.

Every computational biologist I know (myself included) bitches about a
lack of funding for this stuff.  In part the lack of funding is
because biologists *still* treat computation with disdain even as they
try to hire people adept at computation [#abby]_.  But in large part
it's because the people doing the computation never both to express
this uncertainty upwards, which means it never makes into the
high-poobah ranks of biology.  I get a lot of flak from collaborators
for doing so, but over the long term they watch the results morph in
front of their eyes into better and better *supported* results, and
they start to appreciate just how mutable computational output is.

So why don't we do a better job on computation?  It's mostly *our*
fault, the fault of the computational people doing biology. We can't
expect people who aren't expert in our area to understand this stuff;
we need to explain it to them.  And we aren't.

Bringing this back around to Assemblathon 2, I think someone should
spend some time figuring out *why* the different assemblers produce
such different results on basically the same data.  This was
completely missing from the paper (which is OK -- it wasn't its
purpose, and trust me when I say it's long enough already) but I think
it is one of the two most valuable things that could be done moving
forward.

--titus

.. [#fyb] Although you can read a bit about the consequences in `A
   farewell to bioinformatics
   <http://madhadron.com/a-farewell-to-bioinformatics>`__, which
   contains the memorable line, "Fuck you, bioinformatics. Eat shit
   and die." -- this has since become a mantra that my software
   engineer chants at me regularly.  Did I mention my lab is ...interesting?

.. [#abby] Which leads to the phenomenon described in my `Dear Abby
   post
   <http://ivory.idyll.org/blog/dear-abby-hiring-computational-people.html>`__.