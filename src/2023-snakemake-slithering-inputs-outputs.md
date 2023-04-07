Title: snakemake for doing bioinformatics - inputs and outputs and more!
Date: 2023-04-07
Category: science
Tags: snakemake, slithering
Slug: 2023-snakemake-slithering-input-outputs
Authors: C. Titus Brown
Summary: Slithering your way into bioinformatics with snakemake - inputs and outputs and more!

# `input:` and `output:` blocks

As we saw [before](http://ivory.idyll.org/blog/2023-snakemake-slithering-section-1.html), snakemake will automatically
"chain" rules by connecting inputs to outputs. That is, snakemake
will figure out _what to run_ in order to produce the desired output,
even if it takes many steps.

We also saw that snakemake will fill
in `{input}` and `{output}` in the shell command based on the contents
of the `input:` and `output:` blocks. This becomes even more useful
when using wildcards to generalize rules, where wildcard values are properly
substituted into the `{input}` and `{output}` values.

Input and output blocks are key components of snakemake workflows.
Below, we will discuss the use of input and output blocks
a bit more comprehensively.

## Providing inputs and outputs

As we saw previously, snakemake will happily take multiple input and
output values via comma-separated lists and substitute them into strings
in shell blocks.

```python
rule example:
   input:
       "file1.txt",
       "file2.txt",
   output:
       "output file1.txt",
       "output file2.txt",
   shell: """
       echo {input:q}
       echo {output:q}
       touch {output:q}
   """
```

When these are substituted into shell commands with `{input}` and
`{output}` they will be turned into space-separated ordered lists:
e.g. the above shell command will print out first `file1.txt
file2.txt` and then `output file1.txt output file2.txt` before using `touch` to
create the empty output files.

In this example we are also asking snakemake to quote filenames for
the shell command using `:q` - this means that if there are spaces,
characters like single or double quotation marks, or other characters
with special meaning they will be properly escaped using
[Python's shlex.quote function](https://docs.python.org/3/library/shlex.html#shlex.quote).
For example, here both output files contain a space, and so `touch
{output}` would create three files -- `output`, `file1.txt`, and
`file2.txt` -- rather than the correct two files, `output file1.txt`
and `output file2.txt`.

**Quoting filenames with `{...:q}` should always be used for anything
executed in a shell block** - it does no harm and it can prevent
serious bugs!

### Digression: Where can we (and should we) put commas?

In the above code example, you will notice that `"file2.txt"` and
`"output file2.txt"` have commas after them:

```python
rule example:
   input:
       "file1.txt",
       "file2.txt",
   output:
       "output file1.txt",
       "output file2.txt",
   shell: """
       echo {input:q}
       echo {output:q}
       touch {output:q}
   """
```

Are these required? **No.** The above code is equivalent to:

```python
rule example:
   input:
       "file1.txt",
       "file2.txt"
   output:
       "output file1.txt",
       "output file2.txt"
   shell: """
       echo {input:q}
       echo {output:q}
       touch {output:q}
   """
```

where there are no commas after the last line in input and output.

The general rule is this: you need internal commas to separate items
in the list, because otherwise strings will be concatenated to each
other - i.e. `"file1.txt" "file2.txt"` will become `"file1.txtfile2.txt"`,
even if there's a newline between them! But a comma trailing after the
last filename is optional (and ignored).

Why!?  These are _Python tuples_ and you can add a trailing comma if
you like: `a, b, c,` is equivalent to `a, b, c`.

So why do we add a trailing comma?! I suggest using trailing commas
because it makes it easy to add a new input or output without
forgetting to add a comma, and this is a mistake I make frequently!
This is a (small and simple but still useful) example of _defensive
programming_, where we can use optional syntax rules to head off common
mistakes.

## Inputs and outputs are _ordered lists_

We can also refer to individual input and output entries by using
square brackets to index them as lists, starting with position 0:

```python
rule example:
   ...
   shell: """
       echo first input is {input[0]:q}
       echo second input is {input[1]:q}
       echo first output is {output[0]:q}
       echo second output is {output[1]:q}
       touch {output}
   """
```

However, **we don't recommend this** because it's fragile. If you
change the order of the inputs and outputs, or add new inputs, you
have to go through and adjust the indices to match.  Relying on the
number and position of indices in a list is error prone and will make
your Snakefile harder to change later on!

## Using keywords for input and output files

You can also name specific inputs and outputs using the _keyword_
syntax, and then refer to those using `input.` and `output.` prefixes.
The following Snakefile rule does this:
```python
rule example:
   input:
       a="file1.txt",
       b="file2.txt",
   output:
       a="output file1.txt",
       c="output file2.txt"
   shell: """
       echo first input is {input.a:q}
       echo second input is {input.b:q}
       echo first output is {output.a:q}
       echo second output is {output.c:q}
       touch {output:q}
   """

```

Here, `a` and `b` in the input block, and `a` and `c` in the output block,
are keyword names for the input and output files; in the shell command,
they can be referred to with `{input.a}`, `{input.b}`, `{output.a}`, and
`{output.c}` respectively. Any valid variable name can be used, and the
same name can be used in the input and output blocks without collision,
as with `input.a` and `output.a`, above, which are distinct values.

**This is our recommended way of referring to specific input and
output files.** It is clearer to read, robust to rearrangements or
additions, and (perhaps most importantly) can help guide the reader
(including "future you") to the _purpose_ of each input and output.

If you use the wrong keyword names in your shell code, you'll get an
error message. For example, this code:
```python
rule example:
   input:
       a="file1.txt",
   output:
       a="output file1.txt",
   shell: """
       echo first input is {input.z:q}
   """
```
gives this error message:
```
AttributeError: 'InputFiles' object has no attribute 'z', when formatting the following:

       echo first input is {input.z:q}
   
```

## Example: writing a flexible command line

One example where it's particularly useful to be able to refer to
specific inputs is when running programs on files where the input
filenames need to be specified as optional arguments.  One such
program is the `megahit` assembler when it runs on paired-end input
reads. Consider the following Snakefile:

```python
rule all:
    input:
        "assembly_out"

rule assemble:
    input:
        R1="sample_R1.fastq.gz",
        R2="sample_R2.fastq.gz",
    output:
        directory("assembly_out")
    shell: """
        megahit -1 {input.R1} -2 {input.R2} -o {output}
    """
```

In the shell command here, we need to supply the input reads as two
separate files, with `-1` before one and `-2` before the second. As a
bonus the resulting shell command is very readable!

## Input functions and more advanced features

There are a number of more advanced uses of input and output that rely
on Python programming - for example, one can define a Python function
that is called to _generate_ a value dynamically, as below -

```python
def multiply_by_5(w):
    return f"file{int(w.val) * 5}.txt"
    
    
rule make_file:
    input:
        # look for input file{val*5}.txt if asked to create output{val}.txt
        filename=multiply_by_5,
    output:
        "output{val}.txt"
    shell: """
        cp {input} {output:q}
    """
```

When asked to create `output5.txt`, this rule will look for
`file25.txt` as an input.

Since this functionality relies on knowledge of
[wildcards](http://ivory.idyll.org/blog/2023-snakemake-slithering-wildcards.html) as well as some knowledge of Python, it's too advanced
to talk about here. More on that later!

## References and Links

* [Snakemake manual section on rules](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#snakefiles-and-rules)

# `params:` blocks and `{params}`

As we saw above, input and output blocks are key to the way snakemake works: they let
snakemake automatically connect rules based on the inputs necessary
to create the desired output. However, input and output blocks are
limited in certain ways: most specifically, every entry in both input
and output blocks _must_ be a filename.  And, because of the way
snakemake works, the filenames specified in the input and output
blocks must exist in order for the workflow to proceed past that
rule.

Frequently, shell commands need to take parameters other than
filenames, and these parameters may be values that can or should be
calculated by snakemake.  Therefore, snakemake also supports a
`params:` block that can be used to provide parameter strings that are _not_
filenames in the shell block. As
you'll see below, these can be used for a variety of purposes,
including user-configurable parameters as well as parameters that can
be calculated automatically by Python code.

## A simple example of a params block

Consider:
```python
rule use_params:
    params:
        val = 5
    output: "output.txt"
    shell: """
        echo {params.val} > {output}
    """
```

Here, the value `5` is assigned to the name `val` in the `params:` block,
and is then available under the name `{params.val}` in the `shell:` block.
This is analogous to using keywords in input and output blocks, but unlike in
input and output blocks, keywords _must_ be used in params blocks.

In this example, there's no gain in functionality, but there is some
gain in readability: the syntax makes it clear that `val` is a tunable
parameter that can be modified without understanding the details of
the shell block.

## Params blocks have access to wildcards

Just like the `input:` and `output:` blocks, wildcard values are
directly available in `params:` blocks without using the `wildcards`
prefix; for example, this means that you can use them in strings with
the standard [string formatting operations](https://docs.python.org/3/library/string.html#formatspec).

This is useful when a shell command needs to use something other than
the filename - for example, the `bowtie` read alignment software takes
the _prefix_ of the output SAM file via `-S`, which means you cannot
name the file correctly with `bowtie ... -S {output}`.  Instead, you
could use `{params.prefix}` like so:
```python
rule all:
    input:
        "reads.sam"

rule use_params:
    input: "{prefix}.fq",
    output: "{prefix}.sam",
    params:
        prefix = "{prefix}"
    shell: """
        bowtie index -U {input} -S {params.prefix}
    """
```
If you were to use `-S {output}` here, you would end up producing a file
`reads.sam.sam`!

## Links and references:

* Snakemake docs: [non-file parameters for rules](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#non-file-parameters-for-rules)

# Using `expand` to generate filenames

[Snakemake wildcards](http://ivory.idyll.org/blog/2023-snakemake-slithering-wildcards.html) make it easy to apply rules to
many files, but also create a new challenge: how do you generate all the
filenames you want?

As an example of this challenge, consider the list of genomes needed
for rule `compare_genomes` from [before](http://ivory.idyll.org/blog/2023-snakemake-slithering-section-2.html) -

```python
rule compare_genomes:
    input:
        "GCF_000017325.1.fna.gz.sig",
        "GCF_000020225.1.fna.gz.sig",
        "GCF_000021665.1.fna.gz.sig",
        "GCF_008423265.1.fna.gz.sig",
```

This list is critical because it specifies the sketches to be created
by the wildcard rule. However, writing this list out is annoying and
error prone, because parts of every filename are identical and
repeated.

Even worse, if you needed to use this list in multiple places, or
produce slightly different filenames with the same accessions, that
will be error prone: you are likely to want to add, remove, or edit
elements of the list, and you will need to change it in multiple
places.

[Previously](http://ivory.idyll.org/blog/2023-snakemake-slithering-section-2.html), we showed how to change this to a list of the
accessions at the top of the Snakefile and then used a function called
`expand` to generate the list:
```python
ACCESSIONS = ["GCF_000017325.1",
              "GCF_000020225.1",
              "GCF_000021665.1",
              "GCF_008423265.1"]

#...

rule compare_genomes:
    input:
        expand("{acc}.fna.gz.sig", acc=ACCESSIONS),

```

Using `expand` to generate lists of filenames is a common pattern in
Snakefiles, and we'll explore it more below!

## Using `expand` with a single pattern and one list of values

In the example above, we provide a single pattern, `{acc}.fna.gz.sig`,
and ask `expand` to resolve it into many filenames by filling in values for
the field name `acc` from each element in `ACCESSIONS`. (You may recognize
the keyword syntax for specifying values, `acc=ACCESSIONS`, from
input and output blocks, above!

The result of `expand('{acc}.fna.gz.sig', acc=...)` here is
_identical_ to writing out the four filenames in long form:
```
"GCF_000017325.1.fna.gz.sig",
"GCF_000020225.1.fna.gz.sig",
"GCF_000021665.1.fna.gz.sig",
"GCF_008423265.1.fna.gz.sig"
```
That is, `expand` doesn't do any special wildcard matching or pattern
inference - it just fills in the values and returns the resulting list.

Here, `ACCESSIONS` can be any Python _iterable_ - for example a list, a tuple, 
or a dictionary.

## Using `expand` with multiple lists of values

You can also use `expand` with multiple field names. Consider:
```
expand('{acc}.fna.{extension}`, acc=ACCESSIONS, extension=['.gz.sig', .gz'])
```
This will produce the following eight filenames:
```
"GCF_000017325.1.fna.gz.sig",
"GCF_000017325.1.fna.gz",
"GCF_000020225.1.fna.gz.sig",
"GCF_000020225.1.fna.gz",
"GCF_000021665.1.fna.gz.sig",
"GCF_000021665.1.fna.gz",
"GCF_008423265.1.fna.gz.sig",
"GCF_008423265.1.fna.gz"
```
by substituting _all possible_ combinations of `acc` and `extension` into
the provided pattern.

## Generating _all_ combinations vs _pairwise_ combinations

As we saw above, with multiple patterns, `expand` will generate all
possible combinations: that is,
```python
X = [1, 2, 3]
Y = ['a', 'b', 'c']

rule all:
   input:
      expand('{x}.by.{y}', x=X, y=Y)
```
will generate 9 filenames: `1.by.a`, `1.by.b`, `1.by.c`, `2.by.a`, etc.
And if you added a third pattern to the `expand` string, `expand` would
also add that into the combinations!

So what's going on here?

By default, expand does an all-by-all expansion containing all
possible combinations. (This is sometimes
called a Cartesian product, a cross-product, or an outer join.)

But you don't always want that. How can we change this behavior?

The `expand` function takes an optional second argument, the
combinator, which tells `expand` how to combine the lists of values
the come after. By default `expand` uses a Python function called
`itertools.product`, which creates all possible combinations, but you
can give it other functions.

In particular, you can tell `expand` to create pairwise combinations
by using `zip` instead - something we did in one of the
[wildcard examples](http://ivory.idyll.org/blog/2023-snakemake-slithering-wildcards.html).

Here's an example:

```python
X = [1, 2, 3]
Y = ['a', 'b', 'c']

rule all:
   input:
      expand('{x}.by.{y}', zip, x=X, y=Y)
```
which will now generate only three filenames: `1.by.a`, `2.by.b`, and `3.by.c`.

The big caveat here is that `zip` will create an output list the length
of the shortest input list - so if you give it one list of three elements,
and one list of two elements, it will only use two elements from the first
list.

For example, in the `expand` in this `Snakefile`,
```python
X = [1, 2, 3]
Y = ['a', 'b']

rule all_zip_short:
   input:
      expand('{x}.by.{y}', zip, x=X, y=Y)
```
only `1.by.a` and `2.by.b` will be generated, as there is no partner
for `3` in the second list.

For more information see the [snakemake documentation on using zip instead of product](https://snakemake.readthedocs.io/en/stable/project_info/faq.html#i-don-t-want-expand-to-use-the-product-of-every-wildcard-what-can-i-do).

## Getting a list of identifiers to use in `expand`

The `expand` function provides an effective solution when you have
lists of identifiers that you use multiple times in a workflow - a common
pattern in bioinformatics!  Writing these lists out in a Snakefile
(as we do in the above examples) is not always practical, however;
you may have dozens to hundreds of identifiers!

Lists of identifiers can be loaded from _other_ files in a variety of
ways, and they can also be generated from the set of actual files in
a directory using `glob_wildcards`.

## Examples of loading lists of accessions from files or directories

### Loading a list of accessions from a text file

If you have a simple list of accessions in a text file
`accessions.txt`, like so:

File `accessions.txt`:
```
GCF_000017325.1
GCF_000020225.1
GCF_000021665.1
GCF_008423265.1

```

then the following code will load each line in the text file in as a separate
ID.

Snakefile to load `accessions.txt`:
```python
with open('accessions.txt', 'rt') as fp:
    ACCESSIONS = fp.readlines()
    ACCESSIONS = [ line.strip() for line in ACCESSIONS ]
    
print(f'ACCESSIONS is a Python list of length {len(ACCESSIONS)}')
print(ACCESSIONS)

rule all:
    input:
        expand("{acc}.sig", acc=ACCESSIONS)

rule sketch_genome:
    input:
        "genomes/{accession}.fna.gz",
    output:
        "{accession}.sig",
    shell: """
        sourmash sketch dna -p k=31 {input} --name-from-first -o {output}
    """

```

and build sourmash signatures for each accession.

### Loading a specific column from a CSV file

If instead of a text file you have a CSV file with multiple columns,
and the IDs to load are all in one column, you can use the Python
[pandas library](https://pandas.pydata.org/) to read in the CSV. In
the code below, `pandas.read_csv` loads the CSV into a pandas
DataFrame object, and then we select the `accession` column and use
that as an iterable.

File `accessions.csv`:
```csv
accession,information
GCF_000017325.1,genome 1
GCF_000020225.1,genome 2
GCF_000021665.1,genome 3
GCF_008423265.1,genome 4

```

Snakefile to load `accessions.csv`:
```python
import pandas

CSV_DATAFRAME = pandas.read_csv('accessions.csv')
ACCESSIONS = CSV_DATAFRAME['accession']

print(f'ACCESSIONS is a pandas Series of length {len(ACCESSIONS)}')
print(ACCESSIONS)

rule all:
    input:
        expand("{acc}.sig", acc=ACCESSIONS)

rule sketch_genome:
    input:
        "genomes/{accession}.fna.gz",
    output:
        "{accession}.sig",
    shell: """
        sourmash sketch dna -p k=31 {input} --name-from-first -o {output}
    """

```

### Loading from the config file

Snakemake also supports the use of configuration files, where the
snakefile supplies the name of the a default config file (which can in
turn be overridden on the command line.)

A config file can also be a good place to put accessions. Consider:

```yaml
accessions:
- GCF_000017325.1
- GCF_000020225.1
- GCF_000021665.1
- GCF_008423265.1

```

which is used by the following Snakefile.

Snakefile to load accessions from `config.yml`:
```python
configfile: "config.yml"

ACCESSIONS = config['accessions']
    
print(f'ACCESSIONS is a Python list of length {len(ACCESSIONS)}')
print(ACCESSIONS)

rule all:
    input:
        expand("{acc}.sig", acc=ACCESSIONS)

rule sketch_genome:
    input:
        "genomes/{accession}.fna.gz",
    output:
        "{accession}.sig",
    shell: """
        sourmash sketch dna -p k=31 {input} --name-from-first -o {output}
    """

```

Here, `config.yml` is a [YAML file](https://en.wikipedia.org/wiki/YAML),
which is a human-readable format that can also be read by computers.
We will talk about config files later!

### Using `glob_wildcards` to load IDs or accessions from a set of files

We introduced the `glob_wildcards` command briefly in the
[chapter on wildcards](https://ivory.idyll.org/blog/2023-snakemake-slithering-wildcards.html): `glob_wildcards` does pattern matching on
files _actually present in the directory_. 

Here's a Snakefile that uses `glob_wildcards` to get the four accessions
from the actual filenames:
```python
GLOB_RESULTS = glob_wildcards("genomes/{acc}.fna.gz")
ACCESSIONS = GLOB_RESULTS.acc

print(f'ACCESSIONS is a Python list of length {len(ACCESSIONS)}')
print(ACCESSIONS)

rule all:
    input:
        expand("{acc}.sig", acc=ACCESSIONS)

rule sketch_genome:
    input:
        "genomes/{accession}.fna.gz",
    output:
        "{accession}.sig",
    shell: """
        sourmash sketch dna -p k=31 {input} --name-from-first -o {output}
    """

```

This is a particularly convenient way to get a list of accessions,
although it can be dangerous to use this. In particular, it is easy to
accidentally delete a file and not notice that a sample is missing!
For that reason we suggest providing an independent list of files to
load for many situations.

## Wildcards and `expand` - some closing thoughts

Combined with wildcards, `expand` is extremely powerful and useful.
Just like wildcards, however, this power comes with some complexity.
Here is a brief rundown of how these features combine.

The `expand` function makes a _list of files to create_ from a pattern and
a list of values to fill in.

Wildcards in rules provide _recipes_ to create files whose names match a
pattern.

Typically in Snakefiles we use `expand` to generate a list of files that
match a certain pattern, and then write a rule that uses wildcards to
generate those actual files.

The list of values to use with `expand` can come from many places, including
text files, CSV files, and config files. It can _also_ come from
`glob_wildcards`, which uses a pattern to _extract_ the list of values from
files that are actually present.

## Links and references

* [snakemake reference documentation for expand](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#the-expand-function)
* The [Python `itertools`](https://docs.python.org/3/library/itertools.html) documentation.
