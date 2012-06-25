A simple idea: standard but optional review criteria for bioinformatics papers
##############################################################################

:author: C\. Titus Brown
:tags: bioinformatics,reviews,openscience
:date: 2012-05-05
:slug: blog-review-criteria-for-bioinfo
:category: science


Brad Chapman (@chapmanb on twitter) wrote and signed a nice review of
my submission to the `Bioinformatics Open Source Conference
<http://www.open-bio.org/wiki/BOSC_2012>`__.  In his review, he said
::

   My only small suggestion is to include some discussion about your
   reproducibility work during the talk: the Amazon AMI, documentation
   and reproducible ipython workflows. This is a great model for how we
   should all be doing science, and it would be interesting to hear the
   feedback you've received.  Are folks positive about it, think you
   wasted your time, or don't care either way? It's a lot of extra work
   that I and many at BOSC will appreciate, and I wonder how the broader
   scientific community has reacted.

(See `this blog post
<http://ivory.idyll.org/blog/apr-12/replication-i.html>`__ for more
info on what he was talking about.)

Since he'd signed the review, I engaged him on twitter and responded::

   @chapmanb And thanks for the nice comments on replication. Unf
   truth: no one who doesn't already think about it cares at all. Low
   impact.

and he responded ::

   @ctitusbrown That's too bad. Love to hear your thoughts at BOSC
   about how to encourage reproducibility broadly. Essential for good
   biology.

I responded ::

   @chapmanb easy -- make replicability/reproducibility of science
   matter for funding or publication :). best proxy right now? citations.

   @chapmanb within small field of bioinformatics, there is a chance,
   though: reviews. Set up an informal checklist for reviewers.

and he thought that was interesting::

   @ctitusbrown Great idea: self-policing > new incentive structure.
   Review-based word of honor amongst bioinfo, like
   http://www.paulgraham.com/patentpledge.html

So I expanded a bit::

   @chapmanb examples: "is code available? can you run code? is data
   available? is format of data documented? can you run code on data?"

   @chapmanb Maybe a Web checklist providing a 1-10 text output for
   reviewers to copy/paste: "Totally irreplicable" => "Replication is easy".

Along that line, then, here are some initial thoughts on just such a
checklist.  The idea would be to put up a little JavaScript page with
checkboxes linked to some copy-pastable text at the bottom.  The
checkboxes could be "yes", "no", or "n/a"; the text at the bottom
would provide a summary, together with a tally of all the "yes"
divided by the "yes" + "no" numbers.

If you were then tasked with reviewing a paper that had some
bioinformatics in it, you could go to the Web page, click through the
questions, and then copy/paste the text into your review.  This would
relieve reviewers of the burden of remember exactly what the important
replication issues are, and also give them a simple reporting mechanism.
If reviewers felt a question wasn't applicable or relevant they could
just click N/A and it would go away.

It seems like a simple, low pressure way to start establishing some
simple standards in the field.  Plus, authors with just a minimal
awareness of bioinformatics could go there to see what kind of
information they could put in their paper.  (I've already gotten
positive feedback from people using my `Top 10 reasons I hate your
bioinformatics software
<http://ivory.idyll.org/blog/jan-12/top-ten-things-i-hate-about-bioinfo-software.html>`__
blog post to figure out what they need to change.)

For example,

----

1. The software is directly available for download.

2. The software license lets readers download and run it.

3. The software source code is available to readers.

4. I downloaded and ran the software.

5. The data for replication is available for download.

6. The data format is either standard, or straightforward, or documented.

7. I downloaded the data.

8. I successfully ran the code on the data.

9. I successfully ran the code on the data and got the results in the paper.

----

You could imagine copy/paste output like this:

   Bioinformatics review criterion: The software is available, +1; the
   software license allows readers to run it, +1; the software is
   available, + 1; I didn't download it.  The data is available, +1;
   the data format is straightforward, +1; I didn't download the data.

   Score: 5/5.  See http://short/url/to/brc for more information.

This has the nice additional features of letting reviewers self-judge
their review effort, without being *too* judgemental about it; and
providing a viral mechanism for spreading the word.

The idea can be extended to a badging system and a self-advertising
system, too, if it gains any traction.

Comments?  Thoughts? Why is this a bad idea?  

And what questions, other than these, should be added?

--titus

p.s. I could easily imagine something like this for GWAS or other fields,
too.  Simple, straightforward, and a guide for reviewers who may not be
experts in every facet of the paper.


----

**Legacy Comments**


Posted by Casey Bergman on 2012-05-06 at 04:12. 

::

   Sign me up. I'll try to use this the next chance I get.      You might
   want to add soething like the following between the current 1 &amp; 2:
   "Is the software sufficiently documented to allow use by a third
   party"


Posted by Brad Chapman on 2012-05-06 at 07:23. 

::

   This is brilliant. Practically, a web form on Heroku could offer up
   the criteria and yes/no or 5 star style rankings for each. This
   produces a copy/paste bit for reviews. Longer term if we stored the
   rankings along with software names and links, this could generate
   Amazon-style easy reviews for software with an average reproducibility
   score.    We could hack this together at the pre-BOSC Codefest (http
   ://open-bio.org/wiki/Codefest_2012). I'll also try to carve out some
   time at BOSC for you to present the idea, and then we can collect
   feedback at a birds of a feather session.


Posted by Simon Goring on 2012-05-06 at 19:45. 

::

   This is great!  Publishers could include it just after the
   acknowledgements or above the introduction making it visible and self-
   reinforcing.  For the time being maybe I'll just start including it in
   my own reviews &amp; publications.


Posted by David Martin on 2012-05-07 at 06:39. 

::

   This is an excellent idea. Would it be possible to persuade a journal
   to take this on board as an editorial? Then it is a referencable
   criteron.  &lt;finds email addresses of symapthetic journal editors
   and points them in this direction&gt;


Posted by tyler on 2012-05-08 at 16:15. 

::

   +1 to @Casey's comment.     Its all good and fun to have a
   reproducible paper and I agree its necessary. But if your code is
   unreadable then you should be docked points.     Points for sure for
   publishing and having runnable code, but to me, to get a 9 I'd have to
   be able to successfully read and/or modify your code in a meaningful
   (non-trivial) way without wanting to strangle the author.    Coding
   standards can help with some of this. If they publish code, it should
   be formatted consistently. If its in python, for example, it should
   adhere to a community-authored style guide for python, etc.


Posted by tyler on 2012-05-08 at 16:17. 

::

   Also, I'd be willing to do just code review (i'm not a biologist, but
   I do work at a reputable software engineering company).    I'd also be
   happy to setup tools for code review, etc, and to offload the task of
   code review from scientific reviewers.


Posted by Titus Brown on 2012-05-11 at 15:59. 

::

   I think the least objectionable way to proceed would be to make sure
   that the minimum checklist is not requiring anything beyond what is
   absolutely necessary for replication &amp; review (and hence is
   required by most journals).    Anything beyond that is overreach IMO
   and would cause irritation amongst the reviewed...    --titus


Posted by Bruce on 2012-05-30 at 11:53. 

::

   You are missing the most critical aspect:    Before anything else,
   what is the license?     By downloading the code, you probably have
   accepted that license that you actually may not like. Really, all the
   software, data and meta-information should be in a select few
   recognized licenses (BSD, GPL v2). Related, but not as important, is
   that all the distributed 'package' has to be correctly licensed -
   files lacking license or even having different licenses.     Item 4
   should be:  I downloaded, COMPILED and ran the software WITHOUT
   INSTALLING IT.    Code may be missing a file or more, or even needs
   certain dependencies. Also, may be non-standard like being from some
   IDE (e.g., MS Visual Studio) or specific compiler version. Finally,
   you should not allow software that needs to be installed to run as
   that may mess with your computer (overwrite files etc.).

