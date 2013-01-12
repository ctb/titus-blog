Thinking about software architecture for heterogeneous data integration
#######################################################################

:author: C\. Titus Brown
:tags: science,software architecture
:date: 2013-01-11
:slug: software-architecture-for-heterogeneous-data-integration
:category: science

I just left the `NAS meeting on Integrating Environmental Health Data
to Advance Discovery
<http://nas-sites.org/emergingscience/meetings/data-meeting/>`__,
where I was an invited speaker.  It was a pretty interesting meeting,
with presentations from speakers who worked on chemotoxicity data,
pollution data, exposure data, and electronic health records, as well
as a few "outsiders" from non-environmental health fields who dealt
with big data and data integration issues.  I was one of the outsiders.

When Carolyn Mattingly spoke with me about coming to this meeting, I
was more than a bit hesitant, because (a) it's not my field, (b) I
mostly *work* with lots of rather homogeneous sequencing data so am not
an expert in *heterogeneous* data, (c) the
integration front is a bit of a horror show in bioinformatics, and (d)
I didn't think many people, anywhere, had done a good job of setting
up structures for solving this problem.  So I wasn't really sure what
I could say.  Carolyn nonetheless convinced me that I might have
something to add (the paraphrase I remember is "you admitted ignorance
more quickly than most, which seems valuable") and bulldozed me into
coming.

(I'm glad I attended!)

I took about a month to prepare, and I ended up deciding to talk about
what kinds of software architecture you might want to invest in for
the long term.  I rephrased my technical goal for the meeting like so:

   How can we best provide a platform or platforms to support flexible
   data integration and data investigation across a wide range of data
   sets and data types in biology?

with the following specific goals:

1. Avoid master data manager and centralization
2. Support federated roll-out of new data and functionality
3. Provide flexible extensibility of ontologies and hierarchies
4. Support diverse "ecology" of databases, interfaces, and analysis software.

In response to these goals, I looked for success stories *outside* of
biology, and in particular for domains and entities

1. with really large amounts of heterogeneous data,
2. that are continually increasing in size,
3. are being effectively mined on an ongoing basis,
4. have widely used programmatic interfaces that support "mashups" and other cross-database stuff,
5. and are intentional, with principles that we can steal or adapt.

and found Amazon [0].  I was already aware of Amazon's approach from
Steve Yegge's `Platform Rant
<https://plus.google.com/112678702228711889851/posts/eVeouesvaVX>`__,
and I found a summary of Amazon's architecture (based on interviews
and such) at `HighScalability
<http://highscalability.com/amazon-architecture>`__.  They have been
demonstrably successful at managing 50 million+ customers, billions of
reviews, hundreds of software services, and basically complexity that
is unimaginable from my perspective. So what I discussed was how, from
a software architecture perspective, taking this kind of platform view
was probably the right way forward.

I peppered the talk with entertaining slides, 'cause walls-o'-text
never works that well and I couldn't use my normal research figures.
I included `a view of the booksthatmakeyoudumb.virgil.gr mashup
<http://booksthatmakeyoudumb.virgil.gr>`__, `the XKCD "standards"
comic <http://xkcd.com/927/>`__, and `the tree-swing design slide
<@@>`__.  Conveniently I was preceded by Stephen Friend (of SAGE), who
made use of oft-wildly irrelevant slides to hold the audience's
attention, and aftr me Matt Martin (from the EPA) put up a GI Joe
slide to make the point that "knowing is half the battle"; my speaking
approach wasn't actually that out of the ordinary :).

I think the talk went OK, with only one major catastrophe (more about that
in my other blog post); a number of people claimed to find it interesting,
at any rate, which is better than being ignored and silently hated!

For the talk itself, you can see my slides `here
<http://www.slideshare.net/c.titus.brown/2013-nasehsdataintegrationdc>`__,
and everything was recorded.  I'll update the post to point to the
transcript and video if and when they are made available.

As I watched the rest of the workshop, though, I realized that I had
stumbled into something deeper than a set of flippant comments that
offered a slightly different perspective on the issues at hand.  I
think I may have converted myself into believing, wholeheartedly, that
the platform view is what we *should* be doing, and, moreover, that I
want to work on it myself, and, more moreover, that it may be the only
successful way forward for the long term.

----

Stripping `Yegge's post <https://plus.google.com/112678702228711889851/posts/eVeouesvaVX>`__ of its irreverence, he claimed that Amazon's
CEO, Jeff Bezos, had mandated the following:

1. All teams must expose data and functionality solely through a
service interface (a service-oriented architecture).

2. All communication between teams happens through that service
interface (no exceptions!).

3. All service interfaces must be designed so that they can be exposed
to the outside world (externalizable).

A more succinct way of putting it is this: **design your service by
dogfooding it** -- design the service *you* want to use, but design
it for others; and then *use it yourself*.

The translation of this into science is that if you want to be a data
provider, you should provide data via an interface that is rich enough
for you yourself to use as a data consumer.  Since, in science, most
data producers and data providers are also consumers of that data,
this would ensure that at least some of the data would be usable by
someone real.  This is directly analogous to the agile software
development approach, in which you design the software with the
end-user in mind, with lots of little iterations to make sure that
you don't deviate too far from a useful course.

In contrast to a service, many (most?) people in biology today provide
data in one of two ways, via a Web GUI or direct data download.  Web
GUIs usually ration the data out piecemeal, via a hard-to-automate but
easy-to-use Web site.  Direct data download is the opposite end of the
spectrum: you can get straight-up file download of everything, but
making use of it in any way requires some amount of scripting or
loading and processing.  When service APIs to query and probe subsets
of the data *are* provided, anecdotes from the DAS folk and others
suggest that people tend to abuse them heavily.

Why would you want to provide service interfaces?  Apart from
architectural and software engineering reasons, the main positive
reason, IMO, is to make serendipitous mashups as easy as possible.
Mashups are Web sites and services where different data sets are
"mashed" together in such a way as to provide novel functionality; for
example, `books that make you dumb
<http://booksthatmakeyoudumb.virgil.gr>`__ "mashed" together
Facebook's "top 10 books" by college lists with a list of average SAT
scores by college to figure out which books were correlated with low
and high SAT scores.  There's no way that Facebook predicted that use,
but because the data for both were available, Virgil Griffiths could
smush the data together to make a new service.  (Note that Virgil is
also the person behind wikiscanner, which correlates changes to
Wikipedia articles by originating domain.)  These kinds of mashups
are basically the same thing as what scientists want to do with
heterogeneous data sets: no one can predict every possible query,
or design their Web site to cover more than the most common use cases.

Why do we need service interfaces?  Service interfaces are basically
remote procedure calls that let you query, manipulate, subset, and
download information and data from remote Web sites.  You can think of
them as libraries of remote functions and data.  In contrast to
service interfaces, Web GUIs tend to channel queries in very specific
directions, and there's a lot of user experience, security, and
authentication involved in building them.  Data downloads go the other
way: to make the data useful, you often need to load in multiple data
files and do your own correlation and querying.  At their worst, service
interfaces can either be as specific as Web GUIs (but without the nice
interface), or as difficult as data downloads ("here's all my data;
have fun") but with higher latency.  But I bet that for most data sets,
there is a broad range of situations where a service interface would
both be considerably more flexible than an HTML Web site

The idea of providing service interfaces is not new by any means.
NCBI and ENSEMBL actually already provide them; their Web sites are,
in some ways, a thin layer over a robust and complex service API.
Plenty of toolkits make use of them.  I just think that, in an era
of large amounts of wildly heterogeneous data, everybody should
be doing things this way.

The more basic point I want to make is this: Amazon and other
companies have to deal with similar (or larger) issues of data size,
data integration, data access, trust, and security as do scientists.
Amazon has settled on a platform architecture, or so it seems; they're
clearly *very* successful, and role out new services with a
frustratingly casual saunter; they have a set of ground rules and
experiences that can be conveyed in techie-speak; and it would be
stupid of us to ignore them.  Just as computational science is
discovering open source, agile programming, version control, and
testing (among other things), I think we should be paying attention to
distributed software architectures that demonstrably can function at
the scale we need.

How practical is this vision?
-----------------------------

Not very, in some ways.  Scientists are notoriously badly trained in
software engineering, and I don't think computer science researchers,
broadly speaking, have distinguished themselves as particularly good
programmers, either.  On the other hand, scientists are really good at picking
up new things (you might call it an occupational requirement ;) and
given the right motivation, I think it could work.

One path towards practical realization is to pick a loosely defined
field, be it environmental health science or genomics, and work to
establish a community of practice within that field.  The rule would
be that anyone seeking new funding for large data production or
provision would have to explain how they were going to make all their
data available via a service interface; this could be provided via
supplemental funding for existing grants, too.  Any group that
obtained this funding would have to hire a techie who would be
responsible for interacting with the other techies at regular
meetings.  Grants would have to include use cases for their data, and
each group would be regularly evaluated on progress towards addressing
those use cases.

The other side of the coin would be data *consumers*, who would need
to be trained. Biologists, for example, are used to dealing with
things via a Web interface; but I think Python libraries combined with
an IPython Notebook install in the cloud would make it possible to
quickly and easily teach scientists to work with single or multiple
remote services.  Workshops at domain conferences, online help desks,
remote tutoring, and all the rest could be brought to bear to help
them through that initial steep learning curve.  More advanced
workshops could focus on building new services that combined data from
producers into mashups that then became new data producers, and people
who wanted to provide specific Web interfaces built on top of some or
all of it would be free to do so.

What are the advantages of this approach?
-----------------------------------------

I think there are a few key advantages.

First, I think we can actually train scientists in both building and
using service APIs. Over at Software Carpentry, Greg Wilson has been
complaining that the only thing we can teach scientists to do with
their data is either build static Web sites or dynamic sites with
massive security holes.  I think with relatively little effort we
could make fairly generic Web services for columnar data (think Excel
spreadsheets), and, with only a little more effort, show them how to
provide subset and query ability on that data.  Integrating other data
sets would be harder, of course, but in many ways not much harder than
building their own SQL database -- which is something we already
purport to teach.

Second, cloud infrastructure makes it easy for groups to build
services that they don't have to actually host themselves; we could
provide common mechanisms for hosting for the field, but leave
scientists to implement their own software.

Third, new services and functionality can be rolled out in a federated
manner -- there is no "master data manager", no centralized site that
you need to argue with to include your data or modify their
functionality.  As long as the APIs are versioned (which is key) then
a tenuous stability can be achieved.

Fourth, it's language independent, thank goodness. You Java, Perl and
Ruby folk can go your misguided ways (note: I am a Pythonista).  R
would make a perfectly good client, and services including R could
enable good service provision for running statistical approaches and
data visualization.  All communication would work via HTTP, which I
think is fast becoming the one true language that everyone actually
has to speak!

Fifth, it's just good software practice. Modularity, separation of concerns,
easy testability, and an acknowledgement that change is inevitable, are all
things that we expect in big systems.

Sixth, enabling interoperability between services would enable a
software ecology, which is desperately needed.  Rather than two
duelling databases with non-overlapping data, we could have many
duelling databases with overlapping or complementary data -- and some
of them would die off, while some of them would succeed.  One might
almost call it a meritocracy, where the most useful survive.  Usage
stats could be used to motivate and drive maintenance funding, while
competitive funding opportunities could be used for extension requests.

Seventh, it provides a formal distinction between the service
providers and the service consumers.  One of my favorite moments
during Matt Martin's talk on providing toxicity data via a Web
services was when one of the audience members asked him if he could
provide a certain custom view on his dashboard app. An appropriate
respone to this would be "no, ma'am, my job is to give you the data
necessary to do that analysis; it's your job to actually do it."  With
tools like IPython Notebook and RStudio, Matt could even give remote
users a set of example views that they could then tweak, modify, and
remix to their own heart's content -- this would be far more enabling
than a straight Web interface could be.

What are the disadvantages of this approach?
--------------------------------------------

A platform approach still requires software development -- if
anything, quite a bit more of it than a centralized approach.  I don't
think there's a way around this, but at least if we get everyone on
the same page, we can establish a community of practice and help each
other out by finding common patterns and problems.

We haven't solved any really hard problems with this, either.
Ontologies and standards are still needed, although they can be more
"casual agreements" than "standards", and, more importantly, they can
be based on real direct immediate use.

The main objection that will be raised, I bet, is that shipping large
amounts of data around via service APIs is inefficient and nasty.  In
response I will say that I think Amazon and Google have made the case
that, past a certain scale, storing massive amounts of data in one big
database is also a really bad idea.  It behooves us to figure this out
*now*.  Even for the massive sequence collections I'm dealing with, I
think this is solvable by providing a richer or deeper set of query
functions, or perhaps just telling people that you need a really
compelling use case to justify the specific development effort needed.

How is this different from every other distributed/remote/blahblah out there?
-----------------------------------------------------------------------------

Most other efforts of which I'm aware have focused on a single problem
or layer.  "I'm going to be the world expert on genome intervals", for
example.  Or "I'm going to be the flexible middleware layer that
enables generic communication."  But I haven't seen many properly
separated-out vertically integrated blobs of functionality.  So
perhaps the combination is different -- separated blobs of lightweight
functionality, intended to provide useful mashups of data via generic
HTTP interfaces, combined with vertically integrated examples and
demos in interactive notebooks like RStudio and IPython Notebook.

It's entirely probable that someone has done this, and I just don't
know about it.  I'd love to hear about it, and success or failure stories.

And how would you get started, Dr. Brown?
-----------------------------------------

On the off chance that someone flung a few $100k at me (anyone?
anyone? Bueller?), I would go out and find three databases that wanted
to work together and had good complex use cases, hire one developer at
each + one local to me, and get to work.  First up would be to
implement some lightweight use cases to iron out the kinks and get
everyone working together.  Then, I would proceed with a series of
small iterations, each time working towards addressing a new use case
or two.  Initially, my developer would be in charge of building
independent libraries and third-party tests, as well as trying out
various mashups; as the collaboration proceeded, my developer would
move towards scalability and security testing, identifying common
needs and development patterns.  At that point, other databases and
data sets and use cases could start to be considered; end users could
also start to be trained on the interfaces, and could come up with
their own use cases for which new functionality was needed.  The
overall goals would be to provide an example set of services, as well
as a set of practices that seemed to work well for this set of use
cases, and -- perhaps most importantly -- a group of people with
experience and expertise in this way of working.

.. BLAST example.

--titus

[0] Disclaimer: Amazon occasionally tosses small research grants my
way, and a family member works rather high up for 'em, as does a
student of mine.  That doesn't entitle Amazon to any slack from me,
though.
