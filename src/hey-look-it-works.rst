Hey look, it works!
###################

:author: C\. Titus Brown
:tags: python
:date: 2009-06-02
:slug: hey-look-it-works
:category: python


Apparently the `ipaddr module
<http://docs.python.org/dev/py3k/library/ipaddr.html>`__ in Python 3.1
is disliked by some, and there was a `reasonably robust discussion
<http://mail.python.org/pipermail/python-dev/2009-June/089809.html>`__
on python-dev about how it's wrong, wrong, wrong.  `Guido finally
ruled
<http://mail.python.org/pipermail/python-dev/2009-June/089840.html>`__:
ixnay on the addr-pay.

This is pretty relevant given the twitstorm caused by Zed
Shaw's `ludicrously self-confident rants
<http://www.zedshaw.com/blog/2009-05-29.html>`__ about `how he always
knows best and is a kickass programmer
<http://www.zedshaw.com/blog/2009-05-30.html>`__ and oh, by the way,
the Python stdlib is kinda lousy in places.  I think the thing to take
away from Zed's rant is that the Python module addition process is, in
fact, moderately FUBARed, with some people able to add perhaps
ill-considered modules while others have to struggle to get the time
of day.  (Aahz's `solution
<http://mail.python.org/pipermail/python-dev/2009-June/089843.html>`__
is good -- require a PEP.)

It's relevant personally, too, as I dig my way through some of pygr's
modules.  It's *way* easier to add code than it is to refactor it,
especially if you don't have a lot of unit tests; if you want to
retain backwards compatibility, you're basically doomed.  DOOOMED, I
say!  And that's why the Python stdlib has so many issues.

(Incidentally, nothing against Zed Shaw -- obnoxiousness is his public
persona, and he's definitely worth listening too -- but it is funny to
realize that all his articles contain arguments that boil down to "he
always knows best and is a kickass programmer."  I especially liked
`his statistics rant
<http://www.zedshaw.com/essays/programmer_stats.html>`__.)

--titus


----

**Legacy Comments**


Posted by Paul Boddie on 2009-06-03 at 05:17. 

::

   If one searches Google with "site:docs.python.org ipaddr", the only
   hits are on pages either describing snapshots of the API documentation
   or in the "What's New in Python 3.1" document for 3.1c1. Searching
   generally for "Python ipaddr module" only yields relevant hits in
   exactly the same documents. I'll admit that PEP 375 mentions the
   module, but not by name.    Maybe it has been mentioned elsewhere,
   too, but I sense a case of "beware of the leopard": it's unreasonable
   to criticise people for not giving feedback on something that wasn't
   brought to their attention. Not everyone reads every message on
   python-dev, every new bug in the tracker, or every commit message. And
   many people aren't reading 3.x series plans or announcements because
   they're still using 2.x, and the corresponding document to PEP 375 for
   Python 2.7 (PEP 373) doesn't mention the module.    I think that if
   the core developers genuinely want feedback on such matters (or don't
   want complaints afterwards), they have to communicate these matters
   explicitly to the community. Since the standard library appeared in
   virtually everyone's "Python hates" list, a communication entitled
   "New Modules in Python x.y" would probably get the attention of
   numerous individuals.    I don't really believe that there's a lack of
   community representation in such decisions, or that the core
   developers are prone to "fast-tracking" stuff into the standard
   library, but perhaps they've forgotten what it's like to be out of the
   loop on such matters.


Posted by Noah Gift on 2009-06-03 at 08:57. 

::

   I actually want to make a better Path API, but work 50-70 hours a
   week.  A PEP might be tough for someone like me.


Posted by Titus Brown on 2009-06-03 at 10:03. 

::

   Paul, I sympathize, but I think that the core dev's argument would be:
   if you care about the future of Python, you watch Python-dev!
   Admittedly, requiring PEPs will help.  But the ipaddr stuff seems to
   have been rooted in poor communication rather than the addition flying
   under the radar.    Noah: exactly.  What makes you think you have the
   time to contribute to core if you don't have the time to explain and
   explore your ideas properly? ;)    --titus

