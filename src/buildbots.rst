Buildbots Galore
################

:author: C\. Titus Brown
:tags: python,programming
:date: 2007-02-08
:slug: buildbots
:category: python


I've finally got a buildbot that compiles `FamilyRelationsII <http://cartwheel.idyll.org/>`__ on Linux and Windows/cygwin, and I've got another buildbot
running tests for `twill <http://twill.idyll.org>`__,
`scotch <http://darcs.idyll.org/~t/projects/scotch/README.html>`__, and
`figleaf <http://darcs.idyll.org/~t/projects/figleaf/README.html>`__ on
Linux and Windows.

The convenience of this cannot be overestimated: I no longer need to
boot Windows in order to compile or test my software, and I can
compile my Linux software on a machine separate from my (no doubt
highly munged) development environment.  Whenever I make changes, I
just need to go look at a Web site to see what I screwed up ;).

Both the Linux and Windows machines are running inside of VMware.
Despite my strong OSS leanings, I've been very happy with VMware,
which is considerably advanced over Xen.  The VMware feature that sealed the
deal was the ability to use Python to control processes on the VM
machines, which is something I'll need down the road.  Someone let me know
when Xen gains this feature, yeh?

I'm still working on getting an OS X build slave going.  The OS X VMware
image that's floating around is (a) illegit and (b) difficult to work with;
at the moment I can't even get Python extension to compile on it, blech.

My only real gripe about buildbot is that it requires both
zope.interface and Twisted to run; unfortunately the prebuilt Windows
binaries for both packages are only available for older versions of
Python.  This means that unless I'm willing to compile packages for
Windows, I can only run python2.3 or python2.4.  Furthermore, even on
Linux, there are annoying problems: Twisted simply cannot be installed
with easy_install, and both buildbot and zope.interface have to be
manually downloaded before they can be installed, because easy_install
doesn't find the right packages automatically.  This renders
installation quite a chore.  Maybe after PyCon I'll take a look at
fixing some of these problems.

--titus


----

**Legacy Comments**


Posted by M March on 2007-02-08 at 03:08. 

::

   Am I reading your post right that you are using Python to control VMs
   under VMWare?    How are you doing that? Via the COM API, something
   else?    thanks!


Posted by Petri Savolainen on 2007-02-08 at 05:04. 

::

   Ahem, there <em>are</em> up to date win32 zope.interface binaries
   (3.3.0 for python 2.5). Just not on pypi but on zope.org, compiled by
   me ("saffe") on zope.org. Ask Jim &amp; Fred (maintainers of the pypi
   pkg) nicely, maybe they'll put the binaries there as well.


Posted by Titus Brown on 2007-02-08 at 13:26. 

::

   Petri,    sorry I missed them.  They don't seem to be here:    <a href
   ="http://www.zope.org/Products/ZopeInterface">http://www.zope.org/Prod
   ucts/ZopeInterface</a>    which is where I was looking...?    thanks,
   --titus


Posted by Titus Brown on 2007-02-08 at 13:29. 

::

   Michael, yes, I **plan** to be doing that; see pyvix:    <a href="http
   ://www.testingreflections.com/node/view/4119">http://www.testingreflec
   tions.com/node/view/4119</a>    Here are some slides from our last
   socal-piggies meeting on this subject:    <a href="http://www.socal-pi
   ggies.org/presentations/benedikt_reiter/2007_01_18/pyvix_presentation.
   html">http://www.socal-piggies.org/presentations/benedikt_reiter/2007_
   01_18/pyvix_presentation.html</a>    -titus


Posted by Scott Lamb on 2007-02-09 at 04:06. 

::

   If you're into RPMs, I have ones prepared for zope-interface, twisted,
   and buildbot. a "rpm --rebuild foo.src.rpm" and you're in business.


Posted by Titus Brown on 2007-02-09 at 13:09. 

::

   Scott, do RPMs work on Windows?  (not cygwin, but Windows proper?)


Posted by Scott Lamb on 2007-02-09 at 18:41. 

::

   Not to my knowledge. I'm talking about Linux.

