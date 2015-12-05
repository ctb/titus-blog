A year-old editorial regarding computational infrastructure sustainability##########################################################################

:author: C\. Titus Brown
:tags: sustainability
:date: 2015-07-20
:slug: 2015-cyberinfrastructure-sust
:category: science

*Note: A year ago, I wrote this in response to an editorial request.
Ultimately they weren't interested in publishing it, and I got distracted
and this languished on my hard disk.  So when I remembered it recently,
I decided to just push it out to my blog, where I should have put it in
the first place. --titus*

**All things come to an end eventually, including funding for
computational services.  What is a field to do?**

As biology steadily becomes more and more data intensive, the need for
community-wide analysis software, databases, data curation, and
Internet services grows.  While writing software and gathering data
are both expensive, the cost of maintaining software and curating data
sets over time can dwarf the upfront costs; in the software industry,
for example, software maintenance and support costs can be 10-or
100-fold the initial investment to develop the software.  Despite
this, there is often little sustained academic funding for software
maintenance, data curation, and Internet service support; in part,
this may be because the maintenance costs for existing data and
software could easily consume all of the available funding!  Yet this
lack of infrastructure is increasingly problematic, as data set sizes
and curation needs grow, and tools to interpret and integrate data
sets become ever more critical to forward progress in biology.  How
can we develop and maintain robust infrastructure services while
enabling creative development of new resources and software?

The volume, velocity, and variety of data in biology is stunning, and
would challenge even the handling capacity of more established
data-intensive fields with larger computational investments.  For
example, by analogy with astronomy, `Golden et al. (2012) <http://www.ncbi.nlm.nih.gov/pubmed/?term=23953643>`__ propose
bringing processing pipelines closer to the data generating instrument
(in this case, the sequencing machine).  While this approach can
certainly help address the volume and velocity of sequencing data, it
fails to address the variety -- there are dozens of types of
sequencing output, with perhaps hundreds of different processing
pipelines, the choice of which depends critically on the biological
system being analyzed and the questions being asked of the data.  Some
subfields of biology may well be able to standardize -- for example,
variation analysis for the human genome is increasingly using only a
few processing pipelines -- but for environmental sequencing, the
types of systems and the metadata being gathered are extremely diverse
and nowhere near standardization.  We must recognize that our
knowledge of the natural biological world is so shallow, and the data
gathering needs so great, that the field is very immature compared to
other data-intensive sciences like particle physics and astronomy.

How can we build sustained computational analysis and data storage
services, in the face of increasingly large and diverse biological
data sets, with fast-moving analysis needs?  This question has been
brought into sharp relief in recent years, with the lapses in funding
of TAIR, Tranche, and CAMERA.

While substantial investments have been made in a variety of genomic
and transcriptomic analysis services, only a few projects have
achieved sustained funding independent of large host institutes.
Chief among these are the biomedically relevant projects, which
include Wormbase, Flybase, and SGD, all of which have been funded for
well over a decade by the NIH.  Many others, including iPlant
Collaborative and KBase, are in a ramp-up phase and are still
exploring options for long-term support.  With rare exceptions, it is
safe to say that no large cyberinfrastructure effort has successfully
weaned itself from continued large-scale support from a granting
agency - and some have failed to find this continued funding, and have
no clear future.

The challenges for sustainability of cyberinfrastructure are
significant.  The necessary mix of data storage, research software
development, database curation, and service hosting requires
substantial and diverse computational expertise, large compute
resources, and extensive community involvement to ensure relevance.
Even individually, these can be hard to find, and yet projects often
try to combine all four of these: to a large extent they buy their own
hardware, manage it with their own infrastructure software, develop
their own research analysis software, store their data, and curate
their databases.  Hybrid models exist -- for example, iPlant
Collaborative works with a number of external computational biologists
to develop and integrate tools -- but these efforts are often
centrally managed and continue to require substantial funding for this
integration.

Another challenge is that of maintaining innovation in algorithm and
software development while continuing to provide robust services.
Many innovative computational tools have emerged from small labs and
become more broadly useful, but it can be hard for small labs to
engage with large, centralized infrastructure projects.  Moreover,
even in these models, the larger efforts can only engage deeply with a
few collaborators; these choices privilege some tools over others, and
may not be based on technical merit or community need.  This may also
arise from the tension between engineering and research needs: large
projects prize engineering stability, while research innovation is
inherently unstable.

There is the hope of a more sustainable path, rooted in two approaches
-- one old, and one new.  The old and proven approach is that of open
source.  The open source community has existed for almost half a
century now, and has proven to be remarkably capable: open source
languages such as R and Python are widely used in data analysis and
modeling, and the Linux operating system dominates scientific
computing.  Moreover, the open source workflow closely tracks the
ideal of a scientific community, with a strong community ethic,
widespread collaboration, and high levels of reproducibility and good
computational practice (`Perez and Millman, 2014
<http://www.jarrodmillman.com/oss-chapter.html>`__).  The new approach
is cloud computing, where the advent of ubiquitous virtualization
technology has made it possible for entire companies to dynamically
allocate disk and compute infrastructure as needed with no upfront
hardware cost.  Open source approaches provide an avenue for long-term
research software sustainability, while cloud computing allows
cyberinfrastructure projects to avoid upfront investment in hardware
and lets them grow with their needs.

Interestingly, two notable exceptions to the cyberinfrastructure
sustainability dilemma exploit both open source practices and cloud
computing.  The Galaxy Project develops and maintains an open source
Web-based workflow interface that can be deployed on any virtual
machine, and in recent years has expanded to include cloud-enabled
services that lets users manage larger clusters of computers for more
compute-intensive tasks.  Importantly, users pay for their own compute
usage in the cloud: tasks that consume more compute resources will
cost more.  Since Galaxy is also locally deployable, heavy users can
eschew the cost of the cloud by installing it on existing local
compute resources.  And, finally, large providers such as iPlant
Collaborative can host Galaxy instances for their user communities.
Likewise, the Synapse project is an open source project developed by
Sage Bionetworks that hosts data and provenance information for
cooperative biomedical analysis projects.  While less broadly used
than Galaxy, Synapse is -- from an infrastructure perspective --
infinitely expandable: the Sage Bionetworks developers rely entirely
on the Amazon cloud to host their infrastructure, and scale up their
computing hardware as their computing needs increase.

A general approach using open source and cloud computing approaches
could separate data set storage from provision of services, active
database curation, and software development.  One example could look
like this: first, long-term community-wide cyberinfrastructure efforts
would focus on static data storage and management, with an emphasis on
building and extending metadata standards and metadata catalogs.
These efforts would place data in centralized cloud storage,
accessible to everyone.  There, separately funded data services would
actively index and serve the data to address the questions and
software stacks of specific fields.  In tandem, separately funded new
data curation and research software development efforts would work to
refine and extend capabilities.

If we follow this path, substantial upfront investment in tool
development and data curation will still be needed -- there's no such
thing as a free lunch.  However, when the project sunsets or funding
lapses, with the open source/open data route there will still be
usable products at the end.  And, if it all rests on cloud computing
infrastructure, communities can scale their infrastructure up or down
with their needs and only pay for what they use.

Funders can help push their projects in this direction by requiring
open data and open source licenses, encouraging or even requiring
multiple deployments of the core infrastructure on different cloud
platforms, and ultimately by only funding projects that build in
sustainability from the beginning.  Ultimately, funders must request,
and reviewers require, an end-of-life plan for all infrastructure
development efforts, and this end-of-life plan should be “baked in” to
the project from the very beginning.

In the end, providing robust services while developing research
software and storing and curating data is both challenging and
expensive, and this is not likely to change with a top-down funding or
management paradigm.  We need new processes and approaches that enable
bottom-up participation by small and large research groups; open
approaches and cloud computing infrastructure can be a solution.

