A mildly crazy idea: crowdsourced -omic analysis with data privacy sunset?
##########################################################################

:author: C\. Titus Brown
:tags: science,genomics,bioinformatics
:date: 2013-03-07
:slug: crowdsourced-analysis-with-data-privacy-sunset
:category: science

Or, "can we crowdsource BGI?" ;)

With all of the crazy need surrounding genomic analysis -- most of
it on a shoestring budget -- I am thinking about a mildly crazy idea.

What if I offered to computationally analyze people's non-model
transcriptomic and metagenomic data for them, in exchange for (a)
non-exclusive access to the data, (b) a citation (but no
co-authorship), and (c) a "data privacy sunset" provision that, 1 year
after our analysis of their data, we could post both the data
and the analysis publicly?

I imagine it working something like this:

1. Dr. Smith receives some sequencing data and ships it to me on a hard
   drive.

2. We load it onto our server and run it through our standard pipeline --
   something we maintain publicly and openly on github, including
   pull-request contributions.

3. When the analysis is done, we provide Dr. Smith with a private,
   password-protected Web link.  This link includes some basic Webby
   analysis data as well as download links so that you can (e.g.)
   feed your data into MG-RAST or a transcriptomic analysis framework.

4. One year after #3, we open up both the data and the Web link under
   a Creative Commons/citation license.  (License suggestions
   welcome.)

This serves all sorts of needs:

First, we'd have a constantly improving public, open source, and
forkable analysis pipeline for both metagenomic and transcriptomic
data.  (You could rely on me to make it runnable on Amazon EC2, too,
for those of you that want to provide your own computers.  And it'd
be BSD licensed, 'cause that's how we roll.)  This would be publishable.

Second, I'd provide all the compute resources and data munging, so, to
participate, no one would need to have a nice Web-runnable user
interface or a big computer or even learn how to use FTP.  A key part
of this proposal is that I can make most of this compute pretty easy
by using `khmer <http://github.com/ged-lab/khmer/>`__ to prefilter the
data -- a big reputational boost for us, obviously, and something that
would really decrease the compute requirements.

Third, the open data and open results and public processing pipeline
would serve as an awesome benchmarking opportunity for people who want
to test new tools, new trimming approaches, etc.  We could start
building up a meta-analysis toolchain around it, too, for the purpose
of comparing the results of two slightly different pipelines.  This
would be publishable.

Fourth, we could work with public sites, e.g. `figshare
<http://figshare.com>`__, to make the results archivable with DOIs, so
that they could be included in publications.

Fifth, any company that wanted to add private services on top of ours
would be welcome to do so.  Sequencing cores and nonprofits and other
labs could participate however they wished; the only requirement from
my perspective would be that anyone using my compute resources would
have to buy into the public data.

Sixth, it would help biologists publish using their own data -- or at
least it wouldn't hurt much -- and it would help computational people
by making more data available, together with a lot of the nasty and
stupid preprocessing steps taken out.

Seventh, we could provide an IPython Notebook and RStudio (?)-like set
of interfaces to work with the data on an EC2 or VirtualBox VM, and
then run Webinars on how to play with your data.  (We'd probably have
to charge for that, just to cover personnel costs.)

I should say we're fairly close (60% of the way?) to this kind of
thing in my lab already, especially since I am stepping up the push to
have all of our research output be scripted and reproducible.  The
transcriptomics is in fact no longer a computational challenge; it's
the metagenomics that would be a real challenge.  But this would be a
real incentive to optimize that.

Anyway, just a random thought.  Feedback welcome.

--titus
