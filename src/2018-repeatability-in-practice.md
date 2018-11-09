Title: Repeatability in Practice (2018 version)
Date: 2018-11-09
Category: science
Tags: repeatability,reproducibility,replication, snakemake, github
Authors: C. Titus Brown
Summary: How we do repeatability in the DIB Lab
Slug: 2018-repeatability-in-practice

* **Note:** These are the notes for a talk I gave in the
  [Crutchfield Lab](http://csc.ucdavis.edu/~chaos/) at UC Davis, by
  kind invitation from Ryan G. James. You can view the original hackmd
  in [view mode](https://hackmd.io/ezULDXU2TkuyZP_sRlDFMw?view) or [slide mode](https://hackmd.io/p/BkreVNKYm#/) if
  you are interested!*

## The basic idea

### Goals of repeatability

In order of importance,

1. Make it as easy as possible for us to rerun everything from any point in the workflow.
2. Make it as easy as possible to try new things.

---

4. Make it easy to add / adjust analyses in response to reviewers.
5. Make it 100% repeatable.

---

### Some diagrams

Tools:

![](https://i.imgur.com/Orzwpt3.png)

---

Fitting the tools together:

![](https://i.imgur.com/MloEjg5.png)

---

### What many of us have converged on in the DIB Lab

git/GitHub + snakemake + (Jupyter Notebook or R) + conda

With this collection of tools, we can generally achieve full repeatability.

---

Some points :

* we use a diverse array of computing environments: Mac vs Linux, HPC vs cloud (AWS/GCP/Jetstream) vs docker vs binder (dynamically configured docker containers). This approach works across all of them more or less seamlessly.
* Software installation was THE last remaining major pain point for us until bioconda came along. This solves almost all of the problems.

---

* And, before that, my workflow tool was Makefiles which no one but me liked - until snakemake, which we've more or less converged on.
* This stack of software is something that (with minor modifications and sometimes major extensions) most data scientists I talk to have converged on.

---

* The Carpentries teaches most of this (not snakemake or conda, but conda is an easy extension)
* We ran a whole ~100 person workshop using (bio)conda with only a few failures!

---

## The Journey

---

### Overall strategy

For each paper we write, we try to provide a repeatable pipeline on GitHub. Then, for publication, we link the GitHub repo to [Zenodo](http://zenodo.org) and cut a new version, which gives us a DOI to cite for exactly the version of the code used. 

This is the strategy we used for the MMETSP paper,
["Re-assembly, quality evaluation, and annotation of 678 microbial eukaryotic reference transcriptomes"](https://www.biorxiv.org/content/early/2018/05/17/323576), which is now accepted at GigaScience (yay!!)

---

Large raw data files are hosted on specific archival services (e.g. the Sequence Read Archive). Zenodo or figshare or the [Open Science Framework](http://osf.io) serve as nice places to dump intermediate files.

---

For figure generation, we tend to use Jupyter Notebooks and/or R scripts that are in the github repo. Where possible we put the summary files used to build the figures in the github repo; if they're bigger than 100MB, we put them on OSF; if they're bigger than 5 GB, we start looking at zenodo.

---

 Note: to the best of our knowledge, no one has ever bothered to reproduce our papers from scratch. But we feel good about it anyway :).

---

### The Bad Old Days

For [Brown and Callan, 2004](http://www.pnas.org/content/101/8/2404), I used a pile of scripts - shell scripts to execute Python scripts to do the heavy lifting. It worked well for the time, but was virtually impossible for anyone else to reproduce unless they were able to compile a specific Python package with C extensions (which at the time was extra hard).

---

#### Cool beans

Of note, this approach let me determine that a bug in the code didn't significantly affect the published results (I found the bug much later, when I was reusing the pipeline elsewhere).

---

### The Days of Make

For many years, I switched to using make.
You can see a old-style repo here, [2016-metagenome-assembly-eval](https://github.com/dib-lab/2016-metagenome-assembly-eval) ([see preprint](https://www.biorxiv.org/content/early/2017/07/03/155358)). The repo contains the LaTeX paper source, some notebooks for graphing, and a `pipeline` directory with [a big-arse Makefile](https://github.com/dib-lab/2016-metagenome-assembly-eval/blob/master/pipeline/Makefile) in it.

---

I'm actually updating this repo to resubmit in response to reviewers, and we're [now using conda](https://github.com/dib-lab/2016-metagenome-assembly-eval/blob/pipeline/pipeline/Makefile) to manage software installs.

---

### The brief middle: Docker! Docker! Docker!

When docker came out, I tried it out for a bunch of blog posts - see [week of khmer](http://ivory.idyll.org/blog/2015-wok-notes.html). This ended up being used in a preprint, [Crossing the streams](https://peerj.com/preprints/890/) - see Docker instructions [here](https://github.com/dib-lab/2014-streaming/blob/master/DOCKER.rst).

---

I wasn't happy with this because it turns out that it's virtually impossible to get docker installed on clusters. But it sure did make it easy to run the software across a variety of platforms.

---

### The last year or so

Now we've converged on an approach that uses conda and snakemake; see [2018 spacegraphcats paper](https://github.com/dib-lab/2018-paper-spacegraphcats/blob/master/pipeline-base/Snakefile)

---

## Other things to mention

---

### The importance of libraries

We tend to encapsulate our reusable functionality in Python libraries that are well tested, versioned, etc. While this has some flaws, it means that the bits of our code that get reused in multiple (often shared) projects in the lab get progressively better tested. It also makes them available to others.  The skillset required is pretty advanced though.  (Examples: [khmer](https://github.com/dib-lab/khmer/), [screed](https://github.com/dib-lab/screed/), [sourmash](https://github.com/dib-lab/sourmash)).

---

On the flip side, we do not generally apply any kind of formal testing to our per-project scripts. At best, we try to identify small data sets that we can use to run the whole paper-specific pipeline from start to finish.

---

### Binder

With relatively little effort, you can make your figure-generating Jupyter Notebooks / RMarkdown executable by anyone with a single click through mybinder.org - see [my example RStudio repo](https://github.com/ngs-docs/2018-ggg-rstudio-bioinformatics-ws/), and try clicking "launch binder".

---

### Lessons from Oslo, 2016

See [this repo](https://2016-oslo-repeatability.readthedocs.io/en/latest/) for some hands-on lessons in Jupyter Notebook, make, and git.

---

### Workflows-as-applications

In [this blog post](http://ivory.idyll.org/blog/2018-workflows-applications.html), I talk about how we're using pydoit and snakemake to **write command line applications**. This is a pretty nifty way to tie a pile of code together into soemthing that looks like a pipeline but can take advantage of things like dependency graphs, cluster execution and Kubernetes.

---

Here are some links:

* [dammit](https://dammit.readthedocs.io/), a transcriptome annotator based around pydoit.
* [dahak metagenomics pipeline](https://github.com/dahak-metagenomics/dahak), based around snakemake.
* [spacegraphcats](https://github.com/spacegraphcats/spacegraphcats/), a fairly simple command line snakemake wrapper around Snakemake.
* [eel pond](https://dib-lab.github.io/eelpond/), an emerging SIMPLE approach to dynamically building up Snakemake dependencies in response to user configuration.

---

The downsides to this approach are that we now writing papers that have workflows in them that call out to workflows that use wrapped workflows... workflows all the way down!!!

---

### Why snakemake?

---

Pros:

* Python-based, so we don't have to use some hacky weird configuration language; everything can be munged in Python. (This is also a downside - things can be come arbitrarily complicated.)
* surprisingly simple and clean
* surprisingly powerful
* can grow the files incrementally as your needs grow

---

* ties seamlessly into workflow engines (clusters, kubernetes), conda, docker & singularity. Like, it **actually works**.

---

Cons:

* a confusing mixture of generic rules and specific rules. For example, [this](https://github.com/spacegraphcats/spacegraphcats/blob/master/conf/Snakefile#L66) is a specific rule for a particular output (configured by user for each workflow and then parameterized from that configuration), while [this](https://github.com/spacegraphcats/spacegraphcats/blob/master/conf/Snakefile#L128) is a general rule that snakemake can parameterize for you.
* like anything else, can become a gigantic mess. We haven't yet worked out ways of keeping it clean.
* Fast evolving ecosystem.

---

### Using argparse in Python

It's a small thing, but I strongly recommend using proper argument parsing - a main() function, with argparse.  See [top of this script](https://github.com/spacegraphcats/spacegraphcats/blob/master/scripts/chunk-genomes-to-vectors.py#L17) for an example.

---

It makes setting default parameters and adding arguments really easy, and gives good error messages too.
