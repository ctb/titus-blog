Assembling genomes with modern sequencing
#########################################

:author: C\. Titus Brown
:tags: bioinformatics,assembly,skepticism,assemblathon
:date: 2011-08-09
:slug: assemblathon-and-assembly
:category: science


As sequencing gets cheaper and cheaper, one would expect the answer
for how to best sequence (and assemble!) any given genome would
change.  Most biologists assume something along these lines: everyone else
has achieved some standard coverage (say 10x, or 100x) for their genome,
so all we need to do is multiply that number times the size of my genome
of interest, and then multiply that by the cost/bp, and voila! I will
be able to have my very own genome sequence!

Naturally it's a bit more complicated than that, for a couple of
reasons.  First, the length of the reads matters quite a bit.  If
you're reading off a 1 GB eukaryotic genome in chunks of 100 bases,
you're going to have trouble assembling the darn thing.  First, you
have to worry about complex repeats, which (in the context of
assembly) are just plain evil, because they create connectivity
structures that simply can't be resolved without additional
information.  Second, you need to think about sequencing bias, such as
GC and AT rich regions -- most sequencers don't do that well on
GC-rich regions, which are plentiful in big eukaryotic genomes.  And
third, normal sampling variation in shotgun coverage will screw you,
on top of all of this, if you don't think about it.

So, what *is* the optimal sequencing strategy, then?

There's been some interesting discussion on the `assemblathon
<http://assemblathon.org/>`__ `mailing list
<http://assemblathon.org/pages/mailing-list>`__ about all of this,
which, for the most part, I'll be paraphrasing and interpreting: the
list archives are closed and the list policy about citing people is
that I need to ask them for individual permission, and that's too much
work :).  If you're interested in the source messages, I recommend
subscribing yourself and looking through the archives for messages
from June 2011; if they open up the archives, I'll link directly to
some of the more interesting messages.

A key component of any sequencing strategy discussion nowadays is that
sequencing has become *very* commercial.  While this drives down costs
(pretty dramatically!), you also can't trust a damn thing that
sequencing companies say, because the market is very competitive and
there's very little percentage in straight-up honesty, much less full
disclosure.  (Paranoid much?  Yeah, buy me beer sometime.)  Moreover,
there are several competing sequencing centers -- primarily the Broad
Institute and the Beijing Genome Institute, as well as the Joint
Genome Institute, Sanger, and St. Louis, and probably another five that
I'm missing -- that all appear to have
adopted different policies with respect to sequencing genomes.  I
don't really know what they are in detail, but (for example) Broad has
a stereotyped sequencing strategy for which it has written its own
software suite (see `ALLPATHS-LG
<http://www.broadinstitute.org/software/allpaths-lg/blog/>`__), and
you can read the details in `the PNAS paper
<http://www.pnas.org/content/early/2010/12/20/1017351108.full.pdf+html>`__.
The bottom line is you need to talk to people who have experience with
actual sequence, and not be overly trusting of either sequencing centers
or company reps.

Another key component of any sequencing strategy discussion is the
software being used to assemble.  Some centers have their own
assemblers (BGI has SOAPdenovo, Broad has ALLPATHS-LG), but there are
literally dozens of assemblers out there.  The assemblers can broadly
be broken down into about four different types:
overlap-layout-consensus, de Bruijn graph, greedy local, and "other".
I'm most familiar with de Bruijn graph assemblers, since that's what
I'm working with here at MSU, but there are advantages and
disadvantages to the various kinds.  Maybe more on that later.
But the bottom line here is that there are many brilliant, passionate,
opinionated people who have written their own assembler, and will
swear by all that is holy that it is the best one.  How do you choose?

A third key component of any sequencing strategy discussion is the
genome itself.  Mihai Pop's group just published a veddy interesting
article on prokaryotic assembly (see `Wetzel et al., 2011
<http://www.ncbi.nlm.nih.gov/pmc/articles/PMC3103447/>`__) in which
they argue that the optimal sequencing strategy needs to be
dynamically adjusted to the repeat structure of the genome: that is,
you need to do a first sequencing run; analyze it for repeat
structures; and then plan out your next rounds of sequencing based on
that information.  While I am always suspicious of plans that require
intelligent thought (slow! expen$ive!) to be inserted into sequencing
pipelines (fast! high throughput!), I think they make a pretty good
argument -- and that's just for prokaryotic genomes, which are simple
compared to eukaryotic genomes... for eukaryotic genomes, you also
have to worry about heterozygosity (how much internal variation there
is between the two haploid genomes you're sequencing).  So how can
you strategize to deal with your genome?

But let's back up.  What are we doing, again?

Sequencing genomes is like this:

Long, not-terribly-random strings of (physical) DNA, O(10^7-10^10) in length.

Goal: determine full sequence and connectivity of strings of DNA.

Process: fragment into lots of bits, sequence in from both ends of each
bit.  Use overlaps, size of bits ("insert size"), to computationally
reassemble.

(You can read an earlier blog post about why this is a hard problem
`here <http://ivory.idyll.org/blog/aug-10/assembly-part-i.html>`__, or
go read the UMD CBCB assembly primer `here
<http://www.cbcb.umd.edu/research/assembly_primer.shtml>`__.)

The challenge, succinctly put, is this: in the face of uneven coverage
and repetitive subsequences, devise the optimal coverage and range of
insert sizes so that you can (a) sample most of the genome
sufficiently and (b) resolve most repetitive regions by looking at
pairs of ends.  Do so (c) as cheaply as possible.

OK, so what are the parameters you can twiddle?

It really boils down to these choices:

Sequencing technology: 454 or Illumina are the main production
machines these days, although I hear things about PacBio, Ion Torrent,
and ABI SOLiD.  454 is much more expensive per base, but gives longer
reads (500bp +); Illumina is (much) cheaper per base, but the reads
are annoyingly short (100-150 bp).  With Illumina you can get ~600 bp
inserts easily, larger inserts (3kb, 5kb, 10kb) with more difficulty.
Not sure about 454.

Coverage: how much money do you want to spend, on what sequencing
technology?

Insert sizes: larger inserts are really useful for bridging repeats, but
also much more expensive.

And... I think that's about it.  Or is it?

Well, you need to ask two more questions: can your assembler of choice
take advantage of mixed read lengths, with mixed error models from
different technologies, and/or various insert sizes?  And can your
sequencing center actually make all the different technologies work
reliably?

(As I keep telling my students, if it were easy they wouldn't need brilliant
people like us to work on it, now would they?)

----

When I get swamped with these kinds of questions, I usually try to
retreat back into my reductionist hidey hole to clear my head.  So
let's back up again.  What are the fundamental issues?

We can't do much about sequencing bias or heterozygosity, except to
say that more coverage is generally going to make both biases and
internal sequence variation stand out more reliably from random error.
If we actually want to assemble our genome, we also can't do much
about improving current assemblers, and it's unclear how to evaluate
assemblers anyway, and most of them don't appear to do a great job on
very heterogenous sequence types (i.e. from multiple types of
sequencers) - anyway, these are the questions the assemblathon is
asking, and they're doing a good job; just read the paper when it
comes out.  And we don't have much control over whether or not our
sequencing center screws up.

So we're left with trying to decide on how much 454, how much
Illumina, and what insert sizes.  (Can you hear the shrieks of pain
from sequencing and assembly aficionados as I ruthlessly strip all
of the subtleties from the argument? Fun!)

For insert size, I like to point people to these two references:

Whiteford et al., Nuc. Acid Res, 2005
http://nar.oxfordjournals.org/content/33/19/e171.full

Butler et al., Genome Res, 2008
http://genome.cshlp.org/content/18/5/810.full

which make the nice point that there are many repeat structures that
you simply cannot resolve with single-ended reads -- you *need*
paired-end reads to do a good job of assembly.  These two papers have
recently been joined by a third, the Wetzel et al. paper above, which
suggests that there are particular (and surprisingly frequent) repeat
structures that cannot be resolved except by a very specific insert
size.  But barring advance knowledge of repeat structure, I would
argue that a nice range of inserts, from 3k to 5k to 10k, should give
you decent results.  We have that for a parasitic nematode project
in which I'm involved, and it's given us decent scaffold sizes.

With 454 vs Illumina, I am skeptical that 454 is a good expenditure of
money at this point.  The number of bases is so astonishingly low
compared to what Illumina is outputting (~1m vs ~1bn for the same
amount of money, I think?  At any rate, at least 100x) that you really
need to justify any 454 expenditure.  That having been said, I may be
so used to working with crappy genome assemblies (buy me beer,
hear me weep) that I'm ignoring how much *better* they would be with
~10x 454 coverage.  Certainly Greg Dick's group at U of M has shown me
pretty good evidence that 454 sequences things that Illumina won't
touch, in metagenomic data.  So I can't give you much more than my
experience that Illumina will get you ~80% of the way to a decent genome
assembly -- which is something many people would love to have.

Is there an elephant in the room, and, if so, what is it?  Well, this
touches heavily on our lab's research, but I think that sequencing
biases are screwing up the assembly game far more than people think.
Right now assemblers have a bunch of poorly understood heuristics that
address sequencer-specific bias, and our experience with these in
metagenomic sequencing suggests that these artifacts and heuristics
are a significant source of misassembly.  More on that ... later.

I'm really at a loss about how to conclude any discussion of
sequencing strategy.  It's ridiculously complicated, comes down to a
lot of guessing about what problems you're likely to run into, and 
involves an extremely rapidly changing technology suite.  Getting
a comprehensive answer out of *anyone* is hard... and won't get any
easier for a while.

That having been said, I'd appreciate pointers to blog posts and open
discussions of these issues on mailing lists.  Having (tried to) teach
some biologists in this area recently, as part of my NGS course, I
think actually providing these discussions could be incredibly
valuable and could raise the level of discourse a fair bit.

--titus


----

**Legacy Comments**


Posted by Cameron Neylon on 2011-08-10 at 03:48. 

::

   It's interesting how things come back around. Towards the end of his
   PhD Nava, of the Whiteford et al paper, looked at putting together a
   benchmarking framework for the growing set of assemblers that were
   appearing at that point. Trying to think about what would be a
   meaningful benchmark was something of a challenge, I think he settled
   on taking a reference sequence and then breaking it up, introducing
   errors, and biases and then feeding each assembler a series of
   fragment collections but it never got that far. And it was unclear
   whether the results would be meaningful without running large numbers
   of tests that at the time was computationally intractable for us.    I
   don't know if it's useful but the other half of the 2005 paper that we
   eventually ripped out before submitting to NAR because no-one seemed
   to believe was a discussion of characterising the repeat structures of
   sequences. We developed some plots that did seem to be useful at
   fingerprinting various repeat structures. Unfortunately we struggled
   to get it published and it eventually appeared in Complex Systems
   where I suspect no-one has ever read it: <a href="http://eprints.ecs.s
   oton.ac.uk/20919/">http://eprints.ecs.soton.ac.uk/20919/</a>


Posted by Mick Watson on 2011-08-10 at 15:25. 

::

   Very interested in sequencing bias, however, there is a barrier to
   this: should one publish data showing there is a bias in your data,
   how do you avoid everyone else saying "Well, ours is fine, it must be
   just your machine".. and all of a sudden your reputation takes a hit.
   How do we create a system whereby sequencing providers can safely
   discuss problems with their sequencers without their reputation taking
   a hit?    I am struck by an anecdote I heard recently: a lab manager
   at a particular sequencing company's annual event found that EVERY
   academic laboratory was having problems with that provider's
   instrument, however, every commercial provider insisted they had no
   problem.  Reputation in science is key.    Finally, on assembly.  I
   wonder if some of the reasons behind de bruijn are now falling away.
   As I understand it, de bruijn graph assembly came along due to the
   short reads, and the sheer noise created when you compare (via an
   overlap approach) millions of 36bp reads with one another.  However,
   reads are now much longer, and advances in computation mean we can
   compare reads pairwise.  I'm also struck by the performance of SGA in
   Assemblathon, which has a (string graph based) overlap approach to
   assembly.  So were/are de bruijn graph assemblers just a flash in the
   pan, only needed for short reads?  Will we see the return of the
   overlap-layout-consensus assembly algorithms?


Posted by Titus Brown on 2011-08-10 at 23:01. 

::

   Mick, thanks for your comments!    We've been tracking down a problem
   in metagenome assembly where sequencing bias is causing systematic
   misassemblies.  How would you NOT discuss that in the context of your
   own science?!  In our case we can show it's coming from multiple
   sequencers and is present in many different data sets.    For mRNAseq
   and metagenomic sequencing, I don't think that long reads will solve
   the scaling problem.  You need deep sampling for both, which is
   something that long reads don't provide yet (and when they do, voila!
   scaling problem!) They should make much better assemblies possible.
   I am intrigued by SGA but know very little about it.  I eagerly await
   awesomeness :)


Posted by Nick Loman on 2011-08-11 at 04:15. 

::

   One point I'd like to make is that many groups have gone off writing
   de novo assemblers as a theoretical exercise and very few have
   established whether they are doing a good job in reconstructing the
   biology.    Now we have efforts like the Assemblathon and GAGE to try
   and bring order to this chaos. Users are now in the habit of running a
   pipeline, chosen for good reasons or ill, and being forced to
   uncritically accept the output because they have no way of knowing
   whether their assembly is good or not.    As you point out; the
   results from 454, Illumina PE, Illumina MP etc. sequencing can be
   quite different.    I would like to see some standardised datasets for
   all platforms with well-validated reference sequences (e.g. lab
   finished) so that software can be objectively tested.    I take issue
   with your idea you NEED mate-pairs. Actually even better than that is
   really long reads, which are unambiguous and easy to assemble - so
   PacBio is going to be the one to watch. They may kill the remaining
   market for 454 de novo.    I think Mick makes an interesting point
   that de Bruijn was optimised for noisy, high-coverage data. Now we
   have better quality, longer Illumina reads it may well be that new
   approaches like SGA will come to the fore. I may have a play with this
   now.    Traditional overlap-layout-consensus algorithms cannot handle
   ultra-deep Illumina coverage, in my experience. It may be though that
   accuraet 150bp base reads treated in a conventional way does not
   require such depth of coverage as we are used to generating.

