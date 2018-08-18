Title: A framework for thinking about Open Source Sustainability?
Date: 2018-07-02
Category: science
Tags: sustainability,software,cpr
Slug: 2018-oss-framework-cpr
Authors: C. Titus Brown
Summary: Can we apply Common Pool Resource work to open online projects?

I just revisited [Nadia Eghbal’s wonderful post](https://nadiaeghbal.com/tragedy-of-the-commons) on “the tragedy of the commons” and her thoughts of an alternate ending for it, based on Elinor Ostrom's work on Common Pool Resources, and it resonated with some thinking I’d been doing in another context, and I wanted to share.

Nadia has been exploring the open source sustainability problem [(ref)](https://www.fordfoundation.org/library/reports-and-studies/roads-and-bridges-the-unseen-labor-behind-our-digital-infrastructure/), in which a good deal of our important open source software is maintained by a relatively small number of people without much in the way of guaranteed funding.  The size and scope of the problem vary depending on who you talk to, but there was [a pretty shocking picture of the scientific python computing ecosystem](https://twitter.com/fringetracker/status/991796881767436288) in which there were only half a dozen maintainers for numpy.  Since quite a bit of the Python scientific computing ecosystem relies on numpy, it seems critically challenging to have so few maintainers.  For an excellent detailed discussion on a specific instance of the general challenges around software development, see ["The Astropy problem"](https://arxiv.org/pdf/1610.03159.pdf), Muna et al., 2016.

(The discussion below is mostly focused on scientific software, but I think it might apply much more broadly.)

I myself work mostly in bioinformatics, where the field uses a constantly frothing mixture of software packages that are maintained (or not ;) by a wide variety of people - some graduate students, some postdocs, some faculty, some staff.  We develop software in my lab (mostly [khmer](https://github.com/dib-lab/khmer/) and [sourmash](https://github.com/dib-lab/sourmash/) along with some other things) and over the years we’ve developed [tips and tricks for keeping the software going](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5142744/), mostly revolving around testing and continuous integration. But there is always something that isn’t working, and even with automation maintenance is a constant low-level burden.  Luckily very few people use our software compared to projects like Jupyter, so we are not particularly deluged by bug reports and maintenance issues.

That having been said, the constant need to maintain our open source software affects us quite a bit.  It is rare that a week goes by where *some* piece of software we maintain isn’t revealed to have a bug, or need some evolution to add a new function or command line flag. If I and the other people in the lab are on a research kick (vs coding kick), then we may not get to the problem for a while.

The same is true of training materials. We run an annual [two-week workshop on sequence analysis](http://ivory.idyll.org/blog/2015-small-batch.html), and every year we need to evolve the lessons a bit to account for new methods, new software, and new data types. While some of the lessons from 2010 may still work, my guess is that most of them have undergone bitrot.

From my own experience as well as from observing quite a few packages over the years, I’ve come to the firm conclusion that open online projects (including software and training materials) that aren’t **actively maintained** quickly decay.  And, if people are actively using a project, they will invariably find bugs and problems that need to be fixed.  This completely ignores the people that (lord forfend) actually want to help you *improve* your online projects and submit pull requests on GitHub that need to be reviewed and merged or rejected, or (if you’re really successful) the companies that want to join your project and merge in their own code.

This need for constant attention to projects, the sprawling ecosystem of amazing scientific software packages, and the relatively small community of actual maintainers, when combined, lead to the open source sustainability problem in science: we do not have the person power to keep it all running without heroic efforts. And when you couple this with the lack of clear career paths for software maintenance in science, it is clear that we cannot ethically and sustainably recruit more people into open source maintainership.

Recently a group of colleagues and I were brainstorming about another open online project (more on that later) and trying to frame it as a common pool resource problem.  We were looking for this framing because we knew that success would present a sustainability problem and were hoping to use the common pool resource framework to think about sustainability.

## Common Pool Resources, the Tragedy of the Commons, and Design Principles for Sustainability

Virtually everything I know about the common pool resource framework comes from Elinor Ostrom's *excellent* book, [Governing the Commons](https://www.amazon.com/gp/product/B015WJ1C8W).  This is a tremendously readable book that outlines the problem in a very general way, and discusses how it has been solved by communities in the past.

Briefly, in the 60s and 70s, Elinor Ostrom and her collaborators noted that the so-called "tragedy of the commons”, in which common pool resources were over-utilized by selfish actors, was not an inevitable end; that government regulation and corporatization were not the only solution to managing commonses; and that, in fact, many communities had figured out how to manage common pool resources locally.  From her own and others' case studies, Ostrom extracted eight "design principles" for sustainability of common pool resources. 

Nadia does a great rundown of this in [her blog post](https://nadiaeghbal.com/tragedy-of-the-commons), so I will just point you at the [eight design principles on Wikipedia](https://en.wikipedia.org/wiki/Elinor_Ostrom#Design_principles_for_Common_Pool_Resource_(CPR)_institution), which are very readable.

For this work, Ostrom received the 2009 Nobel prize.

## Back to open online projects

So, my colleagues and I wondered, how would this framework apply to an open online project in which we were working with *digital* resources? After all, digital resources are not consumable in the same way as physical resources, and (to borrow from the open source musings above) it’s not like someone using our project’s source code is consuming that source code in such a way that it would not be usable by others.

During this conversation, we realized the answer: effort. **The common pool resource in open online projects is effort**.

When a contributor to a project adds a feature, what are they doing? Applying effort. When a contributor files a bug report? They’re applying effort. When they file a *good* bug report? *More* effort. When they write documentation? When they test a feature? When they suggest a new feature? They’re applying effort, all of it.

But it goes deeper than that.  When you bring a new contributor into a project, you’re growing the available pool of effort. When you engage a new investor in supplying funding for an open source project, often that funding goes to increasing the amount of dedicated effort that is being applied to the project.

Of course, not all contributions are positive in their effect on effort, as [I wrote about here](http://ivory.idyll.org/blog/2018-how-open-is-too-open.html). Some contributions (new feature proposals, or bad bug reports) *cost* the project more net effort than they bring. Significant feature additions that don’t come with contributions to the underlying maintenance of the project can be very costly to the core project maintainers, if only in terms of reviewing and rejecting. And underpinning all of this is the low susurration of maintenance needs: as I outline above, maintenance needs act as a *net drag* on project effort.

At #GCCBOSC, Fernando Perez riffed on this same idea a bit, and pointed out that there are other extractive approaches being used by people who recruit from open source projects. Many companies recruit out of open source communities, and in a simple sense they are mining the effort that the open source community put into training the people in question.

If you look at the list of [eight design principles for a sustainable common pool resource](https://en.wikipedia.org/wiki/Elinor_Ostrom#Design_principles_for_Common_Pool_Resource_(CPR)_institution), and define “effort” as the common pool resource in question, you see that they apply more or less directly to the way open source projects have evolved:

1. Who is a contributor to an open source project is clearly defined.
2. Effort in open online projects is applied locally, to the needs of the project.
3. Many open source projects follow the rule that those who contribute participate in design decisions.
4. People who contribute significantly are often invited to join the project officially in more significant decision making roles.
5. There is often a range of sanctions for contributors who violate community rules.
6. Most conflicts are handled internally to the project, rather than being escalated to the legal system.
7. Most conflicts are handled by lightweight methods and discussions.
8. Many open source contributors contribute to multiple projects, e.g. in the Python ecosystem there are many projects to which the same people contribute. In this sense the Python ecosystem can be considered a larger-scale CPR of effort with many locally articulated CPRs like "core CPython dev" and "numerical computing/numpy library".

It seems likely to me that this will generalize to open communities of many kinds.

## So, uhh, what does this all mean?

Since my colleagues and I started thinking this way, and I started looking at open source projects and other online community resources through this lens, it has proven to be a really nice simple framework for me to think about open source sustainability. The entire [“How open is too open?” blog post](http://ivory.idyll.org/blog/2018-how-open-is-too-open.html) came directly out of this thinking! It also gives a straightforward explanation for why recruiting more people to your project is viewed so positively: you’re increasing the pool of effort available for allocation to the project's needs; this further explains why Codes of Conduct and contributor guidelines are becoming so important, because they enable you to recruit and retain effort over the long term.

By itself, this perspective doesn’t solve any problems. But it does tie into a really nice collection of case studies, and a lot of deep thinking from the CPR literature about how to sustainably manage community resources.

More specifically, in the context of generic open online projects, it suggests a few points of consideration.

First, the pool of effort available to an open online project needs to be preserved against encroachment. For successful projects, this means that potential contributions should evaluated in terms of their net likely impact on the pool of effort. While this principle is already enshrined for technical contributions (see: “technical debt”), it should also be considered for bug reports and feature suggestions. (Many projects already do this, of course!)

Second, the cost of the constant maintenance needs (code, documentation, installation, etc.) on the pool of available effort needs to be taken into account. Contributions of new features that do not come with effort applied to maintenance should be carefully considered - is this new contributor likely to stick around? Can they and will they devote some effort to maintenance? If not, maybe those contributions should be deferred in favor of contributions that add maintenance effort to the project, e.g. via partnerships.

Third, training and nurturing new contributors should be considered in the cold hard light of increasing the available effort over the long term.  [But contributor psychology is tricky](https://twitter.com/havocp/status/988592572258975744), so it may not be simple to predict who will stick around. Some projects have excellent incubators, like the [Python Core Mentorship Program](https://www.python.org/dev/core-mentorship/), where people who are interested in applying their effort to recruiting new contributors can do so.  I suspect that considerations like creating a friendly environment and laying out expectations like “we’re happy to help you get up to speed on both adding new features AND FIXING BUGS so that you contribute to our maintenance effort” might help point new contributors in the right direction. In the long term, the health of the community *is* the health of the project.

Fourth, there are some interesting governance implications around allowing all or most of the resource appropriators to participate in decision making. I need to dig more into this, but, briefly, I think projects should formally lay out what level of investment and contribution is rewarded with what kind of operational, policy making, and constitutional decision making authority.

Fifth, defining maturity metrics may help with setting funder expectations and obtaining investments. From experience, the primary goal of many funders is to chart a path to *project sustainability*.  I think the above design principles (and the case studies from CPR) can serve as a foundation for a set of project maturity rubrics that connect to sustainability. If a project is writing a funding proposal, they could articulate which design principles they’re targeting for improvement and how that ties into a broader framework of sustainability. For example, a project could say “right now we are worried about our ability to onboard many new contributors, and we’re starting to get some inquiries from companies about contributing on a larger scale; we’d like to build out our governance principles and improve our guidance for contributors, so that new contributors and investors have clear expectations about what level of investment is expected from them.” I suspect funders would welcome this level of clarity :).

##  Does the Common Pool Resource framework for “effort" really fit open source projects, and open online projects generally?

Good question! I am by no means knowledgeable about CPR, and I have a _lot_ of reading ahead of me. I can see a few disconnects with the CPR framework, and I need to work through those; but I’m really, really excited by how well it fits with my intuition about how open source projects work.  Having a conceptual framework like CPR is letting me revisit my observations and fit them into a neater picture and maybe reach different conclusions about fixes. Again, check out the [“How open is too open?”](http://ivory.idyll.org/blog/2018-how-open-is-too-open.html) blog post for an example of this.

Something else I really want to try is to engage in case studies of open source projects to see how practices in real living sustained open source projects do and don’t fit this framework. I have a sabbatical opportunity coming up in a few years… hmm….

One of the things I really like about this framework is that it divorces open source project thinking from the fuzzy woo that I *used* to value so much about free and open source software -- “we should be a big happy family and all work together!” starts to pale in the face of maintainers' lives getting destroyed by their commitment to open. This intersects with a comment that Fernando Perez made: open source projects really *do* run a significant part of the world these days, and  we cannot afford to think about any part of them - including sustainability - in the informal way we are used to. We should hold ourselves accountable to the goal of building sustainable open projects, and lay out a realistic and hard-nosed framework by which the investors with money (the tech companies and academic communities that depend on our toolkits) can help foster that sustainability. To be clear, in my view **it should not be the job of (e.g.) Google to figure out how to contribute to our sustainability; it should be our job to tell them how they can help us, and then follow through when they work with us.** Many important projects are really incapable of doing this at the moment, however, and in any case there are no simple solutions in this space. But maybe CPR is a framework for thinking about it. We shall see!

On a personal level, it's interesting to look back at my various open source project efforts (none of which are sustainable/sustained :) and see why they fail to meet the design principles laid out by Ostrom. That may be another blog post down the road...

--titus

P.S. I'd like to especially thank Cameron Neylon and Michael Nielsen for pointing Elinor Ostrom's work out to me a few years back! I would also like to thank Nadia Eghbal for all of her explorations of this topic - the framing she provided in her blog posts is really instrumental to this post, and I hope to be fellow travelers going forward :)

P.P.S. While I'm dropping names, I got excellent feedback and suggestions on this topic from many people, including Luiz Irber, Katy Huff, Katie Mack, Cory Doctorow, Jake VanderPlas, Tracy Teal, Fernando Perez, Michael Crusoe, and Matthew Turk - thank you all! Several of these conversations were enabled by #scifoo18 and #gccbosc, so thanks, SciFoo and BOSC!
