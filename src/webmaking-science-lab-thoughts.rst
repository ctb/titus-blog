Enabling dynamic, online data-driven narratives
###############################################

:author: C\. Titus Brown
:tags: open science,webmaking, w4s
:date: 2013-01-29
:slug: webmaking-science-lab-thoughts
:category: science
:status: draft


I've been chatting with people at Mozilla about their new Webmaking
Science Lab, at the intersection of "webmaking" and "science".  While
it's blazingly obvious that science can benefit from the Web; what's
been less clear to me is how the Web can benefit from science, and
this is the question that Moz folk have been asking me about.

The question is actually a bit more specific: it's not "how, in
theory, could science do things for the Web", but rather, "how,
intentionally, can we use science and scientists to do things for the
Web."  The big distinction is "intentionally" -- there's no question
that science has impacted the Web, with one dead obvious example being
`the invention of HTTP itself
<http://en.wikipedia.org/wiki/Tim_Berners-Lee>`__.  But I'm pretty
sure far more ideas from science and academic research have failed to
have an impact on the Web than have succeeded.

Part of the problem is that academic ideas often impact only a small
audience -- in the words of Michael Stonebraker at XLDB 2012, science
is a $0 billion industry, and it's also notoriously hard to
intentionally translate scientific advances into societally impactful
results -- this is `something that Bell Labs was really good at
<http://ivory.idyll.org/blog/idea-factory-internet.html>`__.  The
continuing brain drain of academic computer scientists into industry
suggests that, at least on the software and infrastructure side,
academic research doesn't have much to offer industry: all the
interesting problems are Web scale, and it's hard to compete with
Amazon, Google, Microsoft, Facebook, etc.

I think there *is* one thing that academics are more practiced at than
almost anyone else, though: telling stories that are carefully backed
with models and data.  These stories are generally formalized in
publications, and/or narrated in talks, but they almost always
integrate some form of data -- qualitative or quantitative
observations -- with some form of conceptual or quantitative model.

I think Mozilla could have a real impact here by combining technology
that already exists for telling stories with data and models,
providing a collaboration platform that enables github-style
collaboration, and publicizing/advocating/training people in how to
make use of it.

I sort of banged on this idea in my `'tech wanted' post
<http://ivory.idyll.org/blog/w4s-tech-wanted.html>`__, items #2
(posting/hosting ipython notebooks in a forkable environment), #3
(adding a storify-like interface to it), and sort of #4 (posting such
things to figshare-like places so that they are archived and static).
At the time I was thinking that this would make a dandy system for
beyond-the-PDF-style executable papers; what I didn't really think
about much, though, is that, with sufficient polish and ease of use,
it *also* makes a dandy system for citizen journalism and citizen
science in the form of data- and model-driven story telling.

Imagine, for example, that someone in NY City builds a model that
combines topographical map data with projected storm surges to
figure out if their neighborhood is likely to flood (and how much).
And then someone down in New Jersey adapts that "story" to their own
neighborhood, and sends it to their neighbors, who can tweak the
confidence intervals on flood surges to see if their particular house
is in danger?

Or imagine that someone takes the data and analysis pipeline from `this analysis of women's contributions to literature <http://www.theawl.com/2013/01/goodbye-anecdotes-the-age-of-big-data-demands-real-criticism>`__, and 

There's a growing recognition that not only is open data important, but open
*process* is important as well -- and for both science and data journalism,
a key part of this process is the way in which data is processed, analyzed,
modeled, and used to support conclusions.  Right now, I can't think of any
good systems that can do this.

But if you combine the ideas and ethos of ipython notebook, figshare,
ifttt, storify, and github, you can come pretty close.  You can build
a process in a notebook, share it via github, edit and modify it via
storify, integrate new processes and data with ifttt, provide
on-demand computing via a cloud service, and "publish" the whole
shebang via something like figshare.  It's just not very easy yet.

of.  The pieces *kind* of exist, but figuring out where the
integration points are or need to be, linking services together,
providing underlying links to data and compute capacity, and developing
both use cases and *users*, is a lot of work.

This kind of system would be of immense use in science, where issues
around reproducibility gets lots of press, but `remixing
<http://ivory.idyll.org/blog/research-software-reuse.html>`__ is less
well appreciated.  As Deepak Singh argues, `we need to think about
programmable data
<http://blog.deepaksingh.net/on-reproducibility/>`__.

Crucially, it would also enable `scientific translators
<http://mathbabe.org/2012/12/30/on-trusting-experts-climate-change-research-and-scientific-translators/>`__,
in which collaborations between scientists (who provide data and
pipeline) and journalists (who poke, combine, tweak, etc analyses) to
build a particular story, can merge into non-experts working with the
data and mashing it up with other data pipelines.

Perhaps I'm just an idealist, but I feel like being able to compare and
cross-link the same or similar data but from different sources would
really help pinpoint where bias is emerging, error is present, or dishonest
actors are acting.

This kind of executable data analysis pipeline also links into the
super awesome burgeoning `"citizen science" movement <http://www.scientificamerican.com/article.cfm?id=public-participation-research-back-in-vogue-ascent-citizen-science&page=4>`__.

Interestingly, this also ties into one of the big unsolved problems in
`Software Carpentry <http://software-carpentry.org>`__, in which we
have been unable to think of a way to enable scientists to effectively
build Web sites!  If Mozilla can provide or nucleate the development
of not only interfaces but also reasonably robust `service mechanisms
<http://ivory.idyll.org/blog/software-architecture-for-heterogeneous-data-integration.html>`__
for publishing data, then it may provide a solution to the Software
Carpentry problem.

At its heart, I'm arguing for the decentralization of data-driven story
telling via a robust set of open APIs and services for publishing, forking,
and modifying such stories.

