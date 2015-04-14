PyCon sprints - playing with named pipes and streaming and khmer
################################################################

:author: C\. Titus Brown
:tags: pipes,khmer
:date: 2015-04-14
:slug: 2015-pycon-sprint-named-pipes
:category: science

I'm at the PyCon 2015 sprints (day 2), and I took the opportunity to play
around with named pipes.

I was reminded of named pipes by Vince Buffalo in `this great blog
post
<http://vincebuffalo.com/2013/08/08/the-mighty-named-pipe.html>`__,
and since `we at the khmer project are very interested in streaming
<https://github.com/ged-lab/khmer/issues/393>`__, and named pipes fit
well with a streaming perspective, I thought I'd check out named pipes
as a way to communicate sequences between different khmer scripts.

----

First, I tried using named pipes to tie digital normalization together with
splitting reads out into two output files, left and right::

   mkfifo aa
   mkfifo bb

   # set up diginorm, reading from 'aa' and writing to 'bb'
   normalize-by-median.py aa -o bb &

   # split reads into left and right, reading from 'bb' and outputting to
   # output.1 / output.2
   split-paired-reads.py bb -1 output.1 -2 output.2 &

   # feed in your sequences!
   cat sequence.fa > aa

Here the setup is a bit weird, because you have to set up all the commands
that are going to operate on the data before feeding in the data.  But it
all works!

----

Next, I tried named pipes.  This does essentially the same thing as above,
but is much nicer and more succinct::

   normalize-by-median.py sequence.fa -o >(split-paired-reads.py /dev/stdin -1 output.1 -2 output.2)

----

Finally, I tried to make use of functionality from our `new
semi-streaming paper <https://peerj.com/preprints/890/>`__ to run
`3-pass digital normalization
<https://khmer-protocols.readthedocs.org/en/latest/metagenomics/2-diginorm.html>`__
using semi-streaming -- ::

   trim-low-abund.py -Z 20 -C 2 sequence.fa -o >(normalize-by-median.py /dev/stdin -o result.fa

but this fell apart because 'trim-low-abund.py' doesn't support -o ;).
This led to a `few <https://github.com/ged-lab/khmer/issues/946>`__
`issues <https://github.com/ged-lab/khmer/issues/947>`__ being filed
in our issue tracker...

----

Very neat stuff. It has certainly given me a strong reason to make
sure all of our scripts support streaming input and output!

--titus
