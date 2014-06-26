What about all those genes of unknown function?
###############################################

:author: C\. Titus Brown
:tags: genes of unknown function
:date: 2014-06-26
:slug: 2014-function-of-unknown-genes
:category: science

I'm at the 2014 Marine Microbes Gordon Conference right now, and at
the end of `my talk
<http://www.slideshare.net/c.titus.brown/2014-marinemicrobesgrc>`__, I
brought up the point that the function of most genes is unknown.  It's
not a controversial point in any community that does environmental
sequencing, but I feel it should be mentioned at least once during
every session on metagenome sequencing :).

The lack of functional information for the vast majority of genes is,
in my view, the broadest and biggest challenge facing environmental
microbiology.  Known colloquially as `"microbial dark matter"
<http://microbialdarkmatter.org/>`__ `(ref
<http://www.nature.com/nature/journal/v499/n7459/full/nature12352.html>`__
and `Nature News
<http://www.nature.com/news/researchers-glimpse-microbial-dark-matter-1.1336>`__),
it is fair to say that we have virtually no window into what the
majority of genes *do*.  This is particularly a problem now that we
can readily access them with sequencing, and several fields are
racking up hundreds or thousands of data sets that are largely
uninterpretable from a functional perspective.

So what are our options?  What can we do to characterize new genes?
There seem to be two poles of opinions: many experimentalists argue
that we need to devote significant efforts to doing more microbial
physiology, which is, after all, how we know most of what we already
know.  People at the other pole seems to think that if we do enough
sequencing, eventually meaning will emerge - enough correlations will
turn into causation.  (While these are obviously caricatures, I think
they capture most of the range of opinions I've heard, so I like 'em ;).

Neither course seems likely to me.  Nobody is going to fund hundreds
or thousands of graduate student projects to characterize the
physiology of individual microbial species, which is more or less the
scale of effort needed.  Similarly, while the sequencing folk have
clearly been "winning" (in the sense that there's a lot of sequencing
being done!)  there's a growing backlash against large-scale
sequencing without a fairly pointed set of hypotheses behind them.
This backlash can be understand as a natural development -- the
so-called `trough of disillusionment
<http://en.wikipedia.org/wiki/Hype_cycle>`__ in the adoption and
understanding of new technologies -- but that makes it no less real.

Over the past few years, I've had the opportunity discuss and debate a
variety of approaches to characterizing gene function in microbes.
Since I'm thinking about it, I thought I'd take the time to write down
as many of the ideas as I can remember.  There are two purposes to
this -- first, I'm trawling for new ideas, and second, maybe I can
help inspire people to tackle these challenges!

Without further ado, here is my list, broken down into somewhat arbitrary
categories.

Experimental exploration and determination of gene function
===========================================================

1. Finding genetic systems and doing the hard work.

   This is essentially the notion that we should focus in on a few
   model systems that are genetically tractable (culturable,
   transformable, and possessed of genome editing techniques) and
   explore, explore, explore.  I'm not sure which microbes are
   tractable, or could be made tractable, but I gather we are lacking
   model systems representative of a broad swath of marine microbes,
   at least.

   The upsides to this approach are that we know how to do it, and all
   of the modern -omics tools can be brought to bear to accelerate
   progress: genome, transcriptome, and proteome sequencing, as well
   as metabolomics.

   The downsides are that this approach is slow, time consuming, and
   not particularly scalable.  Because of that I'm not sure there's
   much support for funding.

2. Transcriptome assisted culture.

   A persistent challenge for studying microbes is that many of them
   cannot be easily cultured, which is a soft prerequisite for
   studying them in the lab.  We can't culture them because often we
   don't know what the right culture conditions are -- what do they
   eat? Who do they like to hang out with?

   One of the neater approaches to resolving this is the concept of
   transcriptome assisted culture, which Irene Newton
   (`@chicaScientific <https://twitter.com/chicaScientific>`__)
   pointed out to me in `this neat PNAS paper on culturing *Coxiella*
   <http://www.pnas.org/content/106/11/4430.short>`__.  Essentially,
   Omsland et al. used transcriptome sequencing in conjunction with
   repeated modifications to the culture medium to figure out what the
   right growth medium was.  In addition to converting an important
   biomedical pathogen into something more easily culturable, the
   authors gained important insights into its basic metabolism
   and the interaction of Coxiella with its host cells.

   Upsides? It's an approach that's readily enabled by modern -omics
   tools, and it should be broadly applicable.

   Downsides? Slow, time consuming, and probably not that scalable.  However,
   it's a rather sexy approach to the hard slog of understanding organisms
   (and you can argue that it's basically the same as the model organism
   approach).

3. Enrichment cultures.

   Another culture-based approach is the enrichment culture, in which
   a complex microbial community (presumably capable of driving many
   different biogeochemical processes) is grown in a more controlled
   environment, usually one enriched for a particular kind of
   precursor.  This can be done with a `flow reactor approach
   <http://en.wikipedia.org/wiki/Flow_chemistry#Continuous_flow_reactors>`__
   where you feed in precursors and monitor the composition of the
   outflow, or just by adding specific components to a culture mix and
   seeing what grows.

   For one example of this approach, see `Oremland et al., 2005
   <http://sciencemag.org/content/308/5726/1305.full>`__, in which the
   authors isolated a microbe, Halarsenatibacter silvermanii, which
   metabolized arsenic.  They did this by serial transfer of the cells
   into a fresh medium and then purifying the organism that grew
   through serial dilution.

   This is a bit of a reverse to the previous methods, where the focus
   was on a specific organism and figuring out how it worked; here,
   you can pick a condition that you're interested in and figure out
   what grows in it.  You can get both simplified communities and
   potentially even isolates that function in specific conditions.
   Also see `Winogradsky columns
   <http://en.wikipedia.org/wiki/Winogradsky_column>`__.  You still
   need to figure out what the organisms do and how they do it, but
   you start with quite a bit more information and technology than you
   would otherwise - most importantly, the ability to maintain a
   culture!

   Pros: this is actually a lot more scalable than the model-organism
   or culture-focused techniques above.  You could imagine doing this on a
   large scale with a fairly automated setup for serial transfer, and
   the various -omics techniques could yield a lot of information for
   relatively little per-organism investment.  Someone would still need
   to chase down the genes and functions involved, but I feel like this
   could be a smaller part of a PhD at this point.

   Cons: it's not terribly hypothesis driven, which people don't always
   like; and you might find that you don't get that much biological
   novelty out of the cultures.

4. Functional metagenomics   

   You can also understand what genes do by putting them into
   tractable model organisms.  For example, one of the ways that Ed
   DeLong's group showed that proteorhodopsin probably actually
   engaged in photosynthesis was by `putting the gene in E. coli
   <http://www.sciencemag.org/content/289/5486/1869.long>`__.  At the
   time, there was no way to investigate the gene (from an uncultured
   SAR86) in its host organism, so this was the only way they could
   "poke" at it.

   A significant and important extension of this idea is to transfer
   random fragments from metagenomic fosmid or BAC libraries into
   large populations of (say) E. coli, and then do a selection
   experiment to enrich for those critters that can now grow in new
   conditions.  For example, see `this paper
   <http://pubs.acs.org.proxy1.cl.msu.edu/doi/full/10.1021/ja002990u>`__
   on identifying the gene behind the production of certain
   antibiotics (hat tip to Juan Ugalde (`@JuanUgaldeC
   <https://twitter.com/JuanUgaldeC>`__ for the reference).  Also see
   the "heterologous expression" paragraph in `Handelsman (2004)
   <http://mmbr.asm.org/content/68/4/669.full>`__, or this other
   `antibiotic resistance paper
   <http://www.ncbi.nlm.nih.gov/m/pubmed/15305923/>`__ from Riesenfeld
   et al. (2004).

   Pros: when it works, it's awesome!

   Cons: most genes work in pathways, and unless you transfer in the
   whole pathway, the gene might not do anything.  This has been
   addressed by transferring entire fosmids with whole operons on them
   between microbes, and I think this is still worth trying, but (to
   me) it seems like a low-probability path to success.  I could be
   wrong.

5. Synthetic biology

   Why not just `build a new genome using synthetic biology
   approaches? <http://en.wikipedia.org/wiki/Synthetic_biology>`__
   This is a radical extension of the previous idea of transferring
   genes between different organisms.  Since we can now `print long
   stretches of DNA on demand
   <http://www.nature.com/nmeth/journal/v11/n5/full/nmeth.2918.html>`__,
   why not engineer our own pathways and put them into tractable
   organisms to study in more detail?

   I think this is one of the more likely ideas to ultimately work
   out, but it has a host of problems.  For one thing, you need to
   have strong and reliable predictions of gene function.  For
   another, not all microbes will be able to execute all pathways, for
   various biochemical reasons.  So I expect the failure rate of this approach
   to be quite high, at least at first.

   Pros: when it works, it'll be awesome!  And, unlike the functional
   metagenomics approach, you can really engineer anything you want -
   you don't need to find all your components already assembled in a
   PCR product or fosmid.
   
   Cons: expensive at first, and likely to have a high failure rate.
   Unknown scalability, but probably can be heavily automated, especially
   if you use selection approaches to enrich for organisms that work
   (see previous item).


Computational exploration and determination of gene function
============================================================

6. Metabolic modeling

   Look at the genome, feed it into a model of metabolism, and try to
   understand what genes are doing and what genes are
   missing. `Metabolic flux analysis
   <http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3108565/>`__ provides
   one way to quickly identify whether a given gene complement is
   sufficient to "explain" observed metabolism, but I'm unsure of how
   well it works for badly annotated genomes (my guess? badly ;).

   You can marry this kind of metabolic analysis with the kind of
   nifty fill-in-the-blank work that `Valerie de Crecy-Lagard
   <http://microcell.ufl.edu/valerie-de-crecy-lagard/>`__ does -- I
   met Valerie a few years back on a visit to UFL, and thought, hey,
   we need hundreds of people like her!
   
   In practice, this is going to be much easier in phylogenetically
   closer organisms where we can make better use of homology to
   identify likely mis-annotated or un-annotated genes.  It also
   doesn't help us identify completely new functions except by missing
   energy.

   Pros: completely or largely computational and hence potentially quite
   scalable.

   Cons: completely or largely computational, so unlikely to work that
   well :).  Critically dependent on prior information, which we
   already know is lacking.  And hard or impossible to validate; until
   you get to the point where on balance the predictions are not wrong,
   it will be hard to get people to consider the expense of validation.

7. Gene-centric metabolic modeling

   Rather than trying to understand how a complete microbe works, you can
   take your cue from geochemistry and try to understand how a set of genes
   (and transcripts, and proteins) all cooperate to execute the given
   biogeochemistry.  The main example I know of this is from `Reed et al.
   2013 <http://www.pnas.org.proxy1.cl.msu.edu/content/early/2014/01/15/1313713111.full.pdf>`__, with Julie Huber (`@JulesDeep <https://twitter.com/JulesDeep>`__) and Greg Dick.

   Pros: completely or largely computational and hence potentially quite
   scalable.

   Cons: requires a fair bit of prior information.  But perhaps easier to
   validate, because you get predictions that are tied closely to a
   particular biogeochemistry that someone already cares about.

8. Sequence everything and look for correlations.

   This is the quintessential Big Data approach: if we sequence everything,
   and then correlate gene presence/absence/abundance with metadata and
   (perhaps) a smattering of hypotheses and models, then we might be able
   to guess at what genes are doing.

   Pros: we're doing the sequencing anyway (although it's not clear to me
   that the metadata is sufficient to follow through, and data availability
   is a problem).  Does not rely on prior information at all.

   Cons: super unlikely to give very specific predictions; much more
   likely to provide a broad range of hypotheses, and we don't have
   the technology or scientific culture to do this kind of work.

9. Look for signatures of positive selection across different communities.

   This is an approach suggested by Tom Schmidt and Barry Williams,
   for which there is a paper soon to be submitted by Bjorn Ostman and
   Tracy Teal et al.  The basic idea is to look for signatures of
   adaptive pressures on genes in complex metagenomes, in situations
   where you believe you know what the overall selection pressure is.
   For example, in nitrogen-abundant situations you would expect
   different adaptive pressures on genes than in more nitrogen-limited
   circumstances, so comparisons between fertilized and unfertilized
   soils might yield something interesting.

   Pros: can suggest genes without relying on any functional
   information at all.

   Cons: unproven, and the multiple-comparison problem with statistics
   might get you.  Also, needs experimental confirmation!

My favorite idea - a forward evolutionary screen
================================================



10. Here's an idea that I've been kicking around for a while with
    (primarily) Rich Lenski (`@RELenski <https://twitter.com/RELenski>`__), based on `some Campylobacter
    work <http://www.ncbi.nlm.nih.gov/pubmed/21283682>`__ with JP
    Jerome and Linda Mansfield.

    Take fast evolving organisms (say, pathogens), and evolve them in
    massive replicate on a variety of different carbon sources or other
    conditions (plates vs liquid; different host genotypes; etc.)  and
    wait until they can't cross-grow.  Then, sequence their genomes and
    figure out what genes have been lost.  You can now assume that
    genes that are lost are not important for growing in those other
    conditions, and put them in a database for people to query when
    they want to know what a gene might *not* be important for.

    We saw just this behavior in Campylobacter when we did serial transfer
    in broth, and then plated it on motility assay plates: Campy lost its
    motility genes, first reversibly (regulation) and then irreversibly
    (conversion to pseudogene).

    Pros: can be automated and can scale; takes advantage of massive
    sequencing; should find lots of genes.

    Cons: potentially quite expensive; unlikely to discover genes specific
    to particular conditions of interest; requires a lot of effort for
    things to come together.

So that's my list.

Can't we all get along? A need for complementary approaches.
============================================================

I doubt there's a single magical approach, a silver bullet, that will
solve the overall problem.  Years, probably decades, of blood, sweat,
and tears will be needed.  I think the best hope, though, is to find
ways to take advantage of all the tools at our disposal -- the -omics
tools, in particular -- to tackle this problem in reasonably close
coordination between computational and experimental and theoretical
researchers.  The most valuable approaches are going to be the ones
that accelerate experimental work by utilizing hypothesis generation
from large data sets, targeted data gathering in pursuit of a
particular question, and pointed molecular biology experiments looking
at what specific genes and pathways do.

How much would this all cost?
=============================

Suppose I was a program manager and somebody gave me $5m a year for 10
years to make this happen.  What would be my Fantasy Grants Agency
split?  (Note that, to date, no one has offered to give me that much
money, and I'm not sure I'd want the gig.  But it's a fun brainstorming
approach!)

I would devote roughly a third of the money to culture-based efforts
(#1-#3), a third to building computational tools to support analysis
and modeling (#6-#9), and a third to developing out the crazy ideas
(#4, #5, and #10).  I'd probably start by asking for a mix of 3 and 5
year grant proposals: 3 years of lots of money for the stuff that
needs targeted development, 5 years of steady money for the crazier
approaches.  Then I'd repeat as needed, trying to balance the craziness
with results.

More importantly, I'd insist on *pre-publication* sharing of all the
data within a walled garden of all the grantees, together with regular
meetings at which all the grad students and postdocs could mix to talk
about how to make use of the data.  (This is an approach that Sage
Biosciences has been pioneering for biomedical research.)  I'd
probably also try to fund one or two groups to facilitate the data
storage and analysis -- maybe at $250k a year or so? -- so that all of
the technical details could be dealt with.

----

Is $50m a lot of money?  I don't think so, given the scale of the
problem.  I note that a few years back, the NIH NIAID proposed to
devote 1-3 R01s (so $2-4m total) to centers devoted to exploring the
function of 10-20 pathogen genes each, so that's in line with what I'm
proposing for tackling a much larger problem.

--titus
