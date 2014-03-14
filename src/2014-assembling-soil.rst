The Story Behind "Tackling soil diversity with the assembly of large, complex metagenomes"
##########################################################################################

:author: C\. Titus Brown
:tags: assembly,diginorm,partitioning
:date: 2013-03-10
:slug: 2014-assembling-soil
:category: science


I'm pleased to announce the publication of "Tackling soil diversity
with the assembly of large, complex metagenomes", by Adina Howe, Janet
Jansson, Stephanie Malfatti, Susannah Tringe, James Tiedje, and
myself.  The paper is openly available on the PNAS Web site `here
(open access)
<http://www.pnas.org/content/early/2014/03/13/1402564111.abstract>`__.

External links:

* `Joint Genome Institute press release <http://jgi.doe.gov/News/news_14_03_10.html>`__
* `GenomeWeb article <http://www.genomeweb.com/sequencing/study-details-analytical-approach-handling-large-metagenome-sample-datasets>`__
* `MSU press release <http://msutoday.msu.edu/news/2014/msu-leads-largest-soil-dna-sequencing-effort/>`__

This paper is a milestone for me personally, because it's one of the
two projects that drove my first five years of research.  This is the
project that led us to develop `scalable k-mer counting
<http://arxiv.org/abs/1309.2975>`__ with `the khmer toolkit
<http://khmer.readthedocs.org>`__; figure out `compressible De Bruijn
graphs and partitioning
<http://www.pnas.org/content/early/2012/07/25/1121464109.abstract>`__;
and ultimately led to `digital normalization
<http://arxiv.org/abs/1203.4802>`__.

The story starts way back in ~2009, when Adina Howe arrived in my lab.
She had applied for an NSF postdoctoral fellowship in bioinformatics
to work between `Jim Tiedje
<http://en.wikipedia.org/wiki/James_Tiedje>`__ and me.  (Adina
endearingly refers to me as her "less famous advisor.")  Over the
first few weeks of her time in our labs, we decided that we would
fling Adina at the `Great Prairie Grand Challenge
<http://genome.jgi.doe.gov/IowNatreferecore/IowNatreferecore.info.html>`__,
an effort to apply the newly available Illumina sequencing technology
to the characterization of soil.  I had some previous experience with
metagenomics `from grad school
<http://www.ncbi.nlm.nih.gov/pubmed/?term=18467493>`__, and somewhat
to my surprise found myself the local expert on shotgun metagenomics,
so I thought, what the heck?

We then proceeded to fail repeatedly for two years.

The fundamental challenge of this project lay at the intersection of
two problems: first, the large volume of data produced by Illumina
made most obvious approaches fail; and second, soil is the most
diverse and rich environment on the planet, exceeding the complexity
of the human genome by 100-1000 fold, meaning most obvious approaches
fail :).

What did we try?

First, we tried BLASTing the reads against nr.  This was frustrating
on several levels.  We had about 500m 2x76 bp reads from the Illumina
GAII machine, and it took a really long time to search these against a
large database like nr.  Most reads didn't match, and, when they did,
they were very short matches that we feared were non-specific.  After
a pain-filled few months of BLASTing, we decided we needed to get longer
contigs out of these.  Cue the decision to attempt assembly!

Now, we faced the problem of actually *completing* an assembly.  With
the diversity and volume of our data, most computers just ...broke.  We
spent *a lot* of time crashing our lab computers, to no avail.

Since the problem was the volume of data, we decided to try
eliminating low-coverage reads by trimming them at low-abundance
k-mers.  The logic was that we only expected high-abundance things to
assemble anyway, so if we stopped feeding low-abundance data into the
assembler maybe we could scale the whole process up. This approach had
been applied to several complex microbial communities, including
`permafrost soil <http://www.ncbi.nlm.nih.gov/pubmed/22056985>`__ and
`the rumen microbiome
<http://www.ncbi.nlm.nih.gov/pubmed/21273488>`__.  Tallymer (the only
k-mer counter available at the time) also crashed on the volume of
data, and didn't seem that useful for trimming, either.  This led us
to adapt `khmer <http://khmer.readthedocs.org>`__ to low-memory k-mer
counting and read trimming -- you can see `one of my first scientific
blog posts on that, here
<http://ivory.idyll.org/blog/kmer-filtering.html>`__.

Once we trimmed the data, we fed it into an assembler and ... got
nothing.  Turns out when you have shallow sequencing of an incredibly
diverse community, everything is low coverage; eliminating
everything with low coverage means you eliminate all your data!

(You may be noticing the "failure" theme here. Yes, it was a slightly
stressful time.)

Then came the `Terabase Metagenomics meeting
<http://www.ncbi.nlm.nih.gov/pubmed/?term=21304727>`__, a gathering of
computational folks and microbiologists interested in environmental
microbiology.  This meeting convinced me that absolutely no one had a
solution -- all of the people working on large metagenomes were stuck just
like us.  This was an important step mentally, because it
convinced me that this project was worth some real effort.  Another
important aspect of this meeting was that the one of the groups that
*claimed* they had a partial solution was unwilling to share their
code with us (despite us being, in theory, collaborators).  So I
mentally said, "screw 'em, I guess we'll have to go this alone."

Discussions at this meeting and follow-on conversations in my lab then
led to the development of the compressible De Bruijn graph
implementation `featured here
<http://www.pnas.org/content/early/2012/07/25/1121464109.abstract>`__.
The conversations went something like this: "We should be able to
subdivide the data by walking from k-mer to k-mer." "How can we do
that?"  "I don't know." "How about..." <repeated banging of head
against table followed by trial implementation> "That doesn't scale,
does it?" "No, shh, the k-mers will hear you." <repeat from beginning>

We eventually solved the problem (see `our paper
<http://www.pnas.org/content/early/2012/07/25/1121464109.abstract>`__).
Entertainingly, the paper that came out of that work happened because I
gave the task of determining the limits of our k-mer graph
storage to Jason Pell.  I specifically remember waving my hands at him, telling
him to figure it out, and
saying "You might look at percolation theory.  I bet there's a
critical point in there somewhere."  He then went off and figured it
out, taking about 6 months to become well versed in percolation theory
and associated simulations.  True story.  Mentorship at its best!

Once that worked we could assemble the Illumina GAII data by breaking it up into
disconnected partitions, or graph components.  Huzzah!  We got
about a 20x scaling factor out of this, so we could now take data that
would ordinarily require a maximum of 300 GB of RAM and work with it
in under 60 GB of RAM.  Of course, in the meantime, Illumina had come out
with HiSeq...

I vividly remember the phone call with our JGI collaborators where we
announced our partitioning approach.  I said, "Hey, so we can assemble
all 500m reads!" And they said, "Great! We just brought our HiSeqs on
line -- here's another 2 billion reads. Does your solution scale to that?"

The answer was no, our solution did not scale to that.  The reason
we'd needed to assemble in ~60 GB of RAM was that Amazon m4.xlarge
machines had 68 GB of RAM; we didn't have access to 300 GB machines.
I became rather depressed at this point.  Because of Illumina's damned
data generation capacity, we'd spent about two years coming up with
solutions that made us fall slightly slower behind than everyone else.
This didn't seem like a good way to do bioinformatics research.

The fundamental problem, it seemed, was that even when we could break
things up into partitions, the partitions would be getting bigger and
bigger as we sequenced more deeply; this led to more data to partition,
which was the blocking step.

Banging our head against this occupied our next few months.  The key
insight we eventually reached was that even though the partitions
were growing larger, at some point the *information content* was
saturated.  We just needed to stop collecting data at saturation!

This led to `digital normalization
<http://arxiv.org/abs/1203.4802>`__, a sublinear algorithm for
discarding redundant data, which turns out to be pretty widely useful
in assembly and beyond.

The story doesn't quite end there, but you can read the rest of it in
the paper we just published.  Our lab could now assemble large,
complex metagenomes fairly easily (although we still have a ways to go
towards the volume of data `we think we need
<http://ivory.idyll.org/blog/how-much-sequencing-is-needed.html>`__).
Adina spent a solid year or more analyzing assemblies and benchmarking
our approaches, and this paper is the result.

Challenges in publication
-------------------------

We submitted the paper to a Glamour Mag, and got rejected without
review.  I inquired as to why, and was told, essentially, that "we
asked several reviewers informally and they said there wasn't anything
new in the methods."  This was because we'd published the partitioning
approach already, and had submitted the diginorm paper separately as
well.  I personally thought it would be a plus that we'd evaluated the
methods thoroughly before applying them to an unknown data set, but
apparently others felt differently.

Upon submission to PNAS, one reviewer likewise commented that they
were unsure of the distinction between our various papers on the topic
of assembly and this new paper.  We tried to clarify this in the
paper, and ultimately the reviewer accepted our argument that we had
neither evaluated diginorm on metagenomes, nor shown that partitioning
led to species bins, in previous papers -- note this is *separate* from
the argument that, hey, we can do bigger assemblies than ever before.

Based on these experiences, I think this paper fell directly into the
`"novelty squared" problem identified by Josh Bloom
<https://medium.com/tech-talk/dd88857f662>`__: it's not enough to
apply validated methods to cool new data, the methods *themselves*
have to be awesome and novel as well.  When combined with the space
crunch of glam mags, this inevitably leads to bad science -- either the methods
(generally) or the data implications (rarely) are shorted in the final
paper.

tl; dr?
-------

If you've made it this far, here are my personal take home messages from
the paper. 

First, our combined partitioning+diginorm approach results in good
sensitivity and specificity when applied to known communities.  This
mirrors what we've heard from many others who are now using the
diginorm approach.

Second, binning metagenome reads by De Bruijn graph partitions results
in species- or strain-level bins of reads.  That was our intuition at the
time, and it's nice to see it born out.

Third, assembling dramatically improves the detection signal for
similarity searches (see figure S5).  Since this was our original
rationale for assembly it's nice to see it born out.  My pithy take
home message here is, **Friends don't let friends annotate single
reads.**

Fourth, we need higher coverage.  We only assembled 20% of the data,
and it seems likely (based on our coverage plots; see Fig 2) that this
is due to low coverage.  Give us 10x as much data and we'll give you
3x as much assembly :).

Related to this, I commonly get the question: "but you're ignoring 80%
of your data by only annotating your contigs!" Yep.  I'd rather have
20% accurately annotated than 100% badly annotated, but YMMV -
hope you have a good rationale for how the increased false positive
rate is not a problem.

Take home career messages
-------------------------

Looking back, I'm pretty sure I wouldn't have taken on this project
if I'd understood the problem better.  But it's been one of the projects
that's defined my research program.  Hmm, food for thought.

Despite our progress, I've repeatedly failed to get funding for
environmental metagenome assembly.  Either I'm really bad at
explaining the problem, or it's not viewed as an important problem, or
we're tackling problems that not many people have yet.  How do you
evaluate this?

Good methods generalize.  We've done our best to minimize parameters and
heuristics in our approaches, and, in reward, our approaches apply broadly.
We don't yet entirely understand the nature of the solutions -- partitioning
is annoyingly sensitive to coverage -- but we're working on it.

Tackling hard problems sometimes pays off! Most of my research program
came out of our various attempts to solve this problem.

--titus
