Title: The #CommonsPilot kicks off!!
Date: 2017-12-11
Category: science
Tags: commonspilot, data commons
Slug: 2017-commonspilot-kickoff
Authors: C. Titus Brown
Summary: The start of a new Data Commons effort!

(Just in case it's not clear, I do not speak for the NIH or for the Data Commons Pilot Phase Consortium in this blog post! These are my own views and perspectives, as always.)

I'm just coming back from the #CommonsPilot kickoff meeting. This was our first face-to-face meeting on the Data Commons Pilot effort, which is a new trans-NIH effort.

The Data Commons Pilot started with [the posting of a funding call](https://commonfund.nih.gov/sites/default/files/RM-17-026_CommonsPilotPhase.pdf) to assemble a Pilot Phase Consortium using a little-known NIH funding mechanism called an "Other Transactions" agreement.  This is a fundamentally different award system from grants, contracts, and cooperative agreements: it lets the NIH interact closely with awardees, adjust funding as needed on very short time scale, and otherwise gives them a level of engagement with the actual work that I've never seen before.

I, along with many others, applied to this funding call (I'll be posting our initial application soon!) and after many trials and tribbleations I ended up being selected to work on training and outreach.  Since then I've also become involved in internal coordination, which dovetails nicely with the training/outreach role.

The overall structure of the Data Commons Pilot Phase Consortium is hard to explain and not fully worked out yet, but we have a bunch of things that kind of resemble focus groups, called "Key Capabilities", that correspond to elements of the funding call -- we've put together [a draft Web site](https://hackmd.io/s/HJKUu1WWf) that lists them all.  For example, Key Capability 2 is "GUIDs" - this group of nice people is going to be concerned with identification of "objects" in Data Commonses.  Likewise, there's a Scientific Use Cases KC (KC8) that is focused on what researchers and clinicians actually want to *do*.

(The complete [list of awardees is here](https://commonfund.nih.gov/bd2k/commons/awardees).)

This kickoff meeting was ...interesting. There were about 100 people (NIH folk, data stewards, OT awardees, cloud providers, and others) at the meeting, and the goal was to dig in to what we actually needed to do during the first 180 days of this effort - aka Pilot Phase I.  (Stay tuned on that front.)  We managed to put together something that was more ["Unconference style"](https://en.wikipedia.org/wiki/Unconference) than the typical NIH organizational meeting, and this resulted in what I would call "chaos lite", which was not uniformly enjoyable but also not uniformly miserable.  I'm not sure how close we came to actually nailing down what we needed to do, but we are certainly closer to it than we were before!

## So... really, what *is* a Data Commons?

No one really knows, in detail.  Let's start there!

(I recalled that Cameron Neylon had written about this, and a quick google search found [this post from 2008](http://cameronneylon.net/blog/how-do-we-build-the-science-data-commons-a-proposal-for-a-scifoo-session/).  (I find it grimly amusing how many of the links in his blog post no longer work...)  Some pretty good stuff in there!) I don't know of earlier mentions of the Commons, but a research commons has been being discussed for about a decade.

What is clear from my 2017 vantage point is that a data commons should provide some combination of tools, data, and compute infrastructure, so that people can bring their own tools and bring their own data and combine it with other tools and other data to do data analysis.  In the context of a *biomedical* data commons we have to also be cognizant of legal and ethical issues surrounding access to and use of controlled data, which was a pretty big topic for us (there's a whole Key Capability devoted just to that - [see KC6!](https://hackmd.io/s/HJKUu1WWf#kc6-research-ethics-privacy-and-security))

There are, in fact, many biomedical data commons efforts - e.g. the NCI [Genomic Data Commons](https://gdc.cancer.gov/), which shares a number of participants with the #CommonsPilot, and others that I discovered just this week (e.g. [the Analysis Commons](https://analysiscommons.com/)).  So *this* Data Commons (#CommonsPilot, to be clear) is just one of many.  And I think that has interesting implications that I'm only beginning to appreciate.

Something else that has changed since Cameron's 2008 blog post is the power and ubiquity of the cloud platforms. "Cloud" is now an everyday word, and many researchers, academic and industry and nonprofit, are using it every day.  So it has become much clearer that cloud is one future of biomedical compute, if not the only one.

(I would like to make it clear that Bitcoin *is not part of the #CommonsPilot effort.* Just in case anyone was wondering how buzzword compliant we were going to try to be.)

But this still leaves us at a bit of an impasse.  OK, so we're talking about tools, data, and compute infrastructure... in the cloud... that leaves a lot of room :).

Things that I haven't mentioned yet, that are explicitly or implicitly part of the Commons Pilot effort *as I see it*.

* openness.   We *must* build an open platform to enable a true commons that is accessible to everyone, vice issues of controlled data access. See: [Commons](https://en.wikipedia.org/wiki/Commons).

* eventual community governance, in some shape or form. (Geoff Bilder, Jennifer Lin, and Cameron Neylon cover this brilliantly in their [Principles for Open Scholarly Infrastructure](https://cameronneylon.net/blog/principles-for-open-scholarly-infrastructures/).)

* multi-tenant. This isn't going to run just on one cloud provider, or one HPC.

* platform mentality. This is gonna have to be a platform, folks, and we're gonna have to dogfood it. ([obligatory link to Yegge rant](https://plus.google.com/+RipRowan/posts/eVeouesvaVX))

* larger than any one funding organization.  This is necessary for long-term sustainability reasons, but also is an important requirement for a Commons in the first place.  There may be disproportionate inputs from certain funders at the beginning, but ultimately I suspect that any Commons will need to be a meeting place for research writ large - which inevitably means not only NIH funded researchers, not just US researchers, but researchers world wide.

I haven't quite wrapped my head around the scope that these various requirements imply, but I think it becomes quite interesting in its implications.  More on that as I noodle.

## Why are Commonses needed, and what would a successful #CommonsPilot enable?

Perhaps my favorite section of the #CommonsPilot meeting was the brainstorming bit around why we needed a Commons, and what this effort could enable (as part of the larger Commons ecosystem).  Here, in no particular order, is what we collectively came up with.  (David Siedzik ran the session very capably!)

(As I write up the list below, I'd like to point out that this is really very incomplete. We only did this exercise for about 30 minutes, and many important issues were raised afterwards that weren't captured by this exercise. So this is definitely incomplete and moreover only reflects my memory and notes.  Riff on it as you will in comments!)

* The current scale of data overwhelms naive/simple platforms.
* The #CommonsPilot must enable access to restricted data in a more uniform way, such that e.g. cross-data set integration becomes more possible.
* The #CommonsPilot must have a user interface for browsing and exploratory investigation.
* The #CommonsPilot will enable alignments of approaches across data sets.
* Integration of tools and data is much easier in a #Commons.
* Distribution and standardization of tools, data formats, and metadata will enhance robustness of analyses
* There will be a community of users that will drive extensions to and enhancement of the platform over time.
* Time to results will decrease as we more and more effectively employ compute across large clouds, and reuse previous results.
* We expect standardization around formats and approaches, writ large (that is, the #CommonsPilot will contribute significantly to the refinement and deployment of standards and conventions).
* The #CommonsPilot will expand accessibility of tools, compute, and data to many more scientists.
* We hope to reduce redundant and repeated analyses where it makes sense.
* Methods sharing will happen more, if we are successful!
* Lower costs to data analysis, and lower barriers to doing research as a result.
* An enhanced ability to share in new ways that we can't fully appreciate yet.
* A resulting encouragement and development of new types of questions and inquiry.
* Enhanced sustainability of data as a currency in research.
* We hope to enhance and extend the life cycle of data.
* We hope to enable comparison and benchmarking of approaches on a common platform.
* We hope to help shape policy by demonstrating the value of cloud, and the value of open.
* More ethical and effective use of more (all!?) data
* More robust security/auditing of data access and tool use.
* Enhanced training and documentation around responsible conduct of computational research.

So as you can see it's a pretty unambitious effort and I wouldn't be at all surprised if we were done in a year.

I'd love to explore these issues in comments or in blog posts that other people write about why we're wrong, or incomplete, or short-sighted, or too visionary. Fair game, folks - go for it!

## How open are we gonna be about all of this?

That's a good question and I have two answers:

1. We are hoping to be more open than ever before.  As a sign of this, Vivien Bonazzi claims that at least one loud-mouthed open science advocate is involved in the effort. I'll let you know who it is when I find out myself.

2. Not as open as I'd like to be, and for good reasons. While this effort *is* partly about building a platform for community, and community engagement will be an intrinsic part of this effort (more on that, sooner or later!), there are contractual issues and NIH requirements that need to be met.  Moreover, we need to thread the needle of permitting internal frank discussions while promoting external engagement.

So we'll see!

--titus


