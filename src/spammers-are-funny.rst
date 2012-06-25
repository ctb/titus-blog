Spammers are funny.
###################

:author: C\. Titus Brown
:tags: python
:date: 2006-10-27
:slug: spammers-are-funny
:category: python


So, I wrote a custom plugin called 'ocomments' that uses an SQLAlchemy-
based database API to assign cookies to users who make comments.  That
way I can control who has automatic posting access (anyone who
posts a sensible message, basically) and who doesn't.  I can also toggle
comment visibility on an individual or user basis.

Initially, I allowed unapproved postings to be made visible.  I hoped
(irrationally) that spammers wouldn't find the blog for a while.

Then spammers found the blog and set up an auto-comment-spam loop.

So I made new posts invisible by default.

And still they post!

Or, at least, they *try* to post.  Heh.

I think that's funny.

It's nice that I can certify users.  It lets anyone who's already
visited post without my ok.  Perhaps someday I'll make the ocomments
plugin publicly available, once I clean it up a bit...

--titus

p.s. I am not Andrew Kuchling!  (c.f. planetpython.org)


----

**Legacy Comments**


Posted by DougN on 2006-10-28 at 00:14. 

::

   Thank you for solving a problem for me I hadn't had time to think
   about yet ^_^.    The same thing can easilly be done with Django
   session cookies and a quick model.


Posted by Titus Brown on 2006-10-28 at 01:32. 

::

   Yeah, but I'm not using Django, I'm using pyblosxom ;)

