Title: sourmash databases as zip files, in sourmash v3.3.0
Date: 2020-05-07
Category: science
Tags: sourmash, minhash, gtdb
Slug: 2020-sourmash-databases-as-zip-files
Authors: C. Titus Brown
Summary: Use compressed databases directly!

The feature that I'm most excited about in [sourmash 3.3.0](https://github.com/dib-lab/sourmash/releases/tag/v3.3.0) is the ability to directly use _compressed_ SBT search databases.

Previously, if you wanted to search (say) 100,000 genomes from GenBank, you'd have to download a several GB .tar.gz file, and then uncompress it out to ~20 GB before searching it. The time and disk space requirements for this were major barriers for teaching and use.

In v3.3.0, [Luiz Irber](https://twitter.com/luizirber/) fixed this by, first, releasing the [niffler](https://lib.rs/crates/niffler) Rust library with [Pierre Marijon](https://twitter.com/pierre_marijon), to read and write compressed files; second, replacing our old khmer Bloom filter nodegraph with a Rust implementation ([sourmash PR #799](https://github.com/dib-lab/sourmash/pull/799)); and, third, adding direct zip file storage ([sourmash #648](https://github.com/dib-lab/sourmash/pull/648)).

So, as of the latest release, you can do the following:

```
# install sourmash v3.3.0
conda create -y -n sourmash-demo \
    -c conda-forge -c bioconda sourmash=3.3.0
    
# activate environment
conda activate sourmash-demo

# download the 25k GTDB release89 guide database (~1.4 GB)
curl -L https://osf.io/5mb9k/download > gtdb-release89-k31.sbt.zip

# grab a genome signature - here, download a demo one from OSF
curl -L https://osf.io/vhnk4/download > genome.sig

# search!
sourmash search genome.sig gtdb-release89-k31.sbt.zip
```
This takes less than 2 GB of disk space total (including conda env), and the search runs in about 3 seconds and 120 MB of RAM.

Using the zip file stuff alone is a slight speed drag (~10-20%?), but the shift to Rust [leads to an overall speed increase of about 4x](https://twitter.com/ctitusbrown/status/1257419632572538882). And you can always unpack the zip file and use the unpacked files directly.

Yay!

## New database releases are coming!

Over the next few months, we plan to release all our SBT databases as zip files!

As usual, per our semantic versioning guidelines, you'll need sourmash v3.3 or later to use the zip files. However, old databases will continue to work for all sourmash v3.x, and probably v4.x as well (and maybe beyond :).

--titus
