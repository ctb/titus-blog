#################################
Code review for application notes
#################################

:author: Jerome Kelleher
:tags: bioinformatics, code review
:date: 2014-01-14
:slug: kelleher-on-code-review
:category: science

**Note:** this post is a guest post by Jerome Kelleher.  Please also
see his `letter to Bioinformatics
<http://figshare.com/articles/Code_review_in_application_notes/899728>`__
on this topic.

========
Overview
========

(1) Many journals provide a mechanism to publish computer 
    programs in the form of application notes or software
    articles. These notes 
    are subject to peer review, but there is no explicit 
    requirement that the quality of the application be 
    taken into account.
(2) Even if reviewers examine the source code, there is no 
    reason to expect that they can provide an informed 
    opinion on its quality. Reviewers are experts in the 
    application domain but not necessarily in the programming 
    language(s) in question.
(3) A system of lightweight code review would greatly improve 
    the quality of the applications available to the  
    community, and incentivize well-written code. Along with 
    the existing scientific review, source code for an application
    should be reviewed by an expert programmer who would provide 
    an opinion on the overall quality of the application, as well 
    as feedback to the developers on how it may be improved. The 
    code reviewer would not be expected to understand the application 
    in any deep sense, and would provide feedback only on the
    obvious signals of quality, such as structure, style, 
    consistency, installation instructions, portability,
    user interface design and so on.
(4) Since code reviewers do not need to understand the application 
    domain they can be drawn
    from the wider developer community. Ideally, contributors
    to free and open source projects should be recruited, since these
    are people with verifiable expertise and a history of contributing 
    their time to a common good. Reviews should not be too 
    time-consuming (a maximum of one hour, say), and there should 
    be public acknowledgement of a reviewer's contribution to a 
    journal.
(5) The benefits would be an immediate improvement in the quality
    of published applications. The majority of problems in scientific 
    applications not caused by fundamental errors in the 
    methods, but by superficial issues that arise through 
    inexperience. Introducing this limited form of code review 
    would also yield valuable insights for the larger goal 
    of making *all* scientific code subject to peer review.


============
The problem
============

A couple of years ago, I reviewed an application note for *Bioinformatics*. 
As part of the review process, I downloaded the Python source code and examined
it to get a feel for the quality of the application. It was so poorly written
that I immediately formed the judgment that this application could not 
be trusted, and should be immediately rejected.
The source code showed clear evidence of being written by 
an unsupervised novice programmer. For example, one function
took 25 parameters and was 1130 lines long. Within this function,
there were 107 conditional statements, indented by up to 9 levels.
The same 18 lines of code were repeated (complete with 
identical comments)  *thirty six* times, with only integer constants
changing between each repeated block. 
Basic mistakes such as these had been made throughout the 
code base.

The application note was rejected, as the other reviewers also had 
serious issues with the work. Neither of them, however, 
brought up the issue of the quality of the code, which in my opinion 
was sufficient grounds for rejection, regardless of whether 
the application *appeared* to work or not. The peer review system 
worked in this instance, but it had failed before. This particular 
application had been published by another journal (the authors
had been seeking a "version 2.0" publication at *Bioinformatics*),
and had been used and cited in  several papers.

Application notes perform an important role, as
they provide a forum for researchers to publicize useful code.
Most importantly, they provide a mechanism by which researchers can 
be given due credit for the work involved in developing these 
important tools. Without the reward mechanism of application note 
publications and citations, there is simply no incentive to develop tools that 
are useful to the wider community.

These tools, however, are often of lamentably low quality. Installation 
can be difficult, and documentation sparse and poor. User interfaces
(command line or graphical) rarely follow established 
conventions, making each tool a challenge to use. 
The quality of source code is often 
rather poor, making any reuse or modification very difficult. 

The problem is that there is no requirement that the reviewers
of an application note examine the source code. 
Most reviewers will download the application and ensure
that it installs and runs on example data. The main goal 
of a review is to assess the novelty and importance 
of the methods, not the quality of the software.
Because there is no assessment of quality
there is no incentive for quality.
I believe that this is a major flaw in the review
process for scientific software, and so 
I wrote a letter of the editors of *Bioinformatics*
in which I suggested the introduction of a system of code 
review for application notes. The editors declined to 
publish this 
`letter <http://figshare.com/articles/Code_review_in_application_notes/899728>`_.

=======================
Lightweight code review
=======================

My suggestion is to introduce a system of lightweight code review for 
application notes.  For many open source projects,
code review is an intrinsic part of the development process. A 
developer submits a patch implementing some new feature  
for review. Other developers then assess this 
patch, to ensure that it meets the required standards, and 
only after it has been reviewed will the code be committed.
There are other forms of code review, but these usually 
involve one developer trying to fully understand
the code another has written in order to improve code quality.

This type of code review would not be feasible in the context 
of application notes. It would be far too laborious, because it 
would require a reviewer to fully understand all aspects of 
an application they have never seen before.
Instead, I suggest a much more lightweight review process. Code 
should be assessed for the more obvious signals of 
quality: readability, consistency, documentation, structure
and packaging.
Code should follow the idioms of the language involved
and should consistently follow a well-known coding style. It 
should be well documented and appropriately commented. 
The structure of the code should be clear, and it should 
be straightforward to find where a particular piece of 
functionality is implemented. 

There is a problem, of course, in finding people to 
perform these reviews. It would seem that we need reviewers who are both 
experts in the application 
domain and in the programming language(s) in question,
and such people might be very difficult to find. 
The solution to this problem is to split the 
responsibility: experts in the application domain review 
the manuscript and application for novelty and utility
to the community, and expert programmers review the source code
in terms of its apparent quality.
We are then free to choose code reviewers from anywhere, even 
from outside of science. An expert programmer could perform 
a lightweight review in less than an hour
and so the demands on their time should not be be too great.

Careful guidelines would be required for reviewers to ensure 
that reviews remain helpful. For example, it should be made 
quite clear that disagreements on aesthetic grounds are
not appropriate. Once code is consistent, idiomatic and 
follows some well-known style, it does not matter which 
particular style it follows. 

Reviewers must be experts in the language that the application 
is written in, and must have a proven track record of 
delivering high-quality software. Convincing such people 
to donate their time to review scientific code is the 
most difficult part of this process, but there are 
encouraging signs that it may be possible.
In a recent `pilot study
<http://blogs.plos.org/biologue/2013/08/08/what-does-peer-review-mean-when-applied-to-computer-code/>`_,
Mozilla engineers reviewed snippets of 
source code from previously published *PLOS Computational Biology* papers.
This `study <http://arxiv.org/abs/1311.2412>`_ found that 
the engineers were happy to perform the reviews, but 
were frustrated by the shallowness of the reviews 
as a result of their lack of domain expertise. 
All of the reviewers indicated that they were willing 
to continue to participate in scientific code review
"provided they felt they could contribute something of value."

Such shallow (or lightweight) reviews are 
precisely what is required for application 
notes. By writing reviews, pointing out the weaknesses of 
applications and indicating how to fix them, reviewers can enter
into a dialogue with application authors. Their expertise would
be highly valued, and provide a great service to the academic 
community, helping to improve the quality of the software
used to progress science.

============
The benefits
============

It may seem that there is little point in such a lightweight 
code review process. If a reviewer is only going to spend 
an hour browsing the code and writing a report, 
then they will surely miss all  
sorts of bugs. This is true, and bugs will 
remain in applications regardless of how much review 
is done. The point is not to make the software published 
in application notes perfect, as this is impossible. The point is 
to try to ensure that published software is  
*reasonably good*, as this would be a major improvement. 


There would be many benefits. The first would be an 
increase in the quality of the applications published.
Through the influence of the expert reviewers, software
would be easier to install and use. Feedback through 
reviews may also result in improved performance, since 
reviewers may point out ways in which implementation 
could be improved. Ultimately, reviewers may choose to 
contribute code directly to a project, if they 
see that their help would make a difference and be
appreciated. This influx of experience and knowledge 
would be a huge boon for science.

Another benefit would be an increased realization that 
significant applications cannot be written by untrained
novice programmers. Applications submitted that are of very 
low quality (such as the example discussed above)
should be immediately rejected. A few manuscript 
rejections may be required before the message filters
through, but the message will surely be received 
eventually. Hopefully, this will help foster a culture 
in which students are trained to program effectively
as a matter of course.


