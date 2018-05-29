# Patterns and anti-patterns for writing command-line bioinformatics software

(these lessons learned with Michael Crusoe, Camille Scott, Luiz Irber,
and Daniel Standage)

(Who knew I had so many opinions? :)

1. Use subcommands.

With khmer, we wrote many individual Python scripts that performed
different end-user functions while relying on an underlying
high-performance Python library.  This fit our own usage pattern
during the early years of khmer, in which we did not install khmer
but instead ran it out of the development directory. Once others
wanted to use it, and we developed release protocols, we realized that
it was probably impolite to populate system bin directories with
a dozen or more scripts that weren't clearly identified as belonging to
the khmer package.

Instead, in sourmash, we use the subcommand format, popularized by git
and hg, among other programs: `sourmash <subcommand> <subcommand
arguments>`.  This lets us develop new subcommands and scripts without
polluting the global namespace, and clearly identifies the software
being run.

2. Required arguments should not use - prefixes.

In both khmer and sourmash, we follow common UNIX parlance, and
only optional arguments are prefixed with '-'.  For example,
`sourmash compute *.fa` uses sensible default arguments to build
MinHash signatures.

Likewise, we name our required arguments so that help messages can be
useful, e.g.

`sourmash compute` yields an error message, `sourmash: error: the following arguments are required: filenames`.

3. Results go to stdout, notifications and progress indicators go to stderr.

In both khmer and sourmash, all results output is sent to stdout,
while all status and progress indicator output is sent to stderr.
This lets users sequester results away from progress indicators and
error messages using '>' and '2>'.

4. Support structured output (CSV or TSV, and even JSON) with column headers.

We do our best to support minimally structured output formats such as
comma-separated values or tab-separated values for most of our
scripts; these formats are supported natively by most modern languages,
which allows the widest possible downstream integration.

If more structured output could be useful, we suggest JSON, which can
be parsed in most modern languages and for which flexible command line
display and query languages exist (e.g. `jq`).

5. Support both short and long arguments.

In both khmer and sourmash, we typically supply both long and short
optional arguments that do the same thing, e.g. -v and --verbose; the
former are shorthand, the latter are easier to remember.

6. Use a standard argument parsing library.

Libraries like the argparse library in Python flexibly support many
common UNIX approaches to argument parsing, including different orders
of options, default argument values, and help output.

7. Support common arguments such as '-h/--help', '-v/--verbose', etc.

We try to support a small list of common arguments on each script:

```
-h / --help
-d / --debug
-v / --verbose
--version
```

because they are reasonably standard across many software packages, so
users have come to expect them.

8. Support proper UNIX-style exit codes.

Standard UNIX parlance is to have non-error exits return status code
0, while a non-zero status code indicates error. This allows proper
pipelining and scripting, e.g. Makefiles and snakemake will know the
command has failed and delete incomplete output files if errors are
detected, and -e can be used in shell scripts to exit if a command fails.

9. Support stdin input and streaming output if possible.

Most of our programs support taking sequence input via '-' or
/dev/stdin, because UNIX piping remains a tremendously powerful way to
chain programs together;

10. Support compressed input

Autodetection and support for gzipped input files eliminates the
need to decompress files, which can be taxing to CPUs. khmer supports
gzipped input.

11. Use semantic versioning for command line arguments.

[Semantic versioning](https://semver.org/), when applied to command line
arguments, means that the arguments a script takes in future minor versions
do not become backwards incompatible.  For example, if we release
sourmash 2.0 with support for the command

`sourmash compute -k 31 *.fa`

then that command will work and do the same thing for all sourmash 2.x.
If we change the default parameters or break the meaning of `-k`, we would
have to release a 3.0, although we could *add* parameters.

This is really useful for pipelines and workflows especially, because
you can safely specify a version range for installation of
dependencies, e.g.  "this pipeline uses sourmash >=2.0,<3.0".

12. Support multiple input files where possible.

`sourmash compute /path/to/*.fa` is unpacked by the shell globbing
functionality, so e.g. given two files `/path/to/a.fa` and
`/path/t/b.fa`, this command becomes `sourmash compute a.fa b.fa`.

13. Support good default output filenames in the current working directory...

`sourmash compute /path/to/*.fa` would output `a.fa.sig` and
`b.fa.sig` in the current working directory, rather than putting them
in the `/path/to` directory. This supports several good "hygiene"
practices including using a a project-specific subdirectory that
contains working files, reading data from other locations that may be
read-only, and producing output files with a name corresponding to the
package being used.

14. ...and also support '-o/--output' and other ways of specifying output file names.

One criticism we have received over the years has been that the
previous approach is a good default but is too inflexible if used
alone, so most of our scripts support specifying an output file, e.g.

`sourmash compute /path/to/*.fa -o /other/path/out.sig` would put both
sets of signatures in `/other/path/out.sig`.

In situations where multiple output files may result, you can provide
`--prefix` or `--suffix` to set default prefixes or suffices on output
files, and/or `--outdir` to provide an output directory location.

15. Handle multiple sets of multiple input files in a tab-completion friendly manner.

Some programs require that you specify multiple input
files via a text file that is passed in on the command line.  This is
confusing because the software takes in two different *kinds* of
files as input - a file containing sequences, and a file containing a list of
filenames containing sequences.

Other programs **require** configuration files, which must then be
created and edited; this is a mild challenge for automated pipelines
to create dynamically and interrupts shell-based interactive workflows.
Often the parameters in these configuration files cannot be modified
at the command line, introducing a barrier to parameter sweeps.

Yet other programs (megahit and SPAdes) take in multiple input files
separated by commas, e.g.

`megahit -1 libraryA-1.fq,libraryB-1.fq -2 libraryA-2.fq,libraryB-2.fq`

but this means you cannot use wildcards or tab completion to fill out
the arguments.

One approach (bwa) is to use -1 and -2, which violates the "required
arguments do not have dashes in front of them" rule above, but seems like
the least of all evils; we suggest something like the following,

`sourmash lca gather --query query1.sig query2.sig --db db1.sig db2.sig`

which enables tab completion and wild cards, 

With a little bit of extra effort, it is relatively easy to allow
intermixed specification, e.g.

`sourmash lca gather --query query1.sig --db db1.sig db2.sig --query query2.sig` which, while we wouldn't recommend as default practice, does offer additional flexibility when quick modifications to a command line are neeed.
