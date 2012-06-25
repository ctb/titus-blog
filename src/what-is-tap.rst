What is TAP?
############

:author: C\. Titus Brown
:tags: testing,perl
:date: 2006-09-18
:slug: what-is-tap
:category: misc


Apparently the Perl community is `crying out for testing tools on par
with other languages`_.  That's cool.  I think it'd be neater if I could
figure out what `TAPx::Parser`_ did, though.

.. _crying out for testing tools on par with other languages: http://use.perl.org/~Ovid/journal/31009?from=rss

.. _TAPx::Parser: http://search.cpan.org/dist/TAPx-Parser/


----

**Legacy Comments**


Posted by Ovid on 2007-01-26 at 18:06. 

::

   Basically, it cleanly separates the parsing, interpreting, and
   presenting of test data.  Currently, Test::Harness does not, and
   can't, do that.  Hence, TAPx::Parser.  This gives us the freedom to
   extend the testing tools any way we like rather than the current "one
   size fits all".

