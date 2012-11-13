w4s - thoughts on making science work better
############################################

:author: C\. Titus Brown
:tags: open science,webmaking,w4s
:date: 2012-11-13
:slug: w4s-overview
:category: science

This is one of a bunch of posts on what I'm calling 'w4s' -- using the
Web, and principles of the Web, to improve science.  The others are:

`The awesomeness we're experiencing <../w4s-awesomeness.html>`__, which
provides some examples of current awesomeness in this area.

`The challenges ahead <../w4s-challenges.html>`__, which covers some of the
reasons why academia isn't moving very fast in this area.

`Strategizing for the future <../w4s-future-strategies.html>`__, which talks
about technical strategies and approaches for helping change things.

`Tech wanted! <../w4s-tech-wanted.html>`__, which gives some specific
enabling technologies that I think are fairly easy to implement.

----

In `Reinventing Discovery
<http://michaelnielsen.org/blog/reinventing-discovery/>`__, Nielsen
talks at great length about the problem of asymmetry in academic
openness: basically, while almost everyone acknowledges the value to
the community of being open, individuals are too busy chasing the
existing incentive structure -- papers! grants! -- to contribute to
open materials.  The example of `qwiki <http://qwiki.stanford.edu/>`__
(which appears to be down now... :( resonated with me: it was created
to great fanfare, but was then actively maintained by only a few
people, and most user-contributed content was on vanity pages.
The incentive system at work!

I think this situation is starting to change, at least in some
reasonably broad ways, and I have two pieces of evidence from the
bioinformatics and genomics community to present in support.

First, blogs and social media.  Relatively few academics have active
blogs or Twitter accounts, but it is increasingly being recognized by
the community as a useful way to broadcast your ideas and connect with
other scientists.  I can think of two simple reasons for this: one
reason is that, increasingly, professors actively engaged in cutting
edge research are blogging and tweeting, so blogging and tweeting have
become excellent ways to emulate and connect with them.  (For example,
Leonid Kruglyak and Jonathan Eisen are
two specific exemplars -- they are well regarded scientists who
regularly blog or tweet and have been very successful at conveying
their research work via social media.)  The second reason is simply
*generational* -- an increasingly greater number of grad students both
have blogs and read them, and are blogging as part of their regular
research lives.  So blogging is both a top down and bottom up phenomenon, at
least in my home field of biology.

The second piece of evidence is from course materials in genomics and
bioinformatics courses.  About half of the people teaching these
courses make their material freely available online, and in some cases
explicitly encourage not only use but reuse and remixing.  This is not
quite as participatory as something like a wiki (although I think
`these materials can be easily made much more open to comments and
contributions
<http://ivory.idyll.org/blog/rtd-comments-and-editing.html>`__) but it
does indicate that attitudes are shifting away from a de facto
"everything closed" to a de facto "everything open."

Between the generational considerations, the way the Web and
personally generated content is permeating everything in society, and
my specific observations above, as well as the stunning progress in
Open Access, I think that the transition to "online
science", with all the trimmings -- open access, open data, online
collaboration, and even the robust communication of the process of
data analysis -- is inevitable.

And we're done, right?  Game over?

Well, no.

I'll discuss three points below.  First, we need to enable remixing, not just
open data/access/etc.  Second, we need to accelerate the process so that we
can tackle big societal problems sooner.  And third, we need to engage
a broader community.

"Open" vs remixable
-------------------

"Open" just isn't enough.  I've carefully avoided defining it, in part
because there are people much more legally inclined than I am who know
far more about it, and also because it's a topic that inspires online
religious wars, and also because even advocates `mean different things
by it
<http://www.plosone.org/article/info%253Adoi%252F10.1371%252Fjournal.pone.0023420>`__.
Plus, corporate interests are attempting to redefine "Open Access" to
mean whatever is best for their bottom line.

So what should 'open' mean? We need to maximize *reusability*
or *remixability* above and beyond *access*.  (I *think* the right
distinction is `gratis vs libre
<http://en.wikipedia.org/wiki/Gratis_versus_Libre>`__, or `"free as in
beer vs free as in freedom" <http://c2.com/cgi/wiki?FreeAsInBeer>`__.
We want research to be libre, not just gratis.)

The scientific process we've developed through several centuries is
predicated on remix with provenance: you publish a paper to
communicate your results and work, I build on the paper and write my
own paper, which cites your paper.  (Michael Nielsen has a great and
much more detailed description of this in Reinventing Discovery.)
This is generally compatible with the idea that very few, if any,
ideas are entirely new -- `we stand on the shoulders of giants
<http://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants>`__
-- and our job, as scientists, is not only to advance our field but to
do so in such a way as to elevate the perspective of those who follow.

*This* is in what is danger: our ability to remix and reuse not just
research ideas, but research data and process.

The pernicious effects of `Bayh-Dole
<http://en.wikipedia.org/wiki/Bayh%E2%80%93Dole_Act>`__ on academic
research is one example of this threat -- I hear that negotiations
over material transfer agreements one must sign in biomedical research
is stifling both basic and translational research, for example,
because of the amount of money that *could* be made.  Closer to home,
`the GATK folk are close-sourcing their variant caller
<http://gatkforums.broadinstitute.org/discussion/17/gatk-2-0-announcement>`__,
presumably to make a buck or three.

I think a bigger threat to remix culture in science is likely to be
the rise of "mixed model" online startups that are attempting to make
a buck off of social data and online material.  For example, courtesy
of Greg Wilson comes `this coulda-seen-it-coming story about Coursera
effectively blocking free institutional use of their materials
<http://hapgood.us/2012/11/09/coursera-praises-mooc-wrapping-as-they-attempt-to-ban-it/>`__.
Less obviously silly examples for research (but just as limiting) are
the `changes to Twitter's TOS that block If-This-Then-That
<http://www.theverge.com/2012/9/20/3364888/ifttt-disables-twitter-triggers>`__;
the rise of "alternate" social networking platforms that aim for
researcher lock-in but don't provide `data liberation APIs
<http://www.dataliberation.org/>`__; and pretty much *any* 'free' but
not 'open' set of services.  There are obvious market reasons for such
companies to restrict export of data and broad free use of their software,
but I think that they are bad for the future of science.

If you want a positive example, I think `Figshare
<http://www.figshare.com>`__ gets it right, by explicitly buying
into a cultural model of remixing by using `Creative Commons <http://creativecommons.org>`__ licenses.

Irony in this space abounds, BTW.  I feel compelled to mention `the
Executable Papers Grand Challenge
<http://www.executablepapers.com/>`__, brought to you ... by Elsevier.
Or one of the first two IPython Notebook executable papers being
`published in ISME, a non-open-access journal
<www.nature.com/ismej/journal/vaop/ncurrent/full/ismej2012123a.html>`__.

The bottom line is this: we need to ensure that open access, open
science, open data, and the rest all permit and encourage *remixing*,
in much the way that open source has institutionalized it with
licensing.  This is just as important for the social networking
metadata of science (or, as we call it, "collaboration" :) as it
is for explicit research products.

Generational change isn't fast enough
-------------------------------------

I'm sure you've all seen this quote -- 

   "a new scientific truth does not triumph by convincing its
   opponents and making them see the light, but rather because its
   opponents eventually die, and a new generation grows up that is
   familiar with it."

This quote, from Max Planck via Thomas Kuhn, is used by Kuhn in
illustration of `the dynamics of paradigm shifts
<http://en.wikipedia.org/wiki/Paradigm_shift>`__.  It's perhaps more
succinctly but even more cynically stated as,

   `Science advances one funeral at a time <http://en.wikiquote.org/wiki/Max_Planck>`__

So, sure, if open* is inevitable, we could simply wait for all the opponents
to retire, and switch the fight over to making sure that it's remixable
(see point #1, above).  But I think we need to figure out how to accelerate
the process.  Why?

We face lots of big, complex societal problems, and my bet is that the
single-scientist approach isn't going to work to solve them.  In my
own domain of expertise, biology, we increasingly rely on big and
heterogeneous data sets, produced by other people, to interpret our
own data and generate hypotheses; these resources, while necessary,
rely on open principles that are not well supported within the
current incentive structure.

Now, what's interesting is that it's clear that the funding agencies
*get* this, at least from the informal discussions that I keep on
having with program officers about Big Data, data use and reuse, data
integration, and publication.  Everyone is aware that it's a problem
and that the production, curation, and interpretation of big
data sets is critical, as well as the development of effective and
usable software.  But we don't really know how to incentive this.

As an increasing amount of effort is put towards generating data sets
and correlating across data sets, funding agencies are certainly
trying to figure out how to reward such effort. The NSF is now
`explicitly allowing software and databases
<http://researchremix.wordpress.com/2011/07/13/biosketch/>`__ in the
personnel BioSketches, for example, which is a great advance.
Surely this is driving change?

The obstacle, unfortunately, may be the peer reviewer system.  Most
grants and papers are peer reviewed, and "peers" in this case include
lots of professors that venerate PDFs and `two-significant-digit
Impact Factors <http://genomebiology.com/>`__.  Moreover, many
reviewers value theory over practice -- Fernando Perez has repeatedly
ranted to me about his experience on serving on review panels for
capacity-building cyberinfrastructure grants where most of the
reviewers pay no attention whatsoever to the plans for software or
data release, and even poo-poo those that have explicit plans.  And if
a grant gets trashed by the reviewers, it's *very* hard for the
program manager to override that.  The same thing occurs with
software, where `openness and replicability don't figure into the
review much
<http://ivory.idyll.org/blog/blog-review-criteria-for-bioinfo.html>`__. So
there's a big problem in getting grants and papers if you're
distracting yourself by trying to be useful in addition to addressing
novelty, impact, etc.

The career implications are that if you're stupid enough to make
useful software and spend your time releasing useful data rather than
writing papers, you can expect to be sidelined academically -- either
because you won't get job offers, or because you won't get grants when
you *do* have a job.  A few program managers are very concerned about
this, because it means that the more competent and hands-on the person
is, the more likely it is that they will not be able to stay in
academia. I'm watching this happen with some of my own students, who
are very good at data analysis and software development, but don't
want to try to make it in academia; and because they have plenty of
other good options in industry, they leave. It's a real problem.

So unfortunately, I don't think it's going to be as simple as getting
the funding agencies to push.  Where are other lever points?

One lever point that I think is ripe for attack is *tools*.  We lack
good tools to robustly *support* good publication of process and data,
and it's unreasonable to expect scientists to learn data-base backed
Web programming in order to publish a paper.  (As Greg Wilson likes to
say, `we don't think we can teach people enough about Web programming
to let them do anything but create security holes
<http://software-carpentry.org/2012/02/comparing-software-carpentry-to-cs-principles/>`__.)
I'd guess that we need both *incentives* at the funding level --
because honestly, it's one of the only ways to get scientists to do
*anything* -- and *enabling technology* that lets scientists publish
process and data easily.  And yes, this guess is the underlying
motivation for many of my `wanted tech
<http://ivory.idyll.org/blog/w4s-tech-wanted.html>`__ and `ideas for
the future <http://ivory.idyll.org/blog/w4s-future-strategies.html>`__

I think it would also be interesting to figure out how to `hack
academic culture <http://esr.ibiblio.org/?p=4564>`__, but I'm not
sure how to begin that mammoth undertaking :).  Good tools would
certainly help.

Enabling citizen science
------------------------

Another big obstacle, especially here in the US, is the lack of
engagement with scientists.  Corporate and liberal anti-science
agendas are crippling our ability to intelligently discuss evolution,
climate science, vaccines, and nuclear energy -- just to name a few
hot-button topics :).  Most people just aren't that involved in the
scientific process, which makes it easy to snow them. What's the
solution?

Personally, I think citizen science is a pretty neat idea.  I was up
at Mozilla in Toronto a few months ago for a Software Carpentry
summit, and a group of us sketched out a bunch of ideas on how to
enable non-academics to interact with data and process.  (In fact, the
first four ideas in my `wanted tech list
<http://ivory.idyll.org/blog/w4s-tech-wanted.html>`__ come partially
or completely from that discussion.)

One specific idea I had at the time was to integrate a sort of
storify-style ipython notebook interface with the `Microbiology of the
Built Environment <http://www.microbe.net/>`__ data, to enable
individuals to examine and correlate their own household microbial
fauna across households and place them in a global context.
The `Earth Microbiome Project <http://www.earthmicrobiome.org/>`__ also
plans to have a citizen science component to enable contributions;
I think integrating citizen-contributed data into a broader context
is a pretty neat idea.

I also believe that Rich Lenski and BEACON would probably be interested
in putting up an integrated interface to all of the Lenski Lab 
`Long Term Evolution Experiment data <http://en.wikipedia.org/wiki/E._coli_long-term_evolution_experiment>`__.  This is less "citizen science" and more
"outreach" but it would still be neat.

So, what's my utopian dream?  It'd be awesome to enable more, better,
and deeper citizen science by enabling easy publication of and rich
interaction with big, open data sets.  Part of this is swiping good
community hacking ideas from massively online collaborations like the
`Polymath Project <http://en.wikipedia.org/wiki/Polymath_Project>`__
and the `Galaxy Zoo <http://en.wikipedia.org/wiki/Galaxy_Zoo>`__;
another big part is developing tools; and a third is figuring out what
fields are ripe for this kind of thing.  Coming from biology, I feel
like efforts such as microbe.net, the Earth Microbiome Project,
`ENCODE <http://www.genome.gov/10005107>`__ and `caBIG
<https://cabig.nci.nih.gov/>`__ are data rich and ripe for more
interaction with a larger community; surely this is true of many other
fields, too.

Concluding thoughts
-------------------

We've made a lot of progress even in the year or two since Michael
Nielsen's book was written -- the advances in open access alone have
been stunning.  But I don't think Open Access is enough; we need to
enable more scientists to be *makers*, not just *consumers*, of data,
code, and online communities.

--titus

p.s. I want to thank Fernando Perez, Carole Goble, and Cameron Neylon
for pointing me towards a bunch of this stuff, and Greg Wilson for
critical commentary.  Interpretations are my own but I bet they agree
with me!
