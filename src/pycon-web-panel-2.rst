PyCon Web Panel Thoughts
########################

:author: C\. Titus Brown
:tags: python,pycon07
:date: 2007-02-14
:slug: pycon-web-panel-2
:category: python


First, let me mention that I've recruited Duncan McGreggor to the panel
to talk about twisted.web and Nevow.  That makes it a real party!  In random order, we now have:

 * Zope: Jim Fulton

 * Pylons: Ben Bangert

 * Django: Adrian Holovaty

 * CherryPy: Robert Brewer

 * TurboGears: Kevin Dangoor

 * pyjamas: James Tauber

 * twisted.web/Nevow: Duncan McGreggor

Now, as Ian point out in the comments on my last `PyCon Web Panel post
<http://ivory.idyll.org/blog/feb-07/pycon-web-panel.html>`__, the
questions on my `original announcement
<http://ivory.idyll.org/blog/oct-06/pycon-web-panel.html>`__ are
pretty insipid and will likely lead to a boring panel.

So, courtesy of our SoCal Piggies members, and David Pollak's `Web Framework Manifest <http://blog.lostlake.org/index.php?/archives/16-Web-Framework-Manifesto.html>`__, here are some slightly more pointed questions.

Can be asked of anyone:

 * why does your framework exist, given that so many others already exist?

 * what future does your Web framework have?

 * what sort of testing hooks have you made available?

 * what's the best Web framework?  ok, yours -- but the next best is...?

 * what's your favorite dead Python Web app/framework/approach?

 * before you wrote/got involved in developing your own Web framework,
   what frameworks did you use?

 * what impact has WSGI had on the way you think about extending your
   Web framework?

Specific framework/person questions:

 * Zope/Twisted: your community seems fairly insular. Is this true?
   (Assume yes.)  Is it by design?  If so, why; if not, what do you
   think are the causes and do you want to change it (and, if so, how;
   if not, why not?)?

 * Robert Brewer: last year you'd just debugged a nasty threading
   problem in CherryPy, and you promised me you'd have a solution for
   debugging Web server/load testing/threading problems of problem by
   PyCon '07.  Now I've got you in front of several hundred people --
   what was the problem? do you have a general testing/debugging solution?
   what is it?

 * pyjamas: JavaScript is quickly gaining more and more toolkits.  Why does
   yours exist?  Where do you plan to go with it?  What Web servers does it
   work well with?

OK, I'm out of creativity for the evening.  Does anyone have any
suggestions?  Remember, the object is to ask interesting questions
that will have *both* entertaining and *informative* responses.  In
particular, I'm not going to ask a question that will get me beaten ;).

I'm also still a bit stuck on the format.  I'd like to do some sort of
introduction, but that will take up a fair bit of time.  I'd also like
to have audience participation.  Blech.  We only have 45 minutes... Thoughts?

--titus

p.s. I have to approve new posts/posters, so comments may be delayed
in appearing.  Sorry.


----

**Legacy Comments**


Posted by Greg Wilson on 2007-02-14 at 06:07. 

::

   You could also ask how each framework performs under heavy load, and
   what data the panelist's answer is based on.  (I'd really, really like
   some cross-framework load benchmarks...)


Posted by Eric Hopper on 2007-02-14 at 09:18. 

::

   I have to verify this, but I strongly suspect that Twisted at its very
   heart has a design flaw that enables DOS attacks on Twisted services.
   This is perhaps not a problem for web services, but it is for things
   that have long-running sessions.    Basically if you can keep on
   sending a Twisted service things that cause it to send you stuff back,
   but you never read what gets sent back, you eventually run the Twisted
   service out of memory because it keeps on buffering output forever.
   This is because in Twisted write calls never fail and don't return
   deferreds.    This could be tested by setting up a simple Twisted
   based echo service and making a client that sent an infinite stream of
   stuff on a single connection but that never read.


Posted by Titus Brown on 2007-02-14 at 13:21. 

::

   Greg, good idea!  I was actually thinking just yesterday that the
   separation of "server" from "app" inherent in WSGI makes this much
   easier now.    Security models might also be useful to discuss...
   Eric, have you talked to the Twisted people about this, or written a
   DOS exploit?  I probably shouldn't bring this up in the panel ;)
   --titus


Posted by matt harrison on 2007-02-15 at 02:19. 

::

   Here's a few::    * Has WSGI (PEP333) actually made your life easier?
   Have you gotten any benefit from it?  Is there some "untapped" benefit
   that we could get from it but aren't?    * If your framework didn't
   exist today, would you use an existing one or re-create yours?  Why?
   (I think this is better than which is "2nd best")    * What are the 2
   or 3 strongest points of your framework?    * What is the weakest
   point of your framework?    * What are some of the things that you
   feel have helped your project run smoothly (or gain developers/users)?
   * Imagine that you had perfect hindsight.  What if anything would you
   have done differently with your project?  Why?    * [Slightly OT] What
   is more important, having a community of users or having a technically
   superior product?  Why?    * What is the best way to deploy a python
   web app?  Mod_python?  Reverse proxy (through apache/lighty/nginx)?
   SCGI?  Mod_wsgi?  (Pylons/TG/Django all tell a different story in
   their docs, why is that?)    * Slightly related to the previous.  What
   is the best way to integrate a python web app with existing apps say
   written in perl or php?  (fex: I want to use wordpress or mediawiki,
   with my widgets++ app)    * I've heard that JRuby support for Rails
   will provide a clean path for lost wandering J2EE souls.  Should
   effort be put into jython/modjy to support your framework?


Posted by Titus Brown on 2007-02-15 at 14:44. 

::

   Matt, clearly you should be running the panel rather than me...
   thanks, those are great questions!


Posted by Eric Hopper on 2007-02-15 at 16:07. 

::

   Titus, I haven't written an exploit yet.  **sigh**  I need to get on
   that.  I'm 95% sure it would work the way I'm expecting.    I will try
   to remember to come back here and say something when I've written it.
   I have mentioned it to the Twisted people on the IRC channel, but they
   (unsurprisingly and quite reasonably) want me to write an exploit as
   well.  :-)


Posted by Drew Perttula on 2007-02-16 at 01:59. 

::

   Another way to trigger discussion about framework features:    Suppose
   your framework cannot be used anymore and you have to port to a
   different one. What are going to be the biggest issues, that is, what
   are the important and practical parts of your framework that you think
   would be hard to emulate in any other?

