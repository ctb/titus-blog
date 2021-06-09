Title: Moving sourmash towards more community engagement - a funding application
Date: 2021-06-09
Category: science
Tags: sourmash, software, czi
Slug: 2021-sourmash-czi-application
Authors: C. Titus Brown
Summary: CZI EOSS4 application for sourmash support

We applied for funding from CZI for sourmash a few weeks back, via the [Essential Open Source Software for Science](https://chanzuckerberg.com/eoss/) program. Here's the core of the application (lightly edited).

(We'll hear about funding by end of September, I believe.)

Feedback welcome, unless you're alerting me to the presence of typos :)

## Proposal details

We seek funding for maintenance and user support for the sourmash software, while embarking on an ambitious plan to improve sustainability through improved governance, enhanced inclusivity, and robust community engagement.

## Short description of software project:

Sourmash is mature software that enables lightweight content search, comparison and classification of microbial genomes and metagenomes. Sourmash works in low memory with compact databases, supports both NCBI and GTDB taxonomies, and can operate on private collections of genomes and metagenomes. The release of v4.1 brings massive-scale search of all Genbank microbial genomes and all public metagenomes to commodity hardware. These features are underpinned by novel data structures and algorithms, including an extension of MinHash that supports containment and the use of min-set-cov to do highly accurate metagenome analysis. Sourmash serves as a robust, reliable, and performant backbone for microbial sequence analysis.

We use development practices based on 30 years of scientific software engineering expertise: we develop in the open, do code review, have tests with 90%+ line coverage, and have a robust release process with semantic versioning. We provide thorough documentation, engage with users via our issue tracker, and use social media to broadcast new features and use cases. The utility of sourmash has been recognized by both users and funding agencies: we are increasingly well cited, the NSF is supporting the development of flexible taxonomies and distant evolutionary classification via protein k-mers, and the NIH is supporting iHMP reanalysis.

## Proposal Summary

Sourmash is mature software that serves as a stable component of sequence analysis workflows, a fast and lightweight tool for massive-scale search of public and private sequence databases, and a platform for novel data structure and algorithm exploration. Sourmash is explicitly designed to meet the computational needs created by the massive expansion of sequencing capacity in microbiome biology.

We have arrived at an important crossroads with sourmash. We are just now releasing mature support for petabase-scale content search (v4.1.x and v4.2), and are currently writing up our novel data structures and algorithms for publication. We have ongoing projects using sourmash to analyze Human Microbiome Project datasets, including discovering strain-specific markers of Inflammatory Bowel Disease. Simultaneously, grant support for the core development of sourmash is ending, and Dr. Luiz Irber, the core developer behind most of the scaling work, is moving to another job where sourmash will become his part-time project. While sourmash research development will continue, we have no way to robustly support our current user base and grow the developer community with traditional funding, and do not have the governance infrastructure to productively engage with other support mechanisms.

We request support from CZI to support our newly released features with continued sourmash core development, while working toward sustainability by growing the project out of the lab and into the community. We propose to use the period to expand the sourmash community, define and grow a governance framework, connect to the Python and Rust bioinformatics ecosystem, and train both biologists and bioinformaticians to better engage with open source bioinformatics software. In particular, we see an opportunity to use sourmash to provide one example of how to grow a small project based in a single lab into a more sustainable community-based project. Importantly, this kind of maintenance and community growth does not fall within the scope of traditional funding opportunities.

At the end of this two year period, we will have continued to release and support high performance, high impact software. We will also have expanded our developer and user community, chosen a governance framework, identified a fiscal sponsorship plan, and published our strategies for project growth and sustainability.

                                         
## Work Plan


### Software development activities:

We propose to follow a “python-dev” model in which maintenance and feature releases proceed on their own timeline, while the roadmap process coordinates the planning and development of related feature sets (e.g. taxonomy extensions and database formats are connected). This separates maintenance updates from the “slow science” process of developing, testing, and evaluating new functionality against scientific use cases, while also ensuring that fully baked new functionality does regularly get released. Software development will proceed under our current “async” model, in which all decisions are discussed and documented openly in GitHub. 

Fully 50% of the funded effort on this proposal goes to the “maintenance mode” activities, which are intended to further regularize the development process and support iterative, gradual performance improvement while preventing feature and performance regressions. This will include regular releases, continued maintenance of and improvements to software development and release process, database updates and releases as new genomes and metagenomes are made public, regular JOSS publications on major new versions (v4, v5, etc.), structural improvements to sourmash core, including a plugin architecture for storage formats, new command-line subcommands, and visualizations, and sketch serialization documentation and format upgrades to store more metadata, and support higher-performance binary formats.

### Community engagement activities:

The community engagement activities below seek to build, grow, and support an active and robust user and developer community that includes biologists, bioinformaticians, computer scientists, and software engineers.

As sourmash matured, we focused our efforts toward building sustainable software and developing advanced use cases within the lab first, with documentation for new users added via github issues, blog posts, and feature papers. However, this has resulted in somewhat uneven support resources: e.g. we lack intermediate-level tutorials helping users transition from our introductory tutorials to advanced use cases or python API usage. We will upgrade our documentation systematically, create a “recipes” site, and construct an FAQ section that is well integrated with the documentation by reorganizing and amending existing content.

We plan to  provide a warm, welcoming community forum that encourages new user questions and contributions. This will require engaged moderators, a strong Code of Conduct process, and a large user base, which we have not had the bandwidth to support previously. A key outcome of this funding will be the clear definition of a single support forum for sourmash, as one of the first outputs of our governance process.

Contributors may come from both the user community and the broader bioinformatics/CS community. We routinely source use cases, ideas for new functionality, and requests for performance improvement from the current biology-focused user community, and will encourage deeper and broader contributions through our governance and contributor framework, discussed below.

Similarly, there are many implementation aspects of sourmash that are interesting to, and may provide fodder for, CS and software engineers who are interested in contributing to bioinformatics software. While this is supported within the lab, these challenges are not immediately obvious or accessible to others without some biological background and appropriate documentation. We will build tutorials and documentation that highlight the algorithmic and implementation aspects of sourmash (sketching approximations, scaling issues, indexing formats, performance benchmarking, and quality-of-result benchmarking) and provide guidance for CS researchers who wish to evaluate new algorithms. Our governance and contributor framework will welcome extensions and evaluations and require neither permission nor involvement from sourmash core.

We see great value in further broadening our contributor base, and will continue to improve our current support for first-time OSS contributors by expanding our new contributor issue labels beyond  “good first issue”, “good next issue”, and “repeatable quest”. While we do not expect many of these contributors to become long-term sourmash contributors, some may; more importantly, a steady influx of new first-time contributors will ensure that our development documentation remains accurate and useful. In support of this effort, we have budgeted for two 10 hrs/wk undergraduates to continue to contribute. We will also offer first-time contributor collaboratives, run documentation and visualization improvement hackyfests, and contribute to hackathons at BOSC and PyCon.

### Governance activities:

We will build a Steering Council that guides governance, defines contributor guidelines, authorship considerations, and oversees the roadmap process. As part of this, we will nucleate “sourmash.bio” and move development activities out of the dib-lab organization. The Steering Council will also define the scope of the project and outline contribution mechanisms, most likely via a fiscal sponsor (perhaps the Software Freedom Conservancy).


## Milestones and Deliverables:

We will deliver regular releases of sourmash under semantic versioning, per http://ivory.idyll.org/blog/2021-sourmash-v4-released.html. We anticipate approximately quarterly releases of major.minor versions, with more frequent patch releases.

We will quarterly update our roadmaps for v4.2.x, v5, and beyond. All planned features for these versions are discussed in the issue tracker. Each minor release will feature a link to updated roadmaps for the coming features. The issue tracker will continue to be constantly updated and refined in conjunction with releases and roadmaps.

These releases will also see regular refinement and updates of both the Python layer and the Rust layer; a major goal of our project is to expand our Rust contributor pool via CS undergrads and also (potentially) engagement with rust-bio.

We will simultaneously engage in iterative refactoring of our documentation to include not just getting-started docs and tutorials, but also detailed guidelines on how to get started contributing, video guides to sourmash, a “recipe” site that outlines solutions to common use cases, developer-oriented documentation for new plugins and visualizations, and a CS-focused introduction to the problems that sourmash is tackling. Recipes will be in place by mid-2022 and major updates will be delivered on a semi-annual basis.

Each summer (2022 and 2023) we will participate in undergraduate research projects (e.g. the National Summer Undergraduate Research Program) and introduce biology and CS undergraduates to problems in microbial genomics and metagenomics, including but not limited to sourmash. We will also participate in summer training courses (STAMPS at MBL, and DIBSI at UC Davis) as was our usual pre-pandemic practice (2010-2019).

We will offer at least two webinars and four hackfests annually, with our focus varied between attracting new users, attracting new developers, refining our documentation, exploring new functionality and improving our UX, and highlighting new analysis opportunities.

In December of 2021, 2022, and 2023 we will provide a detailed update of our governance progress and future plans. By December 2021, we will have issued invitations to a Steering Council, and begun the process of holding quarterly meetings. By December 2022, we will have engaged with potential fiscal sponsors and identified a path forward.

By mid-2022, we will have designated and seeded a support forum for sourmash.

While this will not be supported by this proposal specifically, we will also have submitted two papers on sourmash by December 2021.

In terms of metrics,
* We will have engaged with over 1000 new users via hackyfests, webinars, etc. as a direct result of CZI funding.
* Our stretch goal is over 500 citations combined for sourmash core papers by Dec 2023.
* We hope to be the “stable, boring” option for petabase-scale content search and expect to have seen a substantial growth in user support and functionality requests for these use cases.
* We also expect to see a dozen or more 3rd party extension modules adding new format import/export and visualizations to sourmash.
* We will have submitted at least two major releases (v4 and v5) to JOSS, one in 2021 and one by end of 2023.

## Value to Biomedical Users:

As the biomedical field increasingly moves towards large-scale sequencing, both of single genomes (e.g. individuals) and metagenomes (e.g. gut microbiome), lightweight analysis tools are becoming an essential part of core biomedical treatment and research. Sourmash provides a lightweight and robust interface for these analyses. In particular, we note four of our well-developed applications have considerable biomedical relevance for sequencing data analysis generally, and microbiome work specifically:

(1) finding the minimal list of relevant genomes for a microbiome, from all available (800k+) microbial and viral genomes;

(2) searching all microbiome data sets for a specific genome;

(3) detecting and removing contamination in metagenome, genome and transcriptome data sets;

(4) extraction of annotation independent features to support machine learning.

These applications are already under active use for large-scale biomedical data: the NIH has provided short-term funding to Dr. Brown in support of applying sourmash systematically to the Human Microbiome Project data sets, and we have an ongoing project using sourmash to discover strain-specific markers of Inflammatory Bowel Disease using a random forest approach.

Beyond the technical aspects of sourmash, we will work towards being a good example of a scientific open source project in biology/bioinformatics, by intentionally moving towards community governance, rewarding a wide variety of contributions, providing use-case focused tutorials, and guiding sourmash users towards how to support and evolve sourmash.

## Diversity, Equity, and Inclusion Statement:

We believe that social barriers to contribution are a major cause of the low diversity in scientific OSS, and we are committed to systematically lowering these barriers while also lifting contributors over these barriers.

We also believe that lightweight and robust methods that support large-scale data discovery and reuse can expand bioinformatics into the “lightly resourced” space, e.g. Primarily Undergraduate Institutions; this is an equity issue because so many current methods require substantial resources simply to get started.

Training modules at the DIBSI and STAMPS workshops will introduce sourmash to a diverse range of research-focused participants. NSURP is focused on undergraduates from underrepresented backgrounds, and in 2020 we hosted two Latinx undergraduates. UC Davis is also an HSI and our undergraduate researchers will be recruited with attention to diversity.

We need a stronger CoC response framework, both for forum moderation and for project contributors; currently, the CoC process is based on the BDFL model, which is inadequate. This is important for DEI and antiracism, and improving our CoC process is one of our main goals in finding a fiscal sponsor who can provide a larger framework within which we can operate.

Last but not least, we believe that providing authorship for all contributors, including those who contribute use cases, recipes, and documentation, provides a way to formally recognize contributions that are traditionally undervalued in both open source projects and academia. Recognizing this kind of “invisible labor” is fundamentally an equity issue.
