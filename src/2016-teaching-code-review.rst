Introducing undergraduates to code review
#########################################

:author: C\. Titus Brown
:tags: code review,khmer
:date: 2016-02-22
:slug: 2016-teaching-code-review
:category: teaching
           
A few days, I gave an invited lecture on code review here at UC Davis.
The class was the ECS capstone class, consisting of about 100 CS
majors who were all working on some form of group project - all but a
few were doing something with programming.  I was told the class had
little to no experience with code review, but did know C++ rather
well.

Since I only had two hours AND I really hate lectures, I really wanted
to do something that was somewhat hands on, but didn't involve
programming or computer use.  Asking my Twitter network, I got a few
links -- Azalee Boestrom has `code review tutorial
<https://2016-aesir.readthedocs.org/en/latest/introducing-hypothesis.html>`__,
and Maxime Boissonneault demoed `exercism.io <http://exercism.io>`__
for me -- but neither fit what I had in mind.

The big thing was this: somewhere during my thought process, I
realized that I wanted to show the students the basic connection
between code review, testing, and refactoring.  How do you show *all*
of that to people who might have never done *any* of that?

I ended up with the plan that follows.  It went better than expected!

In preparation for class, I extracted some code from our khmer package --
specifically, the `KmerIterator code
<https://github.com/dib-lab/khmer/blob/master/lib/kmer_hash.hh#L275>`__
that takes a string of DNA and produces a succession of hashed values
from it -- and defactored it into a horrid function.  You can see the
result `here
<https://github.com/ctb/2016-code-review/blob/0c4337189b068646e69c052313c9c0e640c9e619/decompose.cc#L55>`__.
I also built a `simple Makefile <https://github.com/ctb/2016-code-review/blob/0c4337189b068646e69c052313c9c0e640c9e619/Makefile>`__.

In class, I started by asking the class what they thought the purpose
of code review was, and polled them on it via a free-text entry Google
Form.  This led to a discussion about **maintainability** vs
**correctness**, and my point that you couldn't approach the latter
over a long period of time without the former.

Then, I moved on to the code:

**First**, I ran through the purpose of the (ugly) code with lots of
hand-waving.

Then, I asked the question: how do we know if the code works?

To answer that, I live-coded a very simple version of the function
that was slow, but so simple that you could guarantee it worked --
`see it here
<https://github.com/ctb/2016-code-review/commit/1a8b3064b4832dd34566a485ea63396b7613cbef#diff-422e12d5a8d59d52ff9de59613bebb97R55>`__.
I saved the output from this "presumed-good" version, and compared it
to the output of the ugly version and showed that it matched.

For good measure, I also `automated that as a smoke test
<https://github.com/ctb/2016-code-review/commit/1a8b3064b4832dd34566a485ea63396b7613cbef#diff-b67911656ef5d18c4ae36cb6741b7965R6>`__,
so that with a simple 'make test' we could check to see if our latest
code changes produced presumed-good output.

Now I had code that probably worked.

**Second**, I polled the class (with a free-text entry approach using
Google Forms) for their thoughts on what the code needed.  Remember,
`it's ugly! <https://github.com/ctb/2016-code-review/blob/0c4337189b068646e69c052313c9c0e640c9e619/decompose.cc#L55>`__

I went through the resulting comments, and pulled out a few
suggestions.

One was "write down in detail what the biology
background is." I explained that you probably didn't want that kind of
comment in the code -- generally, anyone working on this code should
already be somewhat versed in the biology.

Another suggestion was "Comment the code." So I started putting in comments
like "set this variable to 0", which led to a discussion of how too many
comments could be silly and what we really wanted was *important* comments.
Here, I brought in my confession that I'd spent `15 minutes trying to understand why i started at k <https://github.com/ctb/2016-code-review/blob/1a8b3064b4832dd34566a485ea63396b7613cbef/decompose.cc#L78>`__, so `we commented that <https://github.com/ctb/2016-code-review/commit/f060393c0df228c9ab21cd1026b4cb2023478c39>`__ plus a few other things.

**Third**, I was running a bit low on time, so I took a previous
suggestion and `refactored the code
<https://github.com/ctb/2016-code-review/commit/152924aea00c9b3843e604626b500803a212b014>`__
by making longer, better variable names.  Here, I could show that the
code not only compiled but passed tests on the first try (hence the
commit comment).

**Finally**, I took the suggestion of one astute observer and split up
my now too-long function by building it into a class.  `The result
<https://github.com/ctb/2016-code-review/commit/1beb6abe8afac8762c8c188b04e2f3a78dedacd4>`__
looks reasonably similar to the actual code in khmer, which I pointed out;
even better, it passed my smoke test (hence the commit comment).
I got applause!

We closed with some discussion about where to look for more information,
and how to think about this stuff.  I showed them some live examples,
and referred them to David Soergel's paper, `Rampant software errors may undermine scientific results <http://f1000research.com/articles/3-303/v2>`__ as an entry point into some literature on error rates; I also showed them `Python coverage output <https://coverage.readthedocs.org/en/coverage-4.0.3/>`__ and `our code review guidelines for the khmer project <https://khmer.readthedocs.org/en/v2.0/dev/coding-guidelines-and-review.html>`__.

----

All in all, I managed to hold their attention (by live coding, by
cracking jokes, and by being energetic).  (I only got one negative
comment about the jokes! :).

I think I demonstrated about 80% of what I wanted to show, and filled
up the two hours nicely.  I can do a better job next time, of course,
and if I get invited back I'll try to provide a better outline of
points to make and references; I winged it too much this time and so
it's not a re-usable approach yet, I think.

--titus
