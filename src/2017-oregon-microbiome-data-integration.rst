How to analyze, integrate, and model large volumes of biological data - some thoughts
#####################################################################################

:author: C\. Titus Brown
:tags: ddd, data integration
:date: 2017-05-14
:slug: 2017-oregon-microbiome-data-integration
:category: science

This blog post stems from notes I made for a 12 minute talk at the
`Oregon State Microbiome Initiative
<http://microbiology.science.oregonstate.edu/osu-microbiome-initiative-ombi>`__,
which followed from some previous thinking about data integration on
my part -- in particular, `Physics ain't biology (and vice versa)
<http://ivory.idyll.org/blog/physics-aint-biology-and-vice-versa.html>`__
and `What to do with lots of (sequencing) data
<http://ivory.idyll.org/blog/2015-what-to-do-with-sequencing-data.html>`__.

My talk slides from OSU are `here <https://osf.io/mhwa5/>`__ if you're
interested.

----

**Note: During the events below, I was just a graduate student.  So my
perspective is probably pretty limited.  But this is what I saw and
remember ;).**

My graduate work was in `Eric Davidson's lab
<https://www.its.caltech.edu/~mirsky/>`__, where we studied early
development in the sea urchin.  Eric had always been very interested
in gene expression, and over the preceding decade or two (1980s and
onwards) had invested heavily in genomic technologies.  This included
lots of cDNA macroarrays and BAC libraries, as well as (eventually)
the sea urchin genome project.

The sea urchin is a great system for studying early development!  You
can get literally billions of synchronously developing embryos by
fertilizing all the eggs simultaneously; the developing embryo is
crystal clear and large enough to be examined using a dissecting scope;
sea urchins are available world-wide; early development is mostly invariant
with respect to cell lineage (although that comes with a lot of caveats);
and sea urchin embryos have been studied since the 1800s, so there was a lot
of background literature on the embryology.

The challenge: data integration without guiding theory
------------------------------------------------------

What we were faced with in the '90s and '00s was a challenge provided
by the scads of new molecular data provided by genomics: that of data
integration.  We had discovered plenty of genes (all the usual
homologs of things known in mice and fruit flies and other animals),
we had cell-type specific markers, we could measure individual gene
expression fairly easily and accurately with qPCR, we had
perturbations working with morpholino oligos, and we had reporter
assays working quite well with CAT and GFP.  And now, between BAC
sequencing and cDNA libraries and (eventually) genome sequencing, we
had tons of genomic and transcriptomic data available.

How could we make sense of all of this data?  It's hard to convey the
confusion and squishiness of a lot of this data to anyone who hasn't
done hands-on biology research; I would just say that single
experiments or even collections of many experiments rarely provided a
definitive answer, and usually just led to new questions.  This is not
rare in science, of course, but it typically took 2-3 years to figure
out what a specific transcription factor might be doing in early
development, much less nail down its specific upstream and downstream
connections.  Scale that to the dozens or 100s of genes involved in
early development and, well, it was a lot of people, a lot of
confusion, and a lot of discussion.

The GRN wiring diagram
----------------------

To make a longer story somewhat shorter:

Eric ended up leading an effort (together with Hamid Bolouri, Dave
McClay, Andy Cameron, and others in the sea urchin community) to build
a gene regulatory network that provided a foundation for data
integration and exploration.  You can see the result here:

http://sugp.caltech.edu/endomes/

This network at its core is essentially a map of the *genomic*
connections between genes (transcriptional regulation of transcription
factors, together with downstream connections mediated by specific
binding sites and signaling interactions between cells, as well as
whatever other information we had).  Eric named this "the view from
the genome."  On top of this is layered several different "views from
the nucleus", which charted the different regulatory states initiated
by asymmetries such as the localization of beta cadherin to the
vegetal pole of the egg, and the location of sperm entry into the egg.

At least when it started, the network served primarily as a map of the
interactions - a somewhat opinionated interpretation of both published
and unpublished data.  There was little to no immediate use of the
network in Boolean or quantitative modeling, although I know Eric had
a long term interest in that; in my view, it mainly served as a
communications medium and a point of reference for discussions about
future experiments as well as an integrative guide to published work.

What was sort of stunning in hindsight is the extent to which this
model became a touchpoint for our lab and (fairly quickly) the
community that studied sea urchin early development.  Eric presented
the network one year at the annual Developmental Biology of the Sea
Urchin meeting, and by the next meeting, 18 months later, I remember
it showing up in a good portion of talks from other labs.  (One of my
favorite memories is someone from Dave McClay's lab - I think it was
Cyndi Bradham - putting up a view of the GRN inverted to make
signaling interactions the core focus, instead of transcriptional
regulation; heresy in Eric's lab!)

In essence, the GRN became a community resource fairly quickly.  It
was provided in both image and interactive form (using BioTapestry),
and people felt free to edit and modify the network for their own
presentations.  It readily enabled in silico thought experiments -
"what happens if I knock out this gene? The model predicts this, and
this, and this should be downstream, and this other gene should be
unaffected" that quickly led to choosing impactful *actual*
experiments.  In part because of this, arguments about the effects of
specific genes quickly converged to conversation about how to *test*
the arguments (for some definition of "quickly" and "conversation" -
sometimes discussions were quite, ahem, robust in Eric's lab and the
larger community!)

The GRN also served to highlight the unknowns and the insufficiencies
in the model. Eric and others spent a lot of time thinking through
questions such as this: "we know that transcription of gene X is
repressed by gene Y; but something must still activate gene X. What
could it be?"  Eventually we did "crazy" things like measure the
transcriptional levels and spatial expression patterns of all ~1000
transcription factors found in the sea urchin genome, which could then
be directly integrated into the model for further testing.

In short, the GRN was a pretty amazing way for the community of people
interested in early development in the sea urchin to communicate about
the details.  Universal agreement wasn't the major outcome, although
I think significant points about early development were settled in part
through the model - *communication* was the outcome.

And, importantly, it served as a central meeting point for *data analysis*.
More on this below.

Missed opportunities?
---------------------

One of the major missed opportunities (in my view, obviously - feel
free to disagree, the comment section is below :) was that we never
turned the GRN into a model that was super easy for experimentalists
to play with.  It would have been fairly straightforward (if a
significant software development effort) to make it possible to do
click-able gene knockdown followed by predicted phenotype readout.  I
suspect (based on dim memory and one-on-one conversations) that this
was because Eric understood the model very well and could do those
things in his head, and didn't understand the power of immediate
interactivity and casual computational exploration for others.  Had I stayed in
the developmental biology game, I like to think I would have invested
significant effort in this kind of approach.

I also don't feel like much time was invested in the community
annotation and updating aspect of things. The official model was
tightly controlled by a few people (in the traditional scientific
"experts know best!" approach) and there was no particular attempt to
involve the larger community in annotating or updating the model
except through 1-1 conversations or formal publications.  It's
definitely possible that I just missed it, because I was just a
graduate student, and by mid-2004 I had also mentally checked out of
grad school (it took me a few more years to physically check out ;).

Taking and holding ground
-------------------------

One question that occupies my mind a lot is the question of how we learn,
as a community, from the research and data being produced in each lab.
With data, one answer is to work to make the data public, annotate it,
curate it, make it discoverable - all things that I'm interested in.

With research more broadly, though, it's more challenging.  Papers are
relatively poor methods for communicating the results of research,
especially now that we have the Internet and interactive Web sites.
Surely there are better venues (perhaps ones like `Distill
<http://blog.ycombinator.com/distill-an-interactive-visual-journal-for-machine-learning-research/>`__,
the interactive visual journal for machine learning research).
Regardless, the vast profusion of papers on any possible topic,
combined with the array of interdisciplinary methods needed, means
that knowledge integration is slow and knowledge diffusion isn't much
faster.

I fear this means that when it comes to specific systems and question,
we are potentially forgetting many things that we "know" as people
retire or move on to other systems or questions.  This is maybe to be
expected, but when we confront the level of complexity inherent in
biology, with little obvious convergence between systems, it seems
problematic to repose our knowledge in dead tree formats.

Mechanistic maps and models for knowledge storage and data integration
----------------------------------------------------------------------

So perhaps the solution is maps and models, as I describe above?

In thinking about microbiomes and microbial communities, I'm not sure
what form a model would take.  At the most concrete and boring level,
a directly useful model would be something that took in a bunch of
genomic/transcriptomic/proteomic data and evaluated it against everything
that we knew, and then sorted it into "expected" and "unexpected".
(This is what I discussed a little bit in my talk at OSU.)  

The "expected" would be things like the observation of carbon fixation
pathways in well-understood autotrophs - "yep, there it is, sort of
matches what we already see."  The "unexpected" would be things like
unannotated or poorly understood genes that were behaving in ways that
suggested they were correlated with whatever conditions we were
examining.  Perhaps we could have multiple bins of unexpected, so that
we could separate out things like genes where the genome, transcriptome,
and proteome all provided evidence of expression versus situations where
we simply saw a transcript with no other kind of data. I don't know.

If I were to indulge in fanciful thinking, I could imagine a sort of
Maxwell's Daemon of data integration, sorting data into bins of
"boring" and "interesting", churning through data sets looking for
a collection of "interesting" that correlated with other data sets
produced from the same system.  It's likely that such a daemon would
have to involve some form of deep correlational analysis and structure
identification - deep learning comes to mind.  I really don't know.

One interesting question is, how would this interact with experimental
biology and experimental biologists?  The most immediately useful
models might be the ones that worked off of individual genomes, such
as flux-balance models; they could be applied to data from new
experimental conditions and knockouts, or shifted to apply to strain
variants and related species and look for missing genes in known
pathways, or new genes that looked potentially interesting.

So I don't know a lot.  All I do know is that our current approaches
for knowledge integration don't scale to the volume of data we're
gathering or (perhaps more importantly) to the scale of the biology
we're investigating, and I'm pretty sure computational modeling of some
sort has to be brought into the fray in practical ways.

Perhaps one way of thinking about this is to ask what types of
computational models would serve as good reference resources, akin to
a reference genome. The microbiome world is surprisingly bereft of good
reference resources, with the 16s databases and IMG/M serving as two
of the big ones; but we clearly need more, along the vein of a community
KEGG and other such resources, curated and regularly updated.

Some concluding thoughts
------------------------

Communication of understanding is key to progress in science; we
should work on better ways of doing that.  `Open science
<http://ivory.idyll.org/blog/2016-what-is-open-science.html>`__ (open
data, open source, open access) is one way of better communicating
data, computational methods, and results.

One theme that stood out for me from the microbiome workshop at OSU
was that of *energetics*, a point that Stephen Giovanonni made most
clearly. To paraphrase, "Microbiome science is limited by the
difficulty of assessing the pros and cons of metabolic strategies."
The guiding force behind evolution and ecology in the microbial world
is energetics, and if we can get a mechanistic handle on energy
extraction (autotrophy *and* heterotrophy) in single genomes and then
graduate that to metagenome and community analysis, maybe that will
provide a solid stepping stone for progress.

I'm a bit skeptical that the patterns that ecology and evolution can
predict will be of immediate use for developing a predictive model.
On the other hand, Jesse Zaneweld at the meeting presented on the
notion that all happy microbiomes look the same, while all
dysfunctional microbiomes are dysfunctional in their own special way;
and Jesse pointed towards molecular signatures of dysfunction; so
perhaps I'm wrong :).

It may well be that our data is still far too sparse to enable us to build
a detailed mechanistic understanding of even simple microbial ecosystems.
I wouldn't be surprised by this.

Trent Northern from the JGI concluded in his talk that we need model
*ecosystems* too; absolutely! Perhaps experimental model ecosystems,
either natural or fabricated, can serve to identify the *computational*
approaches that will be most useful.

Along this vein, are there a natural set of big questions and core
systems for which we could think about models?  In the developmental
biology world, we have a few big model systems that we focused on
(mouse, zebrafish, fruit fly, and worm) - what are the equivalent
microbial ecosystems?

All things to think about.

--titus

p.s. There are a ton of references and they can be fairly easily found,
but a decent starting point might be `Davidson et al., 2002, "A genomic regulatory network for development." <https://scholar.google.com/citations?view_op=view_citation&hl=en&user=O4rYanMAAAAJ&citation_for_view=O4rYanMAAAAJ:u5HHmVD_uO8C>`__
