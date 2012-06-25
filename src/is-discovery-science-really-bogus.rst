Is Discovery Science Really Bogus?
##################################

:author: C\. Titus Brown
:tags: science,metagenomics,molgula
:date: 2011-12-06
:slug: is-discovery-science-really-bogus
:category: science


This blog post was inspired by two recent events.

First, in response to a `NY Times article about the "data deluge"
affecting biologists
<http://www.nytimes.com/2011/12/01/business/dna-sequencing-caught-in-deluge-of-data.html>`__,
one of my Facebook friends said something like "stop whining about how
hard it is to analyze the data and do some good experiments instead!"
I vehemently disagreed with this simple statement -- but why??

Second, I used the 4th domain paper by Jonathan Eisen in my
computational science class, and we discussed how one would reject or
accept the 4th domain with more confidence.  Somewhat to my surprise,
my own conclusion was that I would ... sequence everything!  Yep, just
go out and sequence everything I could get my hands on in the
`tree of life <http://pacelab.colorado.edu/images/Big_Tree_Bold_Letters_white.png>`__, as well as a bunch of communities from ocean and soil.  I was
surprised to reach this conclusion (which we can debate on its own
merits some other time) because my background is in *real* science,
not "discovery science", and I'd been trained to believe that the
discovery-based approach of shaking the trees to see what falls out
was kind of unintellectual and unscientific.

Both of these events made me rethink my attitude towards discovery
science.  The first, because the guy that told us all to stop whining
isn't dumb, but I also don't think he's entirely or even mostly right;
and the second, because, together with the first, it made me challenge
the conventional wisdom in molecular biology that hypothesis driven
science is the Right Way.

Hypothesis-driven biology
-------------------------

The way many (most? all?) molecular biologists work is something like
this: they develop a theory about some process (physiological or
developmental or genomic or whatnot), develop a specific hypothesis or
set of hypotheses, and then figure out how to test those hypotheses
using controlled experiments.  "Hypothesis: objects of near equal mass
accelerate equally in a uniform gravitational field; test: drop two
objects of equal mass; control for wind resistance."  In developmental
biology, the molecular field with which I'm most familiar, you might
say "I think that the pax3/7 gene is necessary for neural crest
specification in these cells at this time, so I'm going to knock it
down and see what happens to neural crest."  The key point is that you
always need to reframe your theory in the form of a fairly specific
hypothesis, and then figure out a way to test it.  Training students
to develop, frame, and test hypotheses is What We Do as professors.
When you write grant proposals, you write about why you have developed
a specific set of hypotheses (that is, you justify your hypotheses by
appealing to prior work and preliminary results), claim that these
hypotheses are important or interesting, and then argue vigorously
that you are the right person to receive beaucoup bucks to test these
hypotheses.  Hypothesis-driven research is what we do!

This somewhat dogmatic picture obscures a number of inconvenient
truths, however.  First of all, many grant agencies (and reviewers)
are risk averse, so they prefer to fund things that appear as certain
as possible.  This means you have to walk the line between crippling
your hypotheses by predetermining them with your data, and coming up
with an interesting and novel hypothesis -- if you've already tested
your hypothesis and you're pretty sure it's right, then it's no longer
that interesting to test!  Second, no research plan survives contact
with reality. So what you really do is sketch out a small extension to
a near-certain hypothesis, get funded (admittedly this step is rather
rare...), and then discover that your extension is incredibly
simplistic and most likely wrong and a dead-end alley. So you end up
working on something else completely.  That is, you get the grant to
work on X and end up working on Z -- not necessarily *too* far away
from X, but not X, either.  This leads to a third truth, which is that
you get grants because you've been able to make a successful argument,
*not* because anyone expects you to accomplish exactly what is in the
grant.  The only people that *really* take your grant proposal
literally are the contracts & grants people at your university; the
grant administrator and you both understand that this is research, and
a real researcher is likely to end up someplace other than where you
intended to go, at least in detail.

(I always like to cite Einstein at this point in a conversation: "If we
knew what we were doing, it wouldn't be called research, would it?")

What happens when a student confronts this situation?  Well, usually
students have to write research proposals as part of their qualifying
exams, and often students try to stick to those research proposals
even when their experiments go awry.  I've been part of a bunch of
committees where the student will say "ok, so these were our original
aims, and here's where I've gone away from them".  They don't seem to
understand that we don't care (or at least I don't): the real point of
the qual is to make sure they know how to frame a hypothesis, and to
ensure that they know what a testable hypothesis looks like, smells
like, feels like, and tastes like.  After that, your research will go
where it goes, and that's as it should be.  (Aside: my most
frustrating (but still positive) moment as a committee member occurred
when a student presented a hypothesis and talked about how she was
going to test that hypothesis with method X, method Y, data analysis
Z, etc.  We asked her a bunch of questions and she seemed strangely
confident and specific about the expected results.  Upon further
probing, it turned out that she'd already *done* the experiments and
*knew* the answers, but thought that the qual needed to be about her
hypotheses de novo, and shouldn't take into account actual data she'd
generated.  WTF??)

Unfortunately, we often stick students with projects where there is no
honest way to frame a specific hypothesis.  This is true of young
labs, which may not have enough specific data to develop a good
testable hypothesis for their system and are still casting about for a
specific direction to take; and it's increasingly true of established
labs that are using next-gen sequencing.

Cue next story: a student of mine was (and still is) part of a
collaboration where we were doing bioinformatic analysis of
genome-scale disease data.  The other professor had funding and
generated the data, which was basically sequencing RNA from an
affected organ.  There literally was *no specific hypothesis* other
than "let's go see how this disease is affecting the spleen
transcriptional response."  This was then given to my student, who
happily pounded away at the data for a few months (making many more
trenchant observations about mRNAseq than about the disease, but
nonetheless making progress).  It came time for his committee meeting,
and his committee insisted that he present a hypothesis.  He cast
about for a while, and finally come up with "there will be a
differential transcriptional response to this disease in the spleen."
This was nearly disastrous, of course, because it's simply not very
specific!  Sure, it's a hypothesis, and it's almost certainly true,
but it's not specific enough to be useful.  So my student nearly
failed his committee meeting (note that I was a young(er) prof at this
point, and hadn't seen this coming; my fault!)  Why am I telling this
story, though?  Because my collaborator, who had generated the data in
a hypothesis free manner, *was a member of the committee, and was very
disturbed by my student's lack of a hypothesis*.  Why?  Because it was
considered *very important* that our students be doing hypothesis
driven science, even though neither he nor I had directed the project
that way!

Before I continue on to draw a lesson from this, let me say: I'm not
anti-hypothesis in any way.  The student is, eventually, going to have
to develop a hyp, or he isn't going to get his PhD; he knows that, and
I know that.  But we were still working on *generating hypotheses from
the data*, and didn't have them ready at hand; developing the
hypotheses was actually the first, very significant component of the
project.  Another point is that the committee was *completely
unprepared* for this.  And a third was that the guy who generated the
data was so wedded to this hypothesis-driven approach that he
basically ended up being hypocritical -- which I point out to
him regularly :).  (Another component that actually played a smaller
part than I'd feared was the computational nature of the research: a
certain subset of molecular biologists will vehemently deny that
useful work can be done without a pipette man in hand.  This either
leads to ineffective one-handed typing in bioinformatics, or
vociferous arguments among professors -- neither good for committee
meetings.)

The lesson I want to draw from this anecdote is simple:
`hypothesis-driven science is dead!
<http://www.wired.com/science/discoveries/magazine/16-07/pb_theory>`__

No, no, not at all.  More seriously, I think that as data generation
becomes easier in some fields of biology, we should recognize that an
extended period of hypothesis generation through discovery-driven
approaches may be useful and necessary for many projects.  Many
biologists may not be any good at this, because they've been honed for
decades to focus on moving as quickly as possible to a hypothesis
based on a relatively small amount of hand-curated data; but in
practice, hypotheses are now cheap (because data is plentiful) and I
think we should focus on developing likely hypotheses and winnowing
out the dumb 'uns computationally before we ever pick up a pipette man
to test 'em.  That is, expand the hypothesis-generation and analysis
stages so that we're more likely to develop a comprehensive and
interesting hypothesis.

About Models, and Model Systems
-------------------------------

One of the limitations of the drive to proximal hypotheses is that you
need to have tractable systems -- systems in which you can relatively
quickly and easily test hypotheses.  This leads to using models, and
model systems.  For example, Drosophila is a great model for genetics
and development: it's been used for decades, and has led to at least
one set of Nobel prizes for basic understanding of genetics.  You can
do lots and lots of things with it way more easily than you could
imagine doing those same things in a mammalian system: mutagenize,
resequence the genome from scratch, do all sorts of crosses in what
appear to be a few weeks, etc. etc.  But, whether you're interested in
biomedical applications, or you're interested in population genetics,
or whatnot, it's still just a model, and to build a connection to the
broader set of science, you need to analogize the model in various
ways.  The bigger the field around the model system gets, the less the
people feel the need to make the model explicit, and then the junior
people forget about it.  And so sometimes the model just doesn't
apply.  One of my favorite examples (just to pick on Drosophila and
C. elegans, which are the two biggest invertebrate animal model
systems) is from the early days of genomics.  We sequenced mouse, and
human, and Drosophila, and C. elegans, and saw that there were about
30% more types of genes and gene families in vertebrates.  This led to
a certain amount of breathless discussion about "the genes that made
us vertebrates".  Then we sequenced hydra (most emphatically not a
vertebrate!), and discovered that it had almost all those gene
families.  Bang!  It turned out that Drosophila and C. elegans were
members of a monophyletic group, the Ecdysozoa, which had undergone
extensive gene loss!  So in some ways, Drosophila and C. elegans are
*really bad* models for vertebrate genomics!  They're from a
relatively distant branch of the animals, they have small genomes
partly because they were chosen for rapid breeding, and there are lots
of things that are just different about them.  They're still awesome,
and they deserve a lot of study, but the history of genetic research
on them really shows both the pluses and minuses of model systems:
sometimes a model system that's great for one reason is *horrible* for
another.

The same thing happens in ecology and population genetics, it seems to
me.  There's a lot of mathematical models that are simple and
tractable and that let you "test hypotheses" about certain kinds of
relationships, but then you have to determine how relevant those
models are to reality.  People would prefer not to spend that kind of
time or effort -- because it's time and effort *not* spent generating
and testing hypotheses.  So the connection is made only for a few
kinds of systems, which limits the vision of people doing research.

What about cancer?
------------------

I think another catalyst that made me think about all of this is the
book **The Emperor of Maladies**, a Pulitzer-prize winning biography of
cancer.  There you see again and again how hypothesis driven
approaches basically failed, while we slowly developed diagnostic
tools and (frankly) guessed randomly about how to deal with cancer.
Only recently have we started to gain an understanding of exactly
what's going on at the genomic and genetic level, but it's still slow
to make its way into therapeutic use; chemo -- killing the cancer
*slightly* more quickly than the normal cells -- is still the main
treatment, for chrissakes.  Do you think we would do that if we had
any other option??  Reading the book, the guy who developed the Pap
smear (an excellent diagnostic for cervical cancer) did so on guinea
pigs, because it was the only way he could detect estrus in guinea
pigs -- by scraping the cervix.  He spent 20 years trying to find a
biomedical use for it!  That's not hypothesis-driven science.
Epidemiology has probably had a greater effect on cancer treatment
than anything else, by tracking down the specific causes of various
conditions like lung cancer, long before we were thinking about
cellular mutations.

In my class the other day, the one where we talked about the 4th
domain work, James Foster from U Idaho made the point that observation
in biology used to be called "Natural History".  One of the greatest
successes of Natural History?  Evolution, the greatest explanatory
theory in biology, came directly from the synthesis of vast amounts of
observation, with no experiment involved.  It took decades for Darwin
and others to put it together, and decades more for it to be validated
in a hypothesis-driven framework (I'm thinking the finches, or the
Lenski E. coli experiment, here; there are probably better places to
cite that I don't know about).

The Molgula
-----------

When my Facebook friend & colleague talked about how we should stop
bitching about data processing and start thinking about experiments,
I'm pretty sure he meant that people should be better
hypothesis-driven scientists.  My instinctive reaction to that thesis
is that he's not right (nor is he entirely wrong -- hypothesis-driven
science is still necessary, just not sufficient!)

One of my current projects is working on a group of sea squirts, the
Molgula, that underwent a dramatic morphological change in the larval
form: many of the larvae lack tails.  We want to know, how did this
happen?

To address this question, we went out and generated about 600 million
reads of mRNAseq from a variety of larval stages for a tailed sea
squirt, a tailless sea squirt, and hybrid crosses between them.  This
has let us ask which genes are present, what their levels of
expression are, and whether there is allele-specific expression of
certain genes in one species over another (never mind, just trust me,
it's important & interesting to know).  In order to analyze this data
- which amounts to about 80 GB of DNA, compressed -- we've had to
invent a whole new series of data analysis and reduction tools.  This
is because the Molgula aren't well-studied model systems: they don't
have genome sequences available, no large scale cDNA projects have
been done on them, and the molecular tools for doing basic probes are
still thin on the ground.  It was far easier to spend $20k on
sequencing and get an answer in a matter of months -- even counting
the development of the data analysis tools -- than it was to do
anything else.

Are we going to now go out and take our high-throughput data and
analyze it and conclude, voila, we know why the tails aren't forming?
No, we're not that dumb!  But we are developing several early
hypotheses based *on* the data we have, and we're checking to see if
they're plausible in the face of tissue-specific gene expression
assays (WMISH).  Then we'll go and do the hypothesis-driven
perturbations to see: is the tail being specified and failing to
extend?  Or is it not being specified at all?

It's worth pointing out that virtually everything known about tail
development in the sea squirts comes from one particular species,
Ciona intestinalis, which is now a pretty established model system:
genome, database, EST projects, a whole community.  The Molgula,
however, which look morphologically pretty similar, are about as far
away from Ciona (evolutionarily speaking) as you can get and still be
a sea squirt.  Wouldn't it be fascinating to know how tails develop in
them?  Well, if we hadn't lucked into some excellent seed funding for
the Molgula project and been able to generate and analyze the vast
amounts of sequence, we wouldn't be on our way to looking at them --
this kind of study is seen as a fishing expedition, not worthy of
being funded.

This is really the problem with hypothesis-driven approaches, and the
priority we give them: they focus us on the questions that can be
answered fairly quickly and easily, and not necessarily on the big
questions.  Sometimes it's possible to find a fundable route to those
big questions; sometimes not.  In the latter case, the questions go
unaddressed.

Soil metagenomes
----------------

The other big-ass data project I'll bring up is the Great Prairie
Grand Challenge, in which the DOE JGI is sequencing literally
terabases worth of DNA extracted from midwestern soil.  The ultimate
goal is to understand the microbial community composition and
function.

Do we have any idea how to do that?

Well, the answer is, "not really".  The field of metagenomics is still
young, and it turns out to be technologically blocked.  That is, the
diversity of soil is so high that you need to sample it really deeply;
but then the depth of sampling yields so much data, that you can't do
anything clever with it computationally.  This is one of the other
focuses of my lab, and it's emphatically a long-term discovery-driven
project.  We have only a little idea of what we're looking for, and
it's likely to be unrecognizable on the first four looks.  We'll have
to look and think deeply, AFTER solving the data analysis problems
(which, again, I think we have.  But it was really hard :).

Rumsfeldian science
-------------------

One of my other favorite citations is that great Rumsfeld quote, about
the known knowns, known unknowns, and unknown unknowns (in his case,
with respect to invading Iraq -- oops).  We know *so* little about
biology that to restrict our gaze to the known knowns, or even to the
known unknowns, is foolish.

Look again at `this evolutionary tree of life
<http://pacelab.colorado.edu/images/Big_Tree_Bold_Letters_white.png>`__,
from Norm Pace's lab.  We understand virtually *nothing* about the
vast majority of those organisms.  Sure, we can start to get at the
commonalities of some aspects of protein composition, cellular
organization, and genomics.  But who knows what's out there?
Certainly not me, and I suspect no one else.  We have a long way to
go.

To return to the original purpose of this rant, a lot of this "known
unknown" and even more of this "unknown unknown" stuff involves
looking at vast amounts of data and finding clever ways to grok the
structure of the data, filter out stuff we think is uninteresting, and
cherry pick the stuff that IS interesting.  This is one of my focuses,
and it is hard, specialized, time consuming, and wonderfully
challenging.  To hear other scientists say, dismissively, that we need
to learn how to do proper experiments is a bit disheartening, and,
even more problematically, rather short-sighted for the field.

Data -- especially the vast amounts of next-gen data starting to come
from sequencers -- is usefully "hypothesis neutral".  In Timo Hanny's
defense of `Chris Anderson's theory that "hypotheses are dead"
<http://www.wired.com/science/discoveries/magazine/16-07/pb_theory>`__
in **The 4th Paradigm**, he pointed out that surely there *is* some
point where "more" is different from "some".  Being able to
sensitively look at minor members of communities, or low-expressed
genes and isoforms, will inevitably be informative; we shouldn't just
discard it as "that useless discovery science stuff".

In conclusion:

A key part of doing good hypothesis driven science is to come up with
good hypotheses based on large-scale observations of biological
systems.  We should respect that initial stage of observing more than
we seem to.  My graduate advisor, Eric Davidson, told me the famous
analogy about scientific practice being similar to a drunk, having
dropped his keys in a dark alleyway, looking for them under the
street light; while some people spend their career carrying flashlights
into dark corners and doing a really detailed search, and others work
on the flashlights, I think it's also going to fruitful to turn up the
wattage on the street light so that all of those dark corners get
illuminated.  And we'll need sharp eyes to search all that newly lit
territory.  DNA sequencing is turning up the wattage; let's develop
the methods to find the nifty stuff that we can now see.

--titus


----

**Legacy Comments**


Posted by Mick Watson on 2011-12-07 at 03:40. 

::

   I can add some comments on my frustrations about large NGS projects ;)
   First of all, when you're a well-funded group with very large budgets
   to spend on sequencning "everything", it's easy to forget that there
   are LOADS of people who would kill to have your problems - I know, I
   **used** to be one, and moved jobs specifically so I could be part of
   the digital deluge.  So stop whingeing about the amount of data you
   have, you're lukcy to have it.    Secondly, I VERY MUCH DOUBT that
   project leaders wrote in "the grant" that they would generate huge
   amounts of data that they would have serious difficulty managing,
   analysing and interpreting.  If they did write that, and got funded,
   then I need to have a bit of what they eat for breakfast.  No, what
   they probably wrote is that by sequencing all of this "stuff" that
   they'd find out loads of interesting information, develop some new
   methods along the way, and answer some fundamental biological
   questions.  Great.  So stop whingeing and go do what you said you'd
   do.    And finally, discovery science or hypothesis-driven science,
   whichever you're doing, you definitely have to have SOME kind of idea
   of the questions you are trying to answer.  I am hopelessly,
   cripplingly bored with "the 1000 genomes project", "the 10000 genomes
   project", "the million genomes project".  Oh f*ck off will you?!!!  I
   think the biggest and best outcome of the 1000 genomes project will be
   the bioinformatics developments that were developed and published, and
   that's a little bit great and a little bit sad.  The impact of NGS on
   human health will not come from these massive, multi-centre, unfocused
   projects - they will come from the clinics, from smaller case-control
   studies, from patient studies in hospitals where we're already seeing
   NGS having an impact on how patients are treated.  So why don't we
   fund more of the focused projects, and less of the massive, unfocused
   ones?    The challenge of NGS is not even analysis; it's
   interpretation.  And for that, I agree with Mike Eisen - go design
   some experiments.


Posted by Titus Brown on 2011-12-07 at 09:25. 

::

   That's quite the set of frustrations :).  If funding priorities were
   at all aligned to solve your frustrations, I would be less frustrated
   myself -- that is, right now there's virtually no support for
   computational tool development, compared to the amount of money spent
   on generating data.  As for the million whatever projects, sure; but
   many small labs are now doing their own "million" projects just
   without the funding or hype...


Posted by Matt on 2011-12-07 at 10:23. 

::

   I think you have hit upon an important issue-- the 1st step in
   developing hypotheses is understanding something about
   nature/biological processes/natural phenomenon.. Without this
   knowledge, we're stuck.     Now, trying to get a natural history
   project funded-- well that is next to impossible.. Most of these large
   scale genome projects are really 'just' natural history-- natural
   history of the Homo genome, characterizing variation, noting
   interesting details or irregularities,  etc.. These studies, done
   properly, would make Joseph Grinnell proud!    In short, science needs
   a mix of both types of work, Hypothesis driven AND "Discovery Science"


Posted by marie on 2011-12-07 at 23:52. 

::

   You should take long flights more often - your rants are great! I
   particularly enjoyed this one because it allowed me to laugh at my own
   predicament of having to increase the scope of my project to
   accommodate a hypothesis-driven component (Aim 1) while really
   (secretly) wanting to do discovery science (Aim 2), along with
   proposing the development of improved computational methods to
   overcome obstacles to the other things I've proposed (Aim 3). It feels
   like overwhelming madness... can I cite your blog as a source to
   justify the virtues of discovery-based science? ha!     And just to
   whine some more - I could just as easily spend all my time working on
   other people's pig-dog-bear-man projects because taking your course
   has apparently given me a magical knows-anything-at-all-about-the-
   buzz-word-of-the-day-NGS popularity. Or just maybe I actually learned
   something ;)     Aside - could I presume that your "sequence
   everything" approach would also include "assemble everything" and
   "annotate everything"?


Posted by Titus Brown on 2011-12-08 at 09:36. 

::

   Hey Marie, I think the null hypothesis is that you've been blessed by
   the NGS magic wand :).  And yes, good catch: sequence, then assemble,
   then annotate :).

