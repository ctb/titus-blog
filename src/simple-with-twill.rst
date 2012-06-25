This is simple with twill
#########################

:author: C\. Titus Brown
:tags: python,twill
:date: 2007-02-12
:slug: simple-with-twill
:category: testing


I don't feel like I need to "defend" `twill
<http://twill.idyll.org/>`__ -- it's successful beyond both my
expectations and my cognizance (I have no idea who's actually using
it, but it's apparently a lot of people!), but I may need to promote
it better.  I ran across `this post
<http://www.answermysearches.com/mechanize-useful-tips/229/>`__
earlier today.  It shows how you can use mechanize to do some simple
"screen scraping," and it spurred me to check the following scripts
into a new "advocacy" section of the twill archive.

Here's how you can use a twill script to do what Greg did with mechanize: ::

   add_extra_header User-Agent "Mozilla/5.0 (compatible; MyProgram/0.1)"
   go http://www.python.org/
   show

You can also use straight Python, if that's your poison: ::

   from twill.commands import *
   import twill

   add_extra_header('User-Agent', 'Mozilla/5.0 (compatible; MyProgram/0.1)')
   go("http://python.org/")
   html = twill.get_browser().get_html()
   print html

Note that twill is based on mechanize, and so promoting twill doesn't
mean pushing mechanize down.  mechanize is amazingly powerful -- but
sometimes you want to just go grab some HTML, and twill (tries to)
make that *easy*.

One unexpected result of all this -- I discovered that the function
``get_browser()`` wasn't actually exported from ``twill.commands`` by
default, which is silly.  It's the first function I wanted to call in
order to do something minimally complex.  So now the API is one call
bigger ;).  One more corner rubbed off...

--titus


----

**Legacy Comments**


Posted by Diane on 2007-02-13 at 17:30. 

::

   $ easy_install twill  ...  $ ipython  In: from twill.commands import *
   In: import twill  In: go("http://google.com")  In: html =
   twill.get_browser().get_html()  In: html  Out: ''  In:
   twill.<em>_version_</em>  Out: '0.8.5'    Somehow I think there's
   supposed to be some data in that html variable?    Also the version of
   twill obtained via easy_install doesn't have 'add_extra_header'.
   Finally why is there twill.commands.get_browser() and
   twill.get_browser()


Posted by Titus Brown on 2007-02-14 at 03:34. 

::

   Now that's just mean, pointing out that I haven't made a release in a
   while ;)    twill.commands.get_browser implements twill.get_browser.
   The other functions are all available in the latest version of twill.
   --titus

