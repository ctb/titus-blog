Title: Transition your Python project to use pyproject.toml and setup.cfg! (An example.)
Date: 2021-02-02
Category: python
Tags: screed
Slug: 2021-transition-to-pyproject.toml-example
Summary: Updating old Python packages, in this year of the PSF 2021!

*Thanks to Luiz Irber for all the pre-work on sourmash, as well as the code reviews on screed; and Brett Cannon for a review of an earlier version of this blog post!*

The future of Python packaging is pyproject.toml, and (for now) setup.cfg, based on [PEP 518](https://snarky.ca/clarifying-pep-518/) and (soon) [PEP 621](https://www.python.org/dev/peps/pep-0621/).

For some background, please read ["What the heck is pyproject.toml"](https://snarky.ca/what-the-heck-is-pyproject-toml/), and also [Where to get started with pyproject.toml?](https://discuss.python.org/t/where-to-get-started-with-pyproject-toml/4906)

The [relevant setuptools docs](https://setuptools.readthedocs.io/en/latest/build_meta.html) have been updated to reflect the new toolchain, too!

My takeaway from all of this is:
* configuration files are better than scripts
* a few standard configuration files are better than many
* declarative/static is better than procedural/dynamic

OK! *rubs hands with glee* let's do this!

## "But what do I actually _do_?"

Brett's post is pretty excellent and was really informative for me, but I have a high tolerance for reading lots of text! It's probably a bit long for people who just want to update their project, though ;).

So I decided to give it a try myself and then post an example!

Recently, I wanted to release a new version of [screed](https://github.com/dib-lab/screed/), in order to get rid of some DeprecationWarnings for the release of [sourmash 4.0](https://github.com/dib-lab/sourmash/). Now, screed is a remarkably ...stable project, by which I mean it does the thing we need it to do and no more, and we're not changing it at all.

BUT. Screed was based on an old school setup.py. So, inspired by Luiz Irber's updating of sourmash to use pyproject.toml, I updated screed similarly. (It was REALLY helpful to have an example!)

## tl;dr

[Here is the diff.](https://github.com/dib-lab/screed/pull/83/files)

In brief,

* your `pyproject.toml` can be very close to boilerplate.
    * It's basically the three lines that Brett posted...
    * the additional stuff for screed has to do with [setuptools_scm](https://pypi.org/project/setuptools-scm/), which we're using to automatically convert git tags like `v1.0.4` into actual version numbers.
* your `setup.cfg` basically contains almost everything your `setup.py` contained, just a bit reformatted to fit into the [setup.cfg format](https://docs.python.org/3/distutils/configfile.html).
* your new `setup.py` can now be a really short stub to permit `python setup.py ...` to continue to work.

I hope this helps! Comment and ask questions as you have them!

(Also: I just released [screed v1.0.5!](https://github.com/dib-lab/screed/releases/tag/v1.0.5) :tada:)

--titus
