What are the 5 best "hidden gem" stdlib modules in Python?
##########################################################

:author: C\. Titus Brown
:tags: python
:date: 2007-11-16
:slug: hidden-gems-in-stdlib
:category: python


Calling all Pythonistas,

What is your personal list of "modules you love and hate" -- stdlib
modules that you use all the time, but that have weak documentation,
poor examples, or are otherwise difficult to use the first time?

Here are five modules that I think could use some documentation help:

 - re (hidden, maybe not -- but I always have trouble reading the docs!)
 - xmlrpclib (once you know you need it and how to use it, it's great!)
 - datetime (check out the "Examples" section!)
 - ConfigParser (no examples whatsoever!)
 - wsgiref (ditto - and who knows they need it?)

What are your five, and why?

cheers,
--titus


----

**Legacy Comments**


Posted by jesse on 2007-11-16 at 07:31. 

::

   * select  * ditto on xmlrpclib  * unittest (examples.)  * ditto on
   ConfigParser  * UserDict    More as I think of them :)


Posted by infixum on 2007-11-16 at 08:22. 

::

   datetime - I'm not going to complain about the doc; I'm just glad it's
   in the standard library.  shutil - for a newb to programming or a Unix
   based system, the name doesn't betray it's most useful functions
   (moving files - presumably shutil is an abbreviation for shell
   utility.)  csv - Really, no problem with the doc - it just took some
   adjusting after processing comma delimited text the old (prior to 2.3)
   way.  Another one where I'm just glad that it's there now.  time -
   good module, once you understand the concept of the Unix timestamp.
   Very useful.  Getting your head around Unix timestamps as a newb takes
   a little effort - explaining it to customers takes a lot.  math - I
   came from a different programming environment - it took me a while to
   figure out that these functions aren't built in (I always forget to
   import math).    All in all, using these modules taught me a good bit
   and made my code more readable.  If you're a seasoned computer
   programmer who has worked on something other than Windows, all of
   these would probably come a good bit easier.    My 2 cents.


Posted by Terry Peppers on 2007-11-16 at 09:24. 

::

   1. re :: Still to this very day, I couldn't tell you what the
   difference is between search and match. I read these docs once a week,
   it seems.    2. logging :: Never had any success using anything but
   logging.basicConfig().    3. os.path :: So many methods, so few
   examples.     4. csv :: Again with the examples. Two weeks ago I had a
   "pipe-delimited" file and couldn't figure out how to set that as the
   delimiter. Mental note - and kind of duh! - reader =
   csv.reader(open("tp_is_a_moron.csv", "rb"), delimiter='|')    5.
   pprint :: Incredibly useful, but indent, depth and width while
   mentioned don't have any examples.


Posted by Pete on 2007-11-16 at 09:59. 

::

   * SocketServer.  Actually, it never gets any easier.  You'd think
   sockets couldn't get any more complicated, but you'd be wrong.   *
   itertools.  Instead of equivalent python code, how about some
   doctests?   * wsgiref - sure, but it's not helped by the fact that the
   WSGI standard is absurdly complicated to begin with.  Yes, it's nice
   that we have a standard, but jeez, what sins did we commit in a past
   life to deserve this one?   * dbapi - not a module, but I needed to
   use it a lot before it finally sank in.   * attribute magic,
   metaclasses &amp; custom comparisons - again, not  modules and
   inherently complex, but the docs don't help matters.


Posted by John Montgomery on 2007-11-16 at 10:16. 

::

   struct I think is quite a good hidden gem.  Obviously not
   <em>always</em> useful, but it does make working with simple binary
   structures fairly easy.


Posted by Derek on 2007-11-16 at 12:20. 

::

   I wrote out an example for just about every kind of functionality in
   ConfigParser while trying to learn how to use it. It's amazingly
   useful. I guess I need to add those to the wiki.


Posted by Doug Winter on 2007-11-16 at 12:32. 

::

   urllib2 is very useful, but really hard to use and poorly documented.
   The logging package is fantastic, but utterly impenetrable to the
   casual user.


Posted by Pete on 2007-11-16 at 14:09. 

::

   glob: This is an often used, one word answer I give to fellow
   programmers.    imp: Want to load a python module not on sys.path?
   StringIO: I wish it was a builtin type.    pprint: Must have
   traceback: The simple print functions are a simple way to log
   conditions but not raise a full exception


Posted by Roberto on 2007-11-16 at 14:11. 

::

   itertools -- a fantastic module, but with shallow documentation that
   doesn't tell you where you could use it.    bisect -- I always have to
   do some testing to remember how it works.    operator -- same as
   itertools.    mmap -- could use more documentation.


Posted by Ian Jones on 2007-11-16 at 14:37. 

::

   - xml.etree.ElementTree has no usage examples. You can find plenty if
   you know who the effbot is, but you'd never know from the module doc
   page.    - The front page of the logging module doc launches right
   into excruciating detail on its own object model, but lists no
   benefits it might have over simple 'print' statements. The basic usage
   example, which actually is useful, is buried on the third page.    As
   with xml.etree, if you were already using the package before it was
   included in the standard library (or in this case perhaps Log4J in
   Java-land), then you **might** be able to use the stdlib docs as a
   reference. But it's not helpful for people who come along later
   without that historical context.    - The unittest module, by
   comparison, carries a whiff of the same problem but deals with it
   somewhat better -- there's a little more intro material, the usage
   example is on page 2 instead of page 3, the next few pages are more
   about usage than implementation details.


Posted by Kumar McMillan on 2007-11-16 at 16:24. 

::

   The compiler module docs are pretty good but still have some "XXX"
   notes for where the docs are incomplete or possibly wrong.  Just
   thought I'd mention.  <a href="http://docs.python.org/lib/compiler.htm
   l">http://docs.python.org/lib/compiler.html</a> .  Also, it took me a
   while to realize that AST stands for Abstract Syntax Tree so that
   should be more obvious.


Posted by Jeff McNeil on 2007-11-16 at 19:05. 

::

   The logging package can do a whole lot, but it's almost impossible to
   get the hang of unless you've worked with log4j and friends.


Posted by Marius Gedminas on 2007-11-17 at 07:12. 

::

   * optparse: great module, no examples given by 'pydoc optparse'.    *
   re: when you forget the regex syntax details (because every regex
   dialect is different), you have to know to 'pydoc sre' instead of re.
   * logging: I've nearly given up on this one.    * difflib: useful, but
   not intuitive.    * email: when you need non-ASCII text in your
   emails, good luck figuring it out.


Posted by Dan on 2007-11-17 at 17:21. 

::

   Where the docs seem to break down is where you have major overlap
   between different modules. So my 5 would be 2 groups of overlapping
   modules:    urllib -- urllib2 -- urlparse  time -- datetime    Without
   learning the ins and outs of each module, its hard to work out which
   you should be using.     Actually, in both cases, I think the modules
   should be combined. It's pretty confusing to have to remember what is
   in urllib, what is in urlparse, what is in urllib2.    The re module
   makes me want to tear my hair out, but that's the design of the module
   more than the docs.


Posted by Doug Hellmann on 2007-11-17 at 18:48. 

::

   re - I can never remember the difference between search() and match()
   timeit - I haven't actually used it that often, but find the API a
   little weird. Why do I pass the text of the code to time, instead of a
   callable like a function or method?    optparse - It's not very object
   oriented. Why do I give a name for the action, instead of
   instantiating different types of option handlers for different
   behaviors?    logging - There are so many options. It has great
   potential, but I always have to look for an example to get a basic
   configuration setup.    bisect - Why isn't this handled as a method of
   list? Something like insert_sorted()?    distutils - Don't even get me
   started.


Posted by Harry Fuecks on 2007-11-18 at 06:27. 

::

   - urllib(2?): is nice for one liners but gives me Tourette's when it
   comes to how it automagically decides what proxy server you are using
   (vi IE on Win32). No no no no no! Just cause Java does it doesnt make
   it right!    - timeit - eval?!?    - itertools - nomenclature is ugly
   plus their mere presence leaves me permanently wondering if I've
   missed something    - optparse et al - can we explore this path please
   - <a href="http://laurentszyster.be/blog/anoption/">http://laurentszys
   ter.be/blog/anoption/</a>    - unittest - more examples for common use
   cases please    - everything under documented - "Oh what version did
   you get that nice feature?" - datetime I'm looking at you!


Posted by Richard Moore on 2007-11-18 at 07:53. 

::

   Re: Marius Gedminas    I have some examples of how to send emails with
   attachments that could be added to the docs, where should such things
   get sent?


Posted by Noah Gift on 2007-11-18 at 22:57. 

::

   I agree on ConfigParser.


Posted by Fredrik on 2007-11-19 at 14:09. 

::

   For me its not so much the any particular lib that bugs me but the
   inconsequent naming conventions used in throughout the built-ins and
   libs. For example Im always uncertain if its "has_key" or "haskey" for
   the dictionary method or  "starts_with" or "startswith" for strings.
   Also there is no standard syntax that depicts objects, modules,
   functions and methods (e.g. "StringIO.StringIO", "datetime.datetime",
   "threading.Thread" etc.).  For me this is the single biggest annoyance
   and counts for most of my need to lookup documentation and annoying
   runtime exceptions.


Posted by fredrik on 2007-11-19 at 17:25. 

::

   For me it's not so much the any particular lib that bugs me but the
   inconsequent naming conventions used in throughout the built-ins and
   libs. For example I'm always uncertain if it's "has_key" or "haskey"
   for the dictionary method or "starts_with" or "startswith" for
   strings. Also there is no standard syntax that depicts objects,
   modules, functions and methods (e.g. "StringIO.StringIO",
   "datetime.datetime", "threading.Thread" etc.). For me this is the
   single biggest annoyance and counts for most of my need to lookup
   documentation and annoying runtime exceptions.


Posted by Zeroth on 2007-11-20 at 11:27. 

::

   The inspect module should have better documentation. It looks like an
   awesome module, some great power... except I have no idea where I'd
   use it.    There's also optparse, that one's bloody difficult, as
   well, distutils. Those are my three.


Posted by Justin Francis on 2007-11-23 at 12:03. 

::

   * profile: the vast majority of options in this module are
   undocumented. Even the primary entry functions are not documented
   enough to use right away without some trial and error   * logging:
   it's complicated, and the docs don't have the overview necessary to
   understand how to use it, and even many details are missing about each
   object type


Posted by Titus Brown on 2007-11-27 at 03:06. 

::

   Also see reddit comments,    <a href="http://programming.reddit.com/in
   fo/60qk4/comments/">http://programming.reddit.com/info/60qk4/comments/
   </a>


Posted by Titus Brown on 2007-11-28 at 00:29. 

::

   See    <a href="http://ivory.idyll.org/blog/nov-07/ghop-
   announce.html">http://ivory.idyll.org/blog/nov-07/ghop-
   announce.html</a>    for my motivation for this post...


Posted by Chris Lasher on 2007-12-03 at 11:38. 

::

   FWIW, I found Python regular expressions quite manageable after
   reading through Andrew Kuchling's Regular Expression HOWTO  <a href="h
   ttp://www.amk.ca/python/howto/regex/">http://www.amk.ca/python/howto/r
   egex/</a>

