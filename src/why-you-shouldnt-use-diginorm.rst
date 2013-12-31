Why you shouldn't use digital normalization
###########################################

:author: C\. Titus Brown
:tags: khmer,diginorm
:date: 2013-12-31
:slug: why-you-shouldnt-use-diginorm
:category: science

Over the last year, `digital normalization
<http://ivory.idyll.org/blog/what-is-diginorm.html>`__ has occupied an
increasingly privileged position in sequence analysis: it's a
lightweight way to achieve an assembly, one that is computationally
cheaper than almost anything else you can do; our software works
reasonably well in practice; sequencing data generation capacity is
only increasing; and our papers, my blog, and our twitter presence
have made diginorm pretty visible.

That having been said, there are lots of situations in which diginorm
is not good or useful. I talk to a lot of people about it and many
people seem a bit hesitant to critique it in front of me. Worse, many
people feel pressure to try it. And, worst of all, people don't always
tell me when they run into problems, incorrectly believing that I am
going to be upset at them.

With all that in mind, I thought I'd write a more critical blog post
about diginorm. These are just the problems I've heard about -- if you
have had bad outcomes from using diginorm, I'd love to hear about it,
so please do either comment on this post or `send me an email <mailto:titus@idyll.org>`__.

One caveat: assembly is still a challenging research problem in many
(most?) circumstances. So consumers should default to critical
evaluation of any statements about assembly - both those made by me,
and those made by others. "It's probably more complicated than anyone
thinks" is a great starting point!

1. False: You should always try digital normalization.

If you can achieve an assembly without running diginorm, then there's
no need to run it!

We developed diginorm because we could not run extant assemblers on
our data: the assembler would run out of memory on our transcriptome
and metagenome date sets. This was partly because very few assembler
authors prioritize memory efficiency over specificity, and partly
because the assembly field was less mature than it is now. While there
are still data sets that you can only assemble on commodity computers
by using diginorm and partitioning, new assemblers and new assembly
approaches have been developed that are much less resource
intensive. I'd particularly like to mention probabilistic graphs (as
used in minia), sparse graphs (soapdenovo2), and distributed graphs
(ray).

I therefore recommend diginorm in only three circumstances: first,
when you can't easily complete an assembly because of ram limitations;
second, when repeat structures or polymorphism break assemblers; and
third, when you want to do a quick and dirty initial assembly because
that's all you need.

If you're doing microbial genomes, use spades or mira. If you're
working with metagenomes, use IDBA-UD or Ray. If you're assembling
transcriptomes, use Trinity. If you can run your current datasets with
those assemblers on your current hardware, there is no very good
reason to apply diginorm: it probably will not yield big gains in
assembly quality, and may cause problems. (If that last sentence is a
bit equivocal, it's because we occasionally do see significant gains
in some aspects of assembly after diginorm, but we don't really know
why.)

2. False: Diginorm rarely or never results in worse assemblies.

Diginorm unquestionably results in more fragmented assemblies, and
also forcibly collapses heterozygosity. I've heard that it does
particularly bad things to plant genomes, which are repetitive and
polyploid :). I've also heard that it performs poorly on viral and
phage metagenomes.

We've also heard that it works well on viral and phage metagenomes,
and in some eukaryotic genome assemblies it has been the only thing
that worked. It drives me a little bit crazy that we don't know why it
works well sometimes and poorly other times :). (People who have had
bad experiences would be doing me a huge service by letting me know
about them!)

3. False: Diginorm works well with all assemblers.

There are a number of assemblers that return bad results with
diginormed data. In fact, there are only two assemblers for which
there is a lot of empirical evidence for good performance on
diginormed data: velvet and trinity. I've heard that ALLPATHS performs
much worse on diginormed data than on raw data; I've not heard
anything concrete from most other assemblers, although Mira uses
diginorm-like algorithms internally.

Why might assemblers do especially badly with diginorm data? Two
reasons.

First, assemblers are heavily heuristic: many of the gains in assembly
quality that have been realized over the last few years have come from
better approximate resolutions of tricky situations observed in real
data. Diginorm may modify the signatures of these situations and
result in misapplication of heuristics. One particularly strong signal
in the data is coverage, which diginorm systematically modifies; it's
no big surprise that many assemblers perform badly on whack data.

Second, diginorm breaks the assembly graph at high-copy repeats. This
is a straightforward consequence of the basic coverage downsampling
algorithm, and is one big reason why we are pursuing alternatives to
our current diginorm approach.

In some sense, that diginorm works at all is kind of amazing; that it
breaks some or many assemblers should not be surprising at all.

----

So where does this leave diginorm? Should you even try it?

A few thoughts.

First, diginorm is pretty computationally inexpensive, comparatively
to almost everything else. If you're not getting a good assembly, it
probably won't cost you too much time to try it out - especially on
transcriptomes and metagenomes. (See `the khmer protocols
<http://khmer-protocols.readthedocs.org>`__ for our recommended
pipeline.) But don't expect miracles, and, if you suspect you have a
problem that khmer isn't targeted at solving, maybe try other
solutions first. (Please do feel free to ask, on the `khmer mailing
list <mailto:khmer@lists.idyll.org>`__, whether khmer might help. We
will try to be honest and often suggest other, better tools when we
know of them.)

Second, we love to hear about situations where you tried khmer and
diginorm and got horrible results. Our response might be "oh, did you
try this other set of options?" but we generally won't expect other
people to invest huge amounts of time in solving problems with our
approach -- although of course we're happy to kibitz if you do want to
put in the time. Regardless, in the short term we want to know where,
when, and why our approach sucks, and trying to spare our feelings may
be polite but isn't effective in the long run :).

Third, the field of assembly is still evolving quite fast. Programs,
data types, and algorithms are changing all the time. One thing this
means is that if you are having trouble with a particular data set,
there may well be a solution out there, or it may be possible to adapt
a solution to someone else's problem. So communicate about your
problems!

--titus
