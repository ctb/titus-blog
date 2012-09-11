A blog post to accompany my XLDB-2012 talk
##########################################

:author: C\. Titus Brown
:tags: physics,biology
:date: 2012-09-10
:slug: xldb-2012-talk-links
:category: science

I'm giving a talk at `XLDB 2012
<http://www-conf.slac.stanford.edu/xldb2012/>`__ tomorrow, and I
thought I'd post a bunch of accompanying links and discussion,
since this audience is pretty far away from my normal audience ;).

Here's the talk itself, on slideshare: `Streaming and Compression
Approaches for Terascale Biological Sequence Data Analysis
<http://www.slideshare.net/c.titus.brown/2012-xldb-talk>`__

**Acknowledgements** (slide 3)

The work I'm talking about today was done by a collection of people in
the lab that includes Adina Howe, a postdoc; Jason Pell, a graduate
student; Arend Hintze, a former postdoc; Rosangela Canino-Koning, a
former graduate student; Qingpeng Zhang, a graduate student; and Tim
Brom, a former graduate student.  Much of the metagenomics work was
driven by Adina, and the compressible graph representation work was
primarily done by Jason.  Qingpeng and Tim work(ed) on k-mer counting
and digital normalization, among many other things.

The data I'm talking about was generated as part of the Great Prairie
Grand Challenge project; the collaborators responsible for the data
generation are Jim Tiedje, Janet Jansson, and Susannah Tringe.  The
sequencing was done by JGI.  My funding comes from the USDA for
sequence analysis tools, a small NSF grant for metagenomics work, and
the `BEACON NSF Center for the study of evolution in action
<http://beacon-center.org>`__.

**Open Science** (slide 5)

Our code is at github.com/ged-lab/.

You're at my blog :).

I'm `ctitusbrown on Twitter <http://twitter.com/ctitusbrown>`__.

I've posted a number of grants and pubs on the lab Web site
at http://ged.msu.edu/interests.html

Our PNAS paper on probabilistic de Bruijn graphs is `Pell et al, 2012
<http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__.

Our digital normalization paper is `available through arXiv
<http://arxiv.org/abs/1203.4802>`__.

You can see a longer, more technical version of this talk from a
presentation at U. Arizona
`over at slideshare <http://www.slideshare.net/c.titus.brown/2012-talk-to-cse-department-at-u-arizona>`__, and when I gave the same basic talk at
MSU last week, they recorded it and `I put it on YouTube <http://www.youtube.com/watch?v=LDty2uFh6Mo&t=1m38s>`__.

**Soil is full of uncultured microbes** (slides 6 and 7)

This is observed by many people; `Gans et al. (Science, 2005)
<http://www.sciencemag.org.proxy2.cl.msu.edu/content/309/5739/1387.full>`__
used DNA reassociation kinetics to estimate that soil contained
upwards of a million distinct genomes.  `Fierer and Jackson (PNAS,
2006) <http://www.pnas.org/content/103/3/626.full>`__ talk about the
biogeography of soil -- what environments, where, are how diverse? --
and there are several other papers worth reading, including
`Dunbar et al. (AEM, 2002) <http://aem.asm.org/content/68/6/3035.abstract?ijkey=813d27c5c83ff93997014e459bfc28d4611c9aec&keytype2=tf_ipsecsha>`__ and
`Tringe et al. (Science, 2005) <http://www.sciencemag.org/content/308/5721/554.abstract?ijkey=7d7da4901fd3478be10bcaf514aa31568b36fdbf&keytype2=tf_ipsecsha>`__.

The "collector's curve" on slide 6 shows the increase in the number of
"Operational Taxonomic Units", or OTUs -- a species analog, but for
uncultured critters -- as you sequence the 16s marker gene more and
more deeply from mixed soil communities.  If this graph showed
saturation it would imply that diversity was capped at that point on
the y axis.  (It's not.)

**Shotgun metagenomics and assembly** (slides 8-13)

Shotgun sequencing and assembly of uncultured microbes is one of the
things I work on.  `Miller et al. (Genomics, 2010)
<http://www.ncbi.nlm.nih.gov/pubmed/20211242>`__ is one of the best
papers I've seen for explaining assembly with de Bruijn graphs.

`Conway and Bromage (Bioinformatics, 2011) <http://www.ncbi.nlm.nih.gov/pubmed?term=21245053>`__ is the reference I use to point out that errors in
sequencing cause de Bruijn graph size to increase linearly with sequencing
depth.

**Sequencing is becoming Big Data** (slide 14)

The infamous `sequencing costs
<http://www.genome.gov/sequencingcosts/>`__ slide shows that
sequencing capacity has been growing faster than Moore's Law for the
last few years.  The point I like to make in connection with this is
that this data generation capacity now extends to many very small labs
-- these sequencers are neither that expensive nor that tricky to
operate -- so many small labs are now generating vast quantities of
data.

I wrote a blog post pointing out that when your data generation
capacity is scaling faster than Moore's Law, `cloud computing is not
the long-term solution
<http://ivory.idyll.org/blog/cloud-not-the-solution.html>`__ -- you
need better algorithms.

**Soil sequencing is particularly obnoxious** (slide 15)

It's a straightforward calculation to go from robustly observing
species at a 1-in-a-million dilution to pointing out that shotgun
sequencing of those 1-in-a-million critters will require about
50 terabases of sequencing:

   If you assume each microbial genome is 5 mb, and you need to randomly sample
   each genome to (at least) 10x for assembly, then you need 50 mb x 1 million
   to robustly sample your rarest genome.

With current assembly approaches that would require about 500 TB of RAM
on a single chassis, partly because of errors, and partly because of the
true underlying diversity of the sample.

Yep.

**Probabilistic de Bruijn graphs** (slides 16-22)

This goes over the approach we just published in `Pell et al, (PNAS,
2012)
<http://pnas.org/content/early/2012/07/25/1121464109.abstract>`__
for partitioning metagenomes using low-memory data structures.

See my `story behind the paper <http://ivory.idyll.org/blog/kmer-percolation-published.html>`__ blog post, too.

**Online, streaming, lossy compression** (slides 23-27)

This goes over the digital normalization approach that's in preprint
form `at arXiv <http://arxiv.org/abs/1203.4802>`__.

See my blog posts `what is diginorm, anyway?
<http://ivory.idyll.org/blog/what-is-diginorm.html>`__ and `our
approach to writing replicable papers
<http://ivory.idyll.org/blog/replication-i.html>`__.

**What do we assemble?** (slide 28)

We get a lot of assembled microbial sequences out of our soil samples.
We have never seen most of 'em.

**Physics ain't biology** (slides 30-39)

This is discussed in more detail in `this blog post <http://ivory.idyll.org/blog/physics-aint-biology-and-vice-versa.html>`__.  I need to write a follow up...

Three anecdotes that I want to give during the talk:

First, one of the (several) reasons I'm in biology now is because
of Hans Bethe, the well known physicist.  We were talking over dinner
(my father and Hans collaborated for many years) and I asked him
what career advice he had for young scientists.  He responded that
were he starting in science today, he would go into biology, as it
had the most opportunities going forward.

Second, the Endomesoderm Network diagram
(http://sugp.caltech.edu/endomes/) started out as an immensely useful
*map* of everything that was known; for the first decade or so, it
focused on laying out the *necessary* genes.  Until it was reasonably
complete, there was no point in trying to model it or use it to
discuss *sufficiency*.  I think the Davidson Lab has been moving in
this direction, although I'm not sure -- I left in 2006.  My main
points with the diagram are that it's immensely complicated in terms
of interactions; it took a decade or more to put together; it's
for only one organism; and there's limited ability to use it for
modeling until you know the majority of the interactions.

Third, my experience in collaborating with physicists is that even if
I'm not as smart as my collaborators, I often know way more biology at
both an explicit and an intuitive level, and this is a useful
contribution.  Physicists go right for the throat of problems and
become monofocused, and sometimes it's nice to remind them that we
don't know everything, but what we do know suggests that maybe
something else is going on too, etc. etc.

--titus
