Title: Speeding sourmash the heck up
Date: 2024-02-20
Category: science
Tags: sourmash, oss, branchwater
Slug: 2024-speeding-sourmash-the-heck-up
Authors: C. Titus Brown
Summary: Faster things are always nice, right?

sourmash is our tool for genome and metagenome investigation. Using and developing it has been a major focus of our lab for over 7 years, and maintaining and extending it is my main passion project. sourmash is a k-mer multitool that enables all sorts of really neat bulk metagenome analyses!

I'm proud to say that last week we released [a new version of sourmash, v4.8.6](https://github.com/sourmash-bio/sourmash/releases/tag/v4.8.6), that continues to improve functionality, increase documentation, and decrease computational requirements. But, you know, we release new versions of sourmash pretty regularly, so that's only moderately exciting :).

A bit more exciting - we are hopefully closing in on an updated Journal of Open Source Software publication via our [pyopensci review](https://github.com/pyOpenSci/software-submission/issues/129). I wanted to highlight something very nice one of our reviewers said:
>Outstanding work with sourmash! Your commitment to creating a package that's both easily maintainable and well-documented truly shines through. The code is impressively organized, accompanied by clear comments explaining each section, making it easy to comprehend the purpose of each file and function.

It's so nice to have your multiple years of effort be appreciated!

The most exciting news is that we've released a significant update to our [branchwater plugin for sourmash](https://github.com/sourmash-bio/sourmash_plugin_branchwater). This plugin supplies fast, low-memory, and multithreaded versions of common sourmash functions. [Version 0.9.0 of sourmash_plugin_branchwater](https://github.com/sourmash-bio/sourmash_plugin_branchwater/releases/tag/v0.9.0) dramatically improves the convenience of using the plugin while also speeding up a common use case and, perhaps most importantly to us maintainers, making significant moves towards convergence with the core sourmash code base.

What's that, you say?? **Fast, low-memory, and multithreaded** sourmash functionality?

Yep. Using our test metagenome, the SRR606249 mock community, you can search all 400,000 genomes in the GTDB rs214 release in around 2 minutes and under 2 GB of RAM, using 64 cores. This is 7 fold lower memory than regular ol' sourmash, and approximately 20x faster.  Even cooler, if you index GTDB first, you can do it in 600 MB of RAM!

| software/version | command | details | time | max RAM |
| -------- | -------- | -------- | -- | -- |
| sourmash v4.8.6 | `gather` | the OG | 42m 26s | 14.5 GB |
| branchwater v0.9.0 | `fastgather` | against zip | <span style="color:green">**2m 5s**</span> | <span style="color:red">**14.1 GB^**</span> |
| branchwater v0.9.0 | `fastgather` | against pathlist | <span style="color:green">**2m 26s**</span> | <span style="color:green">**1.8 GB**</span> |
| branchwater v0.9.0 | `fastgather` | against manifest | <span style="color:green">**2m 19s**</span> | <span style="color:green">**1.9 GB**</span> |
| branchwater v0.9.0 | `fastmultigather` | against rocksdb | <span style="color:green">**2m 8s**</span> | <span style="color:green">**600 MB**</span> |
| branchwater v0.8.6 | `fastgather` | against pathlist | 2m 24s | 1.6 GB |
| branchwater v0.8.6 | `fastgather` | against zip | <span style="color:purple">**28m 34s**</span> | 1.7 GB | 

^ This benchmark number isn't really real, despite it being reported under Max RSS. The measurement is high because the zip library we're using in Rust uses `memmap` - actual heap consumption is in the 2 GB range, matching the other approaches. See [sourmash#2340](https://github.com/sourmash-bio/sourmash/issues/2340) for more info. 

Anyhoo. sourmash v4.8.6 and sourmash_plugin_branchwater v0.9.0 are both available via conda & conda-forge. Enjoy!

--titus
