Proposal: Integrating the OSF into Galaxy as a remote data store
################################################################

:author: C\. Titus Brown
:tags: cos,osf,galaxy
:date: 2015-04-27
:slug: 2015-osf-galaxy-dibs-funding
:category: science

**Note** - this was an internal funding request solicited by the
`Center for Open Science <http://cos.io>`__.  It's been funded!

**Brief:** We propose to integrate OSF into Galaxy as a data store. For
this purpose, we request 3 months of funding (6 months, half-time) for
one developer, plus travel.

**Introduction and summary:** Galaxy is a commonly used open source
biomedical/biological sequence data analysis platform that enables
biologists to put together reproducible pipelines and execute analyses
locally or in the cloud.  Galaxy has a robust and sophisticated
Web-based user interface for setting up these pipelines and analyzing
data. One particular challenge for Galaxy is that on cloud instances,
data storage and publication must be done using local filesystems and
remote URLs, which adds a significant amount of complexity for
biologists interested in doing reproducible computing. Recently,
Galaxy gained a data abstraction layer that permits object stores to
be used instead of local filesystems.  The Center for Open Science’s
Open Science Framework (OSF), in turn, is a robust platform for
storing, manipulating, and sharing scientific data, and provides APIs
for accessing such data; the OSF can also act as a broker for
accessing and managing remote data stores, on e.g. cloud
providers. Integrating the OSF’s object store into Galaxy would let
Galaxy use OSF for data persistence and reproducibility, and would let
Galaxy users take advantage of OSF’s data management interface, APIs,
and authentication to expand their reproducible biomedical science
workflows. This integration would also rigorously test and exercise
newly developed functionality in both Galaxy and the OSF, providing
valuable use cases and testing.

Our “stretch” goal would be to expand beyond Galaxy and work with
Project Jupyter/IPython Notebook’s data abstraction layer to provide
an OSF integration for Project Jupyter.

We note with enthusiasm that all groups mentioned here are robust
participants in the open source/open science ecosystem, and all
projects are full open source projects with contributor guidelines and
collaboration workflows!

Broader impacts: If successful, the proposed project addresses several
broader issues.  First, the OSF would have an external consumer of its
APIs for data access, which would drive the maturation of these APIs
with use cases.  Second, the OSF would expand to support connections
with a visible project in a non-psychology domain, giving COS a
proof-of-concept demonstration for expansion into new communities.
Third, the Galaxy biomedical community would gain connections to the
OSF’s functionality, which would help in execution, storage, and
publication of biomedical data analyses. Fourth, the Brown Lab would
then be able to explore further work to build their Moore-DDD-funded
data analysis portal on top of both Galaxy and the OSF, leveraging the
functionality of both projects to advance open science and
reproducibility.  Even a partial failure would be informative by
exposing faults in the OSF or Galaxy public APIs and execution models,
which could then be addressed by the projects individually.  This
project would also serve as a “beta test” of the COS as an incubator
of open science software projects.

Longer-term outcomes: the Brown Lab and the COS are both interested in
exploring the OSF as a larger hub for data storage for workflow
execution, teaching and training in data-intensive science, and
hosting the reproducible publications.  This proposed project is a
first step in those directions.
