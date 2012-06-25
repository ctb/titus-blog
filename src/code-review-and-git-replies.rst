Lazyweb results: code review and git.
#####################################

:author: C\. Titus Brown
:tags: python
:date: 2008-12-24
:slug: code-review-and-git-replies
:category: python


Here's a summary of the e-mail responses I got to my `lazyweb query re
code review and git
<http://ivory.idyll.org/blog/dec-08/code-review-and-git.html>`__.

A few people (Paul Nasrat and Jeff Balogh) pointed out that `Review
Board <http://www.review-board.org/>`__ supports git.  So I may try
that.

Charles McCreary has had good experience with Rietveld, but I don't
think that it has mature git integration -- although `git-cl looks
interesting
<http://groups.google.com/group/codereview-discuss/browse_thread/thread/d9f65d04165e274f/b8740b9beab78e4c?lnk=raot>`__.
However, from what I understand git-cl works in tandem with svn,
letting you associate git patches with particular Rietveld issues and
then commit them to svn.  Since we're eschewing svn completely, that might
not work well.

Jeff Balogh also discussed `Gerrit
<http://google-opensource.blogspot.com/2008/11/gerrit-and-repo-android-source.html>`__
a bit, and suggested I try it; it's an adaptation of Rietveld to
support git.

Jeff also pointed me towards some great resources: Alex Martelli's
`Code Reviews for Fun and Profit <http://tr.im/2fk4>`__ and some launchpad (?) discussion
on a mailing list about `how to make code reviews work better <http://basieproject.org/pipermail/basie-dev/2008-September/000569.html>`__.

Jeff's other words of wisdom for code reviews:

 - ask lots of questions, but be prepared for blowback from people that
   think you're being a jerk.

 - get as many people involved in code reviews as possible, as soon as
   possible, or else you might get stuck being the "code review" person.

Finally, Andriy Khavryuchenko pointed me towards his new startuplet,
reviework.com -- `blog post here
<http://a.khavr.com/2008/11/12/our-first-startuplet-code-review-service/>`__.
This is a "code discussion" service that seems like it would integrate
well with a lightweight git-based code review approach.  I may bug him
about an opportunity to beta test reviework once I actually have some
experience with code review...

Thanks, everyone!  I'll be sure to post about how the code reviews go.

--titus


----

**Legacy Comments**


Posted by Gregg Sporar on 2008-12-26 at 13:55. 

::

   To a certain extent, it's **how** you ask a question during code
   review that influences whether people think you are being a jerk.  For
   example, instead of asking "why did you use method x()..." ask "by
   using method x(), what did you have in mind?"  More tips here: <a href
   ="http://smartbear.com/docs/CodeReviewSocialEffects.pdf">http://smartb
   ear.com/docs/CodeReviewSocialEffects.pdf</a>

