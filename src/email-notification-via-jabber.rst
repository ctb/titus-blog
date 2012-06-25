E-mail notification via Jabber/iChat
####################################

:author: C\. Titus Brown
:tags: python
:date: 2006-10-26
:slug: email-notification-via-jabber
:category: python

A simple program to get pinged whenever you get new e-mail: ::

   #! /usr/bin/env python
   import sys, email
   from pyxmpp.jid import JID
   from pyxmpp.jabber.simple import send_message

   inp = sys.stdin.read()
   message = email.message_from_string(inp)

   jid = 'someid@xmpp.us'
   password, recpt = 'XXXXX', 'otherid@xmpp.us'

   jid = JID(jid)
   if not jid.resource:
       jid = JID(jid.node,jid.domain,"send_message")

   recpt = JID(recpt)

   s = "From: %s\nSubject: %s" % (message['From'], message['Subject'])

   send_message(jid, password, recpt, s, "")

Just pipe each new e-mail message into this, and voila!

I'd like to write something like for buildbot, so that a failing build notifies
you.  Should be pretty easy.

And, of course, PyXMPP is cool.

--titus


----

**Legacy Comments**


Posted by Grig Gheorghiu on 2006-10-26 at 20:35. 

::

   Cool stuff! Buildbot already has an IRC notifier, but a Jabber one
   would be a welcome addition I'm sure. Send a patch to the buildbot-
   devel list!


Posted by Mark Eichin on 2006-10-27 at 20:05. 

::

   Once we added a simple shell "send jabber message to user|group"
   commandline tool (using python-xmpp which isn't quite this elegant,
   though it does work with gssapi/kerberos) people started dropping
   notifications into lots of things.  (just like we learned with
   zwrite/Zephyr at MIT in the early 90's :-)  "New release candidate
   available" or even "pre-installed testing machine ready to ssh into"
   messages are great for letting people not **wait** for resources to be
   available, since they can have the resource interrupt them.  Good for
   productivity though sometimes a little surprising when you get a
   message from **yourself** saying something is ready :-)


Posted by John on 2006-11-02 at 22:24. 

::

   Very cool script.    It works great with most Jabber servers (e.g.
   jabber.org), but for some reason I'm having trouble getting it to work
   with Google Talk. Any tips?


Posted by Titus Brown on 2006-11-03 at 12:03. 

::

   Sorry, no ideas... does iChat work with Google Talk?


Posted by Titus Brown on 2006-11-20 at 13:13. 

::

   Here's a patch to make PyXMPP work with Google Talk:    <a href="http:
   //www.stillhq.com/google/gtalk/000001.html">http://www.stillhq.com/goo
   gle/gtalk/000001.html</a>

