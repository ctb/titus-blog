Our MEGAHIT review
##################

:author: C\. Titus Brown
:tags: assembly,megahit
:date: 2015-01-23
:slug: 2015-megahit-review
:category: science

It may not surprise peope to learn that I was one of the reviewers on
the MEGAHIT metagenome assembly paper... which `is now published!
<http://bioinformatics.oxfordjournals.org/content/early/2015/01/19/bioinformatics.btv033.short?rss=1>`__.

Below is my review, edited to remove all of the stuff they addressed
in their revision.

Please also see `our first blog post on MEGAHIT
<http://ivory.idyll.org/blog/2014-how-good-is-megahit.html>`__ and
Adam Rivers' `blog post on metatranscriptome assembly with MEGAHIT
<http://tinyecology.com/assembling-metatranscriptomes-megahit/>`__,
too!

It's worth noting that the evaluation I did for the first blog post
was used in the final paper ;). Successful adventures in peer review!

----

Li et al describe a new approach to metagenome assembly and provide an
implementation of this approach in the MEGAHIT software.  The new
approach constructs a succinct de Bruijn graph using multiple k-mers,
and uses a novel "mercy k-mer" approach that preserves low-abundance
regions of reads. They also use GPUs to accelerate the graph
construction.

The paper reads well.  The "mercy k-mer" approach is novel to
my knowledge, but makes intuitive sense.  The GPU implementation seems
to yield a significant improvement (although we did not test it). The
software is available, licensed under GPL, is fairly straightforward
to compile, and runs cleanly.  In our hands, it produced good results
on known datasets and ran extraordinarily fast and in low memory (see
below).  The authors are to be commended on all of this!

[ ... ]

See http://ivory.idyll.org/blog/2014-how-good-is-megahit.html for a
blog post on the evaluation we did. The authors should feel free to
take our makefile & results and build off of them; it's all under BSD
license.

----

In sum, I find this to be a great piece of software, with good
algorithmic insights, good implementation (at least from a cursory
usage), and lots of promise.

----

--titus
