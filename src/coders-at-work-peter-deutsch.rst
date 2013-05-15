Excerpts from Coders At Work: Peter Deutsch Interview
#####################################################

:author: C\. Titus Brown
:tags: python,codersatwork
:date: 2013-05-14
:slug: coders-at-work-peter-deutsch
:category: python

I've been reading Peter Seibel's excellent book, `Coders at Work
<http://www.codersatwork.com/>`__, which is a transcription of
interviews with a dozen or so very well known and impactful
programmers.  After the first two interviews, I found myself itching
to highlight certain sections, and then I thought, heck, why not post
some of the bits I found most interesting?  This is a book everyone
should be aware of, and it's surprisingly readable.  Highly
recommended.

This is the second of my blog posts.  The first contained excerpts
from Seibel's `interview with Joe Armstrong
<http://ivory.idyll.org/blog/coders-at-work-joe-armstrong.html>`__.

The excerpts below come from Seibel's `interview with Peter Deutsch
<http://www.codersatwork.com/l-peter-deutsch.html>`__, who is (among
many other things) the creator and long-time maintainer of
Ghostscript.

My comments are labeled 'CTB'.

----

On programmers
~~~~~~~~~~~~~~

Seibel: So is it OK for people who don't have a talent for
systems-level thinking to work on smaller parts of software?
Can you split the programmers and the architects? Or do you
really want everyone who's working on systems-style software, since it is
sort of fractal, to be able think in terms of systems?

Deutsch: ... But in terms of who should do software, I don't have
a good flat answer that. I do know that the further down in the plumbing the
software is, the more important it is that it be built by really good people.
That's an elitist point of view, and I'm happy to hold it.

...

You know the old story about the telephone and the telephone operators?
The story is, sometime fairly early in the adoption of the telephone,
when it was clear that use of the telephone was just expanding at an incredible
rate, more and more people were having to be hired to work as operators
because we didn't have dial telephones. Someone extrapolated the
growth rate and said "My God. By 20 or 30 years from now, every single
person will have to be a telephone operator." Well, that's happened.
I think something like that may be happening in some big areas of programming
as well.

*CTB: This seemed like interesting commentary on the increasing ...
democratization? ... of computer use.*

Fast, cheap, good -- pick any two.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deutsch: ...The problem being the old saying in the business: "fast, cheap,
good -- pick any two." If you build things fast and you have some way of building them inexpensively, it's very unlikely that they're going to be good.  But this school of thought says you shouldn't expect software to last.

I think behind this perhaps is a mindset of software as expense vs
software as capital asset. I'm very much in the software-as-capital-asset school. When I was working at ParcPlace and Adele Goldberg was out there evangelizing object-oriented design, part of the way we talked about objects and part of the way we advocated object-oriented languages and design to our customers and potential customers is to say, "Look, you should treat software as a capital asset."

And there is no such thing as a capital asset that doesn't require ongoing
maintenance and investment. You should expect that there's going to be
some cost associated with maintaining a growing library of reusable software.
And that is going to complicate your accounting because it means you can't
charge the cost of building a piece of software only to the project
or the customer that's motivating the creation of that software at this
time. You have to think of it the way you would think of a capital asset.


CTB: A really good perspective that's relevant to `scientists' concerns about software and data <https://metarabbit.wordpress.com/2013/05/06/people-are-right-not-to-share-scientific-code/>`__.

On how software practice has (not) improved over the last 30 years
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seibel: So you don't believe the original object-reuse pitch quite as strongly now. Was there something wrong with the theory, or has it just not worked out for historical reasons?

Deutsch: Well, part of the reason that I don't call myself a computer scientists any more is that I've seen software practice over a period of just about 50 years and it basically hasn't improved tremendously in about the last 30 years.

If you look at programming languages I would make a strong case that programming languages have not improved qualitatively in the last 40 years.  There is no programming language in use today that is qualitatively better than Simula-67. I know that sounds kind of funny, but I really mean it. Java is not that much better than Simula-67.

Seibel: Smalltalk?

Deutsch: Smalltalk is somewhat better than Simula-67. But Smalltalk as it exists
today essentially existed in 1976. I'm not saying that today's
languages aren't better than the languages that existed 30 years ago. The language that I do all of my programming in today, Python, is, I think, a lot better
than anything that was available 30 years ago. I like it better than Smalltalk.

I use the word *qualitatively* very deliberately. Every programming language
today that I can think of, that's in substantial use, has the concept of
pointer. I don't know of any way to make software built using that fundamental
concept qualitatively better.

*CTB: Well, that's just a weird opinion in some ways.  But interesting,
especially since he has been around and active for so long, and his
perspective is obviously not based in ignorance.*

On temptation
~~~~~~~~~~~~~

Deutsch: Every now and then I feel a temptation to design a
programming language but then I just lie down until it goes away.  But
if I were to give in to that temptation, it would have a pretty
fundamental cleavage between a functional part that talked only about
values and had no concept of pointer, and a different sphere of some
kind that talked about patterns of sharing and reference and control.

More on Smalltalk and Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Seibel: So, despite it not being qualitatively better than Smalltalk,
you still like Python better.

Deutsch: I do. There are several reasons. With Python there's a very
clear story of what is a program and what it means to run a program
and what it means to be part of a program. There's a concept of
module, and modules declare basically what information they need from other
modules. So it's possible to develop a module or a group of modules and share
them with other people and those other people can come along and look at those modules and know pretty much exactly what they depend on and know what their boundaries are.

...

I've talked with the few of my buddies that are still at VisualWorks about
open-sourcing the object engine, the just-in-time code generator,
which, even though I wrote it, I still think is better than a lot of what's
out there. Gosh, here we have Smalltalk, which has this really great code-generation machinery, which is now very mature -- it's about 20 years old and it's extremely reliable. It's a relatively simple, relatively retargetable, quite efficient just-in-time code generator that's designed to work really well with non type-declared languages. On the other hand, here's Python, which is this wonderful language with these wonderful libraries and a slow-as-mud implementation. Wouldn't it be nice if we could bring the two together?

(I'm a bit fixated on Python. OK?)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Deutsch: ... But that brings me to the other half, the other reason I
like Python syntax better, which is that Lisp is lexically pretty
monotonous.

Seibel: I think Larry Wall described it as a bowl of oatmeal with
fingernail clippings in it.

Deutsch: Well, my description of Perl is something that looks like it
came out of the wrong end of a dog. I think Larry Wall has a lot of
nerve talking about language design -- Perl is an abomination as a
language.  But let's not go there.

*CTB: heh.*
