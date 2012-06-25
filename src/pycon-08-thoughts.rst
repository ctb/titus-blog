PyCon '08: The Brain Dump
#########################

:author: C\. Titus Brown
:tags: python,pycon,testing
:date: 2008-03-17
:slug: pycon-08-thoughts
:category: python


Just left PyCon yesterday; now I'm up in Michigan looking at some more
houses, arranging lab stuff, talking with people, and getting ready to
prosyletize the `Google Summer of Code
<http://code.google.com/soc/>`__ to a bunch of Michigan State CSE
students as well as a few professors.

Some freeflow thoughts.  Feel free to comment my ideas into oblivion :)

PyCon was a blast, even though I didn't attend many talks.  I feel
that for many -- if not most -- of the talks, I can more easily digest
the material by simply going and reading about the project.  The
worthwhile talks are the ones that present new ideas or info and are
presented well; sadly, the vast majority of geeks do not give good talk.
For this and other reasons, I simply hung out for lunch and dinner and
met with old friends from previous PyCons.

I wholeheartedly support the adoption of an advanced-technical-only
track.  As it was this year the talks I was interested in (mostly very
technical) were embedded in the middle of a bunch of other talks that
were *not* technical.  I wasn't up to picking them out of the mix.

Speaking of "good talks", I think the whole review system is effed up.
What's with the anonymous authorship of proposals?  In 2007 my
proposal for a twill/etc. talk nearly got rejected because of "lack of
detail"; I thin this was partly because the reviewers couldn't take
into account that I wrote all of the damned tools I was talking about.
Anyway, it ended up being the third or fourth most popular talk of the
conference, and the highest ranked non-plenary talk.  Why not actively
solicit or help those people that have a history of giving interesting
or entertaining talks (as measured by audience response)?  I don't
think this is unjustified elitism: half the point of a conference is
to have interesting talks, right?  (The other half is the social
aspect, and then there are various "thirds" running about too.)  Maybe
I'm just bitching, but I think that if a good & highly technical
speaker submits a proposal that sounds boring to you as a reviewer,
your estimate of the proposal is more likely to be wrong than right.
(For example, when was the last time Brett Cannon gave a boring
talk??)

Yes, I'd be happy to help review, but I want to know who the author
is.  Then my reviews could look like this: "This topic is really
interesting, but your one paragraph summary doesn't reassure me that
you actually know what you're talking about.  Please justify your
ability to give this talk."  Or: "This could be an interesting talk,
but your presentation last year was a on a similar topic and was
really boring (see poll HERE).  I vote to accept based on the hope
that you will improve."  Or: "Awesome presenter, boring topic.  He
will make it work."

During dinner with Leapfrog people, a talk scheduling proposal
emerged: rather than trying to group talks in some logical coherent
way, why not try to minimize scheduling conflicts and auditorium
changes by asking people what talks they want to go to?  It's actually
a fun constraint solving/ expectation maximization problem...

Our testing tutorial went OK, although I think we've got to find a new
tutorial format if Grig and I are going to stay interested :). Our
audience members had widely varying skillsets and backgrounds, too,
which meant that some of them were bored through most of the tutorial,
while others were confronted with a huge volume of new information.

I'm thinking about how to improve for next year; we may try to do a
whole day of tutorials, and bring computers and Ethernet cables, and
help attendees solve their actual problems.

The conference support for tutorials was kind of minimal: normally we
don't need anything more than a projector and a mike, but (for
whatever reason) the conference organizers alternated between treating
us *really* impersonally (sending mass mailings that ignored previous
information we'd sent them) or *really* curtly ("No.  That's your
problem.")  I understand getting overwhelmed -- I've run several
conferences the size of PyCon '06 myself -- but if you let it change
the nature of your interaction with people, you're doing no one any
favors, least of all the conference or yourself.

Next year I may also ask for the tutorials to cover up to my own
expenses (registration, hotel room and flights) from student fees,
rather than having them simply give me $500 & free reg.  I feel like
I'm paying out for the privilege of giving each tutorial, and that's a
bit frustrating.  Probably they'll say "no", which will then leave
me/us with the option of cancelling the tutorial or just sticking with
it... we could also move the tutorial to a "sprint day" and encourage
people to stick around for real "free consulting with grig and titus".
I think we'd have more fun that way, and I'm damn sure we'd be more
useful!

The few lightning talks I saw were great fun.  Apparently I hit the
few technical ones :); `Bruce Eckel and others have complained
<http://groups.google.com/group/comp.lang.python/browse_thread/thread/2b6cb0e7245347be#>`__.
I didn't see any of that and I think the organizers, by and large, did
a great job.

I got a whole boatload of T-shirts without even stopping by the booths.

I finally met Leslie Hawthorn (Google Open Source Programs Goddess, or
some such) in person, which was a huge mistake to make.  She's like a
freakin' woman-shaped ball of energy (albeit low key even I know that
sounds like a contradiction) and she pushes pushes pushes people to do
Good Stuff for open source.  I appear to be susceptible.  More on that
later.

Leslie buys a mean glass or three of Lagavulin.  (Yum.)  And it was great
to meet her.  But I suspect that every time I meet her, I will get talked
into doing more stuff.  Sigh.

I'd like to thank O'Reilly (represented by Julie Steele) for buying me
dinner on Friday, and Leapfrog (represented by the entire testing team
there :) for buying me dinner on Saturday.

My OLPC interactions were interesting:

On Sunday, I gave a talk on automated testing and the OLPC GUI, Sugar.
I'll post slides and a screencast later, but a brief summary goes like
this: Sugar development is a bit of a disaster, with very little in
the way of any software engineering principles being applied.  In
particular, there's my particular bugaboo: they have no automated
tests, at all.  My talk discussed the situation and talked a bit about
using technology to remedy the situation; ultimately, though, the
choice the OLPC people have to make is whether or not their software
is going to suck.  (This version of my argument is intentionally
provocative, but I strongly believe that this is indeed the choice
they face.  See `"jwz CADT"
<http://www.google.com/search?q=CADT%20jwz>`__ and also my future
posts on this topic.)  In particular, their testing plans consist of
this: "really hope that other people step up and test our shit."  In
stark contrast to some of their other detractors, I'm trying to become
one of those people that *does* test their shit, but it also seems to
me that without a sea change in the focus of the software management
layer at OLPC, I will be wasting my time.

Anyway, so that's a mildly obnoxious talk to give and I did my best to
leaven it with humor and some rilly rilly cool testing tech.  What was
interesting to me, though, was the private advice from a number of
people -- there appears to be a large undercurrent of dissatisfaction
with the OLPC project in the Python community.  In particular, one
group of people basically said "burn the f$$!ckers to the ground".  (I
largely ignored this advice and tried to focus on the positive.)
These are not normally mean-spirited people, so from this, if nothing
else, I conclude that the OLPC has mismanaged its interactions with
the Python community.  I'm not sure exactly where things have gone
awry, but I hope it's not too late to get back some community
luuuuuurve: for all their software failings, the OLPC is an awesome
awesome project that has changed, and hopefully will continue to
change, this world we live in.  Advice and thoughts on this issue
welcome; I will post (or re-post) those that I think are especially
worthy of attention.

One interesting idea: one person suggested that after having done so
many impossible things already, the OLPC folk think that software is
going to be one more example where they have to break the mold.  Well,
guys, if you think you can break out of the Software Death Spiral without
building in any automated testing, I think you're batshit crazy...

I do feel good about using whatever "testing" community capital I may
have in putting forth a critique of the OLPC.  I'm still nervous about
having done it, frankly, because (as I said in my talk) it's like
kicking the family dog.  In this case neither the dog nor the rest of
the family bit, but perhaps I've just missed the negative comments?

I did finally see Ivan Krstic talk about the OLPC effort.  Due partly
to a laptop failure (ironic!), his presentation was largely photos
from his recent Peruvian and ???ian deployment of OLPC, which I'd
already seen through his feed.  Fantastic stuff, but a bit
disappointing to see a blog summary as a talk :(.  He's an engaging
speaker.

Ivan did not come to my talk.  I heard someone say, sotto voce, that
it was partly because he was afraid that I was going to say what I did
say.  This is only a rumor, though, and regardless I would encourage
him to engage me in a constructive conversation at some point...

I met Zed Shaw, too.  He's a hoot (I think that's the technical term
:).  Clearly very smart and equally opinionated.  He encouraged me in
some of my technical geekdom for the OLPC talk, and then of course
failed to come see the talk.  Ehh, I'll send him my screencast when I
finish it. There's no avoiding me, Zed!

Oh, I almost forgot -- I'm now a member of the Python Software
Foundation (unless they retract it for criticizing both PyCon and OLPC
in a single post)!  Hurrah!  I guess this means I'll have to run
PSF/GHOP again, yeargh.

Hanging out with everyone was awesome, and I will probably pay the fee
for next year's conference just for that.  I will make an extra effort
to attend the sprints next year, though, because they must be an
absolute blast.

I'm sure I'm forgetting stuff, but this is all my brain can stand for 
now.  More anon, esp about the OLPC and testing stuff.

--titus


----

**Legacy Comments**


Posted by pam zerbinos on 2008-03-17 at 18:12. 

::

   Hey Titus,  It was nice to meet you finally, after lurking on your
   blog for a while now. I had a blast at the testing nerds dinner on
   Saturday (but note that our 'entire testing team' wasn't actually
   there; three of them were missing. I'm sure they're feeling left
   out.).     Also, I've been having tutorial thoughts. I'll comment or
   e-mail or something when they're a little more cohesive, but if you
   and Grig are going to be doing something different, I do think it'd be
   cool to give my wacky plan a shot.     -p


Posted by Brett on 2008-03-17 at 23:11. 

::

   The biggest drawback from the conference becoming so large is that
   there were several people, like you, who I didn't run into at the
   conference! I wanted to say hi but it just never happened. Hopefully
   next year.    And thanks for the compliment about my talks. The only
   reason you were able to say that this year is that I made the
   Vancouver Python user's group suffer through a version of the talk
   that had no flowcharts. =)    And as for the anonymity in the review
   process, I agree with you. I always try to figure out who a presenter
   would be and give extra weight to people who I know will be
   entertaining. Perhaps we will be able to change it for 2009.    And
   yes, the sprints are a blast. Someone is here this year is using your
   blog post on running coverage on Python (and may have found an obscure
   bug in the process).


Posted by Mike Pirnat on 2008-03-19 at 00:07. 

::

   I thought your talk on the OLPC and its testing situation was pretty
   reasonable, and nothing that the fine folks who work on the OLPC
   should take offense at.    The community can't just pretend everything
   in OLPC-land is coming up roses just because it's such an interesting
   and ambitious project.  When someone in your family is in need of
   help, you have to be honest with them, and that's what your talk did.
   Hopefully it will be received constructively.  The OLPC's successes
   are quite moving, and it'd be a shame for the effort to collapse from
   lack of good practices.


Posted by David Goodger on 2008-04-08 at 23:35. 

::

   I posted a response on the PyCon blog: <a
   href="http://pycon.blogspot.com/2008/04/response-to-titus-browns-
   pycon-08-brain.html">http://pycon.blogspot.com/2008/04/response-to-
   titus-browns-pycon-08-brain.html</a>

