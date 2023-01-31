Title: A brief overview of automation and parallelization options in UNIX/on an HPC
Date: 2023-01-31
Category: science
Tags: parallel, slurm, hpc, snakemake, shell scripts
Slug: 2023-automation-and-parallelization
Authors: C. Titus Brown
Summary: Automating things! Parallelizing them!

What do you do if you have a lot of computing jobs to run, and lots of computing resources to run them?

Let's play with some options! We'll run a simple set of bioinformatics analyses as an example, but all of the approaches below should work for a wide variety of command line needs.

Most of the commands below should work as straight-up copy/paste. Please let me know if they don't!

## Setup and file preparation

Download some metagenome assemblies from [our metagenome assembly evaluation project](https://osf.io/vk4fa/?view_only). These are all files generated from from [Shakya et al., 2014](https://pubmed.ncbi.nlm.nih.gov/23387867/) - specifically, assemblies of SRR606249.
```
mkdir queries/
cd queries/
curl -JLO https://osf.io/download/q8h97/
curl -JLO https://osf.io/download/7bzrc/
curl -JLO https://osf.io/download/3kgvd/
cd ..
mkdir -p database/
cd database/
curl -JLO https://osf.io/download/4kfv9/
cd ../
```

Now you should have three files in queries/
```
ls -1 queries/
```

~~~
>idba.scaffold.fa.gz
>megahit.final.contigs.fa.gz
>spades.scaffolds.fasta.gz
~~~

and one file in database/
```
ls -1 database/
```

~~~
>podar-complete-genomes-17.2.2018.tar.gz
~~~

Let's sketch the queries with sourmash:
```shell
for i in queries/*.gz
do
    sourmash sketch dna -p k=31,scaled=10000 $i -o $i.sig
done
```

Next, unpack the database and create `database.zip`:
```shell
cd database/
tar xzf podar*.tar.gz
sourmash sketch dna -p k=31,scaled=10000 *.fa --name-from-first -o ../database.zip
cd ../
```

Finally, make all your inputs read-only:
```
chmod a-w queries/* database.zip database/*
```
This prevents against accidental overwriting of the files.

## Running your basic queries

We're going to run [sourmash gather](https://sourmash.readthedocs.io/en/latest/command-line.html#sourmash-gather-find-metagenome-members) for all three assembly files in `queries/` against the 64 genomes in `database.zip`. These specific commands will run quickly, but note that they are a proxy for a much bigger analysis against larger databases.

You could do these queries in serial:
```shell
sourmash gather queries/idba.scaffold.fa.gz.sig \
    database.zip -o idba.scaffold.fa.gz.csv

sourmash gather queries/megahit.final.contigs.fa.gz.sig \
    database.zip -o megahit.final.contigs.fa.gz.csv

sourmash gather queries/spades.scaffolds.fasta.gz.sig \
    database.zip -o spades.scaffolds.fasta.gz.csv
```
but then your total compute time would be the sum of the individual compute times. And what if each query is super slow and/or big, and you have dozens or hundreds of them? WHAT THEN?

Read on!

## Automation and parallelization

### 1. Write a shell script.

Let's start by automating the queries so that you can just run one command and have it do all three (or N) queries.

Create the following shell script:

`run1.sh`:
```shell
sourmash gather queries/idba.scaffold.fa.gz.sig database.zip -o idba.scaffold.fa.gz.csv

sourmash gather queries/megahit.final.contigs.fa.gz.sig database.zip -o megahit.final.contigs.fa.gz.csv

sourmash gather queries/spades.scaffolds.fasta.gz.sig database.zip -o spades.scaffolds.fasta.gz.csv
```

and run it:
```
bash run1.sh
```

This automates the commands, but nothing else.

Notes:

* all your commands will run in serial, one after the other;
* the memory usage of the script will be the same as the memory usage of the largest command;

### 2. Add a for loop to your shell script.

There's a lot of duplication in the script above. Duplication leads to typos, which leads to fear, anger, hatred, and suffering.

Let's make a script `run2.sh` that contains a for loop instead.

`run2.sh`:
```shell
for query in queries/*.sig
do
output=$(basename $query .sig).csv
sourmash gather $query database.zip -o $output
done
```

While this does exactly the same thing _computationally_ as `run1.sh`, it is a bit nicer because it is less repetitive and lets you run as many queries as you have.

Notes:

* yes, we carefully structured the filenames so that the `for` loop would work :)
* the `output=` line uses `basename` to remove the `queries/` prefix and `.sig` suffix from each query filename.


### 3. Write a for loop that creates a shell script.

Sometimes it's nice to _generate_ a script that you can edit to fine tune and customize the commands. Let's try that!

At the shell prompt, run
```shell
for query in queries/*.sig
do
output=$(basename $query .sig).csv
echo sourmash gather $query database.zip -o $output
done > run3.sh
```

This creates a file `run3.sh` that contains the commands to run. Neato! You could now edit this file if you wanted to individually change up the commands.  Or, you could adjust the for loop if you wanted to change _all_ the commands.

Notes:

* same runtime parameters as above: everything runs in serial.
* be careful about overwriting `run3.sh` by accident after you've edited it!

### 4. Use `parallel` to run the commands instead.

Once we have this script file ready, we can actually run the commands in parallel, using 
[GNU `parallel`](https://www.gnu.org/software/parallel/):
```
parallel -j 2 < run3.sh
```

This runs up to two commands from `run3.sh` at a time (`-j 2`). Neat, right?!

Notes:

* depending on the parameter to `-j`, this can be much faster - here, twice as fast!
* it will also use twice as much memory...!
* `parallel` runs each line on its own. So if you have multiple things you want to run in each parallel session, you need to do something different - like write a shell script to do each compute action, and _then_ run those in parallel.

### 5. Write a second shell script that takes a parameter.

Let's switch things up - let's write a generic shell script that does the computation. Note that it's the same set of commands as in the for loops above!

`do-gather.sh`:
```shell
output=$(basename $1 .sig).csv
sourmash gather $1 database.zip -o $output
```

Now you can run this in a loop like so:
```shell
for i in queries/*.sig
do
   bash do-gather.sh $i
done
```

Notes:

* here, `$1` is the first command-line parameter after the shell script name.
* this is back to processing in serial, not parallel.

It would be easy to make this into something you can run in parallel, by providing a list of `do-gather.sh` commands as in (4), above.

### 6. Change the second shell script to be an sbatch script.

Suppose you have access to an HPC that has many different computers, and you want to run a bunch of big jobs _across_ those computers. How do we do that?

All (most?) clusters have a queuing system; ours is called slurm. (You can see a tutorial [here](https://ngs-docs.github.io/2021-august-remote-computing/executing-large-analyses-on-hpc-clusters-with-slurm.html).)

To send jobs to many different computers, you can write a shell script that executes a particular job, and then run lots of those.

Change `do-gather.sh` to look like the following.

```shell
#SBATCH -c 1     # cpus per task
#SBATCH --mem=5Gb     # memory needed
#SBATCH --time=00-00:05:00     # time needed
#SBATCH -p med2 

output=$(basename $1 .sig).csv
sourmash gather $1 database.zip -o $output
```

This is now a script you can send to the HPC to run, using `sbatch`:
```shell
for i in queries/*.sig
do
    sbatch do-gather.sh $i
done
```

The advantage here is these commands can be scheduled by the HPC to run whenever and wherever there is computational "space" to run them. (Here, the `#SBATCH` lines in the shell script specify how much compute time/memory is needed.)

Notes:

* this distributes your job across the HPC;
* these jobs only take up as much time/memory as each job individually! but now they're running in parallel on multiple machines!
* `do-gather.sh` is actually still a bash script so you can still run it that way, too.

### 7. Write a snakemake file.

An alternative to all of the above is to have snakemake run things for you. Here's a simple snakefile to run things in parallel:

`Snakefile`:
```python
QUERY, = glob_wildcards("queries/{q}.sig")

rule all:
    input:
        expand("{q}.csv", q=QUERY)
        
rule run_query:
    input:
        sig = "queries/{q}.sig",
    output:
        csv = "{q}.csv"
    shell: """
        sourmash gather {input.sig} database.zip -o {output.csv}
    """
```

and run it in parallel:
```
snakemake -j 2
```

Notes:

* this will run things in parallel as in the above example (4).

## Strategies for testing and evaluation

Here are the three strategies I use when trying to scale something up to run in multiple jobs and across multiple computers:

1. Build around an existing example.
2. Subsample your query data.
3. Test on a smaller version of your problem.

## Appendix: making your shell script(s) nicer

The above shell scripts are not actually the way I recommend writing shell scripts! Here are a few additional thoughts for you -

### 1. Make them runnable without an explicit `bash`

Put `#! /bin/bash` at the top of the shell script and run `chmod +x <scriptname>`, and now you will be able to run them directly:

```shell
./run1.sh
```

### 2. Set error exit

Add `set -e` to the top of your shell script and it will stop running when there's an error.
