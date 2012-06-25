Naive Lazyweb Question: Programmatic Form Editing
#################################################

:author: C\. Titus Brown
:tags: python
:date: 2007-11-29
:slug: naive-lazyweb-question-about-forms
:category: python


Dear lazyweb,

I would like to be able to write Python code like the following: ::

  page_obj = parse(html_code)

  form_obj = page_obj.forms[0]
  
  form_obj.my_name = 'bob'
  form_obj.my_select.choose('option2')

  new_html_code = page_obj.emit_html()

That is, we have an *existing* HTML form, and I would like to be able
to parse it, programmatically update the form settings, and then emit
it again as HTML with the same style attributes, etc., but with updated
form data.

(I'm horrendously out of date with HTML libraries in Python, so I thought
I'd just ask... ;)

thanks,

--titus



----

**Legacy Comments**


Posted by Jacob Kaplan-Moss on 2007-11-29 at 18:51. 

::

   I haven't looked too deeply into it, but it looks like htmlfill
   (http://formencode.org/htmlfill.html) will do what you want.


Posted by A Different Jacob on 2007-11-29 at 23:00. 

::

   htmlfill addresses this specific problem very directly, but I believe
   it uses the standard library's HTMLParser module, which is not up to
   the task of dealing with much real-world html.  I suggest
   lxml.etree.HTML, optionally in conjunction with lxml.objectify.


Posted by Ian Bicking on 2007-11-30 at 00:23. 

::

   Yes, htmlfill does exactly that.  I also implemented that in
   lxml.html: <a href="http://codespeak.net/svn/lxml/trunk/doc/lxmlhtml.t
   xt">http://codespeak.net/svn/lxml/trunk/doc/lxmlhtml.txt</a>
   (unfortunately the generated docs don't seem to be up to date, and so
   don't include information on forms).  With that you can do
   page_obj.forms[0].fields = request_dict


Posted by Max Ischenko on 2007-11-30 at 03:41. 

::

   I think Beautiful Soup does this, see <a href="http://www.crummy.com/s
   oftware/BeautifulSoup/documentation.html">http://www.crummy.com/softwa
   re/BeautifulSoup/documentation.html</a>.


Posted by Martijn Faassen on 2007-11-30 at 11:56. 

::

   Mechanize can do this. zope.testbrowser builds on top of this to
   integrate it into doctests for testing purposes.    <a href="http://py
   pi.python.org/pypi/mechanize">http://pypi.python.org/pypi/mechanize</a
   >    <a href="http://pypi.python.org/pypi/zope.testbrowser">http://pyp
   i.python.org/pypi/zope.testbrowser</a>


Posted by Titus Brown on 2007-11-30 at 14:12. 

::

   Martijn, I'm pretty sure mechanize can't do this; ClientForm doesn't
   re-emit the HTML AFAIK.    BeautifulSoup, hmm, for some reason didn't
   think it could either.  Will have to check.    htmlfill looks perfect.
   thanks!    --titus


Posted by Dan on 2007-11-30 at 15:35. 

::

   Beautiful Soup will certainly do it.e.g:    from BeautifulSoup import
   BeautifulSoup  soup=BeautifulSoup(originalhtml)
   soup.find('input',attrs={'name':'somename')['value']="New Value"
   newhtml=soup.renderContents()

