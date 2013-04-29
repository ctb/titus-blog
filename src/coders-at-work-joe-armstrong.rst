Excerpts from Coders At Work: Joe Armstrong Interview
#####################################################

:author: C\. Titus Brown
:tags: python,codersatwork
:date: 2013-04-29
:slug: coders-at-work-joe-armstrong
:category: python

I've been reading Peter Seibel's excellent book, `Coders at Work
<http://www.codersatwork.com/>`__, which is a transcription of
interviews with a dozen or so very well known and impactful
programmers.  After the first two interviews, I found myself itching
to highlight certain sections, and then I thought, heck, why not post
some of the bits I found most interesting?  This is a book everyone
should be aware of, and it's surprisingly readable.  Highly
recommended.

This is the first in what I expect to be a dozen or so blog posts, time
permitting.

The excerpts below come from Seibel's `interview with Joe Armstrong,
the inventer of Erlang
<http://www.codersatwork.com/joe-armstrong.html>`__.

My comments are labeled 'CTB'.

----

On learning to program
~~~~~~~~~~~~~~~~~~~~~~

Seibel: How did you learn to program? When did it all start?

Armstrong: When I was at school. I was born in 1950 so there weren't
many computers around then. The final year of school, I suppose I must
have been 17, the local council had a mainframe computer -- probably
an IBM. We could write Fortran on it. It was the usual thing -- you
wrote your programs on coding sheets and you sent them off. A week
later the coding sheets and the punch cards came back and you had to
approve them. But the people who made the punch cards would make
mistakes. So it might go backwards and forwards one or two times. And
then it would finally go to the computer center.

Then it went to the computer center and came back and the Fortran
compilter had stopped at the first syntactic error in the program. It
didn't even process the remainder of the program. It was something
like three months to run your first program. I learned then, instead
of sending one program you had to develop every single subroutine in
parallel and sned the lot. I think I wrote a little program to dispay
a chess board -- it would plot a chess board on the printer. But I had
to write all the subroutines as parallel tasks because the turnaround
time was so appallingly bad.

*CTB: I think it's fascinating to interpret this statement in light of
Erlang's pattern of small components, working in parallel
(http://en.wikipedia.org/wiki/Erlang_(programming_language).  Did
Armstrong shape his mental architecture in this pattern from the early
mainframe days, and then translate that over to programming design?
Also, this made me think about unit testing in a whole new way.*

On modern gizmos like "hierarchical file systems", and productivity
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Armstrong: The funny thing is, thinking back, I don't think all of
these modern gizmos actually make you any more
productive. Hierarchical file systems -- how do they make you more
productive? Most of software development goes on in your head
anyway. I think having worked with that simpler system imposes a kind
of disciplined way of thinking. If you haven't got a directory system
and you have to put all the files in one directory, you have to be
fairly disciplined. If you haven't got a revision control system, you
have to be fairly disciplined. Given that you apply that discipline to
what you're doing it doesn't seem to me to be any better to have
hierarchical file systems and revision control. They don't solve the
fundamental problem of solving your problem. They probably make it
easier for groups of people to work together. For individuals I don't
see any difference.

*CTB: If your tools require you to be as good as Joe Armstrong in order to
get things done, that's probably not a generalizable solution...*

On calling out to other languages, and Domain Specific Lanaguages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seibel: So if you were writing a big image processing work-flow
system, then would you write the actual image transformation in some
other language?

Armstrong: I'd write them in C or assembler or something. Or I might
actually write them in a dialect of Erlang and then cross-compile the
Erlang to C. Make a dialect - this kind of domain-specific language
kind of idea. Or I might write Erlang programs which generate C
programs rather than writing the C programs by hand. But the target
language would be C or assembler or something. Whether I wrote them by
hand or generated them would be the interesting question. I'm tending
toward automatically generating C rather than writing it by hand
because it's just easier.

*CTB: heh. So, I'd just generate C automatically from a dialect of Erlang...*

On debugging
~~~~~~~~~~~~

Seibel: What are the techniques that you use there? Print statements?

Armstrong. Print statements. The great gods of programming said,
"Thou shall put printf statements in your program at the point where
yout hink it's gone wrong, recompile, and run it.

Then there's -- I don't know if I read it somewhere or if I invented
it myself -- Joe's Law of Debugging, which is that all errors will be
plus/minus three statements of the place you last changed the program.

*CTB: one surprising commonality amongst many of the interviews thus far
is the lack of use (or disdain for) debuggers.  Almost everyone trots
out print statements!*
