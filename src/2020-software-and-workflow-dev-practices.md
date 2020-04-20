Title: Software and workflow development practices (April 2020 update)
Date: 2020-04-18
Category: science
Tags: repeatability,reproducibility,replication, snakemake, github, conda, bioconda
Slug: 2020-software-and-workflow-dev-practices
Authors: C. Titus Brown
Summary: How we develop software and workflows in the DIB Lab


@@update charcoal README a bit to finish output docs

Over the last 10-15 years, I've blogged periodically about how my lab develops research software and build scientific workflows. The [last update](http://ivory.idyll.org/blog/2018-repeatability-in-practice.html) talked a bit about how we've transitioned to snakemake and conda for automation, but I was spurred by an e-mail conversation into another update - because, y'all, it's going pretty well and I'm pretty happy!

Below, I talk through our current practice of building workflows and software.
These procedures work pretty well for our (fairly small) lab of people who mostly work part-time on workflow and software development. **By far** the majority of our effort is usually spent trying to understand the **results** of our workflows; except in rare cases, I try to guide people to spend at most 20% of their time writing new analysis code - preferably less.

Nothing about these processes ensures that the scientific output is correct or useful, of course. While scientific correctness of computational workflows necessarily depends (often critically) on the correctness of the code underlying those workflows, the code could ultimately be doing the wrong thing scientifically. That having been said, I've found that the processes below let us focus much more cleanly on the scientific value of the code because we don't worry as much about whether the code is correct, and moreover our processes support rapid iteration of software and workflows as we iteratively develop our use cases.

As one side note, I should say that the complexity of the scientific process is one thing that distinguishes research computing from other software engineering projects. **Often we don't actually have a good idea of what we're trying to achieve**, at least not any level of specificity. This is a recipe for disaster in a software engineering project, but it's our day to day life in science! What ...fun? (I mean, it kind of is. But it's also hellishly complicated.)

## Workflows and scripts

Pretty much every scientific computing project I've worked on in the last (counts on fingers and toes... runs out of toes... 27 years!? eek) has grown into a gigantic mess of scripts and data files. Over the (many) years I've progressively worked on taming these messes using a variety of techniques.

Phillip Brooks, Charles Reid, Tessa Pierce, and Taylor Reiter have been the source of a lot of the workflow approaches I discussed below, although everyone in the lab has been involved in the discussions!

### Store code and configuration in version control

Since I "grew up" simultaneously in science and open source, I started using version control early on - first RCS, then CVS, then darcs, then Subversion, and finally git. Version control is second nature, and it applies to science too!

The first basic rule of scientific projects is, **put it in git.**

This means that I can (almost) always figure out what I was doing a month ago when I got that neat result that I haven't been able to replicate again. More importantly I can see _exactly_ what I changed in the last hour, and either fix it or revert to what last worked.

Over almost 30 years of sciencing, project naming becomes a problem! Especially since I tend to start projects small and grow them (or let them die on the vine if my focus shifts). So my repo names usually start with the year, followed by a few keywords -- e.g. [2020-long-read-assembly-decontam](https://github.com/ctb/2020-long-read-assembly-decontam). While I can't predict which code I'll go back to, I always end up going back to some of it!

### Write scripts using a language that encourages modularity and code sharing

I've developed scientific workflows in C, bash, Perl, Tcl, Java, and Python. By far my favorite language of these is Python. The main reason I switched wholeheartedly to Python is that, more than any of the others, Python had a nice blend of modularity and reusability. I could pick up a blob of useful code from one script and put it in a shared module for other scripts to use. And it even had its own simple namespace scheme, which encouraged modularity by default!

At the time (late '90s, early '00s) this kind of namespacing was something that wasn't as well supported by other interpreted languages like Perl (v4?) and Tcl. While I was already a knowledgeable programmer, the ease of code reuse combined with such simple modularity encouraged systematic code reuse in my scripts in a new way. When combined with the straightforward C extension module API, Python was a huge win.

Nowadays there are many good options, of course, but Python is still one of them, so I haven't had to change! My lab now uses an increasing amount of R, of course, because if its dominance in stats and viz. And we're starting to use Rust instead of C/C++ for extension modules.

### Automate scientific workflows

Every project ends up with a mess of scripts.

When you have a pile of scripts, it's usually not clear how to run them in order. When you're actively developing the scripts, it becomes confusing to remember whether your output files have been updated by the latest code. Enter workflows!

I've been using `make` to run workflows for ages, but about 2 years ago the entire lab switched over to snakemake. This is in part because it's well integrated with Python, and in part because it supports conda environments. It's been lovely! And we now have a body of shared snakemake expertise in the lab that is hard to beat.

snakemake also works really well for combining my own scripts with other programs, which is of course something that we do a _lot_ in bioinformatics.

There are a few problems with snakemake, of course. It doesn't readily scale to 100s of thousands of jobs, and we're still working out the best way to orchestrate complex workflows on a cluster. But it's proven [relatively straightforward to teach](https://github.com/ngs-docs/2020-GGG201b-lab), and it's nicely designed, with an awful lot of useful features. I've heard good things about nextflow, and if I were going to operate at larger scales, I'd be looking at CWL or WDL.

### New: Work in isolated execution environments

One problem that we increasingly encounter is the need to run different incompatible versions of software within the same workflow. Usually this manifests in underlying dependencies -- **this** package needs Python 2 while **this other** package requires Python 3.

Previously, tackling this required ugly heavyweight hacks such as VMs or docker containers. I personally spent a few years negotiating with Python virtualenvs, but they only solved some of the problems, and only then in Python-land.

Now, we are 100% conda, all the time. In snakemake, we can provide [environment config files](https://github.com/ctb/2020-long-read-assembly-decontam/blob/master/environment.yml) for running the basic pipeline, with rule/step-specific [environment files](https://github.com/ctb/2020-long-read-assembly-decontam/blob/master/conf/env-sourmash.yml) that rely on pinned (specific) versions of software.

Briefly, with `--use-conda` on the command line and `conda:` directives [in the Snakefile](https://github.com/ctb/2020-long-read-assembly-decontam/blob/master/Snakefile#L26), snakemake manages creating and updating these environments for you, and activate/deactivates them on a per-rule basis. It's beautiful and Just Works.

### New: Provide quickstart demonstration data sets.

(This is a brand new approach to my daily practice, supported by the easy configurability of snakemake!)

The problem is this: often I want to develop and rapidly execute workflows on small test data sets, while also periodically running them on bigger "real" data sets to see what the results look like. It turns out this is hard to stage-manage! Enter ...snakemake config files! These are YAML or JSON files that are automatically loaded into your Snakefile name space.

**Digression:** A year or three ago, [I got excited](http://ivory.idyll.org/blog/2018-workflows-applications.html) about using workflows as applications. This was a trend that Camille Scott, a PhD student in the lab, had started with [dammit](https://dib-lab.github.io/dammit/), and we've been using it for [spacegraphcats](https://github.com/spacegraphcats/spacegraphcats/) and [elvers](https://github.com/dib-lab/elvers).

The basic idea is this: Increasingly, bioinformatics "applications" are workflows that involve running other software packages. Writing your own scripts that stage-manage other software execution is problematic, since you have to reinvent a lot of error handling that workflow engines already have. This is also true of issues like parallelization and versioning.

So why not write your applications as wrappers around a workflow engine? It turns out with both pydoit and snakemake, you can do this pretty easily! So that's an avenue we've been exploring a few projects.

**Back to the problem to be solved:** What I want for workflows is the following:

1. A workflow that is approximately the same, independent of the input data.
2. Different sets of input data, ready to go.
3. In particular, a demo data set (a real data set cut down in size, or synthetic data) that exercises most or all of the features of the workflow.
4. The ability to switch between input data sets quickly and easily **without** changing any source code.
5. In a perfect world, I would have the ability to develop and run the same workflow code on both my laptop and in an HPC queuing system.

This set of functionality is something that snakemake easily supports with its `--configfile` option - you specify a *default* config file [in your Snakefile](https://github.com/ctb/2020-long-read-assembly-decontam/blob/master/Snakefile#L6), and then override that with other config files when you want to run for realz. Moreover, with the rule-specific conda environment files (see previous section!), I don't even need to worry about installing the software; snakemake manages it all for me!

With this approach, my workflow development process becomes very fluid. I prototype scripts on my laptop, where I have a full dev environment, and I develop synthetic data sets to exercise various features of the scripts. I bake this demo data set into [my default snakemake config](https://github.com/ctb/2020-long-read-assembly-decontam/blob/master/test-data/conf.yml) so that it's what's run by default. For real analyses, I then override this by specifying [a different config file](https://github.com/ctb/2020-long-read-assembly-decontam/blob/master/conf/conf-necator.yml) on the command line with `--configfile`.  And this all interacts perfectly well with snakemake's cluster execution approach.

As a bonus, the demo data set provides a simple quickstart and example config file for people who want to use your software. This makes [the installation and quickstart docs](https://github.com/ctb/2020-long-read-assembly-decontam/blob/master/README.md#installing) really simple and nearly identical across multiple projects!

(Note that I develop on Mac OS X and execute at scale on Linux HPCs. I'd probably be less happy with this approach if I developed on Windows, for which bioconda doesn't provide packages.)

## Libraries and applications

On the opposite end of the spectrum from "piles of scripts" is research software engineering, where we are trying explicitly to build maintainable and reusable libraries and command-line applications. Here we take a very different approach to the workflow approach detailed above, although in recent years I've noticed that we're working across this full spectrum on several projects.  (This is perhaps because workflows, done like we are doing them above, start to resemble serious software engineering :).

Whenever we find a core set of functionality that is being used across multiple projects in the lab, we start to abstract that functionality into a library and/or command line application.  We do this in part because [most scripts have bugs](http://ivory.idyll.org/blog/automated-testing-and-research-software.html) that should be fixed, and we remain ignorant of them until we start reusing the scripts; but it also aids in efficiency and code reuse. It's a nice use-case driven way to develop software!

We've developed several software packages this way. For example, the [khmer](https://github.com/dib-lab/khmer/) and [screed](https://github.com/dib-lab/screed/) libraries emerged from piles of code that slowly got unified into a shared library.

More recently, the [sourmash](https://github.com/dib-lab/sourmash/) project has become the in-lab exemplar of intentional software development practices. We now have 3-5 people working regularly on sourmash, and it's being used by an increasingly wide range of people. Below are some of the key techniques we've been using, which will (in most cases) be readily recognized as matching basic open source development practices!

I want to give an especially big shoutout here to Michael Crusoe, Camille Scott, and Luiz Irber, who have been the three key people leading our adoption of these techniques.

### Automate tests

Keeping software working is hard. Automated tests are one of the solutions.

We have an increasingly expansive [set of automated tests](https://github.com/dib-lab/sourmash/tree/master/tests) for sourmash - over 600 at the moment. It takes about a minute to run the whole test suite on my laptop. If it looks intimidating, that's because we've grown it over the years. We started with one test, and went from there.

We don't really use test-driven development extensively, or at least I don't. I know Camille has used it [in her De Bruijn graph work](http://www.camillescott.org/2017/11/15/pytest-magic/). I tend to reserve it for situations where the code is becoming complicated enough at a class or function level that I can't understand it -- and that's rarely necessary in my work. (Usually it means that I need to take a step back and rethink what I'm doing! I'm a big believer in [Kernighan's Lever](https://www.linusakesson.net/programming/kernighans-lever/index.php) - if you're writing code at the limit of your ability to understand it, you'll never be able to debug it!)

### Use code review

Maintainability, sustainability, and correctness of code are all enhanced by having multiple people's eyes on it.

We basically use [GitHub Flow](https://guides.github.com/introduction/flow/), as I understand it. Every PR runs all the tests on each commit, and we have a checklist to help guide contributors.

We have a two-person sign-off rule on every PR. This can slow down code development when some of us are busy, but on the flip side no one person is solely responsible when bad code makes it into a release :).

Most importantly, it means that our code quality is consistently better than what I would produce working on my own.

### Use semantic versioning

[Semantic versioning](https://semver.org/) means that when we release a new version, outside observers can quickly know if they can upgrade without a problem. For example, within the sourmash 3.x series, the only reason for the same command line options to produce different output is if [there was a bug](https://github.com/dib-lab/sourmash/pull/942).

[We are still figuring out some of the details, of course.](https://github.com/dib-lab/sourmash/issues/655) For example, we have only recently started tracking performance regressions. And it's unclear exactly what parts of our API should be considered public. Since sourmash isn't _that_ widely used, I'm not pushing hard on resolving these kinds of high level issues, but they are a regular background refrain in my mind.

In any case, what semantic versioning does is provide a simple way for people to know if it's safe to upgrade. It also lets us pin down versions in our own workflows, with some assurance that the behavior shouldn't be changing (but performance might improve!) if we pin to a major version.

### Nail down behavior with tests, then refactor underneath

I write a lot of hacky code when I'm exploring research functionality. Often this code gets baked into our packages with a limited understanding of its edge cases.  As I explore and expand the use cases more and more, I find more of these edge cases. And, if the code is in a library, I nail down the edge cases with [stupidity-driven testing](http://ivory.idyll.org/blog/stupidity-driven-testing.html). This then lets me (or others) refactor the code to be less hacky and more robust, without changing its functionality.

For example, I'm currently going through a [long, slow refactor](https://github.com/dib-lab/sourmash/pull/946) of some formerly ugly sourmash code that creates a certain kind of indexed database. This code worked reasonably well for years, but as we developed more uses for it, it became clear that there were, ahem, opportunities for refactoring it to be more usable in other contexts.

We don't start with good code. We don't pretend that our code is good (or at least I wouldn't, and can't :). But we iteratively improve upon our code as we work with it.

### Explore useful behavior, then nail it down with tests, and only **then** optimize the heck out of it

The previous section is how we clean up code, but it turns out it also works really well for **speeding up code**.

There this really frustrating bias amongst software developers towards [premature optimization](https://wiki.c2.com/?PrematureOptimization), which leads to ugly and unmaintainable code. In my experience, flexibility trumps optimization 80% or more of the time, so I take this to the other extreme and rarely worry about optimizing code. Luckily some people in my lab counterbalance me in this preference, so we occasionally produce performant code as well :).

What we do is get to the point where we have pretty well-specified functionality, and then benchmark, and then refactor and optimized based on the benchmarking.

A really clear example of this applied to sourmash was [here](https://github.com/dib-lab/sourmash/issues/573), when Luiz and Taylor noticed that I'd written really bad code that was recreating large sets again and again in Python. Luiz added a simple "remove_many" method that did the same operation in place and we got a really substantial (order of magnitude?) speed increase.

Critically, this optimization was to a new research algorithm that we developed over the period of years. **First** we got the research algorithm to work. **Then** we spent a lot of time understanding how and why and where it was useful. **During this period** we wrote a whole bunch of tests that nailed down the behavior. And then when Luiz optimized the code, we just dropped in a faster replacement that passed all the tests.

This has become a bit of a trend in recent years. As sourmash has moved from C to C++ to Rust, Luiz has systematically improved the runtimes for various operations. But this has always occurred in the context of well-understood features with lots of tests. Otherwise we just end up breaking our software when we optimize it.

As a side note, whenever I hear someone emphasize the speed of their just-released scientific software, my strong Bayesian prior is that they are really telling me their code is not only full of bugs (all software is!) but that it'll be really hard to find and fix them...

### Collaborate by insisting the tests pass

Working on multiple independent feature sets at the same time is hard, whether it's only one person or five.  Tests can help here, too!

One of the cooler things to happen in sourmash land in the last two years is that [Olga Botvinnik](https://twitter.com/olgabot) and some of her colleagues at CZBioHub started contributing substantially to sourmash. This started with Olga's interest in using sourmash for single-cell RNAseq analysis, which presents new and challenging scalability challenges.

Recently, the CZBioHub folk [submitted a pull request to significantly change one of our core data structures](https://github.com/dib-lab/sourmash/pull/925) so as to scale it better. (It's going to be merged soon!) Almost all of our review comments have focused on reviewing the code for understandability, rather than questioning the correctness - this is because the interface for this data structure is pretty well tested at a functional level. **Since the tests pass, I'm not worried that the code is wrong.**

What this overall approach lets us do is simultaneously work on multiple parts of the sourmash code base with some basic assurances that it will still work after all the merges are done.

### Distribute via (bio)conda, install via environments

Installation for end users is hard.
I've spent many, many years writing installation tutorials. Conda just solves this, and is our go-to approach now for supporting user installs.

Conda software installation is awesome and awesomely simple. Even when software isn't yet packaged for conda install (like [spacegraphcats](https://github.com/spacegraphcats/spacegraphcats/), which is research-y enough that I haven't bothered) you [can still install it that way -- see the pip commands, here](https://github.com/spacegraphcats/spacegraphcats/blob/master/environment.yml).

### Put everything in issues

You can find most design decisions, feature requests, and long-term musings for sourmash in our [issue tracker](https://github.com/dib-lab/sourmash/issues). This is where we discuss almost everything, and it's our primary help forum as well. Having a one-stop shop that ties together design, bugs, code reviews, and documentation updates is really nice. We even try to [archive slack conversations](https://twitter.com/ctitusbrown/status/1247524069596991488) there!

## Concluding thoughts

Academic workflow and software development is a tricky business. We operate in slow moving and severely resource-constrained environments, with a constant influx of people who have a variety of experience, to solve problems that are often poorly understood in the beginning (and maybe at the end). The practices above have been developed for a small lab and are battle-tested over a decade and more.

While your mileage may vary in terms of tools and approaches, I've seen convergence across the social-media enabled biological data science community to similar practices. This suggests these practices solve real problems that are being experienced by multiple labs. Moreover, we're developing a solid community of practice in not only using these approaches but also teaching them to new trainees. Huzzah!

--titus

(Special thanks go to the USDA, the NIH, and the Moore Foundation for funding so much of our software development!)
