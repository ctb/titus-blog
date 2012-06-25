Patching subprocess revisited
#############################

:author: C\. Titus Brown
:tags: python
:date: 2007-06-05
:slug: subprocess-patch-revisited
:category: python


So, I've finally put together a patch for subprocess; see
`replacing-commands-with-subprocess <http://ivory.idyll.org/blog/mar-07/replacing-commands-with-subprocess>`__
for background, and `this python-dev thread
<http://www.gossamer-threads.com/lists/engine?post=553519;list=python>`__
for discussion.

You can go grab my patch (or the entire subprocess module) `here
<http://iorich.caltech.edu/~t/transfer/subprocess-patch-a.tar.gz>`__.
I'm interested in comments, either here or `via e-mail
<mailto:titus@idyll.org>`__.

Note that I am putting together a separate docs patch.

--titus

Here's the relevant part of the docstring for the updated module: ::

  get_status_output(cmd, input=None, cwd=None, env=None):
    Run command with arguments, redirecting stderr to stdout, returning stdout.

    stderr is redirected to stdout, and stdout is collected from the
    running process (via Popen.communicate). The exit status and all
    of the stdout output is returned. Example:

       (status, output) = get_status_output(["ls", "-l"])
      
    Note that the recorded stdout is kept in memory.

    The string value of the keyword argument 'input' is written to
    stdin, if given.

    Most of the keyword arguments accepted by Popen are accepted by
    get_status_output, excepting only 'universal_newlines', 'stdout',
    'stderr', and 'bufsize'.  However, unlike Popen, 'shell' defaults
    to True.
    
  get_status_output_errors(cmd, input=None, cwd=None, env=None):
    Run command with arguments, returning exit status, stdout, and stderr.

    Both stdout and stderr are collected from the running process (via
    Popen.communicate). The exit status and all of the stdout and stderr
    are returned in a tuple. Example:

       (status, output, error_output) = get_status_output_errors(["ls", "-l"])

    Note that the recorded stdout and stderr are kept in memory.
    
    The string value of the keyword argument 'input' is written to
    stdin, if given.

    Most of the keyword arguments accepted by Popen are accepted by
    get_status_output_errors, excepting only 'universal_newlines',
    'stdout', 'stderr', and 'bufsize'.  However, unlike Popen, 'shell'
    defaults to True.

  get_output(cmd, input=None, cwd=None, env=None):
    Run command with arguments and return stdout.

    Both stdout and stderr are collected separately from the running process
    (via Popen.communicate). The stderr is discarded and the stdout is
    returned. Example:

       output = get_output(["ls", "-l"])

    Note that the recorded stdout and stderr are kept in memory.

    If the keyword argument 'require_success' is True, this function requires
    that the resulting exit code is zero, or else CalledProcessError will be
    raised (see the check_call function). Example:

      try:
         output = get_output(cmd, require_success=True)
      except CalledProcessError:
         print 'command %s failed' % (cmd,)
        
    The string value of the keyword argument 'input' is written to
    stdin, if given.

    Most of the keyword arguments accepted by Popen are accepted by
    get_output, excepting only 'universal_newlines', 'stdout',
    'stderr', and 'bufsize'.  However, unlike Popen, 'shell' defaults
    to True.

  system(cmd, **kwargs):
    Run command inside a system shell. Return the exit status of the command.

    This function replaces os.system and has a more straightforward
    (platform-independent) return value.


----

**Legacy Comments**


Posted by Sebastian Rittau on 2007-06-07 at 05:57. 

::

   In general I welcome this consolidation of the standard library by
   moving related stuff into one module. Nevertheless I think the
   function names are hideous. get_XYZ implies a cheap, side-effect free
   function. Also the names don't reflect at all the function's main
   purpose, which is calling an external program, instead focusing on a
   detail (the return value). You should really go with the "call"
   convention already used by subprocess, e.g. "call_status_output".
   "system" is okayish as a name, but deeply rooted in Unix tradition.
   For someone not knowing the POSIX API this name has no meaning.
   ("System? Which system?") I would also suggest a different name that
   better reflects the purpose of the function (e.g. "call_shell").


Posted by Kumar McMillan on 2007-06-07 at 14:38. 

::

   @Sebastian: the names are dilliberately similar to older modules to
   allow for easy deprecation (see the dev thread for details)    @Titus:
   subprocess.system(), yes!  It is very confusing that os.system returns
   what's basically a useless value ;)  May I suggest that you update the
   docs for os.system (in case you haven't already) saying to use
   subprocess.system for a more consistent value.

