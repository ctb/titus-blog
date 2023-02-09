Title: conda & mamba on shared clusters works better now!
Date: 2023-02-09
Category: programming
Tags: conda, mamba, conda-forge, rstats, python
Slug: 2023-conda-mamba-shared
Authors: C. Titus Brown
Summary: conda is great!

Friends! Countrymen! I bring you good tidings! The [bug is dead!](https://github.com/mamba-org/mamba/issues/488#issuecomment-1400575225) Long live conda/mamba on shared clusters!

OK, wait. Let's back up. What's this bug, and why does it matter that it's fixed?

It all starts with teaching...

## conda is, like, the best for teaching bioinformatics!!

I've been teaching bioinformatics using conda for about 5 years now. Not only do I straight up [teach conda/mamba](https://hackmd.io/VTcCz9dmSf6vclaHRwavlw?view) but I also use it extensively in my Intro Bioinformatics hands-on lab for graduate students, where I teach [variant calling](https://github.com/ngs-docs/2023-ggg-201b-lab/blob/main/lab-1.md), de novo assembly, and RNAseq.

Mostly I teach on a shared cluster, the 'farm' HPC, because that's where many of the students will be doing their research.

And I teach conda (and mamba) for a few reasons:

* it works!
* you don't need admin privileges to install specific versions of your software!
* most bioinformatics command-line software is available via conda!
* many (most?) Python packages _and_ many (most?) R packages are available from conda-forge or bioconda!
* and, most recently, one of our admins, Camille Scott, got RStudio Server working so that it loads R and R packages from conda environments!

So, basically, conda is a full solution for students to take and use _after_ my class is over.

## My teaching setup for conda

I teach using a bunch of accounts specifically created for the course. These accounts are set up so that I have ssh access into them, which is really important; and they have specific queue access. It all works really well! Well, mostly.

Things that work out of the box: software installed with conda. Yay!

Things that don't work out of the box: 30 students simultaneously downloading the same packages from conda-forge.

This is because 30 students downloading 500 MB of packages from the same remote Web site is slow ;).

The thing is, it's not really necessary for everyone to download the packages - most of the time, students are only downloading packages all at the same time during class, and they're all downloading the _same_ packages. We should be able to cache them!

So I've set up the accounts with a central cache. Read on...

## Using a central package cache for a bunch of accounts

It's actually pretty straightforward to set up; there are two components: a [condarc file](https://github.com/ngs-docs/shared-conda-on-farm/blob/main/condarc),
```yaml
pkgs_dirs:
  - ~/.conda/pkgs
  - /home/ctbrown/remote-computing.cache
```
that specifies a package cache directory that's shared; and an [install script](https://github.com/ngs-docs/shared-conda-on-farm/blob/main/install-mambaforge.sh) that I run in each "child" account that installs and configures conda to use the shared cache:
```shell 
$ cd ~/
$ mkdir -p ~/.conda/pkgs
$ cp ~ctbrown/shared-conda-on-farm/condarc ~/.condarc
$ bash ~ctbrown/shared-conda-on-farm/Mambaforge-Linux-x86_64.sh -b -p $HOME/miniforge3
```
This sets things up so that all the accounts look for packages in one place, and download them to their local account if they're not there.

I run this script in each child account, and then I set up a separate parent account that has write privileges to the cache directory. This parent account must then download all of the desired conda packages, at which point they are then available to all the child accounts to use without download.

This works great, except for one thing: until recently, the child account mamba calls would complain bitterly if permissions were wrong.  And sometimes things would work out even less well and there would be crashes. So I had to be very mindful of how I installed packages. Which I wasn't always. Which caused problems.

And that's the bug that was fixed! - the specific [conda issue I've been paying attention to](https://github.com/mamba-org/mamba/issues/488#issuecomment-1400575225) references [this fix](https://github.com/mamba-org/mamba/pull/2141), which was actually pointed at [this issue](https://github.com/mamba-org/mamba/issues/1123). 

All's well that ends well - I upgraded all of the accounts to mamba 1.30 and ran some tests and it all seems to work! We did a stress test on Wednesday with ~30 people running through my snakemake lesson, and other than network glitches, life was good!

## Taking a step back: is conda all that?

Yes, it's great.

I'm sure it doesn't solve all the packaging problems, and I'm positive it's theoretically inferior to many things, but I've gotta say, it really **just works** for me (and people in my lab) 99% of the time.

Even better, other people are reporting that it's working well for them - including for R software installations.

## Conda and R

Conda solves a lot of R package installation problems for me.

I'm no R expert, but here is what I've gathered as to why I have a lot of problems:

The challenge with R installation is that many R packages need to be compiled before installation; I gather the R packaging ecosystem typically distributes things as source. This means installing them requires having a particular compiler tool-chain installed. Dependencies also become an issue. Basically, this is a point of fragility.

Conda conveniently does things in a different way: packages are distributed as binaries with no compilation required, and their dependencies include everything required for runtime. When this works, it works really well - you just download and install the compiled package for your system!

Even better, all of the conda magic works - you get to use an isolated environment, with the version of R you wanted to use, with all of the compatible packages installed. And if you need to install something yourself, you can do so _in_ that isolated conda environment without potentially contaminating your other R installs.

So, I now regularly use conda environments that look like this:

```yaml
channels:
    - conda-forge
    - bioconda
    - defaults
dependencies:
    - r-ggplot2
    - r-dplyr
    - r-readr
    - r-pheatmap
    - r-knitr
    - r-rmarkdown
    - r-rsqlite
    - r-data.table
    - r-kableextra
    - bioconductor-tximeta
    - bioconductor-deseq2
    - bioconductor-summarizedexperiment
    - r-base
    - r-irkernel=1.1
    - r-devtools
```
and it works really well for me.

I'll note that the situation has really improved over the last 3 years - I used to have lots of issues, but conda-forge has really stepped up their game and now most of my problems occur elsewhere (problem-specific stuff, basically).

One concern with conda has been the availability of common R packages. Here I'm happy to say that Fredrik Boulund reported that he was able to find that all but one of 600 of their internally used R packages were already available on conda-forge. So that's pretty cool!

## One last thought for you...

...or maybe two ;).

Packaging for data science software really requires a community. There are so many packages, and so many diverse and disparate needs, that if you want a solution that satisfies > 80% of the needs you need to build off a diverse community. If the community mechanisms include a way to add your own packages of interest (like conda-forge and bioconda do) then that results in magic!

Also, I think software solutions have to incorporate the newbie/learners perspective. If I can't get a class of 30 people to robustly use your solution, then that's a problem.

--titus
