Title: How does sourmash's lca classification routine compare with GTDB classifications?
Date: 2019-12-31
Category: science
Tags: sourmash, taxonomy, metagenomics, minhash, gtdb
Slug: 2019-sourmash-lca-vs-gtdb-classify
Authors: C. Titus Brown
Summary: GTDB databases again!

Yesterday
[I posted](http://ivory.idyll.org/blog/2019-sourmash-lca-db-gtdb.html)
about the
[GTDB taxonomy](https://www.biorxiv.org/content/10.1101/256800v2); we
are now providing prepared databases that can be used with sourmash's
taxonomy classification routines to classify genomes with GTDB.

The databases we posted are built from the dereplicated 25k GTDB
genomes distributed as part of the
[GTDB-Tk classification toolkit](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btz848/5626182),
and not the full 145k classifications in GTDB. So they are smaller
than they could be, and also potentially lower resolution. Moreover,
sourmash uses k-mers instead of amino acids, which may lead to
different classifications.

A good first question is, how well do classifications with `sourmash
lca classify` & 25k genomes compare to the full 145k classifications
in GTDB? This is basically a measure of generalizability - how
reliably can we infer the classifications of the 145k genomes from the
25k?

## Comparing `sourmash lca classify` on Genbank to GTDB

I classified all 420k Genbank genomes using `sourmash lca classify`
with k=31, and I then wrote a script to compare the output to the GTDB
taxonomy. This involved some rather nasty identifier conversion which
sometimes failed, but we ended up with a good number of comparable
items:

```
identifiers in gtdb only:                  6901
identifiers in sourmash lca classify only: 247987
identifiers in both:                       137185
```

So we are using the harmonized 95% of gtdb identifiers and 35% of
sourmash identifiers for the below comparisons. (The missing items are
due to failed identifier munging, different versions of genbank, and
me using genbank-entire instead of refseq (which is the source of the
bulk of the sourmash-specific identifiers)).

Of the 137,185 genomes in common, a straight-up comparison of
classifications gave the following:

```
same:      79666 (58.1%)
different: 57519 (41.9%)
```

The 58.1% identical number is reassuring, but 41.9% disagreement is
not great - what's going on here?

It turns out that, in almost all situations, sourmash **agrees with**
but is **lower resolution than** GTDB.

```
different but consistent: 57498
   rank: superkingdom / count: 201
   rank: phylum / count: 36
   rank: class / count: 176
   rank: order / count: 94
   rank: family / count: 2260
   rank: genus / count: 54731
   rank: species / count: 0
```

That is, 201 of the sourmash classifications stop at the superkingdom
level, 36 continue to the phylum level, and so on.  Fully 95.1% match
at the genus level! And for all of these, the sourmash classifications
agree with the GTDB taxonomy - a full 99.96% of the time.

What about the disagreements?

```
inconsistent: 21
   rank: superkingdom / count: 0
   rank: phylum / count: 0
   rank: class / count: 0
   rank: order / count: 0
   rank: family / count: 0
   rank: genus / count: 21
   rank: species / count: 0
```
So all 21 of the disagreements are at the genus level... whew.

The upshot is that `sourmash lca classify` seems to work pretty well
as a first-round classification system, and will only lead you astray
at the genus level (and even then only rarely).  The species-level
accuracy could potentially be improved by using k=51 instead of k=31,
but that would probably decrease the number being identified, too.

## Comparing `sourmash lca classify` to GTDB-Tk.

The next question I had was, how does sourmash's computational
performance compare with the
[GTDB-Tk toolkit](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btz848/5626182)?
GTDB-Tk is the standard way to classify new genomes using the GTDB
taxonomy. How does sourmash lca classify compare computationally?

Using the sourmash k=21 LCA database (https://osf.io/9d5rx/), I
analyzed 336 randomly chosen genbank genomes with both sourmash and
GTDB-Tk. As with the full comparison above, the results are pretty
comparable:

* if sourmash lca classify yields a species-level designation, it is
  identical to what GTDB-Tk produces.
* at k=21, sourmash lca classify will never disagree with GTDB-Tk. At
  worse it will fail to classify out to species, genus, etc. level.

But how did the compute compare?

sourmash lca classify takes about 2 minutes to compute the signatures
and 35 seconds to classify 336 signatures. GTDB-Tk takes about 2 hours
with GTDB-Tk, using 8 threads.

sourmash lca classify used about 5 GB of RAM, compared to about 120 GB
of RAM for GTDB-Tk.

## Conclusions

So, it seems like sourmash lca classify is a decent prefilter for
GTDB-Tk, and that if you need to classify a lot of genomes quickly,
you could start with sourmash and then use GTDB-Tk to focus in on the
ones that aren’t classified at the species level.

In summary,

1. sourmash rarely disagrees with GTDB-Tk, and when it does, it's only
   at the genus level.
2. sourmash often fails to classify genomes that GTDB-Tk does.
3. sourmash is faster and requires less memory than GTDB-Tk. Compute
   efficiency is admittedly a focus of our project, so ...that's good?
   :)

Special thanks go to Taylor Reiter for suggesting that we look into
the GTDB taxonomy for sourmash, and Donovan Parks for corresponding with
me on various GTDB issues!

--titus

p.s. Here's the sourmash command I used to classify genomes:

```sourmash compute -k 21,31,51 —scaled=1000 *.fna.gz
sourmash lca classify \
    --query *.sig \
    --db gtdb-release89-k31.lca.json.gz  > lca-classify-all-k31.txt
```

p.p.s. To do the comparison, I ran our [sourmash bulk classify](https://github.com/dib-lab/2019-sourmash-gtdb/blob/master/bulk-classify-sbt-with-lca.py) script and then [converted the results into a lineage CSV](https://github.com/dib-lab/2019-sourmash-gtdb/blob/master/bulk-csv-to-lineages-csv.py). I separately [converted the GTDB taxonomy file](https://github.com/dib-lab/sourmash_databases/blob/master/translate_gtdb_gb_foo.py) to a lineage CSV, and then [compared the two](https://github.com/dib-lab/2019-sourmash-gtdb/blob/master/compare-bulk-lca-to-gtdb-entire.py). Do not try this at home, the scripts are ugly and require a lot of data that's only on our HPC at the moment :)
