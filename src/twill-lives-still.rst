Twill lives!
############

:author: C\. Titus Brown
:tags: python,testing,twill
:date: 2009-04-12
:slug: twill-lives-still
:category: testing


One of the advantages of this year's PyCon was that it was (again)
held in Chicago, the home town of Leapfrog Online.  Since they use
twill quite a bit, and were bothered by some of the poor design
decisions and bugginess, they were keen to get together with me to
move twill forward.  So we scheduled a sprint for the Monday after
PyCon.

In preparation for the sprint, I did a bit of research into how widely
twill was being used.  Downloads only roughly correlate, but I was
surprised to discover that in just the last year, there were over
6,000 downloads from my site; this doesn't count Debian users, who can
install it from one of the Debian dists.  I'd also been surprised by
the number of people at PyCon who came up to me and told me that they
were using twill internally in their companies -- at least two very
expert groups had settled on it for some of their internal monitoring
and testing.  Very cool!  What this told me is that twill is very
nice, simple and usable for many people and we shouldn't get too
adventuresome; good thing to know ;).

The sprint basically consisted of us talking through a few fundamental
issues like bundling and future development, then fixing a few items,
while I forwarded on all of the bug reports I've gotten over the last
two years.

The source code has now moved to `code.google.com/p/twill
<http://code.google.com/p/twill/>`__ and you can see `all of the
issues in the usual place
<http://code.google.com/p/twill/issues/list>`__.

During the sprint we made a few decisions:

 - 0.9.2 is Coming Real Soon, as a largely feature/API-stable release
   that fixes a number of simple bugs and integrates the latest
   mechanize.

 - for 0.9.2 and 1.0 we will provide both bundled and unbundled
   versions of twill; the bundled versions will contain BeautifulSoup,
   mechanize, ClientForm, and pyparsing.  The unbundled version will
   simply specify what versions of those packages it needs.  This
   unbundling will help packagers out while letting individuals (like,
   say, Windows users) install twill easily.

 - 1.0 is further down the road, but will only add a few features.
   The main goal of 1.0 is to be nice & stable.

 - 2.0 and beyond is on the table but exactly what it will be is
   unclear.  I have my own ideas but since I'm not doing much Web
   developing I may let others take over.

Since the sprint, Pam Z. finished putting the issues into the tracker
and we've been slowly trying to work through them.

Props to Pam Z., Nat W., Kevin B., and Jesse for coming to the sprint,
and to Terry Peppers and Leapfrog for pushing it!  And thanks to
Leapfrog for an excellent steak dinner afterwards ;)

--titus


----

**Legacy Comments**


Posted by pam on 2009-04-12 at 14:55. 

::

   Hey, and thanks for actually having the sprint. I had a surprisingly
   good time. (And I'm continuing to have a good time, in case my antics
   weren't making that clear.)

