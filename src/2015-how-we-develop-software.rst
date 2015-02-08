How we develop software (2015 version)
######################################

:author: C\. Titus Brown
:tags: khmer, oss
:date: 2015-02-08
:slug: 2015-how-we-develop-software
:category: science

A colleague who is starting their own computational lab just asked me
for some advice on how to run software projects, and I wrote up the
following.  Comments welcome!

----

A brief summary of what we've converged on for our own needs is this:      

* everything's on github (you can have private repos there, note)

* the khmer and screed projects are our two main software development
  projects, and we have an increasingly robust code contribution process;
  see http://khmer.readthedocs.org/en/v1.3/dev/getting-started.html for 
  a run through.

  https://github.com/ged-lab/khmer

  https://github.com/ged-lab/screed

  In particular, for these "reusable library" projects, we enforce code
  review, test coverage, and have continuous integration running.

  We've been writing up some of this here:

  http://files.figshare.com/1209108/wssspe13_ged.pdf

* we try to make distinctions between solidly tested and supported
  code, and experimental code; see `issue #471
  <https://github.com/ged-lab/khmer/issues/471>`__ for our decisions
  on this front (basically, we allow a certain amount of fragility in
  the sandbox/ directory).

* the khmer-recipes project is where we put little recipes that we
  want to make available, so these would be useful parts of data analysis
  pipelines but not entire pipelines;

  https://khmer-recipes.readthedocs.org/en/latest/

* the khmer-protocols project is where we put protocols that we would like
  to *support* - these are entire pipelines or protocols that show how to
  use our software on real data;

  https://khmer-protocols.readthedocs.org/en/latest/

* our papers are basically makefiles + scripts:

  http://ivory.idyll.org/blog/2014-our-paper-process.html

* we've started planning ahead and making roadmaps:

  http://khmer.readthedocs.org/en/v1.3/roadmap.html

----

--titus
