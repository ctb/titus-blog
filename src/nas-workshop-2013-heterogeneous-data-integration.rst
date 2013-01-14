My takeaways from a 2013 NAS Meeting on Heterogeneous Data Integration
######################################################################

:author: C\. Titus Brown
:tags: science,data
:date: 2013-01-11
:slug: nas-workshop-2013-heterogeneous-data-integration
:category: science

I just left the `NAS meeting on Integrating Environmental Health Data
to Advance Discovery
<http://nas-sites.org/emergingscience/meetings/data-meeting/>`__,
where I was an invited speaker.  It was a pretty interesting meeting,
with presentations from speakers who worked on chemotoxicity data,
pollution data, exposure data, and electronic health records, as well
as a few "outsiders" from non-environmental health fields who deal
with big data and data integration issues.  I was one of the outsiders.

The entire meeting was recorded and should soon be available, in which
case I'll update this post with links to those materials.  Rather than
blog the entire thing, I'm going to try to distill out three main
take-homes. (Think "lossy compression," heh.)

tl; dr? It's all about incentives; nobody really cares about education,
but it's really really important; and standards and ontology are the
really hard technical problems.

1. It's all about incentives
----------------------------

A number of people quite convincingly pointed out that it was not in
the direct interests of scientists to share data well, and that
cooperation between groups was not particularly rewarded in general.
Stephen Friend's entire talk was about incentives, in a way;
incentives to share, incentives to collaborate, incentives to release
data, incentives to come up with better analyses.

These are not new arguments, of course.

But what came out of this meeting is the very clear sense that the
slowest people to change (apart from the larger part of the mass of
scientists themselves) are the mid- and upper-level bureaucrats at
universities.  Since universities are where most basic research
happens, this is A Problem: not only do they not encourage change,
they actively block researchers from doing things differently by
firing ("failing to give tenure to") those who do.  The particular
problem we're confronting here is the scientific equivalent of how to
get enough street cred to get tenure -- a topic of
some personal interest to me :).

If anyone can crack this problem in a general way, the research world
will change.  One hopes it will be for the better.

A number of people made the point that the most likely pivot point for
manipulating institutional incentives was funding; if the NSF and NIH
provide the appropriate incentives to change, then change will happen,
because MOOLAH.  (This is why I'm so amazed by the `set of reviews I
recently got
<openness-and-online-reputation-recognized-in-grant-reviews>`__,
because it rather directly went against common wisdom in the
university.) Stephen Friend invoked Elinor Ostrom's work on how to
change institutions, and Michael Neilsen (via Twitter) strongly
suggested her book `"Governing the Commons" <www.amazon.com/Governing-Commons-Evolution-Institutions-Collective/dp/0521405998>`__.

On further reflection, though, this is a chicken-and-egg problem.
Funding agencies have different incentives than universities, but are
largely staffed by academics on furlough.  Moreover, grants are
typically reviewed by guess who? By academics, of course, who can
subvert the stated intent of a grant program by reviewing and ranking
the grants however they please.  We're not going to get change very
fast unless we can figure out how to drive the grant review process
differently.  (See above amazement, again. ;) There was a lot of
discussion of data analysis competitions, gamification, and incentive
systems that rewarded progress directly, and I have a hunch that those
will result in faster change than is possible via the standard
grant mechanism -- and again, Stephen Friend presented some convincing
experiences in this direction.

Stephen also made the surprising prediction that in some number of
years (like 10 -- soon!) that most research dollars will come from
crowdfunding solutions.  (This occasioned some skepticism on Twitter.)
Interesting prediction; I suggest we all watch `Ethan Perlstein's
experiment
<www.rockethub.com/projects/11106-crowdsourcing-discovery>`__
veeeeeeeeeeery closely, and not just because I'm concerned about the
meth-crazed yeast.

Barbara Wold had a really interesting and (to me, novel) idea for
incentivizing the production and distribution of *good* data.  She
suggested that in addition to just providing an archive of *all* data,
an additional archive of only high-quality data -- data that passed
some set of benchmarks and quality controls -- be created.  If this
data became regarded as more trustworthy than the default archive by
reviewers, work based on the data could be more highly regarded; given
`citation mechanisms for data <http://www.figshare.com>`__ this could
result in regular producers of good quality data gaining cred.  This
idea passes my smell test for being something that could be quietly
subversive and effective, in part because Barbara is both smart and
understands the system very well from all sides.

2. Education is important and undervalued
-----------------------------------------

There's a weird blank spot amongst biology faculty about education.
On the one hand, everyone acknowledges that grad students, or postdocs
(who come from grad students, note), do most of the work.  But there's
a strong bias against teaching them anything outside of the lab,
'cause it's a waste of time when they could be doing research.  So
most of what they learn, they learn in the lab which is necessarily
very focused and directed towards the research the lab is doing.  The
question is, in an era where most labs lack computational skills, how
do students become more broadly knowledgeable and capable beyond what
is already done in the lab?

Personally, I think this situation is an implicit indictment of the
graduate classes we offer, which often lack practicality (I've
certainly gotten this feedback from people who go into industry, BTW).
In my previous blogging about this, I came to the surprising
conclusion that `we should only force bio grad students to learn stuff
they don't know they should learn
<whats-the-matter-with-bio-grad-school.html>`__, and leave the rest to
survey courses, seminars, and self-education.  Maybe.

Me myself, I had the luck to be in the lab of someone who helped found the field
of developmental molecular biology and genomics and insisted that we
learn a lot of background, but this is hard to pull off as a young
prof -- trust me.  I also came into bio from a weird background of
computing, math, and physics.  Institutionalizing either of these
things is impossible.

The meta-problem, of course, is that if we really want to bring computing
into biology, or Big Data into wide use, we need to confront not just
the manpower gap but the meta-gap: the lack of training programs in
this area.  The NSF has offered an IGERT-CIF21 training program grant in
Big Data for just this reason, but they're only going to award 2 this year
-- *two*.  And each will train only about ~30 grad students in 5 years.

For comparison, we received 169 applications for 24 spots in our NGS
course last year, including applications from more than 20 tenure-line
faculty.  I could almost do an IGERT-CIF21 *just with the faculty
applicants*.  (Assuming they wanted to get another PhD, of course.
Hmmmmmmm.)

Another problem is that even if the NSF offered lots more money for
training, these grants come with little institutional overhead (which
is what universities value); one chair told me that if I'd asked
before getting into it, he'd have discouraged me from participating in
the IGERT, because it is likely to be a lot of work for little respect
or reward (see: Incentives, above).  I'm already running into this
with my `Analyzing Next Generation Sequencing Data course
<http://bioinformatics.msu.edu/ngs-summer-course-2013>`__, which is
`lot of work for little institutional reward
<ngs-course-where-next.html>`__.  Both of my chairs were downright
discouraging about a $200k education supplement that I got, because it
looked like I was "going educational", which, as everyone knows, isn't
good honest work; and I have encountered a number of obstacles putting
this grant into practice -- "sabotage" is maybe too strong a word, but I'm
certainly not being officially encouraged in any of these endeavors.
And let's not even *talk* about Software Carpentry, which is clearly a
useless effort, right, because no one gets credits for it?

<whipes froth from lips> Sorry, sometimes I just get going...

The solution, of course, is money.  Money money money.

There are rumbles that more significantly funded training efforts will
emerge from NIH, who has realized that just producing lots of data is
not as useful as producing lots of data and then analyzing it really
well, for which they need lots of trained graduate students and
postdocs.  I await with baited breath!  (That's not sarcasm -- I am
really hopeful!)

A point I tried to make at the NAS workshop panel was that since we have this
massive Big Data worker shortage, and the NSF wants to change that, we
need both undergrad and grad training programs, the bigger the better;
if Big Data really is important to research, those people will have a
competitive advantage in academia as well as in industry, and everyone
will be desperate to hire them.  So it should be a win-win-win.

3. Ontologies and standards are the real technical problem
----------------------------------------------------------

Or, "Give me but a set of primary keys, and I will pivot the world
around them."

It's no surprise that entity resolution is probably the single most
pressing challenge when integrating heterogeneous data, and making
sure that THIS value in THIS database means the same thing as THAT
value in THAT database is a fundamental semantic challenge.  In my
talk I pointed out that the first 90% of bioinformatics is identifier
munging, while the second 90% of bioinformatics is figuring out what
each different database means, exactly, by the term "gene".

In my talk, I inadvertently appeared to recommend completely ditching
ontologies and standards.  Ann Richards rightly took me to task (at
length) for this in the Q&A session ;).  Ewan Birney and Barbara Wold
said what I should have said: there is a sweet spot between rigor and
"winging it" in ontology and standard development, and one of the best
ways to find the sweet spot is to get real live practitioners to
engage in this development.  Or, to paraphrase Stephen Friend,
individual researchers working on a particular problem come up with a
partial solution, and then iterating, seem to be better at standards
development than are committees.

I have avoided standards and ontologies as much as possible, and will
probably continue to do so; I have never heard someone talk about
their time on an ontology development project with enthusiasm, and I
am personally much better at winging it then at any sort of advance
planning.  So I don't have much more to say other than that it seems
like a really hard problem.  But I asked around: Before the meeting, I
tapped into an old friend of mine who works in data quality in a
non-academic field -- Clint Bidlack of ActivePrime.  He gave me the
lay of the land, and pointed out that the general problem of
heterogeneous data integration appears to rival the development of
truly autonomous robots in difficulty.  I will therefore be expecting
fully automated solutions to heterogeneous data integration when my
robot bartender first brings me a gin & tonic when I want one, without
my having asked.  But Clint *did* point me at an academic research
field that looked very promising: Unsupervised Feature Learning.  He
bade me watch `this video
<http://www.youtube.com/watch?v=ZmNOAtZIgIk>`__, but pointed out that
this is still a deep research topic with limited practical
applicability so far.

----

Overall, a very interesting meeting that got me thinking hard about some
interesting problems.

--titus
