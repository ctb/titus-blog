Title: The story behind the spacegraphcats project and paper
Date: 2018-11-19
Category: science
Tags: spacegraphcats, graphs, dbg, cdbg, metagenomics, k-mers
Slug: 2018-spacegraphcats-paper
Authors: C. Titus Brown
Summary: The TRUE story!

We recently posted a preprint entitled "Exploring neighborhoods in large metagenome assembly graphs reveals hidden sequence diversity" ([biorxiv link](https://www.biorxiv.org/content/early/2018/11/05/462788)). This work is the *first* but hopefully by no means the *last* product of the **spacegraphcats project**, a collaboration between my lab, Blair Sullivan's lab at NC State, and Jeff Heer's lab at UW Seattle. It is the first fruit of two and a half years of intense work by one of the most interdisciplinary teams I've ever had the pleasure of working with, and I want to share some of the story!

## The background

In January and February of 2016, I read two papers that had a tremendous impact on my thinking - the [MetaPalette paper](http://msystems.asm.org/content/1/3/e00020-16) and the [mash paper](https://genomebiology.biomedcentral.com/articles/10.1186/s13059-016-0997-x) (see [my blog post on k-mers and taxonomy for more background here](http://ivory.idyll.org/blog/2017-something-about-kmers.html)).  I immediately jumped on these concepts, [reimplementing mash in Python](http://ivory.idyll.org/blog/2016-sourmash.html) and started playing around with it - this was the start of [sourmash](http://joss.theoj.org/papers/3d793c6e7db683bee7c03377a4a7f3c9).

I then spent a few months playing around with applying MinHash to De Bruijn graphs of metagenomes. Since MinHash works with k-mers, and De Bruijn graphs are just collections of k-mers, I thought, hey, maybe we can do something cool with MinHash and De Bruijn graph structure. So I spent a lot of time hacking on khmer and sourmash and playing with various concepts.

(I *still* think the ideas I generated during this phase are really promising, but after two years I have many, many, many detailed reasons as to why most of them are naive and not only don't work but can't work. Science sucks, man. But it did lead in several excellent directions so the work is not wasted.)

The conclusion I reached from all this work was that we needed a good way to select k-mers from *neighborhoods* within a graph. Collections of shotgun reads were not so useful for this - close bits of the graph are not local within the reads. We'd done some work on partitioning graphs as part of [Pell et al., 2014](http://www.pnas.org/content/109/33/13272) but I knew that partitioning wouldn't work here. (Turns out assembly graphs are generally completely connected, for Reasons.)

## Enter the Barnraising for Data-Intensive Discovery

In May 2016, I joined about 20 people at an event organized by Blair
Sullivan and Casey Greene, entitled the Barnraising for Data-Intensive
Discovery.  The idea was to gather a bunch of researchers in an
isolated location for a week, define some projects of mutual interest,
and hack on them together in a spirit of mutual assistance - hence
"Barnraising".  The invitees included anyone funded by the Moore Data
Driven Discovery program, and we ended up with a nice mixture of
computer scientists, biologists, mathematicians, and other
researchers.

The Barnraising was held at the Mount Desert Island Biological
Laboratory in Maine, and while the weather was absolutely miserable
(cold and rainy!) the environment **inside** was pretty great!  At the
opening meeting I pitched my "hey I need to cut graphs up into
neighborhoods" idea and it intrigued several people, including Blair
and two people from her lab, Felix Reidl and Michael O'Brien, a
postdoc and grad student respectively.  We also recruited Dominik
Moritz, a graduate student from Jeff Heer's lab at UW (Jeff was also
an Investigator, and the UW eScience Institute was a Moore DDD Data
Science Environment awardee).

(These four researchers ended up being four of the other five
authors on this paper!)

## My initial (bad) idea, and the origin of the name "spacegraphcats"

The idea I'd pitched to the larger group was that metagenome assembly
graphs should, by all rights, consist of neighborhoods of more densely
connected k-mers (representing individual species) that were sparsely
connected to other (unrelated) k-mers; and that this sparse graph
could, potentially, be **cut** into species neighborhoods. I was
interested in looking directly at the assembly graph structure to make
these cuts, without going through the filter of outputting contigs
(which _do_ cut the graph, but... not in a way that I trust :).

During the course of the project, the ideas got significantly modified
as it became clear that I didn't know that much about graphs in general,
or metagenome graphs, and that my intuition was (in places) flatly
wrong. 

Now, you may wonder why the software mentioned in the paper is called
"spacegraphcats". Well, if you pass "sparse graph cuts" through the
mind of an idle German mathematician (coff FELIX coff) then said mathematician
may come up with the name "spacegraphcats". And of course when looking for
logos and related memes online, well, "space" and "cats" make things easy. And
thus "spacegraphcats" was born.

Despite the changes in the project focus, the name stayed at
"spacegraphcats", 'cause it was cool... and why not?

## What did we actually end up doing?

The whole project has a pretty broad scope, but for this first paper,
we ended up focusing in on a fairly targeted question: can we improve
the completeness of metagenome-assembled genomes, or MAGs?

Briefly, MAGs are genomes computationally extracted from metagenomes.
The usual process of inferring MAGs is to assemble a metagenomic
sample, then group contigs together into putative genomes based on
sequence composition, estimated contig abundance, and
phylogenetic marker genes.  The completeness of these "genome bins"
could then be estimated by the fraction of single copy
genes thought to be essential for life.

The process seems to work pretty well, and MAGs have become incredibly
popular, with well over 10,000 MAGs extracted in the last few years (see
the first paragraph of the spacegraphcats paper for references).

But I suspected that there was more to be done. There are several
shortcomings of MAGs and the binning progress: the main one (for me)
is that generally the binning depends on contigs that come out of DNA
sequence assembly, which is a challenging and fragile process.  I
believed that metagenomes probably contained more sequence and more
sequence *variation* than was represented in the MAGs, and I thought
we were probably underestimating the content of MAGs by ignoring
accessory genome content.  But, while I have reasons for these
opinions, I don't (didn't) have specifics - it is surprisingly difficult to nail
down missing content in complex communities!

So I was really, really interested in taking a look at what was in the
graph neighborhood of these bins. And after some significant
rephrasing of the original sparse graph cuts question by Felix, Mike,
Dominik, and Blair, we realized that a **graph neighborhood search**
function would be directly useful.  The idea would be to reach into
the assembly graph with a set of query k-mers (or reads) and extract
the full set of k-mers proximal (in the graph) to those queries.

What this led to was an implementation of an r-dominating set
algorithm, where a subset of nodes in the compact De Bruijn graph are
chosen such that *every* node in the cDBG is within distance r of one
of these chosen nodes. This forms what is known as a dominating set,
and it provides a kind of clustering over the entire graph.  These
dominating nodes could then be used to define a local neighborhood:
we could go from a k-mer to a cDBG node to its dominator to the
dominated nodes, and retrieve everything that belonged to a dominated
nodes as part of that neighborhood.

Now, defining an r dominating set is NP-hard on large graphs, but
conveniently, Blair's group was interested in and knowledgeable about
efficiently calculating certain properties for graphs of
[bounded expansion](https://en.wikipedia.org/wiki/Bounded_expansion).
Graphs of bounded expansion permit certain optimizations of otherwise
difficult algorithms, and (mirabilis visu) compact De Bruijn graphs
turn out to be just this kind of graph, because each node has at most
8 edges.

In the end, we were able to calculate r-dominating sets in *linear*
time for cDBGs because of this property.  (Again, see the paper for details.)

## Implementation, implementation, implementation ...and real data.

We actually walked out of the barnraising with a functioning dominating
set calculator that we could apply to real data. But we had to build
*a lot* of code infrastructure around this, including -

* code to build a cDBG (since thankfully replaced with BCALM);
* graph indexing that let us go from a k-mer to a cDBG node (we ended up using the bbhash minimal perfect hash function for this);
* graph indexing that let us go from a cDBG node to the set of reads that had contributed k-mers to that node;

...all of which now resides in the spacegraphcats codebase.

The process of building the spacegraphcats program was <ahem> heavily
iterative. I think we went through at least two rewrites of the
dominating set algorithm, which is now the least computationally
intensive part of the whole package.  I spent more than 18 months
trying to get MinHash based search to work, only to essentially prove
that due to the rampant strain variation in real data sets, MinHash
based methods were too insensitive to find graph regions at the
necessary resolution.  (More on this at some other time.)  Overall, I think
we wrote 5-10x as much code as we ended up using in the final paper.

## So what did we find?

The two key biological findings of the paper, in my mind, are these:

1) The graph neighborhoods of metagenome-assembled genomes contain
real content that almost certainly belongs in the bin, but that was
not included in the bin.

2) *One* of the reasons for this content to be missing is that there
is a lot of strain variation present in the neighborhood, and this
prevents assembly (and hence binning). It's hard to estimate the
magnitude of this effect but it's at least 10-20% in the data set we
chose to benchmark with.

We do lots of other stuff in the paper, and it's chock full of interesting
ideas, but those are the two main takeaways for biologists.

(If you're a computer scientist, you _should_ be salivating at the
dominating set algorithm and implementation. But this blog post is for 
biologists :)

## What is particularly neat about the paper?

I think the underlying spacegraphcats algorithm, code, and way of
thinking is powerful and will be enabling in all sorts of unexpected
ways.  But of course I'm not yet sure which parts are going to
actually be useful to others. We chose the binning work for this paper
because it was the part we could most concretely discuss; it is
definitely _not_ the most interesting thing about the spacegraphcats
project overall.

Probably the coolest unexpected thing about *this* paper was how well
the Plass amino acid assembler worked on the neighborhoods. And therein
lies a bit of a story --

You see, we got to the point where everything was *working* in
~February or March of 2018. We could do the genome queries, we could
get the reads from the neighborhood, and... we were kinda stuck there.
If (as we suspected) the reads didn't assemble well due to strain
variation, then what do you do with them? We were thinking of running
different nucleotide assemblers, but it is rare that one assembler
unambiguously outperforms another assembler. And there wasn't much
we could do without an assembler here.

This point bears repeated emphasis. The strong underlying hypothesis was
that *one of the major reasons sequence wasn't being binned was because
it wasn't assembling.* But you can't really do all that much with
100 bp reads _other_ than try to assemble them! And (as we suspected)
the nucleotide assemblers didn't perform all that well on the reads, when
we measured it. What could we do??

## Assembling in amino acid space

So we started hunting around for ways to look at the reads that would
not involve running them through a nucleotide assembler. I'd recently
seen the
[Plass paper](https://www.biorxiv.org/content/early/2018/08/07/386110),
which talked about assembling in amino acid space, and so I decided to
give it a try; in theory, at least, amino acids should be less
affected by nucleotide strain variation, because all of the synonymous
codons would be collapsed.

Somewhat to my surprise, the Plass assembler worked wonderfully well
out of the box, and - in at least a few cases - dramatically increased
the estimated completeness of the bins.  When we looked, we confirmed
that Plass was (as hoped) assembling many more protein sequences.  And
we also saw a surprising amount of amino acid variability in what *was*
being assembled.

But what did it mean? WHAT DID IT MEAN??

## Enter the final author!

Here we asked Taylor Reiter to dig in. Taylor is a graduate student
in my lab who joined the project to help with the biological data
analysis.  She'd been working on assessing the functional content of
the bins since March 2018 or so, and when I threw the Plass assemblies
her way she tore into them.

What she discovered was that even with *ridiculously* stringent error
trimming on the underlying data (a hard k-mer trim of abundance=5 on
all the reads prior to assembly), we were seeing many minor variants
in really highly conserved genes like gyrA. I think we still don't
have a handle on the number and importance of these variants, but at
the nucleotide level there seem to be dozens of variants. And, at
least in a few neighborhoods, there seem to be two or more high
abundance amino acid contigs, suggesting two or more significant strains.

## And that's where we left the paper.

The paper concludes with the observation that there's a lot of unseen
variability in metagenomes, and that they are unseen in part because
of challenges with the tools that we use.  It's not clear how much
biological impact this might have on MAG analysis, e.g. on attempts to
reconstruct metabolic potential, but indications are that it has at
least some.  We're thinking about how to follow up on this concretely.

In the meantime, with this first paper, we have produced a reasonably
robust tool, based on a strong and efficient algorithm, that lets us
systematically look at metagenomes in a way that we basically haven't
been able to do before.  I'm pretty stoked about this, in part because
(as has been my experience with other papers like this) I suspect that
there will be many interesting computational extensions that can be
built on this foundation, by people that are smarter than me about
assembly graphs.  I'm looking forward to it!

--titus
