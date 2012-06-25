zounds, for running lots of BLASTs
##################################

:author: C\. Titus Brown
:tags: python,bioinformatics
:date: 2008-07-03
:slug: zounds-announce
:category: science


I finally got sick of manually schlepping BLAST files around, so I wrote
something to do it for me.  'zounds' is a very simple server/client
system for coordinating a bunch of 'worker' nodes through a central
server; it does everything in Python with objects and pickling, so it's
easy to do extra Python-based processing on the worker nodes.  See 
'filters' for more info.

You can read a bit more about zounds here:

        http://iorich.caltech.edu/~t/zounds/README.html

It's freely available, open-source, etc. etc.

Comments and thoughts welcome; send them to the `bip list
<http://lists.idyll.org/listinfo/biology-in-python>`__.

--titus
