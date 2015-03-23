What to do with lots of (sequencing) data
#########################################

:author: C\. Titus Brown
:tags: dib,sequencing,ddd,open science
:date: 2015-03-23
:slug: 2015-what-to-do-with-sequencing-data
:category: science

On a recent west coast speaking junket where I spoke at OSU, OHSU, and
VanBUG (Brown PNW '15!), I put together a new talk that tried to
connect our past work on scaling metagenome assembly with our future
work on driving data sharing and data integration.  As you can maybe
guess `from the first few talk slides
<http://www.slideshare.net/c.titus.brown/2015-osumetagenome>`__, the
motivating chain was something like

1. We want to help biologists move more quickly to hypotheses;

2. This can in part be done by aiding in hypothesis generation and refinement;

3. Right now it's painful to analyze large sequencing data sets;

4. Let's make it less painful!

At both OHSU and OSU, where I gave very similar talks, I got important
and critical feedback on these points.  The three most valuable points
of feedback were,

* what exactly do you mean by data integration, anyway, Titus?

* you never talked about generating hypotheses!

* no, seriously, you never talked about how to actually generate hypotheses!?

The culmination point of this satori-like experience was when Stephen
Giovannoni leaned across the table at dinner and said, "Perhaps you
can tell me *what all this data is actually good for?*" This led to a
very robust and energetic dinner conversation which led to this blog
post :).  (Note, Stephen clearly had his own ideas, but wanted to hear
mine!)

The underlying point is this: I, and others, are proselytizing the
free and open availability of large data sets; we're pushing the
development of big data analytic tools; and we're arguing that this
is important to the future of science.  Why? What good is it all?  Why
should we worry about this, rather than ignoring it and focusing
instead on (for example) physiological characterization of complex
environments, clinical trials, etc. etc.?

So, without further ado,

What is all this data potentially good for?
-------------------------------------------

Suppose you set out to use a body of sequencing data in your
scientific research.  This sequencing data is maybe something you
generated yourself, or perhaps it's from a public data set, or from
multiple public data sets.  Either way, it's a bunch of data that you
would like to make use of.  What could you do with it?

(This isn't specific to sequencing data, although I think the exploratory
approaches are particularly important in biology and sequencing data are
well suited to exploratory analysis.)

1. Computational hypothesis falsification.

   "I thought A was happening. If A is happening, then when I looked at
   my data I should have seen B. I didn't see B. Therefore A is probably
   not happening."

   For example, if you are convinced that a specific biogeochemical
   process is at work, but can't find the relevant molecules in a
   metagenomic survey, then either you did something wrong, had
   insufficient sensitivity, or your hypothesis is incorrect in the
   first place.

   This is one place where pre-existing data can really accelerate the
   scientific process, and where data availability is really
   important.

2. Determination of model sufficiency.

   "I have a Boolean or quantitative model that I believe captures the
   essential components of my system under investigation.  When I fit
   my actual data to this model, I see several important mismatches.
   Therefore my model needs more work."

   For gene regulatory networks, or metabolic modeling, this kind of
   approach is where we need to go.  See, for example, `work from my
   graduate lab on sea urchin GRNs
   <http://sugp.caltech.edu/endomes/>`__ - this approach is used
   there implicitly to drive forward the investigation of underdetermined
   parts of the GRN.

3. Comparison with a null or neutral model.

   "If interesting interactions were happening, I would see patterns
   that deviated from my model of what an uninteresting system should
   look like. I don't, therefore my model of what is interesting or
   uninteresting needs to change."

   Somewhat of an elaboration of the above "model sufficiency", here
   we are choosing an explicit "null model" to interpret our data and
   concluding that our data is either interesting or boring.  For me,
   the difference is that these models need not be mechanistic, while
   the models in the previous point are often mechanistic.  One
   example I'd point to is Ethan White's `work on maximum entropy
   models <http://www.esajournals.org/doi/abs/10.1890/11-2177.1>`__.

4. Hypothesis generation (or, "fishing expedition.")

   "I have no idea what processes are at work here. Let's look at the
   data and come up with some ideas."

   A thoroughly underappreciated yet increasingly default approach in
   various areas of biology, fishing expeditions can feed the masses.
   (Get it? Hah!)

   But, seriously, this is an important part of biology; I wrote about
   why at some length `back in 2011
   <http://ivory.idyll.org/blog/is-discovery-science-really-bogus.html>`__.
   All of the previous points rely on us already knowing or
   believing something, while in reality most of biology is poorly
   understood and in many cases we have almost no idea what is going
   on mechanistically.

So, this is my first take on the reasons why I think large-scale data
generation, availability, analysis, and integration can and should be
first class citizens in biology.  But I'd be interested in pushback
and other thoughts, as well as references to places where this
approach has worked well (or poorly) in biology!

--titus

p.s. Thanks to Stephen Giovannoni, Thomas Sharpton, Ryan Mueller, and
     David Koslicki for the dinner conversation at OSU!
