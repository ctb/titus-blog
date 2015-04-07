Towards a bioinformatics middle class
#####################################

:author: C\. Titus Brown
:tags: python,bioinformatics
:date: 2015-04-07
:slug: 2015-bioinformatics-middle-class
:category: science

Jared Simpson `just posted
<http://simpsonlab.github.io/2015/03/30/optimizing-hmm/>`__ a great
blog entry on `nanopolish <https://github.com/jts/nanopolish>`__, an
HMM-based consensus caller for Oxford Nanopore data.  In it he describes
how he moved from a Python prototype to a standalone C++ program.
It's a great blog post, but it struck one discordant note for me.
In the post, Jared says:

    I was not satisfied with the Python/C++ hybrid design. I am
    sensitive to installation issues when releasing software as I have
    found that installing dependencies is a major source of problems
    for the user (...). I admire Heng Li's software where one usually
    just needs to run git clone and make to build the program.

Fundamentally, moving from a lightweight Python layer on top of a
heavier, optimized C++ library into a standalone binary seems like a
step backwards to me.  I wrote `on Twitter
<https://twitter.com/ctitusbrown/status/585401215250522112>`__,

    I worry ... that short-term convenience is lost at expense of
    composability and flexibility. Thoughts?

which spawned an interesting conversation about dependency hell,
software engineering done proper, funding, open source process
and upstream contributions, and design vs language.

I don't have a single coherent message to give, but I wanted to make a few
points in a longer format (hence this blog post).

First, *format hell* is directly caused by everyone developing their
own programs, which consume and emit semi-standard formats.  In the
absence of strong format standards (which I don't particularly want),
our choice may be between this format hell, and internal manipulation
of rich formats and data structures.  (Maybe I'm over-optimistic about
the latter?)

Second, a component ecosystem, based on scripting language wrappers
around C/C++, strikes me as a major step forward in terms of
flexibility and composability. (That's what we're working towards with
some of our khmer development.) A bunch of lightweight components that
each do one interesting thing, well, would let us separate specific
function from overall processing logic and format parsing.  Moreover,
it would be **testable** - a major concern with our current "stack"
in bioinformatics, which is only amenable to high level testing.

Third, and this is my real concern - C++ is an utterly opaque language
to most people.  For example, Nick Loman - a pretty sophisticated
bioinformatics dude, IMO - is almost certainly completely incapable of
doing anything with nanopolish's internals.  This is because his
training is in biology, not in programming. I'm picking on Nick
because he's Jared's partner in nanopolish, but I think this is a
generally true statement of many quite capable bioinformaticians.
Heck, I'm perfectly capable in C and can scratch my way through C++
programming, but I do my best to avoid packages that have only a C++
interface because of the procedural overhead involved.

I disagree strongly with Jared's black & white `statement
<https://twitter.com/jaredtsimpson/status/585434975408889857>`__ that
"this isn't a language problem" -- part of it absolutely is!
Scripting languages enable a much more flexible and organic
interaction with algorithms than languages like Java and C++, in my
extensive personal experience.  People can also pick up scripting
languages much more easily than they can C++ or Java, because the
learning curve is not so steep (although the ultimate distance climbed
may be long).

This leads into my choice of title - at the end of the day, what do we
want?  Do we want a strong division between bioinformatics "haves" -
those who can grok serious C++ code at a deep level, and interact with
the C++ interface when they need to adapt code, vs those who consume
text I/O at the command line or via hacked-together pipelines?  Or do we
want a thicker "middle class", who appreciate the algorithms and can
use and reuse them in unexpected ways via a scripting language, but without
the investment and time commitment of digging into the underlying library
code?

I've put my energy squarely on the latter vision, with teaching, training,
software development, and publication, so you know where I stand :).  Maybe
I'm naive in thinking that this approach will build a better, stronger
set of approaches to bioinformatics and data-intensive biology than the
other approach, but I'm giving it the ol' college try.

--titus

p.s. I'm hoping to post a powerful demonstration of the component/library
approach in a few weeks; I'll revisit the topic then.

p.p.s. It should go without saying that Jared and Nick and Heng Li are
all great; this is not a personal diatribe, and given the amount of
time and energy we put into building khmer as a Python library, I wouldn't
recommend this approach in the current funding climate.  But I want to
(re)start the discussion!
