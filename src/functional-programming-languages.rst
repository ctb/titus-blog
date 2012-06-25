Which functional programming language(s) should we teach?
#########################################################

:author: C\. Titus Brown
:tags: python,msu,cse
:date: 2010-06-24
:slug: functional-programming-languages
:category: misc


Laurie Dillon just posted the SIGPLAN eduction board article on `Why
Undergraduates Should Learn the Principles of Programming Languages
<http://mt4.acm.org/educationboard/2010/06/why-undergraduates-should-learn-the-principles-of-programming-languages.html>`__
to our faculty mailing list at the `MSU Computer Science department
<http://www.cse.msu.edu>`__.  One question that came up in the ensuing
conversation was: what functional programming language(s) would/should
we teach?

I mentioned OCaml, Haskell, and Erlang as reasonably pure but still
pragmatic FP languages.  Anything else that's both "truly" functional
and used somewhat broadly in the real world?

thanks!

--titus


----

**Legacy Comments**


Posted by Paul Moore on 2010-06-24 at 15:48. 

::

   One interesting option might be clojure (http://clojure.org/). It's a
   functional lisp (all values are immutable, data structures are
   persistent) hosted on the JVM (so interoperability with Java and all
   its libraries is easy) which makes writing usable "real-world" code
   practical in a course setting. While clojure itself is fairly new and
   hence not widely used, it seems to be catching on fast, and the JVM
   infrastructure is certainly widely used (!)    Check for yourself -
   I've only just discovered clojure so my knowledge is somewhat limited
   - but it's at least worth a look.


Posted by Jeff Kowalczyk on 2010-06-24 at 16:20. 

::

   Clojure could be included in that list of pragmatic FP languages. It's
   younger than the others, but mature enough for production work.
   Clojure targets the JVM, making it directly usable in many corporate
   environments.


Posted by Pierre on 2010-06-24 at 16:20. 

::

   Not only functional (object too) but I would suggest Scala as well.
   On the same line, I like F# too. But it is less used that scala is
   afaict.


Posted by Daniel Nilsson on 2010-06-24 at 17:00. 

::

   I'd vote for Haskell, being pure and having a clean syntax makes it a
   great language for teaching FP.


Posted by Nathan Gray on 2010-06-24 at 18:10. 

::

   Why would you want to teach your students something so useless as
   functional programming?    Just kidding.  :)    Erlang has a lot going
   for it in terms of innovative treatment of distributed computing, but
   I would lean towards something with a Hindley-Milner style type
   system.  Until you've been exposed to H-M you don't really know what
   modern type systems are capable of.  But then again, I'm talking to a
   Pythonista so this line of argument might not get me very far.  ;^)
   I'm partial to OCaml in my own work, as you know, but it seems like
   Haskell is the hotness in FP circles.  Scala and F# are very appealing
   languages, but they have the disadvantage that you end up needing to
   understand an unrelated technology (Java or .NET) to really understand
   the language.


Posted by George on 2010-06-24 at 20:25. 

::

   Honestly, none of them is used broadly (at least with any reasonable
   definition of "broadly") as a simple search on any job site shows. In
   relative terms, currently Erlang has the most momentum and real-world
   success stories (ejabberd, RabbitMQ, Couchdb, Riak and of course
   Erickson) so that would be my first choice. Clojure seems to have some
   potential for the future but it's too early to declare it as "the next
   big thing" for now. As for Ocaml and Haskell (or for that matter
   Common Lisp, Scheme and friends), they'll always have a small core of
   enthusiasts, academics and hobbyists extolling their purity, superior
   type system or other more esoteric virtues but I don't think they'll
   become significantly more relevant than they are now, 20+ years after
   they first came out.


Posted by James Thiele on 2010-06-25 at 00:03. 

::

   Don't worry about which languages are "used somewhat broadly in the
   real world". Teach whatever FP language you think gets the concepts of
   FP across.


Posted by Olaf Lenz on 2010-06-25 at 08:42. 

::

   In my time (but that is already a bit ago), it looked as though
   Concurrent Clean (see <a
   href="http://clean.cs.ru">http://clean.cs.ru</a>.nl/) was a cool
   language with a future. I don't know whether the future caught on,
   though.


Posted by matt harrison on 2010-06-25 at 09:39. 

::

   Go with lisp.  If they are interested in learning something practical
   they should be able to pick it up later.  (I'm surprised that there
   are CS degrees that don't expose students to FP....).      If
   practicality is a concern, you'd only teach java and c#.....


Posted by Ben on 2010-06-25 at 10:08. 

::

   I'd honestly use Python, or some multi-paradigm language like it. You
   start with an imperative implementation and move parts of it very
   naturally to functional idioms, and finally move almost entirely to
   FP.    You can go from for a in range(0, 10): l.append(a * 2) to [a *
   2 for a in range(0, 10)], and immediately you have transitioned from a
   for-loop to a list comprehension.    That smooth transition is also
   important, I think, in learning. Say you give someone an assignment in
   FP. And you have an enterprising student who is able to do 95% of the
   problem using only functional idioms. With a language like Python, he
   can hack the last 5% together using imperative idioms and get it
   running, which provides a huge amount of motivation to keep going.
   Moreover, he can then come back and you can see, through his code,
   what his mental model is and show him how to close the gaps.


Posted by Pete Hunt on 2010-06-25 at 10:18. 

::

   I'd suggest something from the ML family, or Scheme. Haskell is
   probably too much as an introduction to functional programming. I was
   able to learn Standard ML as an undergrad relatively quickly and I
   thought it was very cool, and Scheme is sort of the canonical
   functional programming teaching language, except it doesn't teach a
   modern type system.


Posted by Rich on 2010-06-25 at 10:35. 

::

   I'm interested in FP for teaching many-core programming to CS majors.
   (I understand that Erlang has gained traction in distributed
   processing.)  So, my question is whether one FP approach makes many-
   core programming easier or are they somewhat equivalent in that
   sphere?


Posted by Steve Rogers on 2010-06-25 at 10:39. 

::

   Racket (formerly known as PLT Scheme) gets my vote.  It's reasonably
   functional and practical, and has a good collection of batteries
   included.      <a href="http://racket-lang.org/">http://racket-
   lang.org/</a>


Posted by Titus Brown on 2010-06-26 at 16:56. 

::

   Thanks, all!  Very helpful.    To those who are supportive of teaching
   theory with no regard for pragmatism (Matt, James) I personally
   believe that it's more interesting and informative to teach a language
   that's used for more than teaching or academia.  You don't really see
   the tradeoffs inherent in languages until you try to **use** them for
   something, and simple math or logic problems are very different from
   writing actual code.  Certainly that's been my experience.    You
   should also realize this will generally be the **only** exposure these
   undergraduate students will have to FP concepts; many of our students
   go on to industry and not grad school.  So it seems like a good idea
   to expose them to something that might actually be useful.


Posted by Titus Brown on 2010-06-26 at 17:10. 

::

   Oh, and also, Matt -- we've moved away from requiring the kitchen sink
   in a CS degree.  CS is very broad and other than core competencies
   (data structures and algorithms, software design and engineering,
   discrete math, etc.) we try to offer options.  These options are
   necessarily limited by the number of faculty we have to teach, also...
   Hence the discussion in the department about FP.

