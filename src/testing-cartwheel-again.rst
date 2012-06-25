Testing Cartwheel, and How Testing Improves Code
################################################

:author: C\. Titus Brown
:tags: python,testing,programming
:date: 2007-01-16
:slug: testing-cartwheel-again
:category: python


Over the last few days, I put a bunch of time into my ongoing refit of
`Cartwheel <http://cartwheel.idyll.org/>`__.

Cartwheel is a sizeable
toolkit for doing bioinformatic sequence analysis; it's got a Web interface,
a batching and queuing system built on PostgreSQL, and a client library
for manipulating things over XML-RPC.  So, it's got a lot of moving
parts, which means that testing it is important, but it's also hard.

(I wrote earlier about how `automated testing is hard
<http://ivory.idyll.org/blog/nov-06/testing-is-hard.html>`__, even
when you wrote all of the software involved, and I also wrote a bit
about how to enable `in-process testing of XML-RPC
<http://ivory.idyll.org/blog/nov-06/making-in-process-xmlrpc-calls.html>`__.)

Cartwheel is actually one of the main motivating factors behind `twill
<http://twill.idyll.org/>`__, my framework for functional Web testing.
I noticed that over the years, Cartwheel had gotten more and more
brittle: as I'd add features, old ones would break or give me trouble.
PBP kept popping up on my radar, and finally I took the time to go try
it out & eventually rewrote it into twill.

So anyway, I've been adding to the functional tests for the Cartwheel
Web and XML-RPC interfaces (what would that be, the HTTP-level stuff?
yeah, that), and I ran into a whole slew of problems connected to
releasing the database handles.  It turns out that even though I had
some finalization code for the database interface, it wasn't enough,
and even the stuff that was there didn't work.  Since the finalization
code was never actually run in deployment -- Linux was actually doing
the cleanup when the process died, of course -- I hadn't understood
just how badly I'd written things.  Database connections weren't
getting closed, and this caused various operations to hang because I
was trying to drop tables while connections were open.

Several hours of head-scratching, code examination, and 'print' statements
later, I now have a large set of tests for both HTTP-level interfaces, and
I'm much more confident that my cleanup routines are working.  Moreover,
I understand the consequences of my original architecture decisions much
better.

This brings me to the meta-lesson: before this experience, I knew that
good finalization routines were important because having them improved
the usability of the code and also having them was simply the Right
Way to program.  Since I never *actually* had to re-use this code in
other contexts, this was largely a theoretical consideration.
However, once I had to do setup and teardown for my functional tests,
which effectively meant I *was* reusing the code, I ran smack into the
wall of reality: yes, it *is* important, and if I'd been smart enough
to write things properly Back When my last two days would have been
much more pleasant.

Next up: CMake, KWWidgets, and the Kitware experience.

--titus
