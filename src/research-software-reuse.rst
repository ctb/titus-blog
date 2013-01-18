Replication, reproduction, and remixing in research software
############################################################

:author: C\. Titus Brown
:tags: science,research software,MickIsStillWrong
:date: 2013-1-18
:slug: research-software-reuse
:category: science

I just spent a really fun and exciting two hours installing a piece of
software that I needed to run to do a paper review.  The software
itself downloaded, but failed routinely on their own test data; after
delving through four layers of Perl and Python, I discovered that the
problems lay in my having installed the wrong version of two pieces of
underlying software.  One, a common microbiology framework whose name
rhymes with 'rhyme', had been updated since the release of the
software under review, and the new version of the framework is
incompatible with the software; since the software under review didn't
specify the versions of any of its dependencies, I had to hunt around
to figure out what it was looking for, find the version containing
that library by surfing github, and install it.  That was easy.  The
other problem was caused by a hidden dependency (four layers deep!)
that failed silently but resulted in a more visible failure a few
lines of code later; this was written in (I think) Python that called
Perl that called Python that called a binary executable, and so I had
to grub through Perl a bit.

2 hours.  Whee!

This resulted in a not-very-disguised `rant
<research-software-quality-a-rant.html>`__ on research software
quality, which was at least partly in response to `Mick Watson's post
on bioinformatics police
<http://biomickwatson.wordpress.com/2013/01/14/call-the-bioinformatics-police/>`__.
In this post -- which you should go read, it has a surprise ending,
and Mick apparently needs the traffic for his Google ads -- Mick says:

   First of all, I want to state quite clearly that I am not a code
   Nazi.  I don't care about your coding practices.  Good
   architecture, an elegant object model, a stable API, version
   control, efficient code reuse, efficient code etc etc.  I don't
   care.  Write all the unit tests you like, because if they fail,
   I’ll just force the install anyway.  I don't care if you used
   extreme programming, whether or not you involved Tibetan monks and
   had your github repository blessed by the Dalai Lama.  Maybe you
   ensured the planets were aligned before you released version 0.1,
   or made sure all of your code monkeys had perfect Feng Shui in
   their bedsits.  I don't care.  That don't impress me much.

   However, I do care that your code goddamn works.

   I think, as a scientist, if I take some published code, that it
   should work.  Not much too ask is it?  Sure, a readme.txt or a
   manual.pdf would be nice too, but first and foremost, it has to
   just do the eff-ing job it's supposed to.

I think this is really confusing, to the point of being wrong.  Now,
Mick `has been wrong before
<http://ivory.idyll.org/blog/big-data-biology-2.html>`__, but this
time I think he's so wrong that it's usefully wrong.

First, Mick and others noted that "surely you shouldn't be complaining
since you got the car for free".  Since I wrote *my* little rant in a
hurry (between child care obligations), I used a somewhat clumsy
analogy and failed to properly point out that while some research
software may be "free" in the sense that you don't pay for downloading
and using, *someone* has -- generally you, the taxpayer.

But that's not really the most important point.

I started thinking about this back when I wrote `my most depressing
blog post ever <http://ivory.idyll.org/blog/anecdotal-science.html>`__
-- depressing because people were actually arguing in the comments
that it's OK to write bad code.  I followed that post up with another
post on `code quality and testing
<http://ivory.idyll.org/blog/automated-testing-and-research-software.html>`__.
At this point realized that there were really several different things
being conflated in the discussion about research software, and I ended
up nailing this down in my own head when I wrote about `making science
better <http://ivory.idyll.org/blog/w4s-overview.html>`__ -- a fine
example of `essay writing generating surprises
<http://www.paulgraham.com/essay.html>`__.

Here is my conclusion:

The three uses of research software
-----------------------------------

**Replication** -- if you used software to do something important, and
publish it, and we can't replicate it by using the same software,
FAIL.  For all intents and purposes, the software can be a big black
box -- all we need to do to replicate your results are run it on your
data, or someone else's data.  This is where things like `RunMyCode
<http://www.runmycode.org/CompanionSite/>`__ come in, by making it
easy to distribute runtime environments.

**Reproduction** -- considered by some to be more important than
replication, reproducibility (`often confused with replication, by me
and others <http://ivory.idyll.org/blog/replication-i.html>`__) is the
question of whether or not your *answers* can be reached via different
means.  This is considered a holy grail of the science process: if
other people can get the same result without using an identical
process, then the result is more likely to be correct.  (I think this
is over-emphasized because systematic bias can be very
reproducible, but it's still important.)

**Reuse** -- in bioinformatics, specifically -- and scientific
software development more generally -- reuse and remixing is very
important. I think *this* is the key point that many just don't think
about.  Science isn't just about discovering facts; it's about making
progress in what we know.  This can be accelerated by reusable,
remixable tools.  Any one individual end goal may be knowing some fact
or set of facts about something, but the process by which we reach
that goal will often better enable others to reach *their* end goal
faster, better, cheaper, and more accurately.  This is the point I
failed to make well in my post `Virtual machines are harmful to
reproducibility
<http://ivory.idyll.org/blog/vms-considered-harmful.html>`__; somewhat
ironically, Mick agrees with me on that one :).  Science can be most
easily accelerated if you make your source code available so that
others can riff off it.

I have read many arguments against this: that publishing a theoretical
description of an algorithm is enough; or that it's actually harmful
to others to provide the source, because it forces people to reproduce
your work rather than merely replicate; or that publishing code
obligates you to support; or that publishing *bad* code is a bad idea,
and you need to clean it up to publish it.  **Bushwah.** These
specific objections are easily answered ((a) efficient and correct
implementation matters, and the algorithmic description often masks
important implementation details; plus, `it's hard!
<http://codecapsule.com/2012/01/18/how-to-implement-a-paper/>`__; (b)
as Victoria Stodden `points out
<http://magazine.amstat.org/blog/2011/07/01/trust-your-science/>`__,
what do you do when two implementations disagree? Write a third? No,
you compare the implementations, for which you need the source; (c)
No, it doesn't; (d) the main reason people avoid publishing code and
data is because they're afraid it's wrong `(and for good reason,
apparently)
<http://andrewgelman.com/2011/11/insecure-researchers-arent-sharing-their-data/>`__),
which indicts the whole field).  None of these arguments hold up, IMO.

I personally hate `anecdotal science
<http://ivory.idyll.org/blog/anecdotal-science.html>`__ tremendously,
and I keep on coming back to that SUPER awesome paper with a data
mining approach we wanted to try... but with a script that had a
syntax error in line 2.  Grr.  Reuse, blocked; I didn't trust any of
their work after that. (A good guess on my part -- the entire approach
turned out to be too fragile and parameter dependent to use, and
frankly the paper should not have been published.)

My inability to use your software aside, though, I think the main
point is this:

Bad code is often wrong code
----------------------------

Sure, you don't need (and I certainly don't have ;) many of the things
that Mick argues are irrelevant: good architecture, an elegant object
model, a stable API, efficient code, etc.  Most of these are about
explicit code reuse, and odds are high that no one is ever going to
look at or reuse your code -- it just needs to be possible to do so,
for all three of the reasons above.

But, Mick?  I'll fight you to the death on version control.  Why?

Writing correct code is hard, and a vast array of effort has been
brought to bear on code correctness over the years; it is simply
stupid to ignore this experience.  This is the point we try to make in
our `Best Practices for Scientific Computing paper
<http://arxiv.org/abs/1210.0530>`__ -- you don't *have* to use version
control, but you have a great chance of introducing regressions if you
don't.  You don't *need* to write tests of any kind, but this goes
against the experience of virtually every modern software professional
you talk to.  Et cetera.

If you `buy a car and it doesn't work in obvious ways
<http://ivory.idyll.org/blog/research-software-quality-a-rant.html>`__
you should be very skeptical about the engineers who designed it.
For example, you might not want to cross the bridge that they designed,
or fly in an airplane.  Why would I treat scientific software any
differently?

But you don't need to listen to me on this -- no less of an expert
than `Van Halen <http://www.snopes.com/music/artists/vanhalen.asp>`__
makes the same point: paying attention to the details is an indicator
of general competence.

The bottom line is this: if the code looks badly written and ignores
essentially all major tenets of modern software design,
it's probably seriously wrong in places.  Not because the authors
aren't good scientists, not because of some lack of Dalai Lama
blessing, but because software engineering is *hard* **hard** *hard*,
and if you can't be bothered to learn how to use version control, you
shouldn't be trusted to write important software.

This is true in much the same way that using basic lab practices are
both importand indicative.  If you wander into someone's lab and you
see someone using TA buffer with lots of solid precipitate to pour a
gel shift gel under the advisor's eyes, might you not wonder about the
reliability of said lab's results?  If the lab's PI says "don't worry
about those negative PCR controls, they're always negative and it's a
waste of reagents to run them" -- run screaming, amiright?

Every now and then some slick shyster comes my way (`usually Randy
Olson <http://www.randalolson.com/>`__ or someone else from `Chris
Adami's lab <http://adamilab.blogspot.com/>`__) and explains how
honest-to-gosh, they have found that unit testing isn't as important
as, say, functional testing in their simulations.  Great!  You have a
reason based on experience -- I respect your right to have an
opinion! It's the people who blithely dismiss Practice X (version
control, usually) because "it's not that important, and I never
learned it anyway" that drive me nuts and turn me stabby.

Punting on software remixability
--------------------------------

A few final words, courtesy of my late night experience with software
installs.

If you say "this software works best when we install it for you and give
you a virtual machine", you are essentially punting on the idea that
anyone will ever combine your software with anyone else's.

If you provide no documentation anywhere, and no README, then I am
pretty sure you're not serious about anyone else ever using it.  (How
hard is this, really?)

If you rely on other packages but never specify a version number or
test for "correct" output of packages you depend on, the odds are that
your software will bitrot to unusability quite quickly.  Please don't
do that.  Your software looks useful and I'd like to try it out in
6 months, after you've moved on to something else.

It's still all about the incentives
-----------------------------------

I don't actually harbor much anger towards the software that expended
so much of my time -- the software seems to work now, and it's not
that badly written; I intend to submit patches or bug reports to
further improve it.  Mick is right that software needs to enable good biology,
above all else, and that's what I'm trying to evaluate in the review.
Sure, my life would be easier if the software had been written with
more of eye towards bitrot, and I'm loathe to recommend it to newbies, but...

...I recognize `that the explicit incentives for writing good, reusable
software are lacking <http://www.bendmorris.com/2012/12/what-incentives-are-there-to-maintain.html>`__.  I'm going to keep on trucking, though, `because
it seems to be working
<http://ivory.idyll.org/blog/openness-and-online-reputation-recognized-in-grant-reviews.html>`__.
`And I'll see *you* from the other side of an anonymous review sheet
:)
<http://ivory.idyll.org/blog/blog-review-criteria-for-bioinfo.html>`__.

One final thought for y'all.  As `Data of Unusual Size
<http://ivory.idyll.org/blog/big-data-biology.html>`__ continues to
make inroads into science, more and more software will be written, and
more and more of the conversation *needs* to be about good software
capacity building, aka software cyberinfrastructure.  Big Data is
sufficiently inconvenient that hastily or badly written software
infrastructure will doom you to irrelevance.  Worth a think.

--titus

p.s. Need training and exposure to good scientific computing practice?
`Know Python, will
travel. <http://software-carpentry.org/blog/2013/01/cold-call.html>`__
Drop us a line.

p.p.s. `Stop hosting code on your lab Web site.  <http://gettinggeneticsdone.blogspot.com/2013/01/stop-hosting-data-and-code-on-your-lab.html>`__