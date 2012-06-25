What's in it for me?  Thoughts on open science.
###############################################

:author: C\. Titus Brown
:tags: science,science20
:date: 2010-12-23
:slug: whats-in-it-for-me
:category: science


If you've been under a rock (or `indulging in arsenic yourself
<http://xkcd.com/829/>`__), you've heard about NASA's "arsenic"
article, claiming the discovery of a microbial species that can
substitute arsenate for phosphate.  The paper was pre-announced via
a press conference that then announced the results.

Immediate blogtastrophe!  The paper was critically reviewed in the
blogosphere by a lot of people; I'm particularly fond of `Rosie
Redfield's
<http://rrresearch.blogspot.com/2010/12/arsenic-associated-bacteria-nasas.html>`__
Moreover, NASA has not covered itself in glory in its responses,
claiming that blog reviews are not worth responding to, even when done
by practicing scientists.

The Guardian has an article by Martin Robbins `summing up much of the
ensuing commentary
<http://www.guardian.co.uk/science/the-lay-scientist/2010/dec/08/2?CMP=twt_gu>`__,
which boils down to some variation on "this paper should not have been
published in Science", or "reviewer fail".

I found the Guardian article interesting, and I wanted to particularly
comment on one of the concluding paragraphs:

    At almost every stage of this story the actors involved were
    collapsing under the weight of their own slavish obedience to a
    fundamentally broken... well... 'system' is the right word, but I
    find myself toying with 'ideology'.

It's almost an article of faith online (blogs, twitter, yada) that
many venerable academic institutions, including peer review and the
whole scientific publication model, are `basically broken
<http://cameronneylon.net/blog/peer-review-what-is-it-good-for/>`__ .
I don't disagree, although I'm hardly an expert.  But I do have a
comment, or rather a question, that I think is pertinent to the
discussion of how to improve science through blogging, online peer
review, and other methods of openness.

**What's in it for me?**

More generally, why should Dr. Jane Random Researcher invest any time
or effort into blogging (and responding to other bloggers), writing
good software, or anything else?  What good does it do her?  Is online
networking just another (still rather poor) social networking tool?

I don't think you can use the arsenic paper as an argument for peer
review in the blogosphere.  The only reason we noticed the arsenic
paper was that it was a .1-percenter: fascinating results with
significant implications, hyped to high heaven by NASA, and reviewed
quite visibly by a number of serious scientists.  If the paper hadn't
been publicized as heavily, little or none of the online stuff would
have matter.  As it is, I can virtually guarantee that the first
author is not going to be able to ride the glory of a Science paper
into a faculty position, because *everyone* knows about the
controversy now.  But that's this paper, not the other thousands that
will be published this year (hundreds in Science alone).

This is the problem with the online world for scientists: there's no
real systematized incentive to any of this online stuff.  And that
makes it really tough.  I'm going through Reappointment right now
(that's where you fill in a lot of little boxes tallying your papers,
grants, teaching, and other stuff, so that your university can decide
if you're worth keeping on for another few years).  Nowhere on there
is there a place for "influential blog posts" -- how would you measure
that, anyway?  Same with software -- I listed my various software
releases on the "scientific products" page of the form, and have since
been asked to describe and discuss the impact of my software.  Since I
don't track downloads, and half or more of the software hasn't been
published yet and can't easily be cited, and people don't seem to
reliably cite open source software anyway, I'm not sure how to
document the impact.

So, why do I release software, or blog?  Well, I do what little I do
because I like it.  Personally, I'm ideologically bent towards
openness: open source, open science, open review, etc.  And I'm
willing to spend some of my time investing in it, writing about it,
and otherwise trying to practice it.  And I've managed to make it work
for me reasonably well, at least so far; more on that in future blog
posts.

Having an identifiable incentive structure, however, is important.  If
you want people in general to change, you need to be able to show them
that there's some gain in it for them - not monetary (no scientist I
know is in it for the money) but economic in the academic sense.
**This boils down to cold hard grant cash & publications.** Why?
Because that's what the hiring, reappointment, promotion and tenure
committees care about, so that's how you get and keep jobs -- and it's
awfully hard to do research without a job.

The notion that publicizing your science leads to `scientific fame and
fortune
<http://scienceofblogging.com/scientists-publicizing-your-research-gets-you-cited-more-often/>`__
is silly.  The idea that additional citations is "a tangible benefit"
is nonsense.  The only "tangible benefit" that junior scientists care
about is more time, more grants, and more publications.  Writing blogs
publicizing your own research is generally not going to help with
that; rather, it's going to reduce the time you get to spend on doing
science.

So how do you go from "online" to "grants and pubs"?

I don't know of any robust mechanisms for converting online
reputation, from blogging or software release, into academic grants or
publications.  There are a few weak venues for software, like the NIH
`Software Maintenance grant program
<http://grants.nih.gov/grants/guide/pa-files/par-08-010.html>`__ or
the NSF `Software Infrastructure for Sustained Innovation
<http://www.nsf.gov/pubs/2010/nsf10551/nsf10551.htm>`__ program, and
some journals do exist to support the publication of software, but
these haven't made much of an impact yet, and -- just as importantly
-- seem to be largely uncoupled from software quality, at least as far
as I can tell.  Sean Eddy wrote a great article `touching on the need
for better software developer incentives <http://selab.janelia.org/people/eddys/blog/?p=313>`__ that is particularly worth reading.

So why write software?  Right now you only write software for the purpose
of doing your own research, and there's very little incentive to make it
public, much less make it *good*.  It's rarely if ever peer reviewed, and
the number of people using your software is (at best) useful for convincing
grant reviewers that maybe you had some useful ideas a few years back.

In light of all of this, I'm very pleased to announce a new journal,
`Open Research Computation
<http://www.openresearchcomputation.com/>`__, or ORC.  ORC is a
journal for those of us who, for one reason or another, spend a lot of
time working on the software.  Cameron Neylon neyls it in `his blog
post
<http://cameronneylon.net/blog/open-research-computation-an-ordinary-journal-with-extraordinary-aims/>`__:

  Computation lies at the heart of all modern research. ... Open
  Research Computation is a journal that seeks to directly address the
  issues that computational researchers have.  ... The primary
  consideration for publication in ORC is that your code must be
  capable of being used, re-purposed, understood, and efficiently
  built on.

I'm extra-specially-pleased to be on the board of editors, not least
because so far it seems like this journal is trying to break
significant new ground.  Our ed board discussions so far have included
discussions on how to properly "snapshot" version control repositories
upon publication of the associated paper (easy for DVCS... not so
much for svn) and considerations for "repeat" publishing of significant
new software versions, as the software matures, in order to help encourage
people to actually update and release their software.

This new journal isn't a panacea, of course.  It's going to take 3-5 years,
or even more, to make a real impact, if it ever does.  But I'm enthusiastic
about a venue that speaks to a major theme of my own scientific efforts --
responsible computing -- and that could help in the struggle to place
responsible computing more squarely in the scientific focus.

I also hope that this kind of journal -- providing incentives for more
online interaction, if only in software -- will help convince scientists
that online interaction is a Good Thing.  At the least it's one more
brick in the road.

--titus

p.s. Merry Christmas, all!


----

**Legacy Comments**


Posted by Titus Brow on 2011-03-11 at 10:46. 

::

   oops, deleted @sciverse comment:    Valid points, Titus, implying
   @NeylonCameron. Our thoughts are heading in the same direction,
   pondering how to shape our SciVerse framework
   (ScienceDirect,Scopus,HUB), built on OpenSocial, as a citation
   framework for software in the scientific space. I would be interested
   to start up a broader (that is: on an implementation level) discussion
   about this. For SciVerse, look at <a
   href="http://developer.scivers.com">http://developer.scivers.com</a>.

