Unintended consequences of the decorator notation
#################################################

:author: C\. Titus Brown
:tags: python
:date: 2007-06-20
:slug: unintended-consequences-of-decorator-notation
:category: python


Spoke yesterday with Bill Punch, a CS professor at MSU who is using
Python for intro CS.  He told me his tale of tracking down what an '@'
sign meant (it's a decorator,
http://docs.python.org/ref/function.html).  Needless to say it took
him quite a while to google about and figure out what it did, because
searching for '@' and 'python', in any combination you care to name,
turns up many irrelevant hits.

A neat example of unintended consequences ;).

--titus

p.s. Incidentally, '@' really should be in the index, no?  It's not
there: http://docs.python.org/ref/genindex.html,
http://docs.python.org/lib/genindex.html.


----

**Legacy Comments**


Posted by Kumar McMillan on 2007-06-20 at 11:31. 

::

   This reminds me of my newbie days; imagine staring at :    def
   foo(**args, ***kw):    pass    and trying to figure out what * and **
   do!  Well luckily searching "python def asterisk" brings up something
   useful now but "python def star" does not.      Maybe we should write
   blog posts entitled "python at sign" and "python def star" :)


Posted by Greg on 2007-06-20 at 13:05. 

::

   My friend Matt says decorators are a way to make your code harder to
   read :-)    In all honesty, I never got used to the syntax, it just
   feels too "magical" to me.  I put this @ thing and now my function
   gets wrapped by another function?  Kinda spooky..  I'm not sure why
   everyone else loves them?  Any ideas?


Posted by Titus Brown on 2007-06-20 at 14:34. 

::

   Greg -- there's a long discussion of the rationale behind the syntax
   in the PEP, <a href="http://www.python.org/dev/peps/pep-0318/">http://
   www.python.org/dev/peps/pep-0318/</a>...

