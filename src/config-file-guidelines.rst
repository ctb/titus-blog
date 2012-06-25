Dear Lazyweb: Config file guidelines?
#####################################

:author: C\. Titus Brown
:tags: python,lazyweb
:date: 2008-01-20
:slug: config-file-guidelines
:category: python


Tracy recently asked me if there were any good guidelines about how to
write configuration files -- not coding-level guidelines, but guidelines
on structure and content.

I was unable to come up with anything: my Google-fu failed me, and my
DevonThink database was silent (although it did have some nice testing
articles, which I of course forwarded on to her).

I must admit to a general mental block on the subject of how to write
config files.  How do you choose the right balance between
configurability and complexity?  What about language -- should they be
native Perl/Python/whatnot (Tracy's package is for programmers) or is
there a benefit to embracing the mental overhead of config file parsing?

Thoughts and pointers appreciated, either in comments or `via email
<mailto:titus@idyll.org>`__.

--titus


----

**Legacy Comments**


Posted by cariaso on 2008-01-20 at 19:40. 

::

   seems relevant to your question  <a
   href="http://www.itworld.com/AppDev/application-design-config-file-
   design-nlstipsm-080109/index.html">http://www.itworld.com/AppDev
   /application-design-config-file-design-nlstipsm-080109/index.html</a>
   I'd like a nice little python module, which would eval a config file,
   but constrain evaluation to within a namespace. Afterwards I could
   pluck out the params by name.


Posted by Moof on 2008-01-20 at 19:55. 

::

   I assume you're going for something that is either cross-platform or
   *nix. Both Windows and MacOS have mechanisms for configuration
   information storage, and there are very many good reasons why you
   should use them. If I had a pint for every times I've been moaned at
   by my windows admin friends because an application wasn't configurable
   through active directory, I'd be suffering from cirrhosis.     Thus,
   if you're targeting Windows, and to a lesser extent, MacOS, then you
   should probably abstract your configuration system enough that you can
   use the platform-friendly storage. Which does imply you'll need to
   fiddle with a parser for unix systems. Use a ready-made one, as it
   makes life easier for people, as they've normally met key = value
   files or Windows Ini files, or XML before. I've no idea if anyone's
   written any freely available libraries for this cross-platform style
   of configuration, but if not, then Someone Should (TM).     To a
   certain extent, your coding language will help you determine this
   also. Java is all about XML configuration files, and makes them pretty
   easy to deal with. In Python, on the other hand, most of the major
   frameworks I've dealt with (notably Twisted and Django) prefer to just
   use plain old Python for configuration.    Certainly, if you're
   writing a library or programmer's tool, make sure that it is fully
   configurable from within your code, and make it trivial for code to be
   loaded from a config file and then modified on a whim. You wont' be
   able to guarantee that the programmers that use your library or tool
   will either want or be able to give you a config file. This is
   normally solved by having a global config object that you can modify
   **before** activating the rest of the library.    In the case of a
   command-line tool, everything needs to have switches, unless it's a
   very complex program, in which case you need to be able to feed it a
   separate config file from the command line.    One thing to keep in
   mind: If you use a plain old programming language to configure your
   program, make sure you've thought the security implications through,
   and what might happen if (a) an average and (b) a malicious user got
   hold of that file. Often it's a case of "if they can get at that file,
   then I have worse security problems than what they can do with my
   file", but not always.    Be wary of writing a conf system too early
   on in the game. A friend of mine prefers not to tack one on until near
   the end of the "1.0" milestone, whatever that may be, as he finds that
   writing config in an agile language is quicker to start up with, and
   you often find yourself evolving your config needs as the program
   matures, and limiting yourself too early in the game means you end up
   spending too long tweaking the config system as opposed to coding your
   program.     Beware, also, of making something that is Turing-complete
   - the world doesn't need another scripting language.    See also: <a
   href="http://www.itworld.com/AppDev/application-design-config-file-
   design-nlstipsm-080109/index.html">http://www.itworld.com/AppDev
   /application-design-config-file-design-nlstipsm-080109/index.html</a>


Posted by Noah Gift on 2008-01-20 at 21:33. 

::

   This is in interesting question, and one that I am attempting to
   tackle in our book, and my PyCon talk to a small degree.  Greg Wilson
   kind of hints about it in Data Crunching, which is a great little
   book.    I suppose I would look at the buildout tutorial, and say try
   using buildout.  I think they have done a superb job at making config
   files simple, yet effective enough for a complex task.    <a href="htt
   p://grok.zope.org/minitutorials/buildout.html">http://grok.zope.org/mi
   nitutorials/buildout.html</a>


Posted by Olivier Tharan on 2008-01-21 at 02:09. 

::

   Consider using YAML, it is pretty easy to read as a human and parsable
   by most languages with the help of modules. Python has pyyaml and
   PySyck, the latter is more complete.    Another advantage (besides
   being human-readable) is that you can include almost any data
   structure and have it readily available as a variable.


Posted by Alcides Fonseca on 2008-01-21 at 05:39. 

::

   I suggest YAML as well. Very good for configuration files and no need
   for knowing some programming language.    However, if action is one of
   the configuration (some times it is!) consider making the
   configuration Python class files. It's simple as well, but requires
   programming skills to understand that (but only if you need to set up
   methods as configuration).


Posted by Mika Eloranta on 2008-01-21 at 18:57. 

::

   There are many positive sides to Unix-style config files, but they are
   not perfect:    1. The input is not validated until it is too late,
   i.e. when the application is starting -&gt; "oh crap, no
   configuration: bail out!" -&gt; downtime.     2. Making changes to
   configuration while the application is running is often not possible.
   If it is possible, it is implemented using the "break the config (see
   issue #1), SIGHUP and grep the log for errors" -method, which
   obviously is not optimal. You cannot just go and say "Hey server app,
   please drop the number of threads in the pool to 20!", in which you
   would get a confirmation response: "OK, done!" (or maybe: "Dude! There
   ain't no thread pool here! It is a process pool, you dork! Please try
   again.")    3. There are so many different config file formats one
   must master to admin a Unix system. Some of the formats are pretty
   weird (still got nightmares of sendmail.cf files)...    4. Config
   files are not usually "upgraded" along with the software. Your config
   file will miss all the cool new settings (and documentation changes!)
   that CoolSoftware v2.0 adds. If the semantics and/or syntax of the
   configuration have changed  in the upgrade AND if you are lucky, you
   will see an error message the next time you start the software.     5.
   Maintaining any kind of revision history is left to the user (e.g. for
   cases when "last known good" configuration is needed).    6. Usually
   the only method of changing configuration is editing by hand. No web
   interfaces or even simple "set setting X to value Y" command-line
   interfaces.    These are just some of the limitations and in my
   opinion already pretty severe. Oh boy, it has been on my list of
   things to do for a long long time to write "a better configuration
   framework" that would, for example, tackle at least some of these
   issues. Actually, I've recently even started working on it. :-) So,
   I'm also very interested in seen others' comments on this topic.
   PS. Python modules are awesome for a lot of configuration uses.      -
   Mika


Posted by Titus Brown on 2008-01-22 at 03:08. 

::

   Thanks guys, this has been very useful!    Gael Varoquaux also pointed
   me towards <a href="http://projects.scipy.org/ipython/ipython/browser/
   ipython1/trunk/sandbox/tconfig">http://projects.scipy.org/ipython/ipyt
   hon/browser/ipython1/trunk/sandbox/tconfig</a>    which looks like a
   good configurator.    --titus

