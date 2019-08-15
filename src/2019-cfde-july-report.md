Title: An initial report on the Common Fund Data Ecosystem
Date: 2019-08-15
Category: science
Tags: cfde,fair,sustainability
Slug: 2019-cfde-july-report
Authors: C. Titus Brown
Summary: Helping DCCs get FAIRer

For the past 6 months or so, I've been working with a team of people on a project called the Common Fund Data Ecosystem. This is a targeted effort within the [NIH Common Fund](https://commonfund.nih.gov) (CF) to improve the Findability, Accessibility, Interoperability, and Reusability - a.k.a. ["FAIRness"](https://www.nature.com/articles/sdata201618) - of the data sets hosted by their Data Coordinating Centers.

(You can see [Dr. Vivien Bonazzi's presentation](https://dpcpsi.nih.gov/sites/default/files/CoC_May_2019_2.00PM_Data_Ecosystem_508.pdf) if you're interested in more details on the background motivation of this project.)

I'm thrilled to announce that our first report is [now available!](https://figshare.com/articles/2019-July_CFDE_AssessmentReport_pdf/9588374) This is the product of a tremendous data gathering effort (by many people), four interviews, and an ensuing distillation and writing effort with Owen White and Amanda Charbonneau. To quote,

> This assessment was generated from a combination of systematic review of online materials, in-person site visits to the Genotype Tissue Expression (GTEx) DCC and Kids First, and online interviews with Library of Integrated Network-Based Cellular Signatures (LINCS) and Human Microbiome Project (HMP) DCCs. Comprehensive reports of the site visits and online interviews are available in the appendices. We summarize the results within the body of the report.

The executive summary is just under four pages, and the full report is about 30 - the bulk of the report document (another 100 pages or so) consists of appendices to the main report.


I wanted to highlight a few things about the report in particular.

## 1. Putting your data in the cloud ...is just the start.

This may be obvious to those of us in the weeds, but supporting long-term availability of data through the use of cloud hosting is only one of many steps. Indexing of (meta)data, auth and access, and a host of other issues are all important to spur actual data reuse.

## 2. Just, like, talking with people is, y'know, really useful!

We did a lot of interviewing and found out some surprising things! In partial reaction to [our experience with the Data Commons](http://ivory.idyll.org/blog/2019-nih-data-commons-update.html), we are taking a much lower key and more ethnographic approach to understanding the opportunities and challenges that *actually* exist on the ground. A lot of the good stuff in the report emerged from these interviews.

## 3. Interoperability is contingent on the data sets (and processing pipelines) you're talking about.

The I in FAIR stands for "Interoperability", and (at least in the context of the CFDE) this is probably the trickiest to measure and evaluate. Why?

Suppose, not-so-hypothetically, that you want to take some data from the GTEx human tissue RNAseq collection, and compare the expression of genes in that data with some data from the Kids First datasets.

At some basic level, you might think "RNAseq is RNAseq, surely you just grab both data sets and go for it", right?

Not so fast!

First, you need to make sure that the raw data is comparable - not all RNAseq can be compared, at least not without removing technical biases. (And I'm honestly not sure what the state of the art is around comparing different protocols, e.g. strand-specific RNAseq to generic RNAseq.)

Second, the processing pipeline used to analyze the
RNAseq data needs to be the same. Practically speaking
this means that you may need to reanalyze all of the raw data.

Third, you need to deal with batch effects. I'm again not actually sure how you do this on data from a variety of different studies.

Fourth, and more fundamental, you need to connect your sample metadata across the various studies so that you are comparing apples to apples. (Spoiler alert: this turns out to be really hard, and seems to be the main conceptual barrier to actual widespread reuse of data across multiple studies.)

There are some techniques and perspectives being developed by various Common Fund DCCs that may help with this, and I hope to talk about them in a future blog post. But it's just hard.

## 4. Computational training is second on everybody's list.

This is something that I first saw when a group of us were talking with a bunch of NSF Science and Technology Centers (STCs): when asked what their challenges were, everyone said "in addition to our primary mission, computational training is really critical." (This broad realization by the STCs led to two funded NSF supplements that are part of Data Carpentry's back story!)

We saw the same thing here - a surprising result of our interviews was the extent to which the Common Fund Data Coordinating Centers felt that computational training could help foster data use and reuse. I say "surprising" not in the sense that it surprised me that training could be important - I've been banging that drum for well over a decade! - but that it was so high on everybody's list. We only had to mention it - "so, what role do you see for training?" - to have people at the DCCs jump on it enthusiastically!

There are many challenges with building training programs with the CF DCCs, but it seems likely that training will be a focus of the CFDE moving forward.

## What's next?

This is only an interim report, and we've only interviewed four DCCs - we have another five to go. Expect to hear more!

--titus

Brown, C. T., Charbonneau, A., & White, O.. (2019, August 13). 2019-July_CFDE_AssessmentReport.pdf (Version 1). figshare. [doi: 10.6084/m9.figshare.9588374.v1](https://doi.org/10.6084/m9.figshare.9588374.v1)
