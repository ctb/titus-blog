Why does my iPhone know how to spell Cthulhu?
#############################################

:author: C\. Titus Brown
:tags: random,python
:date: 2009-08-30
:slug: iphone-cthulhu
:category: python


Very odd.  I mean, it's nice to have my prayers spell-checked and all,
but really, Apple?  Cthulhu?

Also, `jinja2 <http://jinja.pocoo.org/2/>`__ rocks.  I think I'll be teaching
it as a templating language this term...

And finally, people interested in using sqlite3 for shelve-like
storage in Python 2.x can take a look at `issue 52
<http://code.google.com/p/pygr/issues/detail?id=52>`__ in pygr's issue
tracker; I've taken the code from `bugs.python.org/issue3783
<http://bugs.python.org/issue3783>`__ and "backported" it to Python
2.x.  Since bsddb is no longer going to be part of the Python stdlib,
we're planning to switch to using sqlite3 for scalable data storage.

--titus


----

**Legacy Comments**


Posted by LE on 2009-08-30 at 16:29. 

::

   sqlite3, scalable data storage? What.


Posted by Titus Brown on 2009-08-30 at 19:39. 

::

   Well, better than other-shelve like options, yes?  What do you
   suggest?  It needs to be in the Python stdlib, OR pure Python and
   easy-to-install, or it becomes a significant burden for our users.
   We already support MySQL etc for power users.    Also see    <a
   href="http://ivory.idyll.org/blog/jan-09/lazyweb-worm-options-in-
   python">http://ivory.idyll.org/blog/jan-09/lazyweb-worm-options-in-
   python</a>


Posted by Catherine Devlin on 2009-08-30 at 23:10. 

::

   That's cool, but does it also know "fhtagn"?  I always have to Google
   it.


Posted by Erich Schwarz on 2009-08-31 at 02:05. 

::

   There once was a time when I didn't have to use Google to remember:
   <i>"Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn"</i>    but
   that was in the long-lost Elder Days, when dinosaurs and Ronald Reagan
   ruled the Earth.    Now, if your iPhone can spell-check <i>that</i>,
   I'd start worrying.


Posted by Gael Varoquaux on 2009-08-31 at 07:10. 

::

   I am really worried by the loss of shelve (or rather the only
   reasonable backend to it). Sure, it is not scalable and fragile, but
   it provided very useful functionality in the standard library.    I
   see that in pygr you have decided to use sqlite3 to replace it. Is
   there a consensus that this is how it will happen in the standard
   library? I have tried following this discussion, but got lost as it
   spread over too many threads.


Posted by j_king on 2009-08-31 at 09:00. 

::

   Ditching bsddb? Ouch.    I'm currently using shelve as the storage
   backend for a small desktop application of mine. Works great. Don't
   see why it needs to be removed.    Is the discussion on this one over?
   As for the "Cthulu" thing, I noticed this too and thought it was
   funny.


Posted by Titus Brown on 2009-08-31 at 09:52. 

::

   j_king, yes, it's gone.  The decision was made back in ... January?
   I'll see if I can track down the python-dev thread.    Gael, there's
   no official solution.  Python-dev hasn't discussed it much if at all,
   and the patch to add shelve/sqlite3 functionality into python 3.x has
   been abandoned.    --titus


Posted by alex dante on 2009-09-01 at 03:24. 

::

   Has the 3rd party shove module been considered as a replacment for
   shelve?    "shove is a object storage frontend inspired by the
   standard library's shelve module. It features a dictionary-style API,
   automatic object storage (with pickle) with in-storage compression
   (with zlib), and multiple storage and caching backends."    <a href="h
   ttp://pypi.python.org/pypi/shove">http://pypi.python.org/pypi/shove</a
   >    Hmm, it's only for 2.x at present, but I'd personally feel a lot
   happier about updated existing code being added to the stdlib than an
   entirely new module.


Posted by Ian L on 2009-09-01 at 18:46. 

::

   Well chrome's autospell doesn't know how to fix it. Perhaps that's
   because google's motto is "don't be evil" which makes me wonder what
   apple really means when they say "think different" ;)


Posted by Titus Brown on 2009-09-08 at 22:28. 

::

   I know about shove, but I haven't heard anyone proposing it for the
   stdlib.  Is it widely used?

