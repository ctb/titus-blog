w4s - tech I'd like to invest in
################################

:author: C\. Titus Brown
:tags: open science,webmaking
:date: 2012-11-04
:slug: w4s-tech-wanted
:category: science
:status: draft

If someone gave me a worry-free salary for a year and told me to
change the world of online science for the better, what would I
work on?

1. A better lightweight process for contributing to materials online.

   The open source world has done a fantastic job of creating an open
   and relatively easy process for contributing to software; the
   transition to distributed version control pretty much sealed the
   deal by making forking and branching a permission-free process.
   But this effectiveness has not really extended to collaborative
   work on documentation and online materials, which shouldn't
   require as much technical expertise as software development -- but
   currently does.

   Wikipedia is the counterexample that proves the rule -- Wikipedia
   is a heavily managed world-wide process that is increasingly
   bureaucratic and staid, with an in-group that manages
   contributions.  It's pretty awesome, but it doesn't scale very well
   to other projects; wikis always require maintenance and the right
   cultural process, to the point where I simply don't use them for
   classes or collaborations.

   I'd love to see the process simplified, which is why I invested an
   hour or two in `mashing up github editing and ReadTheDocs
   <http://ivory.idyll.org/blog/rtd-comments-and-editing.html>`__
   based on some inspiring Plone work.  It's still a bit clunky, but I
   think this kind of thing could be a revolution in online
   collaboration for text.

2. Posting/hosting ipython notebooks publicly, in a sandbox, with easy
   forking.

   I really, really want to provide a lightweight way for scientists
   to provide data + code that other scientists could fork, modify,
   and repost easily.  Think of it like github but with data and CPU :).
   Or, storify, but with forking and serious execution horsepower behind
   it.

3. Storify-style forking of ipython notebooks to enable parameter tweaking
   and interactive changes to visualization strategies, in support of
   citizen science and science journalism.

   This is really an extension of the previous one, but -- speaking of
   `storify <http://storify.com>`__, wouldn't it be nice to be able to
   have a storify-like Web interface for ipython notebook that would
   let you take someone's published analysis pipeline, tweak it to
   apply to your own data or to highly an otherwise unnoticed detail,
   and republish it?  With a nice storify-like interface?

   Just think -- non-pro scientists could explore the data analysis in your
   paper!  High school kids could test alternate assumptions!  Journalists
   could write articles based on your actual data!
   
3. An easy way to copy blog posts to figshare and give them DOIs.

   Seriously, why hasn't this already been done?  It should be a short
   hack to make use of the storify API to suck down a blog entry to
   figshare, "freeze" it, and post the DOI to the original blog entry.

   This would enable a community of opinionated microcontributions,
   each of which is citable.

4. Tech to sweep your local disk for papers + DOIs, so that you can
   (selectively) start to network based on shared paper collections.

   Wouldn't it be awesome to find new papers based on what you have
   on your hard disk?  Or globally figure out which papers are actually
   kept my people?  At the very least it would be an alternative way
   to measure impact.

   You could even set up scientist dating sites to find people with
   matching or complementary sets of papers...

5. Build tools to construct trust networks from existing data and then
   "recenter" or personalize the global trust network around your own
   links.

   I've been a long-time member of the `advogato
   <http://advogato.org>`__ site, a community blogging and discussion
   site which has high page rank in Google and absurdly low amounts of
   spam.  I'm pretty sure that it's because of their `trust metric
   <http://www.advogato.org/trust-metric.html>`__, which lets a key
   set of trusted users delegate trust transitively.

   The main problem I see with applying advogato's trust metric
   implementation to science is that there probably shouldn't be a
   single set of key trusted users; rather, I'd want to recenter the
   trust network around a set of people *I* choose.  Making this
   all work fluidly would be a challenge, but I don't think it's
   an impossible one.

6. Twitter, but open.

   Twitter is great, but their terms of service are too restrictive
   for really maximizing its scientific potential.  Ideally I'd like
   to be able to integrate twitter and other social networking stuff
   into one gigantic ball of wax, or, even better, many *different*
   balls of wax.

   I'm ambivalent about this one -- it could be a gigantic waste of
   time and effort.  Twitter works pretty well in certain communities
   already...

7. A better/more open Dropbox.  Or git/github for data.

   'nuff said.  Dropbox is great -- simple, straightforward, and easy.
   It makes sharing stuff easy.  But it doesn't really track provenance,
   which is something we want to do.  Kinda like github.  But, you know,
   for data.

--titus
