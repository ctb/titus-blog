Data implies software.
######################

:author: C\. Titus Brown
:tags: futurepaper, data reuse
:date: 2017-01-08
:slug: 2017-data-implies-software
:category: science

Note: This is the second post in a mini-series of blog posts inspired
by the workshop `Envisioning the Scientific Paper of the Future
<http://caltech.stacksdiscovery.org/scientific-paper-future>`__.

An important yet rarely articulated assumption of a lot of my work in
biological data analysis is that **data implies software**: it's not
much good gathering data if you don't have the ability to analyze it.

For some data, spreadsheet software is good enough.  This was the situation
molecular biology was in up until the early 2000s - sure, we'd get numbers
from instruments and sequences from sequencers, but they'd all fit pretty
handily in whatever software we had lying around.

Once numerical data sets get big enough -- e.g. I did approximately
50,000 qPCRs in my last two years of grad school, which was unpleasant
to handle in Excel -- we need to invest in software like R or Python,
which can do bulk and batch processing of the data.  Software like
`OpenRefine <http://openrefine.org/>`__ can also help with "manual" cleaning
and rationalization of the data.  But this requires skills that
are still relatively specialized.

For other data, we need custom software built specifically for that
data type.  This is true of sequence analysis, where most of my work
is focused: when you get 200m DNA sequences, each of length 150 bp,
there's no simple, effective way to query or summarize that using general
computational tools.  We need specialized code to parse, summarize,
explore, and investigate these data sets.  Using this code doesn't
necessarily require serious programming knowledge, but data analysts
may need fortitude in dealing with potentially immature software, as well
as a duct-tape mentality in terms of tying together software that
wasn't designed to integrate, or repurposing software that was meant for
a different purpose.

There is at least one other category of data analysis software that I
can think of but haven't personally experienced - that's the kind of
stuff that CERN and Facebook and Google have to deal with, where the
data sets are so overwhelmingly large that you need to build deep
software and hardware infrastructure to handle them.  This becomes (I
think) more a matter of systems engineering than anything else, but I
bet there is a really strong domain knowledge component that is required
of at least some of the systems engineers here.  I think some of the
cancer sequencing folk are close to this stage, judging from a talk I heard
from Lincoln Stein two years ago.

Data-intensive research increasingly lives beyond the "spreadsheet" level
-------------------------------------------------------------------------

As data set sizes increase across the board, researchers are
increasingly finding that spreadsheets are insufficient.  This is for
all the reasons articulated `in the Data Carpentry spreadsheet lesson
<http://www.datacarpentry.org/spreadsheet-ecology-lesson/00-intro.html>`__,
so I won't belabor the point any more, but what does this mean for us?

So increasingly our analysis results don't depend on spreadsheets;
they depend on custom data processing scripts (in R, MATLAB, Python,
etc.)  and other people's programs (e.g. in bioinformatics, mappers
and assemblers) and on multiple steps of data handling, cleaning,
summation, integration, analysis and summarization.

And, as is nicely laid out in `Stodden et al. (2016)
<http://science.sciencemag.org/content/354/6317/1240>`__, all of these
steps are critical components of the data interpretation and belong in
the Methods section of any publication!

What's your point, Dr. Brown?
-----------------------------

When we talk about "the scientific paper of the future", one of the facets
that people are most excited about - and I think this Caltech panel
will probably focus on this facet - is that we now possess the technology
to readily and easily communicate the details of this data analysis.
Not only that, we can communicate it in such a way that it becomes
repeatable and explorable and remixable, using virtual environments and
data analysis notebooks.

I want to highlight something else, though.

When I read excellent papers on research data management like `"10
aspects of highly effective research data"
<https://www.elsevier.com/connect/10-aspects-of-highly-effective-research-data>`__
(or is this a blog post? `I can't always tell any more
<http://ivory.idyll.org/blog/2017-top-ten-reasons-blog-posts.html>`__),
I falter at section headings that say data should be "comprehensible"
and "reviewed" and especially "reusable".  This is not because they
are incorrect, but rather because these are *so* dependent on having
methods (i.e. software) to actually *analyze* the data. And that
software seems to be secondary for many data-focused folk.

For me, however, they are one and the same.

If I don't have access to software customized to deal with the
data-type specific nuances of *this* data set (e.g. `batch effects of
RNAseq data <https://f1000research.com/articles/4-121/v1>`__), the data
set is much less useful.

If I don't know exactly what statistical cutoffs were used to extract
information from this data set by others, then the data set is much less
useful.  (I can make my own determination as to whether those cutoffs
were *good* cutoffs, but if I don't know what they were, I'm stuck.)

If I don't have access to the custom software that was used in
removing noise, generated the interim results, and did the large-scale
data processing, I may not even be able to approximate the same final
results.

Where does this leave me?  I think:

Archived data has diminished utility if we do not have the ability to
analyze it; for most data, this means we need software.

For each data set, we should aim to have at least one fully
articulated data processing pipeline (that takes us from data to
results). Preferably, this would be linked to the data somehow.

What I'm most excited about when it comes to the scientific paper of
the future is that most visions for it offer an opportunity to do
exactly this! In the future, we will increasingly attach detailed (and
automated and executable) methods to new data sets.  And along with
driving better (more repeatable) science, this will drive better data
reuse and better methods development, and thereby accelerate science
overall.

Fini.

--titus

p.s. For a recent bioinformatics effort in enabling large-scale data
reuse, see `"The Lair" <https://pachterlab.github.io/lair/>`__ from
the Pachter Lab.

p.p.s. No, I did not attempt to analyze 50,000 qPCRs in a spreadsheet.
...but others in the lab did.
