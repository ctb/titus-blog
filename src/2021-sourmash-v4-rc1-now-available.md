Title: sourmash v4.0.0 release candidate 1 is now available for comment!
Date: 2021-02-19
Category: science
Tags: sourmash, software, release
Slug: 2021-sourmash-v4-rc1-now-available
Authors: C. Titus Brown
Summary: sourmash v4.0.0 is coming!

Hello everyone,

we are happy to announce the (imminent ;) release of sourmash 4.0, and present sourmash v3.5.1 and sourmash v4.0.0rc1 (release candidate 1) for your comments and questions!

sourmash is a command-line tool + Python & Rust library for quickly searching, comparing, and analyzing genomic and metagenomic data sets.

If you use sourmash regularly and are interested in upgrading, we are providing you with this release candidate so you can try out the migration guide and the new/revised functionality.

Draft release notes for 4.0.0 are [here](https://github.com/dib-lab/sourmash/releases/tag/v4.0.0rc1), and we have a [migration guide as well](https://sourmash.readthedocs.io/en/latest/support.html#migrating-from-sourmash-v3-x-to-sourmash-v4-x).

Please note that sourmash uses [semantic versioning](https://sourmash.readthedocs.io/en/latest/support.html#versioning-and-stability-of-features-and-apis), so v3.5.1 should not break any features or functionality. You should [version pin](https://sourmash.readthedocs.io/en/latest/support.html#version-pinning) your sourmash dependencies to `>=3,<4` if you want to continue using sourmash as before.

## sourmash v3.5.1 is the last release of v3.x

sourmash v3.5.1 should be the last release of sourmash v3. It adds warnings for features changed in 4.0.

More info on 3.5.1: https://github.com/dib-lab/sourmash/releases/tag/v3.5.1

You can install it like so from [PyPI](https://pypi.org/project/sourmash/3.5.1/
):
```
pip install sourmash==3.5.1
```

or with conda from bioconda and conda-forge:
```
conda install -c conda-forge -c bioconda sourmash=3.5.1
```

## sourmash v4.0.0 is coming soon!

sourmash v4.0.0rc1 is a feature-complete release of 4.0, with full migration docs. It contains many improvements and some breaking changes from 3.x.

Please see https://github.com/dib-lab/sourmash/releases/tag/v4.0.0rc1 for details!

To install [sourmash v4rc1 from PyPI](https://pypi.org/project/sourmash/4.0.0rc1/), please use:

```
pip install --pre sourmash==4.0.0rc1
```

(You can also install sourmash v3.5.1 from conda to get the
dependencies, and then upgrade to the latest version using pip.)

## Feedback requested!

We would very much appreciate feedback on the new features in sourmash, as well as comments and questions about upgrading. Please put comments on [the migration issue](https://github.com/dib-lab/sourmash/issues/1338).

C. Titus Brown and Luiz Irber

(for the sourmash development team :)
