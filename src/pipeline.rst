My new data analysis pipeline code
##################################

:author: C\. Titus Brown
:tags: python,bioinformatics,science
:date: 2011-03-11
:slug: pipeline
:category: science


First, I write a recipe file, 'metagenome.recipe', laying out my
job description for, say, sequence trimming and assembly with Velvet::

   fasta_file soil-data.fa

   qc_filter min_length=50 remove_Ns=true 

   graph_filter min_length=400

   velvet_assemble k=33 min_length=1000 scaffolding=True

Then I specify machine parameters, e.g. 'bigmem.conf'::

   [defaults]
   n_threads=8

   [graph_filtering]
   use_mem=32gb

   [velvet]
   needs_mem=64gb

And finally, I run the pipeline::

   % ak-run metagenome.recipe -c bigmem.conf

If I have cloud access (and who doesn't?) I can tell the pipeline to
spin up and down nodes as needed::

   % ak-aws-run metagenome.recipe -c bigmem.conf

(Bear in mind most of these tasks are multi-hour, if not multi-day, operations,
so I'm not too worried about optimizing machine use and re-use.)

Hadoop jobs could be spawned underneath, depending on how each recipe
component was actually implemented.

As for testing reproducibility of pipeline results, which is the
short-term motivation here, I can store results for regression
testing with later versions::

   % ak-run metagenome.recipe -c bigmem.conf --save-endpoint=/some/path

and then compare::

   % ak-run --check-endpoint=/some/path

---

Now, does anyone know of a package or packages that actually do this, so
I/we don't have to write it??

See `texttest <http://texttest.carmen.se/>`__ and `ruffus
<http://www.ruffus.org.uk/tutorials/simple_tutorial/simple_tutorial.html>`__
for some of my inspiration/interest.

--titus


----

**Legacy Comments**


Posted by Nick Loman on 2011-03-11 at 10:35. 

::

   I've been playing with EC2 the last few days and want something
   similar.    Packages that look potentially interesting include:
   Fabric (Python lib for controlling bunches of servers either local or
   remote)    MIT Starcluster - roll a proper MPI-capable cluster on EC2
   Kokki (config management) <a
   href="http://samuelks.com/kokki/">http://samuelks.com/kokki/</a>


Posted by Greg Wilson on 2011-03-11 at 13:01. 

::

   Why not ruffus itself?


Posted by Titus Brown on 2011-03-11 at 14:01. 

::

   ruffus doesn't seem to handle any of the configuration or setup or
   data management; isn't it primarily for dependency management?  That's
   not a big problem for me; we know the recipes and they don't change.
   But maybe I'm missing something?

