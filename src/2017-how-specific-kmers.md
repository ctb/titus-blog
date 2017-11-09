Title: How specific are k-mers for taxonomic assignment of microbes, anyway?
Date: 2017-11-09
Category: science
Tags: bioinformatics, minhash, ngs, metagenomics, taxonomy
Slug: 2017-how-specific-kmers
Authors: C. Titus Brown
Summary: K-mers are pretty specific at the genus level.

I've been on [a bit](http://ivory.idyll.org/blog/2017-something-about-kmers.html) of [a k-mers](http://ivory.idyll.org/blog/2017-taxonomy-of-tara-ocean-genomes.html) and [taxonomy](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-part-1.html) [kick](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-part-2.html) [lately](http://ivory.idyll.org/blog/2017-grokking-the-taxonomies.html), as readers [may have seen](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-try-again.html).  Now that I can [parse "free" taxonomies](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-try-again.html) from sources other than NCBI, I decided the code was well-enough baked to put it into [sourmash](https://github.com/dib-lab/sourmash/). So, over the last week I started integrating the lowest common ancestor code and taxonomy parsing code into sourmash; once [that pull request](https://github.com/dib-lab/sourmash/pull/367) is merged, sourmash will have `lca index`, `lca classify`, `lca summarize`, and `lca rankinfo` commands - see [the tutorial](https://github.com/dib-lab/sourmash/blob/add/lca/doc/tutorials-lca.md) for more information on how to run this stuff.

To celebrate the addition of all this code, I thought I'd address the question, "how specific are k-mers?" That is, if we reach into a bucket of metagenome sequence and pick out a k-mer that is identified with a particular species, how certain can we be of that identification (vs it being actually a different species in the same genus, family, order, etc.)

This question comes up routinely in discussions and now I have the information to answer it, at least in the context of all known microbial genomes!  (The answer will, of course, be very biased by what's not in our databases.)

After downloading the genbank LCA database, I ran the command:
```shell
sourmash lca rankinfo genbank-k31.lca.json.gz
```

and after a little data munging got this:

```shell
superkingdom: 38077 (0.4%)
phylum: 24627 (0.3%)
class: 39306 (0.4%)
order: 66423 (0.7%)
family: 97908 (1.1%)
genus: 1103223 (12.0%)
species: 7818876 (85.1%)
```

That is, 85% of the 31-mers in genbank are specific to the species level; 12% are specific to the genus level; and the remaining ~3% are family or above.

I would argue this makes genus level assignments pretty reliable, when using k-mers. (It doesn't say much about what you're missing, of course.)

--titus
