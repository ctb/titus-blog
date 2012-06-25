Metagenomics: we have all the answers (they're just all different)
##################################################################

:author: C\. Titus Brown
:tags: metagenomics,assembly,ngs
:date: 2011-10-14
:slug: jgi-workshop
:category: science



I'm just on my way back from a JGI workshop on metagenome informatics,
and I thought I'd take the opportunity to write up a short review.

The workshop was, frankly, excellent.  We saw a bunch of talks on
metagenome assembly (my current interest) as well as single-cell
sequencing approaches, and a whole spate of data analysis platform
talks.  The basic perspective seems to be this: nobody has the
solution to everything, and those who do have some answers seem to get
different answers from others.  The one possible exception to this was
Jill Banfield, who gave a really inspiring talk about how they're
using metagenomics on low- and medium-complexity communities to do
some excellent science.

(Advertisement: my talk on scaling metagenome assembly is online
`here, at slideshare <http://www.slideshare.net/c.titus.brown/beacon-101-sequencing-tech>`__.)

The only somewhat dissatisfying note to the whole conference was the
overall lack of inter-project cooperation and cross-validation.  While
some of the analysis platform folk are talking to each other, I don't
think they have a good handle on how to really test each other's
software, much less combine forces; too much of it all boils down to
"trust us -- our approaches work", which is simply not the way to do
science.  Period.

Pain
----

"The thing that is driving all of us is pain." -- Victor Markowitz

This single statement probably sums up the workshop best!  One of the
most obvious tensions in the workshop was between *sensitivity of
results* and *scaling*.  For many microbial populations, it is
critical to sequence deeply in order to see rare variants and species;
and yet our assembly and annotation tools are, generally speaking,
unprepared to handle this volume of data (dozens of Gb, if not Tb).
This leads to *pain*, as we desperately attempt to make use of the
data to address our biology.

There were also quite clearly two camps of people.  One group had
experience with metagenomic data sets of simple- to
middling-complexity: think human microbiome, with up to a few hundred
species of microbes per sample.  The other group was confronting water
and most especially soil, which may have hundreds of thousands if not
millions of species per sample.  The first group was prone to saying
things like "it's not that tough a problem, folks! you just need to
analyze more sequence! and then you can do anything you want!" to
which the second group would then say "yeah, that's the problem,
innit? all that sequence?"

I think in a year or so it will be easier to characterize this gap in
complexity.  We're finally getting results from soil assembly, and
it's clear that we need terabases of sequence to get good results; but
we don't yet have the ability to quickly & confidently analyze those
terabases of sequence.  Once we do, we can make quantitative statements
illustrating the divide.

It was also nice to hear that everyone had settled on the best
possible data processing pipeline at the meeting!  (Although perhaps
coincidentally, it was almost always their own software.)

Standards
---------

The second day featured a lot of discussion of standards.  Many people
seemed to have a community standard that, if everyone would just start
using theirs, would solve all the problems!!!

.. image:: http://imgs.xkcd.com/comics/standards.png

Of particular interest to me, Owen White gave a talk where he
presented on the Open Source Data Framework. This is basically a
central-server NoSQL implementation for storing metadata and data
together.  Eventually it will support data migration for locality, and
lots of other nice features.  The response to building Yet Another Big
Database (But This Time, With No Schema!!) was muted, although I'm
personally quite bullish on the idea that maybe, just maybe, we can
have a place where the data and metadata are combined (!!!).  It seems
that the alternative to an OSDF-like database is to continue using
flat files -- maybe even with URLs sometimes!!  -- and I see that
approach continuing to engender chaos.  An alternative would be nice.

(I hate SQL for dataset storage, but maybe that's not a majority
opinion.)

One particularly good quote from Victor Markowitz on the OSDF
proposal, paraphrased: "This system will let us spread
misunderstandings further and more quickly!"  Hmm, is that a negative?

Also, someone said the HMP has 14 trillion reads, or 1.4 petabases of
sequence.  Whuh?  Apparently this is what IMG/HMP and METAREP are
being built to analyze.  Yikes.

Big Black Data Analysis Boxes
-----------------------------

Big black boxes for data analysis is a running theme in metagenomics,
although I'm not entirely sure why -- something in the water?  (We
should sequence that.) Things like MG-RAST, IMG/M, CAMRA, and the
various K-base projects offer to take your data (raw or not); fold,
spindle, and mutilate it; and then return Results.

This approach gives me the heebiejeebies.  I have lots of questions:
What software are they running, how, with what parameters?  What kind
of internal QC do they have, and how can I run it myself on my own
data?  What version of what databases are used?  What filtering do
they do?  The response (more or less) always seems to be "TRUST us! We
know what we're doing!"

That line works better in a `sitcom <http://en.wikipedia.org/wiki/Sledge_Hammer!>`__ than it does in real life.

I really, really want to see a platform mentality evolve.  Cue Steve
Yegge's "platform" rant: http://news.ycombinator.com/item?id=3101876
or http://steverant.pen.io/

What's the goal, anyway?  Reads vs. assembly
--------------------------------------------

Several people were particularly grumpy about this whole "assembly"
thing.  I can only imagine this stems from having to go to too many
meetings where a lot of really theoretical assembler discussion goes
on, and is nonetheless treated like the central activity necessary for
metagenomics.  Since I work on assembly now, I enjoy those talks, but
I fully understand that I am a masochist when it comes to science, and
not everyone likes assembly.

Nonetheless I think people skeptical of assembly are largely wrong, at
least in the overall concept.  Assembly is a really important approach
in metagenomics for several reasons, which Kostas Mavrommmmmmmmatis
laid out the second day: scientifically speaking, assembly gives way
better statistical signals for both gene finding and analysis of
variation; you can also get linkage information from assembly, which
is important for operon analysis.  And, just as important -- from a
pragmatic perspective, the reduction in data size from assembly saves
both space and computation time, and assembly smooths out errors
in way that not much else does.

That's not to say assembly is easy, or a panacea, but I think it's an
incredibly valuable approach for all those reasons.

As for single read analysis, I am deeply skeptical of any conclusions
reached from analyzing reads of length 120 or less -- that's not much
signal, bub.  (Note, I'm also guilty of this; check out my publication
with Victoria Orphan in 2006.  What can I say?  I was younger and
naiver.)  Friends don't let friends analyze Illumina short reads.  And
yet, it seems to be a prevalent, perhaps even dominant, activity in
metagenomics.  Boo.

So: assemble, man.  It's needed.

But as for goals... well, Brooklin Gore said it well when he said,
"You come to understand that the purpose of a machine is ultimately
not to run programs, but to solve problems."  What problems do we want
to solve?

Good question.

There wasn't much unity in the goals of the attendees.  Some people
wanted whole genomes. Others wanted genes.  Yet others wanted
variations in those genes.  Presumably most people wanted metabolic
profiles of one sort or another, except for those who didn't.  I think
this reflects something that Guy Cochrane pointed out: sequencing is
fast becoming a common feature to much of biology, and it is extremely
hard to address everyone's needs in one platform.  So, that makes it
even more unlikely that one single approach or one single analysis
platform will answer even a majority of users's needs.  There's a lot
of room out there, folks.

On benchmarking
---------------

Everyone got up and gave a different set of assembly results, and it
became kind of obvious that everyone optimizes their assembler for a
specific set of statistics and then reports only those.  Hey -- what
about a standard set of benchmarks??

Well, there was a strange reluctance on the part of some Senior
Scientists to invest in assembly benchmarking.  As near as I could
make out, this was because of a fear that assembler authors would then
dive into optimizing for those benchmarks at the expense of Platonic
truth.  Fair 'nuff.  But I think there's gotta be a happy medium
between No Benchmarks and Only Benchmarks.  Right now I find it
extremely difficult to figure out which assemblers are better for what
purposes, and I'm pretty sure everyone else is just as confused
(modulo the authors of assemblers themselves, who are generally quite
positive that their assembler is the best).

Anyhoo, I'm thinking quite hard about setting up a couple of single
cell and metagenomic data sets, along with assembly and evaluation
pipelines, on Amazon Web Services.  That should at least make it easy
to run people's assemblers on the same data sets & compare the
results.

--

Hmm, conclusion time...

The metagenomic and single cell data is already coming, thanks to our
sequencing center overlords.

Generally speaking, we don't know how to handle it, either by assembly
or by single read analysis.  We certainly don't know how to scale all
the analyses that everybody wants to do.

The data will still be coming, regardless.

Good times!

--titus
