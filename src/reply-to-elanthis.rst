A reply to Elanthis: Python Annoyances
######################################

:author: C\. Titus Brown
:tags: python
:date: 2008-08-01
:slug: reply-to-elanthis
:category: python


In reply to `elanthis's post <http://www.advogato.org/person/elanthis/diary/384.html>`__ on Advogato,

1.  I agree that the documentation could be improved, and we've been
working on it.  The next release should add a whole bunch of examples.
Google is your friend, as is the Python Cookbook.

2. Files as modules.  What about importing those symbols in the package __init__.py? e.g.

  foo/some/other/package/blah.py:
    class MyClass:
       ...

  foo/__init__.py
       from foo.some.other.package.blah import MyClass

The physical layout is for you, the developer, while the exposed
package interface can be pretty much whatever you want.

3. Classes are weak: yes, I guess so, but I don't really know how to
address your concerns without adding a lot of syntax.  Are you just
lusting after variable declarations 'cause that's how you think?

Your take on unit testing seems just plain wrong.  I know of no useful
language that can prevent the majority of programming errors without
some form of actually running the code, a.k.a. "testing".  You might think
YMMV, but you're almost certainly wrong.

4. I agree that the decorator syntax is inelegant and inconsistent.

5. No variable declaration: you'd catch most of these problems with
even the most rudimentary of unit tests and code coverage analysis.
Shadowing is a concern, though.  In practice it's never caused problems
for me.

6. There are official recommendations regarding docstrings; see `PEP
257 <http://www.python.org/dev/peps/pep-0257/>`__.  The (new) Python
documentation is formatted with Sphinx, which you might like better.

I think you have a good point or two, but I also think you need to
spend some more time programming in Python to figure out which of your
complaints are actual problems with Python and what is simply a legacy
of bad habits garnered from experiences with other languages.  Even if
you abandon Python for another dynamic language, I think you'll have
the same (or stronger) criticisms of those.

cheers,
--titus


----

**Legacy Comments**


Posted by Carlo Cabanilla on 2008-08-01 at 21:25. 

::

   (Replying on your blog because the original blog doesn't have
   comments)    Regarding #3, using <em>_slots_</em> makes python classes
   enforce a rigid set of member variables and makes the class more self
   documenting. For example:    class MyClass(object):
   <em>_slots_</em> = ('foo', 'bar')    c = MyClass()  c.foo = 1 # works
   fine  c.baz = 1 # raises AttributeError


Posted by Paddy3118 on 2008-08-01 at 22:03. 

::

   Hi Titus,  After reading the Post from Elanthis and your reply. I
   think you did right. I personally don't think that Elanthis is giving
   Python a chance, for example, his criticism of Docstrings I find more
   a criticism of the way he writes docstrings, and a lot of what he
   writes is the old static vs dynamic language arguments. I really
   wonder what pushes him towards dynamic languages as it seems to show
   up an inner turmoil of his.    - Paddy.


Posted by Titus Brown on 2008-08-01 at 23:15. 

::

   Thakns, Paddy!    Carlo, <em>_slots_</em> is meant solely as a memory
   optimization.  It's not supposed to be used that way, although I must
   admit it's tempting sometimes :)    --titus


Posted by baoilleach on 2008-08-02 at 16:05. 

::

   (A bit off-topic) Do you know if pydoc obeys PEP257 in relation to
   attribute docstrings? In my hands, I've found that it doesn't extract
   triply-quoted strings at the top level of a module (where used to
   document a module-level variable).


Posted by Titus Brown on 2008-08-03 at 09:57. 

::

   baoilleach,    I don't know about pydoc, but PEP 257 explicitly states
   that the first line of a docstring should be a summary of the
   function/class/module/method.    That behavior by pydoc sounds buggy.

