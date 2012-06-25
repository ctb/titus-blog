Lazyweb query: CloudStore (or KosmosFS)
#######################################

:author: C\. Titus Brown
:tags: python,cloud
:date: 2009-11-24
:slug: lazyweb-cloudstore
:category: science


Does anyone have any experience with CloudStore, formerly known as
KosmosFS?  From http://en.wikipedia.org/wiki/CloudStore: ::

  CloudStore (KFS, previously Kosmosfs) is Kosmix's C++ implementation of
  Google File System. ... CloudStore supports incremental scalability,
  replication, checksumming for data integrity, client side fail-over and access
  from C++, Java and Python.

The project site is here: http://kosmosfs.sourceforge.net/

I'd be interested in comments on general usability, quality, and "feel"...

thanks!

--titus


----

**Legacy Comments**


Posted by Jonathan Ellis on 2009-11-25 at 09:13. 

::

   My impression is that HDFS has at least one and maybe two orders of
   magnitude more users shaking the bugs out.  So if I needed a GFS clone
   I would use that one.    Also, if I needed to use the source I'd much
   rather read someone else's Java than C++.


Posted by Titus Brown on 2009-11-25 at 20:33. 

::

   hey Jonathan, thanks -- GFS advertised differently so I didn't think
   it would fit my needs, but it does seem to in actuality.  It's pretty
   usable from Python?


Posted by Titus Brown on 2009-11-25 at 20:33. 

::

   Sorry, that would be HDFS :)


Posted by Jonathan Ellis on 2009-11-26 at 22:20. 

::

   Dunno, but I would think that between the Jython, Thrift, and libhdfs
   options something probably works.  It looks like third-party SWIG and
   ctypes wrappers for libhdfs are out there.    The command line is
   pretty complete, too: <a href="http://hadoop.apache.org/common/docs/cu
   rrent/hdfs_shell.html">http://hadoop.apache.org/common/docs/current/hd
   fs_shell.html</a>

