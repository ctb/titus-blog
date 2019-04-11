Title: Things to think about when developing shotgun metagenome classifiers
Date: 2019-04-11
Category: science
Tags: sourmash,minhash,metagenomics
Slug: 2019-developing-metagenome-classifiers
Authors: C. Titus Brown
Summary: Thoughts on goals and tradeoffs in classifying shotgun metagenome data.

So I was talking to someone about how we think about benchmarking and
developing [sourmash](https://sourmash.readthedocs.io), and then it
got long and kind of interesting, so I decided to write it up as a
blog post.

(I asked Luiz Irber for comments, and he had the best reaction ever:
"many feels, no time to write them, mostly agree, publish")

---

When benchmarking, often people end up comparing *their* tool to tools developed to tackle different problems. To no big surprise, the first tool ends up winning out.

Here are questions that we asked ourselves, or decisions we made implicitly, when developing sourmash. Many of these have direct or indirect implications for benchmarking.

**Are we developing a library, a command line application, or a Web site?** It's hard to do more than one at a time well. We've decided to focus on command line with sourmash, as a light wrapping around a Python library (which was a light wrapping around a C++ library, and will soon be a light wrapping around a Rust library). I think after 3 years we've reached a level of maturity where we could also support a Web site (but we don't really have the focus in the lab to do a good job of it, and would prefer to support someone else if they want to do it).

**How sensitive to coverage do we want to be?** Phillip Brooks showed that sourmash is really specific and very sensitive, until you have fewer than (approximately) 10,000 reads from your genome of interest. Once your data set has fewer than 10,000 reads from a genome in it, we can't really detect that genome. (This is of course a tradeoff in terms of speed, underlying approach, database size, etc., and we're happy with that tradeoff.)

**Do we envision our tool being used in isolation, or as one part of an exploratory pipeline?** We are firmly in the camp of using sourmash to do hypothesis generation, following which more compute intensive approaches are probably appropriate. For example, sourmash can tell you *which* known species are in your metagenome, but we haven't focused too much on assessing *how much of those species' genomes* are there - after all, that's (fairly) easy to do once you narrow down the list of possible genomes. And again, there are tradeoffs with many of the other design considerations below. But if we wanted to have a single software package that did everything we would design it differently (and it would be a lot harder, since you'd probably want to use multiple methods).

**Do we envision our tool being used by programmers?** We really like having scriptable tools in our lab. That means the tool has decent command line behavior, has a high level Python API, and consumes and emits standard formats. This may not be what everyone wants to focus on though!

**Do we care about speed?** Premature optimization can make your codebase ugly and complex. We've chosen (for now) to instead go with a fairly simple code base, which we then test the bejeezus out of. It supports optimization (Luiz Irber has done some amazing things with a profiler :) but we are against trading simple code for speed, because this is a research platform.

**What are our desired memory, disk, and time performance metrics?** Do we care about one over the other? In general, we have chosen to prioritize low memory over performance, and performance over low disk space. But this isn't clear cut, and depends a lot on what methods we find interesting and implementable.

**What's our desired database resolution?** Do we want ALL the genomes? Or just some genomes? We made the decision with sourmash to go for ALL the genomes. This causes problems when you think about the next few questions...

**What's our desired taxonomic resolution?** We implicitly settled on strain-level resolution as our goal for `sourmash gather`, largely because of the algorithm we chose. (It works quite well for that!) But, unsurprisingly, `sourmash gather` performs quite poorly when looking at organisms from novel genera and families. It's actually quite hard to do both well.

**Who updates the database?** And is it easy and straightforward to build new databases, or not?  We worked hard on a friendly and flexible database building toolchain, because we expect new genomes to come out on a (very) regular basis (and we wanted to include them in our databases, based on our desired resolution).

**Do we want to support private databases, or not?** We really like the idea of people using our tool in the privacy of their own lab to search their own collections of genomes. This means that we need to forego certain requirements (e.g. an NCBI taxid).

**Do we want a big centralized database, or not?** One of our big concerns about models for database distribution & update that require one massive database, that can only realistically be updated by one group, is that they tend to go stale over time (as the group loses interest, etc.) Maintenance is not the strong suit of academic researchers :). So Luiz Irber has been working on IPFS and Dat-based models for database decentralization. This will (soon) permit incremental database updates without massive database download, among other things.

**What's our publication model?** Do we want others to use our software for cool things? Or are we trying to publish our own innovative methods that we try and get into high impact-factor journals? Are we building a platform for others to build their own tools? Are we playing around with different methods and ideas and so on? We're not particularly interested in high-impact factor journals for sourmash, and we have a surprising number of people just using it do their own thing, so we've opted for providing citation handles via JOSS and F1000Research.

**How do we decide what functionality belongs in sourmash?** Did we have explicit use cases that we decided up front? Or do we [discover them as we go](https://github.com/dib-lab/sourmash/issues/208)? I'm much more comfortable doing iterations, finding users, and waiting for inspiration to strike, than I am in planning out sourmash years in advance. But then again, I'm an academic researcher and this fits our needs; we're not trying to serve a particular community.

**What's our contribution model?** Are you interested in supporting collaboration and community development? Or are you interested in limiting external contributions to potential use cases? We are OK interested in both, but it adds a certain level of chaos and coordination challenges to the situation.

--titus
