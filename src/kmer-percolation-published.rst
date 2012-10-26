The story behind "Scaling Metagenome Assembly with Probabilistic de Bruijn Graphs"
##################################################################################

:author: C\. Titus Brown
:tags: metagenomics,khmer,k-mers,assembly
:date: 2012-08-04
:slug: kmer-percolation-published
:category: science

This is the story behind our PNAS paper, `"Scaling Metagenome Assembly
with Probabilistic de Bruijn Graphs"
<http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__ (released
from embargo this past Monday).

Why did we write it?  How did it get started?  Well, rewind the tape
2 years and more...

There we were in May 2010, sitting on 500 million Illumina reads from
shotgun DNA sequencing of an Iowa prairie soil sample.  We wanted to
reconstruct the microbial community contents and structure of the soil
sample, but we couldn't figure out how to do that from the data.  We
knew that, in theory, the data contained a number of partial microbial
genomes, and we had a technique -- de novo genome assembly -- that
could (again, in theory) reconstruct those partial genomes.  But when
we ran the software, it choked -- 500 million reads was too big a data
set for the software and computers we had.  Plus, we were looking
forward to the future, when we would get even more data; if the
software was dying on us now, what would we do when we had 10, 100, or
1000 times as much data?

We'd already tried a number of other approaches.  Shotgun sequencing
delivers the sequences in random order, sampled randomly from the
community of genomes; we thought perhaps we could get an approximate
idea of the microbial community gene content by comparing these
sequences to known genes and looking for similarities.  This approach
was, it turned out, really slow and error prone; there were lots of
reads, and the reads were also pretty short so there wasn't much
information in each read.  We'd calculated that we would need a few
weeks of computer time to get kind of a crummy result.  And, even
worse, when we got 1000x as much data we would need many years of
compute power (or even bigger computers) to do the search.

We also had tried throwing out some of the sketchier bits of data, an
approach used by several earlier metagenome publications ( the
`rumen <http://www.ncbi.nlm.nih.gov/pubmed/21273488>`__ and `MetaHit
<http://www.ncbi.nlm.nih.gov/pubmed/20203603>`__ papers).  The idea
here was that reads that contained random sequencing errors would not
look like other reads, and so we could throw away reads that didn't
overlap with many other reads.  The problem here was that we already
knew that soil communities were really complicated and contains lots
of different species, so we suspected that even with a lot more data
there wouldn't be much similarity between real reads -- so we'd throw
out errors *and* real information together.  Even worse, it *still*
wouldn't scale -- when we got 10x more data, we'd have to calculate
the similarities for all of it, and it just wasn't going to be
possible.

The real problem was just that it was *so much data*.  500m reads,
with each read of length 100 bases, equates to 50 billion bases of
DNA, or 50 gigabases; that's approximately 17 human genomes worth of
DNA, or 5000 microbial genomes.  Even worse, this data was from a
really genetically diverse sample, which meant that when we tried to
count the unique sequences in it, we tended to break the computer we
were using.

It was actually this breakage of computers that led, indirectly and
inadvertently, to the breakthrough that underlies this paper.  One of
my graduate students kept on crashing our server by trying to count
the number of unique subsequences within the data set.  The existing
software (a program called 'tallymer') consumed too much memory and
disk space to be usable on this data set, and every time he ran it
on more than half of the data, the computer would die.  This got me
upset and led to the conclusion that there was simply no way to tackle
this problem with an existing approach.  (Moral: giving up on other
people's software is sometimes the first step to success!)

Concurrently, we'd asked some collaborators to loan us a program
that they'd been using for eliminating sketchy sequences.  It sounded
like it might solve some of our problems, if not all.  However,
luckily they refused to give us that early version of their software,
because it turned out to be somewhat of a blind alley for them
(and would have been for us, too).

Irritated with both my graduate student crashing my machines and the
collaborators who refused to share their source, I went home that
evening and tried to figure out a clever way of counting subsequences.
After an hour or two of thought, I realized that I could combine some
simple counting software I'd written in graduate school with an
inexact counting mechanism, and upon trying it out, it seemed to work
and be pretty low memory -- thus was `khmer
<http://github.com/ged-lab/khmer>`__ reborn.  (Later, it turned out
that we'd reinvented a variant of the counting `Bloom filter
<http://en.wikipedia.org/wiki/Bloom_filter>`__, also known as the
`Count-Min sketch <http://en.wikipedia.org/wiki/Count-Min_sketch>`__
data structure; see `my first blog post on this, too
<http://ivory.idyll.org/blog/kmer-filtering.html>`__.)

This approach let us complete a bunch of analyses, and it's actually
at the core of our *second* paper, which has not yet been accepted for
publication (`see it on arXiv <http://arxiv.org/abs/1203.4802>`__);
but it turned out that just counting things wasn't going to solve our
problem.

We banged our heads against the wall for a few more months, trying
this and that -- something that people may not appreciate about Big
Data is how darned *long* it takes to do anything with multiple
gigabytes of data... -- but made little progress.  Then I went to the
`Terabase Metagenomics meeting
<http://ivory.idyll.org/blog/terabase-metagenomics.html>`__, which was
something of a catalyst.  As my `report on the computational side of
the meeting said
<http://ivory.idyll.org/blog/computation-for-terabase-metagenomics.html>`__,
metagenome assembly should, in theory, be scalable.  Metagenomes
consist of dozens to millions of species, and it should be possible to
break up the short read data set by which species the reads come from.
If this could be done efficiently, it would then be easy to put
together the reads from each of the species.

Well, ok, yes.  And it took us another year and a half to get it working :).

I came back from the meeting (in summer 2010) with the belief that
this problem must be solvable, and then spent an afternoon sitting
around a table and brainstorming with Jason Pell, Rose Canino-Koning,
Arend Hintze, and Adina Howe.  And what we came up with was the
solution we just published!  Basically, we took the khmer solution
we'd built for counting subsequences, switched it over to store just
presence/absence, and then figured out how to walk from subsequence to
subsequence.  This let us figure out what subsequences were connected
transitively, which let us figure out what subsequences *weren't*
connected at all, which then let us separate reads into disconnected
bins, which (in theory, and mostly in practice) represent different species.

Overall, this is a pretty hard problem to compute.  We were looking at
graphs that contained billions of nodes, and traversing them
systematically to determine which nodes are disconnected from each
other.  Doing this efficiently and in limited memory circumstances is
... hard.  But we did it, although it's barely mentioned in the paper.

We actually got that working in under a year, but we were left with a
problem.  We were using a data structure that threw in more false graph
connections the less memory we used, and we weren't sure how to prove
that the graph was still basically accurate.  This was the problem
that Jason Pell and Arend Hintze set out to address.

Here's an intuitive rephrasing of the problem.  Suppose you have a big
piece of paper with a map drawn on it.  You want to store the map more
compactly without changing the structure of the map itself.  You don't
want to fold the map up, because then it wouldn't be easy to look at.
You can't shrink it, for technical reasons.  But one way to make the
paper more compact -- the way we used for our graph -- is to crumple
the paper locally: basically just compact each part of the map
equally. (It's not something a person would do, but a computer can do
it pretty easily.)  Now, how much can you crumple the map?  You know
if you don't crumple it at all, it's too big; but if you crumple it
too much, then disparate parts of of the map will connect and you
won't be accurate any more.  Where does the map become inaccurate?

.. image:: http://ivory.idyll.org/permanent/graph-compression.png
   :width: 80%

Jason and Arend turned to `percolation theory
<http://en.wikipedia.org/wiki/Percolation_theory>`__ for this.
Percolation theory describes how graphs become connected as a function
of graph density: if there are a lot of points in a graph, at some
point you can walk from one side of the graph to the other using the
points, and percolation theory can guide you in calculating the point
density required such that this path will exist.  We knew that *if* we
could connect the graph crumpling problem to percolation theory, then
it would mean that, as you crumpled the map, at some point there would
be an abrupt change in the map structure where it went from "basically
accurate" to "no longer even remotely accurate".

And, long story short: that's exactly what Jason and Arend did.  They
showed that for both our actual graph storage *and* a simulation of
it, the graph crumpling problem was identical to the bond percolation
problem.  They also showed that when the graph crumpled to a point
where there was an ~18% chance of a false connection between any two
local points in the graph, the large-scale graph structure could no
longer be relied upon.  (Note that we couldn't show this purely
analytically, because the bond percolation problem hasn't been solved
analytically.  *That* would have been a whole different paper ;)

What this means is actually pretty simple: it tells you precisely how
far you can crumple the graph before it becomes unreliable, or, to
put it more formally, it tells you at what false positive rate our
graph storage becomes untenable for our purpose of separating reads
into different bins.

Backing waaaaay up to our original problem, it means that we could
place pretty hard limits on our ability to store and explore the data
we had.  Were these limits good or bad?  Well, the short answer is
"good" and the longer answer is "it depends" -- for subsequences of
length 31, we can store a graph containing a billion unique subsequences
in about 500 megabytes, compared to the best "uncrumpled" storage of
about 4 gigabytes.  That's pretty good.

So, in short form, what did our paper show?

First, we built a system for partitioning metagenomic data sets based
on connectivity.  Our estimate at the moment is that we can scale
metagenome assembly by a factor of about 20 better than anyone else,
i.e. given a computer we can assemble a data set that is 20x larger
than anyone else can assemble.

Second, this system is actually deployed and functional -- it works
for us, it'd work for you, it's all open source, etc. etc.  We're
using it ourselves to assemble pretty freakin' big metagenomes.  More
on that real soon now.

Third, we provided a data structure that is theoretically well
understood, in addition to being practically useful.  This lets other
people use it without fear, and in fact our method of graph
storage was picked up by another group (see `arXiv FTW
<http://ivory.idyll.org/blog/science-f-yeah.html>`__) and used to
build an actual assembler.  Pretty cool.

Fourth, this first paper is -- just like `our second paper
<http://ivory.idyll.org/blog/apr-12/replication-i.html>`__ -- entirely
replicable, although we didn't use ipython notebook or anything
particularly clever.  You can regenerate all the results in it as well
as the pre-publication paper PDF itself by `following the instructions
<http://ged.msu.edu/papers/2012-kmer-percolation/>`__.

Fifth, this paper, together with our next paper on `digital
normalization
<http://ivory.idyll.org/blog/diginorm-paper-posted.html>`__, provides
a way to completely solve the scaling problem with metagenome
assembly: we haven't done it yet, but we explained how in `my NSF
CAREER proposal <http://ivory.idyll.org/blog/grants-posted.html>`__.
(If someone wants to give me \\$200k I will give them a nice functioning
solution, hint hint.  Or you can implement it yourself; how hard can
it be?  heh. heheh.)

IMO, the real novelty of this paper lies in its being the first paper
that I know of to provide a scaling solution specific to metagenome
assembly.  In fact, I know of only one other group that's working on
metagenome assembly scaling (the Banfield group) and their solution is
orthogonal (complementary) to ours, so we actually hope to combine it
with ours.  (If you know of others, leave a comment below.)

But whatever others may make of it, the paper is a nice, solid
first bit o' science, and I am really proud of it and my co-authors.  If we
can maintain this level of quality for all our papers (high quality
*independent* of editorial estimate of impact, note) then I will be a
happy camper.

--titus
