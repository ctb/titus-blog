Replaying HTTP
##############

:author: C\. Titus Brown
:tags: python,scotch
:date: 2007-02-17
:slug: replaying-http
:category: personal


Ran across `this diary entry
<http://www.advogato.org/person/wainstead/diary.html?start=56>`__ from
wainstead, and just wanted to mention that this sort of thing
(replaying HTTP traffic) is something that I do with `scotch
<http://darcs.idyll.org/~t/projects/scotch/doc/>`__ quite
successfully.  It hasn't proven to be particularly useful in my own
projects yet, but it has been nice when debugging JavaScript-y web sites
for clients.

(wainstead, if you see this, you might take another look at `twill <http://twill.idyll.org/>`__. Yes, it's in Python, but we can have the mortal combat about languages AFTER you see if it helps you solve your problem(s) ;).  It integrates well with scotch, does HTTP and HTTPS, and can be integrated with unit test frameworks quite easily.  I see you've already tried it, so I'd like to hear what problems you had with it.)

--titus


----

**Legacy Comments**


Posted by Steve Wainstead on 2007-02-22 at 17:59. 

::

   Hey Titus! Thanks for the reply on advogato.    I did look at twill; I
   think the reason I didn't use it was because I'd have to roll my own
   testing stuff then (did the page say "Parse error"? Things like that).
   And anything I looked at that used a proxy server couldn't do https.
   Does scotch get around that?    I have no fear of Python :o) I did a
   lot of LDAP and DB2 scripts with Python up until about a year ago.
   ~swain

