10 Simple Rules for Biology to Survive and Thrive in a Data Intensive Future
############################################################################

:author: C\. Titus Brown
:tags: future
:date: 2016-03-28
:slug: 2016-data-intensive-future
:category: science

For a recent talk at Sars in Bergen, Norway, I tried to be cute and
come up with a 12-step program for biology to "survive and thrive" in
a data-intensive future.  The cute idea didn't really work that well
`(see the talk slides)
<http://www.slideshare.net/c.titus.brown/2016-bergensars>`__ but I
ended up liking the pithy nature of some of the steps.  So, I
refactored it into a blog post.  Comments solicited!

Note - there are more than 10 rules, and none of them are simple.
Sorry for the misleading title.

----

Biology is facing an increasingly data-rich future, with genomics
merely being the tip of one of several spears.  How should we be
thinking and planning to take advantage of this inevitable future?

Here are my thoughts:

**Methods matter.**

All of the methods used in gathering, cleaning, and analyzing data
matter - wet and dry.  I think our wet methods (in particular,
sequencing) outperform our dry methods, and we need to invest deeply
in all aspects of data analysis.

**Repeatability is important for scaling.**

What works for analyzing one data set (hand entering commands) needs
to be updated for three (scripting commands and doing pattern
analysis) and again for 100 or 1000 (moving from a procedural to a
declarative framework in which we specify *what* should be done to the
data, not *how* to do it).

**Aim for streaming and online analyses.**

In a world of infinite data, we'll never be able to look at all the
data in its entirety before reaching conclusions or making
decisions. We need to develop approaches that let us ask questions of
data as it comes in, and update the answers as more and better data
arrives.

**Computational training for practicing biologists is critical.**

Biologists need training in how to think about data, what's possible
to extract from data, and how to do it - and the complexity and
diversity of biological systems and questions means we have to train
people who already know and care about the systems, rather than trying
to build a new scientific workforce from scratch.

**We have to move beyond PDFs.**

PDFs are as good as anything at communicating interpretations. But in
a data intensive world, we need to communicate data, methods, and
interpretation together - and then integrate data and interpretations
from multiple labs, and enable computational query.  PDFs (and
scientific papers more generally) are a poor way to do this. We need a
new vehicle.

**Biology has to be built in.**

You can always find significance in a large enough data set, but that
doesn't mean it's really there. Structure your data collection and
interpretation around a specific biological question or process, so
that you don't spend all your time wandering the maze of data in the
hopes of finding something worth publishing.

**We must attack the unknowns.**

The unknowns (genes, proteins, pathways) will dominate large, complex
data sets for the foreseeable future. We will need to spend
significantly more effort on developing new ways to uncover the
function and meaning of unknown genes and genomic elements.

**Invest in data integration.**

Data can often be more easily interpreted (and almost always better
controlled) when cross-referenced with other data types. However, each
type of data has different resolution, accuracy, and bias, and fully
understanding these will be a lot of work.

**Layer your information.**

Some information - like transcribed elements and exon boundaries - can
be measured directly and reported with reasonable confidence. Other
information - full-length isoforms, predicted ncRNAs and regulatory
elements - may be less certain. We should develop more advanced data
visualization and dissection methods that allow us to select,
visualize and interpret types of information together with its
reliability and strength of evidence.

**Update resources incrementally, rather than recomputing from scratch.**

As new data comes in, the way in which we build reference resources
(e.g. genomes, gene sets) should move towards incremental update and
frequent release, instead of big, infrequent updates as we currently
do.

**Invest in data sharing and data analysis infrastructure.**

If we want to accelerate scientific progress, we need better tools to
share data, analyze data, and share the results of analyses. (Think
hosted methods and databases.)

**What rules am I missing?**

Some additional thoughts --

Invest in models - the best way to interpret lots of data is to work
towards a causal model.

Build better tools for computationally exploring hypotheses.

Invest in unsupervised analysis.

Think multivariate stats.

Invest in social media and online community - someone else probably has
something relevant to say about your methods, data or question, and it's
probably in your best interest to find them more quickly than not.

--titus
