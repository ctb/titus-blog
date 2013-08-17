Is version control an electronic lab notebook?
##############################################

:author: C\. Titus Brown
:tags: version control
:date: 2013-08-17
:slug: is-version-control-an-electronic-lab-notebook
:category: science

In my post on `proselytizing version control
<../proselytizing-version-control.html>`__, an underlying and implicit
assumption was that version control was *not* fulfilling the function
of a lab notebook.  But I didn't make that explicit.  And then
someone asked in the comments.  So now I'm making it explicit.

tl; dr? Version control's a really good idea, and should be used by
everyone; but you can do science without using it, and I don't think
it's the computational equivalent of a lab notebook.

-----

It's a good question: is version control an electronic lab notebook?
Because if so, then it should be easy to convince practicing
biologists that they should use version control for their computational
work.

I'm not convinced it's that easy to make that argument.

Having spent some reasonable part of my life in a lab, I have
basic experience with a lab notebook.  In my graduate lab, I used my
notebook to write out what protocol I used to do a particular
experiment; what animals I used, at what stages of development; and I
pasted in the printouts from various machines detailing my results
(e.g. DNA concentrations).  It was an indispensable way to track my
experimental conditions and results.

Now that I'm once again only doing computational work, I don't really
use a lab notebook at all.  I don't think I need to.  Why not?

Lab notebooks seem to serve two purposes: first, they document
*provenance*, the origin of ideas, data, and results; and second, they
document *protocol*, the methods used to achieve a particular result.
Provenance is primarily an intellectual issue -- where did your ideas
come from? how did you get to where you got? -- while protocol is
primarily about reproducibility: how did you reach the particular
results?

In experimental science, it's often very hard to re-run experiments.
The lab notebook tracks the experiments and results and makes sure
that *when* an experiment needs to be reproduced, it can be.  One of
the most publicized scientific misconduct cases in my memory, `The
Baltimore Affair
<http://www-vortex.mcs.st-and.ac.uk/~alvarov/aacte/etica/baltimore_1998.html>`__,
was largely about sloppy record keeping.  More generally, this is why
good lab notebook keeping is considered essential to academic wet lab
practice.

For computational research, protocol tracking ensures reproducibility,
which is `rather important
<http://ivory.idyll.org/blog/research-software-reuse.html>`__ for all
sorts of reasons.  This is where scripting and version control have
been critical to my lab (well, along with these being the only sane
way to do software development).  While version control is helpful,
Sue Huse `convinced me <../proselytizing-version-control.html>`__ that
it's not absolutely necessary.  A the end of the day, I don't care
*how* you got to your final analysis; I care that your final pipeline
is reproducible.  You don't need version control for that.

But provenance? I see relatively little requirement for legal
provenance tracking in my computational work: for IP concerns, first
publication seems to matter a lot more than who had an idea, and I'm
not trying to patent anything.  Were I, I'm still not sure it would
matter; it's hard for me to imagine someone poring over my lab
notebook (or version control system) to document the very first time
we used a probabilistic de Bruijn graph, for example.

(I'm not a lawyer, and I'd welcome corrections or other perspectives.)

So I don't see a strong requirement for version control in
computational science, and, in fact, I know several people that I
would consider to be quite good computational scientists who don't use
it at all.  I hesitate to disbar these people doing good, reproducible
computational work from the scientific establishment simply because
they're not using version control.

More, I worry that the analogy between version control and lab
notebooks is a facile analogy that obscures a deeper divide between
experimental and computational work.  Experimental work is often slow,
expensive, "hands" dependent, and context dependent, and hence hard to
reproduce; most computational work requires a lot of development up
front, but should be neither "hands"-y or context dependent, and
should be relatively easy to reproduce.  These differences should
drive different methods of thinking about reproducibility.

----

And yes, you should still use version control.  It's simply good
computational practice.  But I don't think it should be justified as
the direct equivalent of lab notebooks; rather, it's an example of
good computational science hygiene, just like keeping a lab notebook
is *also* an example of good experimental science hygiene.

--titus

p.s. An interesting question: is the challenge of strict
reproducibility in experimental work one of the reasons why
*computational* reproducibility has not been demanded in biology?
If the reviewers have an experimental background, maybe they expect
computational reproducibility to be tougher than it really is, so
they let researchers get away with it?
