w4s - tech I'd like to invest in
################################

:author: C\. Titus Brown
:tags: open science,webmaking,w4s
:date: 2012-11-13
:slug: w4s-tech-wanted
:category: science


This is one of a bunch of posts on science and the Web.  `Start here
<../w4s-overview.html>`__ for an overview.

----

I don't think I can devote myself to any big projects, but I do
have a bunch of ideas for relatively small projects that I think
could lead to worthwhile change.

Here are some things I'm thinking about working on --

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
   hack to make use of the figshare API to suck down a blog entry to
   figshare, "freeze" it, and post the DOI to the original blog entry.

   This would enable a community of opinionated microcontributions,
   each of which is citable (and versioned).

   And once you can blog executable notebooks, well, there you go!

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
   set of trusted users delegate trust transitively.  This distributes
   the effort of validating real users, and leaves spammers dead in the
   water.  (I'm honestly not sure why more sites don't use this kind
   of thing.)

   The main problem I see with applying advogato's trust metric
   implementation to science is that there probably shouldn't be a
   single set of key trusted users; rather, I'd want to recenter the
   trust network around a set of people *I* choose.  Making this
   all work fluidly would be a challenge, but I don't think it's
   an impossible one.

   This one is a bit ambitious and open-ended, but I think there might
   be simple ways to leverage blogs and pre-existing social networks
   to build this automatically - like klout, but less stupid.  Mozilla
   `appears to be thinking about how to bring badges into it
   <http://carlacasilli.wordpress.com/2012/08/24/mozilla-open-badges-building-trust-networks-creating-value/>`__,
   which is another approach.

6. Hack together ways to collect bloggish interactions along with
   other online interactions into a single view of a scientist, much
   like `INSPIRE <http://inspirehep.net/>`__ has helped integrate
   arXiv into reputation metrics in particle physics, and PLoS One and
   altmetrics are bringing social networking and publication together.
   (Google Scholar is doing an interesting job with this, too, although
   I'm not sure what their long term goal is.)

--titus
