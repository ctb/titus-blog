PyCon sprints - playing with Docker
###################################

:author: C\. Titus Brown
:tags: docker,khmer
:date: 2015-04-14
:slug: 2015-pycon-sprint-docker
:category: science

I'm at the PyCon 2015 sprints (day 2), and I took the opportunity to play
around with Docker a bit.

----

First, I created a local docker container that contained an installed version
of khmer.  I ran a blank docker container::

   docker run -it ubuntu

and then installed the khmer prereqs on it, followed by khmer (run on the docker container)::

   apt-get update
   apt-get install -y python-pip python-dev
   pip install khmer

then I logged out, and created a named docker container from that::

   docker commit -m "installed khmer" -a "Titus Brown" 28138ab4095d titus/khmer:v1.3

And now I can run the khmer scripts like this -- ::

   docker run -it titus/khmer:v1.3 /usr/local/bin/normalize-by-median.py

----

Next, I automated all of this with a Dockerfile::

   cat > Dockerfile <<EOF
   FROM ubuntu:14.04
   MAINTAINER Titus Brown <titus@idyll.org>
   RUN apt-get update && apt-get install -y python-dev python-pip
   RUN pip install -U setuptools
   RUN pip install khmer==1.3
   EOF

   docker build -t titus/khmer:v1.3 .

----

Either container lets me run normalize by median on a file *outside*
of the container like so::

   mkdir foo
   curl https://raw.githubusercontent.com/ged-lab/khmer/master/data/100k-filtered.fa > foo/sequence.fa

   docker run -v $PWD/foo:/data -it titus/khmer:v1.3 normalize-by-median.py /data/sequence.fa -o /data/result.fa

Here, I'm running 'normalize-by-median' on the input file 'foo/sequence.fa',
and the output is placed in 'foo/result.fa'.  The trick is that the './foo/'
directory is mounted on the docker container as '/data/', so normalize-by-median.py sees it as '/data/sequence.fa'.

----

Nice and easy, so far...

--titus
