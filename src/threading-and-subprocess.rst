Threading and subprocess
########################

:author: C\. Titus Brown
:tags: python
:date: 2008-04-19
:slug: threading-and-subprocess
:category: python


I'm having a long-running discussion with some people about threading
and why using threads with simple subprocess calls is almost certainly an
overcomplicated (== BAD) use of threads.  Everyone seems to think I'm
wrong (at least, there's either deafening silence or straight out argument ;)
and I think I finally figured out why.

The task at hand: use subprocess to run some command (say, 'ping') a
bunch of times.  Because the command is I/O bound, you want to run the
commands in parallel.  Should you use threads to do this?  Is it necessary
in order to achieve good performance?

Well, consider these two examples ('common.py' is down at the bottom;
it just contains the list of IP addresses to ping, and a function to
call subprocess.Popen).

nothread.py: ::

  from common import IP_LIST, do_ping
  
  z = []
  for i in range(0, len(IP_LIST)):
     p = do_ping(IP_LIST[i])
     z.append(p)
  
  for p in z:
     p.wait()

thread.py: ::

  import threading
  from common import IP_LIST, do_ping
  
  def run_do_ping(addr):
     p = do_ping(addr)
     p.wait()
  
  ###
  
  # start all threads
  z = []
  for i in range(0, len(IP_LIST)):
     t = threading.Thread(target=run_do_ping, args=(IP_LIST[i],))
     t.start()
     z.append(t)
  
  # wait for all threads to finish
  for t in z:
     t.join() 

Both of these work fine, and in both cases are easily modifiable to
retrieve the output, exit status, etc. of the ping command.  (In the
threaded example you have to keep track of 'p' in 'run_do_ping' to
retrieve this kind of info, and I wanted to keep things as simple as
possible.)

They also run in about the same amount of time, although the non-threaded
one is quicker by a few milliseconds for me.  I think this is because
thread starts & joins are extra overhead.

The key misunderstanding in the discussion seems to have been that the
examples at hand were using subprocess.call, which **blocks**
waiting for the subprocess to exit, i.e. equivalent to
using this code in nothread.py: ::

  for i in range(0, len(IP_LIST)):
     p = do_ping(IP_LIST[i])
     p.wait()

Here the pings would execute serially rather than in parallel, with
the obvious performance problem :).  However, you can bypass this
effect of subprocess.call by using subprocess.Popen, which creates a
new process that executes in parallel with the calling process.

So, for this simple use of subprocess -- running a shell command and
gathering the output -- which is "better"?  I think 'nothread.py' is
better because it is simpler, shorter, clearer, and less complicated.
Of course, as soon as you start doing more complicated stuff like
reading the streams of information coming out of the subprocess
commands, the threaded version may well have its advantages.  But
that's not the case here, I think.

Comments welcome.

--titus

common.py: ::

  import subprocess

  IP_LIST = [ '131.215.17.3',
              '131.215.17.4',
              '131.215.17.5',
              '131.215.17.16',
              '131.215.17.17',
              '131.215.17.18',
              '131.215.17.19',
              '131.215.17.24',
              '131.215.17.25',
              '131.215.17.31']
  
  cmd_stub = 'ping -c 5 %s'
  
  def do_ping(addr):
      cmd = cmd_stub % (addr,)
      return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)


----

**Legacy Comments**


Posted by Shannon -jj Behrens on 2008-04-19 at 04:31. 

::

   A few comments:    * I don't like threads either.  I'm more a fan of
   Stackless and Erlang.  Sure, anytime you can get away with being
   linear, **of course** it's better.  Sometimes you can't.    * You are
   correct, if all you have to do is popen something and then ignore the
   output, there's not much point in using threads.  It makes a lot more
   sense to use threads if you have to **talk** to multiple external
   programs in parallel.  If you have to talk to multiple sockets in
   parallel, linear programming just won't cut it.  You have to use
   threads or asynchronous programming.    * I updated your code:    I
   switched popen to call.    I set:    IP_LIST = [ 'google.com',
   'yahoo.com',    'yelp.com',    'amazon.com',    'freebase.com',
   'clearink.com',    'ironport.com' ]    cmd_stub = 'ping -c 5 %s'    I
   got rid of the wait() because it's not needed with call.    I updated
   the code to print whether the ping succeeded or failed.    python
   thread.py  0.05s user 0.08s system 0% cpu 15.082 total    python
   nothread.py  0.04s user 0.08s system 0% cpu 39.509 total    By the
   way, I ran the commands multiple times to make sure DNS was cached.
   This is the output I was expecting.


Posted by Titus Brown on 2008-04-19 at 05:08. 

::

   You can't use subprocess.call; it blocks.


Posted by Shannon -jj Behrens on 2008-04-19 at 05:30. 

::

   Oh, I get it!  Ugh, that was hard.    It reminds me of the time my
   boss told me he wanted to use UTF-8 (strings) but not Unicode
   (objects).  It took me a while to figure out  what he meant and why he
   was right for that situation.  Long story.    Anyway, I agree with you
   Titus for the case of ping.    Titus's approach is to launch a bunch
   of external programs in parallel, and then wait for them all.  Once
   you do the wait, you can figure out if each succeeded or not.  No
   threading is required.  Yes,  I agree that that is much cleaner.
   What I was trying to say was that if you have a bunch of **long
   running** processes or sockets that you need to have **conversations**
   with, you're stuck using either threads or asynchronous programming.
   Titus, do you agree with this point?    For the case of ping, Titus is
   right.  Titus, sorry that took me so long.  I warned you that my brain
   wasn't up to full speed yet ;)


Posted by Glyph Lefkowitz on 2008-04-19 at 06:07. 

::

   You don't need threads to run subprocesses in parallel.    <a href="ht
   tp://twistedmatrix.com/documents/current/api/twisted.internet.interfac
   es.IReactorProcess.html#spawnProcess">http://twistedmatrix.com/documen
   ts/current/api/twisted.internet.interfaces.IReactorProcess.html#spawnP
   rocess</a>


Posted by Titus Brown on 2008-04-19 at 06:13. 

::

   To clarify, see this code:    from common import IP_LIST, do_ping    z
   = []  for i in range(0, len(IP_LIST)):    p = do_ping(IP_LIST[i])
   z.append(p)    for p in z:    p.wait()    for (ip, p) in zip(IP_LIST,
   z):    if p.returncode != 0:    print '%s is not alive' % (ip,)


Posted by Jeremy M. Jones on 2008-04-19 at 07:06. 

::

   OK - so here I am breaking the deafening silence.    It seems like in
   this case, using the nonthreaded version is "better".  You really just
   want to see if each site responded to `ping`.  And `ping` doesn't
   require any additional interaction.  I've modified common.py to this:
   import subprocess  import time    IP_LIST = [ 'google.com',
   'yahoo.com',    'yelp.com',    'amazon.com',    'freebase.com',
   'clearink.com',    'ironport.com' ]    cmd_stub = 'ping -c 5 %s'
   def do_ping(addr):    print time.asctime(), "DOING PING FOR", addr
   cmd = cmd_stub % (addr,)    return subprocess.Popen(cmd, shell=True,
   stdout=subprocess.PIPE)    And nothread.py to this:    from common
   import IP_LIST, do_ping  import time    z = []  #for i in range(0,
   len(IP_LIST)):  for ip in IP_LIST:    p = do_ping(ip)    z.append((p,
   ip))    for p, ip in z:    print time.asctime(), "WAITING FOR", ip
   p.wait()    print time.asctime(), ip, "RETURNED", p.returncode    (BTW
   - why are you iterating over range(len(IP_LIST)) when you should be
   iterating over the IP_LIST? :-) )    And here's the output I get:
   jmjones@dinkgutsy:thread_discuss$ python nothread.py   Sat Apr 19
   06:45:43 2008 DOING PING FOR google.com  Sat Apr 19 06:45:43 2008
   DOING PING FOR yahoo.com  Sat Apr 19 06:45:43 2008 DOING PING FOR
   yelp.com  Sat Apr 19 06:45:43 2008 DOING PING FOR amazon.com  Sat Apr
   19 06:45:43 2008 DOING PING FOR freebase.com  Sat Apr 19 06:45:43 2008
   DOING PING FOR clearink.com  Sat Apr 19 06:45:43 2008 DOING PING FOR
   ironport.com  Sat Apr 19 06:45:43 2008 WAITING FOR google.com  Sat Apr
   19 06:45:47 2008 google.com RETURNED 0  Sat Apr 19 06:45:47 2008
   WAITING FOR yahoo.com  Sat Apr 19 06:45:47 2008 yahoo.com RETURNED 0
   Sat Apr 19 06:45:47 2008 WAITING FOR yelp.com  Sat Apr 19 06:45:47
   2008 yelp.com RETURNED 0  Sat Apr 19 06:45:47 2008 WAITING FOR
   amazon.com  Sat Apr 19 06:45:57 2008 amazon.com RETURNED 1  Sat Apr 19
   06:45:57 2008 WAITING FOR freebase.com  Sat Apr 19 06:45:57 2008
   freebase.com RETURNED 0  Sat Apr 19 06:45:57 2008 WAITING FOR
   clearink.com  Sat Apr 19 06:45:57 2008 clearink.com RETURNED 0  Sat
   Apr 19 06:45:57 2008 WAITING FOR ironport.com  Sat Apr 19 06:46:58
   2008 ironport.com RETURNED 0      If I wanted to get the same type of
   thing out of the threading example, it looks like I'd have to add a
   queue and pass it in to run_do_ping so we could get the return code
   back from by way of the queue.  I don't think we can get the return
   code back from what the thread `run`ned.    So, I think using the
   nonthreaded actually allowed us to get the information back more
   simply.  But on this one, I'd actually prefer to communicate directly
   with a Python library rather than subprocessing out to ping.  That
   feels clunky to me.  I'd prefer to find a ping Python library (don't
   think there's one in the stdlib) and in this case, either use threads
   or Twisted.    - jmj


Posted by Jeremy M. Jones on 2008-04-19 at 08:55. 

::

   Forgot to mention that I totally agree with what I assume to be your
   presupposition: the simplest thing that works is usually best.  I
   always (or at least almost always) try to only use the simplest thing
   that I can to get something working.  Then I add complexity from there
   as needed.  So, I think I'm in agreement with you in principle as well
   as in this particular situation.    - jmj


Posted by Jesse on 2008-04-19 at 09:13. 

::

   In this case, I agree: nothreads makes sense - however, I actually
   like threads :)    If you are not processing the output of the
   command, there's no reason to use threads in this case: you are paying
   the penalty of spawning those threads.    If you want to see the
   penalty - remove the do_ping code from your function (or make do_ping
   simply pass), this will show you the raw overhead of constructing the
   thread objects, starting and joining them.    In any case, you're
   right - it doesn't make a ton of sense to use threads, however I don't
   see the "additional complexity" of the threaded example - both have
   the same "build an object, put it in a list and wait" semantics - one
   is running concurrently, and the other linearly.    Question - are you
   running on a multi-core machine?


Posted by Floris Bruynooghe on 2008-04-19 at 10:59. 

::

   For this simple example there's no advantage of the threads.  But as
   said, if you want to read and write to it you do.  The .communicate()
   method does an implicit .wait() thus blocking every process.  And
   unless I have good reason I don't like to re-implement .communicate().


Posted by Titus Brown on 2008-04-19 at 12:43. 

::

   Jesse, the threaded case has more code and the code is just ... more
   complicated.  Consider that you have to know what join() does, as well
   as wait(), and you have to understand the need to **call** join.  You
   also need to use a class (if you plan to recover the return value) as
   in this example:    import threading  from common import IP_LIST,
   do_ping    class PingThread(threading.Thread):    def
   <em>_init_</em>(self, ip):    self.ip = ip
   threading.Thread.<em>_init_</em>(self)      def run(self):    self.p =
   do_ping(self.ip)    self.p.wait()    ###    # start all threads  z =
   []  for i in range(0, len(IP_LIST)):    t = PingThread(IP_LIST[i])
   t.start()    z.append(t)    # wait for all threads to finish  for t in
   z:    t.join()    if t.p.returncode != 0:    print '%s is not alive!'
   % (t.ip,)    Floris, you're right about communicate.  I tried to write
   a version to monitor multiple subprocesses, and it was hard.    Glyph,
   my example above runs subprocesses in parallel.  Why do I need
   twisted, again? :)    --titus


Posted by Justin on 2008-04-19 at 13:02. 

::

   Sort of a bad example, if you want to ping a lot of hosts from python,
   use fping or nmap.    If you want to use threading, google for
   'iterthreader' then you can just do    for ip, result in
   iterthreader.Threader(do_ping, IP_LIST, numthreads=8):    print ip,
   result


Posted by Titus Brown on 2008-04-19 at 13:55. 

::

   Oooh, one more note -- if your command is going to produce lots of
   output, you will have to worry about the command blocking when it hits
   the buffer size of the subprocess stdout pipe.


Posted by Jeremy M. Jones on 2008-04-19 at 16:00. 

::

   Titus,    Good to note on your last point about processes blocking
   when they hit the stdout pipe buffer size.  I wonder, though, if that
   might be an argument **for** using Twisted.  Here's a chunk from the
   link Glyph sent:    """  If it is the string 'r', a pipe will be
   created and attached to the child at that file descriptor: the child
   will be able to write to that file descriptor and the parent will
   receive read notification via the IProcessProtocol.childDataReceived
   callback. This is useful for the child's stdout and stderr.  """    I
   wonder if Twisted just automatically handles that for you by feeding
   stdout data to a callback (that unless overridden goes nowhere).  (I
   don't know that it does that - it just seems a Twistedish thing to do
   and seemed to match the docs.)      But using non-Twisted, you should
   be able to send that output to /dev/null or somewhere.  Unless you
   want to read it for something.  In which case, you probably want the
   process to block, anyway.  But definitely good to keep in mind.


Posted by Chad on 2008-04-19 at 19:57. 

::

   I'm missing the point of the post overall, but I couldn't let this
   slide:      z = []  for i in range(0, len(IP_LIST)):  ....p =
   do_ping(IP_LIST[i])  ....z.append(p)      **hork**  What the hell is
   that?  Are you a C programmer in secret?      The Pythonic way of
   writing that is      z = []  for address in IP_LIST:
   ....z.append(do_ping(address))      or just      z = [do_ping(a) for a
   in IP_LIST]


Posted by Titus Brown on 2008-04-19 at 22:36. 

::

   Now that's just mean... the code evolved over time from something much
   uglier, so you were seeing historical contingency at work.    The
   point of the post overall was that several (many) people were claiming
   that the nothread.py solution couldn't work and that thread.py was a
   simple way of doing things.


Posted by Doug Hellmann on 2008-04-20 at 20:20. 

::

   Speaking of evolving code:    Part of the problem is the example
   you've been analyzing was simplified from a more complex program that
   did more than call ping.  It started out life as small part of a
   pipeline where IP addresses were fed in one end and detailed server
   configuration information (host, OS, all IP addresses, MAC addresses,
   storage space, etc.) came out the other end.  Some operations were
   parallelized (i.e., trying to ping several hosts at once), but we
   didn't want to automatically spawn a separate process for **every** IP
   address because there could be hundreds and that would flood the
   network.  Each stage in the pipeline had a limited number of workers,
   based on the overhead involved in doing the particular task assigned
   to that stage.    So there was a worker pool reading IPs from a queue,
   doing a bunch of operations (some involving processes, some not), and
   then sticking the results in another queue for the next stage of the
   process.  The ping worker was implemented last, after we already had
   some other worker thread code in place that was doing far more
   complicated interaction with a sub-process to do SNMP interrogation.
   In the face of all of the existing code, it was very simple to
   refactor what we had working and make it call ping instead of the
   other command it had been calling.  That left us with a consistent
   design for all of the worker threads, even though not every operation
   needed to be in its own thread.    That's all by way of explanation,
   rather than excusing the state of the simplified code as it is today.


Posted by rgz on 2008-04-21 at 12:51. 

::

   I'd change:    z = []  for i in range(0, len(IP_LIST)):    p =
   do_ping(IP_LIST[i])    z.append(p)     to:    z = map(do_list,
   IP_LIST)     I don't have that much experience with threads and
   subprocess but I can't help but notice there is a call to wait() in
   both versions. If I'm correct, in both instances wait() block until
   the subprocess/thread is done, because, it was running in parallel.
   So isn't this enough to conclude that using subprocess is a form of
   threading? Therefore this blog post can be resumed as "Running threads
   is better than running threads that run threads*" which is really easy
   to accept.     But I guess you get into this a lot and you had to rant
   about it.     * I is being aware of the difference between sub process
   and threads.


Posted by Titus Brown on 2008-04-21 at 14:24. 

::

   rgz -- subprocess uses fork (or the Windows equivalent) and starts a
   new **process**, so while it is muiltitasking it is not threading per
   se.    That's why when I saw people talking about using one preemptive
   multitasking mechanism to control and monitor anothre, I said WTF...


Posted by Robert Brewer on 2008-04-22 at 12:27. 

::

   It's multithreading with all threads named "MainThread". &gt;;)


Posted by Noah Gift on 2008-04-28 at 01:58. 

::

   I am finally commenting on this post because I was asleep, literally,
   for a few days from exhaustion.  I do agree with you Titus, using
   subprocess to fork a bunch of processes is much cleaner, then having
   threading fork a process for the heck of it.      On the other hand, I
   do like the threading/Queuing API quite a bit, and find it more
   natural the subprocess API in terms of  waiting for output of task.
   I also agree with Doug too, that sometimes it is a good idea to keep
   the same design pattern throughout a library even if it means part of
   the design isn't as inefficient as you would like.  For the original
   example this design was based on, it did make sense.  There is a good
   example of this in PEP 8, about camel case names.    I do have a few
   followup questions this post brought up:    1.  Are there any cases in
   which subprocess.Popen will block and threading, or say the processing
   module won't?    2.  Why even use the processing module if you can
   just iterate and fork a way with subprocess.Popen?  I personally like
   the processing module, but part of that is that it is modeled after
   the threading API.  Is there anything processing can do that
   subprocess can't?    3.  Why does the subprocess.call and
   subprocess.Popen API differ such that one blocks and one doesn't?  I
   also like this very simple API for subprocess.call:  ret =
   subprocess.call(cmd, shell=True)    4.  It seems like there really
   should be a standard library "pinger" that doesn't require root to
   run.    5.  This pattern of spawning system processes seems common
   enough that it would be nice if there was better support for it in the
   standard library.  Maybe this could a keyword argument passed to
   subprocess.call?  I guess I do like the processing modules idea.

