Trying (and failing?) to build a Scalable CountMin Sketch
#########################################################

:author: C\. Titus Brown
:tags: data structures,khmer
:date: 2014-05-30
:slug: 2014-scalable-cms-problems
:category: science

.. @HN?
.. @scatterbean, @bitly

(or, What I Did For One Day Of My Summer Vacation.)

----

tl;dr? I played around with building a CountMin Sketch that is dynamic
in size, based on a scalable Bloom Filter approach.  I'm not sure it
worked.  Thoughts, suggestions, help?

Bloom Filters
-------------

In our research, we've made some hay using `Bloom filters
<http://en.wikipedia.org/wiki/Bloom_filter>`__.  They're remarkably
easy to implement; I've talked about them a couple of times on my blog
-- `take a look at my PyCon 2013 talk, for example
<http://ivory.idyll.org/blog/2013-pycon-awesome-big-data-algorithms-talk.html>`__
-- but it's almost easiest to just introduce them with pseudocode.

Bloom filters are data structure that allow presence/absence queries;
they implement two functions, add(obj) and query(obj), that
respectively let you add an object into the filter and query for the
presence of an object.  Here's a simple Python implementation of a sliced
Bloom filter::

   N = ...           # a number >= 1, and not that big
   primes = [ ... ]  # N prime numbers

   filters = []
   for i in range(N):   # create N arrays of [0], each w/a prime # of entries
      filters.append([0] * primes[i])

   def add(obj):
      h = hash(obj)
      for i, filter in enumerate(filters):
          address = h % primes[i]
          filter[address] = 1

   def query(obj):
      h = hash(obj)
      for i, filter in enumerate(filters):
          address = h % primes[i]
          if not filter[address]:
              return False

      return True

Essentially you're recording the presence of objects by flipping N
bits to 1 for each object, and upon a query, examining the bits that
*would* have been flipped to 1 to see to see if they are all actually
1.  If they are, you cry huzzah, and say that the object is there;
if they aren't, you know that the object isn't there.

The main thing to understand about Bloom filters is that they are
*probabilistic*.  There's some probability that when you query for the
presence of a particular object, you return a "True" even when the
object isn't there.  This happens when all of the bits that correspond
to a particular object are set because they belong to *other* objects
that have been inserted.  However, this error is one-sided -- you
never falsely claim that an object *isn't* present, just (sometimes)
that it *is*.  The error rate depends on the size of the Bloom filter
and how many objects you stick in it, and it is fairly straightforward
to calculate (see `our khmer-counting paper
<http://arxiv.org/abs/1309.2975>`__ for some references).

Bloom filters are also tricky because they are constant in size.  In
the construction above, you specify the total size of the Bloom
filters as the sum of the prime numbers, and you cannot increase its
size without re-creating it and re-adding all of the objects.  In some
situations this is ideal: Bloom filters never increase in size, so
you never run out of memory when inserting elements.  However, in
situations where you don't know how many elements you have, you may
*want* to be able to increase the size.

Enter... scalable bloom filters!

Scalable Bloom filters
----------------------

`Scalable Bloom filters
<http://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf>`__ are one of a
`near-infinite set of Bloom filter derivatives and extensions <http://www.dca.fee.unicamp.br/~chesteve/pubs/bloom-filter-ieee-survey-preprint.pdf>`__.  The
main thing that scalable Bloom filters provide is dynamic scaling:
they let you make use of the (super efficient) Bloom filter storage
without fixing memory usage a priori.

(See Jay Baird's excellent `python-bloomfilter project <https://github.com/jaybaird/python-bloomfilter>`__ for the implementation of the scalable Bloom
filter that made me first understand how they worked.)

They do this in a brilliantly simple way, using Bloom filters as a building
block.  Essentially you maintain a *list* of Bloom filters::

   blooms = [ BloomFilter(size0) ]
   
and then the 'add' operation checks to see if the element is already present
in one of the Bloom filters already in the list, and if not, adds it to
the last one::

   def add(obj):
      for b in reversed(blooms):
         if b.query(obj):
            return

      # not there? add!
      b = blooms[-1]
      if b.is_at_capacity():
         b = BloomFilter(sizeN)
         blooms.append(b)

      b.add(obj)

The query then looks for the element in each of
the Bloom filters::

   def query(obj):
       for b in reversed(blooms):
           if b.query(obj):
              return True
       return False

The important bit here is the 'if b.is_at_capacity()' condition.  What
the scalable Bloom filter does is successively allocate and fill new
Bloom filter tables *as old ones fill up*.  This means that the
overall memory consumption goes up as new objects arrive.

There are some tricks needed to make this work -- you need to define
the progression in table sizes as you load in more elements, and you
need to ratchet down the false positive rate of later tables so as to
maintain an overall acceptable false positive rate -- but it's very
easy to implement a dynamically scaling Bloom filter.

The scalable version is not quite as efficient as the static Bloom
filter; if you look at figure 2 in the `SBF paper
<http://gsd.di.uminho.pt/members/cbm/ps/dbloom.pdf>`__ you'll see that
depending on the parameters, you can get between 1.5 and 4x loss in
memory efficiency over a static filter, depending on the desired
performance.

The CountMin Sketch
-------------------

Imagine that instead of mere element presence/absence you want to get
the *frequency distribution* of elements -- how many elements show up
once, or twice, or 50 times?  You can modify the Bloom filter to keep
totals, like so::

   N = ...           # a number >= 1, and not that big
   primes = [ ... ]  # N prime numbers

   filters = []
   for i in range(N):   # create N arrays of [0], each w/a prime # of entries
      filters.append([0] * primes[i])

   def add(obj):
      h = hash(obj)
      for i, filter in enumerate(filters):
          address = h % primes[i]
          filter[address] += 1           # changed to increment @ each location

   def query(obj):
      h = hash(obj)
      count = 0
      for i, filter in enumerate(filters):  # changed to take min across all
          address = h % primes[i]
          count = min(count, filter[address])

      return min

The behavior of this is similar to the Bloom filter: fixed size, some
probability that you have an overcount, but *very* memory efficient
for keeping track of counts.  `(See the khmer counting paper
<http://arxiv.org/abs/1309.2975>`__ for our exploration of this in
relation to sequence analysis.)

Can we build a scalable CountMin Sketch?
----------------------------------------

For several Reasons, we'd really like to have a CountMin Sketch that
behaved like a scalable Bloom filter: dynamic size, but still memory
efficient.  (I also like the simplicity of the scalable Bloom filter
-- there are other memory-efficient data structures, but they all look
difficult to implement, which means I'd have to spend a lot of time
debugging them.)  Since the scalable Bloom filter is based on,
basically, a bunch of Bloom filters -- why not use the same idea with
a CountMin Sketch? What happens if we extend the concept of the
scalable Bloom filter to build on a CountMin Sketch?

Conveniently, we already have a good-performing implementation of a
CountMin Sketch in the `khmer project
<https://github.com/ged-lab/khmer>`__ (implemented in counting.cc and
counting.hh).  And as we saw above, it's pretty easy to implement a
scalable Bloom filter.  So... voila! I implemented `a simple scalable
CountMin Sketch data structure
<https://github.com/ged-lab/khmer/blob/0d6babeedf11aefd0bde22da23106d7ead2ad865/sandbox/scalable_cms.py>`__.

Testing it out
~~~~~~~~~~~~~~

To evaluate this scalable CMS, I wrote a little bit of test code (at
the bottom of the file).  The __main__ block of our scalable_cms.py
creates a counter, and then adds 10,000 random objects to it (in this
case, k-mers -- but it doesn't really matter).  Then it outputs the
counts of each of the things it added, to check for accuracy.  Here's
the output::

   Creating new ScalableCounter: growth rate 2, error ratio 0.50, bound 0.100
   added new table of size 512/capacity 427 (now 1 tables total)
   ...added 0
   last table is full! 427 counts, FP rate 0.093
   added new table of size 1024/capacity 656 (now 2 tables total)
   ...added 1000
   last table is full! 656 counts, FP rate 0.057
   added new table of size 2048/capacity 1066 (now 3 tables total)
   ...added 2000
   last table is full! 1066 counts, FP rate 0.025
   added new table of size 4096/capacity 1796 (now 4 tables total)
   ...added 3000
   ...added 4000
   last table is full! 1796 counts, FP rate 0.016
   added new table of size 8192/capacity 3102 (now 5 tables total)
   ...added 5000
   ...added 6000
   ...added 7000
   ...added 8000
   last table is full! 3102 counts, FP rate 0.010
   added new table of size 16384/capacity 5458 (now 6 tables total)
   ...added 9000
   TCCTATACATTCGCAGATTG 5
   GAAATCTGAGCGCACGTCCA 3
   TGCTAGGTTAATGATGTGAA 1
   GCGGCGGTACCTCCGATAGC 2
   ACATTCTCCTCCACCCTGCT 4
   AGTGGAAGAGCCTCCGATTG 3
   ATACGCGCGTTGTCATACGT 3
   TGGCTAGGCTTTTTCCCACG 1
   GGCTTCACCGGGGCGTTACA 4
   GGTCGGACTATCCTGTGGAA 1
   total memory used: 129.6k
   average miscount: 0.4294

You can see a couple of things going on here.

First, note that things proceed as expected.  As we add more counts,
the last table saturates, and then we add a new one that's bigger.
Huzzah!

Second, the parameters: the growth rate ('s' in the scalable Bloom
filter paper) is the rate at which we grow the size of each additional
table, while the tightening ratio ('r' in the paper) is related to the
factor by which we clamp down on the allowable error in each
successive table.  You can see the effects of the growth rate and
tightening ratio by looking at the sizes of each successive table
(512, then 1024, then 2048...) and the capacity for each table (427
for the first, 656 for the second, 1066 for the third...)

Third, the counts.  I output the average miscount and the counts of
the first 10 things added to the table.  The average miscount (the
average number by which we're off from the true count) is 0.0!
But... if we're adding each random k-mer once, the counts should all
be one.  Why do we have so many counts that are *higher* than one?

Ruh-roh
~~~~~~~

It took me a long time to figure this out, but it spells doom for this
idea, at least without modification.

First, let me show you the output if I choose objects at random,
rather than in the order I added them::

   Creating new ScalableCounter: growth rate 2, error ratio 0.50, bound 0.100
   ...
   shuffling items
   TCAGAGCTCAACTTATCCCA 1
   GTGGGGCTATAATTCTCGCG 1
   AACGCTTGCAAGGTAAGAGT 1
   CTAGTAGACTAGACCTGGCA 1
   GACTCATCTGACCTTGAAGG 2
   AGCCGCTGGGTCACTTTCAG 2
   GTATCAGTAGGTCCCCAACA 3
   AGGGCGCTCCTATACGTCGA 2
   TGCCGACGAGATCACCTCGA 1
   CGGCAAGATTAGCATCCGTT 1
   total memory used: 129.6k
   average miscount: 0.4313

Looks a little better, eh?  But the total miscount isn't any
different... Why?

Basically what's going on is this: the first table is consulted for *every*
new object we add, and it has a certain false positive rate at which it
falsely answers "yes, we've seen this before" and increments the associated
counts.  For the scalable Bloom filter, this doesn't cause any problems:
the false positive rate is still the same, but all we're doing is indicating
presence and absence.  For the CountMin Sketch, however, we're *incrementing*
the counters when there's a false positive -- and since the early tables
get consulted a lot more frequently than the later tables, they have a lot
more false positive matches, and get incremented a lot more.  This results in
a systematically higher miscount for the frequency of objects added earlier
vs later.

DOOOOOOM.  I can imagine situations where this might not matter that
much but I think it does matter for our purposes in khmer, where a
bias towards higher counts in the early objects added would be Bad.

I played around with a few ideas.  One idea is to adjust the counts in
the early tables based on the number of total objects added to the
counter; this could be done either by tweaking the actual counts, or
adding in per-table weights that are adjusted with each increment.
Another idea is to decrement counters in the tables at random as we
increment new counters.  A third idea (that I haven't actually tested
yet) was to move heavy hitters from early tables to later tables, by
decrementing all their counts in the early table and then adding them
in to the later table. Any or all of these might work, but require
further research and probably some Math.

You can actually do some good by setting the total error bound to something
smaller::

   Creating new ScalableCounter: growth rate 2, error ratio 0.50, bound 0.010
   ...
   total memory used: 260.7k
   average miscount: 0.0417

but the memory required doubles, and -- of even more concern -- the
fundamental problem is still there: if we add an infinite number of objects,
the counts in the early tables will be infinitely wrong.  So we need an
approach that's sustainable in theory, too.

What's next?
------------

From a skim of `this review
<http://www.dca.fee.unicamp.br/~chesteve/pubs/bloom-filter-ieee-survey-preprint.pdf>`__,
I plan to look at decaying Bloom Filters, dynamic Bloom filters,
and retouched Bloom filters next.

Help?
-----

I would, at this point, love some help :).

First, if the problem above has been solved already, then great! I'd love
references.  If you're working in this area and want to tackle it,
please let me know; I'd love to either collaborate or make use of your
work.

Second, if there are good implementations of scalable and
memory-efficient probabilistic counting data structures, I'd love to
know.  We're already looking at Google's `sparsehash
<https://code.google.com/p/sparsehash/>`__ for exact storage, but I
think we can probably get 10x or more improved memory usage out of a
probabilistic solution (see `the diginorm discussion in khmer-counting
<http://arxiv.org/abs/1309.2975>`__ for reasons why.)  Note, it needs
to be BSD-license-compatible before we can include it in khmer, which
prevents us from using several of the published k-mer counting
solutions :(.

--titus

p.s. Note that bitly's `dablooms
<https://github.com/bitly/dablooms>`__ takes a similar approach, and
may be subject to the same problem.

p.p.s. Thanks to Sherine Awad, Qingpeng Zhang, and Charles Ofria for
pre-posting discussions!
