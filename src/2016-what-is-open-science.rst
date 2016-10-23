What is open science?
#####################

:author: C\. Titus Brown
:tags: essay
:date: 2016-10-22
:slug: 2016-what-is-open-science
:category: science


.. When I present work from my lab, I usually mention our interest in open science, and wave my hands around a bit and talk about open data and open source as well as open access.  Every now and then people ask me how I think about a specific issue (preprints, for example).  But I don’t think I’ve ever written something high level about what I think open science actually is, or why I practice it.  So when Biella Coleman asked me for an essay on open science, I decided to write up my perspective what open open science is!

Science advances because we share ideas and methods
---------------------------------------------------

Scientific progress relies on the sharing of both scientific ideas and
scientific methodology - “If I have seen further it is by standing on
the shoulders of Giants”
(https://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants). The
natural sciences advance not just when a researcher observes or
understands a phenomenon, but also when we develop (and share) a new
experimental technique (e.g. microscopy), a mathematical approach
(e.g. calculus), or a new computational framework (e.g. multi scale
modeling of chemical systems).  This is most concretely illustrated by
the practice of citation - when publishing, we cite the previous
ideas we’re building on, the published methods we’re using, and the
publicly available materials we relied upon.  Science advances
*because of* this sharing of ideas.

Despite this, however, there are many barriers that lie in the way of
sharing ideas and methods - ranging from cultural (e.g. peer review
delays before publication) to economic (e.g. closed access publishing)
to methodological (e.g. incomplete descriptions of procedures) to
systemic (e.g. incentives to hide data and methods).  Some of these
barriers are well intentioned - peer review is intended to block
incorrect work from being shared - while others have simply evolved
with science, e.g. closed access publishing.

What is open science?
---------------------

Open science is the *philosophical* perspective that sharing is good
and that barriers to sharing should be lowered as much as possible.
The *practice* of open science is concerned with the *details* of how
to lower or erase the technical, social, and cultural barriers to
sharing.  This practice includes not only what I think of as “the big
three” issues -- open access to publications, open publication and
dissemination of data, and open development, dissemination, and reuse
of source code -- but also issues such as social media, open peer
review, posting and publishing grants, open lab notebooks, and other
methods of disseminating ideas and methods quickly.

The potential *value* of open science should be immediately obvious:
easier and faster access to ideas, methods, and data should drive
science forward faster! But open science can also aid with
reproducibility and replication, decrease the effects of economic
inequality in the sciences by liberating ideas from subscription fees,
and provide materials for teaching and training.  And indeed, there is
some evidence for many of these benefits of open science even in the
short term (@@erin paper).  This is why many funding agencies and
institutions are pushing for more science to be done more openly and
made available sooner - because they want to better leverage their
investment in scientific progress.

Some examples of open science
-----------------------------

Here are a few examples of open science approaches.

Preprints
~~~~~~~~~

In biology (and many other sciences), scientists can only publish
papers after they undergo one or more rounds of peer review, in which
2-4 other scientists read through the paper and check it for mistakes
or overstatements. Only after a journal editor has received the
reviews and decided to accept the paper does it “count".  However, in
some fields, there are public sites where draft versions of papers can
be publicly posted prior to peer review - these “preprint servers”
work to disseminate work in advance of any formal review.  The first
widely used preprint server, arXiv, was created in the 1980s for math
and physics, and in those fields preprints now often count towards
promotion and grant decisions.

The advantages of preprints are that they get the work out there,
typically with a citable identifier (DOI), and allow new methods and
discoveries to spread quickly.  They also typically count for
establishing priority - a discovery announced in a preprint is viewed
as a discovery, period, unless it is retracted after peer review.  The
practical disadvantages are few - most journals allow authors to
preprint their work, and so preprints typically just act as an
extension of the traditional publishing system.  Perhaps the major
disadvantage is also an advantage - the work is published with the
names of the authors, so the reputation of the authors can be affected
both positively and negatively by their work.  This leads to what some
people tell me is the major drawback to preprints for them - that the
work is publicly posted without any formal vetting process, which
might catch major problems with the work.

I have been submitting preprints since my first paper in 1993, which
was written with a physicist (@@cite avida).  In graduate school, I lapsed
for many years because my field (developmental biology) didn’t “do”
preprints. When I started my own lab, I returned to preprinting, with
all of my senior author papers submitted as preprints.  Far from
suffering any harm, I have found that our ideas and our software have
spread more quickly because of it - for example, by the time my first
senior author paper was reviewed, someone had already built on top of
it based on what we wrote in the preprint (`Pell et al., 2014
<www.pnas.org/content/109/33/13272.abstract>`__, and @@hierarchical
bloom filters).

Social media
~~~~~~~~~~~~

There are increasingly many scientists of all career stages on Twitter
and writing blogs, and they discuss their own and others’ work openly
and even candidly.  This has the effect of letting people restricted
in their travel into social circles that would otherwise be closed by
physical limitations, and accelerates cross-subject pollination of
ideas. In my field (bioinformatics), it is typical to hear about new
bioinformatics or genomics methods online 6 months to a year before
they are even available as a preprint.  The downsides are the typical
social media downsides: social media is a club, however welcoming;
identifiable women and people of color operate at a disadvantage here
as elsewhere; cultivating a social media profile can require quite a
bit of time that could be spent elsewhere; and online discussions
about science can be gossipy, negative, and even unpleasant.
Nonetheless there is little doubt that it can be a useful tool for
many occasions (cite McKiernan) and can foster networking and
connections in ways that don’t rely on physical presence - a major
advantage to labs without significant travel funds, parents with small
children, etc.

In my case, I tend to err on the side of "open", writing blog posts
about my research and talking openly about ideas on twitter.  This has
led to many more international connections than I would have had
otherwise, as well as a broad community of scientists that I consider
personal friends and colleagues.  Since many of my bioinformatics
colleagues tend to be housed in biology or computer science
departments rather than any formal computational biology program, the
online world of social media serves as an excellent way of discovering
colleagues and maintaining collegiality in an interdisciplinary world,
completely independent of its use for spreading ideas and building
reputation.

Posting grants
~~~~~~~~~~~~~~

While reputation is the key currency of advancement in science, good
ideas are fodder for this advancement.  Ideas are typically written up
in the most detail in grant proposals - requests for funding from
government agencies or private foundations. The ideas in grant
proposals are guarded jealously, with many professors refusing to
share grant proposals even within their labs. A few people (myself
included) have taken to publicly posting grants when they are
submitted, for a variety of reasons (@@cite ethane post).  In my case,
I was hoping to engage with a broader community to discuss the ideas
in my grant proposal; while I haven’t found this engagement, the
grants did turn out to be useful for junior faculty who are confused
about formatting and tone and are looking for examples of successful
(or unsuccessful) grants.  More recently, I have found that people are
more than happy to skim my grants and tell me about work outside my
field or unpublished work that bears on my proposal; with `my most
recent proposal
<http://ivory.idyll.org/blog/2016-mybinder-workshop-proposal.html>`__,
I discovered a number of potential collaborators within 24 hours of
posting my draft.

Why *not* open science?
~~~~~~~~~~~~~~~~~~~~~~~

The open science perspective - "more sharing, more better" - is slowly
spreading, but there are many challenges that delay its spread.

One *challenge* of open science is that sharing takes effort, while
the immediate benefits of that sharing largely go to people other than
the producer of the work being shared.  Open data is a perfect example
of this: it takes time and effort to clean up and publish data, and
the primary benefit of doing so will be realized by other people.  The
same is true of software .  Another challenge is that any unexpected
positive consequences of sharing, such as serendipitous discoveries
and collaboration, cannot be accurately evaluated or pitched to others
in the short term - it requires years, and sometimes decades, to make
progress on scientific problems, and the benefits of sharing do not
appear on demand.

Another block to open science is that many of the mechanisms of
sharing are themselves somewhat new, and are rejected in unthinking
conservatism of practice.  In particular, most senior scientists
entered science at a time when the Internet was young and the basic
modalities and culture of communicating and sharing over the Internet
hadn’t yet been developed.  Since the pre-Internet practices work for
them, they see no reason to change. Absent a specific reason to adopt
new practices, they are unlikely to invest time and energy in adopting
new practices.  This can be seen in the rapid adoption of e-mail and
web sites for peer review (making old practices faster and cheaper) in
comparison to the slow and incomplete adoption of social media for
communicating about science (which is seen by many scientists as an
additional burden on their time, energy, and focus).

Metrics for evaluating products that can be shared are also
underdeveloped.  For example, it is often hard to track or summarize
the contributions that a piece of software or a data set makes to
advancing a field, because until recently it was hard to cite software
and data.  More, there is no good technical way to track software that
supports other software, or data sets that are combined in a larger
study or meta-study, so many of the indirect products of software and
data may go underreported.

Intellectual property law also causes problems. For example, in the
US, the Bayh-Dole Act also stands in the way of sharing ideas early.
This act was intended to spur innovation by granting universities the
intellectual property rights to their research discoveries and
encouraging them to develop them, but I believe that it has also
encouraged people to keep their ideas secret until they know if they
are valuable.  But in practice most academic research is not directly
useful, and moreover it costs a significant amount of money to
productize, so most ideas are never developed commercially. In effect
this simply discourages early sharing of ideas.

Finally, there are also commercial entities that profit exorbitantly
from restricting access to publications.  Several academic publishers,
including Elsevier and MacMillan, have profit margins of 30-40%
(@@cite)! These corporations are invested in the current system and
have worked to politically block government efforts towards
encouraging open science (@@eisen thing on pubmed central 1st
attempt). One outrageous common practice is to charge a single lump
sum for access to a large number of journals each year, and only
provide access to the archives in the journals through that current
subscription - in effect making scientists pay annually for access to
their own archival literature.  Just as bad, the subscription gateways
make it difficult for scientists to access literature; this fueled the
rise of scihub, an illegal open archive of academic papers that is
heavily used by academics with subscriptions because it is easy to
search and download from in comparison to publisher Web sites
(@@scihub discussion).

A vision for open science
~~~~~~~~~~~~~~~~~~~~~~~~~

A great irony of science is that a wildly successful model of sharing
and innovation — the free and open source software (FOSS) development
community— emerged from academic roots, but has largely failed to
affect academic practice. The FOSS community is an exemplar of what
science could be: highly reproducible, very collaborative, and
completely open.  These ideas are explored in depth in `Millman and
Perez @@
<http://www.jarrodmillman.com/publications/millman2014developing.pdf>`__.

It is easy and (I think) correct to argue that science has been
corrupted by the reputation game (see e.g. `@@
<https://neurochambers.blogspot.com/2016/09/methodological-terrorism-and-other-myths.html>`__)
and that people are often more concerned about job and reputation than
in making progress on hard problems.  The decline in public funding
for science, the decrease in tenured positions (`@@
<https://aeon.co/ideas/without-tenure-academics-are-becoming-terrified-sheep>`__),
and the increasing corporatization of research all stand in the way of
open science and thus in the way of faster scientific progress.

I remain hopeful, however, because of generational change. The
Internet and the rise of free content has made younger generations
more aware of the value of frictionless sharing and collaboration.
Moreover, as data set sizes become larger and data becomes cheaper to
generate, the value of sharing data and methods becomes much more
obvious. Young scientists seem much more open to casual sharing and
collaboration than older scientists; it’s the job of senior scientists
who believe in open science to see that they are rewarded, not
punished, for this.

----

More thoughts --

Internet and software

Bioinformatics and data science.



Incentive structures get in the way.

lalRef Erin, NEJM.

https://ilovesymposia.com/2015/12/26/why-scientists-should-code-in-the-open/

https://speakerdeck.com/jakevdp/in-defense-of-extreme-openness

https://github.com/svaksha/aksh/blob/master/open-research.md

https://medium.com/the-spike/how-a-happy-moment-for-neuroscience-is-a-sad-moment-for-science-c4ba00336e9c#.fyvgkzsi7

