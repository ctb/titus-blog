On benchmarking: when should you publish a comparison of two data analysis pipelines?
#####################################################################################

:author: C\. Titus Brown
:tags: benchmarking
:date: 2015-01-19
:slug: 2015-on-benchmarking
:category: science

A while back, someone else's graduate student asked me (slightly edited
to protect the innocent :) --

   I already have two independent sets of de novo transcriptome
   assemblies and annotations of the NGS data [...]  1) from the
   company who did the sequencing and analysis, and 2) from our
   pipeline here.  It would be great to have a third set from your lab
   to compare. Do you think such a comparison of independent analyses
   is worthwhile?

----

My response, somewhat edited:

Well, yes, and no -- first, just to make my hypocrisy clear, see:

https://peerj.com/preprints/505v1/

(which is about exactly this!)

I definitely think evaluating pipelines and assemblies is worthwhile, but at
the end of the day it's time consuming and I worry that it distracts from
the science.  My experience is that it takes a lot more time and effort
than anyone realizes before they start the project -- either that, or
the researchers do a bad job of evaluation :).  So my two guidelines (for
myself) are --

1) how reproducible is the analysis by you, and by others?  If you're
   simply evaluating what one person did against what some other
   person did, without having carefully recorded what was actually
   done, then it's all anecdatal.  In this case, no one is going to
   learn anything long term, and you shouldn't bother.

   A good way to self-evaluate here: suppose one of your reviewers
   said, "tweak these parameters because I believe that they make a
   big difference."  How long would it take you to reanalyze
   everything?  If the answer is going to be "an annoyingly long time"
   then don't write the paper in the first place!

2) Is there anything to be learned about the underlying science?  In
   our case we pushed a bit to show that though Trinity seems to have
   recovered more low abundance isoforms, we got essentially no new
   biologically relevant information out of it - something that I
   think will hold generally true for a wide range of data sets.  To
   me, that's reasonably important and useful information.  Not sure I
   would have liked the paper as much if we'd just said "hey, look, we
   get basically the same results, with some small differences. Cool?"

   A good self-evaluation question: is anyone going to find anything
   you say surprising or useful for building intuition and
   understanding?  If not, why bother doing the work?

---

So that was my response.  You'll see some of these sentiments echoed
in my blog post `about the Critical Assessment of Metagenome
Interpretation <http://ivory.idyll.org/blog/2014-on-cami.html>`__; if
you're not automating it and it's not reproducible, why bother?  The
software is going to change tomorrow and your benchmark will be
outdated.

This is also why I'm a huge fan of `nucleotid.es
<http://nucleotid.es/>`__.  These principles are also guiding
our development of `computational protocols
<http://khmer-protocols.readthedocs.org/en/latest/>`__ and `paper pipelines
<http://www.ncbi.nlm.nih.gov/pubmed/25062443>`__.  And, fundamentally,
it's why I'm planning to rain swift and sudden death down on
benchmarking and comparison papers that aren't highly reproducible.

--titus
