Title: The Open Source Anti-Sisyphean League
Date: 2018-07-09
Category: science
Tags: sustainability,software,cpr
Slug: 2018-anti-sisyphean-league
Authors: C. Titus Brown
Summary: We need an Open Source Anti-Sisyphean League!

(This title commonsed from Cory Doctorow)

I’ve [been thinking about the design principles for sustainable open online resources](http://ivory.idyll.org/blog/2018-oss-framework-cpr.html) a lot lately, and I really like a phrase that Cory Doctorow came up with: “an open source anti-Sisyphean league.” And I am wondering if this is one of the major motivations for community formation around open online resources.

Whence “Sisyphean”? Sisyphus is a figure from Greek mythology; to quote [Wikipedia](https://en.wikipedia.org/wiki/Sisyphus), "He was punished for his self-aggrandizing craftiness and deceitfulness by being forced to roll an immense boulder up a hill only for it to roll down when it nears the top, repeating this action for eternity. [...] tasks that are both laborious and futile are therefore described as **Sisyphean**."

When I was pitching the Common Pool Resource framework to Cory, and trying to relate it to the shared community labor meme in [_Walkaway_](https://en.wikipedia.org/wiki/Walkaway_(Doctorow_novel)), one of the points that came up is that there is a non-trivial amount of maintenance labor that simply needs to be done by *somebody* to keep the project going. In open source projects this can range from keeping the continuous integration running to curating new issues to dealing with tests broken by from some dependency upgrade; in wikis, spam removal and link fixing qualify; and in the Carpentries, lesson maintenance is an ongoing burden. Riffing on this idea, Cory said, “It’s like we need an ‘effin open source anti-Sisyphean League!” to handle these laborious and never-ending issues *in common*.

So perhaps one organizing principle in communities that sustain open online resources is that they are partly organized around these maintenance issues?

I think Cory is taking it further, tho.  I took the “league” term as referring to the idea that, in open source, another organizing principle is that there is some number of **common** goals that simply need to be done by **someone**. In a perfectly spherical world where IP restrictions didn’t exist, knowledge and code could flow freely from project to project, so when someone solved a problem like, oh, say, [building a system to link and distribute content via a distributed network of servers](https://en.wikipedia.org/wiki/World_Wide_Web), that solution could be reused and remixed be everyone. (It's just crazy enough to work!) And, while there might be different trial solutions to any given problem, the communities behind those solutions would be able to learn from each other and iterate and maybe eventually converge to a small set of high quality solutions.

This bears a close resemblance to how my favorite open source communities work. When I look at the Python world, I see a plethora of small experimental Python modules that solve various problems, and a much smaller, higher quality collection of maintained modules. It’s relatively rare for me to have to _choose_ between two Python libraries for a particular task, because usually there is only one well maintained one. When I do have to choose, it’s either because it’s in an expanding area (Web dev, back when), or because the Python stdlib has an old library that is kept around for reasons of backwards compatibility, or because there are still really strong differing opinions on how to handle that particular use case (see: argparse and the plethora of command line option parsers).

I’d guess that in any open community, there are several sources of friction that prevent more rapid convergence to a single solution. Poor awareness and/or bad communication are definitely one set of reasons - sometimes it’s hard to find the right search keywords to discover a project that does what you need, or you find that the project didn’t document itself properly.  Another source of anti-convergence friction is stability: some people are going to go with a suboptimal solution that has been around for a while, because the existing community and documentation is so good, or maybe just because they’re familiar with it. Another obvious friction is ego and personality, where people refuse to adopt another community’s approach because key people in one community don’t like key people in the other community at an interpersonal level. And, of course, there may actually *be* several near-optimal solutions to any given problem, in which case multiple stable solutions may exist.  Perhaps another is honest disagreement on approach - for example, while I am certainly aware of the Carpentry genomics lessons, we have chosen a somewhat different style and delivery format for [our ANGUS 2018 genomics lessons](https://angus.readthedocs.io/en/2018), because we find it fits our needs better. (But here, I am hoping that we eventually converge, and we’re doing experiments to figure out what does and doesn’t work in both sets of lessons.) 

(Interestingly, academia has failed quite spectacularly in the area of converging solutions. The plethora of virtually identical bioinformatics solutions to any given problem (mapping! annotation!) largely exists because in academia we are incentivized more for the **appearance** of knowledge production than for *actual* progress on hard problems. Many of my colleagues persist in working on the really hard problems out of idealism, but it’s a long and somewhat thankless road! In academia, we have adopted many of the bad approaches above: we communicate about solutions poorly with high latency (publications anyone?), we have little incentive to shift to new & better solutions, and ego and self-promotion run rampant within academic circles.)

On the flip side, you can see an amazing convergence in many places in the more practical side of computing. The convergence on R and Python as the data science lingua francas has been amazing - yes, there are still two languages, but even there I am starting to notice that approaches are converging, helped along by cross-language interlocutors. (Any bets on how long it will take for the #rstats folk to converge on [vega for viz?](https://rud.is/b/2016/02/28/a-tale-of-two-charting-paradigms-vega-lite-vs-rggplot2/)) The rise of Docker and convergence on Kubernetes has been astounding. The speed with which the bioinformatics community seems to have adopted [bioconda](https://bioconda.github.io/) is astonishing -  my entire lab shifted to using it overnight, AFAICT.

Returning to the [Common Pool Resource framework](http://ivory.idyll.org/blog/2018-oss-framework-cpr.html), if we view "effort" or “labor” as the common pool resource being managed in the creation and maintenance of open online resources, then what we are trying to do here is _minimize redundant labor_ being used to solve problems of collective interest . To again borrow from Cory, "We only want to push that effin' rock up the hill *once*, if we can manage it."

## So what really isn’t obvious about this, Dr. Brown?

If you were to say “but this is all obvious!”, I would agree that this anti-Sisyphean organizing principle is entirely obvious and clear to me in retrospect.

Moreover, it can be rephrased in several ways (practical utility suggests that fewer solutions are better, all other things being equal! ecosystem principles suggest that a winner-take-all approach is likely when information flows freely!)

But in some sense that’s the point of writing this blog post: we should articulate the obvious stuff when we’re thinking about design principles for open online resources! This is for two reasons. First, if it *doesn’t* fit, then best to find counterexamples early. Second, if it *does* fit, then by articulating it we are not only communicating it clearly to others but also building a foundation for the next steps of inquiry.

For example, I have questions! How does a community coalesce around recognition of a common goal? How do we distinguish between global common goals (“how do we enable flexible viz in data science?”) vs more local goals (“my local bioinformatics community really needs a library to help me visualize this type of data”)? What is the community lifecycle beyond creation, e.g. maintenance, sustainability, merging, and forking? What are the unique properties of open online resources (or [digital public goods, as Nadia Eghbal calls them](https://medium.com/@nayafia/an-alternate-ending-to-the-tragedy-of-the-commons-446b4e960887)) that makes them different - is it “just” the ease with which digital resources can spread in a networked environment, or is there more to it?

Inquiring minds want to know!

best,
—titus

p.s A really interesting question is, are there common organizing principles around building these open source anti-Sisyphean leagues? Gosh I sure hope someone's asking that!

p.p.s. I will abandon the tortured “open online resources” term soon, I promise - I have been discovering a whole new world of terminology that fits this idea much better, and it seems only appropriate to try to coalesce around some common terminology in this space. See the entire above post for reasons. :)

p.p.s. Nadia Eghbal pointed me at this fascinating post by Jill Carlson: ["Free Company: the Decentralized Future of Work"](https://www.tokendaily.co/blog/free-company), which comes at the same question from a different angle.
