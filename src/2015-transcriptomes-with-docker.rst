Transcriptomic analysis with Docker containers and data volumes
###############################################################

:author: C\. Titus Brown
:tags: docker,transcriptomes
:date: 2015-11-26
:slug: 2015-transcriptomes-with-docker
:category: science

As part of our `Docker hands-on workshop
<https://github.com/ngs-docs/2015-nov-docker/blob/master/README.md>`__
earlier this month, I learned a lot about building Dockerfiles,
running Docker containers on remote hosts with docker-machine, and
using data volumes to manage data in remotely hosted Docker
containers.

During and after the workshop, I put together Docker images (and, more
importantly, `build instructions *for* those images
<https://github.com/ctb/2015-docker-building>`__) for a few different
pieces of transcriptomics software: `khmer
<http://khmer.readthedocs.org>`__, for digital normalization; `salmon
<http://salmon.readthedocs.org/>`__, for transcript quantification;
`transrate <http://hibberdlab.com/transrate/>`__, for transcriptome
quality evaluation; and `dammit <http://camillescott.org/dammit/>`__,
a pipeline for transcriptome annotation.

Other than remedying my basic ignorance of (first) docker-machine and
(second) data volumes, the only somewhat tricky bit was dammit's
databases.  dammit relies on a fairly large collection of databases,
and these databases need to be established locally (downloaded and
processed) in order to run dammit.  While time consuming, this only
needs to be done once.  So I had to fiddle around a bit, and ended up
with an image that downloads the data if it's not present
(diblab/dammit-db-helper).

It's important to note that these data volume issues are things you
run into when you *can't* (or don't want to) mount local volumes
because you're using docker-machine to run your Docker containers on a
remote host.  If you're using Docker locally, you can just put
everything on local disk and mount those to the running Docker
containers.  But in this case I explicitly want to make use of
resources greater than are available on my laptop by using
docker-machine.

Below are some demo instructions for running transrate and dammit to
evaluate and annotate a transcriptome, using Docker containers.
Everything below should work on both local and remote Docker hosts
(i.e. docker default install or docker-machine), assuming the docker
host has about 15 GB of disk space available for the dammit databases.
The time consuming bits are (a) downloading the Docker images, and (b)
downloading & installing the dammit databases.

Personally, I found installing transrate and dammit (and salmon) to be
big PITA so the fact that I may never have to do that again is a big
win :).

Comments welcome -- I'd love to find easier/better ways of doing this!

--titus

----

Preparing the data
~~~~~~~~~~~~~~~~~~

First, create a data volume containing your transcriptome, and name it
`nema_vol`` (after *Nematostella vectensis*, the organism's
transcriptome that we're using)::

   docker create -v /nema --name nema_vol ubuntu:15.10 /bin/true

Next, extract the transcriptome (``nema.fa.gz``) from `the remote tar ball <https://s3.amazonaws.com/public.ged.msu.edu/nema-subset.tar.gz>`__::

   curl -L https://s3.amazonaws.com/public.ged.msu.edu/nema-subset.tar.gz | tar xzf - nema.fa

Gzip and then copy the transcriptome to ``/nema/nema.fa.gz`` on the
``nema_vol`` container::

   gzip nema.fa && docker cp nema.fa.gz nema_vol:/nema

This makes it available to other containers via the ``nema_vol`` container,
which can be mounted as ``/nema`` via the ``--volumes-from`` command.

Next, uncompress the ``nema.fa.gz`` file::

   docker run --rm --volumes-from nema_vol -it ubuntu:15.10 \
          gunzip -f /nema/nema.fa.gz

Now, the data is ready: it's available as ``/nema/nema.fa`` on any containers
where ``--volumes-from nema_vol`` has been used.

Running transrate
-----------------

To run transrate in its most basic mode, to generate assembly statistics,
you can execute::

   docker run --rm --volumes-from nema_vol -it diblab/transrate \
          transrate --assembly /nema/nema.fa --output=/nema/nema.fa.transrate

This will output::

   [ INFO] 2015-11-20 16:25:07 : Loading assembly: /nema/nema.fa
   [ INFO] 2015-11-20 16:25:49 : Analysing assembly: /nema/nema.fa
   [ INFO] 2015-11-20 16:25:49 : Results will be saved in /nema/nema.fa.transrate
   [ INFO] 2015-11-20 16:25:49 : Calculating contig metrics...
   [ INFO] 2015-11-20 16:26:25 : Contig metrics:
   [ INFO] 2015-11-20 16:26:25 : -----------------------------------
   [ INFO] 2015-11-20 16:26:25 : n seqs                       198151
   [ INFO] 2015-11-20 16:26:25 : smallest                        201
   [ INFO] 2015-11-20 16:26:25 : largest                       17655
   [ INFO] 2015-11-20 16:26:25 : n bases                   137744672
   [ INFO] 2015-11-20 16:26:25 : mean len                     695.15
   [ INFO] 2015-11-20 16:26:25 : n under 200                       0
   [ INFO] 2015-11-20 16:26:25 : n over 1k                     37271
   [ INFO] 2015-11-20 16:26:25 : n over 10k                       64
   [ INFO] 2015-11-20 16:26:25 : n with orf                    46134
   [ INFO] 2015-11-20 16:26:25 : mean orf percent              63.77
   [ INFO] 2015-11-20 16:26:25 : n90                             252
   [ INFO] 2015-11-20 16:26:25 : n70                             573
   [ INFO] 2015-11-20 16:26:25 : n50                            1315
   [ INFO] 2015-11-20 16:26:25 : n30                            2271
   [ INFO] 2015-11-20 16:26:25 : n10                            4111
   [ INFO] 2015-11-20 16:26:25 : gc                             0.44
   [ INFO] 2015-11-20 16:26:25 : gc skew                        0.01
   [ INFO] 2015-11-20 16:26:25 : at skew                         0.0
   [ INFO] 2015-11-20 16:26:25 : cpg ratio                      1.73
   [ INFO] 2015-11-20 16:26:25 : bases n                           0
   [ INFO] 2015-11-20 16:26:25 : proportion n                    0.0
   [ INFO] 2015-11-20 16:26:25 : linguistic complexity          0.13
   [ INFO] 2015-11-20 16:26:25 : Contig metrics done in 36 seconds
   [ INFO] 2015-11-20 16:26:25 : No reads provided, skipping read diagnostics
   [ INFO] 2015-11-20 16:26:25 : No reference provided, skipping comparative diagnostics
   [ INFO] 2015-11-20 16:26:25 : Writing contig metrics for each contig to /nema/nema.fa.transrate/nema/contigs.csv
   [ INFO] 2015-11-20 16:26:55 : Writing analysis results to assemblies.csv

Running dammit
--------------

For dammit annotation, let's extract only a few sequences so it doesn't
take too long! ::

   docker run --rm --volumes-from nema_vol -it ubuntu:15.10 \
       sh -c 'head -110 /nema/nema.fa > /nema/short.fa'

Now prepare the dammit databases; this can be run multiple times but should
complete very quickly after the first run::

   # create a dammit-db data volume; will fail (safely) if run multiple times.
   docker create -v /dammit-db --name dammit-db ubuntu:15.10 /bin/true

   # download & prepare the databases; can be run multiple times.
   docker run --rm --volumes-from dammit-db -it diblab/dammit-db-helper

Finally, run dammit, loading the databases from ``dammit-db`` and the
transcriptome data from ``nema_vol``, and putting the output annotation
in ``/nema/short.fa.dammit``::

   docker run --volumes-from dammit-db --volumes-from nema_vol \
       -it diblab/dammit \
       dammit annotate /nema/short.fa -o /nema/short.fa.dammit

This yields the following runtime output::

   --- Running annotate!

          Transcriptome file: /nema/short.fa

          Output directory: /nema/short.fa.dammit

          [x] sanitize_fasta:short.fa

          [x] transcriptome_stats:short.fa

          [x] busco:short.fa-metazoa

          [x] TransDecoder.LongOrfs:short.fa

          [x] hmmscan:longest_orfs.pep.x.Pfam-A.hmm

          [x] TransDecoder.Predict:short.fa

          [x] cmscan:short.fa.x.Rfam.cm

          [x] lastal:short.fa.x.orthodb.maf

          [x] maf_best_hits:short.fa.x.orthodb.maf-short.fa.x.orthodb.maf.best.csv

          [x] maf-gff3:short.fa.x.orthodb.maf.gff3

          [x] hmmscan-gff3:short.fa.pfam-A.tbl.gff3

          [x] cmscan-gff3:short.fa.rfam.tbl.gff3

          [x] gff3-merge:short.fa.dammit.gff3

----

After all of this, you can grab the annotation results like so::

   # copy off the transrate output:
   docker cp nema_vol:/nema/nema.fa.transrate/assemblies.csv .
   docker cp nema_vol:/nema/nema.fa.transrate/nema/contigs.csv .

   # copy off the final GFF3 transcriptome annotation from dammit:
   docker cp nema_vol:/nema/short.fa.dammit/short.fa.dammit.gff3 .

The nema_vol data volume can be removed with::

   dammit rm -v nema_vol
