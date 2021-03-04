Title: sourmash 4.0 is now available! Low low cost if you buy now!
Date: 2021-03-02
Category: science
Tags: sourmash, software, release
Slug: 2021-sourmash-v4-released
Authors: C. Titus Brown
Summary: sourmash v4.0.0 is here!

So, we just [released sourmash 4.0](https://github.com/dib-lab/sourmash/releases/tag/v4.0.0), our Python- and Rust-based open source tool for k-mer sketch-based analysis of metagenomes and genomes.

The high notes of this release are -

* much better user experience design around creating and storing sketches;
* removal of several obsolete features that were holding us back;
* improved default Python API;

but they really don't particularly matter, to be honest :).

What's most cool about this release is...

## Semantic versioning, feature compatibility, and deprecations

...it's a release where we purposely broke compatibility with previous versions, and went through a whole deprecation effort, and documented it all.

We use semantic versioning for sourmash. What this means is that major versions of sourmash (v3, v4, etc.) can break backwards compatibility, but minor versions (v3.1, v3.2) cannot. In practical terms, it means that when you use sourmash in a workflow or application, you can pin your software install to the major version without worrying about breakage - e.g. specify `sourmash >=3,<4`.

In the case of v3.x and v4.0, we systematically upgraded and improved sourmash performance and features during 3.x, and reserved breaking features for 4.0. Further, we added warnings and deprecations to v3.5 about features that were *going* to break in v4.0. Then we wrote a [migration guide](https://sourmash.readthedocs.io/en/latest/support.html#migrating-from-sourmash-v3-x-to-sourmash-v4-x).

It was a lot of work! I probably put 40-80 hours into just this aspect of things over the last three months.

So... why did we do it?

## Why did we do all this work?

We're not really sure how many people use sourmash outside the lab, but _in_ the lab, we use it quite a bit. It's a pretty effective Swiss army knife tool for hacking and slashing at sequencing data, and a lot of basic questions about taxonomy and k-mer content can be answered with a little creative sourmashing.

And we have 5-6 workflows and pipelines that rely on sourmash.

So the first answer is that we did it for ourselves, so that we could robustly rely on sourmash in our workflows.

But the more complete answer is that we wanted to go through the semantic versioning & deprecation workflow and user communication/documentation stuff, so that we could just bake it into project expectations (for this project and for others).  And we wanted to do this because we think this is the right way to do scientific software, and we wanted to communicate our expectations about changing sourmash behavior clearly and unambiguously.

## What do we get out of it?

We're signaling to our current and prospective user base that we are open to their concerns.  This results in improved user communication: for example, after our first release candidate we got some feedback that caused us to explicitly note that (1) numerical results shouldn't change and (2) old sourmash databases are still compatible with the new version.

We're providing a path to ourselves, as well as future developers (and future us), on how to think about pacing our changes to the software. On the one hand it's frustrating to delay cool and important changes to the software because we're not yet ready to release a big version; on the other hand, we took the time to more completely bake some of the new features and did several rounds of documentation improvement.

And, frankly, I think we ended up with better code reviews and development processes internally, because we had to think explicitly about how each particular change would impact users. (FWIW, our best guess is that we have about 1,000 users.)

## What are the downsides?

Well, it was a lot of work :). And investment in the future of an academic software project is always a gamble!

Also, we don't have the person power to maintain multiple releases of sourmash, so it does mean we're more or less abandoning people who want to continue using sourmash v3.x. We didn't break any particularly big features, but it does require effort on our users' side to upgrade, so maybe some people will hold off because of that. And while I'll backport fixes to really important bugs if we have any in the next few months, we don't intend to backport performance improvements or new features. So maybe users will suffer a bit from that.

## What's next?

We have a lot of new features that will probably come out in v4.1 and beyond, now that we can switch our efforts to that! Lots of exciting stuff is coming in the areas of protein k-mers and massive-scale database search!

I'm already looking forward to v5, where we can remove some of the features that we deprecated for v4.0.

And I think it's more than time for a new JOSS paper...

--titus

