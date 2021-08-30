Title: Using snakemake to do simple wildcard operations on many, many, many files
Date: 2021-08-30
Category: science
Tags: snakemake, python
Slug: 2021-snakemake-simple-operations
Authors: C. Titus Brown
Summary: snakemake is awesome

I recently co-taught [another snakemake lesson](https://ngs-docs.github.io/2021-august-remote-computing/automating-your-analyses-with-the-snakemake-workflow-system.html) (with Dr. Abhijna Parigi), and was reminded of one of my favorite off-label uses of snakemake: replacing complicated bash `for` loops with simple and robust snakemake workflows.

## An example

As a bioinformatics researcher, I frequently need to do simple operations to many files. As part of this, I usually want to change the filename to represent the change in file content.

For example, let's suppose I have a bunch of FASTQ files (say, the ones [here](https://github.com/ngs-docs/2021-remote-computing-binder/tree/latest/data/MiSeq)), and I want to subset them to the first 400 lines. The filenames all have the form `NAME.fastq`, and I want to add `.subset.fastq` to the end of the subset filenames to distinguish them. 
(See [this shell scripting lesson](https://ngs-docs.github.io/2021-august-remote-computing/automating-your-analyses-and-executing-long-running-analyses-on-remote-computers.html#subsetting) for more background and motivation for this particular operation.)

### Using `bash`, round 1

For many years I did this with bash `for` loops. The following code works, assuming the original fastq files are in a `data/` subdirectory:

```
mkdir subset
for i in data/*.fastq
do
    head -400 $i > subset/$(basename $i).subset.fastq
done
```


Starting from a bunch of files,

```
>data/F3D0_S188_L001_R1_001.fastq
>data/F3D0_S188_L001_R2_001.fastq
>...
```

this loop will produce

```
>subset/F3D0_S188_L001_R1_001.fastq.subset.fastq
>subset/F3D0_S188_L001_R2_001.fastq.subset.fastq
```

### Improving the bash solution

The output filenames are kind of ugly, because `fastq` is repeated. That's just because bash makes it so easy to append to filenames - we can fix this by adding `.fastq` into the `$(basename ...)` call:

```
mkdir subset2
for i in data/*.fastq
do
    head -400 $i > subset2/$(basename $i .fastq).subset.fastq
done
```

So... not difficult to read, and fairly straightforward. Why would I use anything else?

## Using snakemake instead

tl;dr The bash code above is brittle when I modify it; it's not robust enough for important work.

In my (extensive &lt;sigh&gt;) experience, the above approach fails some reasonable percent of the time. Usually I get it right the first time I write it, and then I modify and tweak it, and chaos ensues because I omit something in the for loop.

So a year or two ago, I decided to try out snakemake for one of these operations.

Here's the contents of a file named `Snakefile.subset`, which does the same thing as the for loop above -

```
# pull in all files with .fastq on the end in the #data
FILES = glob_wildcards('data/{name}.fastq')

# extract the {name} values into a list
NAMES = FILES.name

rule all:
    input:
        # use the extracted name values to build new filenames
        expand("subset3/{name}.subset.fastq", name=NAMES)

rule subset:
    input:
        "data/{n}.fastq"
    output:
        "subset3/{n}.subset.fastq"
    shell: """
        head -400 {input} > {output}
    """
```

and you can run it with `snakemake -s Snakefile.subset -j 1`.

With this Snakefile, snakemake pulls in all files that match the glob pattern and extracts their names, and then constructs a set of "targets" in rule `all` that it must create. The `subset` rule specifies how to build targets of that name.

## Why I like snakemake more than bash for this

So why do I like snakemake more? A few reasons that I think are intrinsic to snakemake vs bash -

* snakemake fails if something is wonky about the filenames, _before_ doing anything!
* if any of the operations fail, snakemake stops and alerts me by default!
* I can do the operations in parallel by specifying e.g. `snakemake -j 4` to use 4 cores.
* the templating language for using `{...}` is nice, simple, and Python-standard (see [this blog post on f-strings](https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python) and also the [the templating minilanguage ref](https://docs.python.org/3/library/string.html#formatspec)).
* as the operations get more complicated, snakemake doesn't need to get more complicated, while the bash solution tends to complexify into illegibility...
* I think the snakemake solution is easier to understand and modify!

Above all, the overall structure of snakemake is _declarative_ rather than _procedural_. We declare what we want the result to look like, and snakemake uses the available rules to create the overall set of steps that must be executed and Makes It Happen. This is what makes the error checking and parallelization possible.

Another "feature" of this solution is that there are more comments because I comment Snakefiles more than bash scripts. This is probably a me-problem that is caused by snakemake _forcing_ me to edit a file :).

I haven't reused Snakefiles that much, but I think you can reuse Snakefiles fairly easily - see next section.

Are there any downsides? The main one is that the snakemake solution feels more heavyweight to me - it involves creating a file, getting the spacing/indentation right, etc. etc. So I still don't use it as much as I probably should.

Thoughts welcome!

--titus

## Appendix: A more reusable Snakefile

Below is a Snakefile that's a bit more reusable for situations where your input and output directories don't match the names I used above - you can override PREFIX and OUTPUT by running `snakemake -C prefix=PREFIX output=OUTPUT`.

(I don't really like the syntax of using f-strings here, but it's cleaner than anything else I've found. Suggestions welcome.)

```
# pull in all files with .fastq on the end in the 'data' directory.             
PREFIX = config.get('prefix', 'data')
print(f"looking for FASTQ files under '{PREFIX}'/")

OUTPUT = config.get('output', 'subset5')
print(f"subset results will go under '{OUTPUT}'/")

FILES = glob_wildcards(f'{PREFIX}/{{name}}.fastq')

# extract the {name} values into a list                                         
NAMES = FILES.name

# request the output files                                                      
rule all:
    input:
        # use the extracted 'name' values to build new filenames                
        expand("{output}/{name}.subset.fastq", output=OUTPUT, name=NAMES)

# actually do the subsetting                                                    
rule subset_wc:
    input:
        f"{PREFIX}/{{n}}.fastq"
    output:
        "{output}/{n}.subset.fastq"
    shell: """                                                                  
        head -400 {input} > {output}                                            
    """
```

