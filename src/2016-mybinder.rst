Is mybinder 95% of the way to next-gen computational science publishing, or only 90%?
#####################################################################################

:author: C\. Titus Brown
:tags: docker,mybinder,reproducibility
:date: 2016-02-17
:slug: 2016-mybinder
:category: science

If you haven't seen `mybinder.org <http://mybinder.org>`__, you should
go check it out.  It's a site that runs IPython/Jupyter Notebooks from
GitHub for free, and I think it's a solution to publishing
reproducible computational work.

For a really basic example, take a look at `my demo Software
Carpentry lesson
<http://mybinder.org/repo/ctb/2016-mybinder-inflammation>`__.  Clicking
on that link brings up a Python notebook that will load and plot some
data; it's interactive and you can go ahead and execute the cells.



There are a couple of really appealing things about this.

First, it's simple -- `the source repository
<https://github.com/ctb/2016-mybinder-inflammation>`__ is just a
directory that contains a Jupyter notebook and some data.  It's pretty
much what you'd have if you were actually, you know, doing data
analysis with data in a repo.

Second, it's built on top of solid technology.  mybinder's
foundation is `Docker <http://docker.com>`__ and `Jupyter Notebook
<http://jupyter.org/>`__, both of which are robust and have large,
supportive communities.  Sure, behind the scenes, mybinder is using
some bleeding edge tech (`Kubernetes <http://kubernetes.io/>`__
running on `Google Compute Engine
<https://cloud.google.com/compute/>`__) to provision and load balance
the compute.  But I bet it would take me no more than 30 minutes to
cobble together something that would let me run any
mybinder-compatible repository on my laptop, or on any compute server
that can run Docker.

Third, it's super configurable -- because it's based on Docker, you
can install pretty much anything you want.  I tested this out myself
by installing R and an R kernel for the Jupyter notebook -- see this
`mybinder link
<http://mybinder.org/repo/ctb/2016-mybinder-irkernel>`__ and `repo
<https://github.com/ctb/2016-mybinder-irkernel>`__.  `The Dockerfile
<https://github.com/ctb/2016-mybinder-irkernel/blob/master/Dockerfile>`__
that installs things is pretty straightforward (given that installing
all that stuff isn't straightforward in the first place ;).

Fourth, it's `open source <https://github.com/binder-project/binder>`__.
Go ahead, do what you want with it!

I believe mybinder is the hitherto missing link for publishing reproducible
computation.  Before this, we could give people our data and our data
analysis scripts, but not our compute environment - or at least not in
a way that was easy to run.  We can now provide readers with a link
that they can use to instantly go from my paper to a running
instantiation of my paper's data analysis.

What's missing and easy?
------------------------

**Authentication and Cost:** right now, mybinder is running on
someone else's dime -- specifically, `the Freeman Lab's dime
<https://www.janelia.org/lab/freeman-lab>`__.  This can't continue
forever, especially since it's totes open for abuse.  I expect that
sooner or later someone will gin up a way to run this on many cloud
compute services; once that works, it should be pretty easy to
build a site that redirects you to your favorite compute service
and lets you enter your own credentials, then *boom* there you go.
Insta-compute.

(I think current mybinder limitations are in the several GB of RAM
range, with a few dozen MB of disk space.)

**Executing anything other than GitHub public repos:** mybinder only
runs off of public GitHub repositories right now, but that's not going
to be too tricky to fix, either.  BitBucket and GitLab and private
repos can be served almost as easily.

**RStudio and RMarkdown:** currently, it's all Project Jupyter, but
it should be pretty easy to get RStudio Server or some sort of
RMarkdown application (Shiny?) working on it.

**Pre-built Docker images:** you need to derive your Dockerfile from
the ``andrewosh/binder-base`` image, which means you can't use
pre-built images from the Docker Hub (even if they were built from
binder-base).  I predict that will go away soon enough, since it's not
a fundamental requirement of the way they're doing things.

What's missing and not easy?
----------------------------

**Big files and big/long compute:** Coordinating the delivery of big
files, big compute, and big memory (potentially for a long period of
time) is something that's out of easy reach, I think.  Docker isn't
ready for really data-intensive stuff, from what I can tell.  More,
I'm not sure when (if ever) people will completely automate the
heavyweight data analysis - surely it's further away than most people
using Jupyter or RStudio for data analysis.

The split that my lab has made here is to use a workflow engine
(e.g. make, pydoit, or snakemake) for the compute & data intensive
stuff, and then feed those intermediate results (assembly and mapping
stats, quantification, etc.) into analysis notebooks.  For mybinder
purposes, there should be no problem saving those intermediate results
into a github repo for us and everyone else to analyze and reanalyze.

What are the next steps?
------------------------

I bet this will evolve pretty fast, because it's an easy way for
scientists to deliver compute to friends, colleagues, and students.

In terms of learning how to make use of mybinder, `Software Carpentry
<http://software-carpentry.org>`__ already teaches scientists how to
do much of the necessary stuff -- scripting, git, and Jupyter
Notebooks are all part of the standard curriculum.  It's not a big
leap to show students some simple Docker files.  There's virtually no
unnecessary configuration required at the moment, which is a big win;
we can talk about why everything is actually important for the end
result, which is <ahem> not always the case in computing.

Beyond that, I'm not sure where the gaps are - as usual we're missing
incentives for adopting this, so I'd be interested in thinking about
how to structure things there.  But I look forward to seeing how this
evolves!

--titus

p.s. `Everware
<https://betatim.github.io/posts/project-everware-reusable-science/>`__
does something similar to mybinder. I'm aware of it, I just haven't
had the chance to try it out - I'd love to hear from people who have used
it!

p.p.s. For a real, and super cool, example of mybinder, see: Min
Ragan-Kelly's `LIGO/gravitational waves tutorial
<https://twitter.com/minrk/status/698172792072761344>`__.
