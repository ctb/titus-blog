Dear Lazyweb: Write-Once/Few-Read-Many Options for Python?
##########################################################

:author: C\. Titus Brown
:tags: python,bioinformatics
:date: 2009-01-05
:slug: lazyweb-worm-options-in-python
:category: science


The decision of python-dev to deprecate bsddb has left us in a bit of
a pickle (hah!) over in the pygr project.  We're looking for a
replacement for bsddb for default storage of infrequently- (or never-) changed
pickled Python objects.  Some of the parameters under consideration are:

 - Python version availability: does it work for 2.2 on up?  What about 
   py3k?

 - cross-platform availability: is it readily available for Mac OS X
   and Windows, **no compilation required**?  Byte-order compatible across
   platforms?  Comes with Python by default is a plus...

 - scalability: can it scale to gigabytes or 10s of gb of data?  10s of
   millions of records?

 - is it fast, whatever that means?

 - is it simple to set up: no sysadminning required?

We're looking at sqlite and `python-cdb
<http://pypi.python.org/pypi/python-cdb/0.32>`__ right now, as well as
a home-grown solution.  What have we missed?

So far Istvan Albert has benchmarked bsddb hashopen and btopen,
sqlite, GNU dbm, and `python-cdb
<http://pypi.python.org/pypi/python-cdb/0.32>`__; you can see the
results `here
<http://pygr.googlecode.com/svn/contrib/benchmark/results.txt>`__.
The `whole discussion thread
<http://groups.google.com/group/pygr-dev/browse_thread/thread/cd06c5a9f7107881>`__
on pygr-dev may be worth reading if you're interested.

A few additional notes --

 - Couchdb, MySQL, PostgreSQL, etc. violate the "no sysadminning required"
   rule.  We will probably support them, but they will not be the default.

 - python-cdb looks blazingly fast, but we would have to port it to Windows,
   and make binaries available.  What's the scoop on python-cdb, anyway?  Is
   it well maintained, a well-used project, etc?

 - sqlite isn't "built in" prior to Python 2.4.

Anyway, at this point I'm just trying to figure out what we're missing, if
anything!

thanks,
--titus


----

**Legacy Comments**


Posted by bryancole on 2009-01-05 at 05:00. 

::

   How about PyTables. It uses HDF5 as the storage format. It's v. fast
   and is designed for Large datasets.


Posted by Titus Brown on 2009-01-05 at 05:27. 

::

   Ah-hah, thanks!  Yes, we looked at HDF5 a while back but it's not
   included in the benchmarks.  We should add it.    --t


Posted by Michael Foord on 2009-01-05 at 05:57. 

::

   Why not continue to use bsddb? The Python module is still maintained
   separately, right?


Posted by Anakron on 2009-01-05 at 06:28. 

::

   What about ZODB? As far as I know it doesn't need configuration and is
   easy to use.


Posted by Zachary Voase on 2009-01-05 at 06:41. 

::

   You might want to take a look at the anydbm module, I don't know how
   it holds up feature-wise but it's in the stdlib and it's multi-
   platform:    <a href="http://docs.python.org/library/anydbm.html
   #module-anydbm">http://docs.python.org/library/anydbm.html#module-
   anydbm</a>


Posted by Alec Thomas on 2009-01-05 at 07:02. 

::

   Metakit might be an option  <a href="http://www.equi4.com/metakit/pyth
   on.html">http://www.equi4.com/metakit/python.html</a>


Posted by Gal Varoquaux on 2009-01-05 at 07:23. 

::

   Hi Titus,    I have the same problem. I haven't had time to think
   about it, so I don't think I can contribute some useful comment.
   However I am interested in your conclusions, so please post them on
   your blog.    @Michael: The way I see it is that bsddb was convenient
   because it was shipped was Python. Now that it goes away, we must make
   a educated choice, rather than use a default.


Posted by Zachary Voase on 2009-01-05 at 08:05. 

::

   You might want to take a look at the anydbm module, I don't know how
   it holds up feature-wise but it's in the stdlib and it's multi-
   platform:    <a href="http://docs.python.org/library/anydbm.html
   #module-anydbm">http://docs.python.org/library/anydbm.html#module-
   anydbm</a>


Posted by Doug Hellmann on 2009-01-05 at 09:25. 

::

   I second ZODB.  They've pulled it out of Zope core, so while it still
   has some code dependencies to run you don't actually have to do that
   much work to use it.    Failing that, take a look at shove (an
   alternative to the standard module shelve).  It supports a variety
   backends, all accessed transparently through the dictionary API.  It
   would make performance testing easy, since changing the backend is as
   simple as changing the URL used to open the database.


Posted by Doug Napoleone on 2009-01-05 at 10:14. 

::

   Another recommendation for PyTables here.    I am not allowed to give
   specifics or details, but um.. 30+ speech scientists on a grid running
   week long experiments generating multiple PB of temp data w/o an admin
   in site... yea... just go with PyTables :-)


Posted by nes on 2009-01-05 at 11:10. 

::

   Has anybody benchmarked PyTables though? I tested it a couple of years
   ago and it was about the same speed or slower than SQLite.


Posted by Michael Watkins on 2009-01-05 at 13:48. 

::

   If ZODB proves to be a contender then Durus[1] would be as well. Its
   simpler than ZODB yet probably offers all the features required for a
   write once read many scenario. It satisfies the "runs on most versions
   of Python" requirement, including running on Python 3.0, today[2].
   Yet it (and perhaps by extension ZODB) may not scale as every object
   in the DB, accessed or not, will consume RAM. A BerkeleyDB or
   postgres/mysql etc back end would remove that issue... writing such a
   back end for Durus is actually fairly trivial - must be, since I wrote
   a pgsql backend as an experiment one afternoon.[3]    Titus didn't
   state what sort of "python objects" need to be stored and
   retrieved/queried - if the python objects are elemental types - tuples
   of strings and numbers for example - Durus (and many such schemes
   probably) can be very fast[4]; if they are complex objects there is
   quite a bit of overhead (this not limited to Durus or ZODB of course):
   (this is from a very old discussion, on a very old machine)
   Inserting 100000 python Tuples into Durus ClientStorage
   testDurusClientServer completed 100000 operations in: 0.274677038193
   seconds.    Inserting 100000 python PersistentObject into Durus
   ClientStorage  testDurusClientServerObjects completed 100000
   operations in: 28.3248071671 seconds.    I guess Cucumber is out of
   the question? :-)      [1] <a href="http://www.mems-
   exchange.org/software/durus/">http://www.mems-
   exchange.org/software/durus/</a>  [2] <a href="http://mail.mems-
   exchange.org/durusmail/qp/441/">http://mail.mems-
   exchange.org/durusmail/qp/441/</a>  [3] <a href="http://mail.mems-
   exchange.org/durusmail/durus-users/921/">http://mail.mems-
   exchange.org/durusmail/durus-users/921/</a>  [4] <a href="http://64.21
   .147.49/durus/performance.py">http://64.21.147.49/durus/performance.py
   </a>


Posted by Martijn Faassen on 2009-01-05 at 14:16. 

::

   Michael Watkins wrote: "Yet it (and perhaps by extension ZODB) may not
   scale as every object in the DB, accessed or not, will consume RAM."
   That's not true for the ZODB as far as I know. Objects that are
   directly connected to objects that are accessed will indeed consume
   RAM (they will be "ghosted"). Objects that are connected only to
   ghosts won't consume RAM at all as far as I know. Finally, the ZODB
   includes powerful BTree facilities, and offloading RAM to disk is what
   BTrees are good at.    The ZODB has the advantage that it's had more
   than 10 years of continued development and is thus rather solid and
   feature-rich. It has minimal set up in the basic case, but can be run
   in a cluster and all kinds of other fun stuff in more advanced cases.
   It also offers efficient large file (blob) storage.    Performance-
   wise it's hard to know. There was some benchmarking done in a sequence
   of blog entries:    <a
   href="http://www.upfrontsystems.co.za/Members/roche/where-im-calling-
   from/zodb-benchmarks-
   revisited">http://www.upfrontsystems.co.za/Members/roche/where-im-
   calling-from/zodb-benchmarks-revisited</a>    One sysadmin drawback is
   that the ZODB (with the usual FileStorage backend) must be "packed"
   once every while.    This blog entry contains a little script that
   uses the ZODB that might serve as a useful example:    <a
   href="http://faassen.n--
   tree.net/blog/view/weblog/2008/06/20/0">http://faassen.n--
   tree.net/blog/view/weblog/2008/06/20/0</a>


Posted by Michael Watkins on 2009-01-05 at 17:41. 

::

   Mea culpa, I made an error in describing one of Durus's limitations -
   in an older, now deprecated, storage format object id's were kept in
   RAM while the newer index scheme (it was introduced in 2006) found in
   the current default file scheme removes this. I inadvertently
   described the old behaviour. Only the object id's new or modified
   since the last pack are maintained in RAM.    I'm gabberflasted that I
   mentioned the old behaviour not the new, as back in 2005 I'd been
   experimenting with some larger datasets in Durus (1.82 million objects
   in an example database)[1] and was running into the limitations of the
   old storage back then.    One thing I like about pgsql as a storage
   back end is the very efficient bulk load capability it has. If you
   have a large data set in some sort of fixed format, it can be very
   quick to load up a pgsql instance; many orders of magnitude faster
   than an "insert". The same can't be said about creating millions of
   Python objects and pickling them... the dumber the "object" or
   serialized format the faster the creation.    [1] <a href="http://mail
   .mems-exchange.org/durusmail/durus-users/291/">http://mail.mems-
   exchange.org/durusmail/durus-users/291/</a>


Posted by Rene Dudfield on 2009-01-05 at 20:15. 

::

   There's so many options...    tokyo cabinet is the state of the art
   <a href="http://tokyocabinet.sourceforge.net/index.html">http://tokyoc
   abinet.sourceforge.net/index.html</a>    cdb is limited in database
   file size...(2/4GiB I think)... however it is the fastest constant
   database... and you can create it **very** quickly.  You'd need to
   update the format to be 64bit aware.  It's also very simple to
   implement, which can be nice.


Posted by Thomas Mangin on 2009-01-07 at 04:32. 

::

   One of my co-worker wrote an implementation the cdb algorithm in pure
   python, I have placed a copy here :  <a href="http://thomas.mangin.com
   /data/source/cdb.py">http://thomas.mangin.com/data/source/cdb.py</a>


Posted by Michael Watkins on 2009-01-07 at 15:26. 

::

   For my own curiosity, I looked at CDB using the Python implementation
   Thomas Mangin linked in above, plus a Python extension module pycdb,
   plus Durus:    Benchmark: return a random choice from the same dict of
   words used to construct the databases...    def doit(): return
   db.get(random.choice(words))    Run 1000 times, several runs in
   succession:    $ python bench_cdb.py   5 runs  Last result:
   autocratrix, elapsed 1.00685787201  Last result: hardbeam, elapsed
   1.05426478386  Last result: Sue, elapsed 0.874281167984  Last result:
   tressful, elapsed 0.722640991211  Last result: Moringaceae, elapsed
   0.718917131424    After my file system cache warmed up (just a run or
   three):  $ python bench_cdb.py   5 runs  Last result: druxiness,
   elapsed 0.303334951401  Last result: heteroclinous, elapsed
   0.256841182709  Last result: resuscitant, elapsed 0.256777048111  Last
   result: entertainer, elapsed 0.244518041611  Last result: sweeping,
   elapsed 0.254623174667    For an all Python solution that's rather
   nice. In comparison if one can afford compiling a module, pycdb offers
   another step up the performance ladder:    5 runs  Last result:
   predoctorate, elapsed 0.0292491912842  Last result: pseudoisatin,
   elapsed 0.0216739177704  Last result: gnaw, elapsed 0.034423828125
   Last result: silkwoman, elapsed 0.0158989429474  Last result:
   superconformist, elapsed 0.0152080059052    (nb: on my system the
   pycdb module wouldn't allow my simple python benchmark to exit to the
   OS prompt, even after raising SystemExit.)    Durus:  $ python
   bench_durus.py  5 runs  Last result: unbeveled, elapsed 1.96095490456
   Last result: tetrarchate, elapsed 1.41660499573  Last result:
   graphoscope, elapsed 1.33317303658  Last result: quail, elapsed
   1.1604487896  Last result: periastral, elapsed 1.21129393578    - this
   remains more or less constant. These accesses are direct via
   FileStorage; if running client/server, the server process uses very
   little RAM; accesses (including writes) can then be read/write. Read
   performance on my overloaded workstation running both client and
   server are about 50 - 60% slower than direct, although if a client
   were do be doing many lookups in the DB, over time you'd expect the
   ClientStorage's cache to be of more use.    File size - same data
   occupies ~ 5X the space...     Note the Durus DB is managing pickled
   Python objects; cdb (at least for the example) is a hash of strings.
   File size has a lot to do with the data being Python objects not dumb
   strings, since dict[2*word] = word and dict[word] = word both point to
   the same "word" object not to copies of strings.    203315388 Jan  7
   10:11 test.cdb   44978765 Jan  7 10:24 test.durus    That might be an
   issue depending on your file system.    Constructing the DB:    I
   created a large dictionary using the same approach in the cdb.py; on
   my system that results in a mapping containing 2,358,800 items.
   Durus was somewhat faster and used a hundred or so megabytes less RAM
   in doing so.     FWIW.


Posted by Anonymous Bastard on 2009-01-08 at 14:33. 

::

   I like CDB; but did you check QDBM?  <a
   href="http://qdbm.sourceforge.net/">http://qdbm.sourceforge.net/</a>
   <a href="http://qdbm.sourceforge.net/benchmark.pdf">http://qdbm.source
   forge.net/benchmark.pdf</a>    &gt; Python version availability: does
   it work for 2.2 on up? What about py3k?  Do not forget you can use it
   with ``dl`` (introduced in Python2.0) or ``ctype`` (Python2.5 and up).
   &gt; scalability: can it scale to gigabytes or 10s of gb of data? 10s
   of millions of records?  I plan to use <a
   href="http://www.pytables.org/">http://www.pytables.org/</a> for
   complex and huge dataset soon.    Let us know your experience!

