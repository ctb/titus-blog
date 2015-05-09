More on scientific software
###########################

:author: C\. Titus Brown
:tags: sustainability, software citation
:date: 2015-04-24
:slug: 2015-more-on-software
:category: science

So I wrote `this thing
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html>`__
that got an awful lot of comments, many telling me that I'm just plain
wrong.  I think it's impossible to respond comprehensively :).  But here
are some responses.

What is, what could be, and what should be
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In that blog post, I argued that software shouldn't be considered a
primary output of scientific research.  But I completely failed to
articulate a distinction between what we do today with respect to
scientific software, what we could be doing in the not-so-distant
future, and what we *should* be doing.  Worse, I mixed them all up!

----

Peer reviewed publications and grants are the current coin of the
realm.  When we submit papers and grants for peer review, we have to
deal with what those reviewers think right now.  In bioinformatics,
this largely means papers get evaluated on their perceived novelty and
impact (even in impact-blind journals).  Software papers are generally
evaluated poorly on these metrics, so it's hard to publish
bioinformatics software papers in visible places, and it's hard to
argue in grants to the NIH (and most of the biology-focused NSF) that
pure software development efforts are worthwhile.  This is what *is*,
and it makes it hard for methods+software research to get publications
and funding.

----

Assuming that you agree that methods+software research is important in
bioinformatics, what could we be doing in the near distant future to
boost the visibility of methods+software?  Giving DOIs to software is
one way to accrue credit to software that is highly used, but
citations take a long time to pile up, reviewers won't know what to
expect in terms of numbers (50 citations? is that a lot?), and my
guess is that they will be poorly valued in important situations like
funding and advancement.  It's an honorable attempt to hack the system
and software DOIs are great for other purposes, but I'm not optimistic
about their near- or middle-term impact.

We could also start to articulate values and perspectives to guide
reviewers and granting systems.  And this is what I'd like to do.  But
first, let me rant a bit.

I think people underestimate the hidden mass in the scientific
iceberg.  Huge amounts of money are spent on research, and I would bet
that there are at least twenty thousand PI-level researchers around
the world in biology.  In biology-related fields, any of these people
may be called upon to review your grant or your paper, and their
opinions will largely be, well, their own.  To get published, funded,
or promoted, you need to convince some committee containing these
smart and opinionated researchers that what you're doing is both
novel and impactful.  To do that, you have to appeal largely to values
and beliefs that they already hold.

Moreover, this set of researchers - largely made of people who have
reached tenured professor status - sits on editorial boards, funding
agency panels, and tenure and promotion committees.  None of these
boards and funding panels exist in a vacuum, and while to some extent
program managers can push in certain directions, they are ultimately
beholden to the priorities of the funding agency, which are (in the
best case) channeled from senior scientists.

If you wonder why open access took so damn long to happen, this is one
reason - the cultural "mass" of researchers that needs to shift their
opinions is huge and unwieldy and resistant to change.  And they are
largely invisible, and subject to only limited persuasion.

One of the most valuable efforts we can make is to explore what we
*should* be doing, and place it on a logical and sensical footing, and
put it out there.  For example, check out `the CRA's memo on best
practices in Promotion and Tenure of Interdisciplinary Faculty
<http://cra.org/resources/bp-view/best_practices_memo_promotion_and_tenure_of_interdisciplinary_faculty/>`__
- great and thoughtful stuff, IMO.  We need a bunch of well thought
out opinions in this vein. What guidelines do we want to put in place
for evaluating methods+software? How should we evaluate
methods+software researchers for impact? When we fund software
projects, what should we be looking for?

----

And that brings me to what we *should* be doing, which is ultimately what
I am most interested in.  For example, I must admit to deep confusion
about what a maturity model for bioinformatics software should look
like; this feeds into funding requests, which ultimately feeds into
promotion and tenure.  I don't know how to guide junior faculty in this
area either; I have lots of opinions, but they're not well tested in the
marketplace of ideas.

I and others are starting to have the opportunity to make the case for
what we *should* be doing in review panels; what case should we make?

It is in this vein, then, that I am trying to figure out what value to
place on software itself, and I'm interested in how to promote
methods+software researchers and research.  Neil Saunders had an
interesting comment that I want to highlight here: `he said
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1982136821>`__,

    My own feeling is that phrases like "significant intellectual
    contribution" are just unhelpful academic words,

I certainly agree that this is an imprecise concept, but I can
guarantee that in the US, this is one of the three main questions for
researchers at hiring, promotion, and tenure.  (Funding opportunities
and fit are my guesses for the other two.)  So I would push on this
point: researchers need to appear to have a clear intellectual
contribution at every stage of the way, *whatever that means*.  What it
means is what I'm trying to explore.

Software is a tremendously important and critical part of the research endeavor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

...but it's not enough.  That's my story, and I'm sticking to it :).

I feel like the conversation got a little bit sidetracked by
discussions of Nobel Prizes (mea partly culpa), and I want to discuss
PhD theses instead.  To get a PhD, you need to do some research; if
you're a bioinformatics or biology grad student who is focused on
methods+software, how much of that research can be software, and what
else needs to be there?

And here again I get to dip into my own personal history.

I spent 9 years in graduate school.  About 6 years into my PhD, I had a
conversation with my advisor that went something like this:

----

Me, age ~27 - "Hey, Eric, I've got ~two first-author papers, and
another one or two coming, along with a bunch of papers.  How about I
defend my PhD on the basis of that work, and stick around to finish my
experimental work as a postdoc?"

Eric - *blank look* "All your papers are on computational methods. None of
them count for your PhD."

Me - "Uhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhmmmmmmmmmm..."

(I did eventually graduate, but only after three more years of experiments.)

In biology, we have to be able to defend our computational
contributions in the face of an only slowly changing professoriate.
And I'm OK with that, but I think we should make it clear up front.

----

Since then, I've graduated three (soon to be five, I hope!) graduate
students, one in biology and two in CS.  In every single case, they've
done a lot of hacking.  And in *every single case* they've been asked
to defend their intellectual contribution.  This isn't just people
targeting my students - I've sat on committees where students have
produced masses of experimental data, and if they weren't prepared to
defend their experimental design, their data interpretation, and the
impact and significance of their data interpretation, they weren't
read to defend.  This is a standard part of the PhD process at Caltech,
at MSU, and presumably at UC Davis.

So: to successfully receive a PhD, you should have to clearly
articulate the problem you're tackling, its place in the scientific
literature, the methods and experiments you're going to use, the data
you got, the interpretation you place on that data, and the impact of
their results on current scientific thinking.  It's a pretty high bar,
and one that I'm ok with.

----

One of the several failure modes I see for graduate students is the one
where graduate students spend a huge amount of time developing software
and more or less assume that this work will lead to a PhD.  Why would
they be thinking that?

* Their advisor may not be particularly computational and may be giving
  poor guidance (which includes poorly explained criteria).

* Their advisor may be using them (intentionally or unintentionally) -
  effective programmers are hard to find.

* The grad student may be resistant to guidance.

I ticked all of these as a graduate student, but I had the advantage
of being a 3rd-generation academic, so I knew the score.  (And I
*still* ran into problems.)  In my previous blog post, I angered and
upset some people by my blunt words (I honestly didn't think "grad
student hacker fallacy" was so rude ;( but it's a real problem that I
confront regularly.

Computational PhD students need to do what *every* scientific PhD
student needs to do: clearly articulate their problem, place it in the
scientific literature, define the computational methods and
experiments they're going to do/have done, explain the data and their
interpretation of it, and explore how it impacts science.  Most of
this involves things other than programming and running software!
It's impossible to put down percent effort estimates that apply
broadly, but my guess is that PhD students should spend at least a year
understanding your results and interpreting and explaining their work.

Conveniently, however, once you've done that for your PhD, you're
ready to go in the academic world!  These same criteria (expanded in
scope) apply to getting a postdoc, publishing as a postdoc, getting a
faculty position, applying for grants, and getting tenure. Moreover, I
believe many of the same criteria apply broadly to research outside of
academia (which is one reason I'm still strongly +1 on getting a PhD,
no matter your ultimate goals).

(Kyle Cranmer's `comment
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1983939707>`__
on grad student efforts here was perfect.)

Software as...
~~~~~~~~~~~~~~

As far as software being a primary product of research -- `Konrad
Hinsen nails it
<https://khinsen.wordpress.com/2015/04/23/software-in-scientific-research/>`__.
It's not, but neither are papers, and I'm good with both statements
:).  Read his blog post for the full argument.  The important bit is
that very little stands on its own; there always needs to be
communication effort around software, data, and methods.

Ultimately, I learned a lot by admitting confusion!  Dan Katz and
Konrad Hinsen pointed out that `software is communication
<https://danielskatzblog.wordpress.com/2015/04/22/software-can-be-a-primary-product-of-scientific-research/>`__,
and Kai Blin `drew a great analogy between software and experimental
design
<http://phdops.kblin.org/software-dev-intellectual-contribution.html>`__.
These are perspectives that I hadn't seen said so clearly before and
they've really made me think differently; both are interesting and
provocative analogies and I'm hoping that we can develop them further
as a community.

How do we change things?
~~~~~~~~~~~~~~~~~~~~~~~~

Kyle Cranmer and Rory Kirchner had a `great comment chain
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1984563237>`__
on broken value systems and changing the system.  I love the
discussion, but I'm struggling with how to respond.  My tentative and
mildly unhappy conclusion is that I may have bought into the
intellectual elitism of academia a bit too much (see: third generation
academic), but this may also be how I've gotten where I am,
so... mixed bag?  (Rory `made me feel old and dull
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1984374660>`__,
too, which is pretty cool in a masochistic kind of way.)

One observation is that, in software, novelty is cheap.  It's very,
very easy to tweak something minorly, and fairly easy to publish it
without generating any new understanding.  How do we distinguish a
future Heng Li or an Aaron Quinlan (who have enabled new science by
cleanly solving "whole classes of common problems that you don't even
have to think about anymore") from humdrum increment, and reward them
properly in the earlier stages of their career?  I don't know, but the
answer has to be tied to advancing science, which is hard to measure
on any short timescale. (`Sean Eddy's blog post has the clearest view
on solutions that I've yet seen
<http://selab.janelia.org/people/eddys/blog/?p=313>`__.)

Another observation (nicely articulated `by Daisie Huang
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1983686261>`__)
is that (like open data) this is another game theoretic situation,
where the authors of widely used software sink their time and energy
into the community but don't necessarily gain wide recognition for
their efforts.  There's a fat middle ground of software that's
reasonably well used but isn't samtools, and this ecosystem needs to
be supported.  This is much harder to argue - it's a larger body of
software, it's less visible, and it's frankly much more expensive to
support.  (`Carl Boettiger's comment is worth reading here
<http://ivory.idyll.org/blog/2015-software-as-a-primary-product-of-science.html#comment-1983743324>`__.)
The funding support isn't there, although that might change in the
next decade.  (This is the proximal challenge for me, since I place my
own software, khmer, in this "fat middle ground"; how do I make a
clear argument for funding?)

Kyle Cranmer and others pointed to some success in "major
instrumentation" and methods-based funding and career paths in physics
(help, can't find link/tweets!).  This is great, but I think it's also
worth discussing the overall scale of things.  Physics has a few
really big and expensive instruments, with a few big questions, and
with thousands of engineers devoted to them.  Just in sequencing,
biology has thousands (soon millions) of rather cheap instruments,
devoted to many thousands of questions.  If my prediction that
software will "eat" this part of the world becomes true, we will need
tens of thousands of data intensive biologists at a minimum, most
working to some large extent on data analysis and software.  I think
the scale of the need here is simply much, much larger than in
physics.

I am *supremely* skeptical of the idea that universities as we
currently conceive of them are the right home for stable, mature
software development. We either need to change universities in the
right way (super hard) or find other institutions (maybe easier).
Here, the model to watch may well be the `Center for Open Science
<http://centerforopenscience.org/>`__, which produces the `Open
Science Framework <http://osf.io>`__ (among others).  My
interpretation is that they are trying to merge scientific needs with
the open source development model.  (Tellingly, they are doing so
largely with foundation funding; the federal funding agencies don't
have good mechanisms for funding this kind of thing in biology, at
least.)  This may be the right model (or at least on the path towards
one) for sustained software development in the biological sciences:
have an institution focused on sustainability and quality, with a
small diversity of missions, that can afford to spend the money to
keep a number of good software engineers focused on those missions.

----

Thanks, all, for the comments and discussions!

--titus
