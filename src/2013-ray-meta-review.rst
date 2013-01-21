A review of Ray Meta: scalable de novo metagenome assembly and profiling
########################################################################

:author: C\. Titus Brown
:tags: science,peer review
:date: 2013-01-20
:slug: 2013-ray-meta-review
:category: science

I was a reviewer on Boisvert et al., `Ray Meta: scalable de novo
metagenome assembly and profiling
<http://genomebiology.com/2012/13/12/R122/abstract>`__, and (as with
`DSK: k-mer counting with very low memory usage
<http://ivory.idyll.org/blog/2013-dsk-review.html>`__) I thought I'd
share my review.

(Sorry, it's really short.  My first round review had some comments
that they handily addressed in the second submission, so I had nothing
to add to what they said in the paper. :)

I do have two quick comments at the bottom that I *didn't* send them at
the time of the review.

---

The authors discuss the use of Ray Meta to assemble metagenomes de
novo, and, separately, to assign them to taxnonomies using a colored
de Bruijn graph approach.  The importance is several-fold: I believe
this is the most scalable metagenome assembler yet published; the
asssembly results are impressive; the scalability is impressive; and
this is the first time the colored de Bruijn graph approach has been
applied to metagenomes.

Ovearll, this is an impressive accomplishment and I am very pleasantly
surprised that they could get such good results with a message-passing
implementation.  The references are very good, and the discussion is
expert and relevant.

The authors are to be commended for releasing their software as open
source through SF and github.  Excellent!

I have no reservations about publication and recommend immediate
acceptance.

Signed,
C\. Titus Brown
ctb@msu.edu

---

OK, now for the two post-review comments --

First, in a comment thread, I urged them to post to arXiv, and Sebastien said:

   But as to pushing manuscripts onto preprint servers, I prefer to let
   the standard peer review process follow its course. And I think it is
   best to have all the karma focused on a single URI. So our paper
   should be out in the wild somewhere soon.

This indicates, in my view, a fundamental misunderstanding of the purpose of
science.  I will be contacting him shortly re pistols at dawn. :)

Second, we are working on our own system for assembling large, nasty
metagenomes -- you can read about it `here
<http://arxiv.org/abs/1212.2832>`__.  I would love to know if Ray Meta
works well on our own data, but I haven't had time to think about how
best to try it out; I don't have the manpower or time to do it myself,
but I really want to play with Ray Meta.  Maybe I'll try it out for
the summer course... hmm.  Anyway, I hope to write a much more
thorough post about Ray Meta based on running it on our own nasty
soil data.  But that will have to wait.

--titus
