A response to "The myths of bioinformatics software"
####################################################

:author: C\. Titus Brown
:tags: lior again,software,sustainability
:date: 2015-07-11
:slug: 2015-response-to-software-myths
:category: science

This is a response to (parts of) Dr. Lior Pachter's post, `"The myths
of bioinformatics software"
<https://liorpachter.wordpress.com/2015/07/10/the-myths-of-bioinformatics-software/>`__.  (You can also see `my post on bioinformatics software licensing <http://ivory.idyll.org/blog/2015-on-licensing-in-bioinformatics.html>`__ for at least some of the background arguments.)

I agree with a lot of what Lior says: most bioinformatics software is
not very good quality (#1), most bioinformatics software is not built
by a team (#2), licensing is at best a minor component of what makes
software widely used (#3), software should have an expiration date
(#5), most URLs are unstable (#6), software should not be "idiot
proof" (#7), and it matters that you use a *specific* programming
language (#8).

I strongly disagree with Lior's point #4, in almost every way. I try
make my software free for everyone, including companies, for both
philosophical reasons and for simplicity; I explained my reasoning in
`my blog post
<http://ivory.idyll.org/blog/2015-on-licensing-in-bioinformatics.html>`__.
(Anyone who doesn't think linking against GPL software is reasonably
complicated and nuanced should through the tweets and comments on that
post!)  From my few involvements with working on non-free software, I
would also add that selling software is a tough business, and not one
that automatically leads to any profits; there's a long tail, just as
with everything else, and I long ago decided that my time is worth
more to me than the expected income from selling software would be.
(I would be thrilled if a student wanted to try to make money off of
our work, but my academic work would remain open source.)

Regardless, Lior's opinion isn't obviously wrong, and I appreciate the
discussion.

----

What surprises me most about Lior's post, though, is that he's
describing the present situation rather accurately, but he's not angry
about it.  I'm angry, frustrated, and upset by it, and I really
want to see a better future -- I'm in science, and biology, partly
because I think it can have a real impact on society and health.
Software is a key part of that.

Biology and genomics are changing.  Large scale data analysis is
becoming more and more important to the biomedical sciences, and
software packages like kallisto and khmer are almost certainly going
to be used in the clinic at some point.  (I believe some of Broad's
variant calling software is already used in diagnosis and treatment
for cancer, for example, although I don't know the details.)  Our
software is certainly being used by people doing basic biomedical
research, although it may not be directly clinical yet - and I think
the quality of computation in basic research matters too.

And this means **bioinformatics should grow up a bit**.  If
bioinformatics is a core component of the future of biology (which I
think is obvious), then the quality of bioinformatics software
matters.

To quote Lior, "Who wants to read junk software, let alone try to edit
it or build on it?" Certainly not me - but then why are we producing
it?  Are we settling for this kind of software in biomedical research?
Are we just giving up on producing decent quality software altogether,
because, uh, it's hard?  How is this different from doing bad math, or
publishing bad biology - topics that Lior and others get really mad
about?

Lior also quotes a Computational Biology interview with James Taylor,
who `says
<http://www.nature.com/nbt/journal/v31/n10/full/nbt.2721.html>`__,

   A lot of traditional software engineering is about how to build
   software effectively with large teams, whereas the way most
   scientific software is developed is (and should be)
   different. Scientific software is often developed by one or a
   handful of people.

That was true in a decade ago, and it may have been a reasonable
reason to avoid using decent software engineering techniques then, but
the landscape has changed significantly in the last decade, with a
wide variety of rapid prototyping, test-driven development, and
lean/agile methodologies being put into practice in startups and large
companies.  So I think James is mistaken here.

I wager that the reason a lot of scientists do bad software
engineering is because they can get away with it, not because there
are no techniques they could profitably use.  Heck, if they wanted to
learn something about it, `Software Carpentry
<http://software-carpentry.org>`__ will come teach workshops for you
on this very topic, and I'd be happy to offer both Lior and James a
workshop to bring them up to speed.  (Note: I don't think either of
them needs my advice, which is actually kind of my point.)

(As for languages, Lior's point #8, there is a persistent expansion of
the Python and R toolchains around bioinformatics and a convergence on
them as the daily workhorses of bioinformatics data analysis.  So even
that's changing.)

Fundamentally the blithe acceptance of badly engineered software in
science baffles me.  I can understand (`and even endorse
<http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html>`__)
not requiring good software engineering for algorithmic proofs of
concept, but clearly `we want to have good, robust libraries for
serious work
<http://gael-varoquaux.info/programming/software-for-reproducible-science-lets-not-have-a-misunderstanding.html>`__.
To claim otherwise would seem to lead to the conclusion that much of
bioinformatics and genomics *should* seek to be incorrect and
irrelevant.

----

I *want* there to be a robust community of computational scientists
and software developers in biology.  I *want* people to be able to
build a new variant caller without having to reimplement a FASTQ
or SAM parser.  I think we *need* people to file bug reports,
catch weird off-by-one problems, and otherwise spot check all the
software they are using.  And I don't think it's impossible or even
terribly difficult to achieve this.

The open source community has been developing software with
distributed teams, with no single employer, and with uncertain funding
for decades.  It's not easy, but it's not impossible. And in the end I
do think that the open source community has a lot of the solutions the
computational science community needs, and in fact is simply `a much
better exemplar for how to work reproducibly and with high technical
quality <http://www.jarrodmillman.com/oss-chapter.html>`__.  Why we
continue to ignore this mystifies me, although I would guess it has to
do with `how credit is assigned in academic software development
<http://ivory.idyll.org/blog/2015-more-on-software.html>`__.

If we went back to the 80s and 90s we'd see that many of the same
arguments that Lior is making were applied to open source software in
contrast to commercial software.  We know how that ended - open source
software now runs most of the Internet infrastructure.  And open
source has had other benefits, too; to quote Bill Janeway, "open
source and the cloud have dramatically decreased the friction of
innovating", and the scientific community has certainly benefited from
the tremendous innovation in software and high tech.  I would love to
see that same innovation enabled in genomics and bioinformatics.  And
that's why we try to practice good software development in my lab;
that's why we release our software under the BSD license; and that's
why we encourage people to do whatever they want with our software.

Ultimately I think we should develop our software (and choose our
licenses), for the future we want to see, not the present that we're
stuck with.

--titus
