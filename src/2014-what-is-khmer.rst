RFC: The khmer project: what are we, and what are our goals?
############################################################

:author: C\. Titus Brown
:tags: khmer,OSS
:date: 2014-11-19
:slug: 2014-what-is-khmer
:category: science

As we think about the next few years of khmer development, it is
helpful to explore what khmer is, and what our goals for khmer
development are.  This can provide guiding principles for development,
refactoring, extension, funding requests, and collaborations.

Comments solicited!

----

Links:

* khmer github repo: https://github.com/ged-lab/khmer/
* khmer docs: http://khmer.readthedocs.org/

Definition
----------

khmer is an open source project that serves as:

* a stable research platform for novel CS/bio research on data structures and algorithms, mostly k-mer based;

* a set of of command line tools for various kinds of data transformations;

* a test bed for software engineering practice in science;

* a Python library for working with k-mers and graph structures;

* an exercise in community building in scientific software engineering;

* an effort to participate in and sustainably grow the bioinformatics ecosystem.

Goals
-----

Our long term goals for khmer, in some rough order of priority, are:

* Keep khmer versatile and agile enough to easily enable the CS and
  bio we want to do.

  Practical implications: limit complexity of
  internals as much as possible.

* Continue community building.

  Practical implications: run khmer as a real open source project,
  with everything done in the open; work nicely with other projects.

* Build, sustain, and maintain a set of protocols and recipes around khmer.

  Practical implications: take workflow design into account.

* Improve the efficiency (time/memory) of khmer implementations.

  Practical implications: optimize, but not at expense of clean code.

  Some specifics: streaming; variable sized counters.

* Lower barriers to an increasing user base.

  Practical implications: find actual pain points, address if it’s easy or makes good sense.

  Some specifics: hash function k > 32, stranded hash function,
  integrate efficient k-mer cardinality counting, implement
  dynamically sized data structures.

* Keep khmer technologically up to date.

  Practical implications: transition to Python 3.

----

--titus

p.s. Thanks to Qingpeng Zhang, Travis Collier, and Matt MacManes for comments in the draft stage!
