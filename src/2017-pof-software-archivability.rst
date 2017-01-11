How I learned to stop worrying and love the coming archivability crisis in scientific software
##############################################################################################

:author: C\. Titus Brown
:tags: futurepaper
:date: 2017-01-11
:slug: 2017-pof-software-archivability
:category: science

Note: This is the fifth post in a mini-series of
blog posts inspired by the workshop `Envisioning the Scientific Paper
of the Future
<http://caltech.stacksdiscovery.org/scientific-paper-future>`__.

This post was put together *after* the event and benefited greatly
from conversations with Victoria Stodden, Yolanda Gil, Monya Baker,
Gail Peretsman-Clement, and Kristin Antelman!

----

Archivability is a disaster in the software world
-------------------------------------------------

In `The talk I didn't give at Caltech <http://ivory.idyll.org/blog/2017-pof-the-talk-i-didnt-give.html>`__, I pointed out that our current software stack
is connected, brittle, and non-repeatable.  This affects our ability to
store and recover science from archives.

Basically, in our lab, we find that our executable papers routinely
break over time because of minor changes to dependent packages or
libraries.

Yes, the software stack is constantly changing!  Why?!

Let me back up --

Our analysis routines usually depend on an extensive hierarchy of
packages.  We may be writing bespoke scripts on top of our own library,
but those scripts and that library sit on top of other libraries, which
in turn use the Python language, the GNU ecosystem, Linux, and a bunch
of firmware.  All of this rests on a not-always-that-sane hardware
implementation that occasionally throws up errors because x was compiled
on y processor but is running on z processor.

We've had every part of this stack cause problems for us.

Three examples:

* many current repeatability stacks are starting to rely on Docker.
  But Docker changes routinely, and it's not at all clear that the
  images you save today will work tomorrow.  Dockerfiles (which
  provide the instructions for building images) should be more robust,
  but there is a tendency to have Dockerfiles run complex shell
  scripts that may themselves break due to software stack changes.

  But the bigger problem is that Docker just isn't that robust.

  Don't believe me? For more, read this and weep: `Docker in
  Production: A history of Failure
  <https://thehftguy.com/2016/11/01/docker-in-production-an-history-of-failure/>`__.

* software stacks are astoundingly complex in ways that are mostly
  hidden when things are working (i.e. in the moment) but that block
  any kind of longitudinal robustness.  Perhaps the best illustration
  of this in recent time is the JavaScript debacle where the author of
  "left-pad" pulled it from the packaging system, `throwing the
  JavaScript world into temporary insanity
  <http://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos/>`__.

* practically, we can already see the problem - go sample from
  `A gallery of interesting Jupyter Notebooks <https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks>`__.  Pick five. Try to
  run them.  Try to install the stuff needed to run them. Weep in despair.

  (This is also true of mybinder repos, just in case you're wondering;
  many of my older ones simply don't work, for a myriad of reasons.)

These are big, real issues that affect any scientific software that relies
on any code written outside their project (which is everyone - see "Linux
operating system" and/or "firmware" above.)

**My conclusion is that, on a decadal time scale, we cannot rely on software
to run repeatably.**

This connects to two other important issues.

First, since `data implies software
<http://ivory.idyll.org/blog/2017-data-implies-software.html>`__,
we're rapidly moving into a space where the long tail of data is going
to become useless because the software needed to interpret it is
vanishing.  (We're already seeing this with 454 sequence data, which
is less than 10 years old; very few modern bioinformatics tools will
ingest it, but we have an awful lot of it in the archives.)

Second, it's not clear to me that we'll actually *know* if the
software is running robustly, which is far worse than simply having it
break.  (The situation above with Jupyter Notebooks is hence less
problematic than the subtle changes in behavior that will come from
e.g. Python 5.0 fixing behavioral bugs that our code relied on in
Python 3.)

I expect that in situations where language specs have
changed, or library bugs have been fixed, there will simply be silent
changes in output.  Detecting this behavior is hard.  (In our own
khmer project, we've started including tests that compare the md5sum
of running the software on small data sets to stored md5sums, which
gets us part of the way there, but is by no means sufficient.)

If archivability is a problem, what's the solution?
---------------------------------------------------

So I think we're heading towards a future where even perfectly
repeatable research will not have any particular longevity, unless
it's constantly maintained and used (which is unrealistic for most
research software - heck, we can't even maintain the stuff we're using
right now this very instant.)

Are there any solutions?

First, some things that definitely aren't solutions:

* Saving ALL THE SOFTWARE is not a solution; you simply can't, because
  of the reliance on software/firmware/hardware interactions.

* Blobbing it all up in a gigantic virtual machine image simply pushes
  the turtle one stack frame down: now you've got to worry about keeping
  VM images running consistently.  I suppose it's possible but I don't
  expect to see people converge on this solution anytime soon.

  More importantly, VMs and docker images may let you reach bitwise
  reproducibility, but they're not scientifically *useful* because
  they're big black boxes that don't really let you reuse or remix the
  contents; see `Virtual machines considered harmful for
  reproducibility
  <http://ivory.idyll.org/blog/vms-considered-harmful.html>`__ and
  `The post-apocalyptic world of binary containers
  <http://ivory.idyll.org/blog/2014-containers.html>`__.

* Not using or relying on other software isn't a practical solution:
  first, good luck with that ;).  Second, see "firmware", above.

  And, third, while there is definitely a crowd of folk who like to
  reimplement everything themselves, there is every likelihood that
  their code is wronger and/or buggier than widely used community
  software; Gael Varoquaux makes this point very well in his blog
  post, `Software for reproducible science
  <http://gael-varoquaux.info/programming/software-for-reproducible-science-lets-not-have-a-misunderstanding.html>`__.

  I don't think trading archivability for incorrectness is a good trade :).

The two solutions that I do see are these:

* run everything all the time.

  This is essentially what the software world does with continuous integration.
  They run all their tests and pipelines all the time, just to check that
  it's all working.  (See `"Continuous integration at Google Scale" <www.slideshare.net/JohnMicco1/2016-0425-continuous-integration-at-google-scale>`__.)

  Recently, my #MooreData colleagues Brett Beaulieau and Casey Greene
  proposed exactly this for *scientific* papers, in their preprint
  `"Reproducible Computational Workflows with Continuous Analysis"
  <http://dx.doi.org/10.1101/056473>`__.

  While this is a potential solution, it's rather heavyweight to set
  up, and (more importantly) it gets kind of expensive -- Google runs
  many compute-years of code each *day* -- and I worry that the cost to
  utility ratio is not in science's favor.  This is especially true
  when you consider that most research ends up being a dead end -
  unread, uncited, and unimportant - but of course you don't know which until
  much later...

* acknowledge that exact repeatability has a half life of utility, and that
  this is OK.

  I've only just started thinking about this in detail, but it is at
  least plausible to argue that we don't really care about our ability
  to exactly re-run a decade old computational analysis.  What we *do*
  care about is our ability to figure out *what* was run and what the
  important decisions were -- something that Yolanda Gil refers to as
  "inspectability."  But exact *repeatability* has a short shelf-life.

  This has a couple of interesting implications that I'm just starting to
  unpack mentally:

  * maybe repeatability for science's sake can be thought of as a
    short-term aid in peer review, to make sure that the methods are
    suitably explicit and not obviously incorrect.  (Another use for
    exact repeatability is enabling `reuse and remixing
    <http://ivory.idyll.org/blog/research-software-reuse.html>`__, of
    course, which is important for scientific progress.)

  * as we already knew, closed source software is useless crap because
    it satisfies neither repeatability nor inspectability. But maybe
    it's not that important (for inspectability) to allow software
    reuse with a F/OSS license? (That license is critical for reuse
    and remixing, though.)

  * maybe we could and should think of articulating "half lives" for
    research products, and acknowledge explicitly that most research
    won't pass the test of time.

  * but perhaps this last point is a disaster for the kind of
    serendipitous reuse of old data that Christie Bahlai and Amanda
    Whitmire have convinced me is important.

  Huge (sincere) thanks to Gail for arguing both sides of this,
  including saying that (a) archive longevity is super important
  because everything has to be saved or else it's a disaster for
  humanity, and (b) maybe we don't care about saving everything
  because after all we can still read Latin even if we don't actually
  get the full cultural context and don't know how to pronounce the
  words, and (c) hey maybe the full cultural context is important and
  we should endeavor to save it all after all.
  <exasperation>Librarians!</exasperation>

Lots for me to think on.

--titus
