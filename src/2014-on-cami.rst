The Critical Assessment of Metagenome Interpretation and why I'm not a fan
##########################################################################

:author: C\. Titus Brown
:tags: metagenomics,assembly
:date: 2014-09-31
:slug: 2014-on-cami
:category: science

If you're into metagenomics, you may have heard of CAMI, the `Critical
Assessment of Metagenome Interpretation
<http://cami-challenge.org/>`__.  I've spoken to several people about
it in varying amounts of detail, and it seems like the CAMI group is
working to generate some new shotgun metagenome data sets and will
then encourage tool developers to bang on them.  (You can also read a
short `Methagora blog
<http://blogs.nature.com/methagora/2014/06/the-critical-assessment-of-metagenome-interpretation-cami-competition.html>`__
on CAMI.)

I've been asked by about a dozen people now what I think of it, so I'm
blogging about it now rather than answering people individually :).

tl; dr? I'm not a fan.

First, what's this subscription nonsense? (`We'll keep you in the loop
if you register here <http://cami-challenge.org/>`__.) There are a
plethora of ways to keep people in the loop *without* asking them to
subscribe to anything (blogs, Twitter, Web sites, e-mail lists...).
Is there a reason to keep the details of the contest secret or hidden
behind a subscriber wall?  (Answer: no.)

Second, I am told that the contest will be run once, with software
that is blind to the content of the metagenome.  I understand the idea
of blind software evaluation, but this is not a long-term sustainable
approach; we need to generate a nice set of orthogonal data sets and
then LART people who fine-tune their software against one or another.

Third, it looks like the CAMI folk will make the same mistake as the
Assemblathon 2 folk, and not require that the analyses be completely
replicable.  So in the end there will be a massive expenditure of
effort that results in a paper, which will then be a nice static
record of how things were back in 2014.  Given the pace of tool and
technology change, this will have a very short shelf-life (although no
doubt tool developers will cite it for years to come, to prove that
IDBA was once worse than their own assembler is now).  Why not re-run
it every 6 months with the latest versions of softwares X, Y, and Z?
We have plenty of ways to automate analyses, and there is simply no
excuse for not doing so at this point.  (ht to Aaron Darling for
alerting me to `nucleotid.es <http://nucleotid.es/>`__.)

Fourth, there are several mock metagenome data sets that are already
underanalyzed.  For example, we're currently working with the `Shakya
et al. (2013)
<http://scholar.google.com/citations?view_op=view_citation&hl=en&user=YJoYY7oAAAAJ&sortby=pubdate&citation_for_view=YJoYY7oAAAAJ:yD5IFk8b50cC>`__
data set, but I don't think anyone else is (and it's pretty clear most
people don't realize what a stinging indictment of 16s this paper is -
or, at least, don't care.  Discussion for another time.).

So why are we not poking at existing data first?  I don't know, but I
suspect it speaks to an underlying bias against re-analyzing published
data sets, which we *really* need to get over in this field.

As I said during the Q&A for my `BOSC 2014 keynote
<http://ivory.idyll.org/blog/2014-bosc-keynote.html>`__, I'm not a big
fan of how we do benchmarks in bioinformatics; I think this is a fine
exemplar.

I probably won't participate in the CAMI benchmark, not just for the
above reasons but because I simply don't have the people to do so at
the moment.  ...plus, as with Assemblathon 2, they're going to need
reviewers, right? ;)

Note that Aaron Darling raised many similar points at ISME, and they
were apparently very well received.  Maybe CAMI will adapt their
approach in response, which would be great!

--titus

p.s. Thanks to Alice McHardy and Aaron Darling for their detailed discussions
of this with me!
