My part of the story of the Haemonchus paper
############################################

:author: C\. Titus Brown
:tags: genomes,assembly,diginorm
:date: 2013-08-28
:slug: haemonchus-my-story
:category: science

Two papers on the *Haemonchus contortus* genome just came out
(`Schwarz et al. <http://genomebiology.com/2013/14/8/R89/abstract>`__
and `Laing et
al. <http://genomebiology.com/2013/14/8/R88/abstract>`__), and I'm an
author on one of them (Schwarz et al.).  *H. contortus*, or Haemonch (as I
affectionately called it) is a `nasty parasitic nematode
<http://en.wikipedia.org/wiki/Haemonchus_contortus>`__ that feasts on
the mucosal blood of ruminants.  It's a big agricultural pest, and
therefore important to study, and these two papers should help on the
way to the development of novel `antihelminthics
<http://en.wikipedia.org/wiki/Anthelmintic>`__.

Genomics leads in random directions, but ... how on earth did I end up
working on this??

The Story begins
~~~~~~~~~~~~~~~~

The story of my role in the Haemonchus paper starts about 3 years ago.
My friend & colleague Erich Schwarz is a guy who specializes in
nematode genomics, and he was sequencing, assembling, and analyzing
the Haemonch genome with a team down in Melbourne (largely Robin
Gasser's group, I think) as well as Paul Sternberg's lab at Caltech.

Well, I *say* he was assembling it, but he wasn't being very
successful at it.  You could have said "throwing assemblers at it
desperately" instead.  Every time I talked with him he regaled me with
tales of woe, some of which have made it into `my slides (see slide
13)
<http://www.slideshare.net/c.titus.brown/2013-ucdavissmbeeukaryotes-20285006>`__
-- to quote, "The power of next-gen sequencing: get 180x
coverage... and then watch your assemblies never finish."  The basic
problem was that every assembler he tried would slurp in the reads,
churn churn churn, and then at some point die.  Or not die.  But one
thing no assembler would do was output anything even remotely
resembling a decent assembly.  Basic quality filtering helped a bit --
Erich could get the sequencing data from short-insert libraries to
assemble, but as soon as he put in the bigger insert data, kablooey.
It didn't seem to have anything to do with compute power; rather,
something was fundamentally weird about the sequence.

While he was busy throwing himself at large volumes of sequencing
data, I was working with Jason Pell and Adina Howe on metagenomics --
that is, we were throwing ourselves at even *larger* volumes of
sequencing data.  Most vexing.  Eventually we figured out a technique
(`partitioning <http://www.pnas.org/content/early/2013/08/21/1314090110.abstract>`__) that let us cut the problem down to size, but it clearly wouldn't
work on genomes so was of no use to Erich.

As we worked, however, we found that there were annoying levels of
`connectivity <http://arxiv.org/abs/1212.0159>`__ in our metagenomic
data.  And our efforts at removing this connectivity turned out to
be of great use (although it wasn't the final kicker).

When Erich and I discussed his assembly problems, we figured it *had*
to have something to do with repeats and polymorphism.  If you have a
repeat-rich genome and a lot of polymorphism, you're gonna have a hard
time assembling much; plus, efforts to traverse those regions and
assemble them into contigs (or ignore them) were going to run into
combinatorial complexity.  So when I said we had a way to remove
highly connected regions but that it was meant for metagenomes, Erich
asked me to run it on his data.

I said no.  There was no reason to believe that it would work.

Erich insisted.

I still said no.

He continued to insist.  At some point, he must have bought me some
good steak or something. And then I decided to run our delumping code
just to get him off my back.

... Voila.  Erich took the delumped data, fed it into Velvet, and went
to sleep.  He woke up the next morning to a crash, or at least what he
*assumed* was a crash -- he'd never had an assembly complete in less
than a week on this data set.  But, of course, it turned out to be an
actual real, useful assembly!  And that was the start of the end of
the basic assembly problem for him.

This delumping wasn't the final filtering stage actually used for the
assembly.  My lab was in an intense stage where we were throwing ideas
around a lot, and about 6 months later we figured out `diginorm
<http://arxiv.org/abs/1203.4802>`__ which turned out to be a much
better tactic for all sorts of things.  (Although we're still very
fond of partitioning.  More on that in a few weeks.)  But that initial
result *was* the breakthrough in many ways, even though even today we
have at best an imperfect understanding of why it worked.

What was wrong with the Haemonch data?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As we now know, as well as originating from many different individuals
the sequence was filled with microbial contaminants; moreover the
genomes had been subjected to whole-genome amplification, which
results in dramatic coverage variation.  So we had an almost perfect
quadrifecta: a eukaryote, steeped in a virtual metagenome, with high
polymorphism, and really nasty amplification bias.  (At one point, I
estimated that the polymorphism rate was 10% -- one in ten nucleotides
was different between the two haplotypes of the diploid genome --
although I believe that number was probably inflated by a high
sequencing error rate.  But still.)  Digital normalization turned out
to solve the biggest of these problems, allowing an initial assembly; this
led to discovering the error problem and the metagenome problem, which
led to decontamination protocols; and then finally Erich built a whole
pipeline to post-process the data into a nice assembly.  It was a heck
of a lot of work on his part, and I still feel marginally guilty about
freeriding into coauthorship (but only marginally ;).

And that, boys and girls, is how I ended up in the *genome* assembly
game, as opposed to staying in my neat little boxes of metagenome and
transcriptome assembly.

Since then, we've applied khmer based techniques -- largely diginorm,
but some others as well -- to a variety of genomes, and discovered
that in many cases they work quite well in terms of producing an
initial assembly.  I believe that at least 2-3 more papers will be
coming out soon from other groups, pointing out that diginorm performs
reasonably well on genome assembly.

**Suuuuuuuuuper awesome.**

It's always nice to actually be useful.

More, I think it's a good story about the, ahem, serendipity that comes
from casual scientific interactions. I was working on soil metagenomes,
Erich was working on nematodes; whoda thunk our technology would help
him?

What's next, bub?
~~~~~~~~~~~~~~~~~

We may build some standard protocols and assessment mechanisms for
genome assembly into khmer.  I know that some groups have made a habit
out of diginorming their genomic data into oblivion, and it would be
nice to codify these practices into something more generally usable.

We also think we can use diginorm-based techniques to do some clever
things with combined Illumina and PacBio data, so hopefully more on
that soon.

And, while I'm still planning to stick mostly in my particular corner
(metagenomes for everyone! transcriptomes for everyone!) I may nip out
every now and then and poke around with a genome.

--titus
