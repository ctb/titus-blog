Posting blog entries to figshare
################################

:author: C\. Titus Brown
:tags: blog,webmaking,figshare
:date: 2012-11-22
:slug: posting-blog-entries-to-figshare
:category: science

Just over a week ago, I `posted a list of wanted tech
<http://ivory.idyll.org/blog/w4s-tech-wanted.html>`__ that I thought
would help further open science.  One item that struck a chord with
a number of people on Twitter and in the comments was the idea
of giving blog entries a DOI:

  4. An easy way to copy blog posts to figshare and give them DOIs.

   Seriously, why hasn't this already been done?  It should be a short
   hack to make use of the figshare API to suck down a blog entry to
   figshare, "freeze" it, and post the DOI to the original blog entry.
   
   This would enable a community of opinionated microcontributions,
   each of which is citable (and versioned).
   
   And once you can blog executable notebooks, well, there you go!

Today (Thanksgiving in the US) I was sitting around in full work-avoidance
mode and I thought I'd give the basic idea a whirl.

The goal: hack together a script to take a blog post of mine, post it
to figshare, and get a DOI.

Some background -- what is figshare?
------------------------------------

`figshare <http://figshare.com>`__ is a site that enables users to
post "stuff", including data; make it publicly available; and assign a
`Digital Object Identifier (DOI) <http://www.doi.org/>`__ to it.  This
makes the object citeable.

figshare is meant to make things *other* than peer-reviewed or
"officially" published papers citeable -- data, negative results,
posters, grants, etc.

First -- is this OK?
--------------------

Scott Edmunds `asked <http://ivory.idyll.org/blog/w4s-tech-wanted.html#comment-710728518>`__ whether blog posts belonged on figshare.  I didn't know, and I poked around, and couldn't find an answer, so `I asked @figshare on Twitter <https://twitter.com/ctitusbrown/status/271754689123602432>`__:

   Hey @figshare, any incite on @SCEdmunds comment differentiating
   between data and publication DOIs? see:
   http://ivory.idyll.org/blog/w4s-tech-wanted.html#comment-710728518
   …

(The 'incite' was not a pun, it was a misspelling; I'm getting old. Sigh.)

@figshare `responded <https://twitter.com/figshare/status/271758341913604097>`__:

   @ctitusbrown Not sure why we'd treat any digital object
   (identifier) any different if we want data to be a first class
   research output.

Answer: yes.

Second -- does a basic hack work?
---------------------------------

`Yes, it does <http://figshare.com/articles/Test_blog_post/97901>`__.
That link points to my w4s-tech-wanted.rst source.

Note a few things.

- I tagged it as 'blog'.  This seems like a good tag for blog posts hosted on figshare, right? :)

- I made it a defined type of 'paper'.  Sure.

- It's in reStructuredText (the source format for this blog), which
  figshare doesn't render -- that's ok, it's pretty readable.

- I added links to both the github source and the rendered full URL
  on my Web site.

- there is a DOI, http://dx.doi.org/10.6084/m9.figshare.97901 (but it
  doesn't work yet -- presumably there's some latency between making
  things public and updating the DOI resolution mechanism (?)

- figshare does version things; some of the commentary on Twitter and
  on my blog post was wondering what would need to happen 

This was all done via the figshare `API documentation for Python
<http://api.figshare.com/docs/demo_python.html>`__.

Third -- what was frustrating?
------------------------------

I ran into all sorts of minor little inconveniences; nothing that a little
trial and error couldn't fix, but still annoying.

- figshare doesn't tell you what you need to set before making something
  public, so I had to just try a bunch of stuff.

  The answer seems to be: in addition to a title and an author, you
  need a defined type, a category, a tag, and a data file to be set.

- figshare doesn't provide a simple way to get a list of all
  available defined types or categories, so I had to go through the
  Web interface to figure out what was available.  Bleargh.

- when adding links, figshare doesn't like 'https' links -- it thinks
  they're invalid.  Didn't test ftp etc.

Concluding thoughts and questions
---------------------------------

On the whole, it was pretty easy to use the figshare API. It could be
made easier and more straightforward, of course, but for anyone who
has done any programming at all it's good and simple.  The biggest
lack IMO is a single page outlining everything I listed above in "what
was frustrating"...

I'm not sure that posting the source for a blog post is the way to go,
but I can't think of a good alternative.  So I will provisionally say
that posting the source and then linking to the rendered view (with
comments etc.) is a good minimum standard.  But what should we do with
people who don't *have* source?  I'm not sure what internal blogging
formats are in use out there... seems like at the worst you could post
the HTML... is that bad?

Is there any way to post software/source code to figshare?  That'd be
cool.  Maybe a new defined_type?

I'd love to have figshare provide a reStructuredText and Markdown
viewer directly on their site, the way they do with PDFs.

A tour of figshare (not a video, but a text tour) would be nice.
After banging on it for a bit I can infer a lot, but I still don't
really understand what it's officially for, where they're planning on
going, what features I should be making use of, etc. etc.  To the
extent that they themselves know, it would be nice to get a single
page summary.

What's next?
------------

Buggered if I know.  I'm not actually sure what is the logical next
step.  Suggestions, anyone? I can write a script to post my reST
directly to figshare easily enough, and I could then provide a
DOI/citation handle on each blog post... any other thoughts?

--titus
