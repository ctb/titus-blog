Learning Python as a CS Professor
#################################

:author: C\. Titus Brown
:tags: python
:date: 2006-11-30
:slug: python-intro-cse
:category: python


Here's a (slightly edited) message from Bill Punch, a professor at MSU
who is hoping to transition their Intro CS class over to Python.  I
would appreciate your thoughts and comments, both on his questions and
my responses!  (I do have permission to post it, in case you're
wondering. ;)

(Just in case you're thinking about being unfriendly or snarky, please
do keep in mind that the friendliness of the Python community is
legendary, *and* we *really* want Python to be taught to CS students...
so don't be unfriendly or snarky.  Or else the PSF will hunt you down
and ... well, let's just say that you may end up programming in Perl for the
rest of your life.)

Bill sez:

"""

So I'm pushing ahead with the transition to Python and trying to see how
it fits with the courses we have here. I've hit a couple of snags (as
you might guess) and I wondered what the general opinion is.

1) The concept of class in python is not what I expected. You can do
some things there that would be hard for C++ people (or other OO
approaches, smalltalk, clos, java, ...) to take. You create instance
variables by assignment, say in an __init__. They are then local to the
instance namespace/dict and always public (never private). After that,
an instances is just another data structure, nothing special. You can
just assign new instance variables to that instance, independent of the
class definition and of any other instance of that class. You can also
just assign a new "class" variable to a class, independent of the def'n,
and it will show up in all instances.

I know this is a result of the namespace lookup, which is how classes
are implemented, but this is really different. Is the use of __slots__
popular to prevent this sort of thing? What do other "language people"
think of this approach?

2) We have typically had trouble teaching pointers to students. They
seem to relate better to standard variables (that have both an address
and a value). However, everything here is a pointer. Whether an
assignment change is local or not depends on the type being assigned
(mutable or non-mutable), since everything potentially is a reference.
Is that a tripping point for people? Do new students pick that up easily?

3) No real overloaded functions in python, at least not in the standard
C++ sense. That is, there is no overloading a function on argument types
(since there are no typed variables) or on number of arguments. Each def
is a statement and the last one run is the one that holds (no multiple
functions with the same name but different argument lists). However,
they do overload in that the operation performed by the function depends
on the type of the arguments. That is, a function "plus" that adds two
arguments does integer summation on two ints, but concatenation on two
strings. Thus you have to know what you are passing in (and what is done
to it) to have an expectation of knowing the result. Is that clear to
you? Seems confusing to me. I expect to know (in a C++ sense) what is
going in and what is coming out, and if I don't get that right then the
program/complier complains. Here, you pass the wrong args (you meant
ints, you passed strings) and it works fine, just not what you expect.
Seems less simple to me, is that right?

"""

My response:

"""

You actually *can* make variables private by naming them with a __ in
front.  (Don't do this.)

And remember that inheritance etc. all works properly in this, so it's
not quite as simple as "oh, it's all just a namespace" -- it's actually
a chained namespace with multiple inheritance ;).

(I can blow your mind with metaclasses later.)

__slots__ is intended *only* for optimization; see

	http://www.dalkescientific.com/writings/diary/archive/2006/03/19/class_instantiation_performance.html

(search for 'The fastest approach uses ')

I focus on the design in OO programming more than on the constraints.
Once I let go of the idea that I could dictate what code is publicly vs
privately vs "protected"ly accessible to subclasses or external code,
I don't think I ever looked back.  After all, it turns out that most
people aren't very good at designing class hierarchies in reality, so
why overly constrain what people can do with them by designing the
constraints in "up front"? (There's some good writing about this
approach in Richard Gabriel's book on Patterns.)

If it's really critical for a particular problem, there are a couple of
approaches.  For one, you can use properties to make read-only
variables: ::

   class A(object):
      def get_p(self):
         return 5
      p = property(get_p)

   a = A()
   print a.p   # calls 'get_p'

   a.p = 6     # raises error

You can also override __getattr__ and __setattr__, but properties are
the recommended way to do it.  See

	http://www.python.org/download/releases/2.2/descrintro/

for waaaaaay too much information.

For (2), 

Yes, I have a tough time explaining this in my head, but then again I
learned to program in C and I unashamedly use pointers ;).

First, I'd go with 'pass by reference' instead of pointer, although they
mean roughly the same thing.

Second, I may be missing something, but aren't assignments ALWAYS local? ::

  def f(a, b, c, d):
     a = 1
     b = SomethingElse()
     c = 'str'

  a = 2
  assert a == 2
  f(a, b, c, d)
  assert a == 2

I would distinguish arguments by whether or not the argument is mutable.
For example, in ::

   def f(a, b, c):
      a = a + 1
      b += "hello"
      c['x'] = 'test'

   d = dict(x='yo')
   f(5, "world", d)

you wouldn't expect '5' to suddenly become '6' simply because you added
one to it, right?  Nor does "world" become "worldhello".  That's because
they are immutable types that are passed by reference but any operation
on them returns an entirely new immutable type.  However, d['x'] does
become 'test', and doesn't stay as 'yo', because you're passing the dict
as a mutable type.

I haven't really thought this through, tho, so let me know if you run
across counterexamples...

My experience has been that new programmers don't get too confused by
this, but that's probably because they don't know C++ ;).

For (3),

I think the concept is known as "duck typing", as in "if it looks like a
duck, and acts like a duck, we should probably treat it like a duck."

Bruce Eckel has written a lot on it; here's one google'd post:

	http://www.mindview.net/WebLog/log-0053

You might also be interested in reading Guido van Rossum's thoughts,

	http://www.artima.com/weblogs/viewpost.jsp?thread=85551

and esp the comments which can at least give you a flavor of the
discussion in the larger python community:

	http://www.artima.com/forums/flat.jsp?forum=106&thread=85551

In practice, the way it's implemented is that each type has its own
__radd__ etc. operators that "know" how to deal with its type.  If you
want to confuse the heck out of people (but make it consistent with your
own C++ knowledge) point out that

        a = a + b

actually can be written

        a = a.__radd(b)__

So as long as you choose your operators wisely, then it all makes sense.

On all of these issues, I would say that it's simply a matter of habit.
I find C++ frustrating at this point, because it doesn't easily let me
do things with lists and strings that I'd *like* to be able to do, like
unpack them intelligently, e.g.

   x, y = y, x

to swap two variables.

HTH!

"""

Thoughts?

If you're posting comments, please note that I need to approve you if you're
a first time poster -- so your comments may take a bit to show up.  Sorry
'bout that.

--titus


----

**Legacy Comments**


Posted by Michael Bernstein on 2006-11-30 at 03:17. 

::

   Regarding the lack of function overloading and typeless args to
   functions, this is Python's automatic implicit polymorphism.    The
   right thing to do in Python (assuming that your code does actually
   care about the type of the arg being passed) is to test for the type
   of the arg value (or for the presence of a relevant method on the arg
   value) in the function itself.    So, instead of creating multiple
   copies of a function with different arg type signatures, you create
   the function once, and add some conditional code to disambiguate the
   cases or to throw an exception if the 'wrong' type is passed.


Posted by Fredrik on 2006-11-30 at 05:32. 

::

   "Whether an assignment change is local or not depends on the type
   being assigned (mutable or non-mutable)"    As you notice on your
   reply, this isn't really true.  A **plain** assignment (name =
   expression) only copies the reference; it never copies (or otherwise
   modifies) the object.  If you do a plain assignment, id(name) usually
   changes.    Things like "name.attrib = expression" and "name[index] =
   expression" and "name.method(expression)" are all method calls, and
   can do whatever they want.  If you do any of these, id(name) **never**
   changes.    Augmented assignment is a bit confusing, though, because
   it can result in either a plain assignment (new id) or a method call
   (same id), depending on what "name" refers to.  If you write "name +=
   expression", Python checks if the the object identified by "name" has
   the right method (<em>_iadd_</em>).  If the method exists, it can do
   whatever it wants, and whatever it returns is assigned to "name".  If
   the method doesn't exist, Python treats the expression as if you'd
   written "name = name + expression".


Posted by Big Ray on 2006-11-30 at 08:27. 

::

   For myself, I think Python has made it easier for me as a programmer
   to get used to the concepts of pointers, and object oriented
   design/programming. I also totally agree with you about the built-in
   constraints on class design.     Ok, I'm done jocksniffing now. Good
   post.


Posted by Marius Gedminas on 2006-11-30 at 09:31. 

::

   +1 for all answers.    One nitpick: a + b maps to a.<em>_add_</em>(b).
   If a doesn't support <em>_add_</em>(b) (i.e, if it returns
   NotImplemented), but b does, then a + b maps to b.<em>_radd_</em>(a).
   <a href="http://docs.python.org/ref/numeric-
   types.html#l2h-258">http://docs.python.org/ref/numeric-
   types.html#l2h-258</a>


Posted by Daniel Arbuckle on 2006-11-30 at 10:12. 

::

   1) You seem to be worried that the Python object system is too
   flexible, due to the ability to alter classes and instances at
   runtime. I ask you to consider on what basis you consider the 'A is-a
   B' relationships represented by inheritance and class membership to
   imply that B is structurally immutable, or that it completely defines
   A. I see no logical implication of those notions. I consider those
   ideas as a sign of having overadapted to the constraints imposed on
   C++ for efficiency reasons.    2) In my experience, pointers confuse
   people because they have two values: an address, and the contents of
   that address. Python's references simply don't invoke that confusion,
   in my experience. There's still room for confusion regarding the
   possibility of aliasing, but that's something that all programmers
   must come to grips with, preferably sooner rather than later.    3)
   Function overloading such as you speak of is rarely useful in Python,
   thanks to the aforementioned duck typing. If the parameters you
   receive support the protocol that you're trying to use with them, then
   your code will work. If not, an exception will be raised. Either way,
   you're in the clear. However, Python is sufficiently flexible to
   implement that functionality if you truly desire it. See for a quick
   example: <a href="http://www.artima.com/weblogs/viewpost.jsp?thread=10
   1605">http://www.artima.com/weblogs/viewpost.jsp?thread=101605</a>


Posted by Xentac on 2006-11-30 at 11:19. 

::

   2) The way I always explain it to people (arguably, they're not first
   time programmers) is if the left side of the assignment is anything
   other than the variable name, you're mutating.  If there is no
   assignment, it's mutating.  If there is nothing other than the
   variable name on the left side, you're updating the reference.


Posted by Titus Brown on 2006-11-30 at 11:21. 

::

   Fredrik, Marius -- thanks!  That clears up my lingering confusion
   nicely.    Thanks to all -- very helpful.    --titus


Posted by Titus Brown on 2006-11-30 at 11:23. 

::

   (and Xentac -- just saw your comment, too!)


Posted by Karl Guertin on 2006-11-30 at 11:53. 

::

   I was at gatech through a number of CS curricula changes (pseudocode
   to Dr Scheme to jython) and I've tutored students in all three
   languages. The most amusing thing about all three languages is that
   students complain that they aren't "real" languages. This amuses me to
   no end, especially when I point out that I've made money programming
   both lisp and python.    Overall, I've found that students struggle
   with the same problems in all the languages: thinking through
   execution, learning to debug, using arrays, etc. Basically, the
   problems are almost always related to programming experience instead
   of the language itself, mostly because they aren't bringing baggage
   from another language. E.g. Scheme is actually easier for first time
   programmers than it is for novice programmers, which have to unlearn
   habits.    Before I get to your questions, I'd like to note that
   Python's philosophy on how to treat developers differs from the
   mainstream statically typed imperative languages. My favorite
   explanation is that Python is a language between consenting adults.
   Many people come and complain about the lack of private members and on
   duck typing. Python programmers have to solve the same problems solved
   by other languages, but the solutions tend to be convention over
   language enforcement.    I'll have a lot of mentions of Java, as
   that's the static language I'm most familiar with. I did take two
   courses using C++, but those were numeric algorithms courses and so
   only needed a small subset of the language. I work programming Python
   and Javascript. :]    1) The lack of private members to some people
   means that they can't do proper OO technique and hide the
   implementation behind a public interface. The Python solution is to
   write private methods prefixed with an underscore. This is the
   convention for 'this is private and subject to change' but still
   allows people to monkeypatch your code if they really need to, but you
   should realize what you're getting yourself into.    If you prefix
   with a double underscore, the interpreter name mangles the member.
   It's still not truly private and I can dig it up, so this is
   considered annoying by most python developers. The ones that are going
   to monkeypatch your code are going to monkeypatch whether you single
   or double underscore your stuff, so making people jump through hoops
   to get your name-mangled code is inconsiderate.    To be explicit,
   monkeypatching is swapping out a method in someone else's code and is
   considered bad form but necessary, hence the name. It's more accepted
   in Ruby where it's called "opening a class".    As for private fields,
   they are not necessary in Python. The standard reason for having
   accessors and modifiers is to allow you to maintain API if your
   implementation changes. Python provides this via the property()
   builtin (mentioned above). The only time explicit accessors/modifiers
   are used is when the author wants you to know that the operation is
   expensive. Further reference: 'Python is not Java'.    2) The
   reference issue doesn't usually come up until you're trying to copy
   data structures. Primitive values (int, string, etc) don't alias. When
   aliasing does become an issue, drawing the variable name boxes on one
   side and the value boxes on the other and drawing arrows between them
   is my solution. Some students (20% or so by my guess) don't get this
   and need explicit tutoring on a case-by-case basis. Once they get it,
   it is an occasional gotcha but isn't mysterious.    3) Operator
   overloading isn't in high demand because it's considered excessively
   magic (explicit is better than implicit) and I believe it's only used
   for the + operator in the stdlib. There are other libraries like
   path.py, which overrides '/' to concatenate paths, but most of the
   negative feedback about those libraries at least mentions the
   overridden operator as a bad thing. ORM layers frequently think about
   using the logical (&amp; |) operators for building SQL expressoins,
   but the precedence doesn't work correctly so almost nobody uses them
   even if they are implemented.    One comment on Duck Typing: Duck
   Typing seems like something prone to breakage. My explanation is that
   Duck Typing is like Ethernet, in theory it will break, but in practice
   it works pretty well. The key things that make it work are the lack of
   static typing and the 'better to beg forgiveness than ask permission'
   pattern where you try to do something and catch the error rather than
   checking that the passed in object has a particular attribute that you
   think is needed or is of a particular type you think you need.


Posted by Titus Brown on 2006-11-30 at 12:22. 

::

   For reference:    Python is not Java: <a
   href="http://dirtsimple.org/2004/12/python-is-not-
   java.html">http://dirtsimple.org/2004/12/python-is-not-java.html</a>
   Python Interfaces are not Java Interfaces:    <a
   href="http://dirtsimple.org/2004/12/python-interfaces-are-not-
   java.html">http://dirtsimple.org/2004/12/python-interfaces-are-not-
   java.html</a>


Posted by tch on 2006-11-30 at 15:24. 

::

   I only wished they used Python in my Intro CSE class at MSU, C++ was a
   pain in the a$$!


Posted by Commander Breetai on 2006-11-30 at 20:07. 

::

   You don't do function overloading in Python, you use keyword
   arguments. This allows you to do some things in Python that you can't
   do in Java:  <tt>  aLine = Line(xIntercept = 4.0, yIntercept = -8.2)
   bLine = Line(slope = 5.7, yIntercept = 2.3)  </tt>  Java would have
   two constructors with the same signature, Line(double, double), and no
   way to tell them apart. You have to be more verbose in your Line
   class's <em>_init_</em>() method, but it gives you more flexibility in
   the long run, I feel.


Posted by Super Mike on 2006-11-30 at 20:40. 

::

   I recommend Perl over Python for intro students. It's far more
   mainstream and provides a more practical chance for students to apply
   skills in the real world right off the bat. I mean, it's not every day
   you hear about Python tasks as much as you do Perl tasks. Python does
   have its advantages, yes, but I was just wondering if you haven't
   considered Perl and why. My favorite language in business intranet web
   apps is PHP, but I can understand that more academic types would
   prefer Perl over PHP because of its academic lean. And moving from
   Perl to PHP is not a huge leap in learning, so there's another
   advantage right there. Starting with Java, I will admit, is not the
   right strategy -- it's way, way too hard. It also requires a grasp of
   strict data typing and it gets annoying to have to compile code all
   the time in order to run it. I'm not a fan of teaching CS 101 to these
   youngsters without a scripting language like Perl or PHP.


Posted by Titus Brown on 2006-12-01 at 01:15. 

::

   Hi, Super Mike,    I programmed in Perl for many years before picking
   up on Python, and I very much disagree (as you would expect!)
   Python is pretty mainstream from my perspective and it's used for a
   number of large applications -- unlike Perl.  Perl is used for a lot
   of scripts, but I think it's much trickier to organize large
   applications with Perl than with Python.  There are quite a few
   companies that explicitly hire Python programmers, so I don't think
   there's any lack of practicality in teaching Python over Perl.    I
   was a bit surprised myself at MSU's interest in teaching Python.
   We'll see if it holds up over time, as they learn more about it ;).
   As for PHP, the goal is to teach general purpose programming, not Web
   programming.  PHP is finely tuned for Web programming but is not a
   particularly good general purpose language, unlike Perl, Python, Tcl,
   C++, etc.    cheers,  --titus


Posted by Kent Johnson on 2006-12-01 at 10:10. 

::

   To some extent the concerns in 1) and 3) are concerns about working
   with a dynamic language. I would say, "Yes, you are right, but it is
   not a problem in practice." Coming from a background of static
   programming languages like C++ or Java it's hard to understand the
   value of the freedom that Python gives you, it looks more like a
   problem than it actually is. Tell Prof. Punch, "Try it, you'll like
   it!" :-)


Posted by Christopher Warner on 2006-12-01 at 14:03. 

::

   Decided to jump into Python after I kept running into people
   exacerbating its praises. One of the first things that annoyed me was
   that it is a formatted language. Meaning I had to precisely indent the
   code I wrote. However, after getting past that it has been easy going.
   My general background is doing stuff in C/C++ or Perl and looking back
   I wish during my intro classes in school python or even perl would
   have been used instead. Primarily because it allows one to do certain
   things inefficiently and to gain from learning how to make those
   things efficient. Too many times I found myself doing other peoples
   work because they couldn't understand pointers or they just couldn't
   logically understand why making things certain objects didn't make
   sense. At least these problems for your students will show up in the
   code that they may actually complete on their own. Some of them will
   at the very least properly complete assignments even if it's done
   incorrectly. So number three I see as a chance to help those students
   who don't understand but you'll be able to identify them which is
   better than just waiting until giving a major project or asking them.
   As far as object orientation goes I'd recommend solid background and
   reading on what the whole thing is about. Developing a method and
   design to identify and use objects. I've been in too many lectures
   where professors start going on about object orientation and how
   everything is an object instead of explaining a system and identifying
   objects where a specific method can be applied. The examples used
   always seem to have so many parts instead of simple everyday systems,
   keeping the system confined to a certain number of actors. This way
   you don't have students who are thinking everything needs to be an
   object and who concentrate more on the design of said program.

