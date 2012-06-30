A good way to publish -- arXiv FTW
##################################

:author: C\. Titus Brown
:tags: papers,arxiv
:date: 2012-06-29
:slug: science-f-yeah
:category: science

(Or, "A better way to publish bioinformatics.")

We just got word that our paper, "Scaling metagenome assembly with
probabilistic de Bruijn graphs" `[ arXiv ]
<http://arxiv.org/abs/1112.4193>`__ `[ github ]
<https://github.com/ged-lab/2012-paper-kmer-percolation>`__ has been
accepted for publication in PNAS.  (Yay!)  I just posted the final
version to github, and the arXiv PDF should be updated to the third
version on Tuesday or Wednesday (July 3rd or 4th).  We're very happy,
not least because this is my first senior author paper and my grad
student Jason Pell's first first-author paper.

But we have other reasons to be happy, too.

You see, back in December when we submitted the paper `(on Dec 28th,
2011) <http://ivory.idyll.org/blog/kmer-percolation-posted.html>`__, I
took the relatively unusual step of posting it to `arXiv
<http://arxiv.org>`__, a preprint server.  This made the paper
available before peer review, which isn't something that we tend to do
in bioinformatics or biology, for whatever reason.

The paper didn't exactly sink like a rock, but I didn't get much in
the way of feedback or publicity from making it available.  That's OK,
it sounds pretty esoteric -- it involves biology, computer science,
and physics, and discusses DNA shotgun sequencing, metagenomics,
probabilistic data structures, and percolation theory.  Apart from
being nearly impossible to review from a position of expertise (my
group may actually be the world expert on the intersection of these
four topics, solely because we wrote this paper), the paper seemed
reasonably impenetrable to pretty much any audience.  Oh well.

Then two super neat things happened.

First, about a month ago I received a request to review a paper on
`quip <http://www.cs.washington.edu/homes/dcjones/quip/>`__, a DNA
sequence compression package that uses probabilistic data structures.
I was asked to review it because they cited our arXiv paper (yes, you
can cite arXiv papers -- it's archival!)  I did review the quip paper
(it's a great paper) and I hope it appears soon.  (I signed the review,
note.)

Second, about two weeks ago I heard about `Minia
<http://minia.genouest.org/>`__, an assembler that used an extension
of our basic idea to do really low-memory assembly of the human
genome.  What was ultra cool about this is that Rayan Chikhi, one of
the authors, told me directly that they built off of our paper: ::

   Thanks sharing your pre-prints on arxiv, our article is a direct
   consequence of that action!

So, not only does our newly-accepted PNAS paper have two citations,
both from *before* it was accepted, but another group has already
extended our approach in a new direction (which looks pretty
significant to me, BTW).

This just seems to be the right way to do science, to me: minimum time
from paper to exposure to (possible) extension.

To be clear, I don't want to claim that our paper is super
consequential (that'll wait for another blog post ;) or even that the
Minia assembler is an amazing breakthrough that totally built off of
our giant contribution.  I just think it demonstrates a way to
accelerate bioinformatics research -- which we should be doing, yeh?

Incidentally, Cameron Neylon, the new advocacy director for PLoS, told
me that in physics (where they've been using arXiv for 20 years or
more) the citation count for papers peaks right around the point where
they're *accepted* for publication -- because by then they're old hat:
everyone has read them on arXiv already.  Wow, physics and
bioinformatics publication culture sure is different :).

--titus

p.s. Note that the paper is under embargo until it's formally
published.  I'm not sure what that means in the age of blogs, exactly,
but if you're a NY Times reporter just itchin' to write a front-page
story about our paper... please wait, okay?
