Strangling Your Code and Growing Your Test Harness: The 9 Phases of Building Automated Tests Into Legacy Code
#############################################################################################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2007-03-30
:slug: strangling-your-code
:category: python


I'm in the early throes of building tests into my `Cartwheel
<http://cartwheel.idyll.org/>`__ project.  Cartwheel was one of the
two projects that inspired my Web testing project, `twill
<http://twill.idyll.org/>`__, so naturally I'm happy to finally be
putting twill to good use in my *own* projects.  Naturally the
transition from building tools for building tools, to actually using
the tools to build a tool, is a bit painful: I can't be *general* any
more, now I have to be *specific*.

The process I'm going through right now is appropriately referred to
as `Strangling Legacy Code
<http://www.stickyminds.com/s.asp?F=S9705_MAGAZINE_2>`__, in this case
by `Growing A Test Harness
<http://www.developertesting.com/archives/GrowYourHarness.pdf>`__
(both great articles).  Leveraging the power of nose directory
hierarchies, I'm slowly growing my setup/teardown code to cover more
and more functional testing scenarios, which in turn exposes more
scenarios to test.  While it's an endless-seeming process, I think I'm
at the inflection point where I've now automated more than half of the
testing tasks for the Cartwheel Web server.  Note that I'm by no means
*testing* even 50 percent of the functionality, but what remains is
relatively specific and accessible to testing by very small increments
in my testing code.  Given my general time constraints, I'm going to
switch my focus to testing newly written code and writing automated
tests for reported bugs; down the road I'll probably use coverage
analysis to figure out what large masses of untestedness lie hidden in
my codebase.

Looking back and prognosticating forward, I'd divvy the process up into
N steps:

 1. Shock.  (How the heck do I start testing this sprawling mass of code??)

 2. Hello, world.  (Hey, look at that, I've got a basic import working in
    my automated tests!)

 3. Fixture code sucks.  (Oh, gawd, I've got to automate setting *that* up,
    and *that*, and *that*...)

 4. Fixtures *rock*.  (Wow, look at what I can test now!)

 5. Over the hump.  (Where I am now.)

 6. What lurks beneath?  (Using coverage analysis to find large areas
    of untested code.)

 7. Relaxing.  (I've got XX% of my code covered with some kind of automated
    test!  Hooray!)

 8. Reaction.  (Hmm, guess I'm not actually testing for *that* specific bug...)

 9. Goto 7, increment XX.

 10. Asymptotically approach perfection.

Regardless of the steps ahead, it feels good to be at stage 5...

--titus


----

**Legacy Comments**


Posted by Ben Finney on 2007-04-01 at 20:29. 

::

   One of the good things I find about writing unit tests is that I am
   encouraged to make all external dependencies parameterisable. In other
   words, the code should **not** expect to be able to make loads of
   calls directly to the database -- it should instead accept a single
   object which encapsulates that functionality, and defer all database-
   specific stuff to that object.    That way, when I'm unit-testing that
   code, I just pass in an easy-to-set-up mock database object, which
   reacts predictably, instead of having to somehow automate the setting
   up of external things.    This is the same for whatever externality
   you find troublesome in your fixtures. If it's a lot of effort to set
   up for the purpose of a test, that's a bad design smell. Your code
   needs to be refactored so it isn't so tightly coupled to that external
   thing, and can be more easily unit tested. You'll find that each unit
   of code incidentally becomes much simpler in its interface as a
   result.


Posted by Titus Brown on 2007-04-02 at 12:37. 

::

   Well, yes and no.  I'm explicitly doing **functional** testing, not
   unit testing; I find functional testing more useful for Web sites.  In
   particular, the complexity in this application has more to do with the
   information communicated via the database (by several different
   processes) than it does with the code sitting between the database and
   the Web site.    Were I doing strict unit testing, I would indeed
   decouple things and mock the database more, although I also think that
   encapsulating a large data model in an easily testable object is ...
   difficult and dangerous to do on the cheap.  So I'd have to really
   expect a big benefit from it before I'd start down that road.    As it
   is, now that I **have** the fixtures, life is quite good ;)    cheers,
   --titus


Posted by Ben Finney on 2007-04-02 at 21:02. 

::

   Yes, you're right that my comment was in the context of unit tests.
   Higher-level, whole-application testing has different tradeoffs.

