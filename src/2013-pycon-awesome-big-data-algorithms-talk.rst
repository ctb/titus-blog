My 2013 PyCon talk: Awesome Big Data Algorithms
###############################################

:author: C\. Titus Brown
:tags: python,science,algorithms,find me maybe
:date: 2013-03-16
:slug: 2013-pycon-awesome-big-data-algorithms-talk
:category: python

`Schedule link <https://us.pycon.org/2013/schedule/presentation/53/>`__

**Description**

Random algorithms and probabilistic data structures are
algorithmically efficient and can provide shockingly good practical
results. I will give a practical introduction, with live demos and bad
jokes, to this fascinating algorithmic niche. I will conclude with
some discussions of how our group has applied this to large sequencing
data sets (although this will not be the focus of the talk).

**Abstract**:

I propose to start with Python implementations of most of the DS & A mentioned in this excellent blog post:

http://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/

and also discuss skip lists and any other random algorithms that catch
my fancy. I'll put everything together in an IPython notebook and add
visualizations as appropriate.

I'll finish with some discussion of how we've put these approaches to
work in my lab's research, which focuses on compressive approaches to
large data sets (and is regularly featured in my Python-ic blog,
http://ivory.idyll.org/blog/).

Misc talk links
~~~~~~~~~~~~~~~

`Slides <http://www.slideshare.net/c.titus.brown/2013-py-con-awesome-big-data-algorithms>`__

`Github repo with IPython Notebooks in it <https://github.com/ctb/2013-pycon-awesome-big-data-algorithms>`__

`Video link <https://www.youtube.com/watch?v=jKBwGlYb13w>`__

Overviews and linkfoo
---------------------

`Wikipedia's category page for Probabilistic Data Structures
<http://en.wikipedia.org/wiki/Category:Probabilistic_data_structures>`__

`The Highly Scalable Blog on Probabilistic Data Structures for Web
Analytics and Data Mining
<http://highlyscalable.wordpress.com/2012/05/01/probabilistic-structures-web-analytics-data-mining/>`__

Specific References
-------------------

SkipLists:
~~~~~~~~~~

`skiplist IPython Notebook <http://nbviewer.ipython.org/urls/raw.github.com/ctb/2013-pycon-awesome-big-data-algorithms/master/01-skiplist.ipynb>`__

`Wikipedia page on SkipLists
<http://en.wikipedia.org/wiki/Skip_list>`__

`John Shipman's excellent writeup
<http://infohost.nmt.edu/tcc/help/lang/python/examples/pyskip/pyskip.pdf>`__

`William Pugh's original article
<ftp://ftp.cs.umd.edu/pub/skipLists/skiplists.pdf>`__

The HackerNews (oops!) reference for my reddit-attributed quote about
putting a gun to someone's head and asking them to write a log-time
algorithm for storing stuff:
https://news.ycombinator.com/item?id=2670632

HyperLogLog:
~~~~~~~~~~~~

`coinflips IPython Notebook <http://nbviewer.ipython.org/urls/raw.github.com/ctb/2013-pycon-awesome-big-data-algorithms/master/02-coinflips.ipynb>`__

`HyperLogLog counter IPython Notebook <http://nbviewer.ipython.org/urls/raw.github.com/ctb/2013-pycon-awesome-big-data-algorithms/master/03-hyper-log-log-counter.ipynb>`__

`Aggregate Knowledge's EXCELLENT blog post on HyperLogLog
<http://blog.aggregateknowledge.com/2012/10/25/sketch-of-the-day-hyperloglog-cornerstone-of-a-big-data-infrastructure/>`__.
The section on Big Pattern Observables is truly fantastic :)

`Flajolet et
al. <http://algo.inria.fr/flajolet/Publications/FlFuGaMe07.pdf>`__ is
the original paper.  It gets a bit technical in the middle but the
discussions are great.

`Nick Johnson's blog post on cardinality estimation
<http://blog.notdot.net/2012/09/Dam-Cool-Algorithms-Cardinality-Estimation>`__

`MetaMarkets' blog post on cardinality counting
<http://metamarkets.com/2012/fast-cheap-and-98-right-cardinality-estimation-for-big-data/>`__

`More High Scalability blog posts, this one by Matt Abrams
<http://highscalability.com/blog/2012/4/5/big-data-counting-how-to-count-a-billion-distinct-objects-us.html>`__

`The obligatory Stack Overflow Q&A
<http://stackoverflow.com/questions/10164608/how-do-you-count-cardinality-of-very-large-datasets-efficiently-in-python>`__

Vasily Evseenko's git repo https://github.com/svpcom/hyperloglog,
forked from Nelson Goncalves's git repo,
https://github.com/goncalvesnelson/Log-Log-Sketch, served as the
source for my IPython Notebook.

Bloom Filters:
~~~~~~~~~~~~~~

`Bloom filter notebook <http://nbviewer.ipython.org/urls/raw.github.com/ctb/2013-pycon-awesome-big-data-algorithms/master/04-bloom-filters.ipynb>`__

The `Wikipedia page <http://en.wikipedia.org/wiki/Bloom_filter>`__ is pretty
good.

Everything I know about Bloom filters comes from `my research
<http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__.

I briefly mentioned the `CountMin Sketch
<http://en.wikipedia.org/wiki/Count-Min_sketch>`__, which is an
extension of the basic Bloom filter approach, for counting frequency
distributions of objects.

Other nifty things to look at
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Quotient filters <http://en.wikipedia.org/wiki/Quotient_filter>`__

`Rapidly-exploring random trees <http://en.wikipedia.org/wiki/Rapidly_exploring_random_tree>`__

`Random binary trees <http://en.wikipedia.org/wiki/Random_binary_tree>`__

`Treaps <http://en.wikipedia.org/wiki/Treap>`__

`StackOverflow question on Bloom-filter like structures that go the other way <http://stackoverflow.com/questions/13263220/is-there-any-probabilistic-data-structure-that-gives-false-negatives-but-not-fal>`__

`A survey of probabilistic data structures <http://www.slideshare.net/StampedeCon/a-survey-of-probabilistic-data-structures-stampedecon-2012>`__

`K-Minimum Values over at Aggregate Knowledge again <http://blog.aggregateknowledge.com/2012/07/09/sketch-of-the-day-k-minimum-values/>`__

`Set operations on HyperLogLog counters <http://blog.aggregateknowledge.com/2012/09/12/set-operations-on-hlls-of-different-sizes/>`__, again over at Aggregate Knowledge.

`Using SkipLists to calculate an efficient running median <http://code.activestate.com/recipes/576930-efficient-running-median-using-an-indexable-skipli/>`__

My research
-----------

`A fairly readable (?) grant on Big Data in sequencing data sets <http://ged.msu.edu/downloads/2012-bigdata-nsf.pdf>`__

`A less readable ;) grant on "infinite assembly" <http://ged.msu.edu/downloads/2012-career-nsf-final.pdf>`__

In addition to our `published paper on using Bloom filters to store
de Bruijn graphs <http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__, you might be interested in:

`Our preprint on streaming lossy compression of sequencing data <http://arxiv.org/abs/1203.4802>`__ (aka Digital Normalization)

`Our use of these techniques to assemble the heck out of large metagenomic data from soil <http://arxiv.org/abs/1212.2832>`__

`A chapter on optimizing our khmer software <http://arxiv.org/abs/1303.2223>`__.


--titus
