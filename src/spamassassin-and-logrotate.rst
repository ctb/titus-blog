Exim, spamassassin and logrotate
################################

:author: C\. Titus Brown
:tags: admin
:date: 2006-10-15
:slug: spamassassin-and-logrotate
:category: science


*Here's some pointlessly complex systems administration stuff.*

I spent an hour or two today debugging my spam filtering setup.  Most
of my e-mail goes through Caltech, which does spam tagging nicely, but
recently there's been a substantial increase in e-mail coming through
various hosted domains.  This bypasses Caltech's tagging, so I get
spam that comes that way.  I only noticed when I started getting 100 to
150 spam messages *a day*, which seemed like a poor false-negative
rate for spamassassin...

I'd set up my spamassassin+exim4 config according to
Martijn Anthonissen's excellent `Combining Exim4 with Spamassassin <http://www.win.tue.nl/~martijna/Debianstuff/>`__ page.  Unfortunately I pretty
quickly figured out that *none* of my e-mail was getting processed
by my setup -- so I finally took the time out to understand all of the
different configuration stuff on that page.

Irony of ironies, it turns out that my e-mail was getting delivered to
procmail in my .forward file *before* it was hitting the spam tagging
system; forward files are ranked at 500 or so in exim, as opposed to
the spam tagging system, which is ranked at 850.  I changed the number to
450 and everything started working!

I'm not sure what Martijn does, but it seems a bit odd that you'd have
a spam tagging system that only operated *after* forwardfiles; he must
use *something* to filter tagged spam out of his box...?

In the process I discovered that my exim4 logs were over 200mb in size,
and growing.  A bit of investigation showed that logrotate was installed
and configured to rotate the exim4 logs -- so why wasn't it happening?
It turns out (*boggle*) that logrotate dies silently if one of the log
files it's supposed to monitor doesn't exist.

Sigh.

--titus
