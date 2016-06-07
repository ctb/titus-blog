Data intensive biology in the cloud: instrumenting ALL the things
#################################################################

:authors: C\. Titus Brown, Leigh Sheneman, Qingpeng Zhang, Chris Welcher, Michael Crusoe
:tags: python,dib
:date: 2013-09-10
:slug: pycon14-sub
:category: python

Here's a draft PyCon '14 proposal.  Comments and suggestions welcome!

----

Title: Data intensive biology in the cloud: instrumenting ALL the things

Description: (400 ch)

Cloud computing offers some great opportunities for science, but most
cloud computing platforms are both I/O and memory limited, and hence
are poor matches for data-intensive computing.  After four years of
research software development we are now instrumenting and benchmarking
our analysis pipelines; numbers, lessons learned, and future plans
will be discussed. Everything is open source, of course.

Audience: People who are interested in things.

Python level: Beginner/intermediate.

Objectives: 

Attendees will

* learn a bit about I/O and big-memory performance in demanding situations;
* see performance numbers for various cloud platforms;
* hear about why some people can't use Hadoop to process large amounts of data;
* gain some insight into the sad state of open science;

Detailed abstract:

The cloud provides great opportunities for a variety of important
computational science challenges, including reproducible science,
standardized computational workflows, comparative benchmarking, and
focused optimization.  It can also help be a disruptive force for the
betterment of science by eliminating the need for large infrastructure
investments and supporting exploratory computational science on
previously challenging scales.  However, most cloud computing use in
science so far has focused on relatively mundane "pleasantly parallel"
problems.  Our lab has spent many moons addressing a large,
non-parallelizable "big data/big graph" problem -- sequence assembly
-- with a mixture of Python and C++, some fun new data structures and
algorithms, and a lot of cloud computing.  Most recently we have been
working on open computational "protocols", worfklows, and pipelines
for democritizing certain kinds of sequence analysis. As part of this
work we are tackling issues of standardized test data sets to support
comparative benchmarking, targeted optimization, reproducible science,
and computational standardization in biology.  In this talk I'll
discuss our efforts to understand where our computational bottlenecks
are, what kinds of optimization and parallelization efforts make sense
financially, and how the cloud is enabling us to be usefully
disruptive.  As a bonus I'll talk about how the focus on pleasantly
paralellizable tasks has warped everyone's brains and convinced them
that engineering, not research, is really interesting.

Outline:

1. Defining the terms: cloud computing; data intensive; compute intensive.

2. Our data-intensive problem: sequence assembly and the big graph
problem. The scale of the problem.  A complete analysis protocol.

3. Predicted bottlenecks, including computation and I/O.

4. Actual bottlenecks, including NUMA architecture and I/O.

5. A cost-benefit analysis of various approaches, including buying
more memory; striping data across multiple volumes; increasing I/O
performance; focusing on software development; "pipelining" across
multiple machines; theory vs practice in terms of implementation.

6. A discussion of solutions that won't work, including
parallelization and GPU.

7. Making analysis "free" and using low-cost compute to analyze other
people's data.  Trying to be disruptive.
