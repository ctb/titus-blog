Eating your own dogfood (but only eating half the bowl)
#######################################################

:author: C\. Titus Brown
:tags: testing,python
:date: 2008-04-20
:slug: eating-your-own-dogfood
:category: python


So I'm `pretty bullish on testing
<http://ivory.idyll.org/blog/mar-08/software-quality-death-spiral.html>`__
for maintenance reasons.  It was nice to see how well it worked out
for me when a user recently reported a problem with `Cartwheel
<http://cartwheel.idyll.org/>`__.

This is what happened: third-party package (LAGAN) that the user was running
through the Web interface depended on certain command-line behavior from
'sort'.  Now, I wasn't aware the the command-line arguments to sort were
still evolving, but apparently they are -- my latest Debian upgrade removed
some options (the '+1' behavior) in favor of '-k 1'.  In any case, I did
this big upgrade of many packages, and didn't realize that this third-party
program was now broken.  (More on that later.)

The user reported weird results, so I went and verified that he'd set
everything up properly and that this was in fact a real problem.  Then
I ran the Cartwheel automated test suite.  Voila!  Problem was instantly
pinpointed in a reproducible manner.

I fixed the program (editing Perl, ick), re-ran the tests, and then
re-ran the user's analyses.  Tada, done.

OK, so, great, the tests pinpointed the error for me after the user had
found it.

**Why did I have to wait for a user to report it?**

Because I wasn't running the tests under continuous integration on my
compute server.

**Why not?**

Can't think of why.

**What would you have done differently?**

I would have made sure all my tests were passing on my compute server
after I upgraded the thing, i.e. not been a schmuck.

**What have we learned?**

Tests are only useful if (first) you write them -- that's half the battle --
and (second) you run them.  Oops.

More generally, it was fun to note that by putting a fairly high-level
functional test on the batch-processing backend, I discovered a bug
several levels down in my software stack -- a problem lying between a
third-party package and a system utility.  Unit tests wouldn't have
found this bug, unless the third-party package had them (don't think
so) *and* I was running the third-party package unit tests (good
grief...)

OK, back to work.

--titus
