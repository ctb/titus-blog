Array permutation in Python
###########################

:author: C\. Titus Brown
:tags: python
:date: 2007-06-05
:slug: array-permutation-in-python
:category: python


Just saw `this <http://www.algoblog.com/2007/06/04/permutation/>`__, in-place
permutation (of a Java array, in this case).

In Python, if you ignore the battery that's included (``random.shuffle``)
you have this: ::

   import random
   l = range(0, 20) # array to permute

   for j in range(1, len(l)):
      k = random.randint(0, j)
      l[j], l[k] = l[k], l[j]

   print l

Cute, but kinda ugly.  It should be possible to make this more Pythonic.

--titus


----

**Legacy Comments**


Posted by Doug Napoleone on 2007-06-05 at 22:32. 

::

   for j in xrange(1, len(L)): L.insert(j, L.pop(random.randint(0, j))
   Because the pop decreases the local sub-length, the insert (which
   inserts before), will insert in the proper place.    Not sure if its
   'more pythonic' or not.


Posted by Doug Napoleone on 2007-06-05 at 22:40. 

::

   On second thought, I am sure my code will cause some nasty thrashing.
   'Never mind'.


Posted by John Montgomery on 2007-06-06 at 08:03. 

::

   I recently did changed from using random.shuffle() to this generator:
   def rand_seq(size):    values=range(size)    for i in xrange(size):
   j=i+int(random.random()*(size-i))
   values[j],values[i]=values[i],values[j]    yield values[i]    So I
   could walk through elements in a random order, but abandon the walk
   part way through.  Helped a lot, as it you only get a few steps in you
   save a lot of calls to random().  Of course not sure how pythonic it
   is...  Did have quite a few attempts at writing it well, but in the
   end this worked the best.


Posted by Paul Moore on 2007-06-06 at 08:53. 

::

   Not sure what you expect by "more Pythonic". For a Pythonic solution,
   I'd use random.shuffle :-)    You could probably do something with
   itertools, but you'd still end up coding a loop over the elements.


Posted by Jack Diederich on 2007-06-06 at 10:44. 

::

   Use random.shuffle!  Shuffling isn't a hard thing to do right but it
   is a very easy thing to do wrong as the <a
   href="http://programming.reddit.com/info/1w1z3/comments">Reddit
   thread</a> about the linked post points out.


Posted by Titus Brown on 2007-06-06 at 11:39. 

::

   Paul, Jack -- so, what did the guy who wrote 'random.shuffle' use?
   random.shuffle?    ;)    --titus


Posted by Benji York on 2007-06-06 at 13:31. 

::

   Related article: How We Learned to Cheat at Online Poker: A Study in
   Software Security
   (http://www.cigital.com/papers/download/developer_gambling.php)
   They exploited a bad shuffling algorithm to know what everyone's cards
   were and what cards would be dealt next.

