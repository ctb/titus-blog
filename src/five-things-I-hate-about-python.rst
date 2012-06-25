Five Things I Hate About Python
###############################

:author: C\. Titus Brown
:tags: python
:date: 2007-03-04
:slug: five-things-I-hate-about-python
:category: python


`Brian D. Foy claims
<http://use.perl.org/~brian_d_foy/journal/32556?from=rss>`__ that if
you want to be an effective advocate for a language, you need to be
able to answer the question, "What are five things you hate about it?"

Hmm, lessee.  I actually have a tough time coming up with five things
off the top of my head, but:

 1. The 'import' command, 'sys.path' modification semantics, and the
    whole "shadow module" import optimization.  It's all just ugly.

 2. Threading, the global interpreter lock, and multiprocessing.  Ugly
    (but beautiful, too; Guido's right when he says writing C
    extensions would be *miserable* w/o the GIL).

 3. The (dis)-organization of the stdlib.  I can't find a damn thing
    in there without already knowing that it exists, and then when I
    do find it the documentation is invariably confusing and poorly
    laid out.  (As an extreme example, try using the subprocess module
    to do, well, anything.  Even if you have a reasonably good
    knowledge of OS behavior, you have to flip back and forth between
    about five doc pages to figure out how to use the module.)  The
    stdlib is still great -- it actually *has* most things! -- but it
    is also frustrating.

 4. The patch mafia.  I like everyone on python-dev that I meet, but
    somehow it is annoyingly difficult to get a patch into Python.
    Like threading, and the stdlib, this is a mixed blessing: you
    certainly don't want every Joe Schmoe checking in whatever crud he
    wants.  However, the barrier is high enough that I no longer have
    much interest in spending the time to shepherd a patch through.
    Yes, this is probably all my fault -- but I still hate it!

 5. easy_install doesn't work on enough packages.  easy_install is
    $DEITY's gift to admins, but it doesn't work on a number of packages.
    This is usually some combination of (a) poor package structure,
    (b) C/C++ code compilation requirements on systems where I don't
    have a C/C++ compiler (i.e. Windows ;), and (c) failure to post
    the package on PyPI.

    I have some ideas (in line with Grig's Cheesecake project) on how
    to start fixing #5, so that's where I'm going to start ;).

So these are the five things that come to my mind when I want to bitch
about Python.

At the risk of starting an out-of-control meme... what are the five things
YOU most hate about Python?

--titus


----

**Legacy Comments**


Posted by Anders Pearson on 2007-03-04 at 12:44. 

::

   I definitely agree on sys.path modification and <em>_init_</em>.py
   ugliness, but is there something else about import that you don't
   like? I generally really like the combination of flexibility and
   clarity of import with help from 'from' and 'as'. Beats the hell out
   of java's import or perl's 'use' or 'require'. The new relative import
   stuff makes sys.path modification less frequently necessary now too.
   I would add having to list 'self' in method signatures. I understand
   the reason behind it, but it still feels like something that the
   language implementation should hide from the programmer.     The
   abundance of '<em>_' methods also bothers me stylistically. Code like
   'if __name_</em> == "<em>_main_</em>"' just makes me cringe every time
   I write it.


Posted by Scott Tsai on 2007-03-04 at 12:59. 

::

   Disagree about the "subprocess" module.  The only documentation one
   needs is the docstring to the subprocess.Popen constructor. The rest
   can be figured out easily in an interactive shell.    Compare
   implementing I/O redirection and custom resource limits with
   subprocess versus a standard fork/exec sequence.    I think subprocess
   is much better than the os.popen and "popen" modules that it osboletes
   and is a jewel in the standard library.


Posted by Greg Wilson on 2007-03-04 at 15:16. 

::

   My five things:    1. Use of indentation to show nesting.  Yeah, yeah,
   I know, but (a) have you ever **read** the studies the claims about it
   are based on? and (b) it makes a lot of things difficult (like multi-
   statement lambdas).    2. stdlib disorganization.  I'm very afraid
   this is going to carry over into Py3K.    3. The "engineering is a
   substitute for documentation" meme.  I mean, c'mon, Scott, Titus is a
   bright guy --- if **he** has trouble with subprocess, how much luck
   are newcomers who haven't yet decided whether to adopt Python, Ruby,
   or something else entirely going to have?    4. Tkinter.  Good for its
   time, but can we please move on?    5. People saying that tuples
   aren't just const lists... ;-)


Posted by Jacob Kaplan-Moss on 2007-03-04 at 15:32. 

::

   I know you didn't mean to start a meme, but I actually think this
   could be a fun one :)    Here's mine: <a
   href="http://www.jacobian.org/writing/2007/mar/04/hate-
   python/">http://www.jacobian.org/writing/2007/mar/04/hate-python/</a>


Posted by Robert on 2007-03-04 at 15:42. 

::

   I'm still a python beginner, so the thing I hate most about python has
   nothing to do with the language itself but with the documentation.
   Coming from a background mostly in java, which has fantastic
   documentation, it is a frustrating to read the docs on python.  I
   truly think if the docs were totally re-written (preferably similar to
   how java docs are formed) the language would get even more use.


Posted by Raffaele on 2007-03-04 at 16:44. 

::

   I really hate the nesting-by-indentation design...can't help it...
   It's like a wonderful car...but painted in pink, with dozens of Hello
   Kitty around...


Posted by Sam Gibson on 2007-03-04 at 17:07. 

::

   1. Disorganization of the stdlib naming/style conventions. Why is
   there no enforced style for modules included in the standard library?
   2. Schizophrenic object orientation. Somethings are methods, some
   things are language functions, some things are module functions... and
   you can never be sure exactly how it's going to be (this is related to
   #1)    3. Lack of any user documentation for Pydoc. Seriously, I just
   said fuck it and switched to epydoc because of frustrations.    4.
   Lack of a "protected" method/property type. Yes I've read the
   arguments. Yes I know "private" methods aren't really private. But it
   makes me cringe everytime I write a method that I want to propagate to
   children but shouldn't ever need to be called by an end user.    5. I
   can't think of a fifth ;-)


Posted by Newbie on 2007-03-04 at 17:30. 

::

   I agree about the documentation. It's not that it doesn't say what you
   need, but it's too hard to find the information.    I think one of the
   reasons why PHP has so many users is the impressive documentation.
   Java and .Net also have impressive documentation. It's a shame that
   Python doesn't have the same. docstrings is not the solution.


Posted by Anatol Ulrich on 2007-03-04 at 17:38. 

::

   import is horribly broken when you try to use it with metaclasses.
   David Mertz wrote an <a href="http://www-128.ibm.com/developerworks/li
   nux/library/l-pymeta.html">import_with_metaclass</a> method, but of
   course it's broken too (it's been 4 years since I looked into the
   issue and I've forgotten the details, unfortunately. I've got a more-
   or-less working import_with_metaclass flying around somewhere, but it
   was a pain to write and still is not waterproof)


Posted by Tennessee Leeuwenburg on 2007-03-04 at 17:44. 

::

   I would have to say, without a doubt:    1.) Tkinter is just ugly  2.)
   Multiprocessing is required  3.) The community is way too fragmented
   4.) The community is way too invisible  5.) Web framework decisions
   and use are too hard


Posted by Karl Guertin on 2007-03-04 at 17:50. 

::

   1. Mixed tabs and spaces (this really should die for Python 3k, I'd be
   surprised if it wasn't but I don't remember it being part of Guido's
   PyCon talks the past two years)  2. File manipulation is annoying if
   you're not using Path.py, but people on the mailing list shoot it down
   without providing counter suggestions/implementations.  3. Typing
   'exit' or 'quit' at the prompt. effbot posted a fix but people on the
   mailing list shoot it down for stupid reasons.  4. Dateutil isn't in
   the stdlib. I haven't read the discussion, but I belive it was shot
   down in a rather nasty discussion on the mailing list...  5. Limited
   commodity hosting.


Posted by Cowmix on 2007-03-04 at 18:11. 

::

   While I agree with the post and the replies above, I have to add one
   more specific thing that drives me crazy... Python doesn't have a SOAP
   implementation as complete as Perl's SOAP::Lite.


Posted by Tim Keating on 2007-03-04 at 19:37. 

::

   Greg Wilson: Making multi-statement lambdas hard isn't a bug, it's a
   feature!    I invite you, and the rest of you  block-delineation-by-
   indentation-haytas, to read my rationale for why this is the ONLY
   logical way to do block delineation: <a
   href="http://www.mrtact.com/blog/2007/01/python-and-
   whitespace.html">http://www.mrtact.com/blog/2007/01/python-and-
   whitespace.html</a>    For my top 5:    1. Self. AAARGH!  2. global.
   Though I can't think of a better way to handle this, and it is
   certainly WAY better than Lua's local (which is basically the same
   thing, inside out).  3. Gotta agree with whoever said the lack of
   consistency in the Python std lib. Hopefully, this will get looked at
   for Py3K. (And hey, maybe I should contribute to that, while I'm
   bitching about it.)  4. No Main() function at the module level. I'm
   pretty sure there's a PEP for this, but I don't remember where it's
   at. if <em>_name_</em> == '<em>_main_</em>' was fine . . . in 1995.
   5. Again, gotta agree with Karl. Mixed tabs and spaces bites. Maybe we
   should add some kind of hinting syntax to the language spec, to tell
   editors which indenting style to use . . .     TK


Posted by Doug on 2007-03-04 at 20:15. 

::

   1. Slower than java.    2. Limited expressiveness.  No multiline
   anonymous closures like in ruby.  Guido stated that this it is
   syntactically impossible.  Not nearly as DSL or macro friendly as
   other languages.    3. self self self self - it's as if OOP was just
   tacked on.    4. Redundant or meaningless symbols and keywords like
   the colon at the beginning of a block, and all the underscores.  What
   is "def"?  Why "elif" instead of "else if"?  "lambda"?    5. The
   python community.  RTFM jerks, rude to all newbies or new ideas.
   Zealots about python (Guido called them the NIMPY crowd: not in my
   python), and they spread absolute FUD about everything else.  Shot
   down most proposals for python, including ones Guido has proposed
   himself, like optional static typing or case-insensitivity.  If you
   don't want python to ever change, stick with python 1.5 or whatever
   version you are holding on to.    Die python die.


Posted by Ilya on 2007-03-04 at 22:59. 

::

   Python is a great language, but    1. It's raw execution speed PALES
   compared to java.  I find it's kinda strange that psyco has not been a
   part of std python distribution. And now psyco itself is pretty much
   abandoned.    2. Lack of decent documentation generator. pydoc is a
   useless toy. Restructured Text might be good but there are no source
   processing tools (not in std rest distribution). In fact I think
   Restructured text's semi official status (used for Peps, etc) has done
   a lot of harm to development/adoption of other alternatives.    3.
   Lack of "official" gui.. Tkinter is pretty good ( from my POV at
   least) but it's slow when it comes to heavy 2D rendering and there
   does not seem to be much active development... Also alternatives are
   recommended so frequently (even on python-dev) that it's hard  not to
   get a feeling that tkinter is about to be replaced.    4. stdlib needs
   a cleanup/reorg. Badly.    5. python 3000... Seems to be mostly about
   trying to remove minor language warts at expense of MAJOR b/w
   incompatibility and major slowdown of python 2.x development.. It may
   easily be the end of python...


Posted by TRauMa on 2007-03-04 at 23:17. 

::

   1. self (a scope issue)  2. having to mention the class name for class
   vars (a scope issue)  3. "for" vars living after the end of the "for"
   (a scope  issue)  4. having to mention the class name in super()  5.
   no module reloading (may come for OLPC?)  6. optionally make INDENT
   and DEDENT replaceable by a special char for generated/embedded code
   Whoops, just pretend i put the first two in one item.


Posted by gasolin on 2007-03-04 at 23:48. 

::

   5 things I hate about Python    1. std documents are too brief, and
   the books are too thick    2. too much batteries to know which to use
   at the first time (a sweet burden)    3. a frequently showed: if
   <em>_name_</em>=="<em>_main_</em>" syntax is not pretty    4. have a
   name everywhere, but no pacesetter in at least one domain, such as
   java in enterprise, php in web, vb in windows app,     5. why wxpython
   not default?


Posted by Titus Brown on 2007-03-04 at 23:56. 

::

   Wow, I seem to have touched a nerve with the subprocess comment.  I
   **love** subprocess. I use it quite a bit. I just hate the docs.
   I'm impressed by how many people seem to hate 'self'.  I quite like
   it.  Implicit scoping is hard to read IMO; I try not to even use
   global myself.    Ilya, do you mean that Java is faster than Python?
   ('cause what you said is the opposite)    Also, Ilya, re Python 3000
   -- had to be done sometime.  I can't see it being the death of Python.
   I think Python's conservatism is a good thing; heck, I wished it
   changed slower.  I'm not going to be affected (positively OR
   negatively) by most of the new features in 3k...    --titus


Posted by Ilya on 2007-03-05 at 01:25. 

::

   Yes, to clarify, I meant, Java is quite a bit (10s of times) faster in
   many CPU-intensive cases...(E.g floating point computation)    When I
   said that python 3000 might kill the python what I meant is this: it
   will bring a huge uncertainty for the next 2-3 years. Why would anyone
   decide to use python for new development if the code will have to be
   ported pretty soon? Furthermore this switch is likely to damage python
   reputation quite a bit and thus affect even existing developers.
   Meanwhile patch review time for python 2X will go upfrom 2 years to 20
   years ;-).. Thus driving away potential new developers..    This is,
   of course, the worst case scenario..    Does py3k have to be done? I
   am not at all sure. While it'll be removing warts, the warts are
   mostly minor...


Posted by rogerv on 2007-03-05 at 02:13. 

::

   Hmm, after reading many of these complaints about Python, I could't
   believe just how screwed up a language it must really be.    You dudes
   should just bail and join me in taking up Groovy. Now this is one nice
   language - yet it runs on a JVM (i.e., tons of hardware/OS platforms),
   and is able to tap a vast, vast universe of Java libraries.    The toy
   languages are those where you have to resort to writing extensions in
   C (and figure out a way to do so portably - both the program code and
   its build process). That is what is wrong with Perl, PHP, Python, and
   Ruby. You know something is fundamentally wrong with a language when
   it is not practical to write truly useful libraries in the language
   itself, but have to resort to C.    Groovy, however, is a dynamic, OO
   language designed exclusively to run on a portable virtual machine -
   and fortunately it is a VM that has already been tuned for over a
   decade. Plus there is millions of lines of pre-existing Java code to
   stand on top of. And from top to bottom it is now entirely open
   source.


Posted by GUI Junkie on 2007-03-05 at 03:05. 

::

   I agree with the documentation issue. I was used to c-type manuals.
   With actual working code examples. The code snippets in Python really
   don't help a newbie to get his grip on.


Posted by Alen on 2007-03-05 at 04:03. 

::

   This is great feedback. Since Python revolves around Open Source
   community, now you have an opportunity to fix things you and others
   are bitching about. Contribute it back to the community in a form of
   bitching or code and write a next weblog titled "Five NEW Things I
   LOVE About Python" :-)    -Alen


Posted by njr on 2007-03-05 at 05:02. 

::

   Not sure too many will agree, but for me:    1. It's easy to end up
   with a version that doesn't have readline.    2. Jython is still stuck
   at 2.1, which in practice, for me, means I can only use 2.1 most of
   the time.    3. Divison defaulting to int.    4. Colons.  As far as I
   can tell, they're just there to support single line stuff, which is
   evil anyway.  I still miss them out repeatedly.  Edward Tufte,
   graphics guru, complains about "chart junk" on graphs---all the stuff
   shouldn't be there because it just gets in the way of the data.
   Colons are "language junk".    5. == to test for equality.  I know no
   one else agrees.  But it's just a legacy from C's insanity in allowing
   you to test the result of an assignment (did anything ever cause more
   bugs?), which python doesn't allow anyway.  It should be =.


Posted by Tom Smith on 2007-03-05 at 05:17. 

::

   I'm not a hardcode coder, lambda physically hurts... but...    1. the
   "if <em>_name_</em> == '<em>_main_</em>':" is awful. I like to
   evangelize python, to teach how easy it is and this I always feel
   embarrassed about...     2. The stuff that you need to add to turn
   pseudo-code into python...    The char I hate the most ":", and also
   "==" and  "elif" (I always read "elif-ant").    3. import xxx...
   import xxx as y... from xxx import y... from xxx import y as x    4.
   The way I HAVE to do a "import * from string". I ALWAYS need
   everything from string... ggr! If I could do with out MY standard
   modules most code would lose about ten lines from the top.    5. I
   don't mind self but having to use a classname for super() sucks.
   5.1 Documentation. Both my own and other peoples'. Using a string as
   the first element was a (nice) hack once... and Debugging. Python
   seems to me have been created from the concept of pseudo-code (a good
   concept) up...and now needs to be re-jigged with the same brilliance
   from the "broken pseudo-code" end. (print for debugging really sucks).


Posted by njr on 2007-03-05 at 05:51. 

::

   Not sure too many will agree, but for me:    1. It's easy to end up
   with a version that doesn't have readline.    2. Jython is still stuck
   at 2.1, which in practice, for me, means I can only use 2.1 most of
   the time.    3. Divison defaulting to int.    4. Colons.  As far as I
   can tell, they're just there to support single line stuff, which is
   evil anyway.  I still miss them out repeatedly.  Edward Tufte,
   graphics guru, complains about "chart junk" on graphs---all the stuff
   shouldn't be there because it just gets in the way of the data.
   Colons are "language junk".    5. == to test for equality.  I know no
   one else agrees.  But it's just a legacy from C's insanity in allowing
   you to test the result of an assignment (did anything ever cause more
   bugs?), which python doesn't allow anyway.  It should be =.


Posted by Paul Boddie on 2007-03-05 at 07:22. 

::

   Some experimental work I did a while ago brought on a list of
   suggested improvements to Python - see the end of this document:    <a
   href="http://www.boddie.org.uk/python/javaclass.html">http://www.boddi
   e.org.uk/python/javaclass.html</a>    Python has its shortcomings but
   is still highly usable. However, I'd point out the following areas
   (alongside those mentioned in that document):    1. The standard
   library: making this coherent is far more important than a lot of the
   Python 3000 changes, but the Python core development situation often
   appears (at least strategically) analogous to a hypothetical situation
   where some GNU/Linux distributor decides to ignore the userland stuff
   and only really do work on kernel hacking. Standard library
   organisation and maintenance needs revisiting, and Python Eggs don't
   provide the panacea some people suggest.    2. The official
   documentation: I have to look around various manuals to find details
   of language semantics (when the reference manual only mentions the
   syntax), and there are features which are only mentioned in Guido's
   essays and AMK's "what's new" notes. This doesn't help people writing
   tools for source code analysis, which is an interest of mine and of
   other people.    3. Language evolution: we started off with
   <em>_getattr_</em> then got <em>_getattribute_</em>; we had old-style
   classes and then new-style classes came about (with that bizarre
   "inherit from object" business, where "object" is a class); we got the
   super function which is more clunky than just calling the superclass
   initialiser; metaclasses were thrown in because some people wanted to
   cover all the language paradigm bases; ditto nested scopes, where the
   only benefit seemed to affect lambda for many people - others were
   using factory classes, anyway, which probably shows up better in any
   generated documentation.    4. Language fixation: python-
   dev/3000/ideas seem to be mostly about touch-ups to the language
   rather than improving the performance, concurrency or deployment
   situations.    I'll leave point 5 to cover all the things I didn't
   already mention. Things like the import machinery (nasty!) are
   probably covered in that document referenced above. Perhaps a lot of
   the behind-the-scenes infighting (or "friendly competition" as some
   people like to call it) might merit a point, but that's not strictly a
   Python-the-language-or-runtime thing.


Posted by Titus Brown on 2007-03-05 at 09:21. 

::

   Paul, I couldn't agree more.    Ilya, Guido is making huge efforts to
   make porting programs from 2.x to 3.x easy.  **Huge**.  It should be
   pretty easy.    rogerv, I love it!  "This language is broken.  Switch
   to **my** favorite language!"  Yah.    Anyway, the point of the
   original post was to ask people who **liked** Python in general what
   they **hated** about it.  Some interesting responses; thanks ;).  I
   doubt whitespace or colons are going to change anytime soon, but there
   do seem to be some areas we can work on.


Posted by Rubynonymous on 2007-03-05 at 10:55. 

::

   1. It's not ruby.  2. It's not ruby.  3. It's not ruby.  4. It's not
   ruby.  5. It's not ruby.    /me ducks and runs ;)


Posted by Titus Brown on 2007-03-05 at 11:40. 

::

   Rubynonymous,    no, sorry, invalid.  You have to tell us five things
   you hate about Ruby, if you're a fan of Ruby ;).    --titus


Posted by schlenk on 2007-03-05 at 14:56. 

::

   Ok, lets start:    - Tkinter, its just one of the worst Tk bindings in
   existance, no wonder its so ugly and hated. (Tk can look good, take a
   look at the tile project which provides theming and other eye candy.
   If you never used Tk from Tcl you haven't really used Tk.).    - The
   global interpreter lock for threads, it sucks (and you can do without,
   take a look at Tcl's threading implementation for example, its not the
   horror for C-modules if done right)    - The lousy stdlib docs,
   everything you don't want to know is there, everything you want to
   know is hidden in the source code.    - The low powered OO model.    -
   The rather weak metaprogramming support.


Posted by holy_robot on 2007-03-05 at 17:08. 

::

   Five things I hate about ruby:    1. Block parameters write over
   existing variables instead of shadowing.    2. You can pass only one
   block to a method and lambda/proc looks really ugly.    3. initialize
   should be abbreviated so variant spellings (eg. initialise) aren't
   even possibly a problem.    4. Passing methods by name sucks. Compare
   def square(x) x*x end  puts
   some_array.map(&amp;method(:square)).join(', ')    # Please excuse my
   python here.  # Hopefully it isn't too bad.  def square(x): return x*x
   print ', '.join(map(square, some_list))    5. Ruby is slower than "my
   brother Bilo."


Posted by Martin v. Lwis on 2007-03-06 at 00:35. 

::

   I really dislike being called part of a mafia. Of your own patches, I
   accepted 443899 , 448227, 450702, and 1104111; 1087808 was closed as
   outdated as somebody else continued to work on it (and then Georg
   Brandl committed it). So it seems that **all** of your patches were
   accepted in some form or the other. Doesn't sound like mafia to me.


Posted by engtech on 2007-03-06 at 01:29. 

::

   re: pydoc short-comings    Doxygen has built-in python support now,
   although it still has bugs.    <a href="http://www.stack.nl/~dimitri/d
   oxygen/">http://www.stack.nl/~dimitri/doxygen/</a>


Posted by Max Ischenko on 2007-03-06 at 03:19. 

::

   My list: <a href="http://maxischenko.in.ua/blog/entries/116/five-
   things-i-hate-about-python/">http://maxischenko.in.ua/blog/entries/116
   /five-things-i-hate-about-python/</a>


Posted by Scott Lamb on 2007-03-06 at 03:47. 

::

   1. General performance.    2. Threading performance (GIL).    3. You
   can't spot type or even spelling errors until runtime. (On the other
   hand, I take advantage of this to do fancy stuff all the time...I love
   it and hate it.)    4. Older versions. Python 2.5 is out, but many,
   many people still use Python 2.3. Some even cling on to Python 2.2. I
   want to use the latest features!    5. DB-API 2.0. Perl's DBI is
   better, and Java's database API is superior in every way. Here's one:
   DB-API doesn't mandate support for any particular form of bind
   variables, so SQL is not even portable between different drivers for
   the same RDBMS. In Java, I can often write queries that run on many
   RDBMSs.


Posted by Titus Brown on 2007-03-06 at 14:13. 

::

   To the person complaining about my use of 'mafia', I was using the
   semi-affectionate term, "A tightly knit group of trusted associates,
   as of a political leader".    Yes, I can get patches accepted.  All I
   need to do is submit a patch that meets all of the personal criteria
   of whoever I hope will be willing to apply it and follow the patch
   through comments, sometimes for weeks.  This often lengthy process is
   why there are so many "abandoned" patches sitting out there.
   Contrast this with the people who have direct commit access, or the
   people who are introducing modules from the community, who can submit
   code that doesn't necessarily meet doc or format standards and isn't
   necessarily well tested or effectively documented.  (I think the
   commenters above make this point about the stdlib fairly well; I
   complained about wsgiref not so long ago, which was committed with
   significant test gaps and  didn't conform to PEP 8.)    Combined, this
   makes me think that different standards apply to people with direct
   commit access and people without it, which is not particularly
   friendly.  Don't get me wrong -- it's **understandable** and I'm very
   happy with Python as a whole, but patch submission **is** one of the
   things I dislike about Python.    And that's what my blog entry was
   about.    From the discussion on python-dev, it's clear that this
   complaint is not an isolated one, either.  It's interesting to think
   about technical and sociological ways to fix it.    My own irritation
   was catalyzed by one of my patches.  After my initial five-line patch
   submission, I was presented with a wishlist necessitating moderately
   severe changes to the module, which I wasn't really competent to do;
   copy/pasting code from another stdlib module to fix the bug was
   rejected, because it wasn't a complete enough fix.  The process failed
   in a few places: the module wasn't well tested; another module that
   worked better still had lousy code in it; and the priority was not to
   get a fix in, but to do it **right** -- **this** time.  Again, all
   understandable and probably the right way to do things, but **not**
   the way to encourage people to submit patches.    Oh, and then there
   was the time I submitted a patch, only to be told "you didn't submit
   it right".  I went back and found the instructions, and sent them
   back, only to be irritably told "gosh, you found the **one place**
   where the instructions were bad and followed those instructions".
   Yep, I sure did!  And of course the response wasn't "oops, I'll go fix
   that" (although I think they did) -- the response was irritation at my
   presumed stupidity.  Not very encouraging.    So all in all the few
   run-ins I've had with python-dev have not been terribly welcoming or
   always very efficient.  Perhaps it's better not to bring these topics
   up?  You're all doing a great job as it is, and I don't want to
   undermine that... I just want to improve ;(    cheers,  --titus
   p.s. see my next post for things I'd like to actually do myself.


Posted by Giacomo on 2007-03-22 at 11:07. 

::

   Titus, your "mafia" point could actually apply to pretty much any
   major OSS project. Same for the attitude of the "community". The Linux
   community is well-known for similar antics, but this didn't stop the
   project from being successful. People are bitching about this since
   forever... but almost always there is a solid reason behind
   encouraging people to Read The Fine Manual. After all, Python wasn't
   created by self-taught "web-plumbers" like myself ;)

