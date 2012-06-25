GTK/GNOME / Python testing tools
################################

:author: C\. Titus Brown
:tags: python,testing,gtk
:date: 2007-10-31
:slug: gnome-testing-query
:category: python


I am in need of some test automation tools for a GTK/GNOME GUI, and
after scanning the `Python Testing Tools Taxonomy <http://pycheesecake.org/wiki/PythonTestingToolsTaxonomy>`__ and doing a bit of investigating, it looks
like there are three possibilites.

`dogtail <http://people.redhat.com/zcerza/dogtail/>`__ and the `Linux
Desktop Testing Project <http://ldtp.freedesktop.org/wiki/>`__ both
use accessibility libraries to drive GNOME applications.  I found two
comparisons `here
<http://blog.chinaunix.net/u/12325/showart_177884.html>`__ and `here
<http://lists.freedesktop.org/archives/ldtp-dev/2006-October/000484.html>`__.
It seems like dogtail is more me-friendly (better Python interface, less
XML) and LDTP is more mature and up-to-date.

A third option is `Xnee <http://savannah.gnu.org/projects/xnee/>`__, which
is a generic (and non-Python) X-Windows event recorder and playback system.
There's a brief mention of it "in the wild" `here <http://squeedlyspooch.com/blog/2006/10/05/ui-test-automation/>`__.

I would be interested in any personal knowledge people have of these
projects.  None of them seem to be that widely used or mentioned,
based solely on Google juice, so anything you can tell me would help.
Right now I'm thinking that I will have to just try each of them out
to see which one fits my needs best... <sigh>

--titus


----

**Legacy Comments**


Posted by Ali Afshar on 2007-10-31 at 19:48. 

::

   Hi Titus, good luck searching for what has become for me the Holy
   Grail of Gui programming.    If you are doing PyGTK, I can recommend
   the (prototype) test recorder/player in Kiwi (also listed on the
   Taxonomy) <a href="http://www.async.com.br/projects/kiwi/">http://www.
   async.com.br/projects/kiwi/</a>. It records your events as a Python
   script that looks very much like a doctest.    Unfortunately it is
   still incomplete, and I am not sure the author (Johan Dahlin) has a
   keen interest in developing it further.    Here is a little example I
   just recorded. The application opened a login dialog, and I am just
   entering the login username "admin":    ... -*- Mode: doctest -*-  ...
   run: pharma.py  &gt;&gt;&gt; from kiwi.ui.test.runner import runner
   &gt;&gt;&gt; runner.start()  &gt;&gt;&gt; runner.sleep(6.7)
   &gt;&gt;&gt; GtkDialog = runner.waitopen("GtkDialog")  &gt;&gt;&gt;
   GtkDialog.GtkEntry.set_text("a")  &gt;&gt;&gt;
   GtkDialog.GtkEntry.set_text("ad")  &gt;&gt;&gt; runner.sleep(0.1)
   &gt;&gt;&gt; GtkDialog.GtkEntry.set_text("adm")  &gt;&gt;&gt;
   runner.sleep(0.1)    You can play the script back then, including
   assertions where required.    On a different note, I use this approach
   to synchronise PyGTK in order to test it properly:    <a
   href="http://unpythonic.blogspot.com/2007/03/unit-testing-
   pygtk.html">http://unpythonic.blogspot.com/2007/03/unit-testing-
   pygtk.html</a>    Ali


Posted by Noah Gift on 2007-11-01 at 19:26. 

::

   Titus,    I just started looking at all three of these as well.  If
   you are testing GTK 1 applications too, as GTK 2 is when user
   accessibility stuff was added, then you are limited to Xnee.  I
   started to use Xnee and it is quite interesting, but one limitation I
   ran into was, how do you assert if a condition has not been met?    If
   you start doing more with Xnee, and find some ways to make Xnee a test
   harness, I would be very interested.  Xnee does have quite a bit of
   raw potential.

