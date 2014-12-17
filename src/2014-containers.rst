The post-apocalyptic world of binary containers
###############################################

:author: C\. Titus Brown
:tags: python,pyblosxom
:date: 2014-12-17
:slug: 2014-containers
:category: science

The apocalypse is nigh.  Soon, `binary executables
<https://github.com/isovic/graphmap/tree/356385631c8e3dacae853e90d354dbac5e994d34>`__
and `containers in object stores
<http://www.mcs.anl.gov/papers/P5209-1014.pdf>`__ will join the many
Web-based pipelines and the several `virtual machine images
<http://escience.washington.edu/blog/reproducible-research-and-cloud-computing>`__
on the dystopic wasteland of "reproducible science."

----

Anyway.

I had a conversation a few weeks back with a senior colleague about
container-based approaches (like Docker) wherein they advocated the
shipping around of executable binary blobs with APIs.  I pointed out
that blobs of executable code were not a good replacement for
understanding or a path to progress (`see my blog post on that
<http://ivory.idyll.org/blog/vms-considered-harmful.html>`__) and they
vehemently disagreed, saying that they felt it was an irrelevant
point to the progress of science.

That made me sad.

One of the things I really like about Docker is that the community
emphasizes devops-style clean installs and configurations over
deployment and distribution of binary blobs (images, VMs, etc.)  Let's
make sure to keep that; I think it's important for scientific progress
to be able to `remix software
<http://ivory.idyll.org/blog/research-software-reuse.html>`__.

I'll just close with this comment:

The issue of whether I can *use* your algorithm is largely orthogonal
to the issue of whether can I *understand* your algorithm.  The former
is engineering progress; the latter is scientific progress.

--titus

p.s. While I do like to pick on the Shock/Awe/MG-RAST folk because
their pipeline is utterly un-reusable by anyone, anywhere, ever, I am
being extremely unfair in linking to their paper as part of this blog
post.  They're doing something neat that I am afraid will ultimately
lead in bad directions, but they're not espousing a binary-only view
of the world at all.  I'm just being funny.  Honest.

p.p.s. Bill Howe and I also agree.  So I'm being multiply unfair.  I know.
