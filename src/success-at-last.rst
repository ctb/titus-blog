Success, at last!
#################

:author: C\. Titus Brown
:tags: python,smoking
:date: 2009-09-06
:slug: success-at-last
:category: misc


For only the second time (out of many tries) I managed to smoke some
salmon and trout so that it was not overcooked and dry as a bone.
Conclusion? I think my smoker thermometer is about 50 deg F off of the
true "on grill" temperature, probably because it's about 3/4 of a foot
above the grill level.  So I just let the smoker sit at a lower
measured temperature and voila, tasty fish!

I *also* got a full Windows dev environment working, from scratch, for
Python.  I took advantage of the Snakebite MSDN account to grab
Windows XP and Visual Studio 2008, and then used Parallels to create
a VM and install everything.

A few comments:

Parallels (a Mac OS X app) makes Windows much more bearable.  On first
blush, they've really got a good setup for people who only occasionally
need to use Windows and generally hate every minute of it.  It's kind
of funny, really; even the Windows emulator is better on the Mac than
Windows is itself!

It took about 24 hrs of futzing to get everything installed and
updated.  I ran into several situations where I had to turn off the
Parallels disk sharing setup (which shares disks between the Mac host
and the Windows VM) in order to install packages.  This included the
Python 2.6.2 MSI installer, the Service Pack 2 upgrade, and (I think)
MySQL 5.1.

The purpose of this Windows futzing is to get a build client system
going for Windows XP; for that, I needed git and svn. I'm happy to
report that both git and svn have clients that are pretty much trivial
to install on Windows, and seem to Just Work: I used `msysgit
<http://code.google.com/p/msysgit/>`__ and the `Tigris.org download
<http://subversion.tigris.org/getting.html#windows>`__.

I ran into an infuriatingly opaque error compiling MySQLdb, and had to
figure it out myself; I didn't run across `this response
<http://forums.mysql.com/read.php?50,247493,247493>`__ until too late.
Briefly, if you have MySQL 5.1 installed, _winreg returns an error,
"the system cannot find the file specified"; you need to update
MySQLdb's site.cfg to look for MySQL 5.1 instead of 5.0.  This seems
like something that should be in MySQLdb...

Speaking of MySQLdb, it'd be nice to have binary packages of some
version or another for Python 2.6.  Binary builds for Windows of
packages with C extensions are really important for users.  Hopefully
I can help provide a better solution for this down the road.

Anyway, now I have a full blown dev environment: I can compile and
test pygr, I can compile and test CPython itself, and I'm happy.

I can even sit back and eat some yummy smoked fish.  How is that not a
win?

--titus

p.s. Now I have to repeat all of this for another Mac by which time I will
be an expert, I'm sure!  Bleah.


----

**Legacy Comments**


Posted by matt harrison on 2009-09-06 at 18:18. 

::

   We want the smoked fish recipe....


Posted by Titus Brown on 2009-09-06 at 19:43. 

::

   Brine medium-to-large trout and/or salmon filets in sealed bag for
   24-48 hrs; I covered them with equal parts water and soy sauce, and
   threw in a cup or so of brown sugar.    Dry for 3-12 hrs by placing on
   paper towels near moving air (a ceiling fan, for example).    Start
   smoker with hickory and/or maple and/or alder.  Bring to a temperature
   of ~200 F.    Once the temperature has stabilized, put fish in smoker.
   Let smoke for 12-16 hours.  Check the temperature -- it should be
   ~140-160 F.    --titus


Posted by Winfried Maus on 2009-09-07 at 10:19. 

::

   &gt; even the Windows emulator is better on the Mac than Windows is
   itself!    Only that Parallels is not a Windows emulator, but a
   virtualization software which is used to run a real - and not an
   emulated - Windows. But you are right that the Parallels virtual
   machine provides an excellent Windows experience - at least for
   Windows XP.    However, in my experience, VMWare Fusion is the
   superior product both in terms of flexibility and robustness.
   Especially when you need to run a 64-Bit flavor of Windows or any
   other operating system.    Unfortunately, Apple's Snow Leopard release
   is almost as much a disaster as the Leopard release was. Leopard
   became usable with the 10.5.2 update but still was a no-go on PowerPC
   machines with less than 2 GB RAM.    It's also sad that I have less
   stability and compatibility issues and better performance when I run
   64-Bit Vista SP2 on my Mac Pro instead of Snow Leopard.    All in all,
   I no longer believe that Apple offers a superior user experience than
   Microsoft. Except for a missing QuickLook-like feature, Windows 7
   looks more promising and mature to me than Snow Leopard.


Posted by Titus Brown on 2009-09-08 at 22:32. 

::

   Winfried, I'm surprised to hear that - I haven't heard of too much
   instability on SL, and in any case SL looks like a really nice
   incremental step.  I have yet to see a Windows release that simplifies
   things...


Posted by Rosangela Canino-Koning on 2009-09-09 at 16:46. 

::

   Regarding gui SVN clients on Windows, I LOVE LOVE LOVE TortoiseSVN,
   which integrates with Windows Explorer and the context menu. Really
   clean and easy to use.

