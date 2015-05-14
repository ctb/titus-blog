Adventures in replicable scientific papers: Docker
##################################################

:author: C\. Titus Brown
:tags: docker,replication,streaming-paper
:date: 2015-05-14
:slug: 2015-docker-and-replicating-papers
:category: science

About a month ago, `I took some time to try out Docker
<http://ivory.idyll.org/blog/2015-pycon-sprint-docker.html>`__, a
container technology that lets you bundle together, distribute, and
execute applications in a lightweight Linux container.  It seemed neat
but I didn't apply it to any real problems.  (Heng Li also tried it
out, and `came to some interesting conclusions
<http://lh3.github.io/2015/04/25/a-few-hours-with-docker/>`__ -- note
especially `the packaging discussion in the comments
<http://lh3.github.io/2015/04/25/a-few-hours-with-docker/#comment-1992304522>`__.)

At the sprint, I decided to try building a software container for `our
latest paper submission <https://peerj.com/preprints/890/>`__ on
semi-streaming algorithms for DNA sequence analysis, but I got
interrupted by other things.  Part of the problem was that I had a
tough time conceptualizing exactly what my use case for Docker was.
There are `a lot of people starting to use Docker in science
<http://ivory.idyll.org/blog/2015-pycon-sprint-docker.html#disqus_thread>`__,
but so far only `nucleotid.es <http://nucleotid.es>`__ has really
demonstrated its utility.

Fast forward to yesterday, when I talked with Michael Crusoe about various
ideas.  We settled on using Docker to bundle together the software
needed to run the `full paper pipeline
<https://github.com/ged-lab/2014-streaming/blob/master/pipeline/Makefile>`__
for the streaming paper.  The paper was already highly replicable
because we had used `my lab's standard approach
<http://ivory.idyll.org/blog/2014-our-paper-process.html>`__ to
replication (first executed `three years ago
<http://ivory.idyll.org/blog/replication-i.html>`__!)  This wasn't a
terribly ambitious use of Docker but seemed like it could be useful.

In the end, it turned out to be super easy!  I installed Docker on an
`AWS <http://aws.amazon.com>`__ m3.xlarge, create a `Dockerfile
<https://github.com/ged-lab/2014-streaming/blob/master/pipeline/Dockerfile>`__,
and `wrote up some instructions
<https://github.com/ged-lab/2014-streaming/blob/master/DOCKER.rst>`__.

The basic idea we implemented is this:

* install all the software in a Docker container (only needs to be done once,
  of course);

* clone `the repository <https://github.com/ged-lab/2014-streaming/>`__ on
  the host machine;

* copy the raw data@@ into the ``pipeline/`` sub-directory of the paper
  repository;

* run the docker container with the root of the paper repository (on the
  host, wherever it might be) bound to a standard location ('/paper') in
  the image;

* voila, raw data in, analyzed results out!

(The whole thing takes about 15 hours to run.)

The value proposition of Docker for data-intensive papers
---------------------------------------------------------

So what are my conclusions?

I get the sense that this is not really the way people are thinking
about using Docker in science.  Most of what `I've seen
<http://ivory.idyll.org/blog/2015-pycon-sprint-docker.html#disqus_thread>`__
has to do with workflows, and I get the sense that the remaining
people are trying to avoid issues with software packaging.  In this
case, it simply didn't make sense to me to break our workflow steps
for this paper out into different Docker images, since our workflow
only depends on a few pieces of software that all work together well.
(I could have broken out one bit of software, the Quake/Jellyfish
code, but that was really it.)

I'm not sure how to think about the volume binding, either - I'm
binding a path on the Docker container directly to a local disk, so
the container isn't self-sufficient.  The alternative was to package
the data in the container, but in this case, it's 15-20 GB,
which seemed like too much!  This dependence on external data does
limit our ability to deploy the container to compute farms though.

The main value that I see for this container is in not polluting my
work environment on machines where I can run Docker.  (Sadly this does
not yet include our HPC at MSU.)  I could also use a Project Jupyter
container to build our figures, and perhaps use a separate Latex
container to build the paper... overkill? :).

I also really like the explicit documentation of the install and
execution steps.  That's super cool and probably the most important
bit for paper replication.  The scientific world would definitely be a
better place if the computational setup for data analysis and modeling
components of papers came in a Dockerfile-style format! "Here's the
software you need, and the command to run; put the data here and push
the 'go' button!"

I certainly see the value of docker for running many different
software packages, like `nucleotid.es <http://nucleotid.es>`__ does. I
think we should re-tool our `k-mer counting benchmark paper
<http://www.ncbi.nlm.nih.gov/pubmed/?term=PMC4111482>`__ to use
containers to run each k-mer counting package benchmark. In fact, that
may be my next demo, unless I get sidetracked by my job :).

Next steps
----------

I'm really intrigued by two medium-term directions -- one is the
`bioboxes-style approach <http://bioboxes.org/>`__ for connecting
different Docker containers into a workflow, and the other is the
`nucleotid.es <http://nucleotid.es>`__ approach for benchmarking
software.  If this benchmarking can be combined with github repos ("go
benchmark the software in this github project!") then that might
enable continuously running testing and benchmarks on a wide range of
software.

Longer term, I'd like to have a virtual computing environment in which
I can use my Project Jupyter notebook running in a Docker environment
to quickly and easily spin up a data-intensive workflow involving N
docker containers running on M machines with data flowing through them
*like so*.  I can already do this with AWS but it's a bit clunky; I
foresee a much lighter-weight future for ultra-configurable computing.

In the shorter term, I'm hoping we can put some expectations in place
for what dockerized paper replication pipelines might look like.
Hint: `binary blobs should not be acceptable!
<http://ivory.idyll.org/blog/2014-containers.html>`__.

Now, off to review that paper that comes with a Docker container... :)

--titus
