Buggy Python code?
##################

:author: C\. Titus Brown
:tags: python,teaching
:date: 2009-09-08
:slug: buggy-python-code
:category: teaching


I'm looking for examples of frustratingly simple-yet-wrong Python code,
suitable for an undergrad class to debug.  I'd prefer things that don't rely on
tricky features of Python (like shared list references), but rather code
where subtly bad logic or program flow leads to bad behavior.

Comment below, or e-mail me; I'll post the ones I pick later.  thanks!

--titus


----

**Legacy Comments**


Posted by Peter Boothe on 2009-09-08 at 22:42. 

::

   &lt;pre&gt;  # Python3 code.  Easily translated to 2.x  import random
   secret = random.randint(1,100)    guess = -1  while guess != secret:
   guess = input("Guess a number!")    guess = int(guess)    if guess
   &gt; secret:    print("Too high!")    else:    print("Too low!")
   print("You got it!)  &lt;/pre&gt;


Posted by Nick on 2009-09-08 at 23:18. 

::

   A condensed version of something that cost me a small chunk of time
   today (adding DB queries and multiple modules into the mix to obscure
   things). I feel a bit stupid.    python -c "x=3; print 3==x; x="3";
   print 3==x"    output:  True  True


Posted by Michele Simionato on 2009-09-08 at 23:21. 

::

   This one is extremely common and I saw it in our codebase at work just
   yesterday:    def make_list(...):    ls  = []    ... add something to
   ls ...    return ls.sort() # instead of sorted(ls)


Posted by Brandon Craig Rhodes on 2009-09-09 at 00:00. 

::

   Gads, Nick! You just wasted more than five minutes of my time. And
   panicked me that there was something basic that I didn't know about
   Python. :-)


Posted by John Eikenberry on 2009-09-09 at 00:06. 

::

   # missing comma    &gt;&gt;&gt; list_of_tuples = [  ...  (1, 'one'),
   ...  (2, 'two')  ...  (3, 'three')  ...  ]  Traceback (most recent
   call last):    File "&lt;stdin&gt;", line 4, in &lt;module&gt;
   TypeError: 'tuple' object is not callable


Posted by Adam Vandenberg on 2009-09-09 at 00:15. 

::

   Improperly recursive <em>_getattr_</em> is always a good one, but is a
   bit "advanced".


Posted by Richard Jones on 2009-09-09 at 01:28. 

::

   Sadly I have nothing to offer. I would very much appreciate it if you
   could post a followup with any useful snippets you do find though :)


Posted by Ben Bass on 2009-09-09 at 03:36. 

::

   Not 'wrong', but equivalent has bitten me sometimes, especially if
   data size varies; looks like the program crashes if suddenly a large
   data packet comes along...    def eat_chunk(data):    n =
   get_packet_size(data)  # O(1)    packet, leftover = data[:n], data[n:]
   process(packet)    return leftover    data = [some large list]  while
   data:    data = eat_chunk(data)    which is effectively equivalent to
   this:    data = [some large list]  while data:    a, data = data[0],
   data[1:]    Problem is O(n**2) running time, but this isn't obvious
   without knowledge of list implementation (or rather deletions from
   start being O(n)...)


Posted by Cal on 2009-09-09 at 03:53. 

::

   # Manipulating a list being iterated confuses newbies to no end
   r=[1,2,3,4]  for n in r:    print n    r.remove(n)


Posted by Foo on 2009-09-09 at 04:22. 

::

   Just make them implement quicksort. ;)


Posted by Tim Golden on 2009-09-09 at 04:22. 

::

   This, and similar <em>_setattr_</em> gotchas:    <code>  class X
   (object):    def <em>_init_</em> (self):    self._attrs = {}    def
   <em>_setattr_</em> (self, attr, value):    self._attrs[attr]= value
   x = X ()    </code>    TJG


Posted by ASG9000 on 2009-09-09 at 06:11. 

::

   Couple of gotchas from a presentation I gave at work:  import time
   def pretty_time(when=time.time()):    return time.strftime("%Y/%m/%d
   %H:%M:%S", time.gmtime(when))    #Another variation of Michele
   Simionato's post:  for k in d.keys().sort(): print k    #Scoping:  x =
   10    def print_x():    print x    def inc_x():    x += 1    print_x()
   inc_x()  print_x()    Other ideas:  Use of isinstance() breaking duck
   typing?  Use of decorators changing method names?  Attempts to modify
   immutable types, strings, tuples?  Something that happily attempts to
   use mutable types as keys to a dictionary (e.g. a less fussy version
   of memoize decorator)?  Using the logical operators to do suprising
   things?:  s = "duck"; num = 2; s += num &gt; 1 and 's' or ''; print s


Posted by ASG9000 on 2009-09-09 at 06:18. 

::

   Stack overflow is a good place to find newbie python questions, e.g.
   <a href="http://stackoverflow.com/questions/1395603/trouble-with-
   simple-python-code">http://stackoverflow.com/questions/1395603
   /trouble-with-simple-python-code</a>    OK, I am going to leave you
   alone and go back to work now.


Posted by Carl T. on 2009-09-09 at 10:21. 

::

   if somethingistrue:      # declare a variable while doing a bunch of
   stuff      x = 4    # now do something with variable    y = 20 * x
   Often you'll get a NameError for x if the condition up top is brittle.
   A consultant I worked with used to do this all of the time.  Not
   really an error, but if you're writing huge 2000 line chunks of code
   in the outer scope (in and of itself bad practice), this sort of thing
   can drive you batty.    Carl T.


Posted by j_king on 2009-09-09 at 12:11. 

::

   In some training sessions I've seen some small things bother a few
   people:    - List comprehensions leak their variable names out of
   their scope    [x for x in range(10)]  print x # will print '9'    -
   Ternary operators in Python are different than most other languages
   x = x if some_condition(x) else y    - Some people get tripped up on
   difference between logic and identity operators: 'is', ==, 'and', etc
   (also sometimes eager evaluations)


Posted by Steffen Oschatz on 2009-09-09 at 13:10. 

::

   #mutable default param    def func(default=[]):    return default
   result = func()  result.append(1)    result1 = func()    assert not
   result1, 'I got you'  assert result is not result1, 'Argh!'


Posted by John on 2009-09-09 at 13:44. 

::

   This has bitten me:  callbacks = []  for val in 1, 2, 3:    def cb():
   print val    callbacks.append(cb)    for cb in callbacks:    cb()
   To me the logical output seemed to be 1, 2, 3 but instead the output
   is 3, 3, 3. A workaround is:    def cb(val=val):    print val    John.


Posted by Colbrac on 2009-09-09 at 15:19. 

::

   Some dataprocessing code to split up a big list of data into an
   unknown number of sublists. The first two list entries are the header
   (description and unit) and I want those appended in front of each
   sublist as all functions that work on the data expect them. So (from
   memory not tested for errors):    def splitData(data):    header =
   data[:2]    oldtime = data[2][3]    output = [header]    idx = 0
   for entry in data[2:]:    if entry[3]-oldtime &lt; 10:
   output[idx].append(entry)    else:     output.append(header)    idx +=
   1    output[idx].append(entry)    return output    Say a delta t of 10
   should split up the data in 10 sublists, written like this I end up
   with an output that is 10 identical sublists, e.g. the same as the
   original input.    Solution: replace output.append(header) with
   output.append(header[:]) to create a new instance of the initial
   header list in memory instead of linking back to the original instance
   in memory.    P.S. If there is an easier way to split datalists like
   this, I'm all ears.


Posted by Titus Brown on 2009-09-09 at 21:29. 

::

   Here's what I've come up with so far; thanks for all the help!    <a h
   ref="http://class.ged.idyll.org/svn/files/lab1/">http://class.ged.idyl
   l.org/svn/files/lab1/</a>    --titus    (I'm hoping not just to
   demonstrate that weird things happen, but rather to give them
   debugging techniques they can use to "attack" the problem.  I'll let
   you all know how it works out.)


Posted by Titus Brown on 2009-09-10 at 11:06. 

::

   p.s. No posting solutions -- I have positive evidence that some of the
   students are reading this blog...


Posted by David on 2009-09-10 at 11:58. 

::

   The ever-popular copying lists  list_a = ["a", "b", "c"]  list_b =
   list_a  list_a[1] = "**"    print list_b  ['a', '**', 'c']    A good
   idea BTW which will hopefully nip some bad habits before they get
   started.


Posted by David on 2009-09-10 at 12:07. 

::

   You see variations on this from experienced programmers.  Run the
   program as is, and then call "some_func()" from another program.
   [CODE]def some_func():    print "\nthis function just prints some
   stuff"    print "to show how a loop works"      outside_ctr = 0
   stop = 5    for ctr in range(0, stop):    print ctr, outside_ctr
   outside_ctr += incr    if <em>_name_</em> == "<em>_main_</em>":
   incr = 2    some_func() [/CODE]


Posted by David on 2009-09-10 at 13:14. 

::

   This turns up on the forums more than it should (expecting 5
   iterations and why does it print these numbers?).  [CODE]x = 0  for x
   in range(0, 10):    x += 2    print x [/CODE]    Along similar lines
   [CODE]empty_list = []  list_of_lists = []  for x in range(0, 5):
   list_of_lists.append(empty_list) [/CODE]    My first college professor
   got our young minds to think about blocks of memory, and away from
   what would be the word processing mentality today, where there are
   nice lines in document in a folder (none of which exist unless the
   programmer creates them).  If your students understand blocks of
   memory instead of variable names, it will save a lot of headaches down
   the road.    Also, a well placed print statement or try/except is very
   enlightening.    There are discussions on the forums sometimes about
   the maximum length of a function or block of code.  10 to 20 lines
   seems to be the consensus.  Smaller blocks of code are much easier to
   debug.


Posted by David on 2009-09-10 at 14:25. 

::

   This turns up on the forums more than it should (expecting 5
   iterations and why does it print these numbers?).  [CODE]x = 0  for x
   in range(0, 10):    x += 2    print x [/CODE]    Along similar lines
   [CODE]empty_list = []  list_of_lists = []  for x in range(0, 5):
   list_of_lists.append(empty_list) [/CODE]    My first college professor
   got our young minds to think about blocks of memory, and away from
   what would be the word processing mentality today, where there are
   nice lines in document in a folder (none of which exist unless the
   programmer creates them).  If your students understand blocks of
   memory instead of variable names, it will save a lot of headaches down
   the road.    Also, a well placed print statement or try/except is very
   enlightening.    There are discussions on the forums sometimes about
   the maximum length of a function or block of code.  10 to 20 lines
   seems to be the consensus.  Smaller blocks of code are much easier to
   debug.


Posted by David on 2009-09-10 at 14:36. 

::

   This turns up on the forums more than it should (expecting 5
   iterations and why does it print these numbers?).  [CODE]x = 0  for x
   in range(0, 10):    x += 2    print x [/CODE]    Along similar lines
   [CODE]empty_list = []  list_of_lists = []  for x in range(0, 5):
   list_of_lists.append(empty_list) [/CODE]    My first college professor
   got our young minds to think about blocks of memory, and away from
   what would be the word processing mentality today, where there are
   nice lines in document in a folder (none of which exist unless the
   programmer creates them).  If your students understand blocks of
   memory instead of variable names, it will save a lot of headaches down
   the road.    Also, a well placed print statement or try/except is very
   enlightening.    There are discussions on the forums sometimes about
   the maximum length of a function or block of code.  10 to 20 lines
   seems to be the consensus.  Smaller blocks of code are much easier to
   debug.


Posted by David on 2009-09-10 at 14:56. 

::

   This turns up on the forums more than it should (expecting 5
   iterations and why does it print these numbers?).  [CODE]x = 0  for x
   in range(0, 10):    x += 2    print x [/CODE]    Along similar lines
   [CODE]empty_list = []  list_of_lists = []  for x in range(0, 5):
   list_of_lists.append(empty_list) [/CODE]    My first college professor
   got our young minds to think about blocks of memory, and away from
   what would be the word processing mentality today, where there are
   nice lines in document in a folder (none of which exist unless the
   programmer creates them).  If your students understand blocks of
   memory instead of variable names, it will save a lot of headaches down
   the road.    Also, a well placed print statement or try/except is very
   enlightening.    There are discussions on the forums sometimes about
   the maximum length of a function or block of code.  10 to 20 lines
   seems to be the consensus.  Smaller blocks of code are much easier to
   debug.


Posted by Jiri Barton on 2009-09-17 at 05:40. 

::

   identity versus copy  a = [[]] * 3  a[0].append(1)    print a  [[1],
   [1], [1]]    But you wanted [[1], [], []]!!

