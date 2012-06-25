Trying out 'cram'
#################

:author: C\. Titus Brown
:tags: python,testing,pycon
:date: 2011-03-13
:slug: trying-out-cram
:category: python


I desperately need something to run and test things at the command
line, both for course documentation (think "doctest" but with shell
prompts) and for script testing (as part of scientific pipelines).  At
the 2011 testing-in-python BoF, Augie showed us `cram
<http://bitheap.org/cram/>`__, which is the mercurial project's
internal test code ripped out for the hoi polloi to use.

Step zero: wonder-twin-powers activate a new virtualenv! ::

 % virtualenv e
 % . e/bin/activate

Step one: install! ::

 % pip install cram

... that just works -- always a good sign!

OK, let's test the bejeezus out of 'ls'. ::

 % mkdir cramtest
 % cd cramtest

Next, I put ::

   $ ls

into a file.  Be careful -- you apparently need *exactly* two spaces before
the $ or it doesn't recognize it like a test.

Now, I run::

  % cram ls.t

and I get ::

  .
  # Ran 1 tests, 0 skipped, 0 failed.

Awesome!  A dot!

The only problem with this is that when I run 'ls' myself, I see::

  ls.t    ls.t~

Hmm.

As a test of the cram test software, let's modify the file 'ls.t' to contain a
clearly broken test, rather than an empty one::

  $ ls
  there is nothing here to see

and I get ::

  !
  --- /Users/t/dev/cramtest/ls.t
  +++ /Users/t/dev/cramtest/ls.t.err
  @@ -1,2 +1,1 @@
     $ ls
  -  there is nothing here to see
  
  # Ran 1 tests, 0 skipped, 1 failed.

OK, so I can make it break -- excellent!  Cram comes advertised with
the ability to fix its own tests by replacing broken output with
actual output; let's see what happens, shall we? ::

  % cram -i ls.t

  !
  --- /Users/t/dev/cramtest/ls.t
  +++ /Users/t/dev/cramtest/ls.t.err
  @@ -1,2 +1,1 @@
     $ ls
  -  there is nothing here to see
  Accept this change? [yN] y
  patching file /Users/t/dev/cramtest/ls.t
  Reversed (or previously applied) patch detected!  Assume -R? [n] y
  Hunk #1 succeeded at 1 with fuzz 1.
  
  # Ran 1 tests, 0 skipped, 1 failed.
  % more ls.t
  $ ls
  there is nothing here to see
  there is nothing here to see

OK, so, first, wtf is the whole reversed patch detected nonsense?  Sigh.
And second, where's the output from 'ls' going!?

Hmm, maybe cram is setting up a temp directory?  That would explain a lot,
and would also be a very sensible approach.  It's not mentioned explicitly
on the front page, but if you read into it a bit, it looks likely.  OK.

Let's modify 'ls.t' to create a file::

  $ touch testme
  $ ls

and run it... ::

  % cram ls.t
  !
  --- /Users/t/dev/cramtest/ls.t
  +++ /Users/t/dev/cramtest/ls.t.err
  @@ -1,3 +1,4 @@
     $ touch testme
     $ ls
  +  testme
  
  
  # Ran 1 tests, 0 skipped, 1 failed.

Ah-hah!  Now we're getting somewhere!  Fix the test by making 'ls.t' read
like so::

  $ touch testme
  $ ls
  testme

and run::

  % cram ls.t
  .
  # Ran 1 tests, 0 skipped, 0 failed.

Awesome!  Dot-victory ho!

Now let's do something a bit more interesting: check out and run my
PyCon 2011 talk code for ngram graphs.  Starting with this in 'khmer-ngram.t',
::

   $ git clone git://github.com/ctb/khmer-ngram.git
   $ cd khmer-ngram
   $ ls
   $ python run-doctests.py basic.txt

I run 'cram khmer-ngram.t' and get ::

   !
   --- /Users/t/dev/cramtest/khmer-ngram.t
   +++ /Users/t/dev/cramtest/khmer-ngram.t.err
   @@ -1,4 +1,15 @@
      $ git clone git://github.com/ctb/khmer-ngram.git
   +  Initialized empty Git repository in /private/(yada, yada)
      $ cd khmer-ngram
      $ ls
   +  basic.html
   +  basic.txt
   +  data
   +  graphsize-book.py
   +  hash.py
   +  load-book.py
   +  run-doctests.py
   +  shred-book.py
      $ python run-doctests.py basic.txt
   +  ... running doctests on basic.txt
   +  *** SUCCESS ***
   
   # Ran 1 tests, 0 skipped, 1 failed.
   
After getting cram to fix the file (using -i), and re-running cram, it now
chokes at exactly one place; betcha you can guess where...::

   !
   --- /Users/t/dev/cramtest/khmer-ngram.t
   +++ /Users/t/dev/cramtest/khmer-ngram.t.err
   @@ -1,5 +1,5 @@
      $ git clone git://github.com/ctb/khmer-ngram.git
   -  Initialized empty Git repository in /private/(yada, yada)
   +  Initialized empty Git repository in /private/(different yada)
      $ cd khmer-ngram
      $ ls
      basic.html
   
   # Ran 1 tests, 0 skipped, 1 failed.

Right.  How do you deal with output that does change unpredictably?
Easy!  Throw in a wildcard regexp like so ::

  Initialized empty Git repository in .* (re)

My whole khmer-ngram.t file now looks like this::

  $ git clone git://github.com/ctb/khmer-ngram.git
  Initialized empty Git repository in .* (re)
  $ cd khmer-ngram
  $ ls
  basic.html
  basic.txt
  data
  graphsize-book.py
  hash.py
  load-book.py
  run-doctests.py
  shred-book.py
  $ python run-doctests.py basic.txt
  ... running doctests on basic.txt
  *** SUCCESS ***

And I can run cram on it without a problem::

  .
  # Ran 1 tests, 0 skipped, 0 failed.

Great!

I love the regexp fix, too; none of this BS that doctest forces upon you.

So, the next question: how do multiple tests work?  If you look above,
you can see that it's running all the commands as one test.  Logically
you should be able to just separate out the block of text and make it
into multiple tests... let's try adding ::
 
  I'll add in another test:

    $ ls

to the khmer-ngram.t file; does that work?  It looks promising::

   !
   --- /Users/t/dev/cramtest/khmer-ngram.t
   +++ /Users/t/dev/cramtest/khmer-ngram.t.err
   @@ -17,3 +17,12 @@
    I'll add in another test:
    
      $ ls
   +  basic.html
   +  basic.txt
   +  data
   +  graphsize-book.py
   +  hash.py
   +  hash.pyc
   +  load-book.py
   +  run-doctests.py
   +  shred-book.py
   
   # Ran 1 tests, 0 skipped, 1 failed.

and it sees two tests... but, after fixing the expected output using
'cram -i', I only get one test::

  .
  # Ran 1 tests, 0 skipped, 0 failed.

So it seems like a little internal inconsistency in cram here.  Two tests
when something's failing, one test when both are running.  No big deal
in the end.

And... I have to admit, that's about all I need for testing/checking
course materials!  The cram test format is perfectly compatible with
ReStructuredText, so I can go in and write real documents in it, and
then test them.  Command line testing FTW?

And (I just checked) I can even put in Python commands and run doctest
on the same file that cram runs on.  Awesome.

Critique:

The requirement for two spaces exactly before the $ was not obvious to
me, nor was the implicit (and silent, even in verbose mode) use of a
temp directory.  I wiped out my test file a few times by answering
"yes" to patching, too.  What was up with the 'reversed patch' foo??
And of course it'd be nice if the number of dots reflected something
more granular than the number of files run.  But heck, it mostly just
works!  I didn't even look at the source code at all!

Verdict: a tentative 8/10 on the "Can titus use your testing tool?"
scale.  

I'll try using it in anger on a real project next time I need it, and
report back from there.

--titus

p.s. To try out my full cram test from above, grab the file from the
khmer-ngram repo at github; see:

https://github.com/ctb/khmer-ngram/blob/master/cram-test.t .


----

**Legacy Comments**


Posted by masklinn on 2011-03-14 at 04:38. 

::

   &gt; The requirement for two spaces exactly before the $ was not
   obvious to me, nor was the implicit (and silent, even in verbose mode)
   use of a temp directory.     Though not perfect by a long shot, note
   that ``cram --help`` mentions both indent (but does not give a default
   value) and temporary directories (it suggests that it can leave them
   around after the tests).    Verbose mode should probably spell out the
   creation of the temp dir though, sounds like there's a need for a bug
   report there.


Posted by Titus Brown on 2011-03-14 at 08:30. 

::

   Thanks!  Good point!


Posted by Brodie Rao on 2011-03-14 at 10:52. 

::

   Thanks for the feedback!    Cram invokes GNU patch when merging
   unexpected output. It sounds like I might need to pass the
   -N/--forward flag to force it to interpret patches as forward patches.
   That said, I'm trying to reproduce the issue, and I can't figure out
   how. Do you have a complete example test that triggers it?    The
   documentation needs some work. I'll take a look at clarifying the temp
   directory and indentation bits.    I'm not married to the current
   output format, so if you have any ideas of what it should look like,
   I'm all ears. The test runner has no notion of specific test blocks
   within test files, but it might be worth adding that.


Posted by Titus Brown on 2011-03-15 at 11:52. 

::

   Brodie, I'll get back to you on all of these as I use cram more.  I'm
   wary of giving too much advice before I actually, you know, use it...


Posted by Ian Bicking on 2011-03-16 at 02:29. 

::

   There's also ScriptTest; it's not a test runner, but it does similar
   things and perhaps more features, specifically giving tools to monitor
   file changes.

