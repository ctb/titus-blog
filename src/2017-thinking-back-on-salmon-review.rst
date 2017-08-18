Thoughts on my Salmon review
#############################

:author: C\. Titus Brown
:tags: salmon,review
:date: 2017-08-18
:slug: 2017-thinking-back-on-salmon-reviwe
:category: science

I was one of the reviewers of the Salmon paper by Patro et al., 2017,
`Salmon provides fast and bias-aware quantification of transcript
expression
<https://www.nature.com/nmeth/journal/v14/n4/abs/nmeth.4197.html>`__,
and I `posted my review <2016-review-salmon.html>`__ in large part
because of Lior Pachter's `blog post levying charges of intellectual
theft and dishonest against the Salmon authors
<https://liorpachter.wordpress.com/2017/08/02/how-not-to-perform-a-differential-expression-analysis-or-science/>`__.
More recently, the Salmon authors posted a `strong rebuttal
<https://t.co/ul5MxMtiKM>`__ that is worth reading.

I posted my review verbatim, without any editing, and with the charge
for the review laid out by the journal.

Looking back on it, I have a few thoughts - especially in light of
Lior's hit piece and Rob et al's response.

First, it is always a pleasure reviewing software papers when you have
used the tool for ages.  My lab uses Salmon, trains people in running Salmon,
and passes around blog posts and papers discussing Salmon results.  So I was
already pretty confident that Salmon performed well in general and I did not
need to try to run it, evaluate it, etc.

Second, my review hit a number of high points about Salmon: generally,
that it was an important new tool of interest and that it was a
significant improvement to the tried-and-tested Kallisto
technique. More specifically, I felt that the GC bias correction was
likely to be critical in the future (see esp the isoform switching
observation) and that the open-source license was an important aspect
of the Salmon software.  To my mind this meant that it warranted
publication, a case I made succinctly but tried to makestrongly.

Third, my review missed at least one very important aspect, which was
the streaming nature of the Salmon implementation. The rebuttal
covers this nicely.

Last, my review uses the term "pseudoalignment" and not
"quasimapping." The distinction between these two terms is part of the
brouhaha; but to my mind the basic idea of finding equivalence classes
for reading mapping is pretty similar no matter what you call it, and
it was clear (both from the citations to Kallisto and the discussion
in the paper) that the core concept had been published as part of the
Kallisto work.  I don't think it matters what it's called - it's a
good idea, I'm glad that there are multiple implementations that agree
well with each other, and I think it was adequately, appropriately,
and generously cited in the Salmon paper.

So, anyway, there are my thoughts. Yours welcome below!

(Before you comment, please do see the code of conduct for this blog -
it's linked below. In particular, I place myself under no obligation
to retain posted comments, and I will delete comments that are
useless, or dishonest.)

--titus
