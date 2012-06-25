Odd Problems with subprocess.py
###############################

:author: C\. Titus Brown
:tags: python,programming,testing
:date: 2007-02-09
:slug: problems-with-subprocess
:category: python


After a fantastic `presentation on subprocess
<http://www.socal-piggies.org/socalpiggies/FourteenthMeeting>`__ at
the SoCal Python Interest Group last June, I bought into it
completely.  That recently translated into making the twill unit tests
work properly on Windows (I switched from ``fork()`` to
``subprocess``) and also building some of the functional tests for
`Cartwheel <http://cartwheel.idyll.org/>`__.  For the Cartwheel tests,
I'm using it to do database setup and teardown by running the ``psql``
command in various ways.

I spent part of my food-poisoning convalescence yesterday getting the
Cartwheel functional tests running in a `buildbot
<http://buildbot.sf.net/>`__ buildslave, and I ran into the darndest
problem.  ``subprocess`` was causing the tests to hang, because the
stdout buffer was filling up and in turn causing ``psql`` output to
hang.  Any command that had only a little bit of output worked fine,
while any command that output more than a 1kb or two of text, failed.
If I sent stdout anywhere other than a pipe, it worked fine -- but
I needed the output!

After an hour or so, I gave up trying to figure out how to configure
``subprocess`` properly and simply wrote a function that converted the
stdout and stderr handles to non-blocking and then polled them
continuously for new data.  (Yes, I probably could use select, but it
was failing for reasons I didn't understand.)  Quite an ugly hack, but
I *do* need the output for consistency checking!

Anyway, my code is below, for those who like to nitpick.  It's ugly.

The really strange thing for me is that this hanging problem didn't
occur on my development machine; only my buildslave (a Linux VM box
running much the same software) had problems.  The meta-lesson here
is (once again) that continuous integration really does help you find
the darndest things, including mysterious configuration/environment
related problems that you never would have thought of looking for.

--titus

::

    def _poll_subprocess(cmd):
        # make stdout/stderr non-blocking
        stdout_fileno = cmd.stdout.fileno()
        stderr_fileno = cmd.stderr.fileno()

        flags = fcntl.fcntl(stdout_fileno, fcntl.F_GETFL)
        fcntl.fcntl(stdout_fileno, fcntl.F_SETFL, flags| os.O_NONBLOCK)

        flags = fcntl.fcntl(stderr_fileno, fcntl.F_GETFL)
        fcntl.fcntl(stderr_fileno, fcntl.F_SETFL, flags| os.O_NONBLOCK)

        # wait for the process to end, sucking in stuff until it does end
        stdout = stderr = ""
        while cmd.poll() is None:
            try:
                stdout += cmd.stdout.read()
            except IOError:
                pass

            try:
                stderr = cmd.stderr.read()
            except IOError:
                pass

        # get the last output
        try:
            stdout += cmd.stdout.read()
        except IOError:
            pass

        try:
            stderr += cmd.stderr.read()
        except IOError:
            pass

        return (stdout, stderr, cmd.poll())


----

**Legacy Comments**


Posted by Scott Lamb on 2007-02-09 at 15:52. 

::

   "A kilobyte" or two is PIPE_BUF bytes (4096 on my system). This is a
   classic deadlock situation - process A is blocking on adding bytes to
   the A-&gt;B pipe, but process B allow it to proceed (by consuming the
   bytes already there)  until process A does something else.    It's
   described in the Python documentation <a
   href="http://docs.python.org/dev/lib/popen2-flow-
   control.html">here</a>, though unfortunately in a spot most people
   won't see anymore since popen2 is obsoleted by subprocess.    Anyway,
   I think subprocess's "communicate" function does the same thing as
   your loop. Another option is to send stdout and stderr to a
   tempfile.TemporaryFile().


Posted by Micha Kwiatkowski on 2007-02-09 at 16:24. 

::

   I had the same problem with Cheesecake just a few days ago. I solved
   it by redirecting output to a temporary file, so it will be written
   there, not blocking the output producer process.    Changeset with fix
   for Cheesecake: <a href="http://pycheesecake.org/changeset/175">http:/
   /pycheesecake.org/changeset/175</a>


Posted by bear on 2007-02-09 at 18:36. 

::

   I ran into this issue last year when exploring subprocess myself.  I
   determined that if I tried to wait() on the process the buffer quickly
   filled up (especially since I was redirecting stderr to stdout to get
   the output intermixed.)    I solved it by letting subprocess handle
   the polling:    import subprocess  p = subprocess.Popen(['foo',
   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)    out =
   p.stdout.readlines()    p.wait()    with the above I no longer was
   getting "mystery" hangs.  This even caused me to do a rare blog post
   about it:    <a href="http://code-bear.com/bearlog/2006/03/02">http
   ://code-bear.com/bearlog/2006/03/02</a>


Posted by Titus Brown on 2007-02-09 at 20:18. 

::

   Doing the same thing with 'read()' instead of readlines() didn't work
   for me.  Maybe readlines does something different?


Posted by Scott Lamb on 2007-02-09 at 21:43. 

::

   read() vs. readlines() shouldn't matter. bear's code fragment works
   because stdout and stderr go to the same stream. If they were separate
   and it read from one, the subprocess could get blocked on the other.


Posted by Titus Brown on 2007-02-09 at 22:30. 

::

   Ahh, good tip.  I'll try that, then.    thanks,  --titus


Posted by Josiah Carlson on 2007-02-12 at 20:37. 

::

   Or you can use the async subprocess subclass available on the Python
   cookbook.  It supports both *nix and Windows.    <a href="http://aspn.
   activestate.com/ASPN/Cookbook/Python/Recipe/440554">http://aspn.active
   state.com/ASPN/Cookbook/Python/Recipe/440554</a>


Posted by Greg Wilson on 2007-02-13 at 16:21. 

::

   I spent several hours messing around with subprocess last summer,
   trying to find an easy way to explain it to people without strong
   backgrounds in CS (the intended audience for Software Carpentry).  I
   eventually gave up in frustration: there are just too many options and
   switches.


Posted by Titus Brown on 2007-03-24 at 12:29. 

::

   Scott, bear -- the 'communicate' function does exactly what I need.
   Thanks, Scott!    --titus


Posted by Noah Gift on 2007-06-14 at 08:23. 

::

   Is there anything subprocess did not take over from os?


Posted by Titus Brown on 2007-06-15 at 20:02. 

::

   from 'os.system'?  not much, as far as I can tell.  However, 'system'
   is apparently a POSIX standard so it's being left in.    --titus

