A grant proposal: A workshop on dockerized notebook computing
#############################################################

:author: C\. Titus Brown
:tags: python,pyblosxom
:date: 2016-03-31
:slug: 2016-mybinder-workshop-proposal
:category: science

I'm writing a proposal to the Sloan Foundation for about $20k to support a
workshop to hack on mybinder.  Comments solicited.  Note, it's, umm, due
today ;).

(I know the section on "major related work" is weak. I could use some help
there.)

If you're interested in participating and don't mind being named in
the proposal, `drop me an e-mail <mailto:titus@idyll.org>`__ or leave
me a note in a comment.

----
           
**Summary:**

We propose to host a hackfest (cooperative hackathon) workshop to enhance and extend the functionality of the mybinder notebook computing platform. Mybinder provides a fully hosted solution for executing Jupyter notebooks based in GitHub repositories; it isolates execution and provides configurability through the use of Docker containers. We would like to extend mybinder to support a broader range of data science tools - specifically, RStudio and other tools in the R ecosystem - as well as additional cloud hosting infrastructure and version control systems.  A key aspect of this proposal is to brainstorm and prototype support for credentials so that private resources can be used to source and execute binders (on e.g. AWS accounts and private repositories). We believe this will broaden interest and use of mybinder and similar resources, and ultimately drive increased adoption of fully specified and executable data narratives.

**What is the subject, and why is it important?**

Fully specified and perfectly repeatable computational data analyses have long been a goal of open scientists - after all, if we can eliminate the dull parts of reproducibility, we can get one with the more exciting bits of arguing about significance, interpretation and meaning. There is also the hope that fully open and repeatable computational methods can spur reuse and remixing of these methods, and accelerate the process of computational science. We have been asymptotically approaching this in science for decades, helped by configuration and versioning tools used in open source development and devops.  The emergence of fully open source virtual machine hosting, cloud computing, and (most recently) container computing means that a detailed host configuration can be shared and instantiated on demand; together with flexible interactive Web notebooks such as RStudio and Jupyter Notebook, and public hosting of source code, we can now provide code, specify the execution environment, execute a workflow, and give scientists (and others) an interactive data analysis environment in which to explore the results.

Fully specified data narratives will are already impacting science and journalism, by providing a common platform for data driven discussion. We and others are using them in education, as well, for teaching and training in data science, statistics, and other fields. Jupyter Notebooks and RMarkdown are increasingly used to write books and communicate data- and compute-based analyses. And, while the technology is still young, the interactive widgets in Jupyter make it possible to communicate these analyses to communities that are not coders.  At the moment, we can’t say where this will all lead, but it is heading towards an exciting transformation of how we publish, work with, collaborate around, and explore computing.

mybinder and similar projects provide a low barrier-to-entry way to publish **and then execute** Jupyter notebooks in a fully customizable environment, where dependencies and software requirements can be specified in a simple, standard way tied directly to the project.  For example, we have been able to use mybinder to provision notebooks for a classroom of 30 people in under 30 seconds, with only 5 minutes of setup and preparation.  Inadvertent experiments on Twitter have shown us that the current infrastructure can expand to handle hundreds of simultaneous users.  In effect, mybinder is a major step closer to helping us realize the promise of ubiquitous and frictionless computational narratives.

**What is the major related work in this field?**

I am  interested in (a) potentially anonymous execution of full workflows, (b) within a customizable compute environment, (c) with a robust, open source software infrastructure supporting the layer between the execution platform and the interactive environment.

There are a variety of hosting platforms for Jupyter Notebooks, but I am only aware of one that offers completely anonymous execution of notebooks - this is the tmpnb service provided by Rackspace, used to support a Nature demo of the notebook. Even more than mybinder, tmpnb enables an ecosystem of services because it lets users frictionlessly “spin up” an execution environment - for a powerful demo of this being used to support static execution, see https://betatim.github.io/posts/really-interactive-posts/. However, tmpnb doesn’t allow flexible configuration of the underlying execution environment, which prevents it from being used for more complex interactions in the same way as mybinder.

More generally, there are many projects that seek to make deployment and execution of Jupyter Notebooks straightforward. This includes JupyterHub, everware, thebe, Wakari, SageMathCloud, and Google Drive.  Apart from everware (which has significant overlap with mybinder in design) these other platforms are primarily designed around delivery of notebooks and collaboration within them, and do not provide the author-specified customization of the compute environment provided by mybinder via Docker containers.  That having been said, all of these are robust players within the Jupyter ecosystem and are building out tools and approaches that mybinder can take advantage of (and vice versa).

We have already discussed the proposed workshop informally with people from Jupyter, everware, and thebe, and anticipate inviting at least one team member from each project (as well as tmpnb).

Outside of the Jupyter ecosystem, the R world has a collection of software that I’m mostly unfamiliar with. This includes RStudio Server, an interactive execution environment for R that is accessed remotely over a Web interface, and Shiny, which allows users to serve R-based analyses to the Web. These compare well with Jupyter Notebook in features and functionality.  One goal of this workshop is to provide a common execution system to support these in the same way that mybinder supports Jupyter now, and to find out which R applications are the most appropriate ones to target. We will invite one or more members of the rOpenSci team to the workshop for exactly this purpose.

**Why is the proposer qualified?**

My major qualifications for hosting the workshop are as follows:

- Known (and “good”) actor in the open source world, with decades of dedication to open source and open science principles and community interaction.
- Official Jupyter evangelist, on good terms with everyone (so far as I know).
- Neutral player with respect to all of these projects.
- Teacher and trainer and designer of workshop materials for Jupyter notebooks, Docker, reproducible science, version control, and cloud computing.
- Affiliated with Software Carpentry and Data Carpentry, to help with delivery of training materials.
- Faculty at a major US university, with access to admin support and workshop space.
- Interest and some experience in fostering diverse communities (primarily from connections with Python Software Foundation and Software Carpentry).
- Technically capable of programming my way out of a paper bag.
- Located in California, to which people will enthusiastically travel in the winter months.
- One of the members and discussants of the ever pub #openscienceprize proposal, which explored related topics of executable publications in some detail (but was then rejected).

**What is the approach being taken?**

The approach is to run a cooperative hackathon/hackfest/workshop targeting a few specific objectives, but with flexibility to expand or change focus as determined by the participants.  The objectives are essentially as listed in my mybinder blog post (http://ivory.idyll.org/blog/2016-mybinder.html):

- hack on mybinder and develop APIs and tools to connect mybinder to other hosting platforms, both commercial (AWS, Azure, etc.) and academic (e.g. XSEDE/TACC);
- connect mybinder to other versioning sites, including bitbucket and gitlab.
- brainstorm and hack on ways to connect credentials to mybinder to support private repositories and for-pay compute.
- identify missing links and technologies that are needed to more fully realize the promise of mybinder and Jupyter notebook;
- identify overlaps and complementarity with existing projects that we can make use of;
- more integrated support for docker hub (and private hub) based images;
- brainstorm around blockers that prevent mybinder from being used for more data-intensive workflows;

About half of the invitations will be to projects that are involved in this area already (listed above, together with at least two people from the Freeman Lab, who develop mybinder). I also anticipate inviting at least one librarian (to bring the archivist and data librarian perspectives in) and one journalist (perhaps Jeffrey Perkel, who has written on these topics several times). The other half will be opened to applications from the open source and open science communities.

All outputs from the workshop will be made available under an Open Source license through github or another hosting platform (which is where the mybinder source is currently hosted). We will also provide a livestream from workshop presentations and discussions so that the larger community can participate.

**What will be the output from the project?**

In addition to source code, demonstrations, proofs of concept, etc., I anticipate several blog posts from different perspectives.  If we can identify an enthusiastic journalist we could also get an article out targeted at a broader audience. I also expect to develop (and deliver) training materials around any new functionality that emerges from this workshop.

**What is the justification for the amount of money requested?**

We anticipate fully supporting travel, room, and board for 15 people from this grant, although this number may increase or decrease depending on costs. We will also provides snacks and one restaurant dinner.  No compute costs or anything else is requested - we can support the remainder of the workshop hosting entirely out of our existing resources.

**What are the other sources of support?**

I expect to supplement travel and provide compute as needed out of my existing Moore DDD Investigator funding and my startup funds. However, no other support explicitly for this project is being requested.
