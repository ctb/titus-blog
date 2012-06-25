Help! Help! Class notes site?
#############################

:author: C\. Titus Brown
:tags: python,teaching,bioinformatics
:date: 2010-05-21
:slug: help-with-class-notes
:category: science


So, I'm running this `summer course
<http://bioinformatics.msu.edu/ngs-summer-course-2010>`__ and I am
trying to figure out how to organize the notes for students.  I'd like
to mix curriculum-specific notes ("here's what we're doing today, and
here are some problems to work on") with tutorials (material independent
of a single course, like "here's how to transfer files between computers"
or "here's how to parse CSV files"), and allow students to search the
documents, annotate them in their Web browser, search the annotations,
and perhaps even do public or private bookmarking and tagging.  The
ability to edit the primary content in something other than a Web GUI
would be really, really nice, too -- that way I can write in something
like ReST and then upload into the system.

(This *is* a system I could write myself, but that's kind of silly,
dontcha think?)

It should also be lightweight, reasonably mature, easy to set up, and
(preferably) written in Python, although I'm willing to compromise
on the last simply because I'm desperate.

Pointers, comments, suggestions welcome!

--titus


----

**Legacy Comments**


Posted by Katie Cunningham on 2010-05-21 at 14:19. 

::

   How savvy are these students? Could they get by on something like a
   Git or SVN repo? Failing that, I've had good experience using the
   Google suite of apps for class collaboration. Not python, but good in
   a pinch.


Posted by Ratufa on 2010-05-21 at 15:01. 

::

   Sounds like a Wiki would do most or all or what you want.  Try
   MoinMoin if you want something written in Python.


Posted by Ari on 2010-05-21 at 15:08. 

::

   Writing a good CMS in a matter of weeks?  That's a bit of hubris.
   Evernote or alternatives already exist for personal use.    MSU
   provides ANGEL.    Care to explain why the wheel needs reinvention?


Posted by Peter Boothe on 2010-05-21 at 15:31. 

::

   Google Wave worked well both this and last term for my students to
   take group notes and annotate said notes.


Posted by Alan Trick on 2010-05-21 at 17:31. 

::

   Well, there's the django book
   (http://www.djangobook.com/about/comments/) but I don't see any
   released code for that. There's also Stet, the tool they used for
   gathering public comments on the GPL-3 (http://weblogs.mozillazine.org
   /gerv/archives/2006/01/gpl_v3_available_for_comments.html)


Posted by Titus Brown on 2010-05-21 at 22:18. 

::

   As always, these comments -- even the mildly obnoxious ones -- help me
   figure out what I want ;)    Ratufa, Wikis generally don't have great
   editing tools for the initial content generation, and I want to make a
   clear distinction between student/visitor comments and my own content,
   too.  Trac is something I was considering, because I was sure that
   there was some content commenting code available for it ... somewhere.
   Peter, maybe I need to spend more time with Wave, but I don't see how
   it fits any of these needs.  I've tried it out for a few different
   things but not deeply.  Any specific pointers to functionality I
   should try out or look at?  (I do see that it may work for my normal
   Web dev course, so I may try that out -- thanks!)    Katie, having
   something based on a version control system is a great idea, but the
   students are going to be learning command-line stuff as they go, so
   requiring that they become reliable git or hg users in order to
   comment on the git/hg tutorial (for example) is too much for this
   course.    And Ari, ANGEL doesn't provide in-line commenting AFAIK,
   and I have a deep and abiding hatred for its clunky hideous UI, its
   slow speed, and its lack of functionality.  If that's the wheel, then
   it's square and could use some reimplementing.  As for implementing a
   (tailored, hacky) CMS in a day or two?  Sure - weeks? Pshaw.  I don't
   need a full CMS; I have more specific needs.  I've even done it
   before, with Ian Bicking's Commentary.  And presumably if I wanted to
   code something new up I wouldn't have asked all you fine folk ;).    I
   wasn't aware of Evernote, which doesn't fit this project but looks
   awesome!    But I think Alan's comments come closest to what I'm
   looking for -- thanks!  The django book looks awesome, and I can
   always ask @jacobian for his code if necessary, but I'm not a
   djangonut so I'm not sure I would be able to learn the ins and outs in
   time.  However, the stet reference is extra cool, because some
   discrete googling discovers that they now recommend a stet
   replacement... written for django! It's called co-ment.  I will take a
   look at that &amp; report back.    thanks all,    --titus


Posted by Titus Brown on 2010-05-21 at 22:26. 

::

   co-ment references:    <a href="http://www.co-ment.org/">http://www
   .co-ment.org/</a>    Markdown based.  Awesome!    I wonder how hard it
   would be to use sqlite for the backend instead.  Hmm.    OK, I'm
   taking another look at Commentary, too.

