DIB jclub: Better reporting for better research: a checklist for reproducibility
################################################################################

:author: Lisa Cohen, Camille Scott, Tamer Mansour, Sherine Awad, C\. Titus Brown
:tags: jclub, reproducibility
:date: 2015-09-23
:slug: 2015-jclub-etc-on-reproducibility
:category: science

**Note:** at the `Lab for Data Intensive Biology
<http://ivory.idyll.org/lab/>`__, we're trying out a new journal club
format where we summarize our thoughts on the paper in a blog post.
For this blog post, `Lisa Cohen
<http:/monsterbashseq.wordpress.com>`__ wrote the majority of the text
and the rest of us added questions and comments; Lisa then further
summarized several conversations around the issue.

The initial paper: 

`Amye Kenall, Scott Edmunds, Laurie Goodman, Liz Bal, Louisa Flintoft,
Daniel R Shanahan, and Tim Shipley. Genome Biology. (2015) 16:141 DOI
10.1186/s13059-015-0710-5
<http://www.genomebiology.com/content/pdf/s13059-015-0710-5.pdf>`_

Press Release: `BioMed Central launches checklist for
reproducibility. <http://www.biomedcentral.com/presscenter/pressreleases/20150723a>`_

In this article, Kenall et al., who are affiliated with the publishing
company `BMC <http://www.biomedcentral.com/>`_, introduce Minimum
Standards of Reporting Checklists for authors and reviewers for a
trial set of 4 of their journals focused on computational research
(idea that computational research should be more reproducible than
other fields):

* `BMC Biology <http://www.biomedcentral.com/bmcbiol/authors/instructions/minimum_standards_reporting>`_  
* `BMC Neuroscience <http://www.biomedcentral.com/bmcneurosci/authors/instructions/minimum_standards_reporting>`_  
* `Genome Biology <http://www.genomebiology.com/authors/instructions/minimum_standards_reporting>`_  
* `GigaScience <http://www.gigasciencejournal.com/authors/instructions/minimum_standards_reporting>`_  

Checklists meet new `NIH Principles and Guidelines for Reporting
Preclinical Research
<http://www.nih.gov/about/reporting-preclinical-research.htm>`_ with
three areas applicable to reproducibility:

1. experimental design
2. statistics
3. availability of data and materials

DIB Lab Group Discussion
========================

*Somewhat Socratic dialogue on philosophy of science ensues:*

**What is reproducibility?**

**Replication** == technical replicates, same experiment, One
person/group has one set of data and another has the same data.

**Reproducibility** == biological replications, different experiment,
One person/group has one set of data and another has the same
data. Same or different results?

What can be eliminated in each situation to suggest error was on the
part of one vs another?

Reproducibility is stronger.

There is disagreement (== things could be correct, but not reproducible). Why?

* biological variability/uncontrolled variability in sampling
* systematic error (miscalibration)
* human error (at least one person screwed up) -- replication can address
* lack of detailed reporting -- on the computational side
* different statistical models
* programming bug in the system (R, python, whatever) -- replication

So, replication is critical *if* there are differences/inability to be
reproducible. It's reproducible if someone with sufficient expertise
can reproduce it.  (Titus credits this observation to Victoria Stodden.)

-----

Tamer: Proving or refuting a study has to be a community effort.

Titus: True reproducibility cannot pragmatically be the function of a single paper.   

Camille: The attempt to reproduce should matter.  

Titus: How long should it be after a robust in-lab result is published but remains without replication before we no longer believe it?  

Camille: The trustworthiness of results is not the main reason to pursue reproducibility in the first place! It's more a matter of reporting to enable efficiency and ability to build on existing results.  

Titus: Do we actually know what the true numbers of reproducibility are?   

----

*Stigma of irreproducibility:*

* Bug vs research mis-conduct: `Example of research misconduct incident <http://www.cbsnews.com/news/scientist-dong-pyou-han-sentenced-prison-for-aids-research-fraud>`_
* If I am a professor, if my student makes a mistake, how do I ensure that I discover it, determine if it is not innocent? (In this lab, Research results are automated and reproducibility is ensured before publication.)
* What to do if a mistake is discovered in my work after publishing? Retract.
* What to do with programs with local maxima changing with every run —not global ?? - this happens in practice, but Titus claims that apart from engineering issues like floating point, the only other possible source is random number seed.
* With public access from the early stages to the last minute, how to guarantee my work is protected?
* Avoid ambiguous abbreviations when documenting: my common mistake: e.g:  s1 ==? sample1/ species1 .while within the context it can be both! 

*Why is reproducibility important?* 

* Authors of papers and recipients of funding are increasingly being required to openly provide raw data and evidence of reproducibility. 
* If results are not reproducible, this doesn't necessarily mean the study was fraudulent or findings incorrect. `Reproducible research can still be wrong <http://www.pnas.org/content/112/6/1645.full>`_. 
* Science as a process is not easy to explain to the general, tax-paying public where funds are often coming from. Generally, scientists could do a better job of documenting and communicating to the public, neighboring scientific community members, and field/clinical practitioners. Establishing better policies to support the process of transparency and verification may benefit scientists through sustainable funding and the general public through translated research.

Titus: So, reproducibility is important because of funding? That seems cynical.

Tamer: Biology is highly variable. Can we just use similar approaches in reporting results?

Camille: "This is why we have error bars?"

Group consensus: We need a *reliable* body of evidence to move forward. There is value in this. (It's not just about funding. :)

*"How easy is it to reproduce or replicate the findings of a published paper?"* 

* In general, difficult. `This paper's <http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0080278>`_ finding 280 hours to reproduce his own work. Another example is `González-Beltrán et al 2015 <http://www.ncbi.nlm.nih.gov/pubmed/26154165>`_, who used a Galaxy virtual research environment to replicate the original `SOAPdenovo2 paper <http://www.ncbi.nlm.nih.gov/pubmed/20019144>`_ and found results to be different than those from the original paper. 

* `Ioannidis 2005 <http://sitemaker.umich.edu/emjournalclub/article_database/da.data/0000c0a8de10000007d55901000001300d2ce5437d22f361/PDF/ycontradicted_highly_cited_research.pdf>`_  found that 45/49 highly cited clinical studies claimed effective intervention, 16% were contradicted by subsequent studies, 16% had stronger effects than subsequent studies, 44% were replicated, 24% remained unchallenged. (learned about this from interesting `talk by Wheat 2014 <http://evomicsorg.wpengine.netdna-cdn.com/wp-content/uploads/2013/03/14-CK-EcoGen-lect1.pdf>`_, encouraging scientists to question results) 
* Microarray reproducibility paper: http://www.biomedcentral.com/1471-2105/8/412

* Aa few examples that are easy to reproduce. From our lab, among others. 
* See `Zhang et al. 2014 <http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0101271>`_, which is 100% reproducible. 
* Also, the Docker `bioenergy paper <http://www.gigasciencejournal.com/content/4/1/33>`__ that just came out from GigaScience. (Titus reviewed ;)
* Much of the ENCODE effort is done in Galaxy and published with a VM.

Additional points:

* The programmer would give you a different script if they knew it was going to be published. (Sad, but true.)

* Checklists seem vague, subject to interpretation. How to define 'rigorous statistical analysis', for example?

* Explicit guidelines are useful for authors to know what to expect in review.

* The checklist is perhaps surprisingly non-computational, even if it's targeted at computation. Code availability is not equal to reproducibility. This is a notable omission from the standards! 

* I worry about implementation. It's quite surprising that there is no
  mention of pipelines in the actual `checklist
  <http://www.genomebiology.com/authors/instructions/minimum_standards_reporting>`__. The
  only portions relevant to software are:

		> If computer code was used to generate results that are central to the paper’s conclusions, include a 
		> statement in the “Availability of data and materials” section to indicate how the code can be accessed.
		> Include version information and any restrictions on availability. For deposited data and published code, a 			> full reference with an accession number, doi or other unique identifier should be included in the reference 		> list.

and under "Resources":

		>  Tools (software, databases and services): report standard tool name, provider and version number, if 			> available.

The first of these is pretty vague. What makes a result "central"? For example, if we're talking about a genome assembly, are the generated contigs the results, or are the assembly statistics and annotation information the results? Even in the case where the authors choose to provide the code for preprocessing, this would allow them to submit an unorganized collection of one-off scripts that are still, essentially, non-reproducible. 

* I'd like to see the inclusion of some basic standards on workflow reporting. Something as simple as requiring a README with execution instructions could go a long way. 
* stochastic algorithms - what do we do about situations where there is a fundamentally statistical/stochastic component to the results?
* minimal code review: "has useful tests." "has documentation" "has version control." "some cases that work, some cases that don't."
* What can computational scientists, such as dib lab do to help other disciplines be more reproducible?
* What about other fields? While NIH is one of the largest (I think?) funding agency because of relevance to human medicine, it is just one funding agency. Are there examples of funding and reporting reproducibility and transparency requirements for agencies other than NIH or journals other than BMC or Nature? What about NSF? Found `this article re EPA <http://toxsci.oxfordjournals.org/content/early/2015/03/19/toxsci.kfv020.abstract>`_.
* Agree or disagree with article's statement? *'...computational biology (which theoretically should be more easily reproducible than “wet lab” work...'*
* Article didn't mention data management or public repositories such as NCBI, SRA and GEO. I'm wondering how checks and balances can be established for these? (anyone can submit, data quality not necessarily checked) Has there been any quantification for how this impacts research?

Other references:
=================================

* http://ivory.idyll.org/blog/blog-review-criteria-for-bioinfo.html.  
* http://ivory.idyll.org/blog/2014-myths-of-computational-reproducibility.html  
* http://ivory.idyll.org/blog/a-conversation-on-reproducibility.html  
* http://ivory.idyll.org/blog/vms-considered-harmful.html  
* http://ivory.idyll.org/blog/kelleher-on-code-review.html  
* `Palmer 2000 <http://www.zoology.ubc.ca/~purcell/palmer%202000.pdf>`_: Fig 1 showing bias from selective reporting, effect from sample size.
* See: `Central Limit Theorem <https://en.wikipedia.org/wiki/Central_limit_theorem>`_
* `A living document: reincarnating the research article <http://www.trialsjournal.com/content/16/1/151>`_  
* `Tools and techniques for computational reproducibility <http://biorxiv.org/content/early/2015/07/17/022707>`_ (reviewed `here <http://ivory.idyll.org/blog/2015-review-six-methods-reproducibility.html>`_)  
* `Ten Simple Rules for Reproducible Computational Research <http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003285>`_

Sherine's summary:

This paper gives a suggestion on the basic things to consider for reproducibility but not limited to these 10 rules/ with comments and questions:

1. For every result, keep track of how it is produced 
2. Avoid manual data manipulation Steps
3. Archive the exact versions of all external programs 
4. Version control all custom scripts
5. Records all intermediate results when possible in standardized formats
6. For analysis that include randomness, note random seeds
7. Always store raw data behind plots
8. Generate hierarchal analysis allowing layers of increased details to be inspected
9.  Connect textual statements to underlying results
10.  Provide public access to scripts, runs and results


Tools for reproducible science:
================================

* `Docker <https://www.docker.com/>`_, with `examples <http://arxiv.org/pdf/1410.0846v1.pdf>`_ and `training coming to UC Davis Nov. 9-10 <http://dib-training.readthedocs.org/en/pub/>`_!  
* `MyExperiment <http://www.myexperiment.org/home>`_
* `Bioconductor <https://www.bioconductor.org/>`_, `article <http://www.nature.com/nmeth/journal/v12/n2/full/nmeth.3252.html>`_
* `Arvados <https://arvados.org/>`_ 
* knitR: http://yihui.name/knitr/
* Jupyter: https://jupyter.org/

Discussion at NGS 2015 workshop. 
================================

Started with great demonstration of Twitter. Not all students were familiar with Twitter and were interested in hearing about the benefits and drawbacks to this media platform. Interesting point that next generation of leaders in science will use social media technology.  

Following, this led into the assigned journal club discussion for the evening about reproducibility and the reanalysis of ENCODE data: http://f1000research.com/articles/4-121/v1 

Some points that were discussed:

* Reading papers and evaluating them publicly can be positive for the scientific community but unpleasant for authors
* Resulting blog and twitter discussions are beneficial for students and people learning 
* Should people who reanalyze others' studies contact authors directly before publishing?
* Embarrassing for authors of studies being scrutinized
* On the other hand, if your study is published, this leaves it open to whole community for judgement.
* Why aren't all papers published as open preprints? Why even publish in peer-reviewed journals at all?
* Negative side of open preprints is that if someone negatively reviews, may prevent from publication
* Open reviews could also prevent authors from continued publication
* A new person in the field could be afraid to publish
* Related articles on retraction: http://iai.asm.org/content/79/10/3855.full
* `Charles' guide to online arguments <http://geekfeminism.wikia.com/wiki/Charles'_Rules_of_Argument>`_
* Don't expect people to change their minds in a debate.

The topic of reproducibility continued during the 3rd week of the NGS 2015 workshop, including 3 excellent tutorials:

* Marian L. Schmidt: http://rpubs.com/marschmi/105639
* Leigh Sheneman: http://angus.readthedocs.org/en/2015/week3/AWS-tips.html
* Titus: http://angus.readthedocs.org/en/2015/week3/CTB_docker.html
