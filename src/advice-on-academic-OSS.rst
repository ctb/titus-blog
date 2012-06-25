Some advice on niche OSS projects
#################################

:author: C\. Titus Brown
:tags: python, oss
:date: 2006-11-03
:slug: advice-on-academic-OSS
:category: python


A local friend asked for advice on her OSS project, because her boss
is questioning the value of making things OSS.  Here's my rambling
reply, preserved for posterity: ::

  There are several de facto models of open source at this level (the
  small niche projects level, that is).
  
  The first is "here's my stuff. I can't be bothered to maintain it, but I
  hope other people find it useful."  This is a good default for academic
  projects.
  
  The second is "here's my stuff.  Let me know if you have trouble     
  installing it or using it and I'll help you work through the issues."
  Most of my projects sit here.
  
  The third is "here's my stuff.  Enough people have been using it that
  you should be able to install/use it without any problems.  Please let
  me know if you have problems and I will fix them."  twill sits here.
  
  The next level is when you have multiple people at multiple places
  orking on the project, which complicates issues in different ways ;).
  
  Making the transition #1 to #3 involves more and more maintenance
  work, both up-front (building automated tests so that bitrot doesn't
  set in) and throughout (supporting people who are installing it).  The
  return is that often you find bugs that you didn't know about, or get
  contributions from people that extend your software in unexpected (and
  good!) ways.
  
  So, why do you push for open source?  Because "it's the right thing to
  do"?  That doesn't necessarily hold much weight with people ;).  Or
  because you want other people to use it, and improve it?  And if the
  latter, what is your model for roping other people into the software?
  
  My two most used projects are FamilyRelations and twill.  For the
  former, I wrote a tutorial and made it as easy to use as possible.  It
  still wouldn't have been used if it weren't actually effective, as
  well.  This seems like a good model for your software, but it requires
  *work* (making it easy to use and documenting it).
  
  twill is also effective, and it has a *very* low barrier to entry.
  Moreover, people actually contribute to it: but it has a much more
  technical audience, too.  (Nobody really contributes to FRII.)
  
  So getting back to your project, I think that may be what you need
  to explain to your boss: that substantial work is needed to make
  software *usable*, and that's a prerequisite for use, which in turn
  is a prerequisite for contributions.  If that's your goal, then you
  need to work more.  If not, then please make it OSS so that when
  I stumble upon your project in 3 years and want to use it, I don't
  need to reimplement it from scratch first.

Long and rambling, but the point I wanted to make is that you can't expect
returns from OSS projects without a certain upfront investment.  I enjoy that
investment, but it's not to everyone's taste or even within their capabilitie
(time & $$ especially).

--titus


----

**Legacy Comments**


Posted by Steve Holden on 2006-11-03 at 15:34. 

::

   It was Fred Brooks in the Mythical Man-Month, I believe, who pointed
   out that a it takes three times as much effort to build a system as a
   program, and three times as much effort to build a product as a
   system.    If you have a program that you want to turn into a program
   system product, therefore, expect to spend about eight times as much
   effort as it took to build the program in the first place.    That's a
   **major** investment that customers who know "a little something"
   about programming frequently fail to appreciate.

