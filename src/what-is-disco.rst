What is disco?
##############

:author: C\. Titus Brown
:tags: python,mapreduce
:date: 2009-04-20
:slug: what-is-disco
:category: python


Anyone out there used `disco (http://discoproject.org/) <http://discoproject.org/>`__?  Comments, good/bad/neutral?

From the page:

   Disco is an open-source implementation of the Map-Reduce framework for distributed computing. As the original framework, Disco supports parallel computations over large data sets on unreliable cluster of computers.

   The Disco core is written in Erlang, a functional language that is designed for building robust fault-tolerant distributed applications. Users of Disco typically write jobs in Python, which makes it possible to express even complex algorithms or data processing tasks often only in tens of lines of code. This means that you can quickly write scripts to process massive amounts of data. 

thanks!

--titus


----

**Legacy Comments**


Posted by phaithful on 2009-04-20 at 16:42. 

::

   I use Disco quite a bit these days. Hadoop sometimes is a bit to
   unwieldy and I just need a simple map/reduce process that can be
   distributed over multiple machines.    It's super easy to setup unlike
   Hadoop and I was up and running in no time.     The only drawbacks is
   that it's not "super" fast, so if you need something realtime than I'd
   go with Hadoop or something else.


Posted by Brad Chapman on 2009-04-20 at 18:48. 

::

   Titus;  I played around with it for parsing GFF files. The short
   answer to your questions is that I had no problems with setup and
   programming to the interface. For my application, files weren't big
   enough to justify the overhead of running on a cluster, but I'd use it
   in the future if a bigger problem comes along. It also integrates well
   with EC2.    I wrote up some detailed thoughts when I was playing with
   it:     <a href="http://bcbio.wordpress.com/2009/03/22/mapreduce-
   implementation-of-gff-parsing-for-biopython/">Basic implementation</a>
   <a href="http://bcbio.wordpress.com/2009/03/29/python-gff-parser-
   update-parallel-parsing-and-gff2/">Running on EC2</a>    Brad


Posted by Jesse Noller on 2009-04-20 at 20:10. 

::

   I only played with it a bit; it's easy to setup and start hacking, if
   I had more crunching needs, it would probably be high up on my list.


Posted by Titus Brown on 2009-04-20 at 22:06. 

::

   Sounds like a Good Thing -- thanks, everyone!

