Why software development practice matters, Containerization version
###################################################################

:author: C\. Titus Brown
:tags: software,sustainability
:date: 2016-01-14
:slug: 2016-containerization-disaster
:category: science

`A while back <https://www.youtube.com/watch?x-yt-cl=84359240&x-yt-ts=1421782837&feature=player_embedded&v=ZACVcJt0oJA#t=7303>`__, Kai Blin (via Nick
Loman) asked Michael Barton:

   If we containerize all these things won't it just encourage worse
   software development practices; right now developers still need to
   consider someone other than themselves installing the software.

and Michael Barton's response, transcribed, was:

   "It's a good point. Ultimately, though, if I can get a container,
   and it works, and I know it will work, do you care how well it was
   developed? I think if a software developer uses unit tests, feature
   tests, and all those things, it will be easier for themselves to
   develop the software, but if I can get a container and even if it
   was, say, developed with terrible software practices, as long as it
   works for me and nucleotide.es will test it and make sure it works,
   then do you care?"

The answer is unambiguously yes, of course.  Here's today's anecdote:

We've spent a few months working with a fairly widely used software
package in bioinformatics.  We found a really obvious but rather minor
bug in it a month or two ago, and in tracking down the location of the
bug, we spent a lot of time looking at the source code.

Because we looked at it, we no longer trust the package.

The source code is long, complicated, poorly modularized, and (in the
place we found the bug) is largely incomprehensible.  It comes with no
test suite. In order to try to fix the bug, we would have to first
create a bunch of our own tests of the larger code base.  We are
therefore declining to fix the bug (although it's obvious enough that
we will probably contact the developers).

Did I mention that it's widely used?

----

So, in response to Michael:

You can containerize bad code all you want, and now you'll have nice,
easy-to-install code that is producing wrong answers.

Yay! Wrong answers more quickly!!!

----

We need to recognize that `most code is broken
<http://f1000research.com/articles/3-303/>`__, and that `bad code is
*much* more likely to be wrong
<http://ivory.idyll.org/blog/research-software-reuse.html>`__.  If
you're not using three of the most obvious lines of defenses against
broken code (small functions, version control, and automated tests)
then your code is probably wrong. Full stop.

----

Back to the software with the bug:

I'm honestly not sure what to do next.  Our options are --

1. File a bug report, stop using the package, and be on our merry way.

2. Dive into the code base, build a test suite, and put the time into
   verifying someone else's code so that we and others can use it reliably.

3. Dive into the code base, find more bugs, and then blog about how unreliable
   the software is - the "name them and shame them" approach.  (Doing this
   without finding more actual bugs would be unfair IMO; at the moment it's
   just an intuition, albeit it a strong one.)

I suppose I could contact the developers and have an frank and robust
discussion with them about how they need to test their software, but I
don't know them very well and think it would lead into a big time
suck.

But I also am concerned about taking the time away from other things
to work on this.  The time tradeoffs are considerable - I have spouse
& children, meetings with postdocs/ grad students/collaborators,
training workshops, and exercise that occupy essentially all my time.
Should I spend what little time I have to think and write and code,
on this?

A fourth option that I am leaning towards is "testing-lite" - test the
key bits that we care about, and then do hack-y or low-performance
reimplementations of the bits that we really care about, and then
compare results.

A fifth approach (that would probably take too much time) would be to
combine 2 and 3 above with refactoring of the code base itself,
followed by re- or co-publication.  This is probably the right approach.

----

More generally, what do we do about this *kind* of thing as a
community?  What do people think about 1-5 above? Are there approaches
that I'm missing here?

--titus

p.s. I'd appreciate it if those who know what software I'm talking
about could avoid outing it; thanks.
