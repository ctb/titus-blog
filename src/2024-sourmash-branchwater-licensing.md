Title: Sourmash and branchwater licensing: thoughts on extractive engagement with projects
Date: 2024-01-07
Category: science
Tags: sourmash, oss, licenses
Slug: 2024-sourmash-branchwater-licensing
Authors: C. Titus Brown
Summary: What licenses should be used, for what purpose?

I am helping maintain some petabase-scale genomic search
infrastructure as part of the
[sourmash](https://sourmash.readthedocs.io/) and
[branchwater](https://branchwater.sourmash.bio/) projects. One of the
questions that's frequently in the back of my mind is how to
incentivize
[commons-style engagement rather than extractive engagement](http://ivory.idyll.org/blog/2018-how-open-is-too-open.html),
and a key tool for this purpose is licensing.

Sourmash is BSD-licensed, which, in essence, means that anyone can do
whatever they want with the code - including incorporating it
unchanged into a commercial closed-source product, rebranding it as a
new product, and/or changing it in incompatible ways (and then
rebranding it as a new and better product). This is typically
something that companies will do, although it also happens with open
source forks. (See: [Elasticsearch to OpenSearch](https://www.infoq.com/news/2021/04/amazon-opensearch/); and [Matrix](https://matrix.org/blog/2023/11/06/future-of-synapse-dendrite/)).

Branchwater, our internal code-name for the collection of
sourmash-based functionality that enables petabase-scale search, is
[licensed under AGPL](https://github.com/sourmash-bio/sourmash_plugin_branchwater/issues/60). This
means that anyone can use it however they want, as long as they
release any modifications they make to the source code. In particular,
this also applies to people providing a service based on the
branchwater code:

>Let’s say you create a software program. Another developer takes and
>modifies it, and then provides access to that modification to paying
>customers through a software-as-a-service model. Under the GPL v3,
>that modification would essentially become proprietary because it
>wasn’t technically distributed. Under AGPL, however, that developer
>would need to make their modified source code available for
>download. [(link)](https://github.com/sourmash-bio/sourmash_plugin_branchwater/issues/60)

IIRC, there are a couple of reasons that Dr. Luiz Irber (the initial
author of the branchwater code, and the originator of most of the
branchwater code and supporting infrastructure) chose AGPL. One of the
main ones (again, IIRC) is to discourage incompatible forks of the
source code. But it also discourages many kinds of extractive
behavior: a company could not, for example, take this code, modify it
in sekret ways, and provide services based upon that sekrecy, without
providing the modified code openly under the AGPL license.

You could argue that the AGPL license decreases certain kinds of
uptake. Perhaps so, and I chose the BSD license for sourmash (with
Luiz's OK, albeit in a situation where I was his supervisor...)
specifically to encourage uptake, reuse, modification, and
experimentation. I don't know how to evaluate the success of this
choice, really, other than to say that I still don't see a blindingly
obvious downside to it (as of Jan 5, 2024 :).

At the end of the day, my thoughts trend towards seeing the value in
sourmash as less algorithmic innovation and more infrastructure
innovation. We are maintaining and sustaining a very functional and
useful piece of software, with good documentation and an
ever-expanding range of use cases. And it remains very useful to me
and my lab, specifically. Not only do I not care if companies extract
value from it - there are many ways to skin this particular cat - but
I am happy and excited that my labor as an academic is actually useful
to someone else.

On the flip side, branchwater is both more niche and more
difficult. There aren't many ways to do petabase-scale search, and
there is a lot more infrastructure maintenance involved. I would be
sad to see someone take our (collective) investment in this
functionality and build upon it without returning something to the
community of developers.

I'm not sure what and where the dividing line between these two
situations is for me. But I think sketching out the current line is a
good start :).

--titus
