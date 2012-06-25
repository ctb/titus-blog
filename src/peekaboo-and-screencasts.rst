peekaboo and associated screencasts
###################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2008-03-26
:slug: peekaboo-and-screencasts
:category: python


The simple application I demoed at PyCon '08 during my talk on the OLPC and
testing is now available: I call it "peekaboo".

peekaboo is a way to watch your code being executed in another process
using sys.settrace, figleaf, and XML-RPC.

The two screencasts below should explain it.

The first screencast, `peekaboo-screencast.mp4
<http://idyll.dreamhosters.com/transfer/peekaboo-screencast.mp4>`__ ,
is a simple demo of peekaboo running on a really simple demo app.  To
try it out yourself, take the peekaboo code and run 'peek_view.py'
and 'demo_app.py', in that order; then visit 'localhost:8080' (for the
viewer) and 'localhost:8081' (for the demo app).  Click around.  Watch
stuff happen.  Whee.

The second screencast, `peekaboo-olpc-gui-driving.mp4
<http://idyll.dreamhosters.com/transfer/peekaboo-olpc-gui-driving.mp4>`__,
is a demo of using peekaboo to watch code execute in the One Laptop
Per Child GUI, Sugar.  In this screencast I use twill and xmacro to
drive the OLPC GUI and then retrieve trace information to the peekaboo
viewer.  The OLPC GUI driving code isn't "released" but then again
it's trivial.  Ask me if you want to see it before I get a chance to
polish it up a bit.

Ultimately I'd like to use peekaboo to host "exploratory test" parties
for the OLPC, where we all run through a bunch of activities and try
to get every last line of code covered by our exploratory tests.
Well, that, and I'd like to get a bunch of automated testing into the
OLPC GUI!

Anyway, peekaboo is basically a really simple mashup of figleaf and a
Web viewer, and it's not anything special in terms of code; the
trickiest bit was getting the XML-RPC server to run inside of Sugar
;).

You can go download the `peekaboo source
<http://darcs.idyll.org/~t/projects/peekaboo-latest.tar.gz>`__ if you
like.

Note that peekaboo is in no way, shape or form ready to be released, but
I just don't have time to work on it at the moment so I'm pushing it out
the door for those who are interested in seeing the raw, ugly code!

Comments welcome, of course!

--titus

p.s. Apologies for the heavy breathing in the second screencast;
peekaboo gets me excited!

p.p.s. No, seriously, it's late at night here and I just want to go home... so I don't want to redo the screencast!
