The lamprey genome paper is out!
################################

:author: C\. Titus Brown
:tags: science,genome assembly,lamprey
:date: 2013-02-26
:slug: the-lamprey-genome
:category: science

A short note -- the lamprey genome (P. marinus) paper is finally out!
You can see `the paper
<http://www.nature.com/ng/journal/vaop/ncurrent/full/ng.2568.html>`__
and the Michigan State University `press release
<http://msutoday.msu.edu/news/2013/ancient-lamprey-dna-decoded/?r44b=no>`__.
(The press release isn't too bad, but I would like to point out that I
had no part in the sentence talking about how this could lead to an
understand of "when humans evolved jaws, matching arms and legs, an
adaptive immune system and more." <sigh>)

The lamprey is a jawless vertebrate that diverged from the jawed
vertebrate lineage around 550 mya.  Lampreys, together with hagfish,
represent the last extant vestiges of the evolutionary lineage
bounded by invertebrate chordates -- organisms without vertebrate
features -- and jawed vertebrates, which include fish, frogs,
and mammals.

The genome was a gigantic pain in the butt.  We (and by "we" I mean
Jeramiah Smith, the first author) could only assemble 800 Mbp, a
maximum of 2/3 of the estimated complete genome (which is in the range
of 1.2-1.6 Gbp, depending on which estimates you believe).  This is
partly because the genome has a bunch of really annoying GC-rich
repeats that confounded much of our BAC sequencing and hence much of
our scaffolding.

The other reason for the incompleteness of the genome is much less
common and more problematic: we constructed our sequencing libraries
from liver, which, in the lamprey means that we're missing 20% or more
of the genome.  This is because the lamprey genome undergoes
`lineage-specific loss of genomic DNA
<http://www.pnas.org/cgi/pmidlookup?view=long&pmid=19561299>`__.  (At
this point you should say "WHAT? WHY!?" and/or lament the cost of
sequencing and analyzing a subset of the germ line genome :).

Remember, genomics *is* out to get you.

What's the single most interesting take-home observation?
---------------------------------------------------------

The main section to read, I think, is "Duplication structure of the
genome."  Here, we (again, mostly Jeramiah, with a lot of input from
others) argue that synteny analysis shows

   "the most recent (two-round) whole-genome duplication event likely
   occurred in the common ancestral lineage of lampreys and
   gnathostomes."

Other things discussed are

   we (i) provide genome-wide evidence for two whole-genome
   duplication events in the common ancestral lineage of lampreys and
   gnathostomes, (ii) identify new genes that evolved within this
   ancestral lineage, (iii) link vertebrate neural signaling features
   to the advent of new genes, (iv) uncover parallels in immune
   receptor evolution and (v) provide evidence that a key regulatory
   element in limb development evolved within the gnathostome lineage.

So, overall, pretty cool.

My main involvement in the nitty gritty of this paper was a sadly
failed attempt to use protein domain alignment to determine the
duplication structure of the genome.  Because the initial assembly we
had was not very good (it was considerably worse than the one that
finally got published!) I tried to develop a novel approach using PFAM
models to drive gene/domain alignment, followed by automatic tree
examination.  This approach unambiguously indicated that there had
been no 2R. However, a few months later, after I did some QC and ran
some models, it turned out that the approach was extraordinarily
sensitive to gene loss.  This occasioned a very embarrassing e-mail
to the lamprey genome list, sigh.

(Genomics *really is* out to get you.)

The syntenic 2R analysis on a new Jeramiah-generated assembly turned out
to be much better and argued for the pre-divergence 2R scenario.

Are you still working on lamprey?
---------------------------------

The lamprey genome is one of two projects that launched my research
into assembly; `digital normalization was
<http://arxiv.org/abs/1203.4802>`__, in large part, driven by the
desire to assemble approximately 5 billion mRNAseq reads produced by
Weiming Li's lab.  We were driven to do this by the poor quality of
the initial lamprey genome, and the newer revelation that large
portions of the genome are simply missing.  (In general, it seems like
the genomics research community is starting to realize that mRNAseq is
a complementary approach to genome assembly, which is often `quite
hard <http://ivory.idyll.org/blog/thoughts-on-assemblathon-2.html>`__.

Our paper on assembling massive mRNAseq is still in the process of
being written.  Preliminary results from that work indicate that we do
see about 20-30% of transcribed & conserved genes missing from the
lamprey genome, but we're still nailing down the numbers -- large
transcriptome assemblies turn out to be really messy!

--titus

(Note: fixed 800 Gbp => 800 Mbp; hat tip to Daniel Standage for noticing!)

