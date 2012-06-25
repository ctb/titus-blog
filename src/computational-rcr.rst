What does responsible conduct of computational research look like?
##################################################################

:author: C\. Titus Brown
:tags: rcr,swc
:date: 2012-05-22
:slug: computational-rcr
:category: science


Greg Wilson, Ethan White and I have been talking a bit about what
Responsible Conduct of Research (RCR) standards would look like for
computational science.  I'm having trouble coming up with more than
the below standards, which are largely related to publication.

Note, if you regard these as obvious, that's great!  I'm more
interested in codifying accepted practice than in breaking new
ground here.

1. Record provenance of computational tools.

The exact version of all tools used for the purpose of research,
including modeling tools, primary data filtering tools, format
conversion scripts, analysis software, and statistical analysis and
graphing code, is part of the research.

Best practice is to use some form of version control software for any
software and tools developed within a project.  For other tools such
as commercial software packages or external tools not developed within
the project, the version used for research should be recorded.

2. Software parameters need to be recorded.

All parameters used in any stage of data analysis or model
execution are part of the research, and must be recorded.

One good practice is to automate the data analysis in a pipline, and
then use version control to store the data analysis pipeline.

3. Experimental data must be archived, where possible.

During data analysis, data may be analyzed and reduced in several
stages.  The raw data should be archived; if that's not possible due
to data size, then data should be archived at as early a stage as
is possible.

4. Any computational approaches used in the process of producing
   results are part of the core research project and should be viewed as
   such.

For example, computational approaches are methods that need
to be described for publication and also need to be replicable.

The underlying principle for these rules is that, in accordance with
standard journal guidelines and practice of science in general,
research must be replicable within the lab and (for publication) by
reviewers.  It's easy to get lost in the details -- for example, what
if reviewers don't have access to the compute resources necessary to
run the analysis pipeline? -- but these are distractions, I think.
The core principle is that of replication: the researchers,
collectively must be able to replicate their own research; reviewers
with access to similar resources must also be able to replicate
the research, at least in theory.

I was thinking about putting in something about using computation
for hypothesis generation vs hypothesis validation, and how the
use of data and statistics could change -- I regard hypothesis
generation as less subject to replication concerns, for example,
as long as the generated hypotheses are validated -- but maybe
that gets too close to something field specific.

--titus


----

**Legacy Comments**


Posted by Jonthan Dursi on 2012-05-23 at 10:20. 

::

   I like these; I think they could usefully be reordered, though.  Item
   #4 seems like it's clearly the most important item; 1 and 2 are almost
   subsets of 4.     When I see computational papers that I have trouble
   replicating, it's almost always because something <em>wasn't</em>
   treated as part of the core project: "...and then from x we computed
   y.." without giving any clear picture of how they went from x to y.
   In an experimental/observational paper that would have a much harder
   time getting past a referee, whereas it's all too common in
   computational work still.    It's less clear to me that #3 has
   anything to do with computational research per se at all; that
   experimental data should be kept is absolutely true, but it seems like
   that's a statement about experimental science.


Posted by Ben on 2012-05-23 at 10:22. 

::

   I'm not sure exactly how it would fit in, but some sort of change log
   documenting what changes between software versions, and why such
   changes were made, also seems important.    In my work, I particularly
   miss this when a group releases an updated version of a model.


Posted by Titus Brown on 2012-05-23 at 12:42. 

::

   Thanks guys, very helpful!  Jonathan, I'd simply point out that much
   of computational science **does** deal with experimental data at one
   point or another, so it seems like an important point to me :)


Posted by Andrew Davison on 2012-05-24 at 08:35. 

::

   I wish these seemed obvious to most of my colleagues. In my field, at
   least (computational neuroscience), they seem to be far from accepted
   practice.    I think one reason for this is that recording the exact
   versions of all tools, and all the values of all parameters, can be
   very tedious and time consuming (for example, when your main program
   depends on a dozen or so libraries, each of which has a half-dozen
   dependencies of its own, and so on), and it is easy to let these
   things go by the board, especially when rushing to meet a deadline.
   Another reason is that using formal pipeline tools can have a large
   initial energy barrier and involve a large change to a scientist's
   workflow.    You might be interested in looking at my project Sumatra
   (http://packages.python.org/Sumatra/), which aims to provide a toolkit
   to automate the capture of version information, paths to archived
   data, parameters, etc. with minimal changes to existing workflows.
   (By the way, if anyone finds this interesting, Sumatra could really
   benefit from more contributors to expand the range of scientific
   workflows it can cover. We have a Google Summer of Code student,
   Dmitry Samarkanov, who is going to work on improving experiment
   browsing and querying, and on dependency-tracking for Matlab, but more
   help is always welcome!)    Another useful lightweight tool for
   capturing the exact software environment used to produce a
   computational result, without going as far as doing all your research
   in a virtual machine, is Philip Guo's CDE
   (http://www.pgbovine.net/cde.html).    More generally, I think that
   Responsible Conduct of Research standards for computational science
   should include things like:   * sensitivity analysis (demonstrating
   that your result is robust in the face of small parameter changes);
   * appropriate use of random number generators;   * appropriate use of
   statistical tests (not limited to computational science, of course);
   * adequate anonymization when using sensitive data (cf <a
   href="http://33bits">http://33bits</a>.org/);   * testing that the
   software you are using really does what it is supposed to do/what you
   think it is doing.    Thanks to you, Greg and Ethan for taking the
   initiative in this area. It would be great to have a document I could
   point my students to and say: "do this!"


Posted by Ethan White on 2012-05-24 at 11:01. 

::

   Looks great. I think this pretty much covers the big stuff.    In
   response to Jonathan's comment I wonder if just making point 3 a bit
   more explicit by pulling in some of what is already in the description
   and adding an explicit link to the computational tools to make it
   something like    3. Experimental data must be archived, with the
   computational tools, in the rawest state possible.    I'm flexible on
   the "with the computational tools" part, though I do think it's
   important and that's the direction we are moving.  If the raw data is
   just in a notebook or on a separate computer somewhere it doesn't
   accomplish the same thing. I think that the "rawest state possible"
   part is something that is often overlooked in that folks like to
   "clean" data before presenting it and we end up loosing the ability to
   evaluate the cleaning step (this happens all the time in ecology and
   we end up not being able to use some great datasets if the method for
   "cleaning" it goes out of style.


Posted by Jonthan Dursi on 2012-05-27 at 14:48. 

::

   "much of computational science does deal with experimental data at one
   point"    Well, sure, computational science deals with lots of things,
   I just don't understand why this particular one and not others are
   specifically called out.    If the idea is that all inputs --
   experimental data or synthetic data or parameters or tabulated rates
   for some process or whatever -- should be archived, then by all means.
   In that case, I'd suggest making #4 a preamble, and merge 2 and 3 into
   talking about all inputs, rather than pulling experimental data out
   seperately.  I also like Ethan's comment about "rawest state
   possible"; in some situations (LHC, SKA) storing all of the raw input
   data without some processing just can't be done.    So it would look
   something like:    As computational approaches to science become more
   and more important, the computational processes of producing results
   are part of the core research project just as much as theoretical
   derivations and experimental methods are, and should be viewed as
   such.  This means that responsible computational research must:     *
   Record and archive all inputs to the computational process: this
   includes software parameters used, input data sets, tables used in
   calculation, etc.  Such inputs should be archived in well-documented
   data formats that will be accessible even if particular tools stop
   being developed.     * Record and describe the provenance of
   computational tools used: record particular software versions,
   analysis software, etc.      * Describe computational methods and
   workflows in such a way that other researchers can replicate the
   computational process used in your work.  In the case of in-house
   software, this means describing in replicatable detail the methods
   used in the software to produce the results.

