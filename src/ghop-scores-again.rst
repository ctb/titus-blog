Google Highly Open Participaton Contest -- another notch in the source code!
############################################################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2008-04-09
:slug: ghop-scores-again
:category: python


Pavel Vinogradov <fastnix> has been keeping me updated on an issue he
discovered while testing `TCMalloc
<http://goog-perftools.sourceforge.net/doc/tcmalloc.html>`__ with
Python as a Google Highly Open Participation (GHOP) task, `task 105
<http://code.google.com/p/google-highly-open-participation-psf/issues/detail?id=105>`__.

Briefly, Pavel discovered a situation in which replacing the Python
memory allocator with TCMalloc resulted in really bad performance.
The latest is that there appears to be a bug or gotcha in TCMalloc
with glibc, where TCMalloc does a poor job in cases where mremap can
be used by glibc.  The TCMalloc folk are going to look into it more, I
gather.  (See google-perftools thread `here <http://groups.google.com/group/google-perftools/browse_thread/thread/4cc0f545c25caecc>`__.)

Anyway, this was a situation where we just threw the task at the
students to see if anything interesting would pop out -- not expecting
much of anything other than a learning experience for the student --
and yet through some simple-yet-dogged testing, Pavel really
contributed something.

Awesome stuff!

There have been several real success stories to GHOP.  I need to write them
down, sigh... my kingdom for some time :)

--titus
