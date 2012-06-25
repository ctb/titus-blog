Conversions between classes in Python
#####################################

:author: C\. Titus Brown
:tags: python
:date: 2007-12-09
:slug: conversions
:category: python


My future colleague, Bill Punch at MSU, is teaching Python to intro
CS students.  He asks (slightly edited):

-----

In C++, you can write multiple constructors, each one taking a different
type and/or number of arguments. Let's say we are writing a
RationalNumber class. I could write 2 constructors: ::
  
  class Rational{
    Rational(int numerator, int denominator);
    Rational (int numerator);
    Rational operator+(Rational r1, Rational r2);
  
The second constructor acts as an automatic conversion function for
integer to Rational, so that the addition operation would work. ::
  
  Rational r1(1,2);
  cout << r1 + 1   /* C++ will call Rational(1), then call the operator+
  method, automatically */
  
In Python, I only get one constructor, __init__. If I want to be able to
add  an integer and a Rational, I have to do some introspection in the
__add__ function and deal with it there, as below ::
  
  class Rational:
    def __init__(self,n,d=1): self.n= n; self.d=d
    def __add__(self,other):
       if isinstance(other,int):   # int case
          val = Rational(other)
       else:   
          val = other  # rational case
      ...do the add... 
  
For commutativity, I also add radd. I THINK that's all correct.
  
So what if I want to write conversion operations. I can write a
__float__(self) in Rational to convert a Rational to self. But that will
not solve the following: ::
  
    r1 + 1.5
  
that is, python won't/can't figure out to convert r1 to a float so the  
operation can proceed. Is that correct? However, the following will work ::
  
  float(r1) + 1.5
  
Finally, let's say I write a container class. I want to be able to
convert it to a list (for whatever reason). If I make the new class
iterable, I can call list() on it, but again it won't automatically
convert, as in ::
  
  [1,2,3] + myContainerInstance
  
but it will ::
  
  [1,2,3] + list(myContainerInstance)

There is a coerce operator, __coerce__ but it appears to be
deprecated in 2.5 and unavailable in 3.0. So there was some reason
to have it at one time and it is now abandoned.

-----

Back to me:

Now, my immediate response is snarky and unhelpful: I've rarely needed this
functionality, and when I do need it, I simply do the conversions explicitly.
But I can understand his point, for example, in the context of his last
example: extending lists.

Frankly, it's not very duck-y of Python to respond to this: ::

  class X:
      internal = [5,6,7,8]
      def __getitem__(self, i):
          return self.internal[i]
  
  x = X()
  
  l = [1,2,3]
  print l + x

with ::

  TypeError: can only concatenate list (not "instance") to list

(It does this for tuple, too, leading me to believe that it is not
my failed implementation of X that is the problem.  And if I subclass
list, the concatenation fails silently.)

So anyway, back to type coercions and implicit type conversions: I
haven't found anything obvious about __coerce__ being dropped, and it
was always a bit confusing to me.

It seems to me like the basic idea is that duck typing should be
sufficient, and where it's not you're SOL.

So, err, what do I say?  Any advice?

--titus


----

**Legacy Comments**


Posted by Konrad on 2007-12-09 at 07:42. 

::

   Inheritance from the list is what's you're looking for:    class
   X(list):    pass    x = X([1, 2, 3, 4])  y = [1, 2, 3] + x    print x,
   y      You can also send some additional arguments to the constructor:
   class X(list):    def <em>_init_</em>(self, data, some_other_arg):
   list.<em>_init_</em>(self, data)    self.some_attribute =
   some_other_arg      x = X([1, 2, 3, 4], 'bruce')  y = [1, 2, 3] + x
   print x, x.some_attribute, y


Posted by Niki on 2007-12-09 at 09:00. 

::

   two things:    first:    a = [1,2,3];b = (4,5);a.extend(b)    works
   second: explicit is better than implicit


Posted by Andre Roberge on 2007-12-09 at 09:07. 

::

   Try having a look at the code here:  <a href="http://www.pycode.com/mo
   dules/?id=17">http://www.pycode.com/modules/?id=17</a>    Disclaimer:
   I have not used it myself ;-)


Posted by pawnhearts on 2007-12-09 at 09:33. 

::

   hm..  <pre>  class X:    def <em>_init_</em>(self,data=[]):
   self._data=data    def <em>_getitem_</em>(self,i):    return
   self._data[i]    def <em>_add_</em>(self,y):    return self._data+y
   </pre>    In [9]: x=X(range(10))  In [10]: x[:5]  Out[10]: [0, 1, 2,
   3, 4]  In [11]: x+[1,2]  Out[11]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2]
   u could also return X(blabla) instead of lists  also there is a
   UserList module, which you can take as a base


Posted by Alec Thomas on 2007-12-09 at 09:44. 

::

   Multi-methods [1] sound like the "Pythonic" way of solving this.
   The <em>_add_</em> would then become:    @multimethod(int)  def
   coerce(val):    return Rational(val)    @multimethod(float)  def
   coerce(val):    ...    return Rational(...)    class Rational(object):
   ...    def <em>_add_</em>(self, other):    val = coerce(other)    ...
   Note that the linked-to multi-method implementation will only handle
   functions, not methods, thus the global "coerce" function. This could
   easily be fixed.    [1] <a href="http://www.artima.com/weblogs/viewpos
   t.jsp?thread=101605">http://www.artima.com/weblogs/viewpost.jsp?thread
   =101605</a>


Posted by ido on 2007-12-09 at 11:37. 

::

   you can move the conversion into the <em>_radd_</em> method:    class
   X:    def <em>_init_</em>(self):    self.internal = [5,6,7,8]    def
   <em>_getitem_</em>(self, i):    return self.internal[i]    def
   <em>_radd_</em>(self, other):    r = X()    r.internal += list(other)
   return r    def <em>_str_</em>(self):    return str(self.internal)
   x = X()  l = [1,2,3]  print l + x  print x + x


Posted by she on 2007-12-09 at 12:45. 

::

   duck typing means more, it means that you no longer even **want** to
   care about types (and their associated behaviour set)    I think what
   will rock the world will be GUI components which can be reshaped and
   reused with great use. No more stupid dedicated text-edit widget
   alone, we could get a nicer abstraction on "edit binary graphics"...
   i.e. a gimp in a scripting language    But i guess that will take more
   time...


Posted by Jeremy Bowers on 2007-12-09 at 13:53. 

::

   Coercion: I think this is a case of Python's "Explicit is better than
   implicit". 1 + 1.5 working in Python is really more of an exception
   and a concession to practicality than the way Python directly works.
   Personally, I wouldn't write a Computer Algebra System in Python. (In
   fact, I am writing a bit of a CAS and I'm not writing it in Python,
   even though the rest of the system will be Python (Django).)    There
   may be a way around this, I'm not thinking about this to the n-th
   degree, but whatever that way is, it probably isn't appropriate for an
   introductory class. You've tried the obvious ways, from what I can
   see.    <em>_coerce_</em> was abandoned because IIRC it was mind-
   bogglingly complicated when you really got down to it, frequently
   resulting in "a + b" having radically different results than "b + a",
   which should not be. I recall some "gotcha" discussions on the topic
   and the take-away lesson was "don't do that", which is probably why it
   got dropped.    Iterators: Iterators aren't lists, and this is another
   place where Python is going to refuse to automatically coerce
   something that probably shouldn't be coerced. If you want to
   concatenate two (or more) iterators into a composite iterator, you can
   use <a href="http://docs.python.org/lib/itertools-
   functions.html">itertools.chain</a>. If you want a list, you'll have
   to make a list out of the iterator. Again, in an introductory
   environment, calling "list" explicitly and perhaps not dealing with
   iterators at all is probably the right answer.    One difference with
   an iterator is that you can affect it "in flight"; for instance, it is
   easy to create an iterator that goes over a tree/graph and allows a
   consumer to tell the iterator whether to descend into the children or
   not. Official support for this was added in 2.5 (IIRC), but it was
   little more than official and centralized syntax for something you
   were always able to do (although it seems to me many people didn't
   catch on to the fact it was always possible). A list, on the other
   hand, is what it is.     By calling list(iterator), you are actually
   committing to a certain semantic action, namely, taking the iterator
   as-is with no further interaction. You do need that additional
   specification before "adding an iterator to a list" really makes
   sense. Otherwise, [1, 2, 3] + iterator could just as easily be
   interpreted as adding "iterator" to the list as the fourth element,
   something that may also be a reasonable thing to do.


Posted by theeth on 2007-12-09 at 15:58. 

::

   Subclassing list seems to work ok, contrary to what you said.    class
   X(list):    pass    print X((2, 3, 4)) + [1,2,3]    worked correctly
   in Py 2.4.4    It might be possible to "cheat" a bit, using add and
   accessing the class of the second operand, like this:    class X:
   def <em>_init_</em>(self, l):    self.l = list(l)    def
   <em>_add_</em>(self, other):    return other.<em>_class_</em>(self) +
   other      def <em>_getitem_</em>(self, i):    return self.l[i]    def
   <em>_len_</em>(self):    return len(self.l)      def
   <em>_str_</em>(self):    return str(self.l)      def
   <em>_int_</em>(self):    return len(self)    print X((2, 3, 4)) +
   [1,2,3]  print X((1,2,3)) + "foo"  print X((1,2,3)) + 2    All of
   those return what would be expected.


Posted by Brett on 2007-12-09 at 16:32. 

::

   In either case, I would just call the conversion in the <em>_add_</em>
   method and thus use EAFP.  If all attempts to use acceptabe interfaces
   or conversions fail then raise NotImplemented.    Basically you just
   want to be positive and assume the user is doing something reasonable.
   So try all the reasonable assumptions you want in your code, and then
   fail if the user made a bad assumption.


Posted by Steve Wedig on 2007-12-09 at 16:45. 

::

   Hey Titus, this is Steve from the socal-pug (haven't attended
   recently). I gave the PyJS talk. This is an interesting question.    I
   agree with your original snarky response, implicit conversion goes
   against Python Zen and type safety. By default, objects of different
   types shouldn't be promoted to a more general shared type. Sometimes
   it is useful though. str/unicode and int/float come to mind.     I
   think your friend conceptually wants Rational to subclass the Float
   class. This makes sense, because classes are sets of objects, and
   subclassing is the subset relationship. The rationals are indeed a
   subset of the floats. Similarly, ints are a subset of both rationals
   and floats. So at the interface level, everything you can do with a
   Float you can do with an Int, but not visa versa. So from at a
   type/interface level, it makes sense to have this subtype chain: Int
   &lt; Rational &lt; Float.    Your friend could define class Rational
   (float), and the type system would allow implicit conversions to float
   (the shared base class). However there is a problem. Your friend wants
   Rational to inherit Float's type/interface, but not it's
   implementation. Rationals are internally reperesented by a nominator
   &amp; demoninator, not an internal C++ floating point. I don't think
   Python supports such fine grained inheritance. So I think your friend
   has to either give up on implicit conversions, or to maintain both the
   rational and float internal representations. Here's how that code
   might look:    class Rational(float):          def
   <em>_init_</em>(self, nom, denom):                  self.nom = nom
   self.denom = denom                  super(Rational,
   self).<em>_init_</em>( float(nom) / denom )    This is far from
   perfect, but I think it could theoretically be made to work. Except it
   doesn't work in my version of Python (mac 2.4). float's constructor
   takes only one arg which must be a string or a number. Python seems to
   enforce this for subclasses of float as well, which surprises me. This
   is apparently a case where subclassing from built-in types doesn't
   work the same way as normal subclassing.    Your friend could get
   around this by not using the constructor, but that could be a pain:
   class Rat(float):          @staticmethod          def create(nom,
   denom):                  f = float(nom) / denom                  r =
   Rat(f)                  r.nom = nom                  r.denom = denom
   return r                            def <em>_add_</em>(s, x):
   if isinstance(x, Rat):                          return s._rat_add(x)
   return super(Rat, s).<em>_add_</em>(x)                    def
   _rat_add(s, x):                  nom = s.nom * x.denom + x.nom *
   s.denom                  denom = s.denom * x.denom
   nom, denom = rat_reduce(s, nom, denom)                  return
   Rat.create(nom, denom)    # testing it out...    x = Rat.create(10, 5)
   print x, type(x)    y = x + 1.5  print y, type(y)    z = x + x  print
   z, type(z)


Posted by Stephen on 2007-12-09 at 16:45. 

::

   The problem is the desire for implicit conversion, which goes against
   the way that Python works.    <a href="http://www.artima.com/weblogs/v
   iewpost.jsp?thread=7590">http://www.artima.com/weblogs/viewpost.jsp?th
   read=7590</a>    The answer is just "automatic, implicit conversions
   are not how Python does things", I think.    The idea is that duck
   typing should be sufficient, and where it's not you convert into
   compatible types explicitly.


Posted by Liam Clarke on 2007-12-09 at 17:18. 

::

   I'd suggest to your colleague that he try "import this", as it shows
   the design philosophies of Python - one of which is a preference for
   the explicit over the implicit.     Further, am I correct that he
   wishes Python to infer how to convert his class to a float? Is that
   really a realistic wish? Why can he not add the desired behaviour to
   his <em>_add_</em> method?    With regards to your class X, why not
   make it an iterator and use list.extend()?    Forgive the following if
   it turns out icky, I'm hoping you have pre tags enabled:
   &lt;pre&gt;  &gt;&gt;&gt; class X:  ...     internal = [5,6,7,8]  ...
   def <em>_iter_</em>(self):  ...             return self  ...     def
   next(self):  ...             if self.internal:  ...
   a = self.internal[0]  ...                     self.internal =
   self.internal[1:]  ...                     return a  ...
   else:  ...                     raise StopIteration  ...
   &gt;&gt;&gt; c = X()  &gt;&gt;&gt; for i in c:  ...     print i  ...
   5  6  7  8  &gt;&gt;&gt; c  &lt;<em>_main_</em>.X instance at
   0x00C6CDA0&gt;  &gt;&gt;&gt; c.next()  Traceback (most recent call
   last):    File "&lt;interactive input&gt;", line 1, in &lt;module&gt;
   File "&lt;interactive input&gt;", line 11, in next  StopIteration
   &gt;&gt;&gt; c = X()  &gt;&gt;&gt; y = ()  &gt;&gt;&gt; y = []
   &gt;&gt;&gt; y.extend(c)  &gt;&gt;&gt; y  [5, 6, 7, 8]  &gt;&gt;&gt;
   class X:  ...     internal = [5,6,7,8]  ...     i = 0  ...     limit =
   len(internal)  ...     def <em>_iter_</em>(self):  ...
   return self  ...     def next(self):  ...             if self.i &lt;
   self.limit:  ...                     a = self.internal[self.i]  ...
   &gt;&gt;&gt; class X:  ...     internal = [5,6,7,8]  ...     i = 0
   ...     limit = len(internal)  ...  ...     def <em>_iter_</em>(self):
   ...             return self  ...  ...     def next(self):  ...
   if self.i &lt; self.limit:  ...                     a =
   self.internal[self.i]  ...                     self.i += 1  ...
   return a  ...             else:  ...                     raise
   StopIteration  ...               &gt;&gt;&gt; x = X()  &gt;&gt;&gt; l
   = [1,2,3]  &gt;&gt;&gt; l + x  Traceback (most recent call last):
   File "&lt;interactive input&gt;", line 1, in &lt;module&gt;
   TypeError: can only concatenate list (not "instance") to list
   &gt;&gt;&gt; l.extend(x)  &gt;&gt;&gt; print l  [1, 2, 3, 5, 6, 7, 8]
   &lt;/pre&gt;    I agree that DWIM is preferable in any language, but
   Guido van Rossum made a decision that implicit coercion was bad, and
   so Python doesn't have it.


Posted by Titus Brown on 2007-12-09 at 17:31. 

::

   Thanks, everyone, for your comments.  Very useful, thanks!
   Regarding subclassing list: if I take the code example I posted (with
   the '<em>_getitem_</em>' and <em>_len_</em> minimum list-like
   interface) and make X inherit from list, + doesn't work.  Frankly, it
   should work either way!    I agree that explicit is better than
   implicit, although better people than me have pointed out that there's
   an unwritten codicil to that, which is "except when it isn't" -- I
   have to go find that article.  To argue, for example, that "for x in
   y" (with all of the multiple things that 'y' can be) doesn't involve a
   lot of implicit manipulation seems wrong ;)    Jeremy, esp., thanks!


Posted by Liam Clarke on 2007-12-09 at 17:39. 

::

   &gt; To argue, for example, that "for x in y" (with all of the
   multiple things that 'y' can be) doesn't involve a lot of implicit
   manipulation seems wrong ;)    Not really. no matter what y contains,
   it is an object that implements <em>_iter_</em>() and next() and
   raises StopIteration when there is nothing further to iterate over.
   Otherwise "for x in y" will fail. There's no conversions or coercions
   required or being done.


Posted by Felix on 2007-12-09 at 19:35. 

::

   implicit conversions are ok when they're standard and everyone knows
   them.  so, implicit conversions in the base language are ok.  (but
   complex rules still cause problems, such as unsignedness in C.)
   user-defined implicit conversions look attractive in toy examples, but
   they cause problems in large projects, because they increase the
   chance that you misunderstand what a particular line of code does.
   also I'd argue: if your code looks cleaner with implicit type
   conversions, then you're doing something wrong.  type conversions tend
   to be expensive operations, and you generally want to do them as
   little as possible.  the standard conversions are the ones that can be
   done cheaply.


Posted by theeth on 2007-12-09 at 21:48. 

::

   &gt; Regarding subclassing list: if I take the code example I posted
   (with the '<em>getitem</em>' and <em>len</em> minimum list-like
   interface) and make X inherit from list, + doesn't work.    There's a
   good reason why that won't work. It uses <em>_add_</em> from the base
   class (list) which refers to the its own list storage, so it ends up
   adding an empty list with your literal. If you inherit from list, it
   rightly assumes that you're using the base class storage (especially
   when using base class methods).

