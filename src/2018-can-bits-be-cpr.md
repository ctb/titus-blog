Title: Can bits be the basis for a digital commons? (No.)
Date: 2018-08-18
Category: science
Tags: cpr, sustainability, commonspilot, data commons
Slug: 2018-can-bits-be-cpr
Authors: C. Titus Brown
Summary: Bits cannot be the basis for a digital commons, because they are not rivalrous.

Recently I’ve been reading a lot about the general area of digital
commons - which includes open online resources, open source projects,
and (presumably)
[whatever a data commons is](http://ivory.idyll.org/blog/2017-commonspilot-kickoff.html).
Most broadly defined, these are resources and projects that are
[open to contribution](http://ivory.idyll.org/blog/2018-how-open-is-too-open.html),
and produce digital public goods. I’m particularly interested in the
question of sustainability, which led me to Ostrom’s
[design principles for common pool resources](https://en.wikipedia.org/wiki/Elinor_Ostrom#Design_principles_for_Common_Pool_Resource_(CPR)_institution),
and the idea that
[“engaged effort” or “attention”](ivory.idyll.org/blog/2018-labor-and-engaged-effort.html)
is the
[common pool resource to be managed by a community for sustainability](http://ivory.idyll.org/blog/2018-oss-framework-cpr.html).

I’ve come across several different ideas about what the common pool
resource is in digital commonses, and I wanted to explore them a
bit. So, here goes.

## Data cannot be the basis of a data commons: a response to the New Zealanders :)

[The Data Commons Blueprint](https://datacommonsnz.gitbooks.io/data-commons-blueprint/content/)
is a brilliant writeup of what a Data Commons might be, and I share
most of their ideas about community governance and the importance of
building communities of practice around data sharing and data
analysis.  But I have a pretty basic disagreement with one pillar of
their argument. The authors define a data commons as being
significantly founded on the availability of *data*:

> Unless all parties feel good about sharing their data, they will be unlikely to do so. … A model where data is fenced off as private property reinforces silos of competing interests rather than data integration of sharing.” (p11)

> How - and why - access to and reuse of data is controlled goes a long way to explaining why creation of a commons faces real challenges. (p20)

This view of data is enshrined in their first Principle of a Data Commons: “Data is a common-pool resource.” (p31).

But there is a fundamental disconnect here with common-pool resource
(CPR) theory. A CPR must be both non-excludable, and rivalrous (see
[this matrix](https://en.wikipedia.org/wiki/Club_good)). Non-excludability
is “easy”, in the context of a Data Commons: it just means that data
access is open to a broad range of participants. But rivalrous is is
harder to achieve with data, because, fundamentally, data doesn’t get
“consumed” by use - and, in fact, opening up data access is an act
with significant positive externalities, in that data use and reuse
generates many indirect benefits for people other than the originator
of the data. That’s actually kind of the point of a data commons!

An additional challenge for me, if not for the general idea of a data
commons, is that the NIH Data Commons *cannot* open up data access to
all because we are including human subjects data, e.g. the TOPmed and
GTEx studies and eventually many more. Access to much this data will
*never* be open due to
[IRB](https://research.oregonstate.edu/irb/frequently-asked-questions/what-institutional-review-board-irb)
requirements. This legal restriction would suggest that the NIH Data
Commons cannot ever be _a_ Data Commons, which seems problematic to
me, at least, as someone engaged in [trying to build it](http://ivory.idyll.org/blog/2018-community-engagement.html).

Interestingly, this intersects with another disagreement I have - this
time, with Albert Wenger in
[World After Capital](http://worldaftercapital.org/), a book that
Nadia Eghbal pointed me towards. In this (fascinating and very
readable) book, Wenger argues that eventually _all information will be
open_, and has a whole section on “Getting over Privacy and
Confidentiality.” While he makes many interesting arguments, I think
he’s arguing past a fundamental mismatch with human psychology and how
humans view risk, and that this will involve a pretty radical shift in
how human brains work.  More to the point, data *discoverability* and
*interoperability* seems at least as important as data access - it
doesn’t matter if you can access the data if you can’t find it or work
with it, and if you can find the data and believe you can work with
it, you will be more motivated to seek access.

I think we can work our way past both of these disagreements if we
state that data openness itself is not the key to a data commons, but
rather a “good” that is *managed* and *curated* by a data commons for
a purpose, e.g. knowledge production from that data. If the data is
not open, it can be viewed as a club good; if it’s open, it’s a public
good. But either way it requires management and curation (and
presumably various kinds of infrastructure to help with knowledge
production).

This brings us back around to the concept of
[engaged effort or attention](http://ivory.idyll.org/blog/2018-labor-and-engaged-effort.html)
as the resource to be managed by a Data Commons, in support of
sustainability.

## Source code cannot be the basis of an open source commons

I just finished my first pass reading of an argument by Schweik in
[Ostrom and Hess, 2007](https://mitpress.mit.edu/books/understanding-knowledge-commons)
that defines **source code** as the common pool resource being
managed by an open source project:

> In FOSS commons, groups of people act collectively to produce a public good (the software), rather than overappropriate the resource. (p279)

I also disagree fundamentally with this. There are some interesting
arguments about copyleft and the GPL and management of the CPR, but at
least on first reading, they fall apart when you realize that (a) a
lot of FOSS uses non-copyleft licenses, and (b) a public good cannot
be a common-pool resource anyway, because source code itself is not
rivalrous.

This intersects with a point that Nadia Eghbal and others pointed out
to me - that successful open source projects are at least partly about
[managing the maintenance effort](http://ivory.idyll.org/blog/2018-anti-sisyphean-league.html)
involved in software production.

## Knowledge (and publications) are probably not the basis of a scholarly commons.

Interestingly, this all connects to another discussion about open
access principles, and scientific publication more
generally. Recently, William Gunn
[made the argument](https://twitter.com/mrgunn/status/1029042440450191360)
that publishers contribute quite a bit to science by “assemb[ing]
thousands of people to devote their lives to producing and
distributing a corpus of high quality [ … ] knowledge. … this is a
valuable thing & it’s worth the money spent.”  Viewed through the
above lens of a commons and its sustainability, what Gunn is saying is
that the *effort* Elsevier and others are putting into sustaining a
scholarly commons is valuable.

I actually agree with that! I have at least two points of major
disagreement, though - first, it is clear that Elsevier in particular
is making a particularly handsome profit off of the scholarly commons,
and that seems like an unwise use of our limited funds for science. I
certainly don’t think this should be a for-profit activity, but I do
see value in it and agree that someone needs to be paid to do it,
somehow; and there are many models for that.

My second (more fundamental) disagreement with Gunn is that Elsevier
and others’ business models depend on restricting access to
information, and this impedes research. More specifically, all
closed-access publishers' business models rely on “successfully
monetizing inconvenience” (this wonderful phrasing is from Justin
Peters at Slate!) Rephrasing this in the terms above, the
academic-publishing complex is producing club goods, and publishers
are not only profiting from *producing* these goods (see previous
paragraph) but for *accessing* these goods. This is bullshit, period -
the marginal cost of *distributing* digital content on this scale is
effectively zero, and this is an absolutely absurd case of rent
seeking. We know this because there is a perfect counterexample:
[Sci-Hub distributes scientific publications to all and sundry for free](https://elifesciences.org/articles/32822).

Circling back around once again: if a scholarly commons is partly
about managing effort in pursuit of sustainability, then universities
and faculty positions can be viewed as one way to pay for the effort
involved, while publication fees can be viewed as another.  This is
quite distinct from the question of whether the knowledge produced
(publications) should be club goods or public goods; whatever they
*should* be, it’s impossible to to argue that publications are a
rivalrous commodity, and hence they cannot be considered as a common
pool resource.

## In conclusion…

Commons should be about managing common-pool resources.

Common-pool resources are defined as resources that are
*non-excludable* and *rivalrous*.

Data is non-rivalrous. Source code is non-rivalrous. Publications are
non-rivalrous. Bits, in general, are non-rivalrous. So bits *can’t* be
the common pool resource being managed by a commons.

This is fine and leads in some interesting directions!

—titus

p.s. Thanks, as always, to Nadia Eghbal for her insight!
