Request for suggestions on a generator API for khmer
####################################################

:author: C\. Titus Brown
:tags: khmer,api
:date: 2015-03-14
:slug: 2015-a-generator-api-for-khmer
:category: science

I've been putting together a streaming API for khmer that would let us
use generators to do sequence analysis, and I'd be interested in thoughts
on how to do it in a good Pythonic way.

Some background: a while back, `Alex Jironkin asked us for high level
APIs
<http://ivory.idyll.org/blog/2015-how-we-develop-software.html#comment-1847486554>`__,
which turned into `an issue on GitHub
<https://github.com/ged-lab/khmer/issues/776>`__.  More recently, we
`posted a paper on streaming and semi-streaming approaches to spectral
sequence analysis <https://peerj.com/preprints/890/>`__, and so for my
`VanBUG talk
<http://www.slideshare.net/c.titus.brown/2015-vancouvervanbug/31>`__ I
was inspired to put together a little API using generators.

The code looks like this, currently (see versioned permalink to `khmer_api.py <https://github.com/ctb/2015-experimental-graphalign/blob/445c200e662719c2bbf2f172a994ab6806d01edd/khmer_api.py>`__ for full implementation)::

    graph = khmer.new_counting_hash(20, 1e7, 4)
    out_fp = open(os.path.basename(filename) + '.abundtrim', 'w')

    ## khmer scripts/trim-low-abund.py -V, using generators
    input_iter = screed.open(filename)
    input_iter = broken_paired_reader(input_iter)
    input_iter = clean_reads(input_iter)
    input_iter = streamtrim(input_iter, graph, 20, 3)
    output_reads(input_iter, out_fp)

Briefly, what this code does is

1. create the core data structure we use
2. open an output file
3. open an input file
4. create a generator that takes in a stream of data and groups records;
5. create a generator that takes in records, does necessary preprocessing,
   and outputs them;
6. create a generator that does our semi-streaming error trimming (from the
   `semi-streaming preprint <https://peerj.com/preprints/890/>`__);
7. outputs the reads to the given output fp.

The key bit is that this uses *generators*, so all of this is happening
with full-on streaming.  The one exception to this is the 'streamtrim'
which has to cache a subset of the reads for processing more than once.

Interestingly, this is an implementation of the core functionality for
the 'trim-low-abund.py' script that we will be releasing with the next
version of khmer (the release *after* khmer 1.3 - not sure if it's
1.3.1 or 1.4 yet).

You can also replace the 'streamtrim' line with::

    input_iter = diginorm(input_iter, graph, 20)

if you want to do digital normalization.  That turns this into an
implementation of the core functionality for the
'normalize-by-median.py' script that has been in khmer for a while.

Obviously these generator implementations are not yet production-ready,
although they *do* give identical results to the current command line
scripts.

The question I have, though, is what *should* the actual API look like?

The two basic options I've come up with are `method chaining <http://en.wikipedia.org/wiki/Method_chaining>`__ and `UNIX-style pipes <http://en.wikipedia.org/wiki/Pipeline_(Unix)>`__.

Method chaining might look like this::

   read(in_fp). \
       clean_reads(). \
       streamtrim(graph, 20, 3). \
       output(out_fp)

and piping would be ::

   read(in_fp) | \
        clean_reads() | \
        streamtrim(graph, 20, 3) | \
        output(out_fp)

...so I guess that's really pretty minor.  I don't know which is more
Pythonic, though, or what would permit more flexibility in terms of
an underlying flexibility.  Thoughts?

There are some other decisions to be made -- configuration and
parameters.

For configuration, ideally we would be able to specify multiple input
and output files to be paired with them, and/or set default parameters
for multiple steps.  Runtime reporting, error handling, and
benchmarking should all be put into the mix.  Should there be a simple
object with hooks to handle all of this, or what? For example, ::

   s = Streamer(...)  # configure inputs and outputs

   s | clean_reads() | streamtrim(graph, 20, 3) | output()

where 's' could help by holding metadata or the like.  I'm not sure -
I've never done this before ;).

As for parameters, I personally like named parameters, so
``streamtrim`` above would better be ``streamtrim(graph, coverage=20,
cutoff=3)``.  But perhaps passing in a dictionary of parameters would
be more flexible - should we support both?  (Yes, I'm aware that in
Python you can use ** - is there a preference?)

I'd love some examples of more mature APIs that have had the rough
edges rubbed off 'em; this is really a UX question and I'm just
not that well equipped to do this kind of design.

Thoughts? Help? Examples?

cheers,
--titus

p.s. Down the road we're going to add ``correct_errors`` and
eventually ``assemble`` to the steps, and perhaps also adapter
trimming, quality trimming, and mapping. Won't that be fun? Imagine::

   assembly = stream_input(filename1).trim().assemble()

to do your assembly... betcha we can stream it all, too.
