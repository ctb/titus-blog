Python Global Interpreter Lock approach: Validated?
###################################################

:author: C\. Titus Brown
:tags: python
:date: 2007-06-28
:slug: python-gil-validation
:category: python


It's nice to see Python `come out on top <http://debain.org/?p=196>`__
for threading.

--titus


----

**Legacy Comments**


Posted by Scott Lamb on 2007-06-28 at 12:32. 

::

   Hmm, I wouldn't call "better than Perl" validation. "Easier to read
   the Perl, better threading support than COBOL, more productive than
   TriMedia VLIW assembler, faster than MUMPS!" We can do better than
   that...


Posted by Robert on 2007-06-28 at 18:46. 

::

   I would not call that validated.


Posted by Titus Brown on 2007-06-29 at 10:58. 

::

   I think you guys are underestimating the damage done to Python's rep
   on account of the GIL.  It's not easy to explain why the GIL is such a
   good idea, and this is an example-in-the-wild of precisely why.
   --titus


Posted by manuelg on 2007-06-29 at 14:59. 

::

   If a threading implementation gives up:    * some latency    to gain:
   * throughput    * ease of use    * simpler implementation    * use of
   C library native OS threads    * and of course, correctness is a must
   That would be a wise thing to do!    That is what the GIL does.  Gives
   up some latency, to gain a lot of desirable properties for a threading
   implementation.    I wish the GIL:    * wasn't global across different
   interpreter running in the same process    * wasn't the **one** and
   **only one** mechanism to handle the parts of the CPython interpreter
   that are not thread safe    * didn't need to be invoked so much (the
   GIL is used for a lot of pointless reference counting bookkeeping for
   immutable objects shared between threads, like integer objects,
   objects representing the classes, etc.)    But, on the whole, not bad.

