Title: Some snakemake hacks for dealing with large collections of files
Date: 2020-03-09
Category: science
Tags: snakemake, python
Slug: 2020-snakemake-hacks-collections-files
Authors: C. Titus Brown and N. Tessa Pierce and Taylor Reiter
Summary: snakemake4life

This winter quarter I taught my usual graduate-level introductory
bioinformatics lab at UC Davis, GGG 201(b), for the fourth time. The
course lectures are given by Megan Dennis and Fereydoun Hormozdiari,
and I do a largely separate lab that aims to teach the basics of
practical variant calling, de novo assembly, and RNAseq differential
expression.

I also co-developed and co-taught a new course, GGG 298 / Tools for
Data Intensive Research, with Shannon Joslin, a graduate student here
in Genetics & Genomics who (among other things) took GGG 201(b) the
first time I offered it. GGG 298 is a series of ten half-day workshops
where we teach shell, conda, snakemake, git, RMarkdown, etc - you can
see
[the syllabus for GGG 298 here](https://github.com/ngs-docs/2020-GGG298/).

This time around, I did a complete redesign of the
[GGG 201(b) lab (see syllabus)](https://github.com/ngs-docs/2020-GGG201b-lab)
to focus on using
[snakemake workflows](http://snakemake.readthedocs.io/en/stable/).

I'm 80% happy with how it went - there's some overall fine tuning to
be done, and snakemake has some corners that need more explaining than
other corners, but I think the basic concepts got through to a lot of
the students. I also think I'm finally teaching people something they
_really_ need to know, which is how to build, automate, place controls
on, and execute complex bioinformatics workflows.

I was traveling the week before last, so I asked Taylor Reiter and
Tessa Pierce to do the first RNAseq lecture for the class (week 8!) As
part of their
[brilliant RNAseq materials](https://github.com/ngs-docs/2020-ggg-201b-rnaseq)
for the class (snakemake! salmon! tximeta! DESeq2! RMarkdown!), Tessa
used a cute trick in the Snakefile that I hadn't seen before. It's
"obvious" if you're a Python+snakemake expert, but many people aren't,
and in any case it's always nice to share, right??

Below, I take the opportunity to share several solutions for loading
sample names into the Snakefile.

(These are fairly boilerplate examples that you can use in your own
code with little modification, too!)

## Cute snakemake trick #1: dictionaries for downloads

The following code snippet is a nice, simple Pythonic way to download
a bunch of files from Web URLs.

```python
# list sample names & download URLs.
sample_links = {"ERR458493": "https://osf.io/5daup/download",
                "ERR458494":"https://osf.io/8rvh5/download",
                 "ERR458495":"https://osf.io/2wvn3/download",
                 "ERR458500":"https://osf.io/xju4a/download",
                 "ERR458501": "https://osf.io/nmqe6/download",
                 "ERR458502": "https://osf.io/qfsze/download"}

# the sample names are dictionary keys in sample_links. extract them to a list we can use below
SAMPLES=sample_links.keys()

# download yeast rna-seq data from Schurch et al, 2016 study
rule download_all:
    input:
        expand("rnaseq/raw_data/{sample}.fq.gz", sample=SAMPLES)

# rule to download each individual file specified in sample_links
rule download_reads:
    output: "rnaseq/raw_data/{sample}.fq.gz" 
    params:
        # dynamically generate the download link directly from the dictionary
        download_link = lambda wildcards: sample_links[wildcards.sample]
    shell: """
        curl -L {params.download_link} -o {output}
        """
```

## Cute snakemake trick #2: loading filenames from the current directory.

(**I don't recommend this approach.** Read on.)

One of the most common questions I've been asked in the last few weeks
is how to avoid typing all of the sample names into the
Snakefile. (This can matter a lot when you have hundreds of samples!)

After you download the files above, you can get a list of the
downloaded files like so:

```python
sample_ids = glob_wildcards("rnaseq/raw_data/{sample}.fq.gz")
```

Now, `sample_ids` is a Python list that behaves just like `SAMPLES`,
and it can be used with `expand`.

Note, for this example, `SAMPLES` and `sample_ids` are going to
contain the same list of files. The difference is that `sample_ids`
are loaded from the directory listing, while `SAMPLES` has to be
written out in the Snakefile somehow (here, in `sample_links`).

**Why don't I recommend this approach?** You can only use this
approach if the files already exist in the directory. That's fine -
often you don't want to copy them in or download them dynamically! -
but it sets up a particular kind of potential error. If you load the
list of samples from your working directory, and you accidentally
delete one of the sample files, you'll omit it from your workflow
without knowing.

It's much better to *independently* specify the list of files, so that
if you accidentally delete one, snakemake will complain. That's where
the next trick comes in.

As a bonus, the next approach lets you specify metadata in the
spreadsheet, which is important!

## Cute snakemake trick #3: loading a list of sample names from a spreadsheet.

This is taken from a really nice, clean
[example RNAseq workflow that uses STAR and DESeq2](https://github.com/snakemake-workflows/rna-seq-star-deseq2),
written by Johannes Köster, Sebastian Schmeier, and Jose Maturana.

Here,
[the Snakefile](https://github.com/snakemake-workflows/rna-seq-star-deseq2/blob/master/Snakefile)
loads sample names from a tab-separated values spreadsheet using
pandas; a simplified version of the code follows:

```python
import pandas as pd

samples_df = pd.read_table('samples.tsv').set_index("sample", drop=False)
sample_names = list(samples_df['sample'])
```

Here, `sample_names` is the same as `SAMPLES` and `sample_ids`, above - a list that you can use in `expand` and so on. The difference here is that `samples_df` is a [Pandas dataframe](https://www.geeksforgeeks.org/python-pandas-dataframe/) that contains other information, such as sample metadata; and it's loaded from a TSV file that can be created, visualized, and edited using spreadsheet software.

## Cute snakemake trick #4: loading a list of download links from a spreadsheet.

The TSV approach is particularly useful for downloading files or
moving files, as the download links or file paths can be included in
the spreadsheet, rather than at the top of the Snakefile (as they were
in cute trick #1).

Considering the same yeast RNAseq data as the first example and a TSV
file containing the sample names and download links, samples can be
downloaded like so:

```python
import pandas as pd

samples_df = pd.read_table('samples.tsv').set_index("sample", drop=False)
SAMPLES = list(samples_df['sample'])

# download yeast rna-seq data from Schurch et al, 2016 study
rule download_all:
    input:
        expand("rnaseq/raw_data/{sample}.fq.gz", sample=SAMPLES)

# rule to download each individual file specified in samples_df
rule download_reads:
    output: "rnaseq/raw_data/{sample}.fq.gz" 
    params:
        # dynamically grab the download link from the "dl_link" column in the samples data frame
        download_link = lambda wildcards: samples_df.loc[wildcards.sample, "dl_link"]
    shell: """
        curl -L {params.download_link} -o {output}
        """

```

Enjoy! And comments are welcome!

--titus (and Tessa and Taylor!)

