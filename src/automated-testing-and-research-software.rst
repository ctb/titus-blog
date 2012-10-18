Automated testing and research software
#######################################

:author: C\. Titus Brown
:tags: science,replication
:date: 2012-10-18
:slug: automated-testing-and-research-software
:category: science
:status: draft

After yet another round of futile Twittering on the subject of
research software, I thought I'd share a deeply personal story -- a
story that explains some of my rather adamant stance that most
research scientists need to think more critically about their code,
and should adopt at least some of the basic coding hygiene used by
virtually every modern practicing programmer.

A painful personal anecdote
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Way back in the early 2000s, I switched over to Python as my
day-to-day working language.  I was in my graduate lab doing
bioinformatics and genomics, among other things, and Python was
rocking my world.  I'd passed through several previous languages for
research work -- C, Tcl (anyone else remember ArsDigita and
AOLServer?), and Perl -- but Python was so readable and easy to
modularize that I found myself actually reusing substantial amounts of
code by sharing it between projects.

An awful lot of the time, this shared code was in the form of scripts,
little snippets of code that read in sequences, did horrible things to
them, and spat them back out.  Or correlated lots of different BLAST
files.  Or whatever needed to be done.

Now, I wasn't yet storing these scripts in version control --
centralized version control is hard to justify for lots o' little
disconnected scripts, and that's all we had in the bad old days -- but
I *was* reusing them.  And just about every time I used a script for
more than one project, I found a bug or two.  Not often a big one,
since I was a reasonably careful programmer and I was doing very
simple things, but almost always *something*.  And, of course, the
longer the script, the more likely I was to find that some portion of
it was buggy.  But even in my smallish 15-30 line scripts, I would
find off-by-one errors, or a misplaced 'if' that lacked an important
'else' for some corner case.

Being a scientist, it was hard to escape the implication that *most*
of my scripts were buggy, not just the ones I ended up reusing.

Did I start doing any kind of automated testing of my scripts?  Hell
no!  Anyone who wants to write automated tests for all their
little scriptlets is, frankly, insane.  But this *was* one of the two
catalysts that made me personally own up to the idea that most of my
code was probably somewhat wrong.

It also led to this aphorism:

   Every time you write a script, `God kills a kitten
   <http://en.wikipedia.org/wiki/Every_time_you_masturbate..._God_kills_a_kitten>`__.

(Please, think of the kittens!)

This encapsulates the idea that yes, you've gotta write scripts -- and
some kittens are gonna die -- but you should try to minimize it.  (See
my second postscript for more on my approaches to scripting.)

So that's why I started thinking about code reliability: because my code
was, demonstrably, not reliable.

On good practice
~~~~~~~~~~~~~~~~

Now, over the years, I've had many, many discussions with scientists
about their code.  Yes, most scientists aren't formally trained in
anything approximating software engineering (note that it turns out
that many *software engineers* were never formally trained in this
either -- our undergrad CS education is 5-15 years behind the times).
And yes, I think a lot of the standard software engineering stuff,
including things like patterns and object-oriented design, is serious
overkill for most scientists.  But I've never been impressed with
any of the multitude of reasons given for avoiding certain kinds of
good programming practice.

I think there are three particularly important points of practice that
we hit on in the `Best practices for Scientific Computing
<http://arxiv.org/pdf/1210.0530v1.pdf>`__ paper:

First, use version control.  Traceability and provenance is important;
we expect experimental scientists to keep a lab notebook, and you
should view version control as a computational equivalent for your
source code. (As I told one postdoc here at MSU, if you aren't using
version control for your code, stop pretending to be a scientist.  I
make myself popular, I do!)

Second, optimize later.  I write all my code in Python first, and
organize my code and algorithms in Python.  I then build in C and C++
sparingly and as needed.  This strategy lets me think about function
and correctness in a language that's succinct, easy to write, easy to
organize, and easy to read -- and it works because Python integrates
so nicely with C and C++, so I can slowly refactor speed and memory
improvements in over time without affecting the core Python
functionality.

Third, plan for mistakes!  You *will* screw up, and the important thing
is not to prevent it in the first place, which is impossible, but to
plan around catching them.

What kind of testing should you do?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I highly recommend three core testing approaches.  The first is what I
(improperly) call regression tests: these are tests that verify that,
on certain test input, code is performing the same today as it did
yesterday.  This corresponds to the basic principle that if your
program's observed behavior changes unexpectedly, you should probably
figure out why.

The second testing approach is `Stupidity Driven Testing
<http://ivory.idyll.org/blog/stupidity-driven-testing.html>`__, in
which you write tests for bugs that you actually find.  The basic
principle here is that once you've found a bug, you should probably
make sure you avoid making that same mistake once.  (This also has the
salubrious effect of adaptively targeting tests at the bits of code
that fail most often!)

The third testing approach I recommend is to use code coverage
analysis to drive the writing of new tests.  Code coverage analysis
(at the statement level, for you purists) simply tracks which lines of
code are executed during your existing tests, and for mature code your
goal should be to reach 80-95% code coverage with your test suite.
Argumentative people are always quick to point out that just because
code is executed by a test doesn't mean that it's correct, which is
true; my response is that if code isn't executed by *any* test
whatsoever, then we *know* it's not being tested.

There are all sorts of other things that people recommend doing, but
I've never been a fan of things like Test Driven Development. *shrug*
If you believe strongly in it, write a blog post telling me why I'm wrong :)

Myths of research software
~~~~~~~~~~~~~~~~~~~~~~~~~~

Let's do some role playing.  You, dear reader, are an overwhelmed and
(in the area of programming practice) a largely uneducated graduate
student/postdoc/faculty member.  You are desperately trying to avoid
the extra work I suggest above, and are convinced that research
software is somehow different from all other software.  And I?  I am
an overly experienced, frustrated, and angry man pointing out that you
are wrong :).

Go!

**Most research software is only run once, or a few times! Why put
in the effort to write tests?** There are a few problems with this
one.  First, you should still care if you get the correct answer,
right?  And second, I think one implication here is that you don't
particularly care about maintainability of research software and
shouldn't expend the extra effort.

But the problem is that maintainability and correctness have an obvious
and intuitive link: programs that are easy to maintain are easier to
understand, and programs that are easier to understand are much more
likely to be correct.  More, I don't know of any studies showing that
cowboy coding (write code! trust results!) results in reliably correct
code, while I can definitely point you at studies that show that *some*
kind of good practice, including any of formal design, code review,
and automated testing, leads to more reliable code.

There is a third problem here, too: successful code often *will* be
reused, either by you, or by your labmates, or by your readers.  (You
*are* publishing your code with the paper, right?)  You'd be surprised
how often I've needed to dig into old code to repurpose it...

**People should be *rewriting* my methods, not *reusing* them** OK,
that is defensible from a purely scientific point of view (see
`Accountable research software
<http://gasstationwithoutpumps.wordpress.com/2012/08/27/accountable-research-software/>`__).
But, as Victoria Stodden pointed out to me in a private response, how
do we track down the source of discrepancies between two
implementations of methods?  What, reimplement it a third time?  And,
more generally, this whole rewrite-and-don't-reuse sounds like a
gigantic waste of time to me.  I'm sympathetic to the idea but
ultimately think we have better things to do, like worry about whether
or not the *results* from running the program are scientifically
useful and correct.

**Good industry practice doesn't fit with research** You can always come up
with a laundry list of rather nonspecific things, like "I'm doing
stochastic simulations; test that, biatch!" (Sure -- that's what
regression testing and pseudo-random number seeds are for.) Or
"version control doesn't work for storing multi-gb data sets." (OK,
don't store them there, then.  Just put the code in version control,
like everyone else.) Or "how do I write unit tests when I don't know
the answer?" (We should probably talk about what you think unit tests
actually are, first.)  Or "github doesn't solve all my problems, so
I'm not going to use it." (Uhhh... ok, how about using it to solve
*some* of your problems?)

Hey, I get you.  It's not easy.  And you've never been trained in it,
either. But you're smart.  If you actually care about whether or not
your code is correct, figure it out.  `(We're Software Carpentry.
We're here to help.) <http://www.software-carpentry.org>`__

I think this notion that research software is something
special and deserving of some accomodation is so wrong that
it's hard to even address it intelligently.  What, you think people at
Google aren't doing exploratory programming where they don't know the
answer already?  You think Amazon customers don't behave in unexpected
ways?  You think Facebook social network data mining is easy? The
difference there is that companies have a direct economic incentive to
solve these problems, and you don't.

More, I have the niggling little feeling that this argument is
frequently trotted out by people who want to be lazy.  I'm actually
*completely* on board with the idea that you find everything I have to
say about actual practice to be useless -- and I'd love to find out
why I'm wrong, and understand how what you're doing is better!  But
when you say "it's just hopelessly different! I give up!" I am
suspicious of your motivations...

**My boss doesn't care.** Yeah, that's a big problem.  They're wrong.
Become your own boss :).

**I don't have time to do all this stuff** Sure, time is my big
problem too.  I just have lots of bad experience that suggests that most
of my code is buggy in one way or another, and that motivates me to do
something about it.

More generally, *are you feeling lucky, punk?*

You are statistically unlikely to be forced to retract your work due
to a software bug (although see the list in `the third paragraph of
our Best Practices paper <http://arxiv.org/pdf/1210.0530v1.pdf>`__).
And you're not in a company, where a bug can cause your company or
your customers real pain.  No, you're just involved in mankind's
greatest endeavor, trying to understand the universe, solve pressing
societal problems, cure diseases, and provide a better tomorrow for
Amarie, Jessie, and Maddie.  But that's ok -- it's not *all* on your
shoulders.  Just a little bit.

Ignorance is not an excuse
~~~~~~~~~~~~~~~~~~~~~~~~~~

Science in general, and `biology and bioinformatics in particular
<ivory.idyll.org/blog/whats-the-matter-with-bio-grad-school.html>`__,
are suffering from the snail's pace at which education changes.
We simply don't train people in this stuff, which is why efforts
like `Software Carpentry <http://software-carpentry.org>`__ are
so #!#%!% important.

But, at the end of the day, it's not ok to be a computational
scientist and ignorant of good practice in programming any more, just
like you can't do data analysis and be completely ignorant of
statistics, even if you have no formal training.  As a researcher it's
your responsibility to do a good job on your research, period.  If
that means learnng something new, well, you've presumably had to do it
before, and you'll have to do it again!

Parting thoughts
~~~~~~~~~~~~~~~~

For those of you that think you don't need to worry about the quality
of your code and its results, you might consider reading about `the
Dunning-Krueger effect
<http://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect>`__.
Or you can take inspiration from Shakespeare, one of the earliest
software engineers -- 

   "The fool doth think he is wise, but the wise man knows himself to be a fool."

or Bertrand Russell, an architecture astronaut --

   "One of the painful things about our time is that those who feel certainty are stupid, and those with any imagination and understanding are filled with doubt and indecision"

which I think applies pretty well to code, or even Charles Darwin, a
somewhat well known research scientist:

   "Ignorance more frequently begets confidence than does knowledge"

If you're confident your code works, you're probably wrong.  And that
should worry you.

--titus

p.s. If you're wondering what the second catalyst was for me becoming
so interested in testing, it was my experience in developing the
Cartwheel Web server for comparative sequence analysis.  I started to
notice that every time I added a feature to Cartwheel, I broke an old
feature.  The argument there is explained in much better detail in my
oooooold blog post on the `(Lack of) Testing Death Spiral
<http://ivory.idyll.org/blog/software-quality-death-spiral.html>`__.

p.p.s. How do I actually deal with the errors-in-scripts issue?
Increasingly I try to build core libraries that contain all the tricky
and error-prone functionality, and then I write 5-15 line scripts that
use those libraries to do useful stuff.  And, once a script becomes
important enough, I wrap it with command line tests.  See
http://github.com/ged-lab/screed and http://github.com/ged-lab/khmer
for examples of this approach.  I'll let you know how it works out in
another 5-10 years :)