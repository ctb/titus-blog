Posted the Chick Genome Improvement Grant
#########################################

:author: C\. Titus Brown
:tags: assembly
:date: 2014-01-26
:slug: 2013-posted-chick-improvement-grant
:category: science

I've just posted `the narrative
<http://ged.msu.edu/downloads/2013-chick-genome-improvement.pdf>`__
for a recently funded USDA grant on improving the quality of the chick
genome assembly on `the lab's research page
<http://ged.msu.edu/research.html>`__.  The issues are laid out in
detail in the grant, but, basically, the question is: how can we
improve the quality of the assembly?  The answer, we think, is to
pursue a range of strategies that include additional sequencing to get
at the microchromosomes, as well as improved assembly merging and
scaffolding tools capable of dealing with a range of sequencing data
types.

For this genome in particular, we now have Sanger, 454, Illumina, PacBio,
and Moleculo data.  How do you cross-evaluate that data, much less
combine it all?  Interesting questions!

We do know that reasonably sizeable chunks of the chick genome are
missing or unscaffolded, in part because they're hard to sequence and
in part because they're hard to assemble.  The PacBio data is already
leading to significant improvement in galGal 4, and now we're trying
to figure out how to make use of the Moleculo data, too.

One particularly interesting approach I'm working on is to release some or
all of the data so that assembler authors can experiment with all of this
data.  In particular, it should be possible to release a small subset of
the data for whatever is *not* represented in the current assembly; this
certainly includes a bunch of microchromosomes. I'll keep you posted.

--titus

p.s. Remember when I didn't work on euk genome assembly? Yeah, me too.  I can
already tell I'm going to long for the days of "simple" metagenome and
transcriptome assembly work ;)