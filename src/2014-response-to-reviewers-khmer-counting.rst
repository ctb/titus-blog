Response to reviewers for paper, "These are not the k-mers you are looking for"
###############################################################################

:author: C\. Titus Brown
:tags: khmer, k-mer counting, reviews
:date: 2014-05-15
:slug: 2014-response-to-reviewers-khmer-counting
:category: science

A few months back, we `received some reviews
<http://ivory.idyll.org/blog/khmer-counting-reviews.html>`__ for `our
paper on k-mer counting with khmer <http://ivory.idyll.org/blog/2013-khmer-counting-paper.html>`__.  After many months, we (mostly Qingpeng
Zhang, the first author) has finished revising the paper.  Here is our
response to reviewers.

The `latest (resubmitted) version of the paper is here
<http://arxiv.org/abs/1309.2975>`__, while the `version the reviewers
reviewed is here <http://arxiv.org/abs/1309.2975v2>`__.

Note that, according to github history, the revisions required `60 commits
<https://github.com/ged-lab/2013-khmer-counting/compare/submit_round1...submit_round2>`__
starting in mid-January.

Our response to reviewers
~~~~~~~~~~~~~~~~~~~~~~~~~

**We thank the reviewers for their comments, and believe we have addressed all of them.**

Major remarks:

1) The authors performed benchmarks on rather small datasets. For the purposes of comparing different algorithms and evaluating features such as miscounts, this is fine. However, the claim that khmer can analyze production data is not supported. The largest read dataset used in the manuscript is of size 5 GB, which is two orders of magnitude lower than a HiSeq 2500 run. The number of distinct k-mers is also several times lower than in an actual mammalian sequencing experiment, and at least an order of magnitude lower than in metagenomics runs. Therefore, I would recommend the authors to show the results of, at least, a single khmer run on a large (> 100 GB) dataset, either metagenomic or large genome.

    khmer has been used extensively in our hands for very large data sets (300 GB-2 TB of sequencing data), and we have written this up in a separate manuscript, which has just been published at PNAS (www.pnas.org/content/early/2014/03/13/1402564111.abstract).  We have adjusted the discussion to cite this.

2) The Section "Using khmer for digital normalization, a streaming algorithm" has several weaknesses: (i) it is missing a key conclusion, (ii) it explores the topic superficially, ((iii) and (iv)) some statements are unclear ((iii) and (iv)).

    We agree that the section is weak, and have amended it in response (details below).  We are wary of placing too much emphasis on digital normalization, which (while fascinating to us!) is only one of several applications of khmer.

2.i The authors mention that "previous work did not explore the lower bound on memory usage for effective digital normalization.", implying that this work does. However, Tables 4 and 5 report at least 40 MB of memory for the E. coli dataset, which, according to Table 3, has 22e6 distinct k-mers. If my back-of-the-envelope calculation is correct, the whole memory usage is 14 bits per k-mer, which is several times higher than the results of [Pell et al 2011]. Furthermore, Tables 4 and 5 indicate that the normalized datasets at mem=40 MB still appear to be of reasonable quality (only 0.02% drop in coverage). Thus, it is unclear whether 40 MB is a tight lower bound for the memory usage of digital normalization on this dataset.

    We have addressed this by doing a number of new analyses, including adding higher false positive rates and evaluating assemblies with QUAST.  Note that the results from Pell et al are in bits, whereas we are using 8-byte counters for tracking k-mer abundance.

    Note that the Velvet assembler takes considerably more memory than khmerÕs diginorm process for all of these false positive rates, which is a key point.  

2.ii. Digital normalization is a very interesting topic, but it is only superficially treated in this section. Applying it on a tiny E. coli dataset, without reporting statistics of the un-normalized assembly, is unsatisfactory. Also, large/local-misassemblies statistics were not reported, the authors should use the tool QUAST. I recommend that the authors focus on extending the results of Table 4 to guide users towards selecting optimal memory usage for khmer / digital normalization. For instance, it is now clear that for an E. coli dataset one can use khmer with 40 MB of memory (by the way, what was the sketch size?), but how should one set the khmer parameters for larger datasets?

    We have added a section detailing the analytic solution to the question of hash table size, and provided details on hash table sizes.  Note that there is, in practice, no way to know how what the final false positive rate will be without actually performing digital normalization, and it is impossible to estimate precisely or even usefully without consuming the entire data set.  We do provide a guide in our documentation, here: http://khmer.readthedocs.org/en/v1.0/choosing-table-sizes.html

2.iii. The following statement seems false (page 8). "[..] digital normalization can be efficiently implemented as a streaming algorithm in which the majority of k-mers in a data set are never loaded into the counting structure". My understanding of khmer is that it loads all k-mers in the CountMin Sketch.

    The digital normalization algorithm chooses whether to accept or reject a read prior to updating the counts with the reads from the k-mer.  We have amended the text to clarify - thank you!

2.iv. The authors refer to Trinity in-silico normalization as a non-streaming algorithm. However, for their evaluation, they use a three-pass digital normalization, which effectively requires to read the input data three times. So, in effect, both processes are non-streaming.

    We have amended our paper to use a single-pass approach only, which is streaming.

3) Section "Sequencing error profiles can be measured with k-mer abundance profiles" appears to be missing some key content. Figure 7 shows the number of unique k-mers per read position. How does this translate to sequencing error profiles: e.g. percentage of errors per base, or percentage of errors per base at position i, for i less than the read length? Note also that looking at unique k-mers only offers a partial picture of sequencing errors. For instance, when an error is seen in two or more reads, the erroneous k-mers will have abundance > 1.

    PMID 11504945 and 12902383 cover this ground well; we have added citations to the relevant literature.  We have also added results from seqtk and FASTX trimming, showing that k-mer abundance trimming is extremely effective.

Minor remarks:

4) page 2: "Z hash tables are allocated, each with a different size of approximately H bytes" A single variable (H) appears to correspond to Z different sizes. The authors could either use H_1, ..., H_Z, and/or explain why the hash tables need to have different sizes, while they are all close to a single size H.

    Thank you -- this text has been updated to clarify!
	 	 	
5) Perhaps the citations [15] and [17] could be updated, now that theyÕve been published in resp. NAR and Bioinformatics.

    Done, thanks!

6) page 4: Section title "khmer counts k-mers efficiently" is misleading, as it deals only with accessing existing k-mer counts. How about replacing it by "khmer accesses k-mer counts efficiently?" The performance of khmer is impressive in that section, nonetheless.

    Done, thanks!

7) The labels of x- and y- axes of Figures 5 and 6 are unclear. Why is the meaning of "offset > 0" in the x-axis? Also, the caption and main text both use the term "miscount" but the axes refer to "offsets".

    Updated to use "miscount" consistently throughout.  Thanks!

8) It would be good to show how abundance-based read trimming differs from classical quality-based trimming methods. Could you run, e.g. seqtk, and report how many bases were trimmed?

    We have added this to our analysis.  We were surprised by the results!  We are wary of focusing too much on this in the paper, since khmer only provides a suite of tools, and the performance of these tools on real data will depend on details of that data.

9) The caption of Table 5 reads "We assembled digitally normalized reads using 3-pass digital normalization". Perhaps the author meant that the reads were digitally normalized using the 3-pass method, then assembled using Velvet?

    Thank you, fixed!

10) Although the authors did a convincing job at comparing Khmer with other methods, it would still be interesting to see a comparison with KMC and Turtle.

     We agree!  We have added this information to the graphs and discussion.  We also added KAnalyze and updated the version of BFCounter used.

11) This is a software-related remark. I wanted to test khmer on my machine (Linux SL 6.2), on the cluster of my institution (Linux RHEL5) or a dedicated server (Linux Centos 6.4). But all these systems ship with Python 2.6 and cannot be easily upgraded to Python 2.7 by running a single command. Is there another way, if so, could you put it in khmer docs? This might be a small technical detail but it could potentially limit other end-users, especially those who do not have root access on their machine.

     We have amended the online docs to specify install instructions for Redhat systems.  khmer works on Python 2.6 (we checked! -- please see https://github.com/ged-lab/khmer/issues/94 if you're interested) although we do not officially support 2.6.

12) It should be noted that all the formulas providing estimations of collision rates in the CountMin Sketch are approximations, also they rely on hash function assumptions that are not necessarily met in the implementation (although, in practice, most hash functions work well).

     We have updated the text appropriately.  Thanks!
				
			
Reviewer #1 corrections:

pg1, line -8:
"reads increases the total number", comma missing between reads and increases. ideally you should rephrase the sentence or split up into two parts.

    Fixed, thank you!

pg1, line -4,
BFCounter does not have a dash, repeated throughout the manuscript

    Fixed, thank you!

pg 2, line 5
Sentence starts with "And", remove or fix.

    Fixed, thank you!

pg 4, line 7 in 2nd para
Melsted et al., the reference has only two authors, should be Melsted and Pritchard depending on the reference style used.

    Fixed, thank you!

pg 4, line 2 in 5th para
"simulated k-mers", this is a bit ambiguous, you mean the randomly generated k-mers, and not simulated reads from a genome, right?

    Fixed, thank you!

pg 4, line 6
"constant in retrieval time", Tallymer should be log and Jellyfish constant in retrieval time (if you discard the loading time), also "independent of the size of the database" would be clearer here.

    Thank you, fixed!

Reviewer #1: Major edits.

Deterministic lower bound.
The guarantees on the counts are stated on page 3, i.e. the probability of the count being wrong. Later in the paper the authors note that the reported answer can never be lower than the true value. I think it would be good to move this discussion to the first section of the results, since this is an important property needed later on. It would also be good to indicate why this is the case.

    We updated the text as suggested; thank you!

CountMin Sketch vs. Counting Bloom filter
The authors describe their implementation as a CountMin Sketch, but it could also be described as a Counting Bloom filter. I believe CBF would be more appropriate given the usage here. CMS was designed and analyzed for streaming algorithms to detect heavy hitters, the bounds on the errors were derived assuming you had multiple collisions and the amount of memory used was independent of the input size (i.e. streaming algorithm). CBF predates CMS and a lot more work has been done on extending this work which would be beneficial to the implementation. I have no issue with the authors picking one name over the other, but they should add a section discussing the use of both terms and cite appropriate literature. Additionally the error analysis on CBF has been more widely studied compared to CMS.

    The counting Bloom filter and CM Sketch is similar in concept, but has significant differences. Initially counting Bloom filter is an expansion of standard Bloom filter that can allow deletions. So it is still more focused on sets and membership testing, although it does have the ability to maintain counts of items approximately.One of the most important analysis from CBF reveals that 4 bits per counter should be enough for most applications. This does not apply to our k-mer counting scenario with many high abundant k-mers. CM Sketch is more concerned with multisets rather than sets. The discussion of counting error rate in our paper,especially the performance for skewness data sets is inspired from the CM Sketch paper. So in our paper, we mainly use the term CM Sketch rather than CBF. We also noticed that there are other varieties of Bloom filter that is related to CM Sketch and the implementation of khmer. Estan and Varghese's Multi-stage filters is more focused on detecting heavy hitters.Cohen and Matias's spectral Bloom filters have more optimizations like minimal increase and dealing with unique minimum count to reduce the possibility of counting error. We discuss this issue briefly and cite these methods in our manuscript as suggested. Thank you!

Usage of streaming and online. 
The algorithm described for counting k-mers is an online algorithm, i.e. we can query the counts at any time given the data we have seen so far. Streaming algorithms impose an additional restriction, in the sense that they require memory that is sublinear in the size of the input. How we measure the size of the input might depend on applications, but the number of reads or the number of distinct k-mers might be reasonable. In any case no general counting algorithm can do better than linear in this sense, so there are no streaming algorithms for counting. The authors use "streaming" and "online" interchangeably throughout the paper, e.g. DSK is not a streaming algorithm, etc. The exception is digital normalization, which could be classified as streaming, although there is no formal analysis, in this case the size of the k-mer count data structure would need to be sublinear (in which case any online data structure would do). The authors should fix this and use the proper terms where appropriate.

    We have updated the text as suggested - thank you! Note that the DSK authors use "streaming" in their paper.

Parallel speedup.
Both Jellyfish and khmer are run in parallel mode, using many cores simultaneously. From the scripts one can see that 8 threads were used for both programs. What I would like to see is how well khmer scales with multiple cores, i.e. run with 1,2,4,8, .. threads, up to the number of cores and see how much speedup is gained. Granted it will not be linear because of I/O overhead, but it would be nice to see that throwing more cores at the problem helps. 

    We have added an explicit reference to our book chapter describing the scaling properties of khmer (McDonald and Brown, Performance of Open Source Applications, ISBN 1304488780).

Fixed memory
pg 6, paragraph 5
The authors claim that the memory usage is fixed, but compared to what. Generally with streaming algorithms we fix the error rate and probability of failure and in this case fixed means independent of the size of the input (or logarithmic). In this setting if we fix the error rate, the memory usage will be linear in the size of the input. Although one can argue that the constants are much better, and this is really important in practice, this does not imply "fixed memory usage". Please fix this issue (no pun intended).

    The text has been adjusted to clarify.  Thanks!

pg 6, line 4-5 (Disclaimer, I am the author of BFCounter and therefore biased)
"Note that ...", this is no longer true, the previous implementation was single threaded and [8] compared single threaded to multithreaded. The current version on https://github.com/pmelsted/BFCounter is multithreaded and competitive in speed. I ran comparisons with Jellyfish on 1,4, and 8 threads and it achieves similar speedups on the same data sets used in the papers.

Command lines used for running BFCounter::

   BFCounter count -k 22 -n 360000000 -t 8 -c 100000 -o iowa.1 -b 4 iowa_prairie_0920.fastq.1
   BFCounter dump -k 22 -i iowa.1 -o iowa.1.txt

.

   Thank you! We have updated our text and figures.

Parameter selection
The memory usage of both khmer and Jellyfish is dependent on the estimated number of k-mers present. For the file iowa_prairie_0920.fa.1, Jellyfish was run with -s 701472602, i.e. 700M 22-mers, whereas khmer was run with --hashsize 1476277798 (1400M) k-mers. Given that there are approx 500M distinct 22-mers in the file how were the parameters selected. The authors describe finding the -s parameter for jellyfish that keeps everything in memory (the table sizes are powers of two), but how was the parameter chosen for khmer?

    The target hash table size and number (H and N) were determined by the desired false positive rate (see false positive rate equations) and then the first N prime numbers larger than H were chosen to create the hash tables.  (These are calculated automatically by khmer.)  We have updated the text to provide an analytic solution to the question of optimal memory usage when the total number of k-mers is known.

Minor edits:

pg1, line -8:
"reads increases the total number", comma missing between reads and increases. ideally you should rephrase the sentence or split up into two parts.

    Fixed, thank you!

pg1, line -4,
BFCounter does not have a dash, repeated throughout the manuscript

    Fixed, thanks!

pg 2, line 5
Sentence starts with "And", remove or fix.

    Fixed, thanks!

pg 4, lines 3-4
"Here .. outperforming jellyfish", looking at the graph this is not supported, it seems that khmer is much faster.
				
    Adjusted in light of the actual data...

pg 3, line -9
it should be noted that khmer's memory usage is not dependent on k because the kmers are stored implicitly in the data structure. Also the total number of k-mers from error reads grows with k (up to half the read length) so that affects the memory usage as well (although equally for all software).

    We have adjusted the text appropriately, thank you!

pg 4, line 7 in 2nd para
Melsted et al., the reference has only two authors, should be Melsted and Pritchard depending on the reference style used.

    Fixed, thank you!

pg 4, line 2 in 5th para
"simulated k-mers", this is a bit ambiguous, you mean the randomly generated k-mers, and not simulated reads from a genome, right?

    Fixed, thanks!
