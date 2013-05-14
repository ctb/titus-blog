The Cost of Open Science
########################

:author: C\. Titus Brown
:tags: science, open science
:date: 2013-05-13
:slug: the-cost-of-open-science
:category: science

I just finished reading `The Immortal Life of Henrietta Lacks
<http://www.amazon.com/Immortal-Life-Henrietta-Lacks/dp/1400052181>`__,
an excellent book about the HeLa cell line cultured from cancerous
cells taken from Henrietta Lacks.  In addition to raising some really
interesting and astonishing questions about the appropriate (mis)use
of patients' tissue samples, a section about George Gey caught my eye
and made me think about some of the challenges associated with open
science.

`George Gey <http://en.wikipedia.org/wiki/George_Otto_Gey>`__ was the
immensely creative scientist who developed a host of cell-culture
techniques, some of which he applied to the cells taken from Henrietta
Lacks.  The quick spread of HeLa cells amongst scientists, which
helped drive their adoption as a standard biological reagent across
biomedical science, was due largely to his decision to make them
freely available upon request.  Since the HeLa cells were
self-replicating, and, moreover, easy to culture, they were quickly
communicated from scientist to scientist.  This let HeLa be used (for
one example) to help `cure polio
<http://fyb.umd.edu/2011/polio.html>`__.

George Gey never really reaped any rewards from HeLa, other than some
reputational rewards.  In the Immortal Life book, Rebecca Skloot says
that he somewhat regretted his generosity, as he watched other
scientists publish experiments that he'd casually done in his own lab
and never bothered to publish.  Yet it is without a doubt that his
decision to make the HeLa cells freely available to others advanced
science tremendously.

This kind of thing is one of the hidden "costs" of open science -- the
cost of pushing science forward as a whole, sometimes at the expense
of one's own career -- and something I'm watching happen with some of
our software approaches.  I'm being asked with increasing frequency to
review papers that extend some of our approaches (especially `diginorm
<http://ged.msu.edu/papers/2012-diginorm/>`__) and while it's really
exciting to see people building on our work, it's also bittersweet,
because we could have done some of this stuff quite easily ourselves,
and (the dogma goes) more publications is better.  If we'd sat on our
code and eked as many publications as possible out of it, we'd
probably be in a better position with respect to a monopoly on certain
kinds of sequence analysis.  But it's also clear that (IMNSHO) some
sequence analysis would be a harder -- the most obvious example is
`Trinity's inclusion of a diginorm-inspired approach
<http://ivory.idyll.org/blog/trinity-in-silico-normalize.html>`__.  I
think we did the right thing, but it's hard to convey this to the
people in charge of convincing MSU to retain me, and I'm not sure too
many granting agencies care, either.

The obvious conflict here is that the incentives in science careers
reward one kind of action -- selfishness -- while progress in science
itself depends on a different kind of action -- a certain amount of
selflessness. Us open science advocates really need to figure out how
to incentivize this better at both an institutional level and at a
granting level.  Lots is being done in this area, including the recent
`expansion of NSF-style CVs to include the broader category of
research outputs
<http://datapub.cdlib.org/data-to-receive-recognition-from-nsf/>`__,
but more needs to be done.  Until it becomes an obvious career win to
share, most people won't.

The hidden cost of potential commercialization
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While we're on the topic of sharing, let's talk about the `Bayh-Dole
Act <http://en.wikipedia.org/wiki/Bayh%E2%80%93Dole_Act>`__, which
encourages recipients of federal funding to pursue commercialization
of inventions.  This is probably a naive statement on my part - and I
welcome corrections -- but I think this is probably the most damaging
legislative act ever perpetrated on open science, and one of the most
damaging acts to progress in science, specifically.

Why?  Because everyone thinks they can get rich off of their research
work, and pursue their stovepiped research instead of broadly sharing
it.  This hits both experimentalists and computationalists.  One
friend who works at a small biotech firm tells me that they have tried
and failed to get access to mouse lines to test a potential therapy;
the other researchers simply won't share, and the cost of hammering
out a formal legal agreement about potential commercialization profits
is worth more than the expected payoff for any given therapy.  Plenty
of people seem to think they're going to get rich off of their
software, and either delay opening it up or prevent commercial users
without an explicit license; more damaging, they block remixing of the
software and algorithms with other systems or approaches so as to
retain intellectual ownership.

I'm sure there are realms where this makes financial sense, but I betcha
it also blocks a lot of forward progress by limiting the relevance of
individual research.

And remember, if George Gey had restricted distribution of HeLa cells,
it is inarguable that science would have been impeded.

The central paradox of open science
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

What I find most frustrating about open science is that while most
funding organizations are coming to see it as a way to better leverage
their funding, and the Internet provides an increasingly excellent
environment for `collaborating on and remixing research
<http://ivory.idyll.org/blog/idea-factory-internet.html>`__, it's
still not making it down to the institutional level.  There is
virtually no pressure, no interest, and no action on opening up the
products of research at the university level.  I can't tell why,
exactly, except that it seems to be driven by a general lack of
incentives -- i.e. virtually no one sees it to be in their interest.
I can't tell if this is short-term thinking, or rational economic
thinking, or what.

In the specific realm of biology and software, I think there's a
strong argument to be made that `the future belongs to those who try
to build good software
<http://ivory.idyll.org/blog/research-software-reuse.html>`__.  I hope
so. But I'm getting tired of the slow pace, and I'm not sure how to
accelerate things -- discussion and ideas `here
<http://ivory.idyll.org/blog/w4s-overview.html>`__.  (I hope to have
some good news on this front in a few weeks, BTW.)

I can tell you that my career has already been immeasurably improved
by my openness, including posting our software, writing blogs, and engaging
with people on twitter.  But I don't know how to convey this as a systematic
approach, and I'm not sure it *is* something that's viable for many kinds
of resarch.

I would welcome a stronger conclusion, but this is all I have.  More
thoughts welcome ;).

--titus
