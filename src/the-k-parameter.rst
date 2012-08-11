What does k control in de Bruijn graph assemblers?
##################################################

:author: C\. Titus Brown
:tags: assembly,metagenomics
:date: 2012-08-09
:slug: the-k-parameter
:category: science

I'm at the MBL STAMPS course, "Strategies and Techniques for Analyzing
Microbial Population Structure," and one of the things I needed to
address in my morning talk was the role that the k parameter plays in
de Bruijn graph assemblers.

In most de Bruijn assemblers that I have used -- Velvet, Oases, ABySS,
SOAPdenovo, MetaVelvet, MetaIDBA -- there is a parameter k that is under
the control of the user.  (Trinity is one of the exceptions -- it
sets k for you.  Remember, the Broad Center knows best. ;) Students never
know how to set it, and in fact for metagenomes and transcriptomes it
turns out to be a problematic parameter to set: you get different, but
valid, results for different k parameters.

This parameter, sometimes referred to as the overlap parameter, plays a
key role in de Bruijn graph assembly.  De Bruijn graphs are composed
of k-mers as nodes and overlaps between k-mers as edges -- for example,
the two sentences ::

   the_quick_brown_fox_jumps
   jumps_over_the_lazy_dog

can be decomposed into a bunch of fixed length subsequences, or k-mers,
like so ::

   the_q -> he_qu -> e_qui -> _quic -> quick -> uick_ -> ick_b -> ck_br

and if you put both sentences into the same graph, then you could just
follow the links in the graph to spell out the 'assembled' sentence, ::

   the_quick_brown_fox_jumps_over_the_lazy_dog

Here, k is 5: the word size that can connect fragments, aka the
overlap parameter, is 5.  If you increased k to six for the two
sentences above, you wouldn't be able to assemble the sentences:
there's no 6-mer word that is in common between the sentence
fragments.  If, on the other hand, you decreased k to four, you'd find
that you'd made the graph more complicated: the word the\_ actually
appears twice in the fragments above, and you wouldn't necessarily
know how to connect the fragments.

This is an enchantingly simple picture of what k is, and apart from
questions about why on earth you'd take sentences and break them up
into shorter sentences (computational efficiency!), it's what people
will tell you when they hand wave about assembly: k is a measure of
specificity.  (You can even read about it in `the Oases transcriptome
paper
<http://bioinformatics.oxfordjournals.org/content/28/8/1086.long>`__.)
The longer the k, the less tangled your assembly graph is, and the
more specific your assembly is!

This explanation has always bugged me, ever since my student Likit
Preeyanon pointed out to me that Oases yielded quite different results
for different values of k.  Some transcripts -- the lower abundance
ones, generally -- assemble out at lower k.  Others -- higher
abundance -- assemble out at higher k.  To get a complete
picture of the transcriptome with Oases, you needed to assemble at
multiple k values and then do a post-assembly merge, which is fraught
with difficulties.  We see the same thing with metagenomics, incidentally:
you get perfectly valid sequences assembling out at low k and high k,
and our own metagenomic assembly protocol includes a post-assembly merge
with minimus2.

Why does the explanation bug me, you say?  Initially because our
results didn't make any sense: if the graph got *more* specific with
longer k, you would expect assembly at a higher k to yield a subset of
the assemblies done at a lower k.  Conversely, if the more tangled
assembly graph at lower k confused the assembler, you'd expect the
higher k assemblies to include the lower k assemblies.  Instead you
simply get overlapping but different results!

Then we started to work on our `low-memory metagenome partitioning
<pnas.org/content/early/2012/07/25/1121464109.abstract>`__ for
metagenomes, and I noticed something REALLY weird.  We were
partitioning graphs at a k of 32.  Now, a key aspect of de Bruijn
graphs is that the graph at a k of 32 *includes* all the connections
in the graph at a k of 33 -- every overlap is 33 is also an overlap of
32, 31, 30, etc.  So we thought we were being really clever when we
partitioned, 'cause we knew that if we partitioned at k=32 the
partitioned assemblies at k >= 32 would all be perfectly identical to
what we got with the unpartitioned assemblies at k >= 32.  And `that
was true <pnas.org/content/early/2012/07/25/1121464109.abstract>`__.
What confused us was that we got even *better* assemblies when we
partitioned at a k of 32 and then assembled at lower k, like k=20.

What?

Yeah.  When we broke links in the graph at a high k, we could still
get good assemblies at a lower k.  This was prima facie evidence
that the Velvet assembler was doing something more with k than
merely using it to guide connections.

So this is the conundrum: what's going on with k?

Here's at least part of the answer: k is *also* tied to coverage.

.. image:: http://ivory.idyll.org/permanent/multi-k-coverage.png
   :width: 60%

This is a graph of k-mer abundance histograms at several different k
values, for a genome-style data set (the same kind of simulated
data set we used in the `digital normalization
<http://ged.msu.edu/papers/2012-diginorm/>`__ paper).  The light blue
line is mapping-based coverage estimation, using bowtie; it
approximate the true coverage of this data set, which is 200x.
The other three distributions are k-mer abundance distributions at
three different k values (k=32, k=26, and k=20).  

What you can see from this graph is that the longer k values lead to
lower effective coverage peaks.  Or, to put it another way, to achieve
the same k-mer coverage peak, as you increase k you also have to
increase your sequencing depth.  This makes sense from the k-mer
perspective: longer k-mers are inherently rarer (that's what "more
specific" really means, above!) and the longer the k-mer the more
likely it is that it includes an error.

This observation *also* fits the results we got with Oases, that
larger k values bias your results towards more abundant isoforms,
while lower k values pick up lower abundance isoforms.  It *doesn't*
directly explain why the high-abundance isoforms don't get assembled
as well with low k values; my guess is that it has to do with errors.
The shorter the k is the more likely it is that you get distracted
by side paths in the assembly -- again, in the end, specificity.

In summary, I think the choice of k represents a tug-of-war between
specificity and coverage.  Longer k values give you a graph with fewer
high-coverage erroneous paths, but also lower coverage over all;
shorter k values give you a high coverage graph, at the cost of a
more complex graph.  The assembler chooses from the available
paths based on a combination of average coverage and path complexity.
Some assemblers embed heuristics that depend quite a bit on k;
other assemblers, like Trinity, fix k and tune their heuristics
to that specific k.

If this was already entirely obvious to everyone, I apologize for the
long blog post :).

--titus
