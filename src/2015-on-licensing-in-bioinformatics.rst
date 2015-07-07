On licensing bioinformatics software: use the BSD, Luke.
########################################################

:author: C\. Titus Brown
:tags: khmer,bsd,gpl,kallisto,lior-is-wrong
:date: 2015-07-07
:slug: 2015-on-licensing-in-bioinformatics
:category: science

If a piece of bioinformatics software is not fully `open source
<http://opensource.org/licenses>`__, my lab and I will generally seek
out alternatives to it for research, teaching and training.  This holds
whether or not the software is free for academic use.

If a piece of bioinformatics software is only available under `the GNU
Public License <http://opensource.org/licenses/gpl-license>`__ or another
`"copyleft" license <http://www.gnu.org/copyleft/copyleft.en.html>`__,
then my lab and I will absolutely avoid integrating any part of it
into our own source code, which is mostly BSD.

Why avoid non-open-source software?
-----------------------------------

We avoid non-open-source software because it saves us future
headaches.

Contrary to `some assumptions
<https://twitter.com/lpachter/status/618435476752437248>`__, this is
not because I'm anti-company or against making money from software,
although I have certainly chosen to forego that in my own life.  It's
almost entirely because such software is an evolutionary dead end, and
hence time spent working with it is ultimately wasted.

More specifically, here are some situations that I want to avoid:

* we invest a lot of time in building training materials for a piece
  of software, only to find out that some of our trainees can't make
  use of the software in their day job.

* we need to talk to lawyers about whether or not we can use a piece
  of software or include some of its functionality in a workflow we're
  building.

* we find a small but critical bug in a piece of bioinformatics software,
  and can't reach any of the original authors to OK a new release.

This is the reason why I won't be investing much time or effort in
using `kallisto
<https://liorpachter.wordpress.com/2015/05/10/near-optimal-rna-seq-quantification-with-kallisto/>`__
in my courses and my research: `it's definitely not open source
<http://www.homolog.us/blogs/blog/2015/05/18/pachters-kallisto-comes-with-unconventional-license/>`__.

Why avoid copyleft?
-------------------

The typical decision tree for an open source license is between a "permissive"
BSD-style license vs a copyleft license like the GPL; see Jake
Vanderplas's `excellent post on licensing scientific code for specifics <http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/>`__.

There is an asymmetry in these licenses.

Our software, `khmer <http://github.com/dib-lab/khmer/>`__, is
available under the BSD license.  Any open source project (indeed,
*any project*) is welcome to take any part of our source code and
include it in theirs.

However, we cannot use GPL software in our code base at all.  We can't
call GPL library functions, we can't include GPL code in our codebase,
and I'm not 100% sure we can even look closely at GPL code.  This is
because if we do so, we must license our own software under the GPL.

This is the reason that I will be avoiding `bloomtree
<https://github.com/Kingsford-Group/bloomtree>`__ code, and in fact we
will probably be `following through on our reimplementation
<https://github.com/ctb/2015-khmer-sequence-bloom-trees>`__ --
bloomtree relies on both `Jellyfish
<https://github.com/gmarcais/Jellyfish>`__ and `sdsl-lite
<https://github.com/simongog/sdsl-lite>`__, which are GPL.

Why did we choose BSD and not GPL for our own code?
---------------------------------------------------

Two reasons: first, I'm an academic, funded by government grants;
second, I want to maximize the utility of my work, which means
choosing a license that encourages the most participation in the
project, and encourages the most reuse of my code in other projects.

Jake covers the second line of reasoning really nicely `in his blog
post
<http://www.astrobetter.com/blog/2014/03/10/the-whys-and-hows-of-licensing-scientific-code/>`__,
so I will simply extract his summary of John Hunter's reasoning:

   To summarize Hunter's reasoning: the most important two predictors
   of success for a software project are the number of users and the
   number of contributors. Because of the restrictions and subtle
   legal issues involved with GPL licenses, many for-profit companies
   will not touch GPL-licensed code, even if they are happy to
   contribute their changes back to the community. A BSD license, on
   the other hand, removes these restrictions: Hunter mentions several
   specific examples of vital industry partnership in the case of
   matplotlib. He argues that in general, a good BSD-licensed project
   will, by virtue of opening itself to the contribution of private
   companies, greatly grow its two greatest assets: its user-base and
   its developer-base.

I also think `maximizing remixability
<http://ivory.idyll.org/blog/research-software-reuse.html>`__ is a
basic scientific goal, and this is something that the GPL
fails.

The first line of reasoning is a little more philosophical, but
basically it comes down to a wholesale rejection of the logic in `the
Bayh-Dole act
<https://en.wikipedia.org/wiki/Bayh%E2%80%93Dole_Act>`__, which tries
to encourage innovation and commercialization of federally funded
research by assigning intellectual property to the university.  I
think this approach is bollocks. While I am not an economic expert, I
think it's clear that most innovation in the university is probably
not worth that much and should be made maximally open. From talking to
`Dr. Bill Janeway <https://twitter.com/billjaneway?lang=en>`__, I he
agrees that pre-Bayh-Dole was a time of more openness, although I'm
not sure of the evidence for more innovation during this period.
Regardless, to me it's intuitively obvious that the prospect of
commercialization causes more researchers to keep their research
closed, and I think this is obviously bad for science.  (`The Idea
Factory <http://ivory.idyll.org/blog/idea-factory-internet.html>`__
talks a lot about how Bell Labs spurred immense amounts of innovation
because so much of their research was open for use.  `Talent Wants to
be Free <http://www.amazon.com/dp/B00EZ22C6O/ref=r_soa_w_d>`__ is a
pop-sci book that outlines research supporting openness leading to
more innovation.)

So, basically, I think my job as an academic is to come up with cool
stuff and make it as open as possible, because that encourages innovation
and progress.  And the BSD fits that bill.  If a company wants to make
use of my code, that's great!  Please don't talk to us - just grab it and
go!

I should say that I'm very aware of the many good reasons why GPL
promotes a better long-term future, and until I became a grad student
I was 100% on board.  Once I got more involved in scientific
programming, though, I switched to a more selfish rationale, which is
that my reputation is going to be enhanced by more people using my
code, and the way to do that is with the BSD.  If you have good
arguments about why I'm wrong and everyone should use the GPL, please
do post them (or links to good pieces) in the comments; I'm happy to
promote that line of reasoning, but for now I've settled on BSD for my
own work.

One important note: universities like releasing things under the GPL,
because they know that it virtually guarantees no company will use it
in a commercial product without paying the university to relicense it
specifically for the company.  While this may be in the best
short-term interests of the university, I think it says all you need
to know about the practical outcome of the GPL on scientific
innovation.

Why am I OK with the output of commercial equipment?
----------------------------------------------------

Lior Pachter `drew a contrast between my refusal to teach non-free
software and my presumed teaching on sequencing output from commercial
Illumina machines
<https://twitter.com/lpachter/status/618435476752437248>`__.  I think there's
at least four arguments to be made in favor of continuing to use Illumina
while avoiding the use of Kallisto.

* pragmatically, Illumina is the only game in town for most of my
  students, while there are plenty of RNA-seq analysis programs.  So
  unless I settled on kallisto being the super-end-all-be-all of
  RNAseq analysis, I can indulge my leanings towards freedom by
  ignoring kallisto and teaching something else that's free-er.

* Illumina has a clear pricing model and their sequencing is essentially
  a commodity that needs little to no engagement from me.  This is not
  generally how bioinformatics software works :)

* There's no danger of Illumina claiming dibs on any of my results or
  extensions - we're all clear that I pays my money, and I gets my
  sequence.  I'm honestly not sure what would happen if I modified
  kallisto or built on it to do something cool, and then wanted to let
  a company use it.  (I bet it would involve talking to a lot of
  lawyers, which I'm not interested in doing.)

* James Taylor `made the excellent points
  <https://twitter.com/jxtx/status/618448066924965888 >`__ that
  limited training and development time is best spent on tools that
  are maximally available, and that don't involve licenses `that they
  can't enforce <https://twitter.com/jxtx/status/618447797109555200>`__.

----

So that's my reasoning.  I don't want to pour fuel on any licensing
fire, but I wanted to explain my reasoning to people.  I also think
that people should fight hard to make their bioinformatics software
available under a permissive license, because it will benefit everyone
:).

I should say that Manoj Samanta has been `following this line of
thought
<http://www.homolog.us/blogs/blog/2014/01/22/gpl-license-dying-world-outside-bioinformatics-aka-real-world/>`__
for much longer than me, and has written several blog posts on this
topic (`see also this
<http://www.homolog.us/blogs/blog/2013/07/31/another-reason-gpl-is-a-bad-license/>`__,
for example).

--titus
