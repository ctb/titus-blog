Intermediate and Advanced Software Carpentry with Python
########################################################

:author: C\. Titus Brown
:tags: python
:date: 2007-02-28
:slug: intermediate-software-carpentry
:category: python


I have been asked to submit an outline for a three day course on Python, for
~20 scientists who already know basic Python.  On fairly short notice, I came
up with the following; what am I missing?  (I plan to make the course materials
publicly available, of course.)

(Note that I was explicitly asked about teaching IDLE.)

Outline
=======

Three days: plan for three hours instruction, three hours hands-on, plus
breaks.

Day 1
-----

Goal: Ensure that participants understand how to build re-usable Python
      code & design for re-use and maintenance.

Straight Python:

 * building Python programs and laying out packages
 * writing for reusability
 * maintaining Python codebases & testing
 * advanced features of the Python language
 * a brief intro to extending Python with C/C++

This day will be devoted to exploring people's knowledge about Python,
and can be adjusted dynamically to provide more basic or more advanced
information.

Day 2
-----

Goal: Introduce participants to the variety of (excellent!) tools for
      working with Python, esp in science.

Tools

 * Wrapping C/C++ code automatically
 * NumPy/SciPy
 * Rpy, matplotlib: tools for plotting
 * UNIX tools to help you develop and collaborate: screen, VNC
 * IDLE/IDEs
 * Centralized and distributed version control 
 * Trac project management
 * IPython interactive Python interpreter

This day will explore the variety of tools for effectively working
with and reaching out from Python.

Day 3
-----

Goal: Provide hands-on experience with automatically producing static
      and interactive views of your data and analysis results.

Databases, data analysis, and data presentation

 * Storing data in a structured manner
 * Built-in Python options (shelve/bsddb)
 * Using SQL
     - SQLite
     - MySQL/PostgreSQL
 * Building static HTML output
 * Building dynamic HTML output with CGI/CherryPy
 * Tying the database into your Web server
 * Testing your Web stuff

This day will introduce people to effective techniques for data storage
and presentation with Python.

(A whole day might be needed because of the variety of topics: both
HTML and SQL must be introduced!)

The menu of topics
===================

Building reusable code:

 - modules, globals vs locals, import issues
 - PYTHONPATH
 - building/installing packages: distutils, easy_install, 'require'

Testing

 - doctests, unittests, test fixtures
 - more advanced unit testing tools: nose/py.test
 - code coverage/figleaf

Simple database stuff
 
 - pickling
 - bsddb/shelve
 - SQL, sqlite, and MySQL/PostgreSQL
 - Durus/ZODB: object databases

Docstrings and automatic generation of documentation

Building Python interfaces to C and C++ code

 - writing simple interfaces manually is easy
 - SWIG, Boost.Python, SIP: examples & tradeoffs
 - C++ special stuff
 - testing C code from Python

Java/Jython

.NET/Mono/IronPython

NumPy/SciPy

matplotlib, a matlib-type Python graphing/display system

Rpy, Python interface to R

Generators, iterators, yield, list/generator comprehensions

The lesser known (but useful!) corners of the Python stdlib 

File management and APIs: how to deal nicely with paths, data files,
  etc.

Using subprocess to flexibly execute external programs.

IPython interactive Python prompt

Another way to develop: scripting with two windows

XML parsing

Generating HTML for analysis summary and presentation

The logging package: logging and py.logging

Python interfaces to MPI

Concurrency and threading in Python: threading vs fork vs...; the
   Global Interpreter Lock

py.lib sshexec, a flexible way to run programs on multiple computers

How Python is developed and how to think about backwards/forwards compatibility

IDEs: IDLE

Building simple Web servers (with CherryPy, probably?  Or CGI.)

A brief introduction to GUI development in Python.

UNIX tricks: screen, VNC

pdb, the Python debugger

Building your own types: using dicts and lists as interfaces to your own
   data; advanced dictionary use.

Version control with subversion, darcs, bzr-ng

Project, ticket, and timeline management with Trac.


----

**Legacy Comments**


Posted by Nicola Larosa on 2007-02-28 at 16:36. 

::

   A few sparse comments.    &gt; UNIX tools to help you develop and
   &gt; collaborate: screen, VNC    You may want to add collaborative
   writing tools like Gobby, SynchroEdit, and maybe web-service ones too:
   Google Docs, Writeboard, WideWord etc.    Databases: if you at all
   care about this people, don't foist the MySQL hack on them. SQLite and
   PostgreSQL are robust, free RDBMS tools.    &gt; Concurrency and
   threading in Python:  &gt; threading vs fork vs...    Ehm, what? "dot
   dot dot"? :-) You definitely need to look up your async events, and
   Twisted. :-)    Start here:    Asynchronous Programming with Twisted
   <a href="http://twistedmatrix.com/projects/core/documentation/howto/as
   ync.html">http://twistedmatrix.com/projects/core/documentation/howto/a
   sync.html</a>    Nice intro to Twisted:    Network Programming for the
   Rest of Us  <a href="http://www.usenix.org/events/usenix03/tech/freeni
   x03/full_papers/lefkowitz/lefkowitz_html/index.html">http://www.usenix
   .org/events/usenix03/tech/freenix03/full_papers/lefkowitz/lefkowitz_ht
   ml/index.html</a>    &gt; Version control with subversion, darcs, bzr-
   ng    Darcs? I thought this was about Python, right? :-)    Definitely
   add Mercurial, the little unknown Python jewel of the distributed
   VCSes.    I would add a mention of Buildbot, for usefulness, and of
   Pygame, just for fun. :-)    That's all, I hope it's useful.


Posted by Titus Brown on 2007-02-28 at 17:20. 

::

   Thanks, Nicola ;)


Posted by tim head on 2007-02-28 at 18:24. 

::

   Hi    sounds like a lot to take in in three days. How much python do
   these people already know?    I am forever wondering about proposing a
   plan to introduce a course in python for first year undergraduates at
   my university. There seems to be a few people willing to listen(even
   to an undergraduate) when they use strong words to describe the
   current teaching when it comes to computing.    As I lack experience
   in teaching I am wondering what things one can show to
   "newbies"(almost no programming experience) which will impress them so
   that they will leave with a grin on their face thinking "hell yeah,
   lots more coffee breaks if i master this python snake" and not "jeez,
   computers are for nerds". So what kind of examples would you suggest?
   Any experience with infecting new people with the python bug?      tim
   ps: beware of stalling when using subrocess() ;]]


Posted by Steven F. Lott on 2007-02-28 at 19:05. 

::

   I'd suggest two alternatives for day 3:    Either an .HTML, .CSS, .JS,
   Cherry-Py web server session    OR     SQL, SQLAlchemy session.
   Both is likely to be too ambitious.  You can take the class' pulse and
   pick a direction during the day 2.  If you can't get a consensus, then
   ignore the whiners and make your own decision that optimizes the time
   of the people who are most likely to benefit the most.    The HTML and
   CherryPy stuff is already a full day of "this is a web server", and
   the subtleties of HTTP.  I find that "experienced" programmers are
   always grumpy about the inherent limitations of HTTP -- I have to
   spend a half-hour on the various "wouldn't it be better" conversations
   that I have to terminate abruptly with "write you own standard if
   you're so smart!"    The best practices for structuring a CherryPy
   application, handling GET/POST and well-designed URL's,
   authentication, authorization and the basics of a minimally usable web
   application is a full day.    The SQL stuff, similarly, has to cover
   SQL basics (it's another language, after all), and how to embed those
   features in DB-API and SQLAlchemy structures.  You'll spend an hour on
   the object-relational impedance mismatch and the ways that you have to
   solve it "manually" and with SQLAlchemy.


Posted by Titus Brown on 2007-02-28 at 19:25. 

::

   Tim,    no proven experience on "infecting" with the Python bug.  I've
   been told that this will be a class for people who already know basic
   Python quite well.    I may be able to tell you more in a year or
   two...    Steven, I'm basing this curriculum on the intended audience,
   which is "scientists".  They tend to be **very** smart, capable of
   dealing with lots of conflicting ideas, and motivated almost
   completely by the desire to simply get something done.  They won't be
   writing Web apps for external use.  Likewise, most of their data work
   can probably be done using shelve, and the rest with simple SQL stuff;
   I don't think they need a theoretical introduction to any of it.  They
   can learn what they need to know once they're motivated to do so, much
   like I have always done.    Or, at least, that's what I think ;).
   cheers,  --titus


Posted by John Tannahill on 2007-02-28 at 20:40. 

::

   Titus,    It looks like this is a great way to get valuable input on
   what our course should cover; keep up the great work!    John


Posted by Scott Lamb on 2007-03-01 at 10:43. 

::

   You're missing performance. I don't know how much of it you can fit
   into a three-day course, but it's something scientific computing
   people will care greatly about. Profiling tools (hotshot), psyco, even
   when to convert an inner loop to a C extension.


Posted by Lee on 2007-03-01 at 10:58. 

::

   I apologize if this is obvious, but I found this to be a great
   resource:    <a
   href="http://www.swc.scipy.org/">http://www.swc.scipy.org/</a>    Here
   is more background on that book (sorry for the godawful URL:    &lt;a 
   href="http://www.computer.org/portal/site/cise/menuitem.92a12adebee187
   78161489108bcd45f3/index.jsp?&amp;pName=cise_level1_article&amp;TheCat
   =1001&amp;path=cise/2006/v8n6&amp;file=tech.xml&amp;;jsessionid=Fm2rTW
   sJDnGhbGH0MpWxv7WWwZ1nr305LgNtG48dkw4NKyV2pfz7!1917851032"&gt;http://w
   ww.computer.org/portal/site/cise/menuitem.92a12adebee18778161489108bcd
   45f3/index.jsp?&amp;pName=cise_level1_article&amp;TheCat=1001&amp;path
   =cise/2006/v8n6&amp;file=tech.xml&amp;;jsessionid=Fm2rTWsJDnGhbGH0MpWx
   v7WWwZ1nr305LgNtG48dkw4NKyV2pfz7!1917851032&lt;/a&gt;


Posted by Steven F. Lott on 2007-03-01 at 13:44. 

::

   Most of my time is spent teaching new technology to already
   experienced programmers.  While smart (not research-scientist smart),
   they have their biases.    Client-server anything (web or database) is
   often a show-stopper.    Client-Server means several things that will
   irritate inexperienced programmers.    1.  They don't "control" the
   other side of the relationship.  Writing a web server means you don't
   control the browser.  Writing a DB client means you don't control the
   DB server.  Theoretical foundations aren't the issue, basic pragmatic,
   "What is going on here?" takes considerable classroom time.    2.
   There are these "protocols" involved.  Most net protocols are
   pleasant, but irrelevant answers to bar-bet trivia questions.
   Suddenly ODBC, DB-API, HTTP, WSGI become serious.  Indeed, until you
   embark on client-server programming, you never really understand
   "protocol" and when you do, it's a shocker.  Again, theory isn't the
   issue, the pragmatic topics of "why doesn't it do that?" have to
   morphed into "here are the design patterns for implementing X with the
   established protocols."    3.  There are the other languages involved.
   HTML, CSS, SQL, etc. muddy up the waters seriously.  It's hard to
   gloss over SQL issues by saying "Here's a 'typical' SELECT statement"
   and leaving it at that.  It leaves them relatively unprepared.
   Let's try to spend a half-hour on basic client-server, and the
   essential protocols that make it work.  You then have about an hour on
   the foreign language so you can spend an hour on the Python side of
   things.      I'm not sure you can cover a useful overview of the
   SELECT statement in an hour, much less cover some common database
   design patterns in the remaining hour.    Perhaps, I'm too close to
   this, but when I teach database classes, I have to spend about 4 hours
   (lecture + exercises) on SELECT alone.  The rest of SQL is another 4
   hours.  Then we can spend the remaining 24 classroom hours on
   programming.    What I find is that the computer-sciency types are
   comfortable switching languages because they work at a higher level of
   abstraction and then implement in the tools at hand.    Much of the
   rest of the world cuts and pastes example code, and can't be bothered
   to work through the problem using the hard-to-master technique of
   "abstraction".      Having broken the world into two camps, of course,
   I've simplified your scientists out of existence.  You know them
   better than I do.  However, I raise the flag around anything client-
   server as being too complex for a half-day introduction.

