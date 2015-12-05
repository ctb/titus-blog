My review of a review of "Influential Works in Data Driven Discovery"
#####################################################################

:author: C\. Titus Brown
:tags: ddd,moore
:date: 2015-05-09
:slug: 2015-ddd-and-open-science
:category: science

I finally got a chance to more thoroughly read Mark Stalzer and Chris
Mentzel's arxiv preprint, `"A Preliminary Review of Influential Works
in Data-Driven Discovery" <http://arxiv.org/abs/1503.08776>`__.  This
is a short review paper that discusses concepts highlighted by the
1,000+ "influential works" lists submitted to the Moore Foundation's
Data Driven Discovery (DDD) Investigator Competition.  (Note, I was
`one of the awardees
<http://www.moore.org/programs/science/data-driven-discovery/investigators>`__.)

The core of this arxiv preprint is the section on "Clusters of
Influential Works", in which Stalzer & Mentzel go in detail through
the eight different concept clusters that emerged from their analysis
of the submissions.  **This is a fascinating section that should be
at the top of everyone's reading list.** The topics covered are, in
the order presented in the paper, as follows:

* Foundational theory, including Bayes' Theorem, information theory, and
  Metropolis sampling;

* Astronomy, and specifically the `Sloan Digital Sky Survey
  <http://www.sdss.org/>`__;

* Genomics, focused around the Human Genome Project and methods for
  searching and analyzing sequencing data;

* Classical statistical methods, including the lasso, bootstrap methods,
  boosting, expectation-maximization, random forests, false discovery rate,
  and "isomap" (which I'd never heard of!);

* Machine learning, including Support Vector Machines, artificial Neural
  Networks (and presumably deep learning?), logistic belief networks,
  and hidden Markov models;

* The Google! Including PageRank, MapReduce, and "the overall anatomy"
  of how Google does things; specific implementations included Hadoop,
  BigTable, and Cloud DataFlow.

* General tools, programming languages, and computational methods,
  including Numerical Recipes, the R language, the IPython Notebook
  (Project Jupyter), the Visual Display of Quantitative Information,
  and SQL databases;

* Centrality of the Scientific Method (as opposed to specific tools or
  concepts).  Here the discussion focused around the `Fourth Paradigm
  <http://research.microsoft.com/en-us/collaboration/fourthparadigm/>`__
  book which lays out the expansion of the scientific method from
  empirical observation to theory to simulation to "big data science";
  here, I thought the point that computers were used for both *theory*
  and *observation* was well-made.  This section is particularly worth
  reading, in my opinion.

This collection of concepts is simply delightful - Stalzer and Mentzel
provide both a summary of the concepts and a fantastic curated set of
high-level references.

Since I don't know many of these areas that well (I've heard of most
of the subtopics, but I'm certainly not expert in ... any of them?
yikes) I evaluated the depth of their discussion by looking at the
areas I was most familiar with - genomics and tools/languages/methods.
My sense from this was that they covered the highlights of tools
better than the highlights of genomics, but this may well be because
genomics is a much larger and broader field at the moment.

Data-Driven Discovery vs Data Science
-------------------------------------

One interesting question that comes up frequently is what the
connection and overlap is between data-driven discovery, data science,
big data, data analysis, computational science, etc.  This paper
provides a lot of food for thought and helps me draw some
distinctions. For example, it's clear that computational science
includes or at least overlaps with all of the concepts above, but
computational science also includes things like modeling that I don't
think clearly fit with the "data-driven discovery" theme.  Similarly,
in my experience "data science" encompasses tools and methods, along
with intelligent application of them to specific problems, but
practically speaking does not often integrate with theory and
prediction.  Likewise, "big data", in the sense of methods and
approaches designed to scale to analysis and integration of large data
set, is clearly one important aspect of data-driven discovery - but
only in the sense that in many cases *more* data seems to be *better*.

Ever since the "cage match" round of the Moore DDD competition, where
we discussed these issues in breakout groups, I've been working
towards the internal conclusion that data-driven discovery is the
*exploration and acceleration of science through development of new
data science theory, methods, and tools*.  This paper certainly helps
nail that down by summarizing the components of "data driven
discovery" in the eyes of its practitioners.

Is this a framework for a class or graduate training theme?
-----------------------------------------------------------

I think a lot about research training, in several forms.  I do a lot
of short-course peer instruction form (e.g. Data Carpentry, Software
Carpentry, and my DIB efforts); I've been talking with people about
graduate courses and graduate curricula, with especial emphasis on
data science (e.g. the `Data Science Initiative
<http://datascience.ucdavis.edu>`__ at UC Davis); and, most generally,
I'm interested in "what should graduate students know if they want to
work in data-driven discovery"?

From the training perspective, this paper lays out the central
concepts that could be touched on either in a survey course or in
an entire graduate program; while my sense is that a PhD would
require coupling to a specific domain, I could certainly imagine a
Master's program or a dual degree program that touched on the
theory and practice of data driven discovery.

For one example, I would love to run a survey course on these topics,
perhaps in the area of biology.  Such a course could go through
each of the subsections above, and discuss them in relation to
biology - for example, how Bayes' Theorem is used in medicine,
or how concepts from the Sloan Digital Sky Survey could be applied
to genomics, or where Google-style infrastructure could be used
to support research.

There's more than enough meat in there to have a whole graduate
program, though.  One or two courses could integrate theory and tools,
another course could focus on practical application in a specific
domain, a third course could talk about general practice and computing
tools, and a fourth course could discuss infrastructure and scaling.

The missing bits - "open science" and "training"
------------------------------------------------

Something that I think was missing from the paper was an in-depth
perspective on the role that open source, open data, and open science
can play.  While these concepts were directly touched on in a few of
the subsections - most of the tools described were open source, for
example, and Michael Nielsen's excellent book `"Reinventing Discovery"
<http://www.amazon.com/Reinventing-Discovery-The-Networked-Science/dp/0691160198>`__
was mentioned briefly in the context of network effects in scientific
communication and access - I felt that "open science" was an
unacknowledged undercurrent throughout.

It's clear that progress in science has always relied on sharing
ideas, concepts, methods, theory, and data.  What I think is not yet
as clear to many is the extent to which practical, efficient, and
widely available *implementations* of methods have become important in
the computer age.  And, for data-driven discovery, an increasingly
critical aspect is the *infrastructure* to support data sharing,
collaboration, and the application of these methods to large data
sets.  These two themes -- *sharing of implementation* and *importance
of infrastructure* cut across many of the subsections in this paper,
including the specific domains of astronomy and human genomics, as
well as the Google infrastructure and languages/tools/implementation
subsections.  I think the paper could usefully add a section on this.

Interestingly, the Moore Foundation DDD competition implicitly
acknowledged this importance by *enriching* for open scientists in
their selection of the awardees -- a surprising fraction of the
Investigators are active in open science, including myself and Ethan
White, and virtually all the Investigators are openly distributing
their research methodology.  In that sense, open science is a notable
*omission* from the paper.

It's also interesting to note that *training* is missing from the
paper.  If you believe data-driven discovery is part of the future of
science, then training is important because there's a general lack of
researchers and institutions that cover these topics.  I'd guess that
virtually no one researcher is well versed in a majority of the
topics, especially since many of the topics are entire scientific
super-fields, and the rest are vast technical domains.  In academic
research we're kind of used to the idea that we have to work in
collaboration (*practice* may be different...), but here academia
really fails to cover the entire data-driven discovery spectrum
because of the general lack of emphasis on expert use of tools and
infrastructure in universities.

So I think that investment in training is where the opportunities lie
for universities that want to lead in data-driven discovery, and this
is the main chance for funders that want to enable the network effect.

Training in open science, tools, and infrastructure as competitive advantages
-----------------------------------------------------------------------------

Forward-thinking universities who are in it for the long game &
interested in building a reputation in data-driven discovery, might
consider the following ideas:

* scientists trained in open science, tool use, and how to use
  existing infrastructure, are more likely to be able to quickly take
  advantages of new data and methods.

* scientists trained in open science are more likely to produce
  results that can be built on.

* scientists trained in open science are more likely to produce useful
  data sets.

* scientists trained in open science and tool building are more likely
  to produce useful tools.

* funding agencies are increasingly interested in maximizing impact by
  requiring open source, open data, and open access.

All of these should lead to more publications, more important
publications, a better reputation, and more funding.

In sum, I think investments in training in the most ignored bits of
data-driven discovery (open science, computational tool use and
development, and scalable infrastructure use and development) should
be a competitive advantage for institutions.  And, like most
competitive advantages, those who ignore it will be at a significant
*disadvantage*.  This is also an opportunity for foundations to drive
progress by targeted investments, although (since they are much more
nimble than universities) they are already doing this to some extent.

In the end, what I like most about this paper is that it outlines and
summarizes the concepts in which we need to invest in order to advance
science through data-driven discovery.  I think it's an important
contribution and I look forward to its further development and
ultimate publication!

--titus
