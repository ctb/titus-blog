Building test fixtures for PostgreSQL
#####################################

:author: C\. Titus Brown
:tags: python,testing
:date: 2008-01-27
:slug: postgresql-test-fixtures
:category: python


I'm having trouble with some tests of a PostgreSQL-based system.  Briefly,
I have a set of functional tests that

 - create a new database
 - populate it with a data model
 - run a Web server (in-process)
 - test the integrated Web server - database functionality

The tests are now slow enough that I'm averse to writing new ones, so
it's becoming important for me to figure out how to run them faster.

The main time sink appears to be in the fixtures, where I create a new
database.  Actually creating an empty postgres database is *slow*: it
takes 18 seconds (on my server, normally a pretty fast computer...) to
create a new, empty database.

So, how can I get a known-good database in place quickly?

The most obvious route is for me to do dev tests with something small
and fast (sqlite?), but I can't switch to another database system
because I'm using PostgreSQL-specific features.

I poked around the PostgreSQL documentation and tried using `template
databases
<http://www.postgresql.org/docs/8.1/interactive/manage-ag-templatedbs.html>`__
but the problem persists: ``createdb`` is just *slow* to run.

I can't figure out how to build user-accessible snapshots (to which I
could revert after tests...)  and `Point-in-Time-Recovery
<http://www.postgresql.org/docs/8.2/interactive/continuous-archiving.html>`__
is only for superusers; I don't want users to have to be postgresql
superusers to run my tests.

The parameters of the problem:

 - At a minimum, my test fixtures need to (quickly!) construct a
   test-only database with a pre-loaded SQL data model, containing no
   data.

 - Ideally, I would be able to specify a single snapshot and then
   revert to that snapshot at any time.

 - No sysadmin access should be required, and *certainly* no raw filesystem
   manipulations should be required.

Any ideas?  As usual, either comment or `drop me a line
<mailto:titus@idyll.org>`__.

--titus


----

**Legacy Comments**


Posted by Grig Gheorghiu on 2008-01-27 at 21:10. 

::

   Just a thought -- have you tried restoring a pg_dump of a known test
   database, instead of creating it from scratch?     Grig


Posted by Moof on 2008-01-27 at 21:54. 

::

   How about a Drop all and recreate the tables? Is that any faster?
   Or just flushing the tables and resetting the various counters and
   indexes? This is the way Django's ORM works by default, at least
   avoiding the createdb overhead more than once (it still creates a new
   db at the beginning, and drops it after a successful run, but running
   the test suite only causes this to happen once)    But yes, this a
   particular frustration of mine with postgres. Creating the test
   database takes significantly longer than running the tests.


Posted by Jonathan Ellis on 2008-01-27 at 22:50. 

::

   Using a ramdisk seems like the easiest solution, but it sounds like
   that violates your constraint #3.    Greg's idea has merit; if the
   CREATE DATABASE is the problem, don't do it every time. :)  It's
   straightforward to write a pl/pgsql (or pl/python but that would be a
   little clunkier since it's dml-heavy) function to query pg_class for
   existing tables and drop them all before starting to add test data.
   For bonus points you could query for the presence of the database and
   run CREATE only if that is needed.


Posted by Anders Pearson on 2008-01-27 at 23:08. 

::

   18 seconds for createdb to run? It only takes 0.6 seconds on my
   ancient Ubuntu desktop (normally a very slow computer).     Do you
   have a million databases on your system or something? Have you tried
   this on a system that doesn't have many other databases? Or running a
   seperate, testing only instance of PostgreSQL? Is there something
   particularly odd about your PostgreSQL config?     0.6 seconds isn't
   great, but 18 seconds sounds way too slow.


Posted by Titus Brown on 2008-01-28 at 00:09. 

::

   Re trying to "flush" the database: I could end up with an unclean
   starting position that caused bugs and inconsistencies.  But I guess
   it'd run faster :)    Anders, thanks for confirming that it runs
   faster on some people's computers.  I'll look into it.  There's
   nothing unusual about my install, AFAIK; it's actually located on the
   system disk, but I don't think it's an unusually active disk.  I'll
   take a look &amp; benchmark it on some other computers.    Thanks,
   everyone!  I was hoping there'd be a magic solution but these
   suggestions are good starting points :)


Posted by Noah Gift on 2008-01-28 at 07:25. 

::

   Titus/If it helps my work needs to make this quicker as well, maybe we
   can have a late night Sprint on this at PyCon?  I also second what
   Jonathan says, using an in memory version of Postgres could be a huge
   saving in time:    <a href="http://www.redhatmagazine.com/2007/12/12
   /tip-from-an-rhce-memory-storage-on-
   postgresql/">http://www.redhatmagazine.com/2007/12/12/tip-from-an-
   rhce-memory-storage-on-postgresql/</a>    I suppose using an ORM can
   really save your butt sometimes, as you won't get locked into using
   database specific features, and will be able to convert tests to
   SQLite.


Posted by Grig Gheorghiu on 2008-01-28 at 13:17. 

::

   My timings are close to what Anders got:    -bash-3.00$ time echo
   'create database test2' | psql template1  CREATE DATABASE    real
   0m0.492s  user  0m0.002s  sys  0m0.007s    This is on a fairly old
   Dell 1650 server running CentOS 4.4.


Posted by alex v. koval on 2008-01-28 at 14:20. 

::

   IMO, something is wrong with your postgres, here it is:
   alex@appserver ~ $ time echo 'create database test2' | psql template1
   CREATE DATABASE    real  0m0.280s  user  0m0.004s  sys  0m0.004s
   Also, as far I know, Django (a framework which I use) for example, in
   its internal tests does not recreate whole DB, instead it does tables
   flush, its faster this way.


Posted by bignose on 2008-01-29 at 04:24. 

::

   &gt; The most obvious route is for me to do dev tests with something
   small and fast (sqlite?), but I can't switch to another database
   system because I'm using PostgreSQL-specific features.    That's a bad
   code smell: If you need to do lots of tests against an actual
   PostgreSQL instance, then your code is too tightly coupled to
   PostgreSQL.    Instead, those PostgreSQL-specific features should be
   abstracted away behind a very narrow layer in your code. Only that
   layer actually needs to have a real PostgreSQL instance to test
   against; the rest of the code should be tested against the interface,
   using test doubles (stubs, mocks, etc.) instead of the real code that
   implements the PostgreSQL-specific features.


Posted by Titus Brown on 2008-01-29 at 05:46. 

::

   bignose -- I disagree, for a few reasons.    First, to all intents and
   purposes, my application is a thin Web presentation layer on top of a
   database.  Introducing another layer of complexity for the purpose of
   better testing violates the KISS principle.  (If I had some **other**
   use for that layer, there'd be a reason; I don't, at the moment.)
   Second, the PostgreSQL specific features are central to the app;
   that's not necessarily good, but I've been able to dramatically
   simplify my codebase by doing that.  On balance, it's been positive.
   Third, I have this weird desire to actually test the application; I
   don't think unit tests are as useful for Web apps as are functional
   tests, because of the layering issue I mentioned above.    ...but
   thank you for bringing it up.  It is an interesting perspective and I
   haven't had to actively defend my design to anyone, so I appreciate
   the comment ;).    There are some interesting posts I've seen about
   the merits of trying to become database-agnostic; how many people
   really need to switch between (say) PostgreSQL and MySQL?  I haven't
   really decided one way or another, but the need to test things
   flexibly is making me lean towards database agnosticism.    Ultimately
   I intend to rewrite the app to use SQLAlchemy, but that is
   unfortunately not something I have time to do soon :(  Which actually
   speaks again to your point -- whether or not my original design is
   good, I'm stuck with it now and need to solve proximal problems first!
   It's a moderately large app and I won't be rewriting it from scratch
   any time soon.    thanks again,  --titus


Posted by Christoph Zwerschke on 2008-01-29 at 07:49. 

::

   As others have already noted, a createdb should really run much
   faster. You can also try running pg_restore with the "-c" option
   instead of dropping and recreating the database. Another idea is to
   shut down the database, copy your complete database cluster on the
   level of the file system, and restart the database again.


Posted by bignose on 2008-01-29 at 17:46. 

::

   &gt; Third, I have this weird desire to actually test the application
   I don't think it's weird, it's quite essential. I'm not sure why you
   make this point.    &gt; I don't think unit tests are as useful for
   Web apps as are functional tests    I think unit tests are very useful
   for **any** code. TDD and all that; write the tests at the time of
   designing the implementation, make each unit tests very focussed in
   its fixtures and assertions (thus fast), and run the entire unit test
   suite continually during development.    However, I missed the mention
   in the opening paragraph that these are functional, not unit, tests.
   :-)    Given that, why is it a problem for the functional test suite
   to take a bit of time? The functional tests of the entire application
   stack will necessarily invoke many subsystems that might be slow. This
   might point to performance issues, but certainly doesn't indicate
   shortcuts need to be taken in the tests themselves.    You shouldn't
   expect the functional tests to execute as quickly as the unit tests,
   nor expect to be able to run them continually after every change the
   way you do with unit tests.    Rather, the functional test suite
   should be run every time you commit a change to version control, or
   some other less-frequent-than-always event.


Posted by Titus Brown on 2008-01-30 at 02:01. 

::

   Re "weird desire", unit tests don't do a good job of testing the
   actual application; they test units of code.  If you are mainly
   slinging information about (and not manipulating it), I don't find
   them all that useful.  (I have unit tests built into the libraries
   that my app **relies** on, of course, and they're great there.)    I
   want to speed up the functional tests because they're reducing my
   velocity of development.    --titus

