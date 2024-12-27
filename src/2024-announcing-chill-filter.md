Title: Announcing: the chill-filter Web site - DNA sample composition at a glance!
Date: 2024-12-27
Category: science
Tags: sourmash, branchwater, chill-filter
Slug: 2024-announcing-chill-filter
Authors: C. Titus Brown
Summary: what's in my sample, dude?

Hi all,

I've spent the last few weeks working on a DNA sample screening Web
site, named "chill-filter". The goal is to support rapid, lightweight
compositional analysis of shotgun sequencing DNA data sets -
basically, "what's in my sample?!"

You can play with it here:
[chill-filter.sourmash.bio](https://chill-filter.sourmash.bio/). It's
free, with no login required, and there are a number of examples.
[Here's one to start with - a human WGS data set with some likely plant and microbial contamination](https://chill-filter.sourmash.bio/97681062/Bu5.abund.k51.s100_000.sig.zip/search).

chill-filter is built on top of our
[sourmash](https://sourmash.readthedocs.io/en/latest/) software (so,
Rust and Python underneath). chill-filter extends and refines sourmash
functionality in a few ways.

First, and most important, it has a user interface - it's a Web
app. "Just write a damn user interface for once, Titus." OK, fine.

Second, it's rapid and lightweight - nearly realtime. The searches
take about 5 seconds for each sample, and they search a database
containing 8 human and animal genomes, all 1700 plant genomes, and
600,000 microbial genomes (GTDB RS220).

Third, we sketch the sample on the browser side, which reduces the
upload bandwidth required by, like, an awful lot. So you're not
uploading your 20 GB data set, but rather a ~2 MB compressed version
of it.

Fourth, there's a near complete absence of configurability, which I
think is good, in this case. Just pick your DNA to upload, and boom,
you're done. We've chosen parameters that optimize for specificity by
minimizing false positives (and sensitivity is really not a problem
for sourmash, within the limits of query size). We'll miss stuff
that's not in our reference database, of course, but otherwise... it
should work well?

Fifth, it's meant to be _comprehensive_. In the not so distant future
it should detect essentially any known genome (barring viruses and
other really small fry), and it will scale to all available reference
genomes without much trouble. This means that you don't/won't need to
pick a database. We'll just include everything.

And last but by no means least: the approach is both theoretically
well understood and practically well implemented. Admittedly it has
taken us 8 years to get to the point where we can implement this
functionality in under a month and in a few hundred lines of code, but
that's scientific software engineering, amirite?

## Use cases.

The basic use case here is figuring out what part of your sample
matches _something_, _anything_ in a known genome.

On the genome sequencing side, this could help detect and remove
contamination.

On the metagenome side, it could help with high level sample profiling
and detection of host contamination. And, realistically, this is
something that could just be applied to any and every sample as a kind
of simple report - it's fast enough to apply comprehensively.

The whole thing would fit on a reasonably powerful phone (with no
network traffic needed), which is pretty cool! (< 1GB of disk, < 2 GB
of RAM, and single CPU.)

But... what other use cases are there? We'd love to explore!

Note that it is open source (AGPL), locally installable, and supports
custom databases.

## What's next?

The site is pretty easy to maintain, he says with uncertainty in his
voice. The code is simple, and I wrote a reasonable number of
tests. (It's written in
[flask](https://flask.palletsprojects.com/en/stable/), which was
rather pleasant )

It's pretty cheap, too, which is good because it's unfunded. I'm
paying about $20/month for it at the moment; it's hosted at
[Digital Ocean](https://cloud.digitalocean.com/). I have a hard time
imagining it becoming popular enough that I would need to scale it
up...?

I have all sorts of vague development goals, but I won't have too much
time over the next few months to do ambitious things.

The main things I plan to prioritize are:

* add more refernce genomes to the database. There's already been a
  request to add fungi and viruses. I think once we add fungi to the
  current database, and maybe a few more animal genomes, we'll be done
  for the short term - and it will be a reasonably comprehensive
  sample screening Web site.

* add some enhanced sample analysis. For example, we can estimate how
  much of your sample should assemble (i.e. is high abundance).

* refine and validate eukaryotic genome predictions. We already know
  that sourmash works quite well on bacteria and archaea, and we have
  some pretty strong indications that it works well on vertebrate
  genomes, but we should do some more careful work there.

* build out the command-line side of things. For once, we started with
  a user interface! But there are reasons to support a CLI.

## Let us know!

Questions? Thoughts? Spam?
[Drop us an e-mail]([chill@sourmash.bio](mailto:chill@sourmash.bio)),
or [create an issue](https://github.com/dib-lab/chill-filter/issues),
or [bump me on bluesky](https://bsky.app/), or send a check to me c/o
UC Davis!

And Happy Holidays!

--titus
