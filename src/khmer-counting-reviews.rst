Reviews for paper, "These are not the k-mers you are looking for"
#################################################################

:author: C\. Titus Brown
:tags: khmer, k-mer counting, ngs, reviews
:date: 2014-02-01
:slug: khmer-counting-reviews
:category: science

A few months back, we submitted a paper, `These are not the k-mers you
are looking for: efficient online k-mer counting using a probabilistic
data structure
<ivory.idyll.org/blog/2013-khmer-counting-paper.html>`__, to PLoS One.
We got the (signed) reviews back in December, and I asked the reviewers
if I could post their reviews publicly.  They said yes!  So here they are.

The editorial decision was "revise", so we are in the process of
revising (almost done, in fact :).  I will also post our responses.

----

Reviewer's Responses to Questions

Comments to the Author

1. Is the manuscript technically sound, and do the data support the conclusions?

*The manuscript must describe a technically sound piece of scientific
research with data that supports the conclusions. Experiments must
have been conducted rigorously, with appropriate controls,
replication, and sample sizes. The conclusions must be drawn
appropriately based on the data presented.*

Reviewer #1: Yes

Reviewer #2: Partly

________________________________

Please explain (optional).

Reviewer #1: Counting k-mers is an important problem in
bioinformatics, whith several applications. This paper describes an
implementation for counting k-mers in an online fashion with
probabilistic guarantees on the counts. The motivation of developing
such an applications as well as the memory, speed, accuracy tradeoffs
are well handled.

Reviewer #2: The authors describe a probabilistic k-mer counting
algorithm and implementation that performs well in IO-limited and
memory-limited architectures. Their idea is innovative, it has already
been adopted and extended by several other authors (while the
manuscript was in pre-publication). In this manuscript, the authors
apply khmer to two data analysis cases: read trimming and digital
normalization. The application of khmer to read trimming appears to be
a good idea, because of the one-sided trimming errors, high-abundance
data is always retained. Figures 6 and 7 provide an interesting
analysis of these one-sided errors. I found the section regarding
digital normalization to be superficial, although the topic itself is
quite promising. The article is well-written, and apart from specific
remarks formulated below, the conclusions are well-supported by data.
Also, it should be noted that this research is exceptionally
well-reproducible, as the authors provide an extensive tutorial for
re-creating all the figures on publicly available machines.

Major remarks:

1) The authors performed benchmarks on rather small datasets. For the
purposes of comparing different algorithms and evaluating features
such as miscounts, this is fine. However, the claim that khmer can
analyze production data is not supported. The largest read dataset
used in the manuscript is of size 5 GB, which is two orders of
magnitude lower than a HiSeq 2500 run. The number of distinct k-mers
is also several times lower than in an actual mammalian sequencing
experiment, and at least an order of magnitude lower than in
metagenomics runs. Therefore, I would recommend the authors to show
the results of, at least, a single khmer run on a large (> 100 GB)
dataset, either metagenomic or large genome.

2) The Section “Using khmer for digital normalization, a streaming
algorithm” has several weaknesses: (i) it is missing a key conclusion,
(ii) it explores the topic superficially, ((iii) and (iv)) some
statements are unclear ((iii) and (iv)).

(i) The authors mention that “previous work did not explore the lower
bound on memory usage for effective digital normalization.”, implying
that this work does. However, Tables 4 and 5 report at least 40 MB of
memory for the E. coli dataset, which, according to Table 3, has 22e6
distinct k-mers. If my back-of-the-envelope calculation is correct,
the whole memory usage is 14 bits per k-mer, which is several times
higher than the results of [Pell et al 2011]. Furthermore, Tables 4
and 5 indicate that the normalized datasets at mem=40 MB still appear
to be of reasonable quality (only 0.02% drop in coverage). Thus, it is
unclear whether 40 MB is a tight lower bound for the memory usage of
digital normalization on this dataset.

(ii) Digital normalization is a very interesting topic, but it is only
superficially treated in this section. Applying it on a tiny E. coli
dataset, without reporting statistics of the un-normalized assembly,
is unsatisfactory. Also, large/local-misassemblies statistics were not
reported, the authors should use the tool QUAST. I recommend that the
authors focus on extending the results of Table 4 to guide users
towards selecting optimal memory usage for khmer / digital
normalization. For instance, it is now clear that for an E. coli
dataset one can use khmer with 40 MB of memory (by the way, what was
the sketch size?), but how should one set the khmer parameters for
larger datasets?

(iii) The following statement seems false (page 8). “[..] digital
normalization can be efficiently implemented as a streaming algorithm
in which the majority of k-mers in a data set are never loaded into
the counting structure”. My understanding of khmer is that it loads
all k-mers in the CountMin Sketch.

(iv) The authors refer to Trinity in-silico normalization as a
non-streaming algorithm. However, for their evaluation, they use a
three-pass digital normalization, which effectively requires to read
the input data three times. So, in effect, both processes are
non-streaming.

3) Section “Sequencing error profiles can be measured with k-mer
abundance profiles” appears to be missing some key content. Figure 7
shows the number of unique k-mers per read position. How does this
translate to sequencing error profiles: e.g. percentage of errors per
base, or percentage of errors per base at position i, for i less than
the read length? Note also that looking at unique k-mers only offers a
partial picture of sequencing errors. For instance, when an error is
seen in two or more reads, the erroneous k-mers will have abundance >
1.

Minor remarks:

4) page 2: “Z hash tables are allocated, each with a different size of
approximately H bytes” A single variable (H) appears to correspond to
Z different sizes. The authors could either use H_1, ..., H_Z, and/or
explain why the hash tables need to have different sizes, while they
are all close to a single size H.

5) Perhaps the citations [15] and [17] could be updated, now that
they’ve been published in resp. NAR and Bioinformatics.

6) page 4: Section title “khmer counts k-mers efficiently” is
misleading, as it deals only with accessing existing k-mer counts. How
about replacing it by “khmer accesses k-mer counts efficiently”? The
performance of khmer is impressive in that section, nonetheless.

7) The labels of x- and y- axes of Figures 5 and 6 are unclear. Why is
the meaning of “offset > 0” in the x-axis? Also, the caption and main
text both use the term “miscount” but the axes refer to “offsets”.

8) It would be good to show how abundance-based read trimming differs
from classical quality-based trimming methods. Could you run, e.g.
seqtk, and report how many bases were trimmed?

9) The caption of Table 5 reads “We assembled digitally normalized
reads using 3-pass digital normalization“. Perhaps the author meant
that the reads were digitally normalized using the 3-pass method, then
assembled using Velvet?

10) Although the authors did a convincing job at comparing Khmer with
other methods, it would still be interesting to see a comparison with
KMC and Turtle.

11) This is a software-related remark. I wanted to test khmer on my
machine (Linux SL 6.2), on the cluster of my institution (Linux RHEL5)
or a dedicated server (Linux Centos 6.4). But all these systems ship
with Python 2.6 and cannot be easily upgraded to Python 2.7 by running
a single command. Is there another way, if so, could you put it in
khmer docs? This might be a small technical detail but it could
potentially limit other end-users, especially those who do not have
root access on their machine.

12) It should be noted that all the formulas providing estimations of
collision rates in the CountMin Sketch are approximations, also they
rely on hash function assumptions that are not necessarily met in the
implementation (although, in practice, most hash functions work well).

________________________________

2. Has the statistical analysis been performed appropriately and rigorously?

Reviewer #1: Yes

Reviewer #2: N/A

________________________________

Please explain (optional).

Reviewer #1: (No Response)

Reviewer #2: (No Response)

________________________________

3. Does the manuscript adhere to standards in this field for data availability?

*Authors must follow field-specific standards for data deposition in
publicly available resources and should include accession numbers in
the manuscript when relevant. The manuscript should explain what steps
have been taken to make data available, particularly in cases where
the data cannot be publicly deposited.*

Reviewer #1: Yes

Reviewer #2: Yes

________________________________

Please explain (optional).

Reviewer #1: (No Response)

Reviewer #2: (No Response)

________________________________

4. Is the manuscript presented in an intelligible fashion and written
in standard English?

*PLOS ONE does not copyedit accepted manuscripts, so the language in
submitted articles must be clear, correct, and unambiguous. Any
typographical or grammatical errors should be corrected at revision,
so please note any specific errors below.*

Reviewer #1: Yes

Reviewer #2: Yes

________________________________

Please explain (optional).

Reviewer #1: pg1, line -8:
"reads increases the total number", comma missing between reads and
increases. ideally you should rephrase the sentence or split up into
two parts.

pg1, line -4,
BFCounter does not have a dash, repeated throughout the manuscript

pg 2, line 5
Sentence starts with "And", remove or fix.

pg 4, line 7 in 2nd para
Melsted et al., the reference has only two authors, should be Melsted
and Pritchard depending on the reference style used.

pg 4, line 2 in 5th para
"simulated k-mers", this is a bit ambiguous, you mean the randomly
generated k-mers, and not simulated reads from a genome, right?

pg 4, line 6
"constant in retrieval time", Tallymer should be log and Jellyfish
constant in retreival time (if you discard the loading time), also
"independent of the size of the database" would be clearer here.

Reviewer #2: (No Response)

________________________________

5. Additional Comments to the Author (optional)

*Please offer any additional comments here, including concerns about
dual publication or research or publication ethics.*

Reviewer #1: Major edits.

Deterministic lower bound.
The guarantees on the counts are stated on page 3, i.e. the
probability of the count being wrong. Later in the paper the authors
note that the reported answer can never be lower than the true value.
I think it would be good to move this discussion to the first section
of the results, since this is an important property needed later on.
It would also be good to indicate why this is the case.

CountMin Sketch vs. Counting Bloom filter
The authors describe their implementation as a CountMin Sketch, but it
could also be described as a Counting Bloom filter. I believe CBF
would be more appropriate given the usage here. CMS was designed and
analyzed for streaming algorithms to detect heavy hitters, the bounds
on the errors were derived assuming you had multiple collisions and
the amount of memory used was independent of the input size (i.e.
streaming algorithm). CBF predates CMS and a lot more work has been
done on extending this work which would be beneficial to the
implementation. I have no issue with the authors picking one name over
the other, but they should add a section discussing the use of both
terms and cite appropriate literature. Additionallky the error
analysis on CBF has been more widely studied compared to CMS.


Usage of streaming and online.
The algorithm described for counting k-mers is an online algorithm,
i.e. we can query the counts at any time given the data we have seen
so far. Streaming algorithms impose an additional restriction, in the
sense that they require memory that is sublinear in the size of the
input. How we measure the size of the input might depend on
applications, but the number of reads or the number of distinct k-mers
might be reasonable. In any case no general counting algorithm can do
better than linear in this sense, so there are no streaming algorithms
for counting. The authors use "streaming" and "online" interchangeably
throughout the paper, e.g. DSK is not a streaming algorithm, etc. The
exception is digital normalization, which could be classified as
streaming, although there is no formal analysis, in this case the size
of the k-mer count data structure would need to be sublinear (in which
case any online data structure would do). The authors should fix this
and use the proper terms where appropriate.

Parallel speedup.
Both Jellyfish and khmer are run in parallel mode, using many cores
simultaneously. From the scripts one can see that 8 threads were used
for both programs. What I would like to see is how well khmer scales
with multiple cores, i.e. run with 1,2,4,8, .. threads, up to the
number of cores and see how much speedup is gained. Granted it will
not be linear because of I/O overhead, but it would be nice to see
that throwing more cores at the problem helps.

Fixed memory
pg 6, paragraph 5
The authors claim that the memory usage is fixed, but compared to
what. Generally with streaming algorithms we fix the error rate and
probability of failure and in this case fixed means independent of the
size of the input (or logarithmic). In this setting if we fix the
error rate, the memory usage will be linear in the size of the input.
Although one can argue that the constants are much better, and this is
really important in practice, this does not imply "fixed memory
usage". Please fix this issue (no pun intended).

pg 6, line 4-5
"Note that ...", this is no longer true, the previous implementation
was single threaded and [8] compared single threaded to multithreaded.
The current version on https://github.com/pmelsted/BFCounter is
multithreaded and competitive in speed. I ran comparisons with
Jellyfish on 1,4, and 8 threads and it achieves similar speedups on
the same data sets used in the papers

Command lines used for running BFCounter::

   BFCounter count -k 22 -n 360000000 -t 8 -c 100000 -o iowa.1 -b 4 iowa_prairie_0920.fastq.1
   BFCounter dump -k 22 -i iowa.1 -o iowa.1.txt

Parameter selection:

The memory usage of both khmer and Jellyfish is dependent on the
estimated number of k-mers present. For the file
iowa_prairie_0920.fa.1, Jellyfish was run with -s 701472602, i.e. 700M
22-mers, whereas khmer was run with --hashsize 1476277798 (1400M)
k-mers. Given that there are approx 500M distinct 22-mers in the file
how were the parameters selected. The authors describe finding the -s
parameter for jellyfish that keeps everything in memory (the table
sizes are powers of two), but how was the parameter chosen for khmer?

minor edits
pg1, line -8:
"reads increases the total number", comma missing between reads and
increases. ideally you should rephrase the sentence or split up into
two parts.

pg1, line -4,
BFCounter does not have a dash, repeated throughout the manuscript

pg 2, line 5
Sentence starts with "And", remove or fix.

pg 4, lines 3-4
"Here .. outperforming jellyfish", looking at the graph this is not
supported, it seems that khmer is much faster.

pg 3, line -9
it should be noted that khmer's memory usage is not dependent on k
because the kmers are stored implicitly in the data structure. Also
the total number of k-mers from error reads grows with k (up to half
the read length) so that affects the memory usage as well (although
equally for all software).

pg 4, line 7 in 2nd para
Melsted et al., the reference has only two authors, should be Melsted
and Pritchard depending on the reference style used.

pg 4, line 2 in 5th para
"simulated k-mers", this is a bit ambiguous, you mean the randomly
generated k-mers, and not simulated reads from a genome, right?

pg 4, line 6
"constant in retrieval time", Tallymer should be log and Jellyfish
constant in retreival time (if you discard the loading time), also
"independent of the size of the database" would be clearer here.

Reviewer #2: (No Response)