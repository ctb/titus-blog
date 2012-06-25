Perl programmers are from Mars, Python programmers are from Venus
#################################################################

:author: C\. Titus Brown
:tags: python
:date: 2006-11-22
:slug: i-just-dont-get-it
:category: python


Here's my dirty little secret: I read `PlanetPerl <http://planet.perl.org/>`__.

I do so for a couple of reasons.  First, there are a number of good programmers
that post through it.  Second, I'm easily amused by any discussion of Perl 6.
And third, occasionally my mind gets boggled.

Take, for example, `Ovid's post
<http://use.perl.org/~Ovid/journal/31672?from=rss>`__ on the `MIT
switch to Python <http://www-tech.mit.edu/V125/N65/coursevi.html>`__.
The primary post itself is silly enough -- Guido doesn't like lambda,
so Guido has serious limitations in his thought process, so Python is
a lousy language -- but some of the comments are even worse, IMO.  The
comments boil down to "programming is hard, so we should make programs
hard to read". I herewith retaliate: ::

   Debugging is twice as hard as writing the code in the first
   place. Therefore, if you write the code as cleverly as possible,
   you are, by definition, not smart enough to debug it.

       --Brian W. Kernighan

I wholeheartedly agree with the `SICP statement
<http://weblog.raganwald.com/2006/10/irony.html>`__ that "Programs
must be written for people to read, and only incidentally for machines
to execute."  I don't really see any irony in SICP containing this
statement, either; programmers *should* know basic math and lambda
calculus, I think, but that's different from making your programs
hard to understand.

In fact, my personal programming motto has become "strive for
simplicity", because simple code is both easy to read and easy to
test, and therefore has a higher probability of being both correct and
maintainable.  Your mileage will not vary.

--titus


----

**Legacy Comments**


Posted by Reg Braithwaite on 2006-11-22 at 15:22. 

::

   Thanks for the link love! I'm looking forward to reading more
   dispatches from the Ivory Basement...


Posted by Sean McGrath on 2006-11-22 at 16:09. 

::

   That Kernighan quote is a gem! I hadn't come across it before.    Sean


Posted by wow on 2006-11-22 at 17:36. 

::

   "Here's my dirty little secret: I read PlanetPerl."    This is one
   pure instant of time where the acronym LOL took all its glory. I
   really laughed out loud. You said this like a "coming out", like
   there's some deep secrets stuffed in the reason you read planet perl.
   The secret of Brokeback Python.


Posted by Titus Brown on 2006-11-22 at 18:56. 

::

   I'm not sure reading PlanetPerl is acceptable behavior for a Python
   dogmatist ;)


Posted by Jules on 2006-11-24 at 13:35. 

::

   And therefore, we shouldn't make it harder by not using lambda (which
   is used A LOT in SICP).


Posted by Ian Bicking on 2006-11-25 at 01:28. 

::

   "And therefore, we shouldn't make it harder by not using lambda (which
   is used A LOT in SICP)."    Maybe the MIT guys were tired of people
   confusing functional programming with the term "lambda"?  Ovid's
   original comment shows quite a bit of confusion towards what they were
   getting at in SICP -- which is something you construct with "lambda"
   in Scheme and "def" in Python.    Though in the same way some
   Pythonistas can be just as confused about the lack of first class
   functions in Ruby -- since really the important thing is the ability
   to pass around code, which Ruby can do just fine even if it is awkward
   to pass "functions"... the same issue with confusing syntax with
   semantics.


Posted by Ovid on 2006-12-18 at 20:08. 

::

   I will freely confess that I am neither an expert in  Python or the
   lambda calculus, so if someone can provide concrete examples of why
   Python's lambda function is not broken, I'd welcome that.


Posted by Ovid on 2006-12-18 at 20:16. 

::

   What I forgot to mention is that there are other reasons why I
   disagree with some of Guido's approaches, but it would take me too
   long to describe here.  Suffice it to say that on use.perl I was
   "preaching to the choir", but I keep forgetting that there are many
   outside the "choir" who read use.perl, so I really need to be more
   descriptive in  what I say.    That being said, I think Guido is
   brilliant and I really like what he's done with Python and my quibbles
   are minor.  It's a "six of one, half dozen of the other" situation for
   many issues.

