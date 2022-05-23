Title: Announcing ribbity - a hacky project to build Web sites from GitHub issue trackers
Date: 2022-05-23
Category: programming
Tags: github
Slug: 2022-announcing-ribbity-github-issue-munging
Authors: C. Titus Brown
Summary: Munging GitHub issue trackers for fun!

For the last few weeks, I've been hacking on a new passion microproject on the side, code-named `ribbity`.

ribbity is the software that builds the [sourmash-examples Web site](https://sourmash-bio.github.io/sourmash-examples/), by producing a [mkdocs](https://www.mkdocs.org) site from the [sourmash-examples issue tracker](https://github.com/sourmash-bio/sourmash-examples/issues/).

In brief, ribbity takes issues descriptions from GitHub and puts them in Markdown files so you can run mkdocs :).

You can see the install and config documentation for ribbity [here](https://ribbity-org.github.io/ribbity-docs/).

## Why oh why would you do this?

You might well ask... why not "just build a Markdown site", maybe with pull requests? A few reasons -

### The GitHub issue tracker is awesome

First, I really like using GitHub issue trackers to organize resources and notes. For example, the [sourmash issue tracker](https://github.com/dib-lab/sourmash/issues) is my "external brain" for all things related to sourmash and genome comparison. I also have several private repos that I use to organize link collections.

Most specifically, I really love the "backlinks" feature of github (where when you refer to issue A from issue B, issue A receives a pointer back to issue B) - this was in the original [Project Xanadu](https://en.wikipedia.org/wiki/Project_Xanadu) plan for interlinked hypertext documents, but it never really made it into the Web. It's awfully handy.

Here, the ability to see backlinks from private repos into public repos is particularly lovely!

### Flexible organization and commenting

I also really like the labeling (categorization) and commenting functionality of github.

Moreover, github has very nice Markdown support, along with a usable editor. And, while writing Markdown in a Web browser is not my most favorite of activities, it sure is nice to be able to do it in a pinch. But more importantly I can write Markdown in a [hackmd page](hackmd.io/) and then copy/paste it into a github issue - this is an [increasingly common workflow](https://github.com/sourmash-bio/sourmash/issues/1968) for me!

### Flexible authentication and notifications

I really like (and use heavily) github's auth and notification systems. You can enable and disable access to repositories, watch specific issues and silence others, lock issues, block people from posting, etc. etc.

I need auth and notifications, but I'm not interested in doing any of
that myself.  Building on top of all of that is a nice simplification.

### GitHub as a platform

More generally, I really like how GitHub is becoming a platform for stuff; you can see an earlier project of mine here, [Using GitHub for janky project reporting - some code](http://ivory.idyll.org/blog/2019-github-project-reporting.html).

Other inspirational projects in this space include [utteranc.es](https://utteranc.es/), which builds a blog commenting platform on top of github; and [Coraline's "low-friction project management"](https://angeliqueweger.com/blog/2021/love-letter-to-lftm/) site. And, while I don't specifically use [datasette](https://datasette.io/) (yet) in any way, it has been a major conceptual contributor to the idea that hosting things statically is a great idea :).

(If you know of other github-based hacks like this, please drop them in the comments or [ping me on Twitter!](https://twitter.com/ctitusbrown/))

### mkdocs static site hosting is simple, esp via github pages

mkdocs produces static sites, and static sites are awesome! (inspiration from [datasette](https://datasette.io/) here, again.) No complicated databases, or authentication, or nasty JavaScripts creepings across my pages. (Side note: I don't know JavaScript.)

Also, github pages sure is easy (and mkdocs natively supports deploying to github pages natively).

And of course you can host mkdocs sites in many places. So it's pretty flexible and enabling to build on top of mkdocs.

## But does it, like, enable anything cool?

One of the prime proximal motivations for building ribbity was the [increasing complexity of the sourmash documentation](https://github.com/sourmash-bio/sourmash/issues/2054), which is in danger of becoming sprawling and labyrinthine.

I really like the idea of a set of documentation that is explicitly intended to be explored and searched in a non-linear way.

That's how I use github issues in practice.

So it seemed natural to try out something new that strips away some of the complexity of the github interface and makes it customizable.

And I'm pretty happy with the resulting [sourmash examples](https://sourmash-bio.github.io/sourmash-examples/) Web site!

In particular, it has really lowered the barrier to contribution for me, personally. I don't have to worry about pull requests or integrating new examples into a big, complicated doc site in a good way - I just throw a new example together, slap a few labels on it, and get on with my day.

In some regards, this is a version of [the pull request hack](https://felixge.de/2013/03/11/the-pull-request-hack/), a contribution model that has always intrigued me. Except instead of giving contributors PR access, they just need to be able to add issues - which, by default, anyone can do on any visible GitHub project!

## How is ribbity implemented??

It's pretty simple underneath -

1. "pull" GitHub issues into a Python pickle dump.
2. process the pickle dump into Python objects, salted with a few regexps.
3. run object model through jinja2 templating to build a `docs/` directory.
4. feed `docs/` directory into mkdocs, which builds a `site/` directory.

I've layered on some tests and some Python package stuff and some CLI, but the core code is pleasingly simple - under 400 lines of code, including spaces and comments.

## Whither ribbity?

A few people have looked at ribbity and gone ...whoa. I want that! So that's nice and validating!

In particular, there's been some enthusiasm amongst colleagues about having a different interface to github issue trackers. One specific motivation is that the responsive search offered by the default mkdocs interface is nice! And I could see an argument for aggregating together multiple issue trackers in a single site, which is a use case some colleagues are interested in.

Basically I see a lot of enthusiasm around specific, customizable hackage of github things.

But... I dunno. There's quite some space between a minimal "this is useful! and limited enough that we can keep it working!" approach, and a janky, badly reimplemented version of everything the github Web site already offers. I'm leaning more towards the former, because I think that's achievable and offers specific utility. But I also have a lot of ideas for how to do ribbity-like things in other directions (Watch This Space!)

If I had to guess, I think my personal interest in ribbity will evolve in the following ways:

* I'll work to push more of ribbity's text munging functionality into jinja2, and make the github download a more complete (and more standardized!) version of the issue repo.
* this will in turn push the core ribbity into being a simple merge of (a) jinja2 templates overlaid on (b) a github object model.
* if I can get the primitives right, this would then make it easy to build custom overlays on github issue trackers entirely in jinja2.

And that actually seems pretty maintainable to me.

Then the current ribbity functionality would just be a specific set of templates we use to build a particular kind of Web site. And new functionality or different issue tracker overlays could be built entirely in jinja2.

But, who knows? I'm definitely not committing to anything; just playing around for now.

That having been said, I'm thinking about applying ribbity to building a directory of training resources, and throwing it at the newsletter problem, and a colleague is using it for their own examples site. So we'll see!

## What other fun experiences did you want to relate?

This was my first experience with [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)! Super cool! Code [here](https://github.com/ribbity-org/ribbity/blob/main/ribbity/objects.py).

(A colleague in the lab, Tessa Pierce, started using them [over in sourmash](https://sourmash.readthedocs.io/), and that finally motivated me to move on from namedtuples or straight up bare Python objects.)

This was also my first parsing experience with [TOML](https://toml.io/en/), which is pretty nice! And I found the [tomli](https://github.com/hukkin/tomli) parser to be easy to use, and thought the [tomllib PEP](https://peps.python.org/pep-0680/) was really great.

## Concluding thoughts

[ribbity](https://github.com/ribbity-org/ribbity) is open source - BSD 3-clause!

[Please file issues](https://github.com/ribbity-org/ribbity/issues) if you have ideas for how you might want to use ribbity!

Pull requests are welcome, but this is a side project, so unless they're fairly minimal or accompanied by good, clear, obvious tests, I might defer them as "too much brain needed". I encourage forking and experimentation!

Your thoughts welcome!

--titus
