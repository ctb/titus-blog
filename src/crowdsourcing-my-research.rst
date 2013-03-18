Does anyone want to work on a hard research problem?
####################################################

:author: C\. Titus Brown
:tags: science,python,crowdsourcing
:date: 2013-03-18
:slug: crowdsourcing-my-research
:category: science

A week or two ago, I posted a crazy idea about crowdsourcing a
bioinformatics analysis pipeline.  I may still try to do that.
But in the meantime, here's another crazy idea.

First, some background.

People are hungry for hard and interesting problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I'm writing this as I fly back from PyCon 2013, where I hung
out with a lot of people who seemed to be looking for challenging
problems to tackle.  I trace this back to a general discontent with
solving problems like increasing the click rate on ads by 0.1%, as
well as the realization that once you are comfortable and settled and
making enough money, it's easy to get bored.

(Side note: we gave @hugs the TiP BoF award for a presentation on how
he's resolving this conflict for himself by teaming up with @dabeaz to
work on Maker stuff.)

I personally think a lot of these people should look into doing
research, but there are a few problems with that.  One is
that most PhD programs -- which I believe is by far the best route
to learning to do research -- have a residential requirement, require
~100% of your attention, and don't pay that well.  The second is that
a lot of PhD research is pretty abstract and appears irrelevant to the
real world, and it's hard to pick projects when you're not really
familiar with the area (a problem that new grad students have, too).
A third is that research virtually requires a close working
relationship with a small group of people, including someone who
knows the lay of the land around the topic of interest and can
serve as a guide.

More broadly, very few of these people even *want* a PhD. While I
think the problems with residential PhD programs could be solved, I
can't imagine that very many well-paid Python hackers want to quit
their job to get a PhD.  I'm skeptical that many companies would want
to pay for or donate their developers' time for 20-40 hours a week to
do a real PhD, too.

Is there a solution?

The Crazy Idea
~~~~~~~~~~~~~~

I have a few really hard data analysis problems to solve.  One of
them, infinite metagenome assembly, is reasonably nicely encapsulated
and bounded, and presents some interesting parallelism and data
structure challenges.  Moreover, we (me, my lab, and my collaborators)
have lots of sample data and understand the basic problem pretty well.
I submitted a grant on it, but in part because of straight up research
funding challenges, and also because of the sequester, I'm unlikely to
get the grant.  But we still need to solve the problem.  I've been
thinking of working on it myself, but I'm increasingly unable to put
in the time.

What if I crowdsourced the problem?

More specifically, what if I issued an open call for people to come
"play" with us on this problem?  I could set up a mailing list and an
`editable community doc project
<http://ivory.idyll.org/blog/rtd-comments-and-editing.html>`__, as
well as a repo with sample data sets and scripts and code (this is
`already available but not necessarily easy to work with <http://github.com/ged-lab/khmer>`__).
The goal would be to come up with a more detailed understanding of
the problem, whatever novel data structures and algorithms that
were needed, an implementation at scale, and a practical engineering
solution with empirically shown "good" scaling behavior.

A statement of the problem
~~~~~~~~~~~~~~~~~~~~~~~~~~

Imagine feeding the world's libraries into a paper shredder, mixing
the output thoroughly, and then digitizing the textual contents of the
shreds into strings (note that the process has errors, so each
character will have an associated likelihood that that individual
character is correct).

Now, reconstruct the source books by assembling the books "de novo",
just from the content of the strings.  Note a few important features:
most books will be present in multiple copies (so you can rely on
overlaps between the randomly fragmented strings); some books will be
more abundant than others (so you can separate out the string
fragments by abundance, potentially); and there will be different
editions of books, so you may have that complication (which may be
impossible to resolve 100% correctly).  This is also using a
restricted alphabet (A/C/G/T), note.

Implement an online streaming solution to this problem that can handle
arbitrarily large amounts of data.

For more more technical reading, see: `the grant proposal
<http://ged.msu.edu/downloads/2012-career-nsf-final.pdf>`__, `a stupid
attempt to explain the problem
<http://ivory.idyll.org/blog/the-mad-photocopier.html>`__, and `UMD's
assembly primer
<http://www.cbcb.umd.edu/research/assembly_primer.shtml>`__.

How would this work?
~~~~~~~~~~~~~~~~~~~~

The goal would be to work collectively towards a solution that was
well characterized, well implemented, and effective.  I'd expect
1-2 years (but, if you think you're super smart, prove me wrong!!)

We would build out a basic documentation site with a statement of the
problem, some tutorials to make use of existing tools, and some test
data sets, all on github.  We'd also set up a mailing list of some
sort, and I'd commit to real interaction on the mailing list.

People who wanted to participate in the project would join the list
and bash on problems cooperatively or coopetitively.  Technical
discussion would occur on the list, and I would encourage people to
post summaries of on-list discussions and detailed potential solutions
or thoughts on their own blogs, and then link them back to the
documentation Web site.  We could describe failures in gross detail,
to make sure that people knew which paths had been explored.

Everyone would be welcome to work on the problem in isolation,
and since the data sets are all public and there's no IP or licensing
problems with our current products, anyone could publish or use the
materials, either.  I'd probably write up a quick paper describing
the challenge and post it on arXiv, where it could be cited; the
only requirement I would have is that you cite that paper when
publishing.

People who worked closely with me and my group would, at the least,
be co-authors on any publication that arose, and the git repo
history and mailing list would serve as a history of intellectual
and technical provenance.

Compute resources would be DIY, although for people who got involved
enough I could supply access to more significant compute resources
as needed.  We could probably inveigle cloud providers to contribute
resources for benchmarking and reputational purposes, too.

We'd probably need some mailing list rules to avoid trolls and people
who wanted to argue about the problem rather than work on the problem,
but I think slightly modified mailing list rules together with a
self-confident project BDFL (yo!) would suffice.

What are the incentives?
~~~~~~~~~~~~~~~~~~~~~~~~

Why would anyone participate?

Non-academic participants would get:

 - the fun of solving a hard problem

 - contributing to an advance in human knowledge, however small;

 - major props in a tiny, irrelevant community;

 - co-authorship (see above);

 - training in biology lingo;

 - an entree to a whole world of other interesting problems

Academic participants would get basically the same thing, although
presumably co-authorship would be a tad more relevant to them.

What do I get?

 - a reputational boost for trying something cool and being open about it;

 - potentially a solution to a really annoying problem that is standing in
   the way of my collaborators' research;

 - another publication;

 - interaction with a bunch of potentially really cool people;

 - did I mention a solution?

Is there more in it for me?  Not really -- I don't get paid based on
problems solved, so the most I would get is the reputational boost and
the publication.  IP and code licensing for anyone participating in the
core cooperative project would need to be open, so I can't swipe your
cool solution and sell it.

Other misc points
~~~~~~~~~~~~~~~~~

Depending on how things worked out, I can see this solving lots of
sub problems in genome and transcriptome and metatranscriptome
analysis.

I'd propose minimizing code churn for cleanup's sake -- our code isn't
that awesome necessarily, but I would want to see people working on the
problem itself rather than on the epiphenomena.

All our code is written in Python and C++.  You can work in (e.g.) Ruby
if you want, but you're going to have to rewrite a lot.

I'd welcome other research groups, provided they cite the paper in
anything that comes out of it, and, if I/we contribute intellectually,
mark it as a collaboration under the usual rules.  In other words,
the mailing list isn't a free source of publishable ideas -- you have
to *gasp* put the names of people on it.  But honestly I'd rather see
a solution than my name on a paper ;).

Victory and max props can only be claimed with a real, implemented
solution.  We appreciate that you have special insight into a simple
theoretical solution, and want to leave the implementation details
to the software engineering plebes, but no, I'm not interested,
thankyouverymuch.

Is this a novel approach to doing research?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I don't think it is, particularly, although I think trying to involve
bored software engineers in a real research problem is not that
common.  I'm certainly aware of the `Polymath Project
<http://polymathprojects.org/>`__ and `Zooniverse
<https://www.zooniverse.org/>`__ projects which have been really
effective at crowdsourcing research problems.  More generally, I
really enjoyed `Michael Nielsen's
<http://michaelnielsen.org/blog/michael-a-nielsen/>`__ book,
`Reinventing Discovery: The New Era of Networked Science
<http://michaelnielsen.org/blog/reinventing-discovery/>`__ which is
about this kind of stuff.

If there's anything novel about this, it's that I think it's a nicely
packaged problem that can be explored by people with computing intuition
but not a huge amount of biology specific background.  But who cares?
It's a problem I think needs to be solved.

What's next?
~~~~~~~~~~~~

I guess the first question is, should I bother?  I could throw a
project and have nobody come.  It's a reasonably big chunk of time and
effort to set this kind of thing up, and I have no idea if there'd be
any real enthusiasm out there.  On the flip side, it'd be a useful
academic adventure anyway, since we generally lack good (hard, nasty)
benchmarking data sets for metagenome assembly and analysis, and I can
definitely provide some.

Another question is, is anyone out there willing to really work on
such a hard problem?  In fact, I'd bet it's too hard for anyone but an
academic researcher to solve... :)

I'll sit on it for a bit and think about it some more.  Any
suggestions or comments for making it more attractive as a project, or
more interesting, would be welcome.

--titus
