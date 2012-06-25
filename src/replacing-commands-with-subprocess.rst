Replacing ``commands`` with ``subprocess``
##########################################

:author: C\. Titus Brown
:tags: python,python-dev
:date: 2007-03-21
:slug: replacing-commands-with-subprocess
:category: misc


After an `innocent question was answered <http://www.gossamer-threads.com/lists/engine?post=553519;list=python>`__ positively, I am putting together a patch to deprecate the `commands module <http://docs.python.org/lib/module-commands.html>`__ in favor of a slightly expanded `subprocess module <http://docs.python.org/lib/module-subprocess.html>`__ (for 2.6).

Briefly, the idea is to add three new functions to subprocess: ::

  output = get_output(cmd, input=None, cwd=None, env=None):

  (status, output) = get_status_output(cmd, input=None, cwd=None, env=None)
  
  (status, output, errout) = get_status_output_errors(cmd, input=None, cwd=None, env=None)

with the goal of replacing ``commands.getstatusoutput`` and
``commands.getoutput``.  (``commands.getstatus`` has already been
removed from 2.6.)

This will provide a simple set of functions for some very common
subprocess use-cases, as well as providing for a cross-platform
alternative to commands, with better post-fork behavior and error
trapping, adhering to PEP 8coding standards.  A win-win-win, I hope
;).

In addition to writing the basic code & some tests, I would like to:

 * reorganize, correct, and expand the subprocess documentation: right
   now it's not as useful as it could be.

 * put some warnings/error reporting into subprocess for bad class
   parameters; e.g. ``Popen.communicate`` should check to be sure both
   subprocess.stdout and stderr are PIPEs.

Questions:

 * anything else I should think about doing to subprocess?

 * right now the functions take only the input, cwd, and env arguments
   to pass through to the Popen constructor.  Any other favorite
   arguments out there?

 * should language be added to the popen2 module pointing people at
   subprocess, and should popen2 be deprecated?

 * GvR suggested that I reimplement ``commands`` in terms of these
   ``subprocess`` functions for 2.6, even though the commands module
   could be deprecated in 2.6 and probably removed in 2.7.  I would
   rather simply amend the documentation to point people at subprocess.

Thoughts?

--titus

p.s. The implementation of the above functions is dead simple: ::

  def get_status_output(cmd, input=None, cwd=None, env=None):
      pipe = Popen(cmd, shell=True, cwd=cwd, env=env, stdout=PIPE, stderr=STDOUT)

      (output, errout) = pipe.communicate(input=input)
      assert not errout

      status = pipe.returncode
  
      return (status, output)
  
  def get_status_output_errors(cmd, input=None, cwd=None, env=None):
      pipe = Popen(cmd, shell=True, cwd=cwd, env=env, stdout=PIPE, stderr=PIPE)
  
      (output, errout) = pipe.communicate(input=input)
  
      status = pipe.returncode
  
      return (status, output, errout)
  
  def get_output(cmd, input=None, cwd=None, env=None):
      return get_status_output()[1]


----

**Legacy Comments**


Posted by Drew Perttula on 2007-03-21 at 18:40. 

::

   Do none of the proposals involve raising an exception when a command
   returns nonzero exit status? Returning status codes is so unpythonic
   (for the common case where commands use nonzero status to mean
   failure).     I'd like it if get_output raised an exception for
   nonzero status. All the output **and** the particular nonzero status
   should be attributes on the exception object. get_status_output is now
   less relevant, but maybe it could stick around as the non-exception-
   raising version, the one you use if your command returns various
   success results through the exit status.    Optionally, get_output
   could have an extra arg success_status=0 which you use if you actually
   want a different status.


Posted by Scott Tsai on 2007-03-21 at 19:15. 

::

   I think you mean to do pipe.wait() instead of just reading
   pipe.returncode.    How about allowing subprocess.Popen's other
   keyword arguments to passed down from get_status_X ?


Posted by Titus Brown on 2007-03-21 at 19:31. 

::

   Drew, the idea is to replace commands.* with functions that do
   substantially the same thing, only  "better".  Given that
   returncode==0 on success is only a convention, and not a requirement,
   I don't know if raising an exception is the right thing to do.
   Scott, no, what I wrote works fine ;).  communicate() automatically
   does a wait().    As for passing through other keyword args, I'd have
   to filter them to make sure they made sense.  In particular, stdout,
   stderr, and bufsize don't make sense in this context; preexec_fn and
   close_fds are UNIX specific; and creationflags and startupinfo are
   Windows specific.  That leaves only universal newlines, which isn't
   relevant if you're gathering all the output at once and returning it
   as a string.    So I could allow all **but** universal_newlines,
   stdout, stderr, and bufsize to be passed through, but that complicates
   the function signatures.  hmm.  Not sure what to think about that.
   --titus


Posted by Scott Tsai on 2007-03-21 at 19:52. 

::

   Titus, thanks for the explaination.    Still thik the platform
   specific features like using preexec_fn to set resource limits is
   reall useful though.    "Raise an exception if return code is non
   zero"  is also something I use almost daily.  This is useful when
   integrating python into an existing build system. Stopping on the
   first non zero return code matches the convention of the unix 'make'
   utility.    I write a lot of test code for embedded device drivers and
   circuit board hardware that executes  external commands.    I have a
   function 'run_cmd' that is just subprocess.call but raises exception
   objects with 'return_code' attributes on error.


Posted by Titus Brown on 2007-03-21 at 20:01. 

::

   Scott,    OK, you've convinced me on the keyword args.  I'll write up
   the functions that way and see if python-dev brutally rejects them.
   I understand you on the exception-raising behavior, but that would
   have to be a new function that acts in a style different from the
   functions already in the module.  I can virtually guarantee that
   getting that past anyone will be tough ;).    --titus


Posted by Kimutaku on 2007-03-21 at 21:31. 

::

   I don't get it. Subprocess has a generic api so it can do (almost)
   anything that can be done with commands, os.system, os.popen*,
   os.spanw*(???), etc. One problem is that the subprocess docs aren't so
   nice. Another is that doing a simple process task seems to be a little
   verbose.    So, for consistency, I would have expected just a bit more
   of documentation, just saying how you could do 'commands' tasks with
   subprocess (i.e., add another subsection to 17.1.3)    If you're going
   to add some utilities, maybe it'd be better to make a submodule called
   'utils', 'shortcuts' or whatever, so you could put functions that can
   resemble the 17.1.3 section from the docs:    from subprocess.shorcuts
   import get_status_output  from subprocess.shorcuts import system  ...
   Ok, maybe a sub-namespace is overkiller but I think the key here is
   that there's some "utilities" living on the docs (section 17.1.3) and
   now there would be others explicitly coded. That's inconsistent from
   my POV.      About deprecating popen2. Absolutely. Indeed pep 3108
   propose just that.    ***Thank you*** for working on this. It would be
   nice if another python guru could make something similar for  the
   httplib/httplib2(??)/urllib/urllib2/urlparse/whatever issue, for the
   mac-related modules, etc... Step by step, cleaning up the mess :)


Posted by Titus Brown on 2007-03-22 at 00:51. 

::

   Kimutaku,    I think it's really valuable to implement very common
   use-cases.  That's the main point -- not to reimplement stuff per se,
   but rather to encode in a few simple functions what 95% of people
   using subprocess need to do.    In this particular case, we want to
   keep functions around that people use, but put them in a better place
   and implement them more nicely.  The real reason to keep those
   functions, though, is not because they're already there, but because
   they're **used** a lot.    --titus


Posted by Nathan LeZotte on 2007-03-22 at 01:01. 

::

   Just a few of things:    1.  I just noticed (after following the link
   to the subprocess documentation above), that a check_call function
   seems to have been added to the subprocess module in Python 2.5.  It
   looks like it's exactly the same as the subprocess.call function
   except that it has the exception raising behavior discussed above.
   2.  Is the unverisal newlines argument really irrelevant for these
   functions?  My impression was that it would determine whether you got
   just '\n' characters for newlines in the resulting output string or
   something else (like '\r\n' on Windows).    Some quick testing shows
   this to be the case (at least on Windows XP with Python 2.5).    3.
   Any thoughts on adding some asynchronous output getting functions to
   the mix?  Perhaps with an iterator interface like the following:
   for line in get_output_line_iter(['ls', '-l']):    print
   process_line(line)    I can see two use cases for this functionality:
   1.  You have a subprocess that produces a lot of output (more than you
   want to keep in memory at the same time).      2.  You have a long
   running subprocess and you want to process its output before it's
   finished (e.g. in realtime).


Posted by Mark Eichin on 2007-03-22 at 01:25. 

::

   0 == success may be a convention, but it's a strong posix one.  I
   would convert basically all of my commands.getstatusoutput calls to an
   exception throwing near-alternative; most of them are already followed
   by "assert st == 0" or the equivalent anyway... it would preserve the
   readability advantages that commands has over subprocess now, while
   having the more pythonic "anything goes unexpected/wrong and you get a
   traceback" reliability that makes constructs like    for line in
   file(...):    cleaner and safer than their perl or C equivalents...


Posted by Drew Perttula on 2007-03-22 at 13:25. 

::

   Another variation to my proposal:      def get_output(cmd, input=None,
   cwd=None, env=None, success=None)    That would be backwards
   compatible, but if I supply success=0, then it raises an exception if
   the return status is not zero. And it sounds like some of us would be
   using success=0 a whole lot.    Writing these 3-line versions of a
   function call is so ridiculously unpythonic:      (status, output) =
   get_status_output("tool")    if status != 0:    raise ValueError("tool
   failed")    and wrapping that in a library function (like many of us
   do) seems somewhat batteries-not-included.


Posted by Titus Brown on 2007-03-22 at 16:16. 

::

   Hmm, maybe I'll propose a "require_success" bool parameter on all
   these functions.  By default it'll be False.    However, if
   get_output(..., require_success=True) is called and the returncode is
   not zero, a CalledProcessError will be raised.    --titus


Posted by Titus Brown on 2007-03-22 at 16:23. 

::

   Nathan, I'll check on the universal newlines bit.  My impression was
   that it changed behavior only if you were reading line-by-line from
   Popen.stdout/Popen.stderr.    Re asynch, my impression is that Popen
   does a fine job of this already with stdout=PIPE.  Am I wrong?


Posted by Titus Brown on 2007-03-22 at 16:24. 

::

   (sorry if I ignored something, I'm finding it difficult to take into
   account all the suggestions; so e-mail me if I forgot to answer
   something!  And thanks for all the suggestions!)    titus@idyll.org


Posted by Titus Brown on 2007-03-22 at 16:40. 

::

   See    <a href="http://mail.python.org/pipermail/python-
   dev/2007-March/072278.html">http://mail.python.org/pipermail/python-
   dev/2007-March/072278.html</a>


Posted by Nathan LeZotte on 2007-03-23 at 00:38. 

::

   Titus,    You may be right about the asynchronous stuff.  In the past,
   I've written some semi-complicated Win32 API code (using the win32all
   modules) in order to handle subprocess output asynchronously.
   However, it's entirely possible that I just overlooked the obvious
   solution:      for line in popen_obj.stdout:    process_line(line)
   I'll have to play around with this a bit to see if it doesn't work the
   way I want it to.


Posted by Kumar McMillan on 2007-03-30 at 11:12. 

::

   @Nathan: what you want for realtime iteration is:    while 1:    line
   = popen_obj.stdout.readline()    if not line:    # becomes None on EOF
   break    process_line(line)    @Titus:    how about a function
   cmdline2list() to complement subprocess.list2cmdline() ??      I found
   that I had to implement this for a test recently when I was trying to
   simulate the way python (gnu readline?) turns a command line into a
   list (the creation of sys.argv).  Is there already a function for this
   somewhere?  There are some funny rules, like --query="title='Foo'"
   becomes ['--query=title=\'Foo\''] and optparse is unhappy unless it
   gets exactly that!    hey, thanks for working on this module.  I think
   it has been one of the most useful additions to stdlib but of course
   could still use some work.  I agree with above that urllib2 and
   urlparse desperately need some work as well.


Posted by John Reese on 2007-04-22 at 17:38. 

::

   Titus:  commands.mkarg is occasionally useful in code building up
   large command-lines.  Do you plan to move that to subprocess as well?
   subprocess.list2cmdline is similar but Windows-specific.      Kumar:
   &gt; the way python (gnu readline?) turns a  &gt; command line into a
   list  It's neither Python nor readline but the shell that's
   responsible for that.  You can simulate it with shlex.split.
   &gt;&gt;&gt; shlex.split('--query="title=\'Foo\'"')  ["--
   query=title='Foo'"]


Posted by Richard Philips on 2007-06-06 at 07:35. 

::

   Thanks for your work on an already excellent subprocess module.    One
   of the thing I would like to see in subprocess.py is fail proof stdin,
   stdout, stderr redirection.


Posted by Titus Brown on 2007-06-06 at 11:40. 

::

   Richard, those are already in there...    --titus

