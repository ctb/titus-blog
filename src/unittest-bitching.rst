``unittest`` bitching: premature; lazyweb request
#################################################

:author: C\. Titus Brown
:tags: python
:date: 2007-03-21
:slug: unittest-bitching
:category: python


From reading `Collin Winter's blog
<http://oakwinter.com/code/a-new-unittest/>`__ he's designing a new
``unittest`` module *first*, and *then* he's going to ask c.l.p and
presumably python-dev about adding it to py3k.  So it's not quite the
fait accompli I thought it was, which reduces my complaints to mild
grumbling.

And, dear lazyweb... is there a good way to find out when a particular
line of code was introduced (or last touched) through subversion?

thanks,
--titus


----

**Legacy Comments**


Posted by Karl G on 2007-03-21 at 14:42. 

::

   svn blame:    <a href="http://svnbook.red-
   bean.com/en/1.0/re02.html">http://svnbook.red-
   bean.com/en/1.0/re02.html</a>


Posted by Robert Brewer on 2007-03-21 at 14:45. 

::

   You mean besides "svn blame"?


Posted by Carl Friedrich Bolz on 2007-03-21 at 14:47. 

::

   To find the person that last modified a file in subversion, use "svn
   blame".


Posted by Ian Bicking on 2007-03-21 at 14:52. 

::

   svn blame does what you want, I believe


Posted by Mark Mc Mahon on 2007-03-21 at 14:54. 

::

   How about      svn blame /path/    to see the revision number that the
   line was last modified in (and user too).    Then    svn log -r XXX -q
   /path/    to get some information on that revision.    I am not an svn
   expert - so maybe there are cleaner ways of getting the same
   information.    Mark


Posted by Titus Brown on 2007-03-21 at 15:31. 

::

   Ahh, thanks all.  I didn't realize that svn blame output that
   information.    tnx,  --titus


Posted by Luis Bruno on 2007-03-21 at 15:46. 

::

   This is the link in the RSS feed, according to Google: <a
   href="http://ivory.idyll.org/blog/2007/03/21/unittest-
   bitching">http://ivory.idyll.org/blog/2007/03/21/unittest-bitching</a>
   Please fix; thanks!


Posted by Titus Brown on 2007-03-21 at 17:38. 

::

   Luis, I don't understand.  There's nothing like that in the atom feed
   that I can see, and I don't name links like that.  Where do you find
   this?  "Google" is big ;).    --titus

