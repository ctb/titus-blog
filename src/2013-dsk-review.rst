A review of DSK: k-mer counting with very low memory usage
##########################################################

:author: C\. Titus Brown
:tags: science,peer review
:date: 2013-01-18
:slug: 2013-dsk-review
:category: science

One of graduate students and I were reviewers on Rizk et al., `DSK:
k-mer counting with very low memory usage
<http://bioinformatics.oxfordjournals.org/content/early/2013/01/16/bioinformatics.btt020.short?buffer_share=64cbf&rss=1>`__,
and I thought I'd share our review.  At the moment I cannot easily
see the entire paper so I have not modified the review to account
for post-review changes; some of our criticisms at the bottom have
probably been fixed.  They weren't big deals anyway so I thought I'd
leave them in.

(The grad student can self-identify if s/he wants to :)

---

The authors describe a fairly simple yet apparently quite efficient
and effective system for counting k-mers.  The problem is a
significant one in bioinformatics, where there are increasingly many
applications reliant on k-mer-based approaches (de Bruijn graph
assembly being one example).  This approach uses fixed (low) memory as
well as disk space to count k-mers.

The basic strategy is to partition k-mer space into multiple partitions,
and then iterate across the sequence multiple times, each time counting a
specific subset of the k-mers.  The partition for each k-mer in that subset
is calculated and the k-mer is appended to an on-disk list for that partition.
After each iteration, the counts for that partition are output. A key point
is to choose the disk space D proportionally to the total size of the
data set v so that it is not a v^2 algorithm.

My graduate student installed the software and ran it through a test
data set successfully, so good job there!

One disadvantage that we can see for more general use is that storing
and retrieving the k-mer counts requires a separate step, unlike in
the Jellyfish or BFcounter applications.

Another problem was that due to the length limitations of the paper,
we were confused by discussion of the tradeoff between D and M with
respect to the data set size.  It seems like the overall approach may
simplify to only one iteration over all the data if D can be chosen to
be big enough.  More importantly, as soon as D is limited, the runtime
starts to become a problem because it becomes an n^2 algorithm.  I
think the paper is quite correct to present the general case of
arbitrary D and M but the most useful case seems to be when n_i = 1.

For the case where the reads file size is used for D, I'm assuming
we're talking about the FASTQ file here?  Not so important to clarify
but we were again confused by this.

So, specifically -- the paper could be improved:

- by emphasizing the case where n_i = 1 earlier in the paper, and simply
  stating that D can be made smaller but (with reference to fig 1) that
  starts to cause problems

- by pointing out that storing the k-mer counts for random access is
  a separate problem, so this is not as generally useful as Jellyfish,
  BFcounter, or Tallymer -- although it may be much improved for specific
  purposes.

but I regard these as minor in the context of the overall advance.

Signed,

C\. Titus Brown, ctb@msu.edu

---
