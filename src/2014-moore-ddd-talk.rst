The Moore DDD Investigator competition: my presentation
#######################################################

:author: C\. Titus Brown
:tags: research,moore
:date: 2014-07-29
:slug: 2014-moore-ddd-talk
:category: science

Here are my talk notes for the `Data Driven Discovery
<http://www.moore.org/programs/science/data-driven-discovery/ddd-investigators>`__
grant competition ("cage match" round).  Talk slides `are on
slideshare <http://www.slideshare.net/c.titus.brown/2014-mooreddd>`__

----

Hello, my name is Titus Brown, and I'm at Michigan State University
where I run a biology group whose motto is "better science through
superior software".  I'm going to tell you about my vision for building
infrastructure to support data-intensive biology.

Our research is focused on accelerating sequence-based biology with
algorithmic prefilters that help scale downstream sequence analysis.
The basic idea is to take the large amounts of data coming from
sequencers and squeeze out the information in the data for downstream
software to use.  In most cases we make things 10 or 100x easier, in
some cases we've been able to make analyses possible where they
weren't doable before;

In pursuit of this goal, we've built three super awesome computer
science advances: we built a low-memory approach for counting sequence
elements, we created a new data structure for low-memory graph storage,
and developed a streaming lossy compression algorithm that puts much
of sequence analysis on a online and streaming basis.  Collectively,
these are applicable to a wide range of basic sequence analysis problems,
including error removal, species sorting, and genome assembly.

We've implemented all three of these approaches in an open source
analysis package, khmer, that we developed and maintain using good
software engineering approaches.  We have primarily focused on using
this to drive our own research, but since you can do analyses with it
can't be done any other way, we've had some pretty good adoption by
others.  It's a bit hard to tell how many people are using it because
of the many ways people can download it, but we believe it to be in the
1000s and we know we have dozens of citations.

The most important part of our research is this: we have enabled some
excellent biology!  For a few examples, we've assembled the largest
soil metagenome ever with Jim Tiedje and Janet Jansson, we've helped
look at deep sea samples of bone eating worms with Shana Goffredi,
we're about to publish the largest de novo mRNASeq analysis ever done,
and we're enabling evo devo research at the phylogenetic extremes of the
Molgula sea squirts.  This was really what we set out to do at the beginning
but the volume and velocity of data coming from sequencers turned out to be
the blocking problem.

Coming from a bit of a physics background, when I started working in
bioinformatics 6 years ago, I was surprised at our inability to
replicate others' results.  One of our explicit strategies now is to
try to level up the field by doing high quality, novel, open science.
For example, our lamprey analysis is now entirely automated, taking
three weeks to go from 3 billion lamprey mRNASeq reads to an
assembled, annotated transcriptome that we can interactively analyze
in an IPython Notebook, which we will publish with the paper.
Camille, who is working on this, is a combination software engineer
and scientist, and this has turned out to be a really productive
combination.

We've also found that 1000s of people want to do the kinds of things
we're doing, but most don't have the expertise or access to
computational infrastructure.  So, we're also working on open
protocols for analyzing sequence data in the cloud - going from raw
mRNASeq data to finished analysis for about $100.  These protocols are
open, versioned, forkable, and highly replicable, and we've got about
20 different groups using them right now.

So that's what I work on now.  But looking forward I see a really big
problem looming over molecular biology.  Soon we will have whatever
'omic data set we want from, to whatever resolution we want, limited
only by sampling.  But we basically don't have any good way of analyzing
these data sets -- most groups don't have the capacity or capability to
analyze them themselves, we can't store these data sets in one place
and -- perhaps the biggest part of the catastrophe -- people aren't
making these data available until after publication, which means that
I expect many of them to vanish.  We need to incentivise
pre-publication sharing by making it *useful* to share your data.  We can
do individual analyses now, but we're missing the part that links these
analyses to other data sets more broadly.

My proposal, therefore, is to build a distributed graph database system that
will allow people to interconnect with open, walled-garden, and private
data sets.  The idea is that researchers will spin up their own server in the
cloud, upload their raw or analyzed data, and have a query interface that
lets them explore the data.  They'll also have access to other public servers,
and be able to opt-in to exploring pre-published data; this opt-in will be
in the form of a walled-garden approach where researchers who use results
from analyzing other unpublished data sets will be given citation information
to those data sets.  I hope and expect that this will start to incentivise
people to open their data sets up a bit, but to be honest if all it does
is make it so that people can analyze their own data in isolation it will
already be a major win.

None of this is really a new idea. We published a paper exploring some of
these ideas in 2009, but have been unable to find funding.  In fact, I
think this is the most traditionally unfundable project I have ever proposed,
so I hope Moore feels properly honored.  In any case, the main point here
is that graph queries are a wonderful abstraction that lets you set up
an architecture for flexibly querying annotations and data when certain
precomputed results already exist.  The pygr project showed me the power
of this when implemented in a distributed way and it's still the best
approach I've ever seen implemented in bioinformatics.

The idea would be to enable basic queries like this across multiple
servers, so that we can begin to support the queries necessary for automated
data mining and cross-validation.

My larger vision is very buzzwordy.  I want to enable frictionless
sharing, driven by immediate utility.  I want to enable permissionless
innovation, so that data mining folk can try out new approaches
without first finding a collaborator with an interesting data set, or
doing a lot of prep work.  By building open, federated infrastructure,
and avoiding centralized infrastructure, I am planning for poverty:
everything we build will be sustainable and maintainable, so when my
funding goes away others can pick it up.  And my focus will be on
solving people's current problems, which in biology are immense,
while remaining agile in terms of what problems I tackle next.

The thing is, *everybody needs this*.  I work across many funding agencies,
and many fields, and there is *nothing* like this currently in existence.
I'm even more sure of this because I posted my Moore proposal and requested
feedback and discussed it with a number of people on Twitter.  NGS has
enabled research on non-model organisms but its promise is undermet due
to lack of cyberinfrastructure, basically.

How would I start?  I would hire two domain postdocs who are tackling
challenging data analysis tasks, and support them with my existing
lab; this would involve cross-training the postdocs in data intensive
methodologies.  For example, one pilot project is to work on the data
from the DeepDOM cruise, where they did multi-omic sampling across
about 20 points in the atlantic, and are trying to connect the dots
between microbial activity and dissolved organic matter, with
metagenomic and metabolomic data.

Integrated with my research, I would continue and expand my current
efforts in training.  I already run a number of workshops and generate
quite a bit of popular bioinformatics training material; I would
continue and expand that effort as part of my research.  One thing
that I particularly like about this approach is that it's deeply
self-interested: I can find out what problems everyone has, and will
be having soon, by working with them in workshops.
