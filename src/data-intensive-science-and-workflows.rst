Data Intensive Science, and Workflows
#####################################

:author: C\. Titus Brown
:tags: bioinformatics,python,workflows,metagenomics,microsoftisstillevil
:date: 2011-12-11
:slug: data-intensive-science-and-workflows
:category: python


I'm writing this on my way back from Stockholm, where I attended a
workshop on the `4th Paradigm <http://research.microsoft.com/en-us/collaboration/fourthparadigm/>`__.  This is the idea (so named by Jim
Gray, I gather?) that data-intensive science is a distinct paradigm
from the first three paradigms of scientific investigation -- theory,
experiment, and simulation.  I was invited to attend as a token
biologist -- someone in biology who works with large scale data, and
thinks about large scale data, but isn't necessarily *only* devoted to
dealing with large scale data.

The workshop was pretty interesting.  It was run by Microsoft, who
invited me & paid my way out there.  The idea was to identify areas of
opportunity in which Microsoft could make investments to help out
scientists and develop new perspectives on the future of eScience.  To
do that, we played a game that I'll call the "anchor game", where we
divvied up into groups to discuss the blocks to our work that stemmed
from algorithms and tools, data, process and workflows,
social/organizational aspects. In each group we put together sticky
notes with our "complaints" and then ranked them by how big of an
anchor they were on us -- "deep" sticky notes held us back more than
shallow sticky notes.  We then reorganized by discipline, and put
together an end-to-end workflow that we hoped in 5 years would be
possible, and then finally we looked for short- and medium-term
projects that would help get us there.

The big surprise for me in all of this was that it turns out I'm most
interested in workflows and process!  All of my sticky notes had the
same theme: it wasn't tools, or data management, or social aspects
that were causing me problems, but rather the development of
appropriate workflows for scientific investigation.  Very weird, and
not what I would have predicted from the outset.

Two questions came up for me during the workshop:

**Why don't people use workflows in bioinformatics?**

The first question that comes to mind is, why doesn't anyone I know
use a formal workflow engine in bioinformatics?  I know they exist
(Taverna, for one, has a bunch of bioinformatics workflows); I'm
reasonably sure they would be useful; but there seems to be some
block against using them!

**What would the ideal workflow situation be?**

During the anchor game, our group (which consisted of two biologists,
myself and Hugh Shanahan; a physicist, Geoffrey Fox; and a few
computer scientists, including Alex Wade) came up with an idea for a
specific tool.  The tool would be a bridge between Datascope for
biologists and a workflow engine.  The essential idea is to combine
data exploration with audit trail recording, which could then be
hardened into a workflow template and re-used.

---

Thinking about the process I usually use when working on a new
problem, it tends to consist of all these activites mixed together:

0) evaluation of data quality, and application of "computational" controls

1) exploration of various data manipulation steps, looking for statistical signal

2) solidifying of various subcomponents of the data manipulation steps into scripted actions

3) deployment of the entire thing on multiple data sets

Now, I'm never quite done -- new data types and questions always come
up, and there are always components to tweak.  But portions of the
workflow become pretty solid by the time I'm halfway done with the
initial project, and the evaluation of data quality accretes more
steps but rarely loses one.  So it could be quite useful to be able to
take a step back and say, "yeah, these steps?  wrap 'em up and put 'em
into a workflow, I'm done."  Except that I also want to be able to
edit and change them in the future.  And I'd like to be able to post
the results along with the precise steps taken to generate them.  And
(as long as I'm greedy) I would like to work at the command line,
while I know that others would like to be able to work in a notebook
or graphical format.  And I'd like to be able to "scale out" the
computation by bringing the compute to the data.

For all of this I need three things: I need workflow *agility*, I need
workflow *versioning*, and I need workflow *tracking*.  And this all
needs to sit on top of a workflow component model that lets me run the
components of the workflow wherever the *data* is.

I'm guessing no tool out there does this, although I know other people
are thinking this way, so maybe I'm wrong.  The Microsoft folk didn't
know of any, though, and they seemed pretty well informed in this area
:).

The devil's choice I personally make in all of this is to go for
workflow agility, and ignore versioning and tracking and the component
model, by scripting the hell out of things.  But this is getting old,
and as I get older and have to teach my wicked ways to grad students
and postdocs, the lack of versioning and tracking and easy scaling out
gets more and more obvious.  And now that I'm trying to actually teach
computational science to biologists, it's simply appallingly difficult
to convey this stuff in a sensible way.  So I'm looking for something
better.

One particularly intriguing type of software I've been looking at
recently is the "interactive Web notebook" --
`ipython notebook <http://ipython.org/ipython-doc/dev/interactive/htmlnotebook.html>`__ and
`sagenb <http://sagenb.org/>`__. These are essentially Mathematica or matlab-style notebook
packages that work with IPython or Sage, scientific computing and
mathematical computing systems in Python.  They let you run Python
code interactively, and colocate it with its output (including
graphics); the notebooks can then be saved and loaded and re-run.  I'm
thinking about working one or the other into my class, since it would
let me move away from command-line dependence a bit.  (Command lines
are great, but throwing them at biologists, along with Python programming,
data analysis, and program execution all together, seems a bit cruel.
And not that productive.)

It would also be great to have cloud-enabled workflow components.  As
I embark on more and more sequence analysis, there are only about a
dozen "things" we actually do, but mixed and matched.  These things
could be hardened, parameterized into components, and placed behind an
RPC interface that would give us a standard way to execute them.
Combined with a suitable data abstraction layer, I could run the
components from location A on data in location B in a semi-transparent
way, and also record and track their use in a variety of ways.  Given
a suitably rich set of components and use cases, I could imagine that
these components and their interactions could be executed from
multiple workflow engines, and with usefully interesting GUIs.  I know
Domain Specific Languages are already passe, but a DSL might be a good
way to find the right division between subcomponents.

I'd be interested in hearing about such things that may already exist.
I'm aware of Galaxy, but I think the components in Galaxy are not
quite written at the right level of abstraction for me; Galaxy is also
more focused on the GUI than I want.  I don't know anything about
Taverna, so I'm going to look into that a bit more.  And, inevitably,
we'll be writing some of our own software in this area, too.

Overall, I'm really interested in workflow approaches that let me transition
seemlessly between `discovery science <http://ivory.idyll.org/blog/dec-11/is-discovery-science-really-bogus.html>`__ and "firing for effect" for hypothesis-driven science.

A few more specific thoughts:

In the area of metagenomics (one of my research focuses at the
moment), it would be great to see `img/m
<http://img.jgi.doe.gov/cgi-bin/m/main.cgi>`__, `camera
<http://camera.calit2.net/>`__, and `MG-RAST
<http://metagenomics.anl.gov/>`__ move towards a "broken out" workflow
that lets semi-sophisticated computational users (hi mom!) run their
stuff on the Amazon Cloud and on private HPCs or clouds.  While I
appreciate hosted services, there are many drawbacks to them, and I'd love
to get my hands on the guts of those services.  (I'm
sure the MG-RAST folk would like me to note that they are moving
towards making their pipeline more usable outside of Argonne:
`so noted <https://github.com/MG-RAST/MG-RAST-pipeline>`__.)

In the comments to my post on `Four reasons I won't use your data
analysis pipeline
<http://ivory.idyll.org/blog/dec-11/four-reasons-i-wont-use-your-data-analysis-pipeline.html>`__,
Andrew Davison reminds me of VisTrails, which some people at the MS
workshop recommended.

I met David De Roure from `myExperiment
<http://www.myexperiment.org/>`__ at the MS workshop.  To quote,
"myExperiment makes it easy to find, use, and share scientific
workflows and other Research Objects, and to build communities."

David put me in touch with Carole Goble who is involved with
`Taverna <http://www.taverna.org.uk/>`__.  Something to look at.

In the `cloud computing workshop
<http://pag.confex.com/pag/xx/webprogrampreliminary/Session1139.html>`__
I organized at the Planet and Animal Genome conference this January, I
will get a chance to buttonhole one of the Galaxy Cloud developers.  I
hope to make the most of this opportunity ;).

It'd be interesting to do some social science research on what
difficulties users encounter when they attempt to use workflow
engines.  A lot of money goes into developing them, apparently, but at
least in bioinformatics they are not widely used.  Why?  This is sort
of in line with Greg Wilson's Software Carpentry and the wonderfully
named blog `It will never work in theory
<http://www.neverworkintheory.org/>`__: rather than guessing randomly
at what technical directions need to be pursued, why not study it
empirically?  It is increasingly obvious to me that improving
computational science productivity has more to do with lowering
learning barriers and changing other societal or cultural issues than
with a simple lack of technology, and figuring out how (and if)
appropriate technology could be integrated with the right incentives
and teaching strategy is pretty important.

--titus

p.s. Special thanks to Kenji Takeda and Tony Hey for inviting me to the
workshop, and especially for paying my way.  'twas really interesting!


----

**Legacy Comments**


Posted by Mary on 2011-12-11 at 11:23. 

::

   We know why they aren't using workflows. They aren't **trained** in
   using them. We've seen how eager they are once they see Galaxy. They
   totally get it, and why it could help them.     But first nobody
   showed them the UCSC Table Browser until we got there either. Or
   BioMart. Or other data sources that they need to get the data to start
   with.    I could go into a whole separate rant on how naive users need
   to be trained--but here's a protip: if you are too close to your own
   tools, you are skipping a LOT of intro stuff that new users need to
   know. And because you represent your tool they are afraid to tell you.
   And they don't want to look stupid on front of their colleagues, so
   they pretend they get it.     \/&lt;end rant&gt;


Posted by Casey Bergman on 2011-12-11 at 12:42. 

::

   "I'd be interested in hearing about such things that may already
   exist."    A list of alternative bioinformatics workflow systems to
   Galaxy and Taverna has been compiled here: <a href="http://en.wikipedi
   a.org/wiki/Bioinformatics_workflow_management_systems">http://en.wikip
   edia.org/wiki/Bioinformatics_workflow_management_systems</a>


Posted by Mary on 2011-12-11 at 13:32. 

::

   Casey: do you edit that wiki page? If so, add ClovR too: <a
   href="http://clovr.org/">http://clovr.org/</a>


Posted by Deepak on 2011-12-11 at 17:28. 

::

   So when you talk about workflows are you talking about the informatics
   types or the bench types.  IMO the former are best served by having
   APIs that they can then pull together in a way they see fit and then
   package all that up.  They could even deploy those packages in
   Taverna, Galaxy, etc.  The latter on the other hand, are probably best
   served by a visual framework or by quasi-black boxes.      The biggest
   impediment still is a lack of computational thinking. Even many
   "informtics" types, can't really code and think about services, etc,
   which is a shame.


Posted by Greg Wilson on 2011-12-11 at 18:57. 

::

   1. Are you going to do the anchor exercise with your grad
   students/research collaborators?  Uncovered something interesting for
   you; might for them.    2. A couple of years ago, I had a very good
   undergrad student spend a term trying to get a simple workflow going
   in Taverna, Kepler, and a homegrown system.  Long story short, he
   couldn't: install this, configure that, blah blah blah, eventually
   defeated him.  Lots of researchers don't have access to sys admins
   with the skills and time to get over these hurdles; those who do are
   often very wary of investing in something that could all too easily
   break underneath them.    Now, if Microsoft really wants to help, let
   'em build a science-friendly, process-run-wherever version of
   PowerShell... :-)


Posted by Titus Brown on 2011-12-11 at 22:48. 

::

   Mary -- good points.  It's one of the reasons I shy away from
   presenting my own tools and approaches in intro workshops (like the
   ngs course we run).    Deepak, good points all.  I think we need a
   workflow system that experts can extend and then give to local non-
   experts.  So, both.    Greg, yeah, installation's a bitch.  We've had
   some local help at our HPC and that's worked out reasonably well...
   but still... I think the cloud is a great opportunity here, but not in
   the "pre-packaged AMI sense" but rather in the "if you can't get
   people to successfully install it on a clean machine, then shoot
   yourself now"... a message some, at least, are resistant to.
   --titus


Posted by satra on 2011-12-12 at 14:43. 

::

   @titus:    we have been developing a python-based workflow system for
   neuroimaging called nipype (nipy.org/nipype;doi:
   10.3389/fninf.2011.00013 ) which might at a basic level address those
   requirements you speak of. could you please clarify what exactly you
   mean by these terms: agility, versioning, tracking?    our primary
   goal was flexibility. we needed a framework that:  - was lightweight
   and scriptable  - ran locally as well as on clusters  - one could
   easily plugin new functionality  - was adaptable to different use-
   cases


Posted by S. Joshua Swamidass on 2011-12-13 at 14:36. 

::

   I'd be happy to explain to you the system we are using, a modified
   version of scons, and the specific difficulties we are encountering.
   This is a ripe area for a new tool that does it right.

