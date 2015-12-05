Arguing for khmer's impact, for an NIH R01 grant proposal
#########################################################

:author: C\. Titus Brown
:tags: khmer,moolah,nih
:date: 2015-06-04
:slug: 2015-khmer-impact
:category: science

I'm starting to work on a grant renewal for khmer, and with *a lot* of
help from the community, including most especially Richard Unna-Smith,
I've put together the following blurb.  Suggestions for things to
rearrange, highlight or omit welcome, as well as suggestions for
things to add.  I can't make it too much longer, though.

----

The primary software product from previous funding is the khmer
software.  khmer provides reference implementations of low-memory
probabilistic k-mer counting with the CountMin Sketch (pmid25062443),
metagenome graph partitioning with probabilistic De Bruijn graphs
(pmid 22847406), lossy compression of large sequencing data sets with
digital normalization (`arXiv <http://arxiv.org/abs/1203.4802>`__),
and streaming error trimming (`PeerJ preprint
<https://peerj.com/preprints/890/>`__).

**Software details** First made available in 2010, khmer now contains
12k lines of C++ code with a 6.6k-line Python wrapper library and test
suite; khmer functionality is exposed at the C++ level, the Python
level, and through the command line.  We have intentionally chosen to
maximize use and reuse by releasing the software early and often,
making preprints available, and lowering barriers to reuse.  In
particular, we make khmer freely available for commercial and
non-commercial use, reuse, modification, and redistribution under the
BSD license.  There are also no IP restrictions on the algorithms
implemented in khmer, so companies have been able to make maximal use
of the software; for example, Illumina directly incorporates the
software in their synthetic long-read pipeline (pmid25188499}.

**Development process and developer community** Our development
process adheres to many good practices, including version control, use
of an issue tracker, maintaining high test coverage ($>$80\%), coding
and test guidelines, a formal code review and contribution process,
and continuous integration (pubmed24415924, `Crusoe and Brown
<files.figshare.com/1194736/wssspe13_ged.pdf>`__).  Our formal release
process (link) tests the khmer software across multiple UNIX
distributions prior to release, and we now have 25 releases.  About 60
people have contributed patches to khmer, and there is an active core
of 5 developers, including one external to our group.  We have a
low-traffic mailing list with 100 subscribers.  The GitHub project has
237 "stars" and 192 forks, placing it in the top 1\% of science
projects on GitHub.

**Documentation, protocols, and recipes** We maintain documentation
for command-line use (link), detailed protocols for integration with
other software (link), and an increasing number of "recipes".  With
Google Analytics, we have seen approximately 10,000 distinct visitors
to these sites within the last 15 months.

**Software use** khmer is widely used by external groups, is
frequently downloaded, and has led to several extensions of the core
algorithms first demonstrated in khmer.  In particular, khmer is
downloaded from the Python Package Index 2-3k times a month, and is
available for install through several UNIX distributions.  Because
khmer is available from many different sites, these are most likely
underestimates.

**Citations** In addition to three publications and N preprints from
our group `(link <http://www.ncbi.nlm.nih.gov/myncbi/collections/48107445/>`__ and citations), and four publications with collaborators (cite), a
literature survey found 26 publications using the software in data
analysis `(link) <http://www.ncbi.nlm.nih.gov/myncbi/browse/collection/48107393/>`__.  Accurate numbers are hard to report because many papers do
not cite computational tools properly, some journals do not allow
preprint or Web site citations, and tool citations are often removed from high
impact-factor citation lists for space reasons; however, searching
Methods sections in open-access biomedical journals (approximately
20\% of the literature) found 26 publications, so we estimate the true
citation count at greater than 100.  Moreover, several pipelines and
workflow engines incorporate khmer, including Illumina TruSeq long
reads (pubmed25188499), DOE KBase, iPlant Collaborative, and
Galaxy, potentially leading to a deflated citation count.

**Scientific usage** khmer has been used for assembling highly
heterozygous genomes, including a number of parasitic nematodes
(e.g. (pmid25730766,24690220,23985341); microbiome analysis, including
both environmental and human/host-associated
(pmid25279917,pmid24632729); mRNAseq de novo assembly
(pmid25758323,pmid24909751); and preprocessing for PacBio error
correction and RNA scaffolding (cite).  (See `(lik)
<http://www.ncbi.nlm.nih.gov/myncbi/browse/collection/48107393/>`__
for a full list of citations.)  Several groups doing large-scale
genomics now incorporate khmer into their pipeline to dramatically
reduce time and memory requirements for assembly; for example, the
Hibberd Lab at Cambridge is using it to reanalyze over 240 deeply
sequenced plant transcriptomes.

**Extensions and reimplementations** In addition to direct use of the
khmer software, several groups have reimplemented and extended
concepts first demonstrated in khmer.  This includes the *in silico*
normalization algorithm included in the Broad Institute's Trinity
package for de novo mRNAseq assembly (pmid23845962); NeatFreq, another
implementation of abundance normalization, released by JCVI
(pmid25407910); bbnorm, developed at JGI `(cite)
<http://seqanswers.com/forums/showthread.php?t=49763>`__; and an
implementation of diginorm in the Mira assembler.  The Minia assembler
(pmid24040893) extends the probabilistic De Bruijn graph approach
first introduced in Pell et al., 2012, and this has been further
extended for cascading Bloom filters (pmid24565280).
