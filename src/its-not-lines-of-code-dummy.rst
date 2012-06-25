It's not the lines of code, dummy.
##################################

:author: C\. Titus Brown
:tags: python,programming
:date: 2007-12-27
:slug: its-not-lines-of-code-dummy
:category: python


Steve Yegge recently wrote a long article, `"Code's Worst Enemy"
<http://steve-yegge.blogspot.com/2007/12/codes-worst-enemy.html>`__,
about how "many lines of code" causes problems in projects.

That's obviously pretty silly.  To see why, let's examine a little
project I've recently started; conservatively, I estimate that it
incorporates well over a million lines of code: ::

  print 'hello, world'

Well, that's one line.

But what's needed to run it?  The Python interpreter; the C compiler
(to build the Python interpreter); the libraries necessary to run
Python and actually make that statement appear on the screen; and the
Linux (or Mac O$ X, or Window$) operating system and drivers needed to
bind them all together.

There's easily a million lines of C code in there, if not ten million.
So have I just coded on the most bloated, worst project of all time?

Nope.  It's not the lines of code that matter.  It's the lines of code
*you need to think about* that matter.

When I write Python code, I rarely need to worry about anything other
than *the code I'm writing*.  I don't need to think about the std lib
all that much, I certainly don't worry about the CPython core code,
and I touch on the UNIX kernel very infrequently.  Why?

Because all of that other code is nicely encapsulated, behaves in
expected ways, and rarely breaks.

And this is why having a full language, good libraries, and a reliable
OS are all ways to decrease the "brain load" of your software.

I also think it points to a deep truth of software engineering, which
is that a good library API is one that you don't need to think about
much.  A good library should be compact, inclusive of core features,
work reliably, and contain functionality orthogonal to your code.  All
of these things will help you worry about the core functionality of
*your own code* and not about any other code.

By almost any measure (excepting that of life itself) our software is
unimaginably (and unmanageably) complex already. We manage that
complexity as best we can by encapsulating functionality in libraries,
APIs, protocols, and "expectations" that are fulfilled, more often
than not.  And *that's* the real lesson you should take away from
Yegge's post: that writing a 500k Ball of Mud is a bad idea indeed,
but more because his design process failed well before he got to 500k
LoJC.

--titus

P.S.  JavaScript?  Really?  This reminds me of Phil Greenspun telling
me how great Tcl was as a way to develop a large framework -- and that
didn't end well...


----

**Legacy Comments**


Posted by Vinny on 2007-12-28 at 13:05. 

::

   Thoughts on the PS:    I've written a lot of Python code and a little
   Javascript code.  Python does the big things well - interpreted,
   dynamic typing, files as modules, single inheritence, instance methods
   as closures around 'self', constructors are functions.  Some parts are
   poor - blocks from whitespace (seriously complicates mixing editors
   and tab preferences), a severely limited lambda syntax, the name
   '<em>_init_</em>' as the constructor, the crufty interpreter
   implementation (hurts embedding), poor debuggers.    JS has a lot of
   problems, mainly in developing large code bases.  There is no
   intrinsic support for modules, prototype based inheritence is strange
   to many people, inheritence in general is poorly implemented, and JS
   lacks many of the niceties that python has - keyword parameters, list
   comprehensions and generators (soon to be added), methods that
   remember the object they are on (method closures).  On the other hand,
   JS has a graphical, resumable debugger (Venkman), a polished cross
   platform GUI framework (HTML / Firefox or XULRunner), a JIT compiler
   (Tamarin), and a syntax thats more familiar to C programmers and more
   editor friendly.    Ultimately, there are a lot of great python
   programmers out there, but there are far more JS programmers and
   growing.  JS has the tools that python is missing, and has the new
   language growth (JS 2.0).  I like python, but my bet in the long run
   is JS all the way.  Unless lisp/scheme makes a long shot comeback
   (still the king of macros and continuations).


Posted by Titus Brown on 2007-12-28 at 13:49. 

::

   But... Yegge's whole article (and my perspective too) is focused on
   maintenance of large, complicated codebases.  None of your comments on
   JS address this.  So JS may "win out" but it will be a pyrrhic victory
   unless it somehow overcomes the intrinsically poor library and code
   organization constructs -- something that Python excels at.


Posted by David Avraamides on 2007-12-28 at 13:51. 

::

   I had a similar reaction when I read Yegge's post. Isn't a large
   portion of that 500k code in reusable libraries or components? Doesn't
   he have things like sprites, a game engine, MUD tools, etc?    It
   would seem that most of that code should have been well-baked by now
   and he wouldn't really need to revisit and maintain it. Or as you put
   it, he wouldn't need to think about it much.


Posted by Paul Moore on 2007-12-29 at 18:41. 

::

   This made me think about an element of David Allen's "Getting things
   done" time management approach. He advocates getting things out of
   your mind by putting them into a filing system you **trust** (so you
   are comfortable you'll get prompted about things when you need to be).
   And it's similar with software - you don't need to concern yourself
   about those lines of code that you trust.    So, generally, I can
   ignore the Python interpreter, the stdlib, the OS, etc, because I
   assume they work. My project's code, I don't. That's why
   reimplementing standard library code is bad - you lose the trust
   element. It's also why bug-ridden libraries are bad - you don't trust
   the library, so all of that library code written by someone else comes
   into the area of "stuff you need to think about".    That's really
   what API encapsulation is about - putting a line around stuff you're
   prepared to trust to "just do its job".


Posted by Steve on 2007-12-30 at 00:25. 

::

   Although I cannot speak on Python, I disagree with what's been said
   about JavaScript. At the company I work for (which I cannot disclose,
   sorry), we have a pretty rock solid in-house JavaScript framework used
   for rapid application development.  The majority of it was written by
   one engineer, in less than 9 months, which consists of an extensive
   set of GUI components, browser inconsistency adjustments, box model
   adjustments, data transport, and a full environment for deploying and
   updating new applications, among other things.  Using this framework,
   two engineers were able to rewrite one of our applications in 1/5th
   the time it took us to write the first time, with a significantly
   shorter debug and QA cycle.  Granted, we did this with a framework we
   developed in-house that fit our needs, but we've shown that JavaScript
   can be used to deploy and maintain a large code base.    I think a lot
   of people hate on JavaScript because they don't understand the sheer
   power of prototyping.  There are a ton of things that you can do in
   JavaScript once you understand just how dumb (and, by nature,
   powerful) the prototype model is.  It's a refreshing change from the
   object-oriented models of most C-based languages, and makes some
   problems really easy to solve.


Posted by bi on 2007-12-30 at 00:37. 

::

   Huh? I thought that, among other things, Yegge made a very reasonable
   point: people keep talking about using the best software maintenance
   techniques to deal with 500k lines of code, but do you really
   <em>need</em> to have 500kloc in the first place?    I'm not sure what
   the analogue is here to Titus's example. Well, maybe it's this:
   Suppose you want to write a simple "Hello world" program, and your
   development and/or production machine isn't even powerful enough to
   run a Python interpreter. Should my system "Requirements" include
   having upgraded machines that can run a Python interpreter which can
   then run "Hello world"?

