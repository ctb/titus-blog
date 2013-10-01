September 2013 workshops
########################

:author: C\. Titus Brown
:tags: teaching
:date: 2013-09-20
:slug: 2013-teaching-workshops
:category: science

I just finished my third workshop in two weeks.  I taught 3.5 days of
`microbial bioinformatics
<http://2013-caltech-workshop.readthedocs.org>`__ at Caltech, 2 days
of `intro computing for biologists
<http://2013-msu-zero-entry.readthedocs.org>`__ at MSU, and another
2-day `intro computing for biologists
<http://2013-uw-zero-entry.readthedocs.org>`__ workshop at UW.  The
Caltech workshop was sponsored by CEMI, the Caltech Environmental
Microbial Initiative; the MSU workshop was co-sponsored by `BEACON
<http://beacon-center.org>`__ and `iCER <http://www.icer.msu.edu>`__;
and the UW workshop was co-sponsored by `BEACON
<http://beacon-center.org>`__ and `the eScience Institute
<http://escience.washington.edu>`__.

All three of the workshops made use of `Amazon Web Services
<http://aws.amazon.com>`__.  And, of course, all workshop materials
are on github and freely available for use and reuse under CC0
(see `Caltech <http://github.com/ged-lab/2013-caltech-workshop/>`__, `MSU <http://github.com/ged-lab/2013-msu-zero-entry>`__, and `UW <https://github.com/beacon-center/2013-uw-zero-entry>`__ materials).

The more extended workshop at Caltech (taught with Chris Welcher and
Yoshiki Baeza, continuing 1.5 days of an intro to QIIME by Rob Knight)
was modeled on our `2013 summer course on NGS
<http://ged.msu.edu/angus/tutorials-2013/>`__, with students spinning
up their own Amazon machines and installing their own software.
About 40 people attended.

The other two workshops were much shorter, about 10 hours each.
Rather than asking everyone to start up their own EC2 machines, we
instead booted up 5-6 big instances, gave students the root key file,
taught 'em to log in with SSH and IPython Notebook,
and wrote up tutorials that made students avoid stepping on each
other's files.

The MSU workshop (co-taught by Tracy Teal and Jory Schossau) had about
50 attendees.  We ran into a fun problem on the second day, where
neither the A/V system nor the teleconferencing system worked due to a
network outage.  I ended up lecturing about stats and coin flipping on
the whiteboard while a student went to get an extra projector... fun
times!

The UW workshop, also attended by about 50 people the first day and 35
people the second day, worked almost flawlessly.  Tracy did not come
out to Seattle with us, so Jory covered both the shell and the Monty
Hall problem, and also did yeoman duty TAing.

In both of the latter workshops I adopted a strategy conveyed to me by
April Wright (`@wrightingapril <https://twitter.com/wrightingapril>`__) at the `"What to Teach Biologists About
Computing" <http://ivory.idyll.org/blog/2013-sesync-meeting.html>`__
meeting: a so-called "zero-entry" strategy, in which I stressed that
**no prior computational experience was needed**.  We then followed through: in these workshops,
we walked people through basic shell, basic IPython Notebook, basic
data analysis and graphing, and basic simulations, and we took real
pains to assume that the students had never seen anything
like it.  We tried to motivate everything with biology, too.

I used this "zero-entry" strategy as a way to make sure that people
who might have `impostor syndrome <http://t.co/U32Ul059XM>`__ felt
welcome.  I can't yet tell whether people felt that it was too basic
(we'll be sending out surveys soon) but I received a number of
comments during the workshop that made me think it wasn't a total
failure.

Of significant note, we had at most 2 installation problems during the
workshops (so, 2-4% of students) as opposed to the usual 20% or so for
Software Carpentry.  I think this is a real benefit of the cloud computing
approach we use for these non-Software Carpentry workshops.

We'll see what kind of long-term feedback I get, but I feel reasonably
confident that the courses served their primary purpose of bringing
students of my `10-week long fall course
<http://ged.msu.edu/courses/2012-fall-cse-891/>`__ up to some basic
level of familiarity with the means and the rationale for doing
computing in biology.

Jory (who regularly teaches Software Carpentry) made one interesting
comment: he said that he was amazed that people seemed happy starting
at such a basic level!  I think that very few computationally capable
people recognize how little most people know about computing, and this
is an obstacle for the people trying to learn it: one person at the UW
workshop told me that she was really glad we were starting at this
basic level, because all the local R workshops started a bit past
anything she knew already.

Amazon Web Services strategies
------------------------------

I've now used three different AWS strategies with success:

1) Spin up machines for 'em.  This is least tricky: I just boot N
   machines up and configure them, and students connect via keypair or
   IPython Notebook.

2) IAM.  Amazon offers a somewhat complex username/password subaccount
   management scheme for regular AWS accounts: you can have multiple
   "users" that all have various rights to start up machines, etc.
   My least favorite of the options, because it's tricky to get the
   rights right, but good for classes where you want to teach booting
   up a cloud machine but don't want to require that everyone
   have a credit card.

3) Students create their own accounts and boot up their own machines.

   This is the most powerful, because the students then know how to do
   all of the tutorials on their own.

Which one I use depends on what kind of workshop I'm teaching: who the
attendees are, what the goal is, whether I've got an AWS grant, etc.
But they all work pretty well.

Why am I doing all of this work?
--------------------------------

Jory asked me a very good question: why am I spending so much time
teaching?? I blew about two weeks on all this stuff just in September,
for no $$ reward and little in the way of direct return!  Plus, I'm
mostly teaching intro stuff that "anyone can teach", that isn't
directly research relevant.  I spend about two months of each year now
preparing and doing workshops, I think.

Well, I came up with five reasons:

1. It's sometimes part of my job.  The two-day workshops actually
   speak to my teaching duties this term, for example.  My summer workshop
   is NIH funded and while I roped myself into it, it's now my job :)

2. It's fun! I spent a week at Caltech (old stomping grounds), and two
   days out in Seattle, eating good food and chatting about science
   with interesting people.

3. Ultimately we need to scale teaching, but we don't know how, so I
   feel the need to spend time hacking on the process. For example,
   with the success of these two-day workshops, I now think I could
   teach other people to teach them at this point, although they'd
   have to spend a fair bit of time in preparation the first time or
   two.

4. I like to think I'm making a difference.  People tell me they're
   learning stuff and I like to believe them ;).

5. Science is the best hope for humanity's future progress.  One thing
   that Greg Wilson and I have in common is that we actually *believe*
   that more efficient and better quality science is critical to our
   future, and, more importantly, the future of our kids.
   
6. It's career boosting!

Whoops, that's *6* reasons... all I can say is that if people
understood how well all this teaching and workshop stuff worked to
boost careers, everyone would be doing it. It's so easy and effective
that it feels like cheating ;).

--titus
