The Use and Abuse of Keyword Arguments in Python
################################################

:author: C\. Titus Brown
:tags: python
:date: 2009-03-21
:slug: on-kwargs
:category: python


I'm 3/4 of the way through my first ground-up code review for `pygr
<http://code.google.com/p/pygr>`__, and I want to gripe about
something that pygr does a fair bit of: use Python's \*\*kwargs.  I
don't want to escale it into a policy argument & policy decision for
pygr, so I'm posting it here; hopefully I can sway minds with, well,
suasion, rather than dictat.

What am I griping about, exactly?  Check out this code: ::

  class SomethingExtensible(object):
     def __init__(self, foo, bar, **kwargs):
         ...
         baz(x, y, **kwargs)

  def baz(a, b, **kwargs):
     ...

Now think about how you'd read code like this in order to answer the
following four questions:

1. What keyword arguments does __init__ take?

2. What does __init__ do with these arguments?

3. What keyword arguments does baz take?

4. What does baz do with these arguments?

(These would among the first questions I'd ask of the code; you too, right?)

Well, one thing you can immediately tell is that there's a big black
box of arguments passed into 'baz', so there's no point in trying to
completely understand the arguments to __init__ without also
completely understanding the arguments to baz.

Another thing you can immediately tell is that without a pretty good
docstring or a detailed examination of both __init__ and baz, you're
not going to be able to begin to understand either function.  And
since docstrings, documentation, and comments are always wrong or
incomplete anyway, you're going to have to grok the entire function.

So, basically, you're going to be lost in this code without a lot of
work.  Also, because there's no concise way to validate that we only
received the set of kwargs we were expecting -- __init__ may not even
know what those are, and people rarely check anyway because it's a bit
of ugly code to do so -- you're subject to errors from misspellings:
arguments that look almost right, but lack an 's' at the end, for
example, when the code expects that 's' right there.

On the flip side, you *do* have an opaque "box" of arguments that
you're passing around, and this can come in *very* handy if you're
doing something like this: ::

  class SomethingExtensible(object):
     def __init__(self, foo, bar, **kwargs):
        ...
        baz(x, y, **kwargs)

     def baz(a, b, **kwargs):
        ...

(note indentation of baz -- it's now a method in the class, rather
than an independent function).  Why is this handy?  Because now you
can subclass SomethingExtensible and potentially redefine 'baz' to
take new arguments without having to change the constructor *at all*
-- you just change what keyword arguments you pass into it.

So it's readability vs extensibility.  I tend to argue for readability
over extensibility, and that's what I'll do here: for the love of
whatever deity/ies you believe in, use \*\*kwargs sparingly and document
their use when you do.

--titus

p.s. It may be that I'm missing some syntax tricks here, where I can unpack
\*\*kwargs and demand that it nicely conforms to my expectations without
doing serial gets and removals: ::

  x = kwargs.get('x', some_default)
  if 'x' in kwargs: del kwargs['x']

  y = kwargs.get('y', some_default)
  if 'y' in kwargs: del kwargs['y']

  ...

  assert len(kwargs) == 0, "error, unexpected kwargs"

or some such.  Any thoughts?


----

**Legacy Comments**


Posted by Mike Hansen on 2009-03-22 at 00:17. 

::

   Using pop is a little bit better:    x = kwargs.pop('x', some_default)
   y = kwargs.pop('y', some_default)


Posted by Chris Lasher on 2009-03-22 at 00:18. 

::

   I agree wholeheartedly. One of the things that the previous FriendFeed
   API Python library made heavy use of was **kwargs. I got rid of those
   very quickly with well documented parameters in my fork of it in
   FriendFeed PyAPI.    On the note of the unpacking of the kwargs
   dictionary, why would you want to assert that you've deleted all the
   entries from it? My understanding of the keyword arguments capture is
   that you just won't know what you will get in it. If you expect to
   receive something in it, then you must know something about the
   structure, and it should be instead be a named parameter.


Posted by Titus Brown on 2009-03-22 at 00:44. 

::

   Mike, thanks!  For some reason didn't realize 'pop' existed on dicts.
   Chris, that's to deal with the issue of misspelling.  I've run into
   situations where the interface specifies kwargs, but you're actually
   fairly sure of what you expect to get in a function call; then making
   sure you only get that is a good way to proceed, if only in a test
   situation.  It's not something I like but I don't always have control
   over the interface.  Not sure what would happen if I explicitly
   unpacked them in the function def.. hmm.    --t


Posted by Huw Giddens on 2009-03-22 at 03:58. 

::

   One of the more persuasive reasons to use **kwargs that I've seen is
   so that calls to your method via super will work in a coherent way -
   http://.ws/ has the gory details, but the part that I think applies
   here is that if your method could be called via super, you don't know
   what arguments your method will be actually called with.    As such,
   if some method is going to call/be called by super, it may not be a
   good idea to assert that ***kwargs contains only expected arguments,
   or to avoid using ***kwargs at all.


Posted by Noah Gift on 2009-03-22 at 06:39. 

::

   I think is a clear case of why doctest are a good thing.  If you write
   a doctest, then the API is understandable and testable.


Posted by anon on 2009-03-22 at 07:51. 

::

   Your second baz is missing the self argument.


Posted by Marius Gedminas on 2009-03-22 at 08:08. 

::

   I agree: **kwargs is a large hammer.  Use it sparingly.  There are use
   cases where it is indispensable (wrapping arbitrary functions, e.g.
   when you're writing a decorator).


Posted by Gael Varoquaux on 2009-03-22 at 11:11. 

::

   Actually, I have the opposite opinion, at least for the examples you
   show:    in <em>_init_</em> **kwargs should be prefered. The reason
   being that it is the only way to have classes enabling changes in the
   parents (with regards to inheritance), without forcing a rewrite of
   the subclasses. This is important, because the subclasses may not be
   in the same codebase as the parent classes.    While this is not a
   golden rule, I would say that a golden rule is: "use positional
   arguments in your <em>_init_</em> sparsingly". The reason being that
   positional arguments are terribly fragile to inheritance.


Posted by Titus Brown on 2009-03-22 at 11:22. 

::

   Hi Gael,    could you give an example?    I suspect I'll still try to
   come down on the side of readability in this case, but I also suspect
   you have hidden levels of nastiness lurking for me if I say that ;)


Posted by Joseph Lisee on 2009-03-22 at 12:56. 

::

   Here is a way I have used **kwargs to good effect (I think) in my own
   project (see website):    class SpecificPanel(wx.Panel):    def
   <em>_init_</em>(self, customArg1, customArg2, **args, ***kwargs):
   wx.Panel.<em>_init_</em>(self, **args, ***kwargs)    # Use customArg1
   and customAgr2    This lets users of SpecificPanel just pass the extra
   args it needs at the front of the list then give all the normal
   arguments they would give to a wx.Panel.  I have found it makes the
   API cleaner, rather then having to duplicate the argument list of
   wx.Panel.


Posted by Doug Hellmann on 2009-03-22 at 18:32. 

::

   We ended up with a similar use of keyword args in some of our
   libraries.  We came up with two solutions.    In some cases, we just
   went back and listed all of the arguments explicitly.  That makes it
   much easier to track down what arguments are needed/supported by a
   class.    Another solution we came up with for cases where there were
   a lot of arguments was to define "options" classes.  The long list of
   args is only defined in the constructor to that class, and a single
   option argument can be passed to the other functions/methods instead
   of the keyword args.  That makes it easy to add new options without
   updating every caller (it also makes it easy to set up fixtures in
   tests).


Posted by Titus Brown on 2009-03-22 at 21:42. 

::

   Huw Giddens' comment vanished, but he wanted to post this link:    <a
   href="http://mail.python.org/pipermail/python-
   dev/2005-January/050656.html">http://mail.python.org/pipermail/python-
   dev/2005-January/050656.html</a>    and this:    <a
   href="http://fuhm.net/super-harmful/">http://fuhm.net/super-
   harmful/</a>    His conclusion: **kwargs is  a fairly good  idea when
   you want your method to play nice with super()


Posted by Ronny Pfannschmidt on 2009-03-23 at 06:02. 

::

   starting with python3 the syntax does support declaring keyword-only
   arguments      see <a href="http://www.python.org/dev/peps/pep-3102/">
   http://www.python.org/dev/peps/pep-3102/</a> for details


Posted by Brandon Corfman on 2009-03-23 at 08:10. 

::

   Hm, which is more readable:    foo = MyObj("bar", (210, 2, 4))  or
   foo = MyObj(title="bar", rgb=(210, 2, 4))    and this is just a small
   example. To me, readability from the caller is more important than for
   the callee (which as you noted is easy to take care of with a
   docstring).


Posted by <em>Mark</em> on 2009-03-23 at 15:44. 

::

   Since calling it "kwargs", though idiomatic, is redundant with the
   "**" itself, perhaps saying "**extra_args_from_derived_classes" (or
   something more elegant) that self-documents <em>why</em> you're asking
   for them?


Posted by Titus Brown on 2009-03-24 at 07:25. 

::

   Brandon, sure... use keyword arguments.  Just don't collect them all
   in a '**' variable and pass them around!


Posted by Chris Lasher on 2009-03-24 at 16:35. 

::

   Gael, perhaps I've misunderstood you, so like Titus, I'm interested in
   an example. Going off of my possible misunderstanding, however, I'll
   disagree and say that **kwargs should be entirely disfavored in place
   of proper arguments in subclasses.    My impression is that in
   "proper" OOP, all subclasses must implement all methods of their
   parent classes, though they may implement more. Likewise, each method
   that is inherited from the parent class, when overridden, must support
   the same arguments as the original, though it may support more. ,
   **kwargs shouldn't be used in overriding methods in place of arguments
   explicitly specified by the parent class. This may be practically
   compatible, but it is of poor practice.    I acknowledge that in the
   short term, it's convenient given the underlying parent classes'
   parameters can change--and perhaps they are even in an external
   library you have no control over. When this happens, if you went the
   **kwargs route, your subclass interface can "stay the same". It's very
   unhelpful shortcut to take, however. If the parent class changes, take
   due diligence and update the subclasses. Chances are, you'll have to
   mess with your own code inside the subclass, anyway, since parameters
   have likely changed, been added, or been removed.


Posted by Yaroslav Halchenko on 2009-03-24 at 23:00. 

::

   Very interesting post. I too have mixed feelings about using **kwargs,
   especially in the <em>_init_</em>'s (where I find myself using them
   more and more).    Since the main problem later on, as you mentioned,
   difficulty to understand what keyword arguments any given constructor
   is needing, for our project (www.pymvpa.org) we worked out following
   solution: use a helper function for <em>_doc_</em> which helps us out
   -- goes through super classes <em>_init_</em> docstrings, parses them
   (we try to be consistent and use ReST for docstrings), and composes
   :Parameters: section for a current class.    Now, whenever a developer
   needs to discover available parameters -- there is no difficulty at
   all. Also a developer can easily subclass, provide only documentation
   for the relevant parameters in a derived class <em>_init_</em>
   docstring and obtain a complete list of parameters whenever doc for
   that class is asked.    Another part of the solution is that for some
   classes we define class level Parameters, which are transformed into
   per-instance attributes later on by the <em>_metaclass_</em> which not
   only takes care about creating per instance collection of those
   'parameters', but extends the docstring of the class with listing of
   those, and description of added arguments to the <em>_init_</em>.
   Altogether now we obtain more or less complete description of all
   arguments which are hidden behind **kwargs ;)    so, now example...
   Constructor information:  Definition:  SMLR(self, **kwargs)
   Docstring:    Initialize an SMLR classifier.        Parameters    lm
   The penalty term lambda.  Larger values will give rise to    more
   sparsification. (Default: 0.1)    convergence_tol    When the weight
   change for each cycle drops below this value    the regression is
   considered converged.  Smaller values    lead to tighter convergence.
   (Default: 0.001)    resamp_decay    Decay rate in the probability of
   resampling a zero weight.    1.0 will immediately decrease to the
   min_resamp from 1.0, 0.0    will never decrease from 1.0. (Default:
   0.5)  ....    whenever actual <em>_init_</em> has only:      def
   <em>_init_</em>(self, **kwargs):    """Initialize an SMLR classifier.
   """


Posted by Gael Varoquaux on 2009-03-25 at 01:09. 

::

   Hi all,    Here is an example, sorry for the delay: I am traveling and
   sprinting.    Suppose you have a plotting library, and the base class
   of the objects you draw on the canvas is an 'Artist' (FWIW, I could be
   talking about a toolkit, and a 'Widget'). This artist is going to be
   taking init arguments such as a 'linewidth', and a 'color'. I am going
   subclass it in a crazy amount of ways, because everything I draw is a
   subclass of 'Artist'. My subclasses are going to add arguments to the
   init. Now suppose that later down the line, I enhance my 'Artist' to
   add an 'alpha' argument to it, that controls transparency. I am going
   to have to add a input argument to every single one of the init method
   of the subclasses. Not only is this tedious, but if somebody has
   implemented custom 'Artists' in a different module, they won't be
   getting this 'alpha' argument.    Is this a good example?

