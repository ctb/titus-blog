Pursuing simplicity
###################

:author: C\. Titus Brown
:tags: python,testing,science
:date: 2009-04-03
:slug: pursuing-simplicity
:category: science


John Gall apparently said:

  A complex system that works is invariably found to have evolved from
  a simple system that worked.  The inverse proposition also appears to
  be true: A complex system designed from scratch never works and cannot
  be made to work.  You have to start over, beginning with a working
  simple system.

Something I noticed at this year's PyCon is that people want me to
make my software more complicated. twill developers want me to
unpackage twill's dependencies from twill, and add features that make
their lives easier. figleaf developers want to add another layer of
features: flexible reporting, "depth" coverage, etc.

I'm balking.

Why?

I've noticed that experienced developers often have a strong and
largely consistent internal model of how things "should be": small
chunks of code, configurable, coupled in certain ways, etc.  The
details vary, of course, and that variation is the focus of intent
debates between developers, but there's an awful lot that's implicitly
shared in the world view of techies.

What's lacking, however, is a focus on simplicity, both simplicity of
use and simplicity of architecture.  This is where I think both twill
and figleaf shine: they're basically trivial packages that do
interesting things, reasonably well.  twill is a simple wrapper around
mechanize, but it gives you a preconfigured mechanize that can handle
80% or more of what non-AJAX-heavy Web sites do.  It's used in what I
think are slightly ridiculous numbers: 6000+ downloads in the last
year, not counting Debian installs.  figleaf is a simple wrapper
around sys.settrace, with some attached recording functionality; now
that I've tossed about 20% of the Python code, it's even simpler than
it was two weeks ago.  The code is straightforward to read in most
places and I'm working to make it simpler.  The coverage storage
format is trivial -- a dictionary of sets -- and that makes
serializing it and unpickling it equally trivial.  I have no idea how
many people are using figleaf, but I get a fair amount of interesting
e-mail from people when I break things, so I'd guess it's a reasonable
number.

I wish I could claim that the simplicity of my packages is a work of
genius.  Really, it's me being sick of stuff that doesn't work: Every
time I try to do something clever, I tie myself into knots.  If genius
is at work, it's the genius of my own stupidity, where I simply am not
smart enough to get complicated things to work.  To paraphrase
Kernighan, debugging is twice as hard as coding: if you write the code
as cleverly as you can, you're by definition not smart enough to debug
it.  That could be what's going on here.

Anyway, here's the kicker: people can install twill and
figleaf. People can understand the internals, people can tweak them,
and people can use them -- so people do.  I know this because of how
little e-mail I get, in comparison to the number of people that
casually mention that they're using the tools in conversation!
*Simplicity* turns out to be coupled to *usability*.

Two anecdotes.

Steve Holden did a "Teach Me Web Testing" tutorial, where the audience
tried to (interactively) teach him how to test his Web site.  A whole
bunch of things went wrong, and we basically ended up with only two
things that worked: twill and nose.  We had two hours; twill and nose
got installed in the first five minutes, and thing went downhill from
there.  We couldn't get Windmill working, because CherryPy couldn't be
easy_installed properly.  Selenium RC was triaged because *nobody*
wanted to watch Steve try to install it.  Steve already had Selenium
IDE installed (and anyway it's a Firefox plugin, so it Just Worked)
but we didn't get to the point of installing the static Selenium HTML.
I don't know how much of problem was caused by the rampant scotch
consumption, but I can pretty much guarantee you that twill and nose
can be easy_installed on *any* platform with virtually no trouble.

Second anecdote: I spent a bit of time talking with some people about
building a buildbot replacement that caters to people who just need
something simple (N.B., this was separate from the TIP discussion,
`"Everybody wants a Pony."
<http://lists.idyll.org/pipermail/testing-in-python/2009-March/001277.html>`__)
The air was full of terms like scalability, and configurability, and
interface programmability, and installability.  What I felt was
lacking was basic comprehension of what I want, nay, *need*: the twill
or figleaf of buildbothood.  I want something that is installable
*and* configurable in 5 minutes flat, on the master side, for a simple
open source project; the slave side should take 30 seconds or less.
Do I really need a binary twisted-sumo package for this??

Why do developers want to write complicated software?  Well, everybody
loves features.  Everybody loves to be clever (although I increasingly
aim to achieve cleverness by breadth, not depth ;).  Everybody loves
to solve the problem completely.  And, frankly, developers like to
code.  It takes experience, and perhaps a certain kind of idiot
savantishness, to *reject* code, to *remove* features.  I'm still
working on doing this, but I still feel like I'm ahead of the curve.

There are a few caveats to be mentioned.  I don't know how much of the
trouble here is caused by my refusal to consider complex needs; I'm
personally willing to jettison 20% of people if I can fulfill the
needs of the 80%.  YMMV, especially if you're in that 20%.  A number
of buildbot users told me I was nuts for wanting to move to something
simpler, that they couldn't conceive of using the system I described
because they had more complex needs.  Yes!  You're right!  Buildbot is
*awesome* for all sorts of reasons!  We need it!  But it's a pain in
the butt to install and configure out of the box, if all you need is
something that downloads a tar.gz and calls 'python setup.py test'.
I'm sure it drives people crazy to know that I want to rewrite yet
another testing framework (twill is a rewrite of PBP; figleaf is a
rewrite of coverage).  But I'm going to guess that people will use
ponybuild, if I can shave enough features off of it.  And how often do
you hear that kind of statement? ;)

Anyway, I'll conclude with this thought: extremism in the pursuit of
simplicity is no vice!

Ludditely yours,

--titus


----

**Legacy Comments**


Posted by dgou on 2009-04-03 at 23:14. 

::

   'twill developers want me to unpackage twill's dependencies from
   twill, and add features that make their lives easier. figleaf
   developers want to add another layer of features: flexible reporting,
   "depth" coverage, etc.'    I get not adding features (and support
   that).  I'm confused by the "unpackage twill's dependencies" part.
   Isn't decoupling dependencies a way to make software simpler? I'd like
   to hear your objections to that, specifically.    Thanks!


Posted by Jack Diederich on 2009-04-03 at 23:27. 

::

   Your post tries to dance between framework-vs-libraries and ends up
   concluding "Well, I tried!"  which is really all you can hope for.  A
   variaton on "As simple as possible and no more."  The distinction
   between small, reusable library parts and a bondage &amp; discipline
   framework is pretty thin in practice.    Unrelated: did you just out
   yourself as a classic liberal with the Goldwater paraphrase?  We're
   tolerated at PyCon dinners but invited mainly as a curiosity.


Posted by Titus Brown on 2009-04-03 at 23:54. 

::

   Hey Doug,    no, I think the answer is categorically not -- at least
   from the user or installer's perspective.    First, you have to posit
   a packaging system that works 100%.  easy_install doesn't.    Second,
   you have to hope that the dependencies are all available in the right
   version, for as long as your package will be distributed.    Third,
   you have to hope that the dependencies remain up to date with respect
   to patches.  It's a bit much for me to ask mechanize to release a new
   version because there's a 2-line fix that some twill user needs.
   From the developer's perspective, of course, throwing more technology
   at the problem is always the answer ;)    Which reminds me, I want to
   do a PyCon talk entitled "solving social problems with technology."
   Not sure what the actual topic would be, but it's a nice ironic title.
   --titus


Posted by Titus on 2009-04-04 at 00:33. 

::

   Jack, no particular reason for the quote -- just came up with it ;)


Posted by dgou on 2009-04-04 at 00:42. 

::

   Ah, excellent answer, it revealed a disconnect in the assumptions I
   was making and the ones you were making.    I was not intending to
   imply that because the code was decoupled that the packaging had to be
   decoupled. I agree that packaging/install is a nightmare. I see the
   simple solution as saying something like: Twill is made up of these
   three parts: A, B, C. When you package/install twill, you get all
   three. However, internal code structure is simpler because you've de-
   hairballed A, B, and C from each other. Nice side benefit is that
   other folks might take any or all of them and build something else
   too.    --doug


Posted by Michele Simionato on 2009-04-04 at 03:04. 

::

   +1000 Titus!  I agree 100% with everything you say. I just want to add
   a point. Simplicity is not only a virtue for users, but even for
   module writers. Take for instance my decorator module. It contains
   more or less 100 lines of code, it has been used for years by
   thousands of people, and I had basically never had any complaint or
   bug to fix. It just works.  No maintenance headache whatsoever.  And
   this not because I am particular smart, but  because it is difficult
   to get something wrong in  100 lines of code.  I had only one a minor
   glitch when I bend to an user request and I added a functionality that
   I immediately removed in the next version, since it was not really
   necessary.  Of course it is much more difficult to remove code than to
   add it, but it seems that people  willing to make that effort are in
   the minority.  Actually, most people do not even realize that  less
   features is a feature in itself.


Posted by Noah Gift on 2009-04-04 at 04:21. 

::

   I had some similar thoughts here on packaging:    <a
   href="http://artificialcode.blogspot.com/2009/03/dynamic-package-
   management.html">http://artificialcode.blogspot.com/2009/03/dynamic-
   package-management.html</a>    I still completely miss the point of
   all of this "on the fly" configuration for end users, it is the source
   of untold pain and suffering, when a simple tar file works 100% of the
   time.    On the ponybuild front, I do want one of those, because I
   like ponies :)


Posted by Titus Brown on 2009-04-04 at 10:13. 

::

   Doug, the internal structure of twill is pretty decoupled.  That's
   just good programming, as you point out ;).  Yes, I was using
   "unbundling" to mean "removing the packages from the distribution."
   Michele, +1000 backatcha ;)    Noah, stop spamming my blog with links
   to yours! ;)    (are you on planetpython?)


Posted by dgou on 2009-04-04 at 11:12. 

::

   Ok, got it now.    Semi-off-topic: I wonder if anyone has tried a
   hierarchical packaging system where the packaging of a tool (say
   twill) can provide by subsumption the packaging of other entities
   (libraries), which are none-the-less defined independently of their
   subsumers.    It seems there is a constant see-saw between "bundle
   everything together" (static linking) and "all dependencies are
   externally provided" (dynamic linking and DLL Hell on Windows). Middle
   ground there should be.    "I would not give a fig for the simplicity
   this side of complexity, but I would give my life for the simplicity
   on the other side of complexity."  --Oliver Wendel Holmes    -doug
   (not quite willing to give life itself :) for simplicity)


Posted by Augie Fackler on 2009-04-04 at 13:31. 

::

   You make a very good point here. I've been extremely hesitant to add a
   library dependency for hgsubversion simply because I know the moment I
   do, it's going to be a source of headaches for people that (for
   whatever reason) can't get it installed.    I suppose there's a flip
   side of this, when people want to depend on your code, but I guess
   there's nothing too terrible about having the "starter kit" which is a
   magical just-works download and also a "module version" which can
   depend on other libraries and so on.


Posted by Michael Foord on 2009-04-04 at 17:43. 

::

   Completely agree!


Posted by Marius Gedminas on 2009-04-05 at 10:31. 

::

   I think you just answered one long-standing question of mine: why have
   figleaf (or coverage) when trace.py is already in the stdlib.    I'm
   99% behind your sentiment: simple things should be simple.  However
   I'd also like complex things to be possible without ditching the
   simple solution and rewriting it from scratch.  This point of view
   looks at software from the outside and ignores any internal
   complications that would be necessary to make complex things possible.


Posted by <em>Mark</em> on 2009-04-05 at 23:34. 

::

   I went to the windmill openspaces session, at least partly to make
   sure I got over the initial install hurdles - after a couple of
   failures with easy_install, someone suggested virtualenv + PIP, and it
   "just worked".    That said, I always look for a debian package first
   :-)  (that path also gets you nose, and twill, but not selenium or
   windmill...)


Posted by Titus Brown on 2009-04-06 at 00:22. 

::

   Marius, does 'trace.py' tell you which lines should have been
   executed?


Posted by Scott on 2009-04-06 at 17:25. 

::

   Wow, beautifully written, very simple, elegant and to the point.


Posted by Rams on 2009-04-08 at 14:20. 

::

   That Kernighan quote about debugging is w.r.t to the code that a
   programmer writes, it's at least 4 times as difficult with other
   people's code.    This breadth vs depth issue finally boils down to
   one of taste. Programming is ultimately a design activity and taste
   makes a huge difference. Lots of brilliant programmers, startup
   founders, good users etc have bad taste.     Doesn't twill have a
   plugin architecture that allows users to implement extensions ? Thx.


Posted by Titus Brown on 2009-04-08 at 22:49. 

::

   Rams: yes, it has a plugin arch.

