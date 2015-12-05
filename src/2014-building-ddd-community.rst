Putting together an online presence for a diffuse academic community - how?
###########################################################################

:author: C\. Titus Brown
:tags: dddi,ddd
:date: 2014-10-05
:slug: 2014-building-ddd-community
:category: python

I would like to build a community site.  Or, more precisely, I would
like to recognize, collect, and collate information from an already
existing but rather diffuse community.

The *focus* of the community will be academic data science, or "data
driven discovery".  This is spurred largely by the recent selection of
the `Moore Data Driven Discovery Investigators
<http://ivory.idyll.org/blog/2014-moore-ddd-investigators.html>`__, as
well as the earlier Moore and Sloan `Data Science Environments
<http://blog.fperez.org/2013/11/an-ambitious-experiment-in-data-science.html>`__,
and more broadly by the recognition that `academia is broken when it
comes to data science
<https://jakevdp.github.io/blog/2014/08/22/hacking-academia/>`__.

So, where to start?

For a variety of reasons -- including the main practical one, that
most academics are not terribly social media integrated and we don't
want to try to force them to learn new habits -- I am focusing on
aggregating blog posts and Twitter.

So, the main question is... how can we most easily collect and
broadcast blog posts and articles via a Web site?  And how well
can we integrate with Twitter?

First steps and initial thoughts
--------------------------------

Following Noam Ross's suggestions in the above storify, I put together
a WordPress blog that uses the RSS Multi Importer to aggregate RSS
feeds as blog posts (hosted on `NFSN
<http://nearlyfreespeech.net>`__).  I'd like to set this up for the
DDD Investigators who have blogs; those who don't can be given
accounts if they want to post something.  This site also uses a
Twitter feed plugin to pull in tweets from `the list of DDD
Investigators <https://twitter.com/NotMooreFound/lists/dddi>`__.

The resulting RSS feed from the DDDI can be pulled into a `River of
News <http://river4.smallpict.com/2014/06/04/welcomeToRiver4.html>`__
site that aggregates a much larger group of feeds.

The WordPress setup was fairly easy and I'm going to see how stable it
is (I assume it will be very stable, but *shrug* time will tell :).
I'm upgrading my own hosting setup and once that's done, I'll try
out River4.

Next steps and longer-term thoughts
-----------------------------------

Ultimately a data-driven-discovery site that has a bit more
information would be nice; I could set up a mostly static site, post
it on github, authorize a few people to merge, and then solicit pull
requests when people want to add their info or feeds.

One thing to make sure we do is track only a portion of feeds for
prolific bloggers, so that I, for example, have to tag a post
specifically with 'ddd' to make it show up on the group site. This will
avoid post overload.

I'd particularly like to get a posting set up that integrates well
with how I consume content.  In particular, I read a lot of things via
my phone and tablet, and the ability to post directly from there --
probably via e-mail? -- would be really handy.  Right now I mainly
post to Twitter (and largely by RTing) which is too ephemeral, or I
post to Facebook, which is a different audience.  (Is there a good
e-mail-to-RSS feed?  Or should I just do this as a WordPress blog with
the `postie plug-in <https://wordpress.org/plugins/postie/>`__?)

The same overall setup could potentially work for a Software Carpentry
Instructor community site, a Data Carpentry Instructor community site,
trainee info sites for SWC/DC trainees, and maybe also a
bioinformatics trainee info site.  But I'd like to avoid anything
that involves a lot of administration.

Things I want to avoid
----------------------

Public forums.

Private forums that I have to administer or that aren't integrated
with my e-mail (which is where I get most notifications, in the end).

Overly centralized solutions; I'm much more comfortable with light
moderation ("what feeds do I track?") than anything else.

----

Thoughts?

--titus
