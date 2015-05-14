Adventures in replicating scientific papers: Docker
###################################################

:author: C\. Titus Brown
:tags: docker,replication,streaming-paper
:date: 2015-05-13
:slug: 2015-docker-and-replicating-papers
:category: science

About a month ago, `I took some time to try out Docker
<http://ivory.idyll.org/blog/2015-pycon-sprint-docker.html>`__, a
container technology that lets you bundle together, distribute, and
execute applications in a lightweight Linux container.  It seemed neat
but I didn't get the time to really try it out.  (Heng Li also tried
it out, and `came to some interesting conclusions
<http://lh3.github.io/2015/04/25/a-few-hours-with-docker/>`__ -- note,
`the packaging discussion in the comments
<http://lh3.github.io/2015/04/25/a-few-hours-with-docker/#comment-1992304522>`__
is pretty fascinating!)

I decided that the first real thing I'd try to do with Docker was
implement a software container for `our latest paper submission
<https://peerj.com/preprints/890/>`__ on semi-streaming algorithms for
DNA sequence analysis, but I got busy for a month or so.  During this
period I had a bit of a tough time conceptualizing exactly how I'd use
Docker - I didn't want to bundle the data, and I wasn't sure of my
actual use case.  (There are `a lot of people starting to use Docker
in science
<http://ivory.idyll.org/blog/2015-pycon-sprint-docker.html#disqus_thread>`__,
but so far only `nucleotid.es <http://nucleotid.es>`__ has convinced
me of its unambiguous utility.)

Fast forward to today, when I talked with Michael Crusoe and got his
input on the general idea.  We settled on trying out Docker to bundle
together the software needed to run the `full paper pipeline
<https://github.com/ged-lab/2014-streaming/blob/master/pipeline/Makefile>`__
of the streaming paper (built with `my lab's standard approach
<http://ivory.idyll.org/blog/2014-our-paper-process.html>`__ to
replication, which we started doing `three years ago
<http://ivory.idyll.org/blog/replication-i.html>`__!)  This wasn't
terribly ambitious but seemed like it could be useful - more on that
below.

So, anyway, it turned out to be really easy!  I installed Docker on an
`AWS <http://aws.amazon.com>`__ m3.xlarge, create a `Dockerfile
<https://github.com/ged-lab/2014-streaming/blob/master/pipeline/Dockerfile>`__,
and `wrote up some instructions
<https://github.com/ged-lab/2014-streaming/blob/master/DOCKER.rst>`__.

The basic idea is this:

* install all the software in a Docker container (only needs to be done once,
  of course);

* clone `the repository <https://github.com/ged-lab/2014-streaming/>`__ on
  the host machine;

* copy the raw data@@ into the ``pipeline/`` sub-directory of the paper
  repository;

* run the docker container with the root of the paper repository (on the
  host, wherever it might be) bound to a standard location ('/paper') in
  the image;

* voila, raw data in, analyzed results out.

The value proposition of Docker for data-intensive papers
---------------------------------------------------------

I get the sense that this is not really the way people are thinking
about using Docker in science, but I'm not really sure.  Most of what
`I've seen
<http://ivory.idyll.org/blog/2015-pycon-sprint-docker.html#disqus_thread>`__
has to do with workflows, and I get the sense that the remaining
people desperately want to avoid having to package their software.
But it simply didn't make sense to break workflow steps for this paper
out into different Docker images, since it mostly depends on our own
software.  If I really wanted to, I suppose I could break the
Quake/Jellyfish step down into their own containers...

I'm not sure how the community feels about the volume binding, either.
In this case, I really didn't want to package the raw data with the
docker image; it's 15-20 GB of data!  But it limits our ability to
deploy the container to compute farms (admittedly, we don't really
want to do that, but maybe we should).  I'm not sure how to deal
with that.

The main value that I currently see is in not polluting my work
environment on machines where I can run Docker.  (Sadly this does not
yet include our HPC at MSU, but maybe we can broker something out at
Davis.)  I could also use a Project Jupyter container to build our
figures, and use a Latex container to build the paper.

I do really like the explicit documentation of the install and
execution steps.  That's super cool and probably the most important
bit for paper replication.  The scientific world would be a better
place if the computation for data analysis and modeling in most papers
came in a Dockerfile-style format! "Here's the software you need, and
the command to run; put the data here and go!"

I can absolutely see the value for stuff like `nucleotid.es
<http://nucleotid.es>`__, and think maybe we should re-tool our `k-mer
counting benchmark paper
<http://www.ncbi.nlm.nih.gov/pubmed/?term=PMC4111482>`__ to just use
containers to run each k-mer counting package.  That may be my next
demo, unless I get sidetracked by my job :).

Next steps
----------

I'm really intrigued by two medium-term directions -- one is the
`bioboxes-style approach <http://bioboxes.org/>`__ for connecting
different Docker containers into a workflow, and the other is the
`nucleotid.es <http://nucleotid.es>`__ approach for benchmarking
software.  If this benchmarking can be combined with github repos ("go
benchmark the software in this github project!") then that would
enable rapid convergence towards continuously running benchmarks
on whatever software we were interested in.

Longer term, I'd like to have a virtual computing environment in which
I can use my Project Jupyter notebook running in a Docker environment
to quickly and easily spin up a data-intensive workflow involving
N docker containers running on M machines with data flowing through
them *like so*.  I can already do this with AWS but it's a bit clunky;
I foresee a much lighter-weight future.

In the shorter term, I'm hoping we can put some expectations in place
for what dockerized paper replication pipelines might look like.
Hint: `binary blobs should not be acceptable!
<http://ivory.idyll.org/blog/2014-containers.html>`__.  Now, off to
review that paper that comes with a Docker container... :)

--titus
