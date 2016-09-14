Publishing Open Source Research Software in JOSS - an experience report
#######################################################################

:author: C\. Titus Brown
:tags: software,joss
:date: 2016-09-14
:slug: 2016-publishing-oss-research-software
:category: science

Our first JOSS submission (paper? package?) is `about to be accepted
<https://github.com/openjournals/joss-reviews/issues/27>`__ and I wanted
to enthuse about the process a bit.

JOSS, the Journal of Open Source Software, is a place to publish your
research software packages.  Quoting from `the about page <http://joss.theoj.org/about>`__,

   The Journal of Open Source Software (JOSS) is an academic journal
   with a formal peer review process that is designed to improve the
   quality of the software submitted. Upon acceptance into JOSS, a
   CrossRef DOI is minted and we list your paper on the JOSS website.

How is JOSS different?

In essentially all other academic journals, when you publish software
you have to write a bunch of additional stuff about what the software
does and how it works and why it's novel or exciting.  This is true
even in `some of the newer models for software publication like
F1000Research
<http://f1000research.com/for-authors/article-guidelines/software-tool-articles>`__,
which hitherto `took the prize for least obnoxious software
publication process <http://f1000research.com/articles/4-900/v1>`__.

JOSS takes the attitude that what the software *does* should be laid
out *in the software documentation*.  JOSS also has the philosophy
that since *software is the product* perhaps *the software itself
should be reviewed* rather than the software advertisement (aka
scientific paper).  (Note, I'm a reviewer for JOSS, and I'm totally in
cahoots with most of the `ed board
<http://joss.theoj.org/about#editorial_board>`__, but I don't speak
for JOSS in any way.)

To put it more succinctly, with JOSS the focus is on the software itself,
not on ephemera associated with the software.

The review experience
~~~~~~~~~~~~~~~~~~~~~

I submitted our `sourmash <https://github.com/dib-lab/sourmash/>`__
project a few months back.  Sourmash was a little package I'd put
together to do MinHash sketch calculations on DNA, and it wasn't
defensible as a novel package.  Frankly, it's not that *scientifically*
interesting either.  But it's a potentially **useful** reimplementation
of `mash <https://github.com/marbl/Mash>`__, and we'd already found it
useful internally.  So I submitted it to JOSS.

As you can see from the `JOSS checklist
<https://github.com/openjournals/joss-reviews/issues/27#issue-159802506>`__,
the reviewer checklist is both simple and reasonably comprehensive.
 `Jeremy Kahn <https://github.com/jkahn>`__ undertook to do
the review, and found a host of big and small problems, ranging from
licensing confusion to versioning issues to straight up install bugs.
Nonetheless his `initial review was pretty positive
<https://github.com/openjournals/joss-reviews/issues/27#issuecomment-226859556>`__.
(Most of the review items were filed as issues on `the sourmash
repository <https://github.com/dib-lab/sourmash/>`__, which you can
see referenced inline in the review/pull request.)

After his initial review, `I addressed most of the issues
<https://github.com/openjournals/joss-reviews/issues/27#issuecomment-232065953>`__
and he did another round of review, where he recommended acceptance
after fixing up some of the docs and details.

Probably the biggest impact of Jeremy's review was my realization that
we needed to adopt a formal release checklist, which I did by `copying
Michael Crusoe's detailed and excellent checklist from khmer
<https://sourmash.readthedocs.io/en/latest/release.html>`__.  This made
*doing* an actual release much saner.  But a lot of confusing stuff
got cleared up and a few install and test bugs were removed as well.

So, basically, the review did what it should have done - checked our
assumptions and found big and little nits that needed to be cleaned
up.  It was by no means a gimme, and I think it improved the package
tremendously.

+1 for JOSS!

Some thoughts on where JOSS fits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are plenty of situations where a focus solely on the software
isn't appropriate.  With our khmer project, we `publish new data
structures and algorithms
<http://www.pnas.org/content/109/33/13272.abstract>`__, `apply our
approaches to challenging data sets
<http://www.pnas.org/content/111/13/4904.abstract>`__, `benchmark
various approaches
<http://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0101271>`__,
and `describe the software suite at a high level
<http://f1000research.com/articles/4-900/v1>`__.  But in none of these
papers did anyone really review the software (although some of the
reviewers on the `F1000 Research paper
<http://f1000research.com/articles/4-900/v1>`__ did `poke
<http://f1000research.com/articles/4-900/v1#referee-response-10508>`__
it with a `stick
<http://f1000research.com/articles/4-900/v1#referee-response-10513>`__).

JOSS fills in a nice niche here where we could receive a 3rd-party
review of the software itself.  While I think Jeremy Kahn did an
especially exemplary review of the sourmash and we could not expect
such a deep review of the much larger khmer package, a *broad* review
from a third-party perspective at each major release point would be
most welcome.  So I will plan on a JOSS submission for each
major release of khmer, whether or not we also advertise the release
elsewhere.

I suppose people might be concerned about publishing software in
multiple ways and places, and how that's going to affect citation
metrics.  I have to say I don't have any concerns about salami slicing
or citation inflation here, because software is still largely ignored
by Serious Scientists and that's the primary struggle here. (Our
experience is that people systematically `mis-cite us
<http://ivory.idyll.org/blog/2015-khmer-impact.html>`__ (despite
`ridiculously clear guidelines
<http://ivory.idyll.org/blog/2014-citations.html>`__) and my belief is
that software and methods are generally undercited.  I worry more about
that than getting undue credit for software!)

JOSS is already seeing a fair amount of activity and, after my
experience, if I see that something was published there, I will be
much more likely to recommend it to others.  I suggested you all check
it out, if not as a place to publish yourself, as a place to find better
quality software.

--titus
