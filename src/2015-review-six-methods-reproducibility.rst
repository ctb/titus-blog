A review of "Tools and techniques for computational reproducibility"
####################################################################

:author: C\. Titus Brown
:tags: review,reproducibility,ipynb,jupyter
:date: 2015-07-18
:slug: 2015-review-six-methods-reproducibility
:category: science

*Note:* Last week, I submitted my review of Stephen R. Piccolo, Adam
B. Lee, and Michael B. Frampton's paper, `Tools and techniques for
computational reproducibility
<http://biorxiv.org/content/early/2015/07/17/022707>`__.  Soon after,
Dan Katz wrote `a blog post about notebooks
<https://danielskatzblog.wordpress.com/2015/07/15/the-need-for-notebooks/>`__,
and in a comment I mentioned Piccolo's paper; and, after dropping a note to
Dr. Piccolo, he put it up on bioRxiv!  This, in turn, meant that I felt
comfortable posting my review - since I sign my reviews, the authors
already know who I am, so where's the harm?  See below.

----

In this paper, Piccolo et al. do a nice (and I think comprehensive?)
job of outlining six strategies for computational reproducibility.
The point is well made that science is increasingly dependent on
computational reproducibility (and that in theory we should be able to
do computational reproducibility easily and well) and hence we should
explore effective approaches that are actually being used.

I know of no other paper that covers this array of material, and this
is a quite nice exposition that I would recommend to many.  I can't
evaluate how broadly it will appeal to a diverse audience but it seems
very readable to me.

The following comments are offered as helpful suggestions, not
criticisms -- make of them what you will.

The paper almost completely ignores HPC.  I'm good with that, but it's
a bit surprising (since many computational scientists seem to think
that reproducible orchestration of many processors is an unachievable
task).  Noted in passing.

I was somewhat surprised by the lack of emphasis of version control
systems.  These are really critical in programming for ensuring
reproducibility.  I also found a missing citation! You should look at
journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001745
(yes, sorry, I'm on the paper).

Speaking of which, I appreciate the completeness of references (and
even the citation of my blog post ;) but it would be interesting to
see if Millman and Perez have anything to offer:
http://www.jarrodmillman.com/oss-chapter.html.  Certainly a good
citation (I think you hit the book, but this is a particularly good
chapter.)

I would suggest (in the section that mentions version control systems,
~line 170 of p9) recommending that authors "tag" specific versions for
the publication, even if they later recommend using updated versions.
(Too many people say "use this repo!" without specifying a revision.)

The section on literate programming could usefully mention that these
literate programming environments do not offer good mechanisms for
*long running* programs, so they may not be appropriate for things
that take more than a few minutes to run.

Also, and perhaps most important, these literate programming
environments provide REPL and can thus track exploratory data analysis
and "harden" it when it works and the author moves onto another data
analysis - so even if the authors don't want to clean up their
notebook before publication, you can track exactly how they got their
final results.  I think this is important for practical
reproducibility.  I don't know quite what to suggest in the context of
the paper but it seems like an important point to me.

Both the virtual machine and container sections should mention the
challenges of raw data bundling, which is one of the major drawbacks
here - not only is the VM large, but (unless you are partnering with
e.g. Amazon to "scale out") you must distribute potentially large data
sets.  I think this is one of the biggest practical issues facing data
intensive sciences.  (There was a nice commentary recently by folk in
human genomics begging the NIH to make human genomic data available
via the cloud; I can track it down if the authors haven't seen it.)

I think it's important to emphasize how transparent most Dockerfiles
are (and how this is a different culture than the VM deployment scene,
where configuration systems are often not particularly emphasized
except in the devops community).  I view this as one of the most
important cultural differences driving container adoption, and for
once it's *good* for science!

The docker ecosystem also seems quite robust, which is important, I think.

[ ... specific typos etc omitted ... ]

Signed,

C. Titus Brown,
ctbrown@ucdavis.edu
