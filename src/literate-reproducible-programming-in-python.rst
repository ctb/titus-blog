How can we do literate programming for reproducibility, in Python?
##################################################################

:author: Yarden Katz
:tags: python,science,open science
:date: 2013-07-13
:slug: literate-reproducible-programming-in-python
:category: python

*Note*: `Yarden Katz <http://www.mit.edu/~yarden/>`__ (the author of
`MISO <http://genes.mit.edu/burgelab/miso/index.html>`__) sent me the
e-mail below, and I asked him if I could post it as a guest-post on my
blog.  He said yes - so here it is!  Feedback solicited.

---

Hi Titus,

Hope all is well.  A recent tweet you had about Ben Bolker's `notes for
lit.  programming in R <http://stevencarlislewalker.wordpress.com/2013/07/12/ben-bolkers-notes-on-workflows-pipelines-reproducible-research-etc/>`__ (via @hylopsar) made me think about the same for Python, with
has been bugging me for a while.  Wanted to see if you have any
thoughts on getting the equivalent in Python.

What I've always wanted in Python is a way to simultaneously document
and execute code that describes an applied analysis pipeline.  Some
easy way to declaratively describe and document a step-by-step
analysis pipeline: Given X datasets available from some web resource,
which depends on packages / tools Y, download the data and run the
pipeline and ensure that you get results Z.  I'd like a language that
allows a description that is easily reproducible on a system that's
not your own, and forces you to declaratively state things in such a
way that you can't cheat with hardcoded paths or quirky
settings/versions of software that apply only to your own system.  A
kind of "literate" pipeline for applied analysis pipelines that allows
you to state your assertions/expectations along the way.

One of the main advantages of R over Python is that they have a
packaging system that actually works, where as
pip/setuptools/distribute are all broken and hard to use, even for
Python experts, let alone people who don't want to delve into the guts
of Python.  So ideally I'd like a system that takes this description
of the code and the inputs and executes on a *new* virtual
environment.  readthedocs.org does this for documentation, and it's a
great way to ensure that you don't have unnoticed hardcoded paths, or
Python libraries or packages that cannot be fetched by package
managers.  Because Python libraries are so hopelessly complicated and
broken, and because in comp. bio we rely so often on external tools
(tophat version/bowtie version/etc.) this is all the more important.
Something that ensures that if you follow these steps, with these
data, it'll be automatically installable on your system, and give you
the expected output -- no matter what!  Knowing that it runs on a
server other than your own is key.

Some related tools/ideas that haven't worked very well for me for this
purpose, or that only partially address this:

- IPython notebook: I've had issues with IPython in general, but even
  when it works, it doesn't address the problem of describing
  systematically the input and output of the problem, which is key in
  analysis pipelines.  It also doesn't give you a way to state
  dependencies.  If I have a series of calls to numpy/scipy/matplotlib
  and I want to share that with you, it's good, but an applied analysis
  pipeline is far more complex than using a bunch of commonly available
  Python packages to get an output.

- Unit tests: Standard unit tests are OK for generic software tools.
  But they don't really make sense for applied analysis pipelines, where
  the software that you're writing is basically a bunch of analysis (and
  possibly plotting) code, and not a generic algorithm.  You're not
  testing internal Python library calls, and testing is only a small
  component of the goal (the other part is describing dependencies and
  data, and how the pipeline works).  You're trying to describe a flow
  of sequential steps, with forced assertions and conditions for
  reproducibility.  Some of these steps might not be fully automated, or
  might take far too long to run as a unit test.  So what I'm looking
  for is closer to some kind of sphinx/pydoc document interspersed with
  executable code, than a plain Python file with unit tests.

- Ruffus: It's too complicated for most things in my view and it
  doesn't give you a way to describe the data inputs, etc.  It's best
  for pipelines that consist of internal Python functions that exist
  within a module, but it gives you no features for describing
  interaction with external world (external input data, external tools
  of a specific version whose output you process.)  that forces you to
  get things somewhat right is Sphinx/Pydoc.  It was for Pycogent which
  I occasionally contribute it to, and they had configured it so that
  all the inline examples in the sphinx .rst file were run in real time.
  That's nice though it's still running only on your own environment and
  has no features for describing complex data sets / inputs, it was
  really made for testing library calls within a Python package (like an
  IPython notebook) -- again, not meant for data-driven pipelines.

The ideal system would even allow you to register analysis pipelines
or Python functions in some kind of web system, where each analysis
can get a URI and be run with a single click dispatched to some kind
of amazon node.  But that's not necessary and I don't use the cloud
for now.

Would love to hear your thoughts (feel free to share with others who
might have views on this.) I've thought about this for a while and
never found a satisfactory solution.

Thanks very much!

Best,

--Yarden
