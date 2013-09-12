My review: "Toward a statistically explicit understanding of de novo sequence assembly"
#######################################################################################

:author: C\. Titus Brown
:tags: assembly,reviews
:date: 2013-09-11
:slug: 2013-review-howison
:category: science

The paper `Howison et al., 2013
<http://bioinformatics.oxfordjournals.org/content/early/2013/09/10/bioinformatics.btt525.full.pdf+html>`__,
just appeared in early form in Bioinformatics.  Here is my first round
review, which they handily addressed in their revisions; since I was
quite positive I felt I might as well post the whole thing, though.

Note that a relevant paper from Mihai Pop et al. came out right around
the time this paper was accepted; looks interesting. `"De novo
likelihood-based measures for comparing genome assemblies"
<http://www.biomedcentral.com/content/pdf/1756-0500-6-334.pdf>`__.

----

My review
~~~~~~~~~

Howison et al. provide a very good and timely review of efforts and
frameworks for assessing "assembly confidence", the likelihood that
any given assembly is correct.  I found the review very well written
and comprehensive.  I see no reason to require any changes.

However, if you asked me what I *thought* should be added to the paper... :)
I think some discussion of the following three topics would be useful.

The Assemblathon 2 paper reached the interesting, if unspoken,
conclusion that the current notion of "an assembly" is a fiction when
it comes to complex eukaryotic genomes, and that what we really have
is a series of oft rather significantly non-overlapping approximations
to the "true" genome.  Which approximation you get is a function of
who does the assembly, what they're interested in, and how motivated
they are in doing parameter optimization and assembly evaluation.  We
seriously need a set of unambiguous quality metrics for evaluation
that can be presented to assembly consumers... I think this is a
strong motivation for this question of confidence, and this point
(that assemblies are simply not that good, comprehensive, or
comparable) should be made clearly and strongly right up front in the
paper.  I don't think most people realize how bad the situation is!

Current efforts on confidence assessment are really focused on variant
calling, primarily SNPs but (as the authors note) also structural
variation.  I haven't seen much work on evaluating repeat content or
assembly sensitivity, or -- what I would think is most fundamental --
on the limits of what could be produced from the data vs what is
actually in the assembly.  Some work on this was done in the
Assemblathon paper but it was rather unsatisfactory, to my mind; mostly
focused on short-insert paired ends.  Another way to put it is, assemblers
throw away an awful lot of data; what is theoretically recoverable from
there?

Mihai Pop had an interesting comment here:

http://ivory.idyll.org/blog/thoughts-on-assemblathon-2.html

regarding amnesia about earlier efforts on assembly correctness.
Might be worth chasing him down for earlier references.

Titus Brown
ctb@msu.edu

----

--titus
