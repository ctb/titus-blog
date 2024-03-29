Title: On minimum metagenome covers, and calculating them for your own data.
Date: 2022-01-18
Category: science
Tags: sourmash, genome-grist, gather
Slug: 2022-calculating-minimum-metagenome-covers-with-genome-grist
Authors: C. Titus Brown
Summary: You, too, can run our software!

We just posted a preprint, [Lightweight compositional analysis of metagenomes with FracMinHash and minimum metagenome covers](https://www.biorxiv.org/content/10.1101/2022.01.11.475838v2), Irber et al., 2022! Some day soon I'd like to write a long blog post about how this is six years in the making, part of a major intellectual endeavor in the lab that I'm incredibly excited about, yada yada yada, but for now let me just say that I think it's got some interesting ideas in it and if you're at all interested in analyzing shotgun metagenome data you should open it in a tab somewhere; a [very readable HTML version is available for just that purpose](https://dib-lab.github.io/2020-paper-sourmash-gather/).

## There is a super cool figure. You should check it out!

But what I'm really here to say is this: you might see a super cool figure in the paper that looks like this:

![figure comparing mapping to k-mer hash matching](images/2022-calculating-gather-vs-mapping.png)

That figure is super cool in part because it tells you what microbial genomes from Genbank are present in your shotgun metagenome.

And it's even _super cooler_ because our software figures out which genomes are present **automatically**, and can use all of Genbank microbial to do so!<sup>1</sup>

We're not talking taxonomic information here, BTW, where you then have to go pick a representative genome after doing an analysis that only gives you vague species-level designations. Nope, we're talking cold, hard DNA-sequence-on-the-table, genome-files-in-a-directory, automatically retrieved and analyzed for you. With mapping and everything.<sup>2</sup>

(Taxonomy *is* available, if you're interested in such. You can use GTDB or NCBI taxonomy as you wish. But you can just have the genomes, too!)

## Where can I get this magickal software?

What, you say? How is this magic possible!?

We wrote some software! And workflows! It's called genome-grist and it's [available](https://github.com/dib-lab/genome-grist) NOW NOW NOW for the LOW LOW COST of FREE!

And (I can't stress enough how excited I am about this) [it's got documentation, too!](https://dib-lab.github.io/genome-grist/)

And, for an _unlimited time only_, you can even integrate [**your own private, unpublished, cherished and hoarded genome sequences!**](https://dib-lab.github.io/genome-grist/configuring/#preparing-information-on-local-genomes)<sup>3</sup>

&lt;ahem&gt;
    
Anyhoo. Feedback is welcome.

And yes, this is actually the software that was used to calculate the figures in the paper about the sourmash software referenced at the top. Yes, we are writing software so that we can generate figures for papers about other software. No, this will never end.

--titus

1: terms and conditions may apply: right now we can only give you Genbank as of July 2020. Sorry. We're working on it.

2: terms and conditions may apply: right now this really only works well with paired-end Illumina metagenomes.

3: And, like, your own private taxonomic classifications for your genomes, if you're into that kind of thing.
