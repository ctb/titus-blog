PyCon '08 Tutorial Proposal - RFC, and suggested projects.
##########################################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2007-11-12
:slug: pycon08-tutorial
:category: python


Hey everyone,

Grig and I are thinking of doing another tutorial at PyCon '08, but
we'd like to break out of the mold of "intro testing" and do something
more exciting for us.  Here's a promotional blurb: ::

  Practical Agile Web Testing
  ---------------------------

  Have Web site?  Need testing?  Bring your tired (code), huddled (unit
  tests), and cranky AJAX to us; we'll help you come up with tactics,
  techniques, and infrastructure to help solve your problems.  This
  includes integration with a unit test runner (nose); use of coverage
  analysis (figleaf); straight HTTP driver Web testing (twill); Web
  recording, examination, and playback (scotch); Selenium and Selenium
  RC test script development; and continuous integration (buildbot).
  We will focus on techniques for automating your Web testing for quick
  turnaround, i.e. "agile" test automation.

Full proposal "below the jump", as they say.  Comments welcome!

The plan is to have attendees send us their projects in advance, along
with some of the real-world problems they need solved.  This can range
from "HELP, I need to start testing!" to "What should I do next?" to
"How can I test this !#%!%$ JavaScript??"  We will then actually
implement test code and infrastructure to solve these
problems. Getting this to work right will be challenging but fun --
Grig and I both love doing live presentations.

We could use some suggestions, though: in case we get a lot of
attendees but no one sends us projects in advance, we'd like to have a
few projects on our back burner.  What Python Web projects need this
kind of testing?  Go ahead, hit us ;)

--titus

Full proposal: ::

  Title: Practical Agile Web Testing (Hands-On)
  
  Presenters: C. Titus Brown <titus@idyll.org>
  	    Grig Gheorghiu <grig@gheorghiu.net>
  
  Intended audience: advanced users.
  
  Tutorial format: hands-on / Q&A.  Attendees should send us actual problems
  	 from open source projects that need solving (preferably more than
  	 an hour in advance...)
  
  Recording: We give permission to record and publish my PyCon tutorial for
  	   free distribution.
  
  Requirements: Python 2.5 or 2.6 installed.  We'll provide media with up-to-date
  	      packages at the tutorial.
  
  Notes for reviewers: we've done two testing tutorials before, with good
        comments afterward.  The goal here is to break out of the mold of
        pre-planned presentations and tackle some real-life problems for people.
        We will prepare in advance, but using other people's source code as
        a starting point.
  
  Promotional summary:
  
  Have Web site?  Need testing?  Bring your tired (code), huddled (unit
  tests), and cranky AJAX to us; we'll help you come up with tactics,
  techniques, and infrastructure to help solve your problems.  This
  includes integration with a unit test runner (nose); use of coverage
  analysis (figleaf); straight HTTP driver Web testing (twill); Web
  recording, examination, and playback (scotch); Selenium and Selenium
  RC test script development; and continuous integration (buildbot).
  We will focus on techniques for automating your Web testing for quick
  turnaround, i.e. "agile" test automation.
  
  Detailed tutorial outline: A 30 minute introduction to the basic testing
  	 philosophy and tools, followed by discussion and implementation
  	 details for the individual problems we have chosen.
  
  Presenter bios:
  
  Titus Brown is a CS professor at Michigan State U. and a contributor
  to numerous open source projects, including twill, scotch, figleaf,
  and nose. Grig Gheorghiu is the Director of Technology at RIS
  Technology, a Web hosting company. Grig maintains the Python Testing
  Tools Taxonomy wiki page, and he blogs fairly regularly on Python and
  agile testing topics at http://agiletesting.blogspot.com.  Together
  with Jason Huggins, they are the authors of **An Introduction to
  Functional Web Testing with twill and Selenium**.
  
  Previous experience:
  
  Grig and Titus have given two previous testing tutorials at PyCon '06
  and '07, with positive results.  They both speak regularly at PyCons
  and they are also organizers of the SoCal PIGgies group where they
  present regularly.


----

**Legacy Comments**


Posted by Terry on 2007-11-12 at 23:01. 

::

   Idea #1...    So I think the one problem that's always perplexed me is
   this:    Say you have:    1) Site A    a) Experience 1    b)
   Experience 2    2) Site B    a) Experience 1    b) Experience 2    The
   sites are really similar in terms of functionality, the experiences
   are really different layouts.     How can I write 1 test to do
   something (anything really, click links, etc) but call it in the
   following fashions:    - Run for Site A, Experience 1  - Run for Site
   A, Experience 2  - Run for Site A, Experience 1 and Experience 2  -
   Run for Site A and Site B, All Experiences    Foolishly, I thought
   this could be a Nose plugin. According to Jason, that might not be
   possible. I'm able to sort of pull it off with some closures but it
   doesn't seem elegant.     -----    Idea #2    What about test
   configuration? I've been using Fuzzyman's ConfigObj with some decent
   success to create configuration files that are helpful for test
   suites.    -----    Idea #3    Exposition of the "holistic" Testing
   pyramid by Brown/Huggins/Gheorghiu. Examples of how a combination of
   how Twill and Selenium attack and solve testing problems differently
   but ultimately are excellent tools to use hand-in-hand.


Posted by Doug Napoleone on 2007-11-13 at 00:35. 

::

   Sounds like a fantastic Idea to me!  I have a website which needs
   testing (though I think that most of it will be done as part of a
   sprint if I can swing it ;-)    The schedule system really needs some
   help with testing for the ajax stuff so I might just end up going for
   it. Complex permission based content can be a real pain.    Any chance
   of another testing tools panel?


Posted by Kumar McMillan on 2007-11-13 at 11:58. 

::

   What Is the most popular blogging software used on the Internet?
   Give Up?    <a href="http://wordpress.org/">spoiler</a>    Since
   everyone uses this, even <a href="http://wordpress.org/">Python
   hackers</a>, it must be a solidly tested product, right?  THERE ARE NO
   AUTOMATED TESTS for this product whatsoever.  It is manually tested by
   hundreds of users before rollout.    So, hey, you could always fire up
   twill/selenium and start adding some regression tests (you will all be
   heroes!).


Posted by Titus Brown on 2007-11-13 at 16:54. 

::

   WordPress is an interesting idea. Dr.Project is an idea that Greg
   Wilson passed on a while ago, too.    Terry, I have to admit to being
   generally confused by your first question.  Could you give me a
   concrete example?    I also would say that having us write yet more
   tools-for-testing might not be the way to go, given that I can't even
   seem to get a 1.0 release out for twill ;)    --titus


Posted by Terry on 2007-11-13 at 22:30. 

::

   Everyone's always confused when I bring this up. Even Kumar and Jason!
   ;)    I'll mock it up.

