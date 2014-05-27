Some thoughts on research coding and Stupidity Driven Development
#################################################################

:author: C\. Titus Brown
:tags: khmer,testing
:date: 2014-05-26
:slug: 2014-research-coding
:category: science

I'm on a European trip that involves several plane flights accompanied
by long airport stays, and I just used some of that time to do a bit
of tedious coding on khmer.

The coding I did was to add proper exception handling to khmer's
internal file loading routines `(see the pull request)
<https://github.com/ged-lab/khmer/pull/333>`__.  The old behavior
threw std::exceptions in C++ code that were not handled by the Python
API, and hence crashed Python.  The new behavior transforms the errors
into an exception class that the C to Python bridge explicitly handles
and turns into IOErrors in Python.

Since khmer is at version 1.0.1 already, you would be excused for
being surprised that an attempt to (say) load a k-mer hashtable from a
nonexistent file would result in the Python interpreter crashing.
Indeed.  This seems like a reasonably important part of maturity.  Why
did we wait so long?  Why wasn't proper exception handling prioritized
well before this?

Well, the short answer is that the code worked well enough!  When our
Python scripts crashed, there was an error message that was pretty
clear, and it didn't happen very often in the normal course of things.

So why update it now?  First, it was time: it'd been on our issue list
for some time, and was one of the last sets of crashing problems we
had.  But, second, some of our file loading code was starting to cause
problems.  We've spent the last year or so steadily accumulating
reports of infinite loops that eventually pointed squarely at our file
loading code `(see the list)
<https://github.com/ged-lab/khmer/pull/333#issuecomment-43455707>`__.
These are now some of our more frequent bug reports, and they come
from non-obvious causes -- they seem to be triggered by anything that
truncates a file, like running out of disk space or having an
NFS-triggered write error.  So, since I had the time during my
travels, I put in the effort to add error handling and exception
propagation.  (The file reading code was also insanely stupid.  It's
slightly less so now.)

And this brings me back to the title.  For research purposes, we're
much more worried about inaccurate research results than we are about
crashing bugs.  The latter are annoying and obtrusive, but don't
result in erroneous results; inaccurate code causes much less visible
problems that can be more serious scientifically.  So we test the
bejeezus out of our scientific code while practicing a kind of long
game with the rest of the khmer code: we wait until there are actual
behavioral problems that we could trace back to some bit of code, and
then we fix it.

A fine example of Stupidity Driven Functional Testing!

If you read some of the many rants about research programming (I ran
across `this one
<http://academia.stackexchange.com/questions/21276/best-practice-models-for-research-code>`__
yesterday), it's clear that choosing the right balance between general
code quality and research functionality right is tough and is probably
individual to the project.  There's also `this problem
<http://www.yosefk.com/blog/why-bad-scientific-code-beats-code-following-best-practices.html>`__
-- that "best practices" all too often is interpreted to mean
over-engineering code for the future.  We have some of that in khmer,
to balance our under-engineered code, but we've mostly stayed away
from complex class hierarchies and the like.

What's the right answer for us?  We don't know, but we're putting a
fair amount of effort into figuring it out :).

--titus
