Partitioning with khmer is not my recommended approach any more
###############################################################

:author: C\. Titus Brown
:tags: khmer,partitioning
:date: 2016-01-20
:slug: 2016-partitioning-no-more
:category: science

I wrote the below in response to someone who e-mailed me about
trying out `our partitioning approach <http://www.ncbi.nlm.nih.gov/pubmed/22847406>`__ for metagenome assembly.

----

yes, the original partitioning approach worked only on low coverage
data sets.  The main reason is that highly connected regions (repeats,
from biology; and some kinds of sequencing errors) are incredibly hard
to traverse.

Our `2014 paper <http://www.pnas.org/content/111/13/4904.short>`__
used a modified protocol, which included both digital normalization
and a "knot removal" approach.  This should work, but...

...since then, we've continued to refine the approach, but it's not something
we're actively working on.  A big part of the reason is that there are
some nifty new metagenome assemblers that resolve most of the problems
we set out to solve -- MEGAHIT is the one that we recommend.

If you're interested in genome separation/binning/strain extraction on
raw reads, the `Cleary et al. 2015 paper
<http://www.nature.com/nbt/journal/v33/n10/full/nbt.3329.html>`__ is
where I would look.  I wrote a `News and Views piece <http://www.nature.com/nbt/journal/v33/n10/abs/nbt.3375.html>`__ on it.

----

The leading edge of technology in metagenomics keeps on moving. Exciting
times ;).

--titus
