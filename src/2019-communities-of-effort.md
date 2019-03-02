Title: Sustaining open source: thinking about communities of effort
Date: 2019-03-02
Category: science
Tags: sustainability,cpr
Slug: 2019-communities-of-effort
Authors: C. Titus Brown
Summary: Thinking about how to sustain open source.

I just finished a day at the SIAM CSE 2019 conference, where I gave a talk
as part of a mini-symposium on software sustainability ([my abstract](http://ivory.idyll.org/blog/2018-siam-abstract.html),
and [my talk slides](https://osf.io/2gzhy/); see the ['cpr' tag](http://ivory.idyll.org/blog/tag/cpr.html) for all my recent blog posts on this topic.)

When I was outlining the talk, I spent a fair amount of time noodling
about how I wanted to approach the subject. I have a lot of
disorganized thoughts that I think can be put together in interesting,
but for a 20 minute talk, I really needed to pick a narrow focus.

Here's what I ended up with. I'm curious for reactions!

## Defining a term, "communities of effort"

I'll start by defining "communities of effort" as a community formed in
pursuit of a common goal. The goal can be definite or indefinite in
time, and may not be clearly defined, but it's something that (generally
speaking) the community is aligned on.

The term "effort" here refers to [focused or engaged attention](http://ivory.idyll.org/blog/2018-labor-and-engaged-effort.html),
and in this sense in particular, I mean the focused attention applied
towards the common goal.

One rational goal of such a community is to achieve the goal without
wasting effort through duplication or redundancy in work. This connects with
my earlier blog post on [the open source anti-Sisyphean League](http://ivory.idyll.org/blog/2018-anti-sisyphean-league.html), a
term coined by Cory Doctorow: the idea is that there are a number of
rocks to be rolled up hills, and (in an open community) there is no
reason for people to roll those rocks up the hill independently, since
they can take advantage of each other's efforts.

This community of effort directs itself towards achieving the goal,
applying the available effort to the task. Here, effort is a *finite*
resource that is consumable - you cannot apply the same effort to more
than one task, and the effort that is applied towards one task is not
available to be applied to another task. (Of course, the available
effort can be *renewed* or *increased* - more on that later.)

## Effort as a common pool resource

The trickiest and most uncertain link is this: I think that the effort
applied towards the common goal is, to some extent, directed by the
community.  That is, the available effort - which consists of work
by individuals towards the collective goal - is at the very least
loosely coordinated with the community, if not coordinated more closely.

(This may be because the community needs to be involved in order to
decrease redundancy. Not sure.)

If this is true - that effort is coordinated by the community rather
than the individual, and so is non-excludable, and also is a finite
resource that can be consumed, and is thus rivalrous, this turns
it into a common pool resource.

Common pool resources are well known to anyone who has heard of the
tragedy of the commons: they are resources that are subject to this
tragedy, of being consumable by many in an unregulated way.

## What are some examples of these "communities of effort"?

A prime example is open source projects like Python. They're rooted
in a community approach; they're not not run by a corporation or a
government agency; and any structure (like a nonprofit) is created
after they already exist (and usually after they are successful!)

I think the Carpentries training community is another good example.
This is a community of people interested in teaching and training in
data science and software engineering that essentially self-assembled,
and is aligned around their mission (of teaching and training). The
non-profit structure around it is, again, an ex post facto creation.

Data analysis commons, in which methods, data, compute resources, and
data analysis interfaces are coordinated to address the data analysis
needs of a community, would be another example.

(Wikipedia might be another, but I'm less familiar with how it works.)

## Why do we care about these communities?

Well, these communities are amazingly *effective*, in at least
some cases. For example, Python and R between them are essentially
*the* modern data science languages - both are open source, both
are community coordinated.

More generally, it is probably not an exaggeration to say that the
products of open source communities of effort underly the vast
majority of Silicon Valley software, as well as most research software.

Sustaining, growing, and supporting these communities is pretty
important!

## How do these communities get started, and why are they effective?

One feature of successful communities of effort - those that seem to
succeed in growing their pool of available effort - is that they are
often very organic in their approach to tackling their mission.  This
is probably an effect of the community-based approach, in that the
members of these communities are to a reasonably significant extent
self-motivated and self-directed to solve their problems, and so the
solutions are often bottom-up created with only a light level of
coordination on top.  (I'll revisit this in terms of governance in a
bit.)

The other kind of fun thing is that these days it's pretty easy to bootstrap
a community of effort: with some enthusiasm and a site like GitHub, you can
spin up a new community project quite quickly.

Last but not least, many (most? all?) communities of effort have at
least one person who has placed their effort at the service of the
community mission. These are the leaders and/or maintainers of the
project.

## So what's the problem? It's all good, right?

Well... there are a few things I don't really understand.

For one, the formation of large groups of people who sustain a collective
to pursue a common goal violates basic tenets of collective action - at least,
as I understand them. The idea here is that, if there is a large group
of people pursuing a common goal, then the smart (economically rational) thing
for someone to do is ...not do any work at all, because the individual will
reap the benefits of the group work. So, what's different with these
communities of effort?

Sustainability and in particular *maintenance* is a big question, too;
these communities often rely on one or a few core maintainers to make things
happen, and it is really unclear why these maintainers (who are often
unpaid or underpaid) would take on these tasks. Yes, they get kudos and
reputation, but kudos and reputation do not put food on the table... why do
they do it?

(One thought - perhaps the creation of a successful community
of effort really depends on there being at least one person who ignores
short-term economic rationality? So then you just don't see all the failed
attempts where someone decides not to be irrational and hence not bother?
Another thought is that perhaps the key aspect of many of these communities
being *open* means that the maintainer-type folk realize that
no one else is tackling the common goal, and since they need the goal met
as well, they might as well do it?)

## Does framing the problem as a common pool resource problem yield any solutions?

I think it does.

First, once you recognize effort as the limiting resource, the
question of how to maintain and increase that resource comes to the
forefront. There are a number of possible mechanisms, including
investing in making the community easy or rewarding to join, welcoming
new contributors, and/or providing special methods or data or access
to community members.  In this view, these activities become more central
than they are if you are thinking only about the overall goal or mission
of the community.

Second, Elinor Ostrom outlined some design principles for
sustainability of common pool resources based on empirical studies, in
[Governing the Commons](https://www.amazon.com/Governing-Commons-Evolution-Institutions-Collective/dp/0521405998). One of these principles is about making
collective choice arrangements that allow most of the appropriators
(members of the community) to participate in the decision making
process.

Basically, this boils down to rewarding people who invest effort with
some level of influence in how that effort is applied towards the
community goals.  This both incentivizes participation with collective
ownership, and also seems to allow a form of organic communication
where the people applying effort feed results from their work back
into the overall community direction. This is, to my mind, one of the
things that leads these communities to be so effective.

This mode of governance **by** members of the community **for** the
community goal leads to another interesting thought. Funders
participate in these communities in indirect ways, by seeking to fund
(or being sought out to fund) effort within the community. Rarely is
the direction of this support directly dictated by the funder; it's
usually laundered through the community member(s) being supported.
This is both good and bad - it limits the degree to which funders (and
companies) can directly influence the project, but also means that
funders may not be able to easily identify the uses to which their
money will be put.

## Who is part of the community of effort?

Anyone who contributes their effort is part of the community, and hence
should get some form of influence over governance (by the above design
principle).

Extractive contributors - contributors who do not contribute to the
overall effort, especially the *maintenance* effort - would not,
however, be considered part of the community. See
[How open is too open?](http://ivory.idyll.org/blog/2018-how-open-is-too-open.html) for this argument.

People who are using the product of the community but not costing the
community any effort (e.g. consumers of the source code) would also
not be part of the community, unless they contribute in some way to the
project.

One interesting result of this kind of thinking is that, for data
analysis commons, people who provide data or methods, or training
people, or contributing documentations, are contributing effort. This
provides a level of rational inclusion of this kind of work within the
community, and also in governance; they are in a direct sense
contributing to the sustainability of the community of effort.

## Is academia a good home for these communities of effort?

I note that the leadership and governance model in basic research, at
least, is often not inclusive of the people who are doing the work,
and instead centers on reputation and hierarchy.  I don't think
universities and colleagues focused on basic research are likely to be
a good part of the support network for communities of effort, in
general.

I have been quite impressed with what I've seen of extension efforts at
universities, which are faculty-level investments of time and energy
in communities. I'm planning to look more in to the idea of a
digital extension model.

## Some final thoughts

I think it's important to recognize that (these days at least) there
are lots of competing projects in which people can invest their time
and effort, and it's probably not a bad thing to frame it as a
competition between these communities for people's time and
attention. Communities that do a good job of attracting contributors
and incentivizing the inclusion of effort can win out and potentially
be more sustainable than communities that do a lousy job.  (This has
potentially dire implications for some scientific research communities,
which are not always very welcoming or inclusive. I'm not sad about this.)

This framing also puts *soft skills* front and center in the equation,
and I think this is also a good outcome.

## Open / unaddressed questions

Two open questions.

First, what are communities of effort *not* good at? I would venture
that any boring or maintenance level jobs would tend to be addressed
poorly by these communities, due to how human enthusiasm works.

Second, I want to return to the missing link mentioned above - that
these communities seemingly depend on one or more people placing their
effort in service of the community. What are the reasons why people do
this, and how do we support and maintain it? Inquiring minds want to
know... It would be nice if we had a reasonably comprehensive picture
of why this occurred, because it doesn't seem like rational behavior
on the face of it. (I'm very thankful that people do this, of course,
which is why I want to better support this path!)

## Acknowledgements

I gratefully acknowledge Adam Resnick, Matter Trunnel, Josh Greenberg,
Nadia Eghbal, Luiz Irber, and Tracy Teal, with whom I've had inspiring
conversations on these fronts.

The NIH (via the Data Commons funding) and the Moore Foundation
provided funding to me to think about, read about, and explore these
issues.

Comments welcome!

--titus
