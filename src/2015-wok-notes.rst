Notes on the "week of khmer"
############################

:author: \C. Titus Brown
:tags: khmer,wok,graphalign
:date: 2015-05-26
:slug: 2015-wok-notes
:category: science

Last week we wrote five blog posts about some previously un-publicized
features in the `khmer software <https://github.com/dib-lab/khmer/>`__
- most specifically, read-to-graph alignment and sparse graph labeling
-- and what they enabled.  We covered some half-baked ideas on
`graph-based error correction
<http://ivory.idyll.org/blog/2015-wok-error-correction.html>`__,
`variant calling
<http://ivory.idyll.org/blog/2015-wok-variant-calling.html>`__,
`abundance counting
<http://ivory.idyll.org/blog/2015-wok-counting.html>`__, `graph
labeling <http://ivory.idyll.org/blog/2015-wok-labelhash.html>`__, and
`assembly evaluation
<http://ivory.idyll.org/blog/2015-wok-evaluate.html>`__.

It was, to be frank, an immense writing and coding effort and one from
which I'm still recovering!

Some details on khmer and replicating results
---------------------------------------------

For anyone interested in following up on implementation details or any
other details of the analyses, all of the results we wrote up last
week can be replicated from scratch using khmer and publicly available
data & scripts.  You can also use a Docker container to run
everything.  To try this all out, use the links at the bottom of each
blog post and follow the instructions there.

khmer itself is licensed under the `BSD 3-Clause License
<http://opensource.org/licenses/BSD-3-Clause>`__, and hence fully
available for reuse and remixing, including by commercial entities.
(Please contact me if you have any questions about this, but it's
really that simple.)

The majority of the khmer codebase is C++ with a CPython wrapping that
provides a Python interface to the data structures and algorithms.
Some people are already using it primarily via the C++ interface,
while our own group mainly uses the Python interface.

More reading and references
---------------------------

One wonderful outcome of the blog posts was a bunch of things to read!
A few I was already aware of, others were new to me, and I was
thoroughly reminded of my lack of knowledge in this area.

In no particular order,

Lex Nederbragt has a wonderful blog post introducing the concept of
graph-based genomics, `On graph-based representations of a (set of)
genomes
<https://flxlexblog.wordpress.com/2015/04/09/on-graph-based-representations-of-a-set-of-genomes/>`__.
The references at the bottom are good for people that want to dive
into this more.

Heng Li wrote a `nicely technical blog post
<http://lh3.github.io/2014/07/25/on-the-graphical-representation-of-sequences/>`__
with a bunch more references.

Zam Iqbal left a `nice comment
<http://ivory.idyll.org/blog/2015-wok-error-correction.html#comment-2033226348>`__
on my first post that largely reiterated the references from Lex and
Heng's blog posts (which I should have put in there in the first
place, sorry).

Several people pointed me at `BGREAT, Read Mapping on de Bruijn graph <http://arxiv.org/abs/1505.04911>`__. I need to read it thoroughly.

Rob Patro pointed me at several papers, including `Compression of high throughput sequencing data with probabilistic de Bruijn graph <http://arxiv.org/abs/1412.5932>`__ and `Reference-based compression of short-read sequences using path encoding <http://www.ncbi.nlm.nih.gov/pubmed/25649622>`__. More to read.

`Erik Garrison pointed me at 'vg', tools for working with variant
graphs. <https://twitter.com/erikgarrison/status/602152715020406784>`__
To quote, "It includes SIMD-based "banded" string to graph
alignment. Can read and write GFA."  See `the github repo
<https://github.com/ekg/vg>`__.

So what was the point?
----------------------

I had many reasons for investing effort in the the blog posts, but, as
with many decisions I make, the reasoning became less clear as I pushed
forward.  Here are some things I wrote down while thinking about the topic
and writing things up --

* we've had a lot of this basic functionality implemented for a while, but
  had never really applied it to anything.  This was an attempt to drive
  a vertical spike through some problems and see how things worked out.

* taking existing ideas and bridging them to practice is always a good way
  to understand those ideas better.

* from writing this up, I developed more mature use cases, found
  broken aspects of the implementation, provided minimal documentation
  for a bunch of features in khmer, and hopefully sharpened our focus
  a bit.

* not enough people realize how fundamental a concept graphs (in general)
  are, and (more specifically) how powerful De Bruijn graphs are!  It was
  fun to write that up in a bit more detail.

* I've found it virtually impossible to think concretely about
  publishing any of this.  Very little of it is particularly novel and
  I'm not so interested in micro-optimizing the code for specific use
  cases so that we can publish a "10% better" paper."  So writing them
  up as blog posts seemed like a good way to go, even had that not been
  my native inclination.

* Providing low-memory and scalable implementations seems like a good
  idea, especially when it's as simple as ours.

So far I'm quite happy with the results of the blogging (quiet
interest, more references, some real improvements in the code base,
etc. etc.).  For now, I don't have anything more to say than that I'd
like to try *more* technical blogging as a way to release potentially
interesting computational bits and bobs to the community, and discuss
them openly.  It seems like a good way to advance science.

--titus
