Title: Four steps in five minutes to deploy a Carpentry lesson for a class of 30
Date: 2017-12-02
Category: science
Tags: binder, docker, reproducibility, swc, carpentry
Slug: 2017-four-steps-five-minutes-binder
Authors: C. Titus Brown
Summary: Binders full of Carpentry!

[binder](http://mybinder.org) is an awesome technology for making GitHub repositories "executable". [With binder 2.0](https://elifesciences.org/labs/8653a61d/introducing-binder-2-0-share-your-interactive-research-environment), this is now newly stable and feature-full!

Yesterday I gave a two hour class, introducing graduate students to things like Jupyter Notebook and Pandas, via the [Data Carpentry Python for Ecologists lesson](https://www.datacarpentry.org/python-ecology-lesson/).  Rather than having everyone install their own software on their laptop (hah!), I decided to give them a binder!

For this purpose, I needed a repository that contained the lesson data and told binder how to install pandas and matplotlib.

Since I'm familiar with GitHub and Python `requirements.txt` files, it took me about 5 minutes. And the class deployment was flawless!

## Building the binder repo

1. Create a github repo (https://github.com/ngs-docs/2017-davis-ggg201a-day1), optionally with a README.md file.

2. Upload `surveys.csv` into the github repository (I got this file as per [Data Carpentry's Python for Ecology lesson](http://www.datacarpentry.org/python-ecology-lesson/01-starting-with-data/)).

3. Create a `requirements.txt` file containing:

```
pandas
numpy
matplotlib
```
    
   -- this tells binder to install those things when running this repository.

4. Paste the GitHub URL into the 'URL' entry box at [mybinder.org](http://mybinder.org) and click 'launch'.

## Two optional steps

These steps aren't required but make life nicer for users.

5. Upload an `index.ipynb` notebook so that people will be sent to a default notebook rather than being dropped into the Jupyter Console; note, you'll have to put 'index.ipynb' into the 'Path to a notebook file' field at mybinder.org for the redirect to happen.

5. Grab the 'launch mybinder' Markdown text from the little dropdown menu to the right of 'launch', and paste it into the README.md in your github repo.  This lets people click on a cute little 'launch binder' button to launch a binder from the repo.

## Try it yourself!

Click on the button below,

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/ngs-docs/2017-davis-ggg201a-day1/master?filepath=index.ipynb)

or [visit this URL.](https://mybinder.org/v2/gh/ngs-docs/2017-davis-ggg201a-day1/master?filepath=index.ipynb)

-- in either case you should be sent ~instantly to a running Jupyter Notebook with the `surveys.csv` data already present.

Magic!!

## What use is this?

This is an excellent way to do a quick demo in a classroom!

It could serve as a quickfix for people attending a Carpentry workshop who are having trouble installing the software.

(I've used it for both - since you can get a command line terminal as well as Python Notebooks and RStudio environments, it's ideal for short R, Python, and shell workshops.)

The big downside so far is that the environment produced by mybinder.org is temporary and expires after some amount of inactivity, so it's not ideal for workshops with lots of discussion - the repo may go away! No good way to deal with that currently; that's something that a custom JupyterHub deployment would fix, but that is too heavyweight for me at the moment.

[(We came up with a lot of additional use cases for binder, here.)](http://ivory.idyll.org/blog/2017-binder-workshop.html).

Thoughts & comments welcome, as always!

--titus
