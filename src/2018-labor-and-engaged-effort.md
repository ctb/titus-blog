Title: "Labor" and "Engaged effort"
Date: 2018-08-10
Category: science
Tags: sustainability,software,cpr
Slug: 2018-labor-and-engaged-effort
Authors: C. Titus Brown
Summary: Are "effort" and "labor" the same?

A few blog posts back, [I suggested that "effort" is a common pool resource to be managed by communities building open online resources](http://ivory.idyll.org/blog/2018-oss-framework-cpr.html), such as open source projects or other "digital commons" projects.  The logic was roughly thus: there is clearly a common pool resource at work in these projects - but what is it?  A common pool resource must be both [*non-excludable* and *rivalrous*](https://en.wikipedia.org/wiki/Club_good). This means that the resource is consumable but you cannot easily limit who consumes it in quantity.  Timber in a shared forest, irrigation water shared amongst many farmers, and grass in a commons are all examples.

But when you start looking at *data*, *source code*, and other resources managed in open online projects, it is clear that they are more like public goods: they can be consumed by anyone, and the costs of distribution are minimal. And yet we know from experience that there are costs associated with these projects, and it's fairly clear that ["maintenance" is one source of costs](http://ivory.idyll.org/blog/2018-anti-sisyphean-league.html) (but not the only source).  "Effort" was my first attempt to name this.

One of the comments I've gotten from multiple people is that "labor" seems like a better word. After all, isn't that what "effort" means? Someone is putting in labor?

## Labor and effort and investment

Let's start by pointing out that I know very little about economics :). So, reader beware.

To me, the term "labor" implies a significant degree of fungibility: anyone can do the work, and the challenge is to find and support *someone*. If labor is a resource to be managed, then it seems to me we are saying (1) there is some fixed pool of labor available, either directly (funds already allocated) or indirectly (fixed pool of funds); (2) the challenge is to allocate that fixed pool of labor among the tasks to be done; and (3) it is not necessarily hard to quickly find someone to perform the labor.

In contrast, when I look at open source projects, I see that while there is some pool of labor available, it is not necessarily fixed (because there is volunteer labor available, given enthusiasm or engagement); and that while we do wish to allocate it amongst the tasks to be done, the labor involved in deciding the allocation is a big part of the challenge; and that it is not easy to quickly find someone to perform the labor, since often rather specialized skills and experience are required.

Open source projects solve these challenges by inviting enthusiasm and supporting self determination of task allocation; communicating in a bottom-up way about tasks that need to be done; and trying to grow the pool of people with specialized skills available to the project over time. This places the pool of "labor" itself in charge of the project direct, which I think is connected to the self-governance aspect of managing CPRs.

So I'm using "effort" to differentiate that kind of "engaged" labor from other labor. It seems like a significant distinction to me.

## Engaged effort and maintenance

In [Ostrom's book](https://www.amazon.com/gp/product/B015WJ1C8W), there are a number of riveting examples of maintenance effort being applied by locally organized efforts. To quote from one (emphasis mine):

> The Bacarra-Vinter federation of *zanjeras* constructs
> and maintains a 100-meter-long brush dam that spans the
> Bacarra-Vinter river \[in the Philippines\]. ... During the
> rainy season each year, the river destroys the federation's
> dam ... During some years the dam will be destroyed three or
> four times.
> 
> \[ ... details of how the dam is rebuilt ... \]
> 
> In terms of the contemporary schedule of 5 days per week, 
> this amounts to **two months of work supplied without direct
> monetary payment**.
 
This is a pretty significant investment of labor! And while there is probably some sociology going on here around ownership - people are more willing to invest labor in things they have ownership in - this level of labor must be tied to pretty strong economic incentives. (In this case, it's that the dams are a critical part of the irrigation system that the *zanjeras* depend upon for farming: no dams, no irrigation, no crops.)

This, to me, is akin to what goes on in open source projects. There is an understanding in the community that [a common problem must be solved](http://ivory.idyll.org/blog/2018-anti-sisyphean-league.html), and so the community solves it - because they gain some kind of utility from the continuation of the project.

## Is effort non-excludable on open online projects?

Another question that I've been thinking about: is "effort" really non-excludable on open online projects? That would mean that anyone in the project's community would be able to appropriate the effort of anyone else on the project. Is that true? How does that work, if so??

Let's back up: one of the implications of claiming that "effort" is a common pool resource in open online projects is that it's non-excludable: it can be appropriated by other people on the project. As a common resource, it would need to be managed by the project rather than managed individually.

Is this true?

I think it actually is. This in fact corresponds to one of the unwritten rules about how open source projects work: when a bug is discovered and posted to the issue tracker, an open source project will immediately evaluate and prioritize working on it (or not). In turn, someone who is devoting their time to the project will pick it up and work on it; the community thus appropriates the effort of someone.  The fact that it's all "voluntary" isn't a relevant distinction, since the culture of open source projects virtually guarantees that someone will pick up and fix important bugs.  This bears some interesting resemblances to how the *zanjeras* above works: a committee figures out if the dam needs to be rebuilt, and then the community of contributors goes forth and rebuilds it.

This culture corresponds directly with the problem of "maintainer burnout" on open source projects, where the maintenance burden becomes a crushing burden on the core contributors. In effect, a project that doesn't steward the common pool resource of engaged effort properly leads to a depleted resource pool of that effort.  (This doesn't explain the part where maintainers continue to contribute effort well past the point of personal sustainability; I think that could be explained [by some aspect of the community engagement around solving shared problems](http://ivory.idyll.org/blog/2018-anti-sisyphean-league.html), but I need to think more about that.)

Interestingly, another parallel that emerges from this perspective is the intersection of community governance with community labor: those who put effort in to prioritizing the bug and fixing it are those who help decide which bugs are going to be fixed next and which features are going to be added. Or, in other words, those who contribute effort become part of the community that decides how to allocate that effort in the future.

## What are the implications, good sir?

If this is not an incorrect perspective, I think there are lots of implications for the active design and growth of open online communities, and more specifically for governance design. One obvious one is that the pool of engaged effort on a project is the central resource to be preserved against encroachment, and that maintaining and growing this effort is a key to sustainability.

Comments and thoughts welcome as always!

--titus

p.s. Thanks especially to Carly Strasser for her quizzical looks and
probing questions on this topic, Josh Greenberg for pointing me at
club goods and this topic more generally, and Adam Resnick, Stan
Ahalt, and Matthew Trunnell for the initial insight!
