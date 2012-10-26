Our approach to replication in computational science
####################################################

:author: C\. Titus Brown
:tags: science,bioinformatics,python,ipython,diginorm
:date: 2012-04-02
:slug: replication-i
:category: science


I'm pretty proud of our most recently posted paper, which is on a
sequence analysis concept we call `digital normalization
<http://ged.msu.edu/papers/2012-diginorm/>`__.  I think the paper is
pretty kick-ass, but so is the way in which we're approaching
replication.  This blog post is about the latter.

(Quick note re "replication" vs "reproduction": The distinction
between replication and reproducibility is, from what I understand,
that "replicable" means "other people get exactly the same results
when doing exactly the same thing", while "reproducible" means
"something similar happens in other people's hands".  The latter is
far stronger, in general, because it indicates that your results are
not merely some quirk of your setup and may actually be right.)

So what did we do to make this paper extra super replicable?

If you go to the `paper Web site
<http://ged.msu.edu/papers/2012-diginorm/>`__, you'll find:

 - a link to the paper itself, in preprint form, stored at the arXiv
   site;

 - a tutorial for running the software on a Linux machine hosted in
   the Amazon cloud;

 - a git repository for the software itself (hosted on github);

 - a git repository for the LaTeX paper and analysis scripts (also
   hosted on github), including an ipython notebook for generating the
   figures (more about *that* in my next blog post);

 - instructions on how to start up an EC2 cloud instance, install the
   software and paper pipeline, and build most of the analyses and all
   of the figures from scratch;

 - the data necessary to run the pipeline;

 - some of the output data discussed in the paper.

(Whew, it makes me a little tired just to type all that...)

What this means is that you can regenerate substantial amounts (but
not all) of the data and analyses underlying the paper from scratch,
all on your own, on a machine that you can rent for something like 50
cents an hour.  (It'll cost you about \\$4 -- 8 hours of CPU -- to
re-run everything, plus some incidental costs for things like downloads.)

Not only *can* you do this, but if you try it, it will actually *work*.
I've done my best to make sure the darn thing works, and this is the
actual pipeline we ourselves ran to produce the figures in the paper.
All the data is there, and all of the code used to process the data,
analyze the results, and produce the figures is *also* there. In
version control.

When you combine that with the ability to run this on a specific EC2
instance -- a combination of a frozen virtual machine installation and
a specific set of hardware -- I feel pretty confident that at least
*this* component of our paper is something that can be replicated.

A few thoughts on replicability, and effort
-------------------------------------------

Why did I go to all this trouble??

**Wasn't it a lot of work?**

Well, interestingly enough, it wasn't *that* much work.  I already
use version control for everything, including paper text; posting it
all to github was a matter of about three commands.

Writing the code, analysis scripts, and paper was an immense amount of
work.  But I had to do that anyway.

The most extra effort I put in was making sure that the big data files
were available.  I didn't want to add the the 2gb E. coli resequencing
data set to git, for example.  So I ended up tarballing those files
sticking them on S3.

The Makefile and analysis scripts are ugly, but suffice to remake
everything from scratch; they were already needed to make the paper,
so in order to post them all I had to do was put in a teensy bit of
effort to remove some unintentional dependencies.

The ipython notebook used to generate the figures (again -- next blog
post) was probably the most effort, because I had to learn how to use
it, which took about 20 minutes.  But it was one of the smoothest
transitions into using a new tool I've ever experienced in my ~25 years
of coding.

Overall, it wasn't that much extra effort on my part.

**Why bother in the first place??**

The first and shortest answer is, because I could, and because I
believe in replication and reproducibility, and wanted to see how
tough it was to actually do something like this.  (It's a good deal
above and beyond what most bioinformaticians do.)

Perhaps the strongest reason is that our group has been bitten a lot
in recent months by irreplicable results.  I won't name names, but
several Science and PNAS and PLoS One papers of interest to us turned
out to be basically impossible for us to replicate.  And, since we are
engaged in developing new computational methods that must be compared
to previous work, an inability to
regenerate *exactly* the results in those other papers meant we had to
work harder than we should have, simply to reproduce what they'd done.

A number of these problems came from people discarding large data sets
after publishing, under the mistaken belief that their submission to
the Short Read Archive could be used to regenerate their results.
(Often SRA submissions are unfiltered, and no one keeps the filtering
parameters around...right?)  In some cases, I got the right data sets
from the authors and could replicate (kudos to Brian Haas of Trinity
for this!), but in most cases, ixnay on the eplicationre.

Then there were the cases where authors clearly were simply being bad
computational scientists.  My favorite example is a very high profile
paper (coauthored by someone I admire greatly), in which the script
they sent to us -- a script necessary for the initial analyses -- had
a *syntax error* in it.  In that case, we were fairly sure that the
authors weren't sending us the script they'd actually used...  (It was
Perl, so admittedly it's hard to tell a syntax error from legitimate
code, but even the Perl interpreter was choking on this.)

(A few replication problems came from people using closed or
unpublished software, or being hand-wavy about the parameters they
used, or using version X of some Web-hosted pipeline for which only
version Y was now available.  Clearly these are long-term issues that
need to be discussed with respect to replication in comp. bio., but
that's another topic.)

Thus, my group has wasted a lot of time replicating other people's
work.  I wanted to avoid making other people go through that.

A third reason is that I really, really, really want to make it easy
for people to pick up this tool and *use* it.  Digital normalization
is super ultra awesome and I want as little as possible to stand in
the way of others using it.  So there's a strong element of
self-interest in doing things this way, and I hope it makes diginorm
more useful.  (I know about a dozen people that have already tried it
out in the week or so since I made the paper available, which is
pretty cool.  But citations will tell.)

What use is replication?
------------------------

Way back when, `Jim Graham politely schooled me
<http://www.scimatic.com/node/361>`__ in the true meaning of
reproducibility, as opposed to replication.  He was about 2/3 right,
but then he went a bit too far and said

   But let's drop the idea that I'm going to take your data and your
   code and "reproduce" your result. I'm not. First, I've got my own
   work to do. More importantly, the odds are that nobody will be any
   wiser when I'm done."

Well, let's take a look at that concern, shall we?

With the benefit of about two years of further practice, I can tell
you this is a dangerously wrong way to think, at least in the field of
bioinformatics.  My objections hinge on a few points:

First, based on our experiences so far, I'd be surprised if the
authors themselves could replicate their own computational results --
too many files and parameters are missing.  We call that "bad
science".

Second, odds are, the senior professor has little or no detailed
understanding of what bioinformatic steps were taken in processing the
data, and moreover is uninterested in the details; that's why they're
not in the Methods.  Why is that a problem?  Because the odds are
quite good that many biological analyses *hinge critically* on such
points.  So the peer reviewers and the community at large need to be
able to evaluate them (see `this RNA editing kerfuffle
<http://seqanswers.com/forums/showthread.php?t=18501>`__ for an
excellent example of reviewer fail).  Yet most bioinformatic pipelines
are so terribly described that even with some WAG I can't figure out
what, roughly speaking, is going on.  I certainly couldn't replicate
it, and generating specific critiques is quite difficult in that kind
of circumstance.

Parenthetically, Graham does refer to the climate sciences `struggles
with reproducibility and replication
<http://www.realclimate.org/index.php/archives/2009/02/on-replication/langswitch_lang/in/>`__.  If only they put the same effort into replication and
data archiving they did into arguing with climate change deniers...

Third, Graham may be guilty of physics chauvinism (just like I'm
almost certainly guilty of bioinformatics chauvinism...) Physics and
biology are quite different: in physics, you often have a theoretical
framework to go by, and results should at least roughly adhere to that
or else they are considered guilty until proven innocent.  In biology,
we usually have no good idea of what we're expecting to see, and often
we're looking at a system for the very first time.  In that
environment, I think it's important to make the underlying computation
WAY more solid than you would demand in physics (see RNA editing above).

As Narayan Desai pointed out to me (following which I then put it in
my `PyCon talk (slide 5)
<http://www.slideshare.net/c.titus.brown/pycon-2011-talk-ngram-assembly-with-bloom-filters>`__),
physics and biology are quite different in the way data is generated
and analyzed.  There's fewer sources of data generation in physics,
there's more of a computational culture, and there's more theory.
Having worked with physicists for much of my scientific life (and
having published a number of papers with physicists) I can tell you
that replication is certainly a big problem over there, but the
*consequences* don't seem as big -- eventually the differences between
theory and computation will be worked out, because they're far more
noticeable when you *have* theory, like in physics.  Not so in biology.

Fourth, a renewed emphasis on computational methods (and therefore on
replicability of computational results) is a natural part of the
transition to `Big Data biology
<ivory.idyll.org/blog/mar-12/big-data-biology>`__.  The quality of
analysis methods matters A LOT when you are dealing with massive
data sets with weak signals and many systematic biases.  (I'll write
about this more later.)

Fifth, and probably most significant from a practical perspective,
Graham misses the point of *reuse*.  In bioinformatics, it behooves us
to reuse proven (aka published) tools -- at least we know they worked
for *someone*, at least once, which is not usually the case for newly
written software.  I don't pretend that it's the responsibility of
people to write awesome reusable tools for every paper, but sure as
heck I should expect to be able to *run* them on *some* combination of
hardware and software.  Often that's not the case, which means I get
to reinvent the wheel (yay...) even when I'm doing the same stupid
thing the last five pubs did.

For our paper, khmer and screed should be quite reusable.  The
analysis pipeline for the paper?  It's not that great.  But at least
you can run it, and potentially steal code from it, too.

When I was talking to a colleague about the diginorm paper, he said
something jokingly: "wow, you're making it way too easy for people!"
-- presumably he meant it would be way to easy for people to criticize
or otherwise complain about the specific way we're doing things.
Then, a day or two later he said, "hmm, but now that I think of it, no
one ever uses the software we publish, and you seem to have had better
luck with that..."  -- recognizing that if you are barely able to run
your own software, perhaps others might find it even more difficult.

Heck, the diginorm paper itself would have been far harder to write
without the data sets from the `Trinity paper
<http://www.ncbi.nlm.nih.gov/pubmed?term=21572440>`__ and the
`Velvet-SC paper
<http://www.ncbi.nlm.nih.gov/pubmed?term=21926975>`__.  Having those
nice, fresh, well-analyzed data sets already at hand was *fantastic*.
Being able to *run Trinity* and reproduce their results was *wonderful*.

There's a saying in software engineering: "one of the main people you
should be programming for is yourself, in 6 months."  That's also true
in science -- I'm sure I won't remember the finer details of the
diginorm paper analysis in 2 years -- but I can always go look into
version control.  More importantly, new graduate students can go look
and really see what's going on.  (And I can use it for teaching, too.)
And so can other people working with me.  So there's a lot of utility
in simply nailing everything down and making it runnable.

Replication is by no means sufficient for good science.  But I'll be
more impressed by the argument that "replication isn't all that
important" when I see lack of replication as the exception rather than
the rule.  Replication is essential, and good, and useful.  I long for
the day when it's not *interesting*, because it's so standard.  In
the meantime I would argue that it certainly doesn't do any harm to
emphasize it.

(Note that I really appreciate Jim Graham's commentary, as I think he
is at worst *usefully* wrong on these points, and substantially
correct in many ways.  I'm just picking on him because he wrote it all
down in one place for me to link to, and chose to use the word 'sic'
when reproducing my spelling mistake.  Low blow ;)

The future
----------

I don't pretend to have all, or even many, of the answers; I just like
to think about what form they might take.

I don't want to argue that this approach is a panacea or a
high-quality template for others to use, inside or out of
bioinformatics.  For one thing, I haven't automated some of the
analyses in the paper; it's just too much work for too little benefit
at this point.  (Trust me, they're easy to reproduce... :).  For
another, our paper used a fairly small amount of data overall; only a
few dozen gigabytes all told.  This makes it easy to post the data for
others to use later on.  Several of our next few papers will involve
over a half terabyte of raw data, plus several hundred gb of ancillary
and intermediate results; no idea what we'll do for them.

Diginorm is also a somewhat strange bioinformatics paper.  We just
analyzed other people's data sets (an approach which for some reason
isn't in favor in high impact bioinformatics, probably because high
impact journal subs are primarily reviewed by biologists who want to
see cool new data that we don't understand, not boring old data that
we don't understand).  There's no way we can or should argue that 
biological replicates done in a different lab should *replicate* the
results; that's where reproducibility becomes important.

But I would like it if people *considered* this approach (or some
other approach) to making their analyses replicable.  I don't mind
people rejecting good approaches because they don't fit; to each their
own.  But this kind of limited enabling of replication isn't that
difficult, frankly, and even if it were, it has plenty of upsides.
It's definitely not irrelevant to the practice of science -- I would
challenge anyone to try to make *that* claim in good faith.

--titus

p.s. I think I have to refer to this `cancer results not reproducible <http://news.yahoo.com/cancer-science-many-discoveries-dont-hold-174216262.html>`__ paper somewhere.  Done.


----

**Legacy Comments**


Posted by Jorgen on 2012-04-02 at 05:24. 

::

   Great post. It's encouraging to see that you care about
   reproducibility in bioinformatics. Now we need to get the reviewers on
   our side: A github page for every paper and all figures and tables
   reproducible with a single 'make' :)    PS: The pyCon-slide link is
   actually pointing to the cancer-not-reproducible link.


Posted by Ben on 2012-04-02 at 09:28. 

::

   I have struggled with reproducing (or replicating) others'
   computational work, as well. This is a fantastic post! I wish more
   computational biologists thought like you do!


Posted by Titus Brown on 2012-04-02 at 10:42. 

::

   Thanks, Jorgen -- updated.  Thanks, Ben!


Posted by David Escott on 2012-04-02 at 16:50. 

::

   Most institutions have required courses in intro statistics for field
   X, but I feel that what would be more useful is a required course in
   version control. The fact that you even know how to use git (sadly)
   puts you well beyond what is known in a wide array of fields. Keep up
   the good work.


Posted by Michael Kellen on 2012-04-03 at 01:10. 

::

   Great to see someone who is so thoughtful and complete in their work.
   Have spent some time looking at GitHub myself as we look to develop a
   similar system targeted at the data analysis space <a
   href="http://wp.me/p2faIU-y">http://wp.me/p2faIU-y</a>


Posted by Raphael on 2012-04-03 at 07:39. 

::

   Great work, great post. I'm looking forward to the ipython notebook!


Posted by Steve P on 2012-04-04 at 10:47. 

::

   Nice post. I've been working on a replication pipeline for a couple
   papers I'm writing. Mine is just a bunch of bash scripts that invoke
   Python and R scripts. I guess I wasn't too worried about platform
   issues, such that I would need to wrap it in a virtual machine, but
   maybe I should be. I definitely agree with your points about how this
   exposes you to more scrutiny, because people can actually pick apart
   the precise steps you took, and you sometimes have to make arbitrary
   decisions that may have a substantial impact on your results.


Posted by Kris on 2012-04-04 at 17:34. 

::

   This is great stuff.  In some venues it might be appropriate to
   require or at least strongly suggest this material be provided during
   peer review.  Sadly, this would really increase the level of effort
   required by a reviewer -- but it would also likely really increase the
   quality of the review!


Posted by Anthony Scopatz on 2012-04-07 at 17:12. 

::

   Titus, how important is the VM / EC2 instance that you are using is to
   the replication - reproducibility distinction?  Given the definition
   of replication here it seems that being able to run on the same
   hardware and in the same computing environment is critical.    For
   example, obtaining the same or similar results using different
   versions of the Linux kernel (say v3.3.1 vs v2.6.35) would be
   reproduction, not replication.  Similarly, if you use different
   chipsets this is reproduction.    With replication being narrowly
   defined as having full equality over the hardware and software stack,
   reproducibility certainly is the harder problem.  Knowing which of the
   hundreds of thousands of extrinsic variables actually may matter to a
   result is a hard problem in general.  However, this is where testing
   &amp; debugging come in and ensure that a code works on many classes
   of systems.    Note that I just trying to get a handle on when it is
   appropriate to use these two terms.  I am not criticizing the good
   &amp; noble pursuit of replication.  I dream of the day where
   replication, testing, v&amp;v, and uq are just done as a matter of
   course in the sciences.      tl;dr: replication is when you have full
   control over the hardware and software stack and reproduction is
   anything else where the tests still pass and you obtain the same basic
   results, right?


Posted by Titus Brown on 2012-04-07 at 21:06. 

::

   Hey Anthony... yeah, good questions.  No idea how to respond.  I'm
   sure there's a fuzzy boundary between replication and reproduction,
   but not sure how to delineate.


Posted by steven mosher on 2012-04-08 at 17:12. 

::

   Great post..

