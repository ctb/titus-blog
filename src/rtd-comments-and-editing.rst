Adding disqus, Google Analytics, and github edit links to ReadTheDocs sites
###########################################################################

:author: C\. Titus Brown
:tags: python,rtd,disqus,github
:date: 2012-11-04
:slug: rtd-comments-and-editing
:category: python

Inspired by the awesomeness of disqus on my other sites, I wanted to
make it possible to enable disqus on my sites on `ReadTheDocs
<http://readthedocs.org>`__.  A bit of googling led me to Mikko
Ohtamaa's excellent work on `the Plone documentation
<http://opensourcehacker.com/2012/01/08/readthedocs-org-github-edit-backlink-and-short-history-of-plone-documentation/>`__,
where a blinding flash of awesomeness hit me and I realized that
github had, over the past year, `nicely integrated online editing of
source, together with pull requests
<https://github.com/blog/905-edit-like-an-ace>`__.

This meant that I could now give potential contributors completely
command-line-free edit ability for my documentation sites, together
with single-click approval of edits, and automated insta-updating of
the ReadTheDocs site.  Plus disqus commenting.  And Google Analytics.

I just had to have it.

`Voila <https://labibi.readthedocs.org/en/latest/>`__.

Basically, I took Mikko's awesomeness, combined it with some disqus hackery,
refactored a few times, and, well, posted it.

The `source is here <https://github.com/ctb/labibi>`__.

Two things --

I could some JS help disabling the 'Edit this document!' stuff if the
'github_base_account' variable isn't set in page.html'.  Anyone?  See
`line 105 of page.html <https://github.com/ctb/labibi/blob/master/_templates/page.html#L105>`__.  You can edit online by hitting 'e' :).

It would be nice to be able to configure disqus, Google Analytics, and
github editing in conf.py, but I wasn't able to figure out how to pass
variables into Jinja2 from conf.py.  It's probably really easy.

But otherwise it all works nicely.

Enjoy!  And thanks to Mikko, as well as Eric Holscher and the RTD team,
and github, for making this all so frickin' easy.

--titus
