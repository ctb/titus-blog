SciPy 2007: Biology BoF
#######################

:author: C\. Titus Brown
:tags: python,biology,bioinformatics,scipy
:date: 2007-08-20
:slug: scipy-biobof
:category: python


So, I "organized" a Biology Birds of a Feather at SciPy 2007.  This mainly
consisted of posting about it and then trying to write stuff on a white
board while keeping abreast of the conversation.  About 15 people attended.

I didn't get everyone's name and in any case I don't want to pin
good/bad opinion labels on people ;).  So this will be anonymous reporting!

Notes from the meeting were posted by two different people, and they
are available from the `biology-in-Python archives
<http://lists.idyll.org/pipermail/biology-in-python/2007-August/000059.html>`__.

First things first: People who are interested in discussion their work
in Python and biology should `subscribe to the biology-in-Python
mailing list <http://lists.idyll.org/listinfo/biology-in-python>`__.
(After a number of negative comments from people about the first two
discussions on the list, I will endeavor to be a bit of a moderator, so
don't take past discussion as indicative of future ;)

Second, the biggest decision to come out of the BoF was to make an
effort to build up a community presence with a bit of a Web site as
well as things like tutorials, code links, discussion, etc.  Brandon
King has very kindly agreed to provide a basic Web site, and we'll
probably start off by hosting everything at scipy.org.  More on that
when it happens.

Third, and I feel like this is a big enough issue that it's worth
saying loudly and clearly, only one person in the room was positive
about BioPython.  Everyone else either had a bad opinion of it
("ugly", "non-Pythonic") or had been warned off by people with bad
opinions of it -- and surprisingly it was dominated by the former and
not the latter.  To me this indicates that these feelings about
BioPython are widely shared.  I don't know that it's worth going into
detail on why -- and we didn't cover it in depth at the BoF -- but
it needs to be mentioned.

The general consensus was that we needed to get the BioPython guys involved
in the biology-in-python mailing list, though, whether or not we wanted to
use "their" code!

Fourth, there was general agreement that Python could solve a lot of
problems for biology (big surprise there!) and that it could do so by
providing next-generation solutions rather than simply providing a
slightly nicer BioPerl-style interface.  What this precisely means
will have to be left to the imagination, but one experienced BioPerl
user said that the type of stuff being done with pygr represented a
real break with what he'd seen from bioinformatics previously.

At the same time, we all still need to parse, we still need to talk to
big databases, and we still need to break down large problems.  This
suggests that there's room for at least common interfaces, if not
necessarily One True Package.  I hope to push on this area myself.

One person made a push for One True Package, but I argued that we had
no Linus/Guido/Larry in the community.  Perhaps we could go with a
ring system like PostgreSQL, which seems to have no BDFL but instead a
small group of sensible people who contribute?  This might be an
option for pushing "BioPython 3k" ;).

We will be setting up facilities to pimp other people's code, as well
as places to discuss it, refine it, and help people build and test it.
Even more interestingly, there was common agreement that doing something
like hosting published results (+ code/source data) was a great idea.
This is a second area where I hope to really push.

Not sure what else there is to say. Overall it was a good, albeit
occasionally heated, discussion, and it was really good to meet
everyone.  Hopefully we can follow up with a PyCon BoF/Sprint where we
can get more the people together in one room!

--titus
