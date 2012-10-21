Guest post
##########

:author: Rohan Maddamsetti
:tags: science,guestblog,beacon,evolution
:date: 2012-10-22
:slug: rohan
:category: science
:status: draft

**Note:** this post is a guest post by Rohan Maddamsetti, posted by the
regular blog author, Titus Brown. Typos are Titus's fault. Flaws in
logic are Rohan's ;). See `the paper on arXiv <http://arxiv.org/abs/1210.0050>`__ [#arxiv]_ and the
discussion on `Haldane's Sieve
<http://haldanessieve.org/2012/10/02/horizontal-gene-transfer-may-explain-variation-in-%CE%B8s/>`__,
also.

I recently wrote a short paper explaining some interesting results
reported by Inigo Martincorena and coauthors [#inigo]_. I replicated the main
result of the original paper, which is that neutral (nearly-neutral if
you want to be a stickler) variation across E. coli genes varies over
several orders of magnitude. Neutral variation is measured by
$\\theta_s = 2 N_e \\mu$, where $N_e$ is the coalescent effective
population size, and $\\mu$ is the mutation rate per
nucleotide. Inigo and I disagree about the source of this variation -
I believe it is in $N_e$ , while Inigo believes it is due to
$\\mu$. In this blog post, I'm going to talk about why I think these
results are important and interesting.

A very important semantic point needs to be made first. Inigo and I
examine the rate of synonymous substitutions, and use this as a proxy
for the rate of neutral mutations. This is why we talk about $\\theta_s = 2N_e\\mu$, rather than $\\theta = 2N_e\\mu$ -- because neither of us
are actually measuring the de novo mutation rate. Drawing conclusions
about the mutation rate from the rate of substitutions is justified by
a classic argument which goes as follows: in an idealized population
with $N_e$ individuals, with a neutral mutation rate $\\mu$ per generation,
new mutations enter the population at a rate of $N_e\\mu$ per
generation. Since each individual is as likely as any other to
eventually be the last common ancestor of the population (probability
$1/N_e$), new mutations substitute (end up in the last common ancestor
of the population) at a rate $N_e\\mu*(1/N_e) = \\mu$.
      
Why talk about $\\theta_s = 2N_e\\mu$ in the first place? This is because
$\\theta_s$ measures the number of neutral mutations that separate two
lineages on an evolutionary tree since the last common ancestor
(Figure 1). So, $\\theta_s$ is a natural measure of genetic variation, and
can be estimated on a gene-by-gene basis. Inigo and I did this for
several thousand E. coli genes using a program called OmegaMap [#omegamap]_.

.. figure:: ../static/images/rohan-1.png
   :width: 500px

   Fig 1.
      
Time is scaled by $N_e$ generations so that the formidable mathematical
machinery of coalescent theory (see the discussion of the coalescent
in Rice's Evolutionary Theory [#rice]_, or Wakeley's Introduction to Coalescent
Theory [#wakeley]_) can be used.
	
Inigo and I both show that some genes in E. coli have far more
synonymous variation than other genes. Inigo thinks that this is
caused by the molecular clock of neutral mutation ticking faster in
some genes than others. I disagree with Inigo; instead, I believe that
some gene genealogies in E. coli have much longer branches than
others. In other words, more time has passed since the last common
ancestor of Individual 1 and Individual 2 in some genes than in
others.

This does not make sense assuming that all genes traveled together in
the lineages of Individuals 1 and 2 since they diverged; however, this
is not the case for bacteria, due to recombination and horizontal gene
transfer. Genes are fairly free to "jump ship" as it were; any two
different E. coli strains can differ by up to thousands of genes! This
means that more diverged, older versions of genes can jump into an E.
coli genome, bringing much more synonymous genetic variation than
would be expected if all genes diverged at exactly the same time.

Horizontal gene transfer can occur through a number of mechanisms,
some of which are "selfish" (hitchhiking through viruses, plasmids,
transposons, or other selfish genetic elements); others of which are
"cooperative" (homologous recombination among related bacteria,
conjugation, or transformation from environmental DNA sequences). I
like to imagine the following scenario: imagine a "wind" of diverse
alleles blowing into a population of E. coli (this "wind" is non-
conservative migration of alleles into the population). Genes under
purifying selection can resist this wind more strongly, and will have
a shorter coalescence time than genes that cannot effectively resist
the input of diverse alleles from horizontal gene transfer. Under this
model, I predict that there should be an association between $\\theta_s$ and
HGT in all clades of bacteria, and not simply in Escherichia. Further,
the strength of this association should vary with the complexity of
the bacterial community from which the genome was isolated. Perhaps
obligate symbiont bacteria with small population sizes will show
little variation in $\\theta_s$ if they don't have many potential partners for
horizontal gene transfer.
  
However, I think the coolest prediction of this model is that some
genes might have much larger population sizes than other genes. I
think this has deep implications for how speciation works in
bacteria. Perhaps the "core genome" is made up of cooperative genetic
elements that need each other to survive, while the "pangenome"
contains a lot of genetic cruft; commensal and parasitic gene
sequences that have recently entered the genome, and that selection
will soon wash out. One prediction of this hypothesis is that genes
with high $\\theta_s$ should tend to be "commensal genetic elements" that
spread easily among genomes without contributing much to
adaptation. In contrast, horizontally-transferred genes that are
important in adaptation, say for antibiotic resistance, should have a
short coalescence time in the population (because they have been
selected for recently), and so should have low $\\theta_s$. Are
multi-level selection approaches necessary to understand bacterial
speciation and genome evolution? I don't know. I think that collecting
more genome data from finer and finer timescales (going from
'Comparative genomics' to 'Population genomics' to 'Meta-population
genomics' to 'Community genomics') will help shed light on how complex
mutational processes beyond point mutation affect genomes over short
time-scales, and how much of these mutational effects end up being
purged by selection over longer time-scales.
	
As an example of complex mutational processes, the point mutation rate
across the 12 lineages of Rich Lenski's long-term E. coli evolution
experiment (LTEE - see [#ltee]_) is not constant! This is due to the fixation of
mutations in some lineages (but not others) that knock out different
DNA repair pathways, increasing the mutation rate in some lineages by
100-fold. In fact, the vast majority of the synonymous substitutions
that I observe come from these "mutator" lineages. Mutator phenotypes
are often observed in natural bacterial populations as well. I think
it's generally believed that mutator lineages tend to burn out over
long periods of evolutionary time, so that mutator subpopulations
don't contribute much to long- term adaptation. But given that over
50,000 generations of evolution, 98% of synonymous substitutions have
occurred in mutator lineages, I wonder how much synonymous diversity
in wild bacterial populations originated in mutators. Perhaps some
genes mutated heavily in a mutator, then were able to jump into a non-
mutator background. Or, perhaps some mutator lineages were able to fix
their defective DNA repair machinery through horizontal gene transfer
or homologous recombination with a non-mutator. I think this is an
interesting open question.
      
There are also mutational processes in the LTEE that do not act like a
Poisson process (any random process with a low rate of events
occurring, where the events are independent from each other, converges
to a Poisson process in the limit; point mutation is a great example of
this). Even though the 12 lineages of the LTEE started from a common
ancestor in 1988, there is an incredible amount of variation in the
number and type of transposition events involving IS elements (IS
elements are a kind of selfish genetic element in bacterial genomes)
that occurred after 40,000 generations of evolution. These events are
certainly important in the evolution observed in the LTEE, but they
behave very differently from point mutations (Figure 2). Why this is,
I really don't know.

.. figure:: ../static/images/rohan-2.png
   :width: 500px

   Fig 2.

Finally, I want to mention that a paper published this week in the
Proceedings of the National Academy of Sciences by Heewook Lee and
co-authors [#lee]_ also argues against Inigo's hypothesis that higher
expressed genes have lower mutation rates. Unfortunately, the state of
the art in sequencing technology doesn't allow for direct measurements
of the de novo mutation rate (much lower error rates are
needed). Instead, Lee et al. perform mutation accumulation experiments
to measure substitution rates in very small populations of E. coli,
thus minimizing the effects of selection. This paper in particular
does a very nice job of reviewing the literature on bacterial mutation
rates and their determinants. I recommend this paper for further
reading if you're interested.

Thanks for reading!

Rohan

p.s. Note from Titus -- the math in this blog post was formatted using
the super-awesome `MathJax <http://www.mathjax.org/>`__ system; see relevant posts on `Circles and Tangents <http://theronhitchman.calepin.co/setting-up-mathjax.html>`__ and `Amic Frouvelle <http://www.ceremade.dauphine.fr/~amic/blog/mathjax-and-pelican-en.html>`__ re configuring it for `Pelican <http://alexis.notmyidea.org/pelican/>`__, the blogging system I use.  The source for this post is `on github <https://raw.github.com/ctb/titus-blog/master/src/rohan.rst>`__ if you want to see exactly how to put in formulas.

Footnotes
~~~~~~~~~

.. [#arxiv] http://arxiv.org/abs/1210.0050
.. [#inigo] http://www.nature.com/nature/journal/v485/n7396/full/nature10995.html
.. [#omegamap] http://www.danielwilson.me.uk/omegaMap.html
.. [#rice] http://www.sinauer.com/detail.php?id=7021
.. [#wakeley] http://www.roberts-publishers.com/authors/wakeley-john.html
.. [#ltee] http://myxo.css.msu.edu/PublicationSearchResults.php?group=mr
.. [#lee] http://www.pnas.org/content/109/41/E2774.abstract
