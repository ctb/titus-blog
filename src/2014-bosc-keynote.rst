Talk notes for the Bioinformatics Open Source Conference (2014)
###############################################################

:author: C\. Titus Brown
:tags: future,bioinformatics
:date: 2014-07-11
:slug: 2014-bosc-keynote
:category: science

These are the talk notes for my opening talk at the `2014
Bioinformatics Open Source Conference
<http://www.open-bio.org/wiki/BOSC_2014_Schedule>`__.

Normally my talk notes aren't quite so extensive, but for some reason
I thought it would be a good idea to give an "interesting" talk, so my
talk title was "A History of Bioinformatics (in 2039)".  My thought
was that this could be fun way to pretend to "look back" on
bioinformatics and make some predictions about what would go wrong
(and right).  In hindsight, this was stupidly ambitious and likely to
fail miserably, but I gave it my best shot and put together a bunch of
notes over a period of several months.  And... here you are!

You can also see `my presentation
<http://www.slideshare.net/c.titus.brown/2014-bosckeynote>`__.

----

Datapocalypse --

Lots of data

Field optimized for data gathering and hyp driven investigation, not
 data exploration.

Computational infrastructure built to service HPC, not HTC.

Queries across data sets needed.

----

Reproducibility crisis --

Computationally speaking, surprisingly easy to resolve, but willpower
and incentives not there.

This started to change in late teens, as more and more papers proved
to be irreproducible; broader than computing, of course, but computing
led the way.

Ultimately required a shift in how recognition was awarded: we no longer
recognize the first to report something until after that report has been
reproduced.

Reviewers frown on building off of unverified work.

Grants often start by promising to validate previous work.

----

Computing in biology --

simply put, there weren't enough people being trained in the teens.
Graduate students would arrive at their research labs and be unable to
work with existing data or new data they generated.
Easy to use tools were created, but it turned out that these tools
embodied so many assumptions that they ultimately had to be abandoned,
except in well-understood clinical scenarios.  As you know, now we
spend a lot more time training beginning researchers in basic programming,
data analysis, modeling, and building computational protocols.

However, there was a sad period in the late 'teens and early 20s where
what we called bioinformatics sweatshops predominated.  These
sweatshops consisted of low-paid students who ended up with no career
path and no significant authorship.  In practice anyone with ambition
left with a terminal degree and moved to California where they could
have a career, leaving only people who could run programs they didn't
understand.

(expand) Huge amounts of bio; Somewhat fewer tools; Competence needed
to apply tools appropriately; Training gap; completely
underappreciated set of expertise.

This led to a several year a "correctness crisis" - at the same time
as biology was becoming more and more computational, fewer and fewer
reviewers were left to review more and more papers written by poorly
trained computational scientists

In recognition of the cultural and career problems, a union of
bioinformaticians formed with a few basic principles.

1) All of the data and source code has to be provided for any computational
part of a biology paper.

2) Methods and full methods sections need to included in review.

3) If an unpublished method was used in analysis of new data, a
separate and thorough description and analysis must be
made available at the time of peer review.

Any papers that did not meet these rules were simply rejected without review.
It took several years for these rules to spread, and it will not surprise
you that the MS Elsevier, back then known as Elsevier, was the last to
buckle.  However, we, the bioinformatics union, stood our ground and pointed
out that as long as we were doing the reviewing we could set review
guidelines in our area of expertise, as the statisticians had done.

It's worth pointing out that in this regard an interesting healthy
attitude was created where public peer reviews of papers were examined
for poor peer review, and then badly peer reviewed papers were
nominated for online workshops where they were re-reviewed and
subjected to replication.  There were several journals at the time
that were devoted to publishing purely computational replications, and
I know that many of the more senior scientists in the crowd owe your
career in some part to those efforts.

This culture of replication has stood the field in good stead: in
addition to considerably raising the quality of peer review, a
community of practice has emerged around the concept of replication,
and new students are immediately educated in how to write replicable
papers.

Finally, this tipping point was exacerbated by the loss of about 80%
of the worlds data scientists in the 2021 Great California Disruption.
We may never know the details of what happened, given the zonal
interdiction and lingering contamination, but I note the irony that so
much effort was made to replicate data globally, while so many of the
worlds' data scientists remained physically clustered within the
former Bay Area.

All of this led to a renaissance in biology, briefly interrupted by
the economic crunch of the mid-2020s and the First International
Police Action.  I would like to highlight four underpinnings of this
renaissance: first, the biomedical enterprise rediscovering non-translational
research; second, the rise and ultimate triumph of open science; third,
the belated recognition that networked science was the future; and fourth,
and perhaps most important, a massive investment in *people* and training.

---

The rediscovery of basic biology --

sequencing enabled!

ecology, evolution, population genetics, and microbial interactions

vetmed and ag

significant investment in a variety of new model organisms, especially vet

----

Triumph of open science -- by 2018, bioinformatics and genomics had
already figured this out, but not experimental biology.  This led to
what I think of as the Curious story of exp biology.  It took about 10
years, but, the biotech realization that most pure research could not
be replicated and most research money was simply burned on experiments
that never made it out of the lab, combined with a funding crunch and
a wave of retirements, meant that many of the more hyp driven labs
simply couldn't compete.  Experimentalists had to reinvent themselves
in two ways: first, guide their experiments with significant up front
data analysis (see: human resources problem); and second, make all
their data maximally available.  By a mere decade ago, in 2030, this
had renovated the field of experimental biology by introducing a wide
range of data-driven modeling and model-driven data analysis approaches,
which continue to further drive experimental research.  In a sense, our
hypotheses simply became better, more aware of what was out there.

These transitions were enabled by the collapse of the majority of
universities, and the accompanying retirement of the vast majority of
full professors.  While this also led to a massive and unfortunate
brain drain, it enabled the third element of the renaissance: a
transition to *networked* science.  No longer was science held back by
technologically challenged full professors; instead, a huge variety of
collaboration and data sharing tools, as well as approaches to
distributed team science, emerged.

My favorite was the walled-garden research collaboration, which is now
obsolete but at the time was quite radical. This emerged from
pioneering work done by Sage Bionetworks in the early 2010s, where a
group of scientists agreed to make data available within the group and
published on it simultaneously.  This coopetitive model, taken
originally from the ocean cruise community and applied to biomedical
work, was further enriched in a move inspired by the early Ft
Lauderdale data sharing agreements: anyone could have access to the
data as long as they agreed to publish after the rest of the group.
Nowadays, of course, all data is simply published as soon as it's generated,
but at the time this was quite radical and helped drive data sharing.

This is not to say that there have not been major disappointments.

As many of you know, we still have no idea what more than 50% of the gene
families discovered in microbes actually do, although biogeochemistry
and synthetic biology have characterized the majority of habitat-specific
genes.

Career paths still uncertain.

And we now have a problem with glam data sets, that mirrors what some of
you may remember as problems with glam mags.

Cancer is at least cured, but:
Some of the more complex diseases, esp neurodegenerative, are uncured;
there seems to be a complex mixture of genetic redundancy and phenotypic
plasticity underlying anything to do with the brain.

Essentially, complex phenotypes are still hard to decipher because
of their Rube Goldberg-esque nature & our inability to constrain
them with our data gathering skills.  This is where more experiments
and better model systems will surely help.

----

Let me now turn to the one of the reasons the organizers invited me. As
you no doubt saw, President Rao has announced a new initiative called
BRAIN2050.  This initiative comes just about 25 years after the first
BRAIN initiative, by president Obama, and it is an ambitious series
of funding proposals to understand the brain by 2050.  The general focus
is on neurodegen diseases, brain regeneration, and understanding the
development of human intelligence.  I have been invited to sit on the
advisory board, and I have some advice to offer this nascent field.

This first one will have you all groaning, but as you know from some
of the high profile journal rejections recently, correlation does not
imply causation!  The original BRAIN effort focused on recording
activation patterns in as many neurons as possible, but it turns out
that the causal linkages between neurons were simply too complicated
to decipher via observation.  Fine-tuned transcranial magnetic
stimulation promised perturbation mechanisms, but as some of you may
remember that research had to be discontinued for ethical reasons.
So we're still left with deciphering really large data sets.  Here,
it seems that modeling may finally offer a solution in terms of ever
more refined hypothesis generation, but of course this requires significant
effort at an experimental level as well as a computational level and it's
simply a very hard problem.

This brings me to modeling.  Top-down and bottom-up modeling have both
proven to be very successful in some circumstances in the brain research
community, and I think my main advice would be to continue straight on!
If there's one regret that I have in the more organismal/biomedical
community it's that modeling has not been pursued thoroughly over the last
quarter century.

I also have some advice concerning reproducibility.  While it is
obvious that results that cannot be independently replicated are not
science, we have to allow some leeway in fast moving fields.  I feel
like we have become to rigid in our review, and it's reduced our
ability to follow up on experimentally time consuming research; the
requirement that every experiment and computation be replicated
completely independently simply takes too long.  In light of all the
horrible reproducibility problems of the late 'teens, this is
understandable, but I would like to suggest that we adapt the
now-venerable concept of technical debt: as long as labs can
collaborate to replicate research done in one lab in another, we
should allow this for exploratory research.  However, this should be
clearly marked as a situation where completely independent replication
has not yet been done.  The concept of technical debt here is simply
that we can accrue "replication debt"; this debt must be paid off at
some point by articulating the protocols and techniques in finer
detail, but for the basic publication we can perhaps allow less rigid
replication requirements.

As a field that is about to receive a major infrastructure investment,
I would strongly suggest investing up front in a range of experimental
collaboration approaches.  While existing tools do a great job of
supporting sharing of data and code, this is still dependent on
personal relationships to drive collaboration.  There has been little
push to discover processes that actually drive collaboration.

25 years ago, Phil Bourne had the idea of automatically connecting
researchers based on automated data analysis "connecting the dots"
between researcher projects, to find those unexpected linkages that
might prove to drive more collaborations.  I think that's a really good
idea, and one that has been surprisingly ignored.  We now have the
informatics, the infrastructure, and the people - why not make use of them?


Another suggestion is to explicitly "tool up" early on.  As data gathering
begins, recruit theoreticians to start building models, and recruit
experimentalists to begin developing model systems.  Keep building and
renewing a core set of common data sets, all around the same well-studied
science problem; this will provide a common core for evaluation and
comparison of tools.  Contests have proven to be stifling of innovation,
because of the tendency to do incremental improvement; but if you can
build a culture of tool evaluation and comparison early on by funding it
and discussing it regularly, you can reap the rewards later on.

In molecular biology, we've also built an excellent pyramid diagram
of software, with a set of commercial data analysis interfaces based
around well-understood algorithms and test data sets.

The neuroscience field should also follow the same strategy as the
more basic biomedical sciences, and invest heavily at the high school
and pre-master's level.  Just to remind everyone, there are two reasons
for this -- one is that yesterday's high school students are tomorrow's
researchers.  The other is that investment in science teaching turns out
to drive public support for science; 15 years ago, we invested heavily
in teaching mechanisms of evolution at the high school level, and we
now have an unprecedented 80% acceptance rate of evolution among the 30-
and-under set.  It will take some time for this to spread through the
population, but we can already see an increase in popular support for
biological sciences, generally.

Ultimately we need a rich interaction between theory, experiment, and
data analysis.  In the heyday of genomic sequencing, we suffered from
too many physicists, who wanted to build reductionist models in the
absence of data.  Along with genomics, neuroscience has evicted many
of these physicists over the last quarter century in favor of
home-grown modelers who are deeply embedded in neuroscience.  But we
also need good interactions between experiments, theory, and data
analysis.  [ ...... ]

At the end of the day, it's clear that biology more generally and
neuroscience specifically share the feature of being "networks" - 
molecular interactions, tissue interactions, species interactions,
and neuronal interactions.  Just as the single-molecule/whole-chromosome
sequences from the late 20s didn't magically provide understanding,
neither will high resolution neuronal sampling.  Reductionist approaches
are necessary but cannot tell us all that we need to know.

----

--titus
