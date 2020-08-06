Title: Improved workflows-as-applications: tips and tricks for building applications on top of snakemake
Date: 2020-08-06
Category: science
Tags: workflows,bioinformatics,snakemake
Slug: 2020-improved-workflows-as-applications
Authors: C. Titus Brown
Summary: Writing applications around workflow systems, take 2.

(Thanks to Camille Scott, Phillip Brooks, Charles Reid, Luiz Irber, Tessa Pierce, and Taylor Reiter for all their efforts over the years! Thanks also to Silas Kieser for his work on [ATLAS](https://github.com/metagenome-atlas/atlas), which gave us inspiration and some working code :).)

A while back, [I wrote about workflow as applications](http://ivory.idyll.org/blog/2018-workflows-applications.html), in which I talked about how Camille Scott had written dammit (link below) in the pydoit workflow system, and released it as an application. In doing so, Camille made a fundamental observation: many bioinformatics tools are wrappers that run other bioinformatics tools, and that is literally what workflow tools are designed to do!

Since that post, we've doubled down on workflow systems, improved and adapted our [good enough in-lab practices for software and workflow development](
http://ivory.idyll.org/blog/2020-software-and-workflow-dev-practices.html), and written [a paper on workflow systems](https://dib-lab.github.io/2020-workflows-paper/)  - [(also on bioRxiv)](https://www.biorxiv.org/content/10.1101/2020.06.30.178673v1).

Projects that we write this way end up consisting of large collections of interrelated Python scripts (more on how we manage that later - see [e.g. the spacegraphcats.search package for an example](https://github.com/spacegraphcats/spacegraphcats/tree/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/search)).  This strategy also allows integration of multiple different languages under a single umbrella, including (potentially) R scripts and bash scripts and... whatever else you want :). 

As part of this effort, we've developed much improved practices around better (more functional) user experiences with our software. In this blog post, I'm going to talk about some of these - read on for details!

This post extracts experience from the following in-lab projects: 

* [the dammit transcriptome annotator](https://github.com/dib-lab/dammit),
* [the dahak metagenomics pipeline](https://github.com/dahak-metagenomics/dahak),
* [the spacegraphcats metagenomics graph query software](https://github.com/spacegraphcats/spacegraphcats),
* [the elvers de novo transcriptome pipeline](https://github.com/dib-lab/elvers),
* and [the charcoal genome decontamination pipeline](https://github.com/dib-lab/charcoal).

## Some background: how do we build applications on top of snakemake?

We've done quite a few times now, and there are 3 parts to the pattern:

first, we build a [Snakefile](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/conf/Snakefile) that does the things we want to do, and stuff it into a Python package.

second, we create a Python entry point ([see `__main__` in spacegraphcats](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/__main__.py)) that calls snakemake - in [this case](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/__main__.py#L128) it does it by calling the Python API (but see below for better options).

third, in that entry point we [load config files, salt in our own overrides, and otherwise customize the snakemake session](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/__main__.py).

and voila, now when you call that entry point, you run a custom-configured snakemake that runs whatever workflows are needed to create the specified targets! See for example [the docs on running spacegraphcats](https://github.com/spacegraphcats/spacegraphcats/blob/master/doc/running-spacegraphcats.md#running-spacegraphcats-search--output-files).

## Problems that we've run into, and their solutions.

The strategy above works great in general, but there are a few annoying problems that have popped up over time.

* we want more flexible config than is provided by a single config file.
* we want to distribute jobs from our application across clusters.
* we don't want to have to manually implement all of snakemake's (many) command line options and functionality.
* we want to support better testing!
* we want to run our applications from within Snakemake workflows.

So, over time, we've come up with the following solutions. Read on!

### Stacking config files

One thing we've been doing for a while is providing configuration options via a YAML file (see e.g. [spacegraphcats config files](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/conf/twofoo.yaml)). But once you've got more than a few config files, you end up with a whole host of options in common and only a few config parameters that you change for each run.

With our newer project, charcoal, I decided to try out stacking config files, so that there's an **installation-wide** set of defaults and config parameters, as well as a **project-specific** config.

This makes it possible to have sensible defaults that can be overridden easily on a per-project basis.

The way this works with snakemake is that you  supply one or more JSON or YAML files [like this](https://github.com/dib-lab/charcoal/blob/dfc18387a7f88abb77941a5c0528b924bc43b237/charcoal/conf/system.conf) to snakemake. Snakemake then loads them all in order and supplies the parameters [in the Snakefile namespace via the `config` variable](https://github.com/dib-lab/charcoal/blob/dfc18387a7f88abb77941a5c0528b924bc43b237/charcoal/Snakefile).

The Python code to do this via the wrapper command-line is [pretty straight forward - you make a list of all the config files and supply that to `subprocess`!](https://github.com/dib-lab/charcoal/blob/dfc18387a7f88abb77941a5c0528b924bc43b237/charcoal/__main__.py#L40)

### Supporting snakemake job management on clusters

Snakemake conveniently supports [cluster execution](https://snakemake.readthedocs.io/en/v5.1.4/executable.html#cluster-execution), where you can distribute jobs across HPC clusters.

With both spacegraphcats and elvers, we couldn't get this to work at first.  This is because we were [calling snakemake via its Python API](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/__main__.py#L128), while the cluster execution engine wanted to call snakemake at the command line and couldn't figure out how to do that properly in our application setup.

The [ATLAS](https://github.com/metagenome-atlas/atlas) folk had figured this out, though: ATLAS uses subprocess to run the snakemake executable, and when I was writing charcoal, I [tried doing that instead](https://github.com/dib-lab/charcoal/blob/dfc18387a7f88abb77941a5c0528b924bc43b237/charcoal/__main__.py#L51). It works great, and is surprisingly much easier than using the Python API!

So, now our applications can take full advantage of snakemake's underlying cluster distribution functionality!

## Supporting snakemake's (many) parameters

With spacegraphcats, the first application we built on snakemake, we implemented a kind of janky parameter passing thing where we [just mapped our own parameters over to snakemake parameters explicitly](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/__main__.py#L45).

However, snakemake has *tons* of command line arguments that do useful things, and it's really annoying to reimplement them all. So in charcoal, [we switched from argparse to click for argument parsing](https://github.com/dib-lab/charcoal/blob/dfc18387a7f88abb77941a5c0528b924bc43b237/charcoal/__main__.py#L67), and simply pass all "extra" arguments on to snakemake.

This occasionally leads to weird logic like [the code needed to support`--no-use-conda`](https://github.com/dib-lab/charcoal/blob/dfc18387a7f88abb77941a5c0528b924bc43b237/charcoal/__main__.py#L29), where we by default pass `--use-conda` to snakemake, and then have to override that to turn it off. But by and large it's worked out quite smoothly.

## A drop-in module for a command-line API

As we build more applications this way, we're starting to recognize commonalities in the use cases. Recently I wanted to upgrade the spacegraphcats CLI to take advantage of lessons learned, and so I [copied the charcoal \_\_main\_\_.py](https://github.com/dib-lab/charcoal/blob/dfc18387a7f88abb77941a5c0528b924bc43b237/charcoal/__main__.py) over to [spacegraphcats.click](https://github.com/spacegraphcats/spacegraphcats/blob/d049876a2f4c452fe9ea42a0db70b7c2f3b6112d/spacegraphcats/click.py) and started editing it. Somewhat to my surprise, it was really easy to adapt to spacegraphcats - like, 15 minutes easy!

So, we're pretty close to having a "standard" entry point module that we can copy between projects and quickly customize.

## Testing, testing, testing!

We get a lot of value from writing automated functional and integration tests for our command-line apps; they help pin down functionality and make sure it's still working over time.

However, with spacegraphcats, I really struggled to write good tests. It's hard to test the whole workflow when you have piles of interacting Python scripts in a workflow - e.g. the [workflow tests](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/search/test_workflow.py) are terrible:  clunky to write and hard to modify.

In contrast, once I had the new command-line API working, I had the tools to make really nice and simple workflow tests that relied on snakemake underneath - see [test_snakemake.py](https://github.com/spacegraphcats/spacegraphcats/blob/d049876a2f4c452fe9ea42a0db70b7c2f3b6112d/spacegraphcats/test_snakemake.py). Now our tests look like this:

```
def test_dory_build_cdbg():
    global _tempdir

    dory_conf = utils.relative_file('spacegraphcats/conf/dory-test.yaml')
    target = 'dory/bcalm.dory.k21.unitigs.fa'
    status = run_snakemake(dory_conf, verbose=True, outdir=_tempdir,
                           extra_args=[target])
    assert status == 0
    assert os.path.exists(os.path.join(_tempdir, target))
```

which is about as simple as you can get - specify config file and a target, run snakemake, check that the file exists.

The one tricky bit in [test_snakemake.py](https://github.com/spacegraphcats/spacegraphcats/blob/d049876a2f4c452fe9ea42a0db70b7c2f3b6112d/spacegraphcats/test_snakemake.py) is that the tests should be run in a particular order, because they build on each other. (You can actually run them in any order you want, because snakemake will create the files as needed, but it makes the test steps take longer.)

I ended up using [pytest-dependency](https://github.com/spacegraphcats/spacegraphcats/blob/d049876a2f4c452fe9ea42a0db70b7c2f3b6112d/spacegraphcats/test_snakemake.py) to recapitulate which steps in the workflow depended on each other, and now I have a fairly nice granular breakdown of tests, and they seem to work well.

(I'm still stuck on how to ensure that the outputs of the tests have the correct content, but that's a problem for another day :).

## Using workflows inside of workflows

Last but not least, we tend to want to run our applications _within_ workflows. This is true even when our applications _are_ workflows :).

However, we ran into a little bit of a problem with paths. Because snakemake relies heavily on file system paths, the applications we built on top of snakemake had fairly hardcoded outputs. For example, spacegraphcats produces lots of directories like `genome_name`, `genome_name_k31_r1`, `genome_name_k31_r1_search`, etc. that have to be in the working directory. This turns into an ugly mess for any reasonably complicated workflow.

So, we took advantage of [snakemake's `workdir:` parameter](https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html#configure-working-directory) to provide a command-line feature in our applications that would stuff all of the outputs in a particular directory.

This, however, meant some _input_ locations needed to be adjusted to absolute rather than relative paths. Snakemake handled this automatically for filenames specified in the Snakefile, but for paths loaded from config files, [we had to do it manually](https://github.com/spacegraphcats/spacegraphcats/blob/2e82cc46cd25e71a1158d641760a11fdb940583d/spacegraphcats/conf/Snakefile#L19). This turned out to be quite easy and works robustly!

You can see an example of this usage [here](https://github.com/dib-lab/2020-ibd/blob/50404a7cfcd41ce1ed809ba8aaddb1939e279e8e/Snakefile#L941). The `--outdir` parameter tells spacegraphcats to just put everything under a particular location.

## Concluding thoughts

I've been pleasantly surprised at how easy it has been to build applications on top of snakemake. We've accumulated some good experience with this, and have some fairly robust and re-usable code that solves many of our problems. I hope you find it useful!

--titus
