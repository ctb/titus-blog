I just finished the second day of a workshop on `Docker
<http://www.docker.com/>`__ at the `Berkeley Institute for Data
Science <http:/bids.berkeley.edu/>`__.  I was invited to give the
workshop after some Berkeley folk couldn't make our Davis workshop in
November.

tl;dr? I think the workshop went well, in the sense that the attendees
all got some hands-on experience with Docker and engaged its
potential benefits (as well as some of its limitations).

We delivered the workshop in a `Software Carpentry style
<http://software-carpentry.org>`__, with lots of command-line
interaction and plenty of time for questions.  People were welcome to
follow along with what I was doing on the screen, or just watch; in
either case, we tried to provide fairly thorough notes so that people
could refer back to them in the future.

The workshop was attended by a variety of people, including software
engineering folk, infrastructure folk, supercomputing folk, librarians,
and grad students / postdocs.  Some people had a fair bit of experience
with Docker, while others had only vaguely heard of it; despite this
spread in experience I gather everyone got something out of it.  The
experienced folk got to see how we used it, while the people new to
Docker got a somewhat thorough overview of the technology and its
potential applications.

The workshop focused on scientific applications of Docker.  `Day one
<https://github.com/ngs-docs/2016-bids-docker/blob/master/day1.rst>`__
was mostly about the basics - Docker containers and images,
docker-machine, building docker images, data volumes, directory
mirroring, and exposing ports.  `Day two
<https://github.com/ngs-docs/2016-bids-docker/blob/master/day2.rst>`__
went a bit further afield and talked about `mybinder
<http://www.mybinder.org>`__, docker-compose and docker-swarm, and
some potential workflows for data-intensive applications.

A few random thoughts --

* I still don't really know how to teach Docker, although the hands-on
  approach has to beat more conceptual or theoretical approaches here :).
  The concept is clear enough for CS people, but the details of the
  implementation (and how it all actually works) are really at the heart
  of putting Docker to use.

* Docker doesn't run on HPCs or other multi-tenant systems very well,
  which everyone recognizes as a problem. There was some discussion
  of `Shifter <https://www.nersc.gov/news-publications/nersc-news/nersc-center-news/2015/shifter-makes-container-based-hpc-a-breeze/>`__, which is a
  Docker-like technology intended to address this deficit.

* Docker still isn't great in terms of data management.  Data volumes
  are poor vessels for communicating data.  Carl Boettiger showed us
  an approach based on `Flocker <https://clusterhq.com/flocker/introduction/>`__ that "required only a little configuration."  I should probably look into
  this.

* We don't have a clear use case for docker-compose in science.

* The ease with which you can get an RStudio Server or a Jupyter notebook
  running inside of Docker is astonishing.

* Everyone was pretty impressed with how easy and obvious
  `mybinder.org <http://mybinder.org>`__ is, and seemed to
  think that it would fit into an only slight evolved data science
  workflow.  I really want to explore at the seams between long-running
  data-intensive tasks, and the all-data-fits-in-github short-run
  analysis supported by mybinder...

  I put together two demos for mybinder, `one of a Software Carpentry
  data set <https://github.com/ctb/2016-mybinder-inflammation>`__ and
  `one showing how to do some significant software installs
  <https://github.com/ctb/2016-mybinder-irkernel>`__.

  It's a super cool service!

  

  

