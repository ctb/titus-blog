Annotating papers with pipeline steps - suggestions?
####################################################

:author: C\. Titus Brown
:tags: replication
:date: 2014-11-30
:slug: 2014-annotating-paper-results
:category: science

A few months ago, I `wrote a short description
<http://ivory.idyll.org/blog/2014-our-paper-process.html>`__ of how we
make our papers replicable in the lab.  One problem with this process
is that for complex pipelines, it's not always obvious how to connect
a number in the paper to the steps in the pipeline that produced it --
there are lots of files and outputs involved in all of this.  You can
sometimes figure it out by looking at the numbers and correlating with
what's in the paper, and/or trying to understand the process from the
bottom up, but that's quite difficult.  Even my students and I (who
can meet in person) sometimes have trouble tracking things down
quickly.

Now, on my latest paper, I've started annotating results in the paper
source code with Makefile targets.  For example, if you are interested
in how we got `these results
<https://github.com/ctb/2014-streaming/blob/ce017f19954c9de77f1fb469c864078c928c51d2/paper/2014-streaming.tex#L163>`__,
you can use the comment in the LaTeX file to go straight to `the
associated target in the Makefile
<https://github.com/ctb/2014-streaming/blob/f94fa5124329ee2e95bea20094448ca164c4bfb3/pipeline/Makefile#L76>`__.

That's pretty convenient, but then I got to thinking -- how do we
communicate this to the reader more directly?  Not everyone wants to
go to the github repo, read the LaTeX source, and then go find the
relevant target in the Makefile (and "not everyone" is a bit of an
understatement :).  But there's no reason we couldn't link directly to
the Makefile target in the PDF, is there?  And, separately, right now
it is a reasonably large burden to copy the results from the output of
the scripts into the LaTeX file.  Surely there's a way to get the
computer to do this, right?

So, everyone -- two questions!

First, assuming that I'm going the nouveau traditional publishing route
of producing a PDF for people to download from a journal site, is
there a good, or suggested, or even better yet journal-supported way
to link directly to the actual computational methods?  (Yes, yes, I
know it's suboptimal to publish into PDFs. Let me know when you've got
that figured out, and I'll be happy to try it out. 'til then kthxbye.)
I'd like to avoid intermediaries like individual DOIs for each method,
if at all possible; direct links to github FTW.

Ideally, it would make it through the publishing process.  I could,
of course, make it available as a preprint, and point interested
people at that.

Second, what's a good way to convey results from a script into a LaTeX
(or more generally any *text* document)?  With LaTeX I could make use of
the 'include' directive; or I could do something with templating; or...?

Well, and third, is there any (good, scriptable) way to do both (1)
and (2) at the same time?

Anyway, hit me with your wisdom; would love to hear that there's already
a good solution!

--titus

