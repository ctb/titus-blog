w4s - strategizing for the future
#################################

:author: C\. Titus Brown
:tags: open science,webmaking,w4s
:date: 2012-11-13
:slug: w4s-future-strategies
:category: science

This is one of a bunch of posts on science and the Web.  `Start here
<../w4s-overview.html>`__ for an overview.

----

I've been reading Michael Nielsen's book `Reinventing Discovery
<http://www.amazon.com/Reinventing-Discovery-The-Networked-Science/dp/0691148902/ref=dp_return_2?ie=UTF8&n=283155&s=books>`__,
which is an awesome and inspirational book about (among other things)
accelerating scientific discovery using the Internet.  Highly recommended.

From my position *within* academia, it's clear that we're not making
anywhere near full use of the Internet.  What's less clear to me is
how to accelerate the process of integrating the Internet into
research.  Here are a bunch of longish-term strategies and ideas.
(The short-term ones are over in `tech wanted <../w4s-tech-wanted.html>`__.)

1. Focus on tech things that are *so useful* that scientists have no
   choice but to pick them up, because the learning curve is worth it.

   Nielsen comes up with a lot of ideas about how scientists could use
   networked collaboration technology, but he only lightly covers our
   motivation for *using* it.  Without strong, explicit incentives --
   which are unlikely to emerge in the short term -- I think it's unlikely
   that most scientists would invest the learning time necessary to
   become usefully proficient in collaboration tech.  Speaking only
   for myself, I can tell you that I am constantly challenged for "thinking
   time", and so I'm perennially scared of new technology that has a learning
   curve (...one reason I like the IPython notebook so much -- no learning
   curve!)  What can we do?

   Well, if we look at which part of collaboration technologies we
   actually use now, it's clear that some things are too useful *not*
   to adopt.  I'm thinking about things like e-mail, Skype, and online
   journals here -- active researchers have virtually no choice but to
   use these technologies.  Dropbox, too.

   So, if we want to sucker scientists into the long hall of improving
   their lives through somewhat more outre collaboration tech, we need
   to make darn sure it's extraordinarily useful and pretty easy to
   dip into.  (Put that way, it sounds obvious, right?)

   For example, reproducible research is a great and popular concept, but
   we haven't built an enabling tool that's both really easy to learn
   and just solves the problem.  How could we do that?

2. Better ways for scientists to share data and process.

   Most scientists use e-mail, physical media, or Dropbox to share
   data.  "Process", by which I largely mean the computational
   processes used in data analysis and modeling, is shared by personal
   contact and e-mail interaction.  This blocks tracking of provenance,
   limits communication of process improvements, and is otherwise
   really inefficient.

   If we could make it easy (or at least easier) to share and explore
   data with collaborators, and to explicitly communicate process to
   collaborators, I think a lot of scientists would jump on it.  This
   is another reason I like IPython Notebook so much, but it's only
   part of the solution -- we need more than a notebook, we need
   associated data and compute!

   There are some pretty interesting attempts to do this explicitly --
   check out `RunMyCode <http://www.runmycode.org/CompanionSite/>`__.  Are
   they working?  If not, why not?  I'd be interested in finding out.

3. Better ways for scientists to *collaborate on* and *teach* their process
   and practice.

   Researchers necessarily embrace lifelong learning.  In addition to
   collaborating on data and process, people need to *learn* new
   techniques and apply them to their own data.  This requires training
   materials. So far most training materials are a disappointing
   gemisch of text, static diagrams, and opaque videos.

   If we could mark up process (see point 2) and share that, and
   provide entry points into and annotations on video... well, that
   would be a good start.  What would be better would be ways for
   scientists to better communicate and manage large-scale interactions,
   including through online real-time collaborations.

4. Better ways for scientists to create and participate in *ad hoc*
   collaborative interactions.

   "Hey, bub, take a look at this data -- what do you think is going on?"
   But across continents.

   Again, IPython Notebook is going to make this possible, but we need
   a rich ecosystem of open collaboration tools so that we can easily tie
   this into video conferencing and phone calls.

5. Offer opportunities for hands-on expectation-free training, e.g.
   sabbatical opportunities in tech-enabled environments.

   Lots of scientists are interested in this stuff, but very few have the
   time to devote to learning new tech (see point 1).  Support 3- or
   6-month sabbaticals, or summers, in environments with enough tech-savvy
   at-risk youth and other practicing researchers to show off
   blogging, online forums, and the rest.  Sucking in young scientists
   with summer funding a la GSoC might also work -- if it was on their
   research rather than some side project.

6. Venues for in-person collaboration and discussion by scientists on tech
   stuff.

   We need venues where crazy people can get together and talk about the
   process that they'd like to be using for their research. There just
   aren't many (if any) -- I tend to have these conversations in the
   hallway at conferences with grad students and faculty, for example.

7. Tech and venues for "living publications", bridging the gap between
   blogs and publications and source code and data.

   Publications are currently very formal and also very dead.  We
   should fix that -- first, make it easy to cite blogs; and second,
   make it easy to link pubs to source code and data, online and
   interactive.  PLoS is very interested in this.

8. Data integration across and within data sets; enable remote interaction
   with and exploration of large data sets.

   The "living publications", above, could be one end of a spectrum that
   would include sites with opportunities for exploration, annotation,
   and publication of "views" of data.

9. "Reddit for scientists" a la Pickrell.

   Joe Pickrell has a great `blog post <http://www.genomesunzipped.org/2011/07/why-publish-science-in-peer-reviewed-journals.php>`__ (and a `follow-up <http://www.genomesunzipped.org/2012/08/the-first-steps-towards-a-modern-system-of-scientific-publication.php>`__) on this.

   Briefly, Joe proposes immedate publication, rapid social
   recommendation of interesting papers connected to existing
   networks, and strong automated recommendations of papers that take
   into account the opinion of existing field-specific social
   networks.  I think reddit, only mildly modified, would be able to
   serve this purpose quite nicely.

   To put it another way, once you decouple publication from perceived
   future impact like PLoS One has, you instantly realize that all that's
   left is winnowing out papers of interest to you.  How can we facilitate
   this?

10. Negative results and open data repositories specifically to combat
    selective publication, bad statistics, and fraud.

    `Retraction Watch <http://retractionwatch.wordpress.com>`__, but on
    steroids.  Encourage a culture of posting data *without* publication,
    and (in some cases) *require* that any registered study of, say,
    a proposed pharmaceutical, post its data.

    Yeah, this requires policy changes.  But why not be ambitious?

--titus
