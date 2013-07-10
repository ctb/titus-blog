"What to Teach Biologists about Computing" - the morning after
##############################################################

:author: C\. Titus Brown
:tags: teaching,learning,software carpentry
:date: 2013-07-10
:slug: 2013-sesync-meeting
:category: science

We all know that biology (along with other sciences) is becoming ever
more data intensive.  Biologists (among other scientists) are not
terribly well prepared for this, because of a lack of computational
culture, lack of computational training, and a lack of tools.  What
do they need to know?

This question drove us in organizing a July 8 & 9, 2013 meeting at
`SESYNC <http://www.sesync.org>`__, in Annapolis, MD.  Greg Wilson (of
`Software Carpentry <http://software-carpentry.org>`__) and I (`MSU
<http://www.msu.edu>`__/`BEACON <http://beacon-center.org>`__)
co-organized it: I provided the money (via an NSF grant), Greg
provided the advice on how to spend it :).

A truly fantastic group of people deigned to attend -- I discovered
that one real value of having blogged, taught, and proselytized open
science, education, and training for years, is that even when you
invite people to a hot, muggy locale in the middle of summer, *they
come*!  We ended up a pretty diverse group of people, almost all
actively and energetically involved in some form of teaching, with
many focused on teaching computing to biologists.

We spent two days discussing, brainstorming, pitching, and outlining
ideas to and at each other.  We generated a 500 line+ Etherpad
document in the process, and Greg has said that he will try to
summarize things in some upcoming blog posts.  However, since I'm
still riding the enthusiasm and energy of the meeting, I thought I'd
blog a few of my morning-after thoughts -- nothing systematic, just
some of what stuck.

Mixing up activities is really important!
-----------------------------------------

The social and topic mixing is even more important than I thought.  I
arrived early Monday morning due to travel delays, and was fried for
much of the day, so Greg ran things on Monday; we had a few
presentations, a breakout session to write a "driver's license" for
biologists who wanted to use computing, a use-case writing stint, and
(carried over to Tuesday) an opportunity to pitch an idea to the group
as a whole.  In contrast, I organized... a few whole-classroom
discussions, which, while useful, were kind of boring and
un-energetic.  If I had to take one thing away from this organizing
experience, it's that smart, creative, and dedicated people don't mind
non-linear conference flow, and in fact can profit from a certain
amount of creative chaos to mix things up.

Everyone who actively teaches has something to contribute
---------------------------------------------------------

For example,

I asked people, what do you do to keep your online material up to
date?  A perennial problem for trainers is that the pace of change
in technology makes most material go stale relatively quickly, and
it's hard to detect and takes time to fix.

I was hoping for a few nuggets of wisdom -- things that I, with my
vast experience and ginormous brain (<- sarcasm), had not prioritized
or emphasized.  I got much, much more, in terms of practical
experiences from other people!  People are actively using a mix of
continuous integration, high trainer turnover with active remixing,
doctest-style output generation, interspersing flipped material with
lots of in-person courses (which makes sure the flipped material stays
up to date), and "report an error" buttons.  No magic bullets, but,
collectively, a set of attitudes and low- and high-tech approaches that
provide a wide range of options.

More importantly, I realized that stale material that no one looks at
is rather unimportant; and that there really was no magic bullet.
(See also "Now I know what no one knows," below.)

Syndication!
------------

Vicky Schneider-Gricar of TGAC, Cath Brooksbank of EBI, and I spent a
fair amount of time chewing over the problem of sharing content --
how can I usefully share content with Vicky, when they want to change
and customize it?  How can Vicky keep up to date with my fixes?

Then Nirav Merchant of iPlant uttered the word "syndication".

Right.  Duh.  Syndicating each other's content is the right way to do this.

OK, the technology and processes don't really exist for this in training
materials, as far as we could tell, but I betcha we can beg, borrow,
and steal them from other areas.

So now I'm planning a hackathon around the idea of developing
practical, documented, and easy to execute workflows based on
syndicating existing content.

Data sharing
------------

Everybody agreed that `figshare <http://figshare.com>`__ was what we
should be teaching for basic data sharing.  I was surprised at the
unanimity on this point -- the only negative bit was that we worried
that figshare would go the way of Mendeley, and be bought out by
an untrustworthy actor.

A bunch of reasons to use the command line (or not)
---------------------------------------------------

Vicky's 5 minute pitch was to have all of us -- in the remaining
4 minutes and 30 seconds -- pair up and write three reasons why
the command line is (or is not) important for biologists to learn.

Here are some of the results:

 - showing them that they can automate stuff that currently takes them ages

 - showing them how it helps the, to reproduce/repeat things

 - being able to do things in a less error-prone manner-doing things manually may introduce human errors.

 - saves time

 - makes it easier to automate, link stuff together

 - identifying a package necessary to perform derived analysis then show how to download and install through command line

 - give tasks like renaming 100 files manually win 10min: see how slow many errors then show very fast and accurate on command line

 - show simple common data + problem: solve it: data transformation problem

 - Make commands available (like R): side-by -side cheat sheets for common commands_cut-paste sampler

 - Lots of useful tools require command line input

 - you can automate some of your processes + save time for beer-drinking

 - you can modify packages that ALMOST do what you want

 - not for everyone, specify group need

 - working with large amounts of data and compute is easier on the command line (but may change)

 - command lines do not lie

 - if you want to be involved in active research in five years you need it.

 - direction of where science is going is going to depend more and more on comp. literacy

 - fetching, access to data speeds up research

 - it's fun

 - more empowering

 - always get latest versions of programs

 - provides record of what you actually did

 - run on bigger computer-provide speed efficiency

 - provides ability to repeat tasks easily

 - example command line versus excel for tasks of interest tobiologists (data crunching), lead/proof by example/hand-on

 - repeat (lead by example) for workflow (R or Python script vs screen shots)

 - buy them or provide them with a copy of "Data Crunching" (Greg's :-)

I didn't really sift through them yet, but there are some gems in there.

Now I know what no-one knows
----------------------------

One important outcome for me was this: there are many approaches to
w2tbac that have not been tried, or not tried thoroughly.  Once you
know what people *have* tried, and understand what they are doing
currently, you have two valuable pieces of information: a list of
people to go talk to about how they do what they do & what hasn't
worked; and, equally, some idea of what hasn't been tried and might be
worth trying.

More succinctly, I now have a much better idea (through the process of
elimination :) of what has not been tried!

Other outcomes
--------------

We came out with some ideas that we really want to try and that I
think will actually happen.  Syndication, above; focusing more on
building lessons around narrative paths; collaboration on protocols &
questionnaires for assessment; trying to share more of the process of
recovering from errors; and thinking more about blended learning,
where we regard online training as one component of training, and
don't force a false dichotomy between online and in-person training.

My personal TODOs
-----------------

My TODO list now includes:

1. Implementing a "data biologist" driver's license quiz;

2. Write up an Excel -> R/Python day-long lesson;

3. Go out to iPlant to grok their cloud-for-scientists infrastructure;

4. Run a focused workshop at NEON;

5. Develop a simple, short, common pre- and post- questionnaire for
   workshop assessment, for those workshops that are bio focused;

6. Integrate IPython Blocks and IPython Browsercast into my term-long
   course on Computing for Evolutionary Biologists;

7. Start making cheat-sheets one of the specific products of my various
   training activities;

8. Get permission from instructors to relicense `all of the NGS course material <http://ged.msu.edu/angus/>`__ under CC0;

9. Arrange a week-long hackathon somewhere nice;

and hey, look, I have funding and/or motivation for all of that. Yay!

--titus
