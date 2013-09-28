A few thoughts on code review of scientific code
################################################

:author: C\. Titus Brown
:tags: code review
:date: 2013-09-28
:slug: on-code-review-of-scientific-code
:category: science

Erica Check Hayden at Nature News wrote `this article
<http://www.nature.com/news/mozilla-plan-seeks-to-debug-scientific-code-1.13812>`__
about a `Mozilla Science Lab <https://wiki.mozilla.org/ScienceLab>`__
effort to bring code review to scientific code.  `Code review
<http://en.wikipedia.org/wiki/Code_review>`__ is an important part of
many open source, startup, and corporate software development cultures,
and the goal of the Mozilla effort is to See What Happens when you
throw seasoned software developers at scientific code.

(My personal bet is that it will not be immediately very effective,
because the seasoned software developers will be facing code with few
tests, implementing research data analysis and simulation methods that
they don't understand.  But I'm eager to be proven wrong!  Note that
my lab is just dipping its toes into `github flow
<http://scottchacon.com/2011/08/31/github-flow.html>`__ as a way to
engage with code review, which is exciting.)

After the article was published, there was a long-ish and somewhat
confused Twitter conversation around Roger Peng's skeptical quote that
"We need to get more code out there, not improve how it looks."
Several of "us" were surprised because Dr. Peng (one of @simplystats)
is a notable reproducible science spokesperson.  After a bit of back
and forth, he wrote `a long blog post explaining his position
<http://simplystatistics.org/2013/09/26/how-could-code-review-discourage-code-disclosure-reviewers-with-motivation/>`__.

It's worth reading even though I think he's wrong :).  Read on.

A few points
------------
 
1. Code review is not (only) about cosmetic changes.

   The wikipedia page on `Code review
   <http://en.wikipedia.org/wiki/Code_review>`__ and `Alex Gaynor's
   recent post on effective code review <http://alexgaynor.net/2013/sep/26/effective-code-review/>`__ make this point loudly and clearly.  "Improving how
   it looks" is not a reasonable way to characterize the point of code review.

2. Code is an important part of the methods for any paper that deals
   with real biological data.

   Jason Chin (@infoecho) spake thusly on Twitter `(ref) <https://twitter.com/infoecho/status/383220552741052418>`__:

   	 it is more important to explain what the code intends to do
   	 well than focusing at the code for science.

   And yet I've been rejecting (or at least sending back for
   revisions) papers that discuss real-world results without providing
   a fair amount of detail as to what was actually run.  This means
   both source code for the primary analysis (if novel to the paper)
   and specific versions and command line options.

   Why?

   Because, in my experience, as soon as "theory" touches "real data"
   there is a gulf of unknown size between the theory and the data.
   Code is what bridges that gap, and specifies how edge cases, weird
   features of the data, and unknown unknowns are handled or ignored.

   (Remember, in theory, theory and practice are the same. In practice,	
   they	are different. `(ref) <http://www.goodreads.com/quotes/66864-in-theory-theory-and-practice-are-the-same-in-practice>`__)

   The more general argument for code release is made very thoroughly
   in `The case for open computer programs
   <http://www.nature.com/nature/journal/v482/n7386/full/nature10836.html>`__.

   Also note that *I, personally, do not require open source
   licensing*.  It's entirely OK, scientifically speaking, for the
   authors to post their code under a "no reuse" license. Sure, I'm an
   open source/open science nutso, and I think the funding bodies
   should require it, but that level of policy is not IMO part of my
   remit as a reviewer.

3. Methods are a fair target for criticism.

   When I read blog posts like the @simplystat's post on how
   disclosing code might subject the code's authors to unfair
   criticism, there's a little game I like to play.  It's called
   's//'.  The game is, can I replace one concept systematically
   throughout the article and thus elucidate an underlying paradox?
   You can see it in action `here
   <http://ivory.idyll.org/blog/dangers-of-conversation-at-conferences.html>`__,
   where I tried to point out that some fella was against Twitter
   because he was basically uncomfortable with technological progress.

   So, when I read `How could code review discourage code disclosure? <http://simplystatistics.org/2013/09/26/how-could-code-review-discourage-code-disclosure-reviewers-with-motivation/>`__, I thought this: Hey, wait, they're arguing that reviewers might criticize their computational methods, and might even be jerks about it.  But doesn't that equally apply to lab protocols and statistical assumptions?  Yes, yes it does.

   Try it out!  For example, lightly edited:

        The problem here is that the reviewer deeply cares about us
        being wrong. This incident highlights one reason for
        concern. I feel we acted in pretty good faith here to try to
        be honest about our assumptions and open with our methods. We
        also responded quickly and thoroughly to the report of a
        mistake in our protocol. But the discussant used the fact that
        we had made a mistake at all to try to discredit our whole
        analysis with sarcasm. This sort of thing could absolutely
        discourage a person from discussing their experimental
        protocols.

   As far as I'm concerned this emperor has no clothes: negative,
   hypercritical, sarcastic, and unfair reviewers are a standard
   (though frustrating) aspect of scientific exchanges, and if you
   want to use this to argue against mandatory code release, you are
   also directly arguing against peer review of ...well, really
   anything substantive in the methods of the paper.  That seems wrong
   to me -- I'm not the biggest fan of the way we do peer review, but
   peer review writ large has its place.

   My Twitter comment on this was that the blog post was basically
   arguing that reviewers are occasionally obstreporous jerks (nolo
   contendere) and maybe they should be nicer.  Yep, but largely irrelevant
   to code release!

4. No scientific paper should rest on only one method.

   If you ever see a scientific paper that concludes with, "by the
   single method of frobnazzling the gliblub, we have now proven that
   bacteria can survive on arsenic alone", disbelieve it.  No
   scientist should ever rely on a single type of analysis or single
   source of data.

   An interesting corollary to this is that, by and large, I'm *not*
   very worried about scientific code being wrong, at least in the
   primary publication.  In order to publish it the authors will have
   to have tested it against known data sets and shown that the
   results are not too wonky, or otherwise shown that it's not
   blatantly and obviously crazy.  The real worry comes from reuse,
   remixing, and long-term maintenance of the code, where it may be
   modified by people other than its original authors, or applied to
   different data sets.  Without solidly engineered code, it's
   **reuse** that will lead you to places where There Be Dragons --
   e.g.  the `sign error problem
   <http://boscoh.com/protein/a-sign-a-flipped-structure-and-a-scientific-flameout-of-epic-proportions.html>`__.
   This is the difference between software engineering and research
   coding: most research code may not be intended for reuse, and will
   therefore not need to be solidly engineered.  Trouble comes when it
   **is** (nearly inevitably) reused (see `my own story on this
   <http://ivory.idyll.org/blog/automated-testing-and-research-software.html>`__).
 
   (This last paragraph, and the suspicion that most scientific code
   is probably not horribly wrong at first, is a somewhat surprising
   conclusion for me to have reached. Enjoy :)

   *Reproducibility* is a whole 'nother kettle of fish: for example,
   people in my lab have requested code from authors and received
   source code with syntax errors in it.  So, clearly not what the
   original authors used... what are we to make of that?
   
Looking forward
---------------

Right now there's an awful lot of apathy in the area of scientific
reproducibility, despite OpEds galore.  This for me is the bigger
issue.  Most scientists seem to be completely unaware of the need to
improve our practices: many faculty are openly dismissive of investing
the time, and even worse, many graduate students seem to be completely
oblivious.  This is incredibly bad for the future of (academic)
science.

I'm a big fan of code review because, first and foremost, it means the
code is accessible and executable!  If most scientific research code
were made available that would already be a big step forward.  But
it's not enough.

What would I like to see going forward?

1. More biology data papers that are explicitly and easily reproducible.
   This, IMSO, requires releasing the full analysis code and data.

2. A good review culture that ensures that, prior to publication, the
   code is at available, exhibits basic characteristics of good
   software hygiene, and doesn't `"smell"
   <http://en.wikipedia.org/wiki/Code_smell>`__ funny.

3. Stronger top-down incentives to reward reproducibility (and ding those
   who don't make the effort.)

--titus
