Title: sourmash has a plugin interface!
Date: 2023-01-08
Category: science
Tags: sourmash, plugins, oss
Slug: 2023-sourmash-plugins-first-effort
Authors: C. Titus Brown
Summary: Enabling plugins in sourmash, for less directed & more incoherent progress!

Over the holiday break, I took on a "palette cleansing" project - something technically neat, that wasn't critically important to anyone or anything, but could be useful. I decided to implement plugins for sourmash.

[Sourmash](sourmash.readthedocs.io/) is open-source scientific software for fast, lightweight exploration of sequencing data set comparison, with a focus on metagenomics. It's largely a command-line program written in Python on top of a Rust library. It is maintained by a small group of developers, most of whom are (or were) affiliated in some way with my academic lab at UC Davis.

Python has (what seems to be) robust support for third-party plugins, where a project can provide hooks for _other people_ to customize functionality.

So the question was, can we add Python plugin support to sourmash?

## First - why focus on plugins?

Plugins serve a lot of purposes for a project, but I think the most interesting justification for supporting them came from Tim Head, who channeled his observations of Simon Willison's [datasette](https://datasette.io/) project into a statement that **plugins are an alternate way to direct open source projects**. (You can read the whole Twitter thread [here](https://twitter.com/betatim/status/1355902709237473281).)

Tim's tl;dr was this: 

>"first class plugins" is my current best answer to "we need a project roadmap"

but what does that mean?

The central idea is that the more extensible you make a project with plugins, the easier it is for everyone to "play" with the project, 
pursue their own directions, and figure out what to do next.

Or, to rephrase: if you focus your planning and governance efforts on defining how others can extend the core functionality of your software, then you free others up to do so without permission or close engagement. This can enable a lot of experimentation and creativity!

That was a large part of my sociotechnical motivation in looking into plugins, but there were several more reasons:

* Maintaining an open source project is a fair bit of work, and I have a lot of interest in keeping the "feature surface" of sourmash small so that there's less to maintain. That battles with the desire to add more functionality to meet research and user needs. Plugins offer a way to segregate efforts to either side of a well-defined interface: either it's a "core" effort (lots of coordination and work!) or an "external" effort (maybe less work, certainly less coordination), and we can allocate our attention appropriately.

* With a robust core, plugins can combine to expand the feature surface of sourmash combinatorially. That's a fancy way of saying that if there's a neat new visualization plugin written by Tina, and a neat new remote-collection loading mechanism written by Steve, people can use these plugins in _combination_ to apply the viz to remote collections.

* Right now it's quite hard to add platform-specific features to sourmash - in particular, there are some software packages that we'd like to use that don't compile on Mac OS ARM laptops. Plugins would be one way to support those features on specific platforms.

* Refactoring internals to support plugins can clean up the internal code! The loading and saving plugins are implemented in exactly the same way as our internal code, and I think the effort to modularize loading/saving over time has ended up with reasonably simple and decent code internally. Plugins reinforce that by standardizing the API.

## And how's that going, Dr. Brown?

What I can say after putting in a dozen or so hours of work on the plugin framework is that it's been very liberating - it's just _so much easier_ to try out new ideas, and clearly distinguish them from "serious" core code contributions that need more care and thought.

So, ...it's going well!

## What types of plugins does sourmash support?

As of this morning, the main branch of sourmash supports `load_from` and `save_to` plugins. As the names suggest, these plugins provide alternate ways of loading and saving sourmash sketches.

Using these, I've built out an [Avro format saving/loading plugin](https://github.com/sourmash-bio/sourmash_plugin_avro) as well as a [load-sketches-from-URIs plugin based on fsspec](https://github.com/sourmash-bio/sourmash_plugin_load_urls).

I'm [currently working](https://github.com/sourmash-bio/sourmash/pull/2438) on adding  support for new command-line subcommands. The idea is that you would be able to add new commands under `sourmash scripts` (a provisional name).

## How did we implement plugin support?

You can see [the first plugin PR here, in sourmash#2428](https://github.com/sourmash-bio/sourmash/pull/2428), but the tl;dr is: we used [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html) to support plugins via [entry points](https://setuptools.pypa.io/en/latest/userguide/entry_point.html).

The code to support plugins is pretty minimal, and currently resides in [sourmash.plugins](https://github.com/sourmash-bio/sourmash/blob/latest/src/sourmash/plugins.py). It looks like this:

```python
# load entry points.
_plugin_load_from = entry_points(group='sourmash.load_from')


def get_load_from_functions():
    "Load the 'load_from' plugins and yield tuples (priority, name, fn)."

    # Load each plugin,
    for plugin in _plugin_load_from:
        loader_fn = plugin.load()

        # get 'priority' if it is available
        priority = getattr(loader_fn, 'priority', DEFAULT_LOAD_FROM_PRIORITY)

        # retrieve name (which is specified by plugin?)
        name = plugin.name

        yield priority, name, loader_fn
```

Then, in the `pyproject.toml` of a Python package, anyone can state that there's a sourmash plugin available like so:

```
[project.entry-points."sourmash.load_from"]
a_reader = "module_name:load_sketches"

[project.entry-points."sourmash.save_to"]
a_writer = "module_name:SaveSignatures_WriteFile"
```

and this will get automatically loaded and used by sourmash.

## How do plugins fit into the sourmash ecosystem?

We have an interesting lab-centric / lab-adjacent ecosystem developing around sourmash.

sourmash itself provides a reasonably rich Python and Rust API, for people wanting to do clever things with it. For example, the [branchwater software](https://www.biorxiv.org/content/10.1101/2022.11.02.514947v1) is a fairly small script for doing parallel search of many genomes, built on top of the Rust library.

There are workflows that make use of sourmash to do cool things, like characterizing metagenomes ([genome-grist](https://dib-lab.github.io/genome-grist/)) and decontaminating databases ([charcoal](https://github.com/dib-lab/charcoal/)). These (and other) workflows wrap sourmash in a larger workflow (snakemake, nextflow, CWL, ...?) to do various things.

There's also a nascent [R library, sourmashconsumr](https://github.com/Arcadia-Science/sourmashconsumr) being built by Taylor Reiter (and others) at Arcadia Science, for taking the output of sourmash and doing nice things with it.

Taylor is also developing code to load sourmash `compare` and `gather` output into MultiQC (see [issue](https://github.com/ewels/MultiQC/issues/1805)). This is in effect using sourmash as a plugin for _other_ software.

And now, sourmash plugins add a nice set of opportunities to diversify sourmash internal functionality to this ecosystem. It will be interesting to watch what happens as we build out this functionality!

## How do we support plugin developers?

An important aspect of plugins is supporting plugin developers - so, [we have some nascent documentation](https://sourmash.readthedocs.io/en/latest/dev_plugins.html), as well as a [getting-started template repository](https://github.com/sourmash-bio/sourmash_plugin_template) to eliminate a lot of the boilerplate.

I'm not 100% sure what to add beyond this, but I find dogfooding it to be a good approach - every time I work on a plugin, I will sand down the sharper corners of our documentation a bit more.

## Where next?

For now, plugins remain experimental and are not subject to semantic versioning considerations. I'm not sure when that will change, but I want to write a few more plugins before committing to the current interfaces!

I think we probably have room for many more _types_ of plugins. We're thinking about how to enable different taxonomy loading functions, for example; and I have specific need for better manifest/picklist manipulation that I think is amenable to being made a plugin. (The plugin design issue is [sourmash#1353](https://github.com/sourmash-bio/sourmash/issues/1353) if you're interested.)

I am also starting to think more about the user experience. How do users find, install, use, debug, and remove plugins? This is all relatively easy if you're a Python developer who is familiar with `pip` and `importlib.metadata`, but that's not our user base ;). For now, I've started by adding plugin reporting to `sourmash info -v`, which at least gives us a chance of figuring out what plugins might be around!

I'm also not quite sure how to manage what I expect to be a flood of small plugins from within my lab. Will we want to have a set of recommended plugins that evolves and matures over time? And how do we avoid massively increasing our maintenance surface? (Simon Willison has some [sage advice for the serial project hoarder that applies here](https://simonwillison.net/2022/Nov/26/productivity/).)

I also have this niggling feeling that I should read through datasette's plugin interface to see what I can learn from all of Simon's hard work and experience...

--titus
