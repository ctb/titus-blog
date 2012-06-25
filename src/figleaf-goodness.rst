Some figleaf goodness
#####################

:author: C\. Titus Brown
:tags: python,figleaf
:date: 2007-02-16
:slug: figleaf-goodness
:category: python


Yesterday for our `SoCal Piggies meeting
<http://www.socal-piggies.org/scp>`__ I whipped up something I'd been
thinking about doing for a while: sectioning in figleaf recording.  (`figleaf
<http://darcs.idyll.org/~t/projects/figleaf/README.html>`__ is my
package for Python code-coverage analysis.)

It's easier to show than to explain, but briefly, I added two new
functions to figleaf: ::

   figleaf.start_section(name)

   figleaf.stop_section()

What these functions let me do is define a name with which code coverage
can be associated.  The goal is to determine what part of your code is
calling some other part of your code; the explicit example I had in mind
is unit testing, where it can be helpful to know which lines of code are
being executed by which unit test.

It took me but a moment to add a 'figleaf-sections' plugin to `pinocchio <http://darcs.idyll.org/~t/projects/pinocchio/doc/>`__, my extensions for `nose <http://somethingaboutorange.com/mrl/projects/nose/>`__.  This plugin wraps each function and method test with section coverage reporting.  Again, it's easier to show than to explain, so here is some sample output: ::

    -- all coverage --
    | test_sections.test_one
    | | test_sections.TestTwo.test_three
    | | | test_sections.TestTwo.test_four
    | | | | 

    +         | def setup():
    +         |     print 'howdy'
              | 
    +         | def teardown():
    +         |     print 'bye!'
              | 
    +         | def test_one():
    + +       |     assert 1 == 1
              | 
    +         | class TestTwo:
    +         |     def setup(self):
    +   + +   |         assert "setup" == "setup"
              |         
    +         |     def test_three(self):
    +   +     |         assert 2 == 2
              | 
    +         |     def test_four(self):
    +     +   |         assert 3 == 3
              | 
    +         |     def teardown(self):
    +   + +   |         assert "teardown" == "teardown"

The '+' marks in the first column represent combined code coverage;
this *includes* all coverage sections (as well as stuff that's
executed outside of section coverage).  The marks in the second,
third, and fourth columns represent the lines of code executed by the
individual nose tests, indicated at the beginning of the output.

Here you see that (as expected) the ``setup()`` and ``teardown()``
functions are executed outside the context of any test; ``test_one()``
is executed individually; and the class fixtures,
``TestTwo.setup(self)`` and ``TestTwo.teardown(self)``, are executed
for *both* ``test_three(self)`` and ``test_four(self)``.  (The function
definitions are executed on module import, of course, and hence lie
outside the coverage sections defined by my nose plugin.)
Neat, eh?

It's even more fun to run this on *real* code.  Here's part of
twill's ``commands.py`` file, which is touched by many (most!) of
the twill tests.  You can see a sort of barcode of tests for each
function; the ``go(url)`` function is obviously pretty important,
and it's nice to see that even in the case of the ``code(n)`` function,
at least one of my tests checks that the assertion is raised properly. ::

                                                          | 
    +                                                     | def exit(code="0"):
                                                          |     """
                                                          |     exit [<code>]
                                                          | 
                                                          |     Exits twill, with the given exit code (defaults to 0, "no error").
                                                          |     """
    +         +       +                                   |     raise SystemExit(int(code))
                                                          | 
    +                                                     | def go(url):
                                                          |     """
                                                          |     >> go <url>
                                                          |     
                                                          |     Visit the URL given.
                                                          |     """
    + + + + +   + + + + + + + + + + + + + + + + + + + +   |     browser.go(url)
    + + + + +   + + + + + + + + + + + + + + + + + + + +   |     return browser.get_url()
                                                          | 
    +                                                     | def reload():
                                                          |     """
                                                          |     >> reload
                                                          |     
                                                          |     Reload the current URL.
                                                          |     """
    +           +             +               +     +     |     browser.reload()
    +           +             +               +     +     |     return browser.get_url()
                                                          | 
    +                                                     | def code(should_be):
                                                          |     """
                                                          |     >> code <int>
                                                          |     
                                                          |     Check to make sure the response code for the last page is as given.
                                                          |     """
    +       +   + +   + + + + +                     + +   |     should_be = int(should_be)
    +       +   + +   + + + + +                     + +   |     if browser.get_code() != int(should_be):
    +                 +                                   |         raise TwillAssertionError("code is %s != %s" % (browser.get_code(),
                                                          |                                                         should_be))

Note that you get a kind of barcode of code execution, which is nifty.

Anyway, I think this functionality is incredibly neat, but then again
I'm a sucker for my own code ;).  It seems like it is more useful for
what I would call "forensic code analysis," i.e. trying to understand
what other people's code is *doing*, than it is for direct testing and
analysis of your own code.  Forensic code analysis is very useful, but
it's difficult to sell because it's removed from what most programmers
seem to think about.  Or am I wrong?

I have some more code to write before I decide on its ultimate
usefulness -- I'd like to be able to dissect *exactly* what code is
run by *precisely one test*, and that's the next feature I'll add.
I'm probably going to turn this into a lightning talk for PyCon, too;
more on that at PyCon.

If you think you have a use for this, please let me know in the
comments.  I'm actively looking for use cases!  And if you're interested
in trying it out, you should be able to do something like this: ::

   easy_install http://darcs.idyll.org/~t/projects/figleaf-latest.tar.gz

   # go to your test directory, and then:
   wget http://darcs.idyll.org/~t/projects/pinocchio-latest.tar.gz
   tar xzf pinocchio-latest.tar.gz
   easy_install pinocchio-latest

   nosetests --with-figleafsections
   figleaf-latest/annotate-sections.py .figleaf <pyfile1> <pyfile2> ...
   
(You need to have nose installed already, of course.)

--titus


----

**Legacy Comments**


Posted by Paul McGuire on 2007-04-30 at 13:46. 

::

   Here is another code coverage display, with a similar "bar-graph"
   coverage timeline.    <a
   href="http://www.visophyte.org/blog/2007/04/25/the-beginnings-of-a
   -gdb-execution-trace-
   visualization/trackback/">http://www.visophyte.org/blog/2007/04/25
   /the-beginnings-of-a-gdb-execution-trace-visualization/trackback/</a>
   (uses pyparsing internally to crack some of the gdb messages).    --
   Paul

