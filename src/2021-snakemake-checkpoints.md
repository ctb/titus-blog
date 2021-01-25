Title: A snakemake hack for checkpoints
Date: 2021-01-25
Category: science
Tags: snakemake, python
Slug: 2021-snakemake-checkpoints
Authors: C. Titus Brown
Summary: snakemake checkpoints r awesome

As I get deeper and deeper into using the excellent snakemake workflow system for ...everything, I have had to learn how to use checkpoints.  I ended up hacking together an approach that made checkpoints easy for me, and now I'm caught between being proud of it and wondering if it's Actually Bad.  So I thought I'd share and see what y'all thought.

(Thanks to Taylor Reiter, Tessa Pierce, and Luiz Irber for their comments on early drafts of this blog post!)

## What are checkpoints for?

By default, snakemake figures out what to run based on the rules in the Snakefile and whatever files are present in the working space. It implements this using a simple but incredibly powerful pattern matching technique that is executed at the very beginning of the run.

The one big problem with doing everything at the beginning of the run is that if you don't know exactly which files are going to be produced by a particular step, you can't write a regular rule to depend on them.

For example, suppose you want to run a BLAST search against a query sequence, and then for each BLAST match you want to download the matching sequence and do more analysis. snakemake could handle doing the BLAST easily enough, but the rule that downloads matching sequences would have somewhere between 0 and N outputs. How many wouldn't be known until the BLAST was done!

There are a few different approaches you can use --

* simply having multiple workflows (I did this for a while :)
* [snakemake dynamic](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#dynamic-files)
* [snakemake checkpoints](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#data-dependent-conditional-execution)

This blog post is about the last option, which is (apparently) the stable approach, going forward!

## What do checkpoints do?

Briefly put, checkpoints trigger a re-evaluation of the Snakefile rules in light of new information.

For each checkpoint, snakemake looks at the rules that depend on the checkpoint's output, and holds off on evaluating downstream inputs until the checkpoint is done. Once the checkpoint is done, the rules are evaluated and new jobs are entered into snakemake's TODO list.

## How do checkpoints work, under the hood?

It took me a surprisingly large amount of time to figure out these details, so I'm going to share in case others are in a similar boat :).

There is a `checkpoints` namespace.

When you create a checkpoint, it is entered into this namespace.

When another rule's input *refers* to a checkpoint to get its outputs, by calling `checkpoint.<name>.get(...)`, snakemake raises an exception. This exception tells it to defer evaluation of the checkpoint outputs until the checkpoint; snakemake tracks the calling rule and waits.

Once the checkpoint is executed, the output becomes available and the rules that depend on it are re-evaluated.

## An example of the syntax

The syntax is straightforward - you define checkpoints
the same way you do rules, and then you refer to the
checkpoint in [an input function](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#snakefiles-input-functions).

```python
checkpoint a:
    output: touch("a.out")

def input_for_b(*wildcards):
    return checkpoints.a.get().output
    
rule b:
    input:
        input_for_b
    run: 
        print(f'input is: {input}')
```

and if you run [rule b in this example](https://github.com/ctb/2021-snakemake-checkpoints-example/blob/latest/Snakefile.example) like so,
```
% snakemake -j 1 -s Snakefile.example b
```
you will see `input is: a.out`.

Note this example is a bit useless, though, because in this case you could make `checkpoint a` a rule; it doesn't do anything here that requires it to be a checkpoint. Specifically, the output of rule `a` and input of rule `b` are both known.

Nonetheless, I think it serves as a useful example of the syntax:

* the output of the checkpoint must be something that fits into the snakemake rules - a filename or a wildcard pattern or something specific.
* the rules that depend on this checkpoint need to use a [function as an input](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#snakefiles-input-functions), so that snakemake can *try* to run it and generate the exception that lets it know this depends on a checkpoint.
* the input function must take a list of potential wildcards, even if there are no wildcards and/or the wildcards aren't used.

## A real example: making a spreadsheet dynamically, and then using that spreadsheet

[Here is an example Snakefile](https://github.com/ctb/2021-snakemake-checkpoints-example/blob/latest/Snakefile.random) that is closer to how I use checkpoints in real Snakefiles.

Briefly, a rule `make_spreadsheet` builds a spreadsheet with some filenames in it (here, the entries are random, but it could be doing something useful, like running BLAST).

Then, I define a checkpoint that waits for that file to be created, and ...does nothing.

Last, I define a rule that depends on that checkpoint. This rule reads in all the names from the spreadsheet and then builds a list of output filenames, `output-{name}.txt` where `{name}` is taken from the spreadsheet.
```python
rule make_all_files:
    input:
        Checkpoint_MakePattern("output-{name}.txt")
```
The individual files are created by another rule; `make_all_files` just has the responsibility of laying out the list of files to be created, which is created by the `Checkpoint_MakePattern` class, discussed a few paragraphs below.

The interesting thing here is that the checkpoint doesn't really do anything; it just requires that the `names.csv` file exist (triggering the correct upstream rule), and it touches a file (because, as it turns out, checkpoints _must_ have an output.)
```python
# second rule, a checkpoint for rules that depend on contents of "count.csv"
checkpoint check_csv:
    input: "names.csv"
    output: # checkpoints _must_ have output.
        touch(".make_spreadsheet.touch")
```

The "magic" here is in the `Checkpoint_MakePattern` class, which I defined. This class takes in and saves a pattern:
```python
class Checkpoint_MakePattern:
    def __init__(self, pattern):
        self.pattern = pattern
```

and then, when called as part of the input function in `make_all_files`, it (a) waits for the checkpoint, (b) gets the names from the CSV file (`get_names()` call), and \(c\) expands the pattern with the names from the CSV file:
```python
    def __call__(self, w):
        global checkpoints

        # wait for the results of 'check_csv'; this will trigger an
        # exception until that rule has been run.
        checkpoints.check_csv.get(**w)

        # the magic, such as it is, happens here: we create the
        # information used to expand the pattern, using arbitrary
        # Python code.
        names = self.get_names()

        pattern = expand(self.pattern, name=names, **w)
        return pattern
```

The only application-specific bit of code is in `get_names()`, which reads in the CSV:
```python
    def get_names(self):
        with open('names.csv', 'rt') as fp:
            names = [ x.rstrip() for x in fp ]
        return names
```

This function can do pretty much anything it needs to do, and could (in cases where a bunch of output files are created) be replaced with snakemake's [`glob_wildcards` function](https://snakemake.readthedocs.io/en/stable/project_info/faq.html#how-do-i-run-my-rule-on-all-files-of-a-certain-directory).

## Another example: taking a count from a file.

[Here is another Snakefile](https://github.com/ctb/2021-snakemake-checkpoints-example/blob/latest/Snakefile.count) that outputs `h+2` (where h is the current hour of the day) to a file `count.txt`.
The number in `count.txt` is then used to create files named "output-1.txt" to "output-{n}.txt", 

Clearly snakemake's runtime analyzer can't know how many files are going to be output up front, so the Snakefile uses a checkpoint to read in the hour from `count.txt`, and then uses `expand` to generate the output file patterns:

```python
rule make_file:
    output:
        "output-{n}.txt"
    shell:
        "echo hello, world > {output}"

rule make_all_files:
    input:
        Checkpoint_MakePattern("output-{n}.txt")
```

## A third example - reimplementing `dynamic`

Luiz made an interesting comment when he read a draft of this blog post: he pointed out that this gets pretty close to the [`dynamic` behavior](https://snakemake.readthedocs.io/en/stable/snakefiles/rules.html#dynamic-files). So I thought I'd (try) to reimplement that!

The result is [here, in Snakefile.dynamic](https://github.com/ctb/2021-snakemake-checkpoints-example/blob/latest/Snakefile.dynamic).

The `make_files` rule makes a bunch of files (mimicking clustering output, for example).  Then the `Checkpoint_MakePattern` class uses `glob_wildcard` to figure out what files there are and extract wildcards, which it uses to fill in the pattern:
```python
    def __call__(self, w):
        global checkpoints

        # wait for the results of 'check_csv'; this will trigger an
        # exception until that rule has been run.
        checkpoints.make_files.get(**w)

        # use glob_wildcards to find the (as-yet-unknown) new files.
        names = glob_wildcards('output-{rs}.txt')[0]

        pattern = expand(self.pattern, name=names, **w)
        return pattern
```

For example, this rule transforms all of the `output-{random}.txt` files into `output-{random}.round2` names:
```python

# final rule that depends on that checkpoint and transforms
# dynamically created files into something else.
rule make_patterns:
    input:
        '.make_rs_files.touch',
        Checkpoint_MakePattern('output-{name}.round2')
```
A bonus feature is that you can easily compute a summary across all the files like so:
```python
# bonus rule that does something with all the files
rule make_summary:
    input:
        '.make_rs_files.touch',
        files=Checkpoint_MakePattern('output-{name}.txt')
    output:
        'output-random.summary'
    shell: """
        cat {input.files} > {output}
    """
```

## This works, but is it a good way to do things?

The `Checkpoint_MakePattern` code that I used above gave me a simple way to make use of checkpoints.  I largely ignored the internal snakemake mechanism for passing around information that is laid out in the docs and in (e.g.) [this very useful blog post](https://evodify.com/snakemake-checkpoint-tutorial/).

I just write Python code that (a) triggered the checkpoint exception and then (b) Did Something in pure Python to spit out a list of files to be created.

I've used essentially this same code a few times now, and I like it a lot! But I would love feedback as to whether I'm doing something unnatural here :), or if I'm missing something that's really much simpler. Feedback welcome!

--titus
