Anecdotal science
#################

:author: C\. Titus Brown
:tags: reproducible
:date: 2012-09-03
:slug: anecdotal-science
:category: science

I'm starting to notice that a lot of bioinformatics is anecdotal.

People publish software that "works for them."  But it's not clear
what "works" means -- all to often either the exact parameters or the
specific evaluation procedure is not provided (and yes, there's
a `double standard <../a-call-for-open-lab-protocols.html>`__ here
where experimental methods are considered more important than
computational methods).

This means that their result is not an example of computational
science.  It's an anecdote.

Worse, it's pretty non-useful.  I used to think biological validation
of bioinformatics was a far more important end goal than validation of
the bioinformatics -- that is, if a paper did some hand waving in the
bioinformatics section but then showed a solid biological result, it
was fine.  But now I'm switching firmly over to the opinion that I was
full of it then, and am now more enlightened.  Read on.

Let's take the `Iverson et al. paper
<http://www.ncbi.nlm.nih.gov/pubmed/22301318>`__ (`published in
Science <http://www.sciencemag.org/content/335/6068/587>`__) as an
example -- I'm picking on it because `someone more important than me
already pointed out some of its problems
<http://phylogenomics.blogspot.com/2012/02/interesting-new-metagenomics-paper-w.html>`__,
but I'm happy to point out many, many more papers in private. I bet
90% of the people reading Iverson et al. are not that interested in
Euryarchaeota.  Most of them want to know how to take metagenomes --
simple or complex -- and assemble genomes out of them.  But they will
be stymied, because in the initial publication, the source code and
parameters are not specified.  (Is the method of evaluation available
in paper??@@)

The lack of computational details causes us lots of headaches (which
is one reason I am so bullish on practical considerations of
reproducible science).  The Iverson et al. paper did a great thing:
they developed an approach to scaffolding contigs from metagenome
assembly that (from reading the paper) looks great and makes sense.
Since we happen to have some awesome metagenome contig generation
technology in our lab, we'd love to use their approach.  But, at least
at the moment, we'd have to reimplement it from scratch, which will
take a both solid reimplementation effort as well as guesswork, to
figure out parameters and resolve unclear algorithmic choices.  If we
do reimplement it from scratch, we'll probably find that it works
really well (in which case Iverson et al. get to claim
that they invented the technique and we're derivative) or we'll find
that it works badly (in which case Iverson et al. can
claim that we implemented it badly).  It's hard to see this working
out well for us, and it's hard to see it working out poorly for
Iverson et al.

(It kind of helps my morale that no one I've talked to can figure out
how the Iverson paper got accepted without the source code being
available. This seems like a failure on the part of the reviewers and
the Science editors rather than something accepted in the field of
metagenomics.  Good thing Science is a high-impact journal, otherwise
I'd be worried that `the paper might be wrong! <http://en.wikipedia.org/wiki/GFAJ-1#Criticism>`__)

All too often, biologists and bioinformaticians spend time hunting for
the magic combination of parameters that gives them a good result,
where "good result" is defined as "a result that matches expectations,
but with unknown robustness to changes in parameters and data."  (I
blame the `hypothesis-driven fascista
<../is-discovery-science-really-bogus.html>`__ for the attitude that a
result that matches expectations is a good thing.)  I hardly need to
explain why that's a problem, I hope; read this `fascinating
@simplystats blog post <http://simplystatistics.org/post/30452945357/increasing-the-cost-of-data-analysis>`__ for some interesting ideas on how to deal
with the search for parameters that lead to a "good result".  But
often the *result* you achieve are only a small part of the content of
a paper -- *methods*, computational and otherwise, are also important.
This is in part because people need to be able to (in theory)
reproduce your paper, and also because in larger part progress in
biology is driven by new techniques and technology.  If the methods
aren't published in detail, you're short-changing the future.  As
noted above, this may be an excellent *strategy* for any given lab,
but it's hardly conducive to advancing science.  After all, if the
methods and technology are both robust and applicable to more than
your system, other people will use them -- often in ways you never
thought of.

Closer to home, I think I can attribute some of my collaborators'
impatience with me to this attitude of mine.  I want to do good,
solid, robust computational science, as well as relevant biology; my
schtick is, at least at the moment, **computational methods**.  Since
my collaborators tend not to be computationally focused, they don't
always get the point of all the computational work.  Some of them are
either more patient or more relaxed about the whole thing -- if you're
wondering why Jim Tiedje is co-authoring papers on probabilistic de
Bruijn graphs, well, that's why :).  Some of them are less patient,
and it's why I would never recommend a bioinformatics analysis position
to anyone -- it leads to computational science driven by biologists,
which is often something we call "bad science".

What's the bottom line?  Publish your methods, which include your
source code and your parameters, and discuss your controls and
evaluation in detail.  Emphasize reproducibility and expect others to
be interested in using your approaches.  Otherwise? You're doing
anecdotal science.

--titus
