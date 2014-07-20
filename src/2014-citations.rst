Citing our software and algorithms - a trial
############################################

:author: C\. Titus Brown
:tags: citations,citing software
:date: 2014-07-20
:slug: 2014-citations
:category: science

Our lab is part of the ongoing online conversation about how to
properly credit software and algorithms; as is my inclination, we're
Just Trying Stuff (TM) to see what works.  Here's an update on our
latest efforts!

A while back (with `release 1.0 of khmer
<http://ivory.idyll.org/blog/releasing-khmer-1_0.html>`__) we added a
`CITATION file
<https://github.com/ged-lab/khmer/blob/master/CITATION>`__ to the
khmer repository and distribution.  This was in response to Robin
Wilson's `call for CITATION files
<http://blog.rtwilson.com/encouraging-citation-of-software-introducing-citation-files/>`__,
and dovetails with some of the efforts of the `R
<http://cran.r-project.org/web/packages/knitr/citation.html>`__ and
`Debian <https://wiki.debian.org/DebianScience/Citations>`__
communities.

In the short term, we don't expect many people to pay attention to
these kinds of infrastructure efforts, and for much of our work we
actually have publications on the algorithms involved. More to the
point, our software isn't *just* software -- it's the instantiation of
novel data structures and algorithms, or at least novel applications
of data structures.  The people who did the research are not
necessarily the same people as the developers and maintainers of our
software implementation, and we'd like to reward both appropriately with
citations.

So, rather than directly citing our tarballs or repositories (see
`F1000 Research
<http://blog.f1000research.com/2013/10/11/open-access-software-our-recent-software-repository-collaborations/>`__
and `Mozilla Science Lab's efforts
<http://mozillascience.org/code-as-a-research-object-a-new-project/>`__)
we have modified our scripts to output the appropriate citation
information.  For example, if you run 'normalize-by-median.py', you
get this output ::

   || This is the script 'normalize-by-median.py' in khmer.
   || You are running khmer version 1.1-9-g237d5ad
   || You are also using screed version 0.7
   ||
   || If you use this script in a publication, please cite EACH of the following:
   ||
   ||   * MR Crusoe et al., 2014. doi: 10.6084/m9.figshare.979190
   ||   * CT Brown et al., arXiv:1203.4802 [q-bio.GN]
   ||
   || Please see the CITATION file for details.

The first citation is the software description, and the second is the
normalization algorithm.

Likewise, if you run 'load-graph.py', you will see::

   || If you use this script in a publication, please cite EACH of the following:
   ||
   ||   * MR Crusoe et al., 2014. doi: 10.6084/m9.figshare.979190
   ||   * J Pell et al., PNAS, 2014 (PMID 22847406)
   ||
   || Please see the CITATION file for details.

which is our De Bruijn graph paper.

Interestingly, GNU Parallel also provides citation information::

   When using programs that use GNU Parallel to process data for publication please cite:

    O. Tange (2011): GNU Parallel - The Command-Line Power Tool,
    ;login: The USENIX Magazine, February 2011:42-47.

   This helps funding further development; and it won't cost you a cent.

which is pretty cool!

Note also that Michael Crusoe, who works with me on khmer (side note:
find Michael some completely over-the-top title - "the khmer software
maestro"?), has been working with the Galaxy folk to `build citation
infrastructure into the Galaxy Tool Shed
<https://wiki.debian.org/DebianScience/Citations>`__.  Mo' infrastructure
mo' bettah.

----

What's next?

Now that we're starting to provide unambiguous and explicit citation
information, it's up to individual actors to cite our software
appropriately.  That's something we can help with (by mentioning it in
e.g. reviews) but I'm not sure how much more we can do in the khmer
project specifically.  (Suggestions welcome here!)

My biggest unanswered concern in this space is now something
completely different: it's providing (and getting) credit for the CS
research.  For example, there are several implementations of the
digital normalization idea -- `in silico normalization (in Trinity)
<http://ivory.idyll.org/blog/trinity-in-silico-normalize.html>`__ and
also BBnorm (see `here
<http://seqanswers.com/forums/showthread.php?p=139223#post139223>`__
and `here <http://seqanswers.com/forums/showthread.php?t=44494>`__).
Those are *implementations* of the underlying idea of normalization,
and I (perhaps selfishly) think that in most cases people using the
BBnorm or Trinity code should be citing our digital normalization
preprint.

This concern emerges from the fact that good *algorithm* development
is largely different from good *software* development.  Many
bioinformaticians provide basic proof of concept for an algorithm or a
data structure, but do not invest much time and energy in software
engineering and community engagement.  While this is a great service
-- we often do need new algorithms and data structures -- we also need
good implementations of data structures and algorithms.  Academia
tends to reward the DS&A and not the implementation folk, but I
think we need to do both, and need to do both *separately*.

So my thought here is that any tool that uses a research algorithm or
data structure developed by others should output citation information
for that other work.

I'm not sure where to draw the line, though -- there are clearly cases
where the data structures and algorithms have been developed further
and our work no longer deserves to be cited in the software, and other
cases where the DS&A work may be irrelevant.  People using Minia, for
example, should *not* need to cite Pell et al., 2012, because the
Minia folk extended our work significantly in their paper and
implementation.  And, for many instances of k-mer counting, our
low-memory k-mer counting work (soon to be published in Zhang et al.,
2014) is not necessary -- so if they're using khmer because of its
convenient Python API, but not depending in any particular way on
low-memory k-mer counting, they probably shouldn't bother citing Zhang
et al.  Or maybe they should, because of accuracy concerns addressed
in that paper?

I'd be interested in your thoughts and experiences here.  (Note, I
haven't sent anything to the Trinity or BBnorm folk because (a) I
haven't thought things through, (b) that'd probably be too aggressive
anyway, and (c) we should figure out what the community norms should
be first...)

--titus
