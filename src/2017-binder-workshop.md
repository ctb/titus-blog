Title: The 2017 binder workshop!
Date: 2017-10-22
Category: science
Tags: binder, docker, reproducibility
Slug: 2017-binder-workshop
Authors: C. Titus Brown
Summary: We had a workshop! On binder!

tl;dr? We ran a workshop on binder. It was fun!

## What is binder?

Imagine... that you are visiting the data repository for a preprint
you are reviewing, and with the click of a button you are brought to a
fully configured RStudio Server containing that data.

Imagine... you are running a workshop, and you want to introduce
everyone in the workshop to a machine-learning approach.  You give
them all the same URL, and within seconds everyone in the room is
looking at their own live environment, copied from your blueprint but
individually modifiable and exportable.

Imagine... your lab has a collection of standard data analysis
protocols in Jupyter Notebooks on your GitHub site, and anyone in your
lab can, with a single click, bring them to life and run them on a
new data set.

Binder is a concept and technology that makes all of the above, and more,
tantalizingly close to everyday realization!  The techie version is this:
currently,

* upon Web request, binder grabs a GitHub repository, inspects it, and
  builds a custom Docker image based on a variety of configuration
  detection;
  
* then, binder spins up a Docker container and redirects the Web browser to
  that repo;
  
* at some point, binder detects lack of activity and shuts down the
  container.
  
All of this is (currently) done without authentication or payment of any
time, which makes it a truly zero configuration/single-click experience for
the user.

## The workshop!

In 2016, I wrote a
[proposal to fund a workshop on binder](https://github.com/dib-lab/2016-binder-proposal-to-sloan)
to the Sloan Foundation and it was funded!! We finally ran the workshop
last week, with the following organizing committee:

* [Abby Cabunoc Mayes](https://twitter.com/abbycabs?lang=en), Mozilla.
* [Tim Head](https://twitter.com/betatim), everware
* [Chris Holdgraf](https://twitter.com/choldgraf), UC Berkeley/Jupyter team
* [Yuvi Panda](https://twitter.com/yuvipanda?lang=en), UC Berkeley/Jupyter team.

## Why a workshop?

Many people, including myself, see massive potential in binder, but it
is still young.  The workshop was intended to explore possible
technical directions for binder's evolution, build community around
the binder ecosystem, and explore issues of sustainability.

One particular item that came up early on in the workshop was that
there are many possible integration pointers for binder into current
data and compute infrastructure providers.  That's great! But, in the
long term, we also need to plan for the current set of endeavors
failing or evolving, so we should be building a community around the
core binder concepts and developing de facto standards and practice.
This will allow us to evolve with endeavors as well as finding new
partners.

So that's why we ran a workshop!

## Who came to the workshop?

The workshop attendees were a collection of scientists, techies, librarians,
and data people.  For this first workshop I did my best to reach out to
people from a variety of communities, and [somewhat succeeded](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Binder%20workshop%20master%20page.md#likely-attendees).  We didn't
advertise very widely, partly just because of a last minute time crunch,
and also because too many people would have been a problem for the space we
had.

As we figure out more of a framework and sales pitch for binder, I expect the
set of possible attendees to expand. Still, for hackfest-like workshops, I'm
a big fan of small diverse groups of people in a friendly environment.

## What is the current state of binder?

The original mybinder.org Web site was created and supported by
[the Freeman Lab](https://www.janelia.org/our-research/former-labs/freeman-lab), but maintenance on the site suffered when
Jeremy Freeman moved to the Chan-Zuckerberg Initiative and became even
busier than before.

The Jupyter folk picked up the binder concept and reimplemented the
Web site with somewhat enhanced functionality, building the new
BinderHub software in Python around JupyterHub and breaking the
repository-to-docker code out into `repo2docker`.  This is now running
on a day-to-day basis on a beta site.

A rough breakdown, and links to documentation, follow:

[JupyterHub](https://jupyterhub.readthedocs.io/en/latest/) - JupyterHub manages multiple instances of the single-user Jupyter notebook server. JupyterHub can be used to serve notebooks to a class of students, a corporate data science group, or a scientific research group.

[Zero-to-JupyterHub](https://zero-to-jupyterhub.readthedocs.io/) - Zero to JupyterHub with Kubernetes is a tutorial to help install and manage JupyterHub.

[BinderHub](https://binderhub.readthedocs.io/en/latest/) - BinderHub builds "binders" containing data+code from GitHub repos and then serves the binders in a custom computing environment. [beta.mybinder.org](http://beta.mybinder.org) is a public BinderHub.

[repo2docker](https://repo2docker.readthedocs.io/en/latest/) - repo2docker builds, runs, and pushes Docker images from source code repositories.


## Highlights of the binder workshop!

What did we do? We ran things as an unconference, and had a lot of
discussions and brainstorming around use cases and the like, with some
super cool results. The notes from those are linked below!

A few highlights of the meeting deserve, well, highlighting --

* Amazingly, we got to the point where binder ran an RStudio Server
  instance, started from a Jupyter console!!  Some tweets of this made
  the rounds, but it may take a few more weeks for this to make it
  into production.  (This was, I think, mostly the product of Carl
  Boettiger sitting down with Yuvi Panda and Aaron Culich to work out
  the actual right base Docker image and shims to make it all work,
  aided and abetted by Adelaide Rhodes asking lots of questions.)
  
* Pretty much everyone who attended the workshop got to the point where
  we had set up our own BinderHub instance on Google
  (using these [JupyterHub](https://zero-to-jupyterhub.readthedocs.io/en/latest/) and [BinderHub](https://binderhub.readthedocs.io/en/latest/) instructions).
  w00000t! ([Session notes](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Jupyter%20Hub-Binder%20Hub%20setup.md))
  
* Yuvi Panda gave us a rundown on the [data8](http://data8.org/) /
  "Foundations of Data Science" course at UC Berkeley, which uses
  JupyterHub to host several thousand users, with up to 700 concurrent
  sessions.
  
We came up with lots of [use cases](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Binder%20workshop%20in%20flight%20-%20schedule,%20links,%20etc.md#use-cases-for-binder) - see ~duplicate set of notes, [here](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Binder%20workshop%20-%20use%20cases%20day%201%20output.md).

## Other stuff we did at the workshop

([All the notes are on GitHub, here](https://github.com/ctb/2017-binder-workshop-notes))

Here is a fairly comprehensive list of the other activities at the workshop --

* We walked through [creating your own binder](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Creating%20a%20binder%20on%20github.md)
* We also did a "round trip" where we modified an existing binder repo and then created a binder with the changes. [see notes](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Titus's%20demo%20of%20Binder.md)
* [Got Data?](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Got%20Data%3F.md) - discussions about how to get data into binders
* [Sustainability and growing a community](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Sustainability%20&%20growing%20a%20community.md)
* [A binder in every pot! The binder ecosystem](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Binder%20for%20everybody.md) - also see Titus' [handwritten notes](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Notes-from-sustainability-2-with-gail.pdf)
* [Best practices for teaching with binder](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Best%20Practices%20for%20teaching%20with%20binder.md)

## Issues that we only barely touched on:

* "I have a read only large dataset I want to provide access to for untrusted users, who can do whatever they want but in a safe way." What are good practices for this situation? How do we provide good access without downloading the whole thing?

* It would be nice to initiate and control (?) Common Workflow Language workflows from binder - [see nice Twitter conversation with Michael Crusoe](https://twitter.com/ctitusbrown/status/922497738029150208).

* How do we do continuous integration on notebooks??

* We need some sort of introspection and badging framework for how reproducible a notebook is likely to be - what are best practices here? Is it "just" a matter of specifying software versions etc and bundling data, or ...??

## Far reaching issues and questions --

* it's likely that the future of binder involves many people running many different binderhub instances.  What kind of clever things can we do with federation? Would it be possible for people to run a binder backend "close" to their data and then allow other binderhubs to connect to that, for example?

* Many issues of publishing workflows, provenance, legality - [notes](https://github.com/ctb/2017-binder-workshop-notes/blob/master/Binder%20-%20notes%20from%20provenance-legal-authorship%20breakout.md)

* It would be super cool if realtime collaboration was supported by JupyterHub or BinderHub... it's coming, I hear. Soon, one hopes!

## Topics we left almost completely untouched:

* [thebe-like libraries](https://github.com/oreillymedia/thebe)
* [nteract.io](https://nteract.io/)
* [tmpnb](https://github.com/jupyter/tmpnb)
* custom remote kernels
* singularity!
* how to authenticate to use binder-like environments on your own
  compute (e.g. HPC) or compute account (e.g. AWS, Google, Azure).

## What's next?

I'm hoping to find money or time to run at least two more hackfests or
conference -- perhaps we can run one in Europe, too.

It would be good to run something with a focus on developing training materials
(and/or exemplary notebooks) - see Use Cases, above.

I'm hoping to find support to do some demo integrations with scholarly
infrastructure, as in in the Imagine... section, above.

If (**if**) we ran a conference, I could see having some of the following
sessions:
- A hackfest building notebooks
- A panel on deployment
- keynote on the roadmap for binder and JupyterHub
- Some sort of community fest

If you're interested in any of this, [please indicate your interest in future workshops!!](https://docs.google.com/forms/d/e/1FAIpQLSfNcUHUjjoaIcpVjAOZfUA32W7BIPHA7NCR8BhsKgj-HqTBBA/viewform)

## Some other links worth mentioning:

* [nbflow](https://github.com/jhamrick/nbflow) - one-button reproducible workflows with Jupyter Notebook and Scons (see [video](https://www.youtube.com/watch?v=Fc2W930NJs8))
* [dataflow](https://github.com/dataflownb/dfkernel) - a kernel to support Python dataflows in the Jupyter Notebook environment.

* [an example](https://github.com/binder-examples/jupyterlab/tree/master/binder) of how to use the new `postBuild` functionality to install jupyter notebook extensions.

aaaand some notes from singularity:

One way to convert docker images to singularity images,
using [docker2singularity](https://github.com/singularityware/docker2singularity)
```
docker run -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/image:/output \
    --privileged -t --rm singularityware/docker2singularity ubuntu:14.04  
```

Another way to simply run docker containers in singularity:
```
singularity exec docker://my/container <runcommand>
```

## The End

No particular conclusion other than we'll have to do this again!

--titus

Lots of examples here

https://github.com/binder-examples


Repo sourced from Ryan Lovett worked on by Carl and others
https://github.com/binder-examples/dockerfile-r

gitter
https://gitter.im/jupyterhub/binder

and google groups
https://groups.google.com/forum/#!forum/binderhub-dev

papermill:
https://t.co/3uxgyxvbmC

thebe:
https://minrk.github.io/thebelab/
