A review of "An Integrated Pipeline for de Novo Assembly of Microbial Genomes"
##############################################################################

:author: C\. Titus Brown
:tags: science,peer review
:date: 2013-04-22
:slug: 2013-a5-paper-review
:category: science

I was a reviewer of the PLoS One paper, `An Integrated Pipeline for de Novo Assembly of Microbial Genomes <http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0042304>`__, and just recently came across the review again.  I didn't post it at the time, but heck, why not now? ;)

Note that for our `recent microbial genomes assembly workshop <http://ged.msu.edu/angus/2013-04-assembly-workshop/index.html>`__ we wrote up `instructions on using A5 <http://ged.msu.edu/angus/2013-04-assembly-workshop/assembly-with-a5.html>`__ on Amazon Web Services.

----

The authors describe a new assembly pipeline, A5, that integrates a
variety of common steps into a single straightforward software
package.  The description of the pipeline is quite good and the steps
included seem well thought out and justified.  Overall it is a
well-written paper that discusses what appears to be a useful
pipeline.

It is especially nice to see an assembly pipeline that is completely
integrated (error trimming, correction, etc.) and has a simple and
sensible input file format.  The separate contigging and scaffolding
stages are also welcome.

The Nextera compatibility is an excellent technical point and it's
great that this is included in the software (although I have no idea
how widely used this protocol is).

A general reservation is that (to paraphrase an excellent point made
in the paper) "A common approach employed by the hapless
bioinformatician involves downloading many different assembly packages
and evaluating the results until a perceived optimum has been
achieved."  I feel like the last thing we need is a new assembly
pipeline, since we really don't have a good sense for how well the
existing ones work... 

(discussion of specific technical remedies omitted.)

---

--titus
