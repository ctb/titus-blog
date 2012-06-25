Lesson of the day
#################

:author: C\. Titus Brown
:tags: python
:date: 2007-10-26
:slug: lesson-of-the-day
:category: python


If you use ``sys.settrace`` to set a tracing function, and that function
prints to ``sys.stdout`, then don't ever trash ``sys.stdout``, even
briefly.  You will raise an invisible exception and your trace function
will be removed.

(I don't know precisely what is *supposed* to happen when a trace
function raises an exception, but it seems like it is being removed.
Fair enough.  But frustrating.)

This cost me a few days of intermittent repair attempts on figleaf.

Perhaps I will track down this behavior and document it in the Python
docs...

--titus


----

**Legacy Comments**


Posted by Brett on 2007-10-26 at 17:18. 

::

   The stopping of the trace makes sense as a trace function is supposed
   to return itself after each call.  Obviously an exception blocks that.
   As for no traceback if sys.stdout is lost, that is also expected as
   the C code actually grabs that attribute directly off of the module
   and prints to it.  I am pretty sure that sys.<em>_stdout_</em> is only
   there to make it easy to reset sys.stdout later if you happen to
   replace it with something.


Posted by Titus Brown on 2007-10-26 at 20:54. 

::

   Right you are -- all expected behavior.  I forgot that the local trace
   function also needs to return itself!    &lt;sigh&gt;

