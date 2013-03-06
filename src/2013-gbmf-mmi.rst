Cyberinfrastructure for Marine 'Omics (2013 version)
####################################################

:author: C\. Titus Brown
:tags: science,software,cyberinfrastructure
:date: 2013-03-05
:slug: 2013-gbmf-mmi
:category: science

I just finished attending a 1-day workshop on Cyberinfrastructure for
Marine 'Omics down in DC.  It was a meeting organized by the Gordon
and Betty Moore Foundation but attended by program managers from about
a dozen different agencies and divisions (NSF BIO, NSF GEO, etc.); a
bunch of pretty serious marine biogeochemists (?) also attended.  And
me.

The workshop was both really interesting and thought provoking, and
very depressing.  The problems are hard, and the solutions aren't
forthcoming.

An imperfect summary and set of thoughts, below.

Links
-----

`My talk slides <http://www.slideshare.net/c.titus.brown/2013-gbmfmmici>`__

`A Storify from my occasionally sarcastic side commentary on Twitter
from the workshop, and responses
<http://storify.com/ctitusbrown/gbmf-march-2013-workshop-on-cyberinfrastructure>`__

`A not-that-well written thing about how to write better metagenomics pipelines <http://ivory.idyll.org/blog/building-better-metagenomics-pipelines.html>`__

`Yes, we should use Service Oriented Architectures
<http://ivory.idyll.org/blog/nas-workshop-2013-heterogeneous-data-integration.html>`__.
Please `reread the Yegge platform rant
<https://plus.google.com/112678702228711889851/posts/eVeouesvaVX>`__.


Building "Cyberinfrastructure" for specific domains is hard
-----------------------------------------------------------

The term "cyberinfrastructure" encompasses hardware, networking, and
software across all levels - the metaphor used in the workshop was
"roads and cars", as in, without roads, cars aren't that useful;
without cars, roads aren't that useful.  We need both.

Personally, I'm mostly focused on the question of "how do we build
useful software, fairly close to the research, that can help enable
domain experts to get their work done?"

The three approaches seem to be (warning, mild sarcasm below):

1. give money to computational folk, who then build low level
   infrastructure and focus on premature optimization of specific
   workflows.  End result: infrastructure that doesn't address
   the actual problem.

2. give money to domain scientists, who then use it to do research.
   End result: software that does awesome stuff, but has unknown
   generalizability and often can't be used by anyone else
   (see: `The Ladder of Scientific Software Notsuck <http://ivory.idyll.org/blog/ladder-of-academic-software-notsuck.html>`__)

3. recognize that there are cross-domain-cutting problems that could
   be addressed by coordinated funding, and try to leverage that
   funding to actually address those cross-cutting problems.  (I would
   argue that metagenome assembly is one such problem shared by many
   fields.)

For examples of the 3rd, see `iPlant
<http://en.wikipedia.org/wiki/IPlant_Collaborative>`__ and `DOE KBase
<http://kbase.us>`__.  My big problem with these is that they are not
run as open source projects so there's a lot of opaque development
focus, opaque money flow, and potentially wasted development.  iPlant
(at least) has `an open source mandate
<http://www.iplantcollaborative.org/about/opensource>`__ although I am
withholding judgment on reusability until they pay me a lot of money
to consult. Haha, no, seriously, I want to see someone else install
their stuff in the Amazon cloud.  Then I'll believe them when they say
it's reusable ("trust, but verify").

A fourth way would be to embrace the Open Source/Open Platform Way and
start building kick-ass reusable components that could then be
combined into analysis pipelines by whomever wants to do so.  As I
said during `my talk
<http://www.slideshare.net/c.titus.brown/2013-gbmfmmici>`__, if the
biggest problem we have in 3 years is how to combine all the awesome
tools that are available, I will be a happy man...

This is also the point where companies could step in and make use of
the components (thus avoiding the CLC Workbench problem of "everything
is secret!") to build integrated pipelines.  I can name a few companies
doing this in other areas.

This 4th way is what we would like to do with `khmer
<http://github.com/ged-lab/khmer>`__.  Hell, it's what we *are* doing
with khmer: one of the personally best things to see at the conference
was the public acknowledgment by Susan Gregurick of KBase that they
were using khmer somewhere in their metagenome assembly pipeline.

We need a new way to fund research software
-------------------------------------------

Another thing I took away from the workshop was that we simply need a
new way to fund research software.  As with my `Dear Abby
<http://ivory.idyll.org/blog/dear-abby-hiring-computational-people.html>`__
post on hiring computational biologists, the domain specialists will
win in any reasonable funding competition, and the computational
people will be kicked to the curb.

Is it really that dire? I think so.

First, the funding cycles are slow and not particularly results driven.
It may take two tries to get a 3 year grant, and at the end of the
grant everyone will want to see a few papers.  The question of whether
or not you actually built anything useful rarely comes up - it's all
measured by pubs.

Second, everyone wants to fund *science*, not *software*. The fact
that some science *requires* software does not escape funders, but if
you give an ocean geochemist reviewer a choice between a potentially
really cool set of experiments and a potentially really cool software
platform, I bet they'll choose the experiments 9 times out of 10.

Third, funding is flat or negative overall, so fairly frequently the
overall size of the pie has effectively decreased and the reviewers
are going to have to decide which of 5 awesome projects to cut.  In
combination with #2, you can bet that new software stuff isn't going
to be funded.  (Yes, given that increasingly science requires
software, this bodes ill for the future.)

Fourth, software is (in theory) too broadly useful, and everyone wants
to leverage other people's funding.  Why would we fund 'omics
platforms for biogeochemistry from NSF Geo, when we need basically the
same thing over in NSF Bio? *They* should fund that! Bounce that
around enough and voila, nobody actually gets any initial funding to
leverage.

Fifth, funding for *building software* is rarely available:
algorithms, yes.  Data structures, yes.  But implementations? Yawn.
(This is for a pretty good reason: scientists basically don't know
how to implement, either, and the salaries we can offer don't bring
in serious software engineers.) The discussion of the three-track
ABI program by Peter McCartney was awesome in this regard -- they
seem to be doing it at least partly "right".

Sixth, we lack senior people who know how to build software, which is
one reason it's not getting built.  (I'm increasingly feeling like the
token "guy who knows about github" in these CI meetings :).  I guess
that's a good change from 5 years ago when there wouldn't have been
anyone, but the fact remains that you need people who are domain
scientists *and* programmers in the room for these conversations.

So I'm not feeling particularly positive here.

Are there any solutions?
------------------------

Dunno.  Everyone seems enamored of the "let's throw more money at it,
oh, wait, we have no more money, drat" conversation, and a strong
recommendation of the workshop was to have another workshop to address
whether more workshops about having workshops would be useful, with
the end goal of having another workshop to produce a white paper that
would inform the next set of workshops.  (You think I'm kidding, but
only slightly -- this wasn't actually the final recommendation,
because we recognized the absurdity.  And, by the way, I'm getting
burnt out on workshops.)  Best part of the conversation: when one of
the organizers said, "the point of this workshop isn't just to update
the recommendations from the 2007, 2009, and 2011 workshops.  It's to
come up with a specific recommendation for the next workshop." heh.

There was a lot of discussion about how to get this on the NSF's
radar by holding community meetings.  But, as one experienced
program manager pointed out, you simply end up robbing Peter
to pay Paul unless new money comes in.  It's not clear anyone
will actually go for that, although I'm all for trying.

I think there are a lot of cheap things that could be tried by the
more experimentally minded, though.

I'd love to see a Sandpit in the area of "meta-omics".  `Sandpits
<http://www.cs.st-andrews.ac.uk/?q=node/200>`__ are brainstorming
sessions to develop grant ideas, and I think one on components would
be really welcome.  The more general idea is `Coopetition
<http://en.wikipedia.org/wiki/Coopetition>`__ -- get a bunch of
smart people in a room and let them figure out what should be done,
and the fund it.  As long as the smart people don't actually like
each other that much, you can avoid collusion ;).

Another thought is that if the Moore Foundation really wants to
address some of the missing components, they need to fund
bioinformaticians.  I know that some of the MMI investigators are
having a hard time with bioinformatics (I partly know this because I
am collaborating with some of them), and I'm increasingly critical of
the very concept of funding data gathering without concomitantly
funding data *analysis*.  (Then again, this recognition is one reason
the workshop was being held, so I'm probably being too mean.  But they
did reject me for MMI :) And yes, this is a self serving suggestion,
but it needs to be said.

I would particularly welcome "collaboration grants" where funding
agencies provide, say, a computational grad students' salary for some
period of time to work with an existing Moore investigator, so that
they can work on building more sustainable infrastructure centered on
a very specific biological problems.  i.e. Take the specific and make
it more general.

Another idea -- it would be great to have rapidly proposed, rapidly
funded, and rapidly evaluated 6- or 12-month software projects.  I'm
not sure if this could work well in isolation, but if you did this as
an open call to build and test components that both iPlant and KBase
could use (for example - maybe add Galaxy in here, too), then you'd
virtually be guaranteed to end up with something useful.  My guess is
the money wouldn't be big enough to actually put in the required time,
but there's an obvious solution to that ;).  And if you required that
the components be open source, well, at least you'd end up with *some*
product.

Ginger Armbrust talked about a meeting that sounded like a great
hackfest-like workshop, where biologists and computational people got
together to work on problems.  We did something similar for the HMP,
nucleated by Rob Knight and the NIH.  More of this kind of communal
workshop would be great, because it makes the problems clearer on both
sides.  (Sprints FTW.)

Final thoughts
--------------

Building software at the interface of research and computation is
really hard, no doubt about it.  People are leery of pouring more
money into what has so often been a failed enterprise.  End Comment.

It's no surprise that resolving the tangle of academia, funding,
career incentives, and training in order to build software effectively
is seemingly intractable.  When I put up my "other things I'm doing
slide" (see `my talk
<http://www.slideshare.net/c.titus.brown/2013-gbmfmmici>`_, slide 7)
it struck me that I'm trying to address exactly this tangle.  Maybe
obvious to people, but there you are.  It's nice to find unifying
themes to one's work.

It was *really* nice to hear an NSF program manager complaining that
they don't like seeing fixed-term faculty on research grants, because
to the NSF it seems like the university isn't putting itself on the
line at all.  Basically, if you hire somebody conditionally on them
finding grants to pay for themselves and all their resources, then
the NSF rightly has no faith that the university will support them
in any way if they run into trouble.  I'd never thought about it
that way.

Program managers and funders really don't like hearing themselves
described as making top-down design decisions about computational
pipelines.  I said something like that early on and then had to defend
it (privately) to about 5 different people.  They did see my point,
though, when I explained it like this: if you have enough money for
only one project, and you write the RFP, find the reviewers, evaluate
the reviews, and pick one specific project, it's hard to argue that
this is a "bottom up" driven process.  Their point is also well taken:
"top down" depends on where you are in the hierarchy of decision
making.  I just happen to be at the bottom, which means that
everything is "top down" from my perspective :)

I asked for examples of successful CI, and people cited the `Protein
Data Bank <http://en.wikipedia.org/wiki/Protein_Data_Bank>`__ and
one other that I've now forgotten.

All in all, an interesting workshop.  We'll see what happens.  I look
forward to the next one :).

--titus
