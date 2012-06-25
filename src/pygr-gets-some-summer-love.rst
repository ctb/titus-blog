pygr gets some summer love
##########################

:author: C\. Titus Brown
:tags: python,bioinformatics
:date: 2008-05-09
:slug: pygr-gets-some-summer-love
:category: science


(`pygr <http://bioinformatics.ucla.edu/pygr/>`__ is a neat
bioinformatics framework in Python.)

After some commenters on my last post seemed happy to hear that pygr
was the focus of some summer work, I realized I had only discussed the
pygr summer work in `a post to the biology-in-python list
<http://lists.idyll.org/pipermail/biology-in-python/2008-April/000306.html>`__.

Whoops.

So, here's the scoop: not only is pygr the focus of `Rachel McCreary's
Google Summer of Code project
<http://code.google.com/soc/2008/psf/appinfo.html?csaid=B6BADB61050FB8F0>`__,
but `Jenny Qian will be using pygr to build an ENSEMBL interface
<http://code.google.com/soc/2008/psf/appinfo.html?csaid=16FD71A42C4B7B>`__,
also as part of the Google Summer of Code.

That's not all!

In addition to Rachel and Jenny (under the sterling mentorship of
Chris Lee, Robert Kirkpatrick, Namshin Kim, and myself) I have two MSU
students working with me over the summer, Alex Nolley and Marie
Buckner.  They'll both be working with pygr-related things, although
like Jenny their efforts may end up being more on ways to use pygr
than on pygr's code itself.

I also have a grad student or two that may drop in on pygr, if only to
use it for something research-y.

So all in all, pygr will get a lot of love this summer.  Hopefully we can
polish the code and documentation and tutorials to the point where the
learning curve is as minimal as it can get, and this fabulous package will
become readily available to many others...

Why am I personally putting so much effort into pygr?  Well, I've been
using it more and more over the last few months, and (`somewhat like
scipy
<http://www.vetta.org/2008/05/scipy-the-embarrassing-way-to-code/>`__)
it's transformed my work by turning annoyingly difficult data
organization problems into trivial Python transformations.  I can
literally throw together a custom genome browser in a matter of hours
-- I've implemented two or three already, for different projects --
and it has enabled several new research program.  pygr seems to be one
of those rare packages (kind of like Python itself) that is not only
functional and effective but presents a unified and coherent
intellectual interface.  pygr is the only good middleware layer I've
seen for sequence intertwingling in bioinformatics.  It's not that
mature yet, but it has serious promise, and I'm hoping to get in on
the ground floor, so to speak :).

cheers,

--titus


----

**Legacy Comments**


Posted by Anthony on 2008-05-09 at 17:09. 

::

   Ok, I'll bite.  I'm a grad student doing bioinformatics, and have been
   using Java for most of my programming... mainly because we have an API
   for it for Ensembl.  (Between perl and Java, I'll take Java anyday.)
   However, recently, I've been customizing and working around the API,
   which I generally consider a bad thing.    In any case, so long as
   there's an API for python, it might be worth switching - I've got
   several 10's of kloc, so migrating now wouldn't be a bad thing.
   What's the best way to get involved and/or started with pygr and the
   future Ensembl API?


Posted by Titus Brown on 2008-05-10 at 13:38. 

::

   Hi Anthony, not sure what to say.  Right now I think pygr has a bit of
   a learning curve, so if you're more focused on getting specific work
   done I'd stick with what you have.  OTOH, if pygr fits your needs and
   you want to give it a serious try, then you have a good opportunity to
   learn about it during the summer when there will be LOTS of help
   available.    The ENSEMBL API is planned but not yet underway.
   Anyway, the place to look is the pygr-dev list, <a
   href="http://groups.google.com/group/pygr-
   dev?hl=en">http://groups.google.com/group/pygr-dev?hl=en</a>    Hope
   to see you there!

