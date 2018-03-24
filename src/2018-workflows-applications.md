Title: Pydoit, snakemake, and workflows-as-applications
Date: 2018-03-24
Category: science
Tags: workflows,pydoit,bioinformatics
Slug: 2018-workflows-applications
Authors: C. Titus Brown
Summary: Writing applications around workflow systems

Ever since [Camille Scott](https://twitter.com/camille_codon), a grad student in the lab, developed [the dammit transcriptome annotator](https://dammit.readthedocs.io/), I've been intrigued by the design decision she made.  Dammit runs a lot of other software, and Camille made the brilliant decision to avoid having dammit coordinate the execution of the dependent software itself - instead, she wrapped dammit around [doit](http://pydoit.org/), a Python workflow library in Python.

doit, like other somewhat related systems such as make, [makeflow](http://ccl.cse.nd.edu/software/makeflow/), and [snakemake](https://snakemake.readthedocs.io/), specifies workflows in a declarative manner: "to reach such and such a target result, you need these intermediate results", and so on - effectively laying out a directed acyclic graph of dependencies. As part of this, these systems coordinate the execution of the commands needed to produce all of the results.  And, because they have insight into the structure of the dependencies, they can do clever things like execute them in parallel, on multiple nodes, restarting failed jobs, etc. etc.

By using doit, Camille was able to set up the dependency graph for the final annotated transcriptome and could then delegate the execution to the pydoit library.  I myself have written many a spaghetti ball of shell commands in my time, and I was impressed with the separation of workflow logic from execution details achieved by dammit.

Now, I was all set to use doit myself for some projects, but in the meantime my lab fell under the sway of my _other_ CS grad student, [Luiz Irber](https://twitter.com/luizirber), who had been slowly converting people in the lab over to [snakemake](https://snakemake.readthedocs.io/en/stable/) without me really noticing.

It turns out that snakemake is much easier to dig into that doit, and between that and Luiz's wealth of knowledge (and inexorable persuasion), I ended up [implementing the spacegraphcats application workflow in snakemake](https://github.com/spacegraphcats/spacegraphcats/blob/master/conf/run).  And I've been pretty happy with that so far, after a few months of working with it.  (More on spacegraphcats at some future point.)

Now, my lab does a lot of workflow-y stuff, because we're a bioinformatics group and bioinformatics is all about running other people's software on other people's data (which is about as much fun as it sounds, but we get by).  So when yet another project, the [dahak metagenomics project](https://github.com/dahak-metagenomics/) decided to use snakemake to specify its workflows, [I requested](https://github.com/dahak-metagenomics/dahak/issues/61#issuecomment-373041670) a command-line interface in the same style as spacegraphcats - but with a few extra fun twists.  I wrote up a quick example in [2018-snakemake-cli](https://github.com/ctb/2018-snakemake-cli), which shows a simple way to combine workflow specification with parameter specification. From the [2018-snakemake-cli README](https://github.com/ctb/2018-snakemake-cli/blob/master/README.md), we use `run` to execute snakemake workflows:

```
./run <workflow_file> <parameters_file>
```

e.g.

```
rm -f hello.txt
./run workflow-hello params-amy
```
creates `hello.txt` with "hello amy" in it, while

```
rm -f hello.txt
./run workflow-hello params-beth
```
creates `hello.txt` with "hello beth" in it.

Here, the workflow file `workflow-hello.json` specifies the target
`hello.txt`, while the parameters file `params-amy` parameterizes
the workflow with the name "amy".

Likewise,

```
rm -f goodbye.txt
./run workflow-goodbye params-beth
```

will put `goodbye beth` in `goodbye.txt`.

All workflows use the same set of Snakemake rules in `Snakefile`.

...and this is now being implemented for dahak in [dahak-taco](https://charlesreid1.github.io/dahak-taco/).  [(Warning: the dahak repos have become self aware and are replicating.)](https://github.com/dahak-metagenomics/dahak-map)

----

Anyway, to bring this back around to the beginning:

I really like the idea of specifying workflows in a dedicated workflow engine, and then building an application around that.  It means we don't have to worry about executing commands, we can tap into a large existing support community, we can make use of more powerful abstractions in our own code, and as the workflow system expands its functionality we can take advantage of it automatically.  For example, snakemake seems to interface well with [biocontainers](https://biocontainers.pro/) and has [support for Kubernetes](https://snakemake.readthedocs.io/en/stable/executable.html#cloud-support) which are both things we intend to make use of in the future.  It also (in theory) makes the application much more extensible and hackable vs the traditional "I wrote my own shell command management foo" stuff I used to do.

--titus
