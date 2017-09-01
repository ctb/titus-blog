Title: Is your bioinformatics analysis package Big Data ready?
Date: 2017-09-01
Category: science
Tags: big data, bioinformatics
Slug: 2017-big-data-ready
Authors: C. Titus Brown
Summary: Plan for incremental data updates when building your tools.

(Apologies for the Big Data buzzword, but it actually fits!)

I find it increasingly frustrating to use a broad swath of bioinformatics tools (and given how inherently frustrating the bioinformatics ecosystem is already, that's saying something!) My bugaboo this time is bioinformatics "prepared databases" - but not [multiple installs of databases](https://twitter.com/BaCh_mira/status/902509776810201088) or [their size](https://twitter.com/ctitusbrown/status/902510783052922881).  Rather, I'm frustrated by the *cost of building them*.  Similarly, I'm frustrated at how many analysis pipelines require you to start from the very beginning if you add data to your experiment or sample design.

We are increasingly living in a world of [what I call "infinite  data"](https://osf.io/b5hmq/), where, for many purposes, *getting* the data is probably the least of your problems - or, at least, the time and cost of generating sequence data is dwarfed by sample acquisition, data analysis, hypothesis generation/testing, and paper writing.

What this means for databases is that no sooner does someone [publish a massive amount of data from a global ocean survey (Tara Oceans, Sunagawa et al. 2015)](http://ocean-microbiome.embl.de/companion.html) than does someone else [analyze the data in a new and interesting way (Tully et al., 2017)](http://www.biorxiv.org/content/early/2017/07/13/162503) and produce data sets that I, at least, *really* want to include in my own reference data sets for environmental metagenome data. (See [Hug et al., 2016](https://www.nature.com/articles/nmicrobiol201648#methods) and [Stewart et al., 2017](http://www.biorxiv.org/content/early/2017/07/12/162578) for even more such data sets.)

Unfortunately, most bioinformatics tools don't let me easily update my databases or analyses with information from new references or new data.  I'm going to pick on taxonomic approaches first because [they're on my mind](http://ivory.idyll.org/blog/2017-something-about-kmers.html) but this applies to any number of software packages commonly used in bioinformatics.

Let's take [Kraken](http://ccb.jhu.edu/software/kraken/MANUAL.html), an awesome piece of software that founded a whole class of approaches.  The Kraken database and toolset is constructed in such a way that I cannot easily do two specific things:

* add just one reference genome to it;
* ask Kraken to search two different reference databases and report integrated results;

Similarly, none of the assemblers I commonly use lets me me add just
one more sequencing data set into the assembly - I have to recalculate
the entire assembly from scratch, after adding the additional data
set. Annotation approaches don't let me update the database with new
sequences and then run an abbreviated analysis that improves
annotations. And etc.

## What's the problem?

There are two classes of problems underneath this - one is the pragmatic engineering issue. For example, with Kraken, it is theoretically straightforward, but tricky from an engineering perspective, to support the addition of a single genome into the database; "all" you need to do is update the least-common-ancestor assignments in the database for each k-mer in your new genome.  Likewise, the Kraken approach should be able to support search *across* databases, where you give it two different databases and it combines them in the analysis - but it doesn't seem to.  And, last but not least, Kraken could in theory support taking an existing classified set of reads and "updating" their classification from a new database, although in practice there's not much point in doing this because Kraken's already pretty fast.

The second kind of challenge is theoretical. We don't really have the right algorithmic approaches to assembly to support fully online assembly in all its glory, although you could imagine doing things like error trimming in an incremental way ([I mean, just imagine...](https://peerj.com/preprints/890/)) and saving that for later re-use.  But we generally don't save the full information needed to add a single sequence and then quickly output an updated assembly. 

And that last statement highlights an important question - for which approaches do we have the theory *and* the engineering to *quickly* update an analysis with a new reference database, or a new read data set?  I can guess but I don't know.

Note, I'm explicitly not interested in heuristic approaches where you e.g. map the reads to the assembly to see if there's new information - I'm talking about using algorithms and data structures and software where you get identical results from doing `analysis(n + m)` and `analysis(n) + analysis(m)`.

Even if we do have this theoretical ability, it's not clear that many tools support it, or at least they don't seem to advertise that support.  This also seems like an area where additional theoretical development (new data structures! better algorithms!) would be useful.

I'm curious if I'm missing something; have I just not noticed that this is straightforward with many tools? It seems so useful...

Anyway, I'm going to make a conscious effort to support this in our tools (which we sort of already were planning, but now can be more explicit about).

--titus

p.s. This post partly inspired by [Meren](https://twitter.com/merenbey/), who [asked for this with sourmash databases](https://github.com/dib-lab/sourmash/issues/229) - thanks!
