Title: sourmash-oddify: a workflow for exploring contamination in metagenome-assembled genomes
Date: 2020-01-02
Category: science
Tags: sourmash, taxonomy, metagenomics, minhash, gtdb
Slug: 2020-sourmash-oddify
Authors: C. Titus Brown
Summary: Using k-mers and taxonomy to find contamination in metagenomes

(Thanks to Erich Schwarz, Taylor Reiter, and Donovan Parks for brainstorming and feedback on this stuff. Thanks also to Luiz Irber and Phillip Brooks for their work on sourmash!)

Yesterday, [I posted](http://ivory.idyll.org/blog/2020-sourmash-gtdb-oddities.html) about using k-mers and taxonomy to investigate Genbank genomes for potential contamination.

The underlying idea is pretty simple: look for subsets of k-mers that don't match the inferred taxonomy of the genome bins they're from, then analyze.

What started me down this path [over two years ago (!!)](http://ivory.idyll.org/blog/2017-comparing-genomes-from-metagenomes.html) was the use of the same underlying Tara Oceans metagenomic data for two separate papers, [Tully et al., 2018](https://www.nature.com/articles/sdata2017203) and [Delmont et al., 2018](https://www.nature.com/articles/s41564-018-0176-9). Both groups released their data early along with bioRxiv preprints, and it proved to be a treasure trove for my bioinformatics methods development - [all of the sourmash lca functionality](https://sourmash.readthedocs.io/en/latest/command-line.html#sourmash-lca-subcommands-for-taxonomic-classification) as well a lot of other functionality came from a series of about 14 blog posts examining these genomes.

I last left off with the Tara oceans taxonomic analysis [back around Thanksgiving 2017](http://ivory.idyll.org/blog/2017-taxonomic-disagreements-in-tara-mags.html), with the realization that I needed to dig some more in order to really understand what was going on.

Then, over the 2019 winter break, while updating our Genbank databases, I started playing with [making sourmash databases for the GTDB taxonomy](http://ivory.idyll.org/blog/2019-sourmash-lca-db-gtdb.html), and [while trying to understand why sourmash classifications were different from GTDB classifications](http://ivory.idyll.org/blog/2019-sourmash-lca-vs-gtdb-classify.html), I [developed a pile of scripts to dig into taxonomically divergent genomes that share sequence](http://ivory.idyll.org/blog/2020-sourmash-gtdb-oddities.html).

While corresponding with Donovan Parks about some of the Genbank oddities I found, he pointed out that this approach might be a useful technique for exploring contamination in metagenome-assembled genomes more generally.

Yep!

## The challenge: metagenome-assembled genome analysis

When people compute metagenome-assembled genomes by assembling metagenomes and then binning the resulting contigs into inferred genomes, they usually assign taxonomy to the genomes using single-copy marker genes. These same genes can also be used in the binning pipeline, and/or in an evaluation step (see e.g. [CheckM](https://genome.cshlp.org/content/early/2015/05/14/gr.186072.114)).

What has always worried me (and others!) is that this taxonomic assignment step drags with it many contigs whose only association with the single-copy marker genes is often that they were binned together. And, absent detailed inspection or knowledge of the genes in those contigs, it's been unclear how to evaluate the inclusion of those accessory contigs.

Here I should note that we + collaborators have looked into similar questions using [assembly graph proximity](https://www.biorxiv.org/content/10.1101/462788v2), which may work as well. Regardless, the question of how to QC MAGs is definitely an obsession of mine!

An angle suggested by the [above Genbank analysis](http://ivory.idyll.org/blog/2020-sourmash-gtdb-oddities.html) was to look at the accessory contigs by doing k-mer-based taxonomic analysis on them, and then see if the k-mer taxonomy agreed or disagreed with the marker-gene-based taxonomy.

There are many reasons why this might fail - the main one being that you would generally expect the DNA sequence in MAGs to be novel, followed closely by issues of genuine horizontal gene transfer, plasmids, etc. But nothing ventured, nothing gained - and I already had functioning scripts! So I gave it a try.

## Connecting everything into a workflow

In my lab, we have been using [the snakemake workflow system](https://snakemake.readthedocs.io/) a lot. It's an excellent way to tie together a bunch of disparate scripts!

So I put together a workflow, [sourmash-oddify](https://github.com/dib-lab/sourmash-oddify), to automate the analysis of genome bins. The steps are:

0. Given a collection of genome bins,
1. Assign taxonomy using [GTDB-Tk](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btz848/5626182)
2. Build a [sourmash taxonomy/LCA database](https://sourmash.readthedocs.io/en/latest/command-line.html#sourmash-lca-index) using the resulting taxonomy
3. Run the [find-oddities](https://github.com/dib-lab/sourmash-oddify/blob/master/scripts/find-oddities.py) and [find-oddities-examine](https://github.com/dib-lab/sourmash-oddify/blob/master/scripts/find-oddities-examine.py) scripts.

and voila! Sprinkle some [YAML config file magic pixie dust on top](https://github.com/dib-lab/sourmash-oddify/blob/master/conf/default.yml) and you have a configurable workflow!

Now I needed to run it on some interesting data... hmm, what collections of MAGs do I have lying around... [hey look, the Tara MAGs!](http://ivory.idyll.org/blog/2019-comparing-binnings.html)

## Running sourmash-oddify on the Tara genomes

So, I ran this on the 2,631 genomes from Tully et al., 2018, and the 957 genomes from Delmont et al., 2018. The GTDB-Tk step took about 12 hours, and the rest (computing signatures, building the LCA database, extracting oddities, aligning genomes) took about an hour. (The config file is [here](https://github.com/dib-lab/sourmash-oddify/blob/master/conf/config-tara.yml).)

The results on the Delmont data are [here](https://osf.io/xj87f/) and [here](https://osf.io/rt6qm/), and the results on the Tully data are [here](https://osf.io/xqt3n/) and [here](https://osf.io/jhq62/).

I decided to dig into two results, one from each data set. In both cases, the two genomes were classified in different superkingdoms:

```
    - TOBG_MED-875 (d__Archaea;p__Thermoplasmatota;c__Poseidoniia;o__Poseidoniales;f__Thalassoarchaeaceae;g__MGIIb-O5;;)
    - TOBG_SAT-1614 (d__Bacteria;p__Actinobacteriota;c__Acidimicrobiia;o__Microtrichales;f__TK06;g__UBA7388;s__UBA7388 sp002470695;)

    - TARA_MED_MAG_00140 (d__Archaea;p__Asgardarchaeota;c__Heimdallarchaeia;;;;;)
    - TARA_PON_MAG_00079 (d__Bacteria;p__Patescibacteria;c__CG2-30-54-11;;;;;)
```

and both pairs shared a lot of sequence between them:

```
TOBG:
cluster2.0: 208kb aln (130k 51-mers) across (root); longest contig: 115 kb
weighted percent identity across alignments: 98.1%
skipped 0 kb of alignments in 0 alignments (< 0 bp or < 95% identity)
TOBG_SAT-1614: removed 330kb of 2514kb (13%), 3 of 28 contigs
TOBG_MED-875: removed 238kb of 1305kb (18%), 2 of 55 contigs

TARA:
cluster14.0: 1497kb aln (970k 51-mers) across (root); longest contig: 11 kb
weighted percent identity across alignments: 98.9%
skipped 15 kb of alignments in 37 alignments (< 0 bp or < 95% identity)
TARA_PON_MAG_00079: removed 1788kb of 6127kb (29%), 507 of 1767 contigs
TARA_MED_MAG_00140: removed 2791kb of 6746kb (41%), 472 of 1411 contigs
```

As a control, I then took the "cleaned" genomes and re-ran the classification with GTDB-Tk. Three of the four classified as their original classification, indicating that the removed sequence didn’t contain essential marker genes (as I would have guessed). TARA_PON_MAG_00079 wasn't classified as anything by GTDB, because fewer than 10% of the markers were present. (AFAICT, GTDB-Tk doesn’t give any more details than that in its logs, so I’ll have to dig to figure out what happened.)

TOBG_MED-875 is classified as d__Archaea, while TOBG_SAT-1614 is classified as d__Bacteria. So what is the sequence that is shared? Conveniently find-oddities-examine.py outputs the contigs it removes, but what next?

I decided to run a quick analysis using Torsten Seeman's [prokka](https://github.com/tseemann/prokka), which did gene calling and gave me protein sequences in FASTA format with a minimum amount of fuss (thanks Torsten!). I took the resulting aa sequences, extracted those over 100 aa in length, shuffled them, and took the first 10. I then BLASTed [these ten sequences](https://osf.io/uds2n/) over at [NCBI BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi).

The top hit to these genes in all 10 cases is to the [TOBG_MED-875 genome in Genbank](https://www.ncbi.nlm.nih.gov/biosample/SAMN07618765), which is labeled as a *Euryarchaeota archaeon*.

However, the second and third hits are generally to a variety of Chloroflexi and/or Acidimicrobiales proteins, in the Bacterial superkingdom. This suggests that the majority of the predicted genes in the DNA shared between TOBG_MED-875 and TOBG_SAT-1614 are bacterial.

Moreover, it suggests that the inclusion of TOBG_MED-875 in Genbank may be messing up some gene taxonomies.

## Summary thoughts

I think it is safe to argue that two different binned genomes from the same metagenomic samples should not share much genomic DNA, unless they are from closely related species. (In general, I would not trust conclusions about lateral gene transfer based solely on computationally inferred genomes.)

[sourmash-oddify](https://github.com/dib-lab/sourmash-oddify) is an alpha-stage automated workflow to identify k-mers and DNA segments that don't follow the taxonomy of their containing genomes. I think using it to flag contamination in metagenome-assembled genomes is (or will be :) straightforward.

It uses the GTDB taxonomy assignment pipeline, GTDB-Tk, to generate the taxonomies, uses a Kraken-inspired approach to identify "incoherent" k-mers shared between genomes, and then runs nucmer to align the genomes.

Indications are that at least on some genomes, it correctly identifies contamination.

This is a pretty lightweight workflow, too, especially if you're already using GTDB-Tk!

## What's next?

I'm not really sure. I have a few ideas for some larger scale analyses, but I'm at the stage where I have 80% of the coding done for a full project, but it's only 20% of the work needed to bring the project to some sort of real fruition.

I think what I'd be looking to do next is to automate the Prokka steps above, and find some way of semi-automatedly reaching conclusions about who the contamination belongs to.

I'd like to work with a group or two who have a large collection of pre-publication MAGs to investigate with this approach. I think the best way to mature an approach like this is in tandem with a biology team that really cares about the specifics of the genomes and genes. [Drop me a line if you're interested!](mailto:ctbrown@ucdavis.edu)

I have other ideas and questions, too - can we use this pipeline on single-cell genomes? Should we work to ingest all genomes everywhere, and would that make this more sensitive in a useful way?

--titus
