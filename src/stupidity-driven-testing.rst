"Stupidity Driven Testing" and PyCon '07
########################################

:author: C\. Titus Brown
:tags: python,pycon07
:date: 2007-02-28
:slug: stupidity-driven-testing
:category: python


Of all the
`fever-induced hallucinatory things I said at PyCon '07 <http://wamber.net/static/PyCon-2007/export-with-imagemap/PyCon2007.html>`__, I'm
proudest of this: "I don't do test-driven development; I do
stupidity-driven testing.  When I do something stupid, I write a test
to make sure I don't do it again."

So true.

For readers that don't get it, my development practice is this:

 1. write code to solve some problem
 2. watch code break in some obvious way
 3. write a test that tests that specific breakage
 4. lather, rinse, repeat.

I don't mind making mistakes, even stupid ones: I just don't want to repeat
them.  Thus, this development technique.

General comments on PyCon:
==========================

I did something every day: tutorial, panel moderator, panel-ee, and
speaker.  Way too much work, stress, and time spent in preparation.

Meeting people was great.  I got to meet & hang out with the `ARINC
people
<http://us.pycon.org/zope/talks/2007/sun/track1/084/talkDetails2>`__,
Shannon ("jj") Behrens, James Taylor of `Galaxy
<http://us.pycon.org/zope/talks/2007/sun/track4/086/talkDetails2>`__,
`Terry Peppers <http://www.swordstyle.com/blog2/>`__, and a bunch of
other people that I knew only from e-mail.  I also saw a bunch of
faces from last year, of course, including Brian Dorsey (thanks for the
lift, Brian & Kirk!)

The talks were (from my limited vantage point) much better this year
than last year.  This is presumably a reflection of the increasing
size of the Python community.

The "nose vs py.test" debate is growing in size, if not reaching any
actual conclusion.  It's very clear to me, at least, that these are
*the* big new testing tools; I'm (obviously) pushing for nose, but I'd
really like to see a showdown of features so that I can convert this
from flame-boy advocacy into informed advocacy.

I regret not attending more Birds-of-a-Feather sessions.

The `keynotes <http://us.pycon.org/TX2007/Keynotes>`__ were fantastic,
in general.  I didn't *enjoy* the education one, per se, but a lot
of interesting stuff was said.

I hope the recordings are up soon.

PyCon: Day -1 (travel)
======================

`Travel sucks. <http://ivory.idyll.org/blog/feb-07/pycon-travel-is-cursed.html>`__

PyCon: Day 0 (tutorial)
=======================

The tutorial day was, as usual, fun!  Grig and I gave our `testing
tutorial <http://us.pycon.org/TX2007/TutorialsPM#PM6>`__ and even
though we *felt* less prepared than last year, I think our significantly
increased experience with actually using these tools (see the `ARINC
talk <http://us.pycon.org/TX2007/TutorialsPM#PM6>`__ in particular)
showed.

Reviews (both positive) by `Shannon -jj Behrens <http://jjinux.blogspot.com/2007/02/pycon-testing-tools-in-python.html>`__ and `Terry Peppers <http://www.swordstyle.com/blog2/?p=1400>`__.

Next year, we should have a book or two out on these topics, which will
be an entertaining addition.

PyCon: Day 1 (Web panel)
========================

I spent most of this day sweating about the `PyCon Web Panel
<http://ivory.idyll.org/blog/feb-07/pycon-web-panel-2.html>`__, which
in any event turned out fine.  Once I finally worked out the format
for the panel in my own head (2 minutes introductions by me, followed
by questions spread evenly among the participants) I was much more
relaxed about things.  (Perhaps the most fun I had with this aspect
was reciprocating Grig's prodding: he constantly told me that I was
over-preparing, and then when it was *his* turn for the Testing Tools
panel I got to prod *him* for over-preparing.  Back atcha... ;)

The panel was really meant to showcase personalities and get faces out
there; 45 minutes is way too short for any meaningful discussion.

Being in front of that many people made me really freakin' nervous.

One obvious (to me) conclusion from the panel was that TurboGears and
Pylons should merge.  This `may happen
<http://groups.google.com/group/pylons-discuss/browse_thread/thread/40899cb2db03bcf6>`__
eventually, but not right now ;).

Another obvious conclusion (and I actually said something to this
effect) was that documentation is a *huge* problem.  *Huge.* The
framework that documents *will dominate* IMO.  (Right now I'm guessing
that this will be Django, but only because Adrian consistently
acknowledged the need for documentation.)

It was interesting to discover that Twisted had AJAX-like behavior a
year or two before AJAX hit.  I think Zope and Twisted both need to
hire a PR expert to publicize their coolness; I get the impression
that the communities are relatively insular and this contributes to
a lack of buzz about their accomplishments.

My favorite comment, by Jonathan Ellis: "Django's ORM is feeble."

James Bennet has a `disturbingly complete <http://www.b-list.org/weblog/2007/02/23/pycon-2007-web-frameworks-panel>`__ transcript.

Other reviews/notes: `Jonathan Ellis <http://spyced.blogspot.com/2007/02/pycon-web-frameworks-panel-notes.html>`__, `James Tauber <http://jtauber.com/blog/2007/02/23/pycon_web_panel>`__ (international man of mystery!), `Nathan Yergler <http://yergler.net/blog/2007/02/24/testing-tools-panel-pycon/>`__ (I agree, Nathan!  But I asked for more time!), `Shannon ("jj") Behrens <http://jjinux.blogspot.com/2007/02/pycon-web-frameworks-panel.html>`__, and `Matt Harrison <http://panela.blog-city.com/web_framework_panel_notes_pycon.htm>`__.

Hopefully a video of this event will be posted.  I want to listen to
what I actually said. ;)

PyCon: Day 2 (Testing Tools panel)
==================================

I wasn't as worried about the Testing Tools panel, 'cause I didn't have
to say anything.  Of course, it turns out `I said too much <http://wamber.net/static/PyCon-2007/export-with-imagemap/PyCon2007.html>`__ as a result ;).

The panel was fun but kind of a blur.  A bit more time next year, perhaps?

Reviews/notes: `Grig Gheorghiu <http://agiletesting.blogspot.com/2007/02/testing-tools-panel-at-pycon.html>`__, and `Matt Harrison <http://panela.blog-city.com/testing_tools_panel_pycon.htm>`__.

I attended the buildbot BoF, which was really fun.  Brian Warner rocks.

PyCon: Day 3 (twill talk)
=========================

I spent most of the prior evening and morning working on my
`twill/scotch/figleaf talk
<http://us.pycon.org/zope/talks/2007/sun/track1/087/talkDetails2>`__.
During this time I learned just enough about CherryPy 3.x and Django
whatever-the-heck-the-latest-version-is-with-or-without-magic-removal-who-the-hell-knows
to actually write test fixtures for them.

I decided to go out on a limb and rather than describe twill/etc.  in
nauseating detail I worked up nine demos (testing CherryPy sites,
doing coverage analysis, writing twill extensions, testing Django
sites, and recording Web traffic) and I ran through the demos
interactively while providing a narrative.

I *really* enjoyed this talk format, although it may not be for everyone.

You can grab my talk source code `here
<http://www.idyll.org/pycon.zip>`__ although this link will eventually
(soon!)  be broken & moved to an archive containing more
documentation.

Review: `The Thiers <http://thethiers.com/?p=96>`__.

I announced the `testing-in-python (TIP) mailing list
<lists.idyll.org/admin/testing-in-python/>`__ in my talk.

Grig's `pybots talk
<http://us.pycon.org/zope/talks/2007/sun/track1/090/talkDetails2>`__
was well-received and (IMO) I think this project is going to
dramatically increase the solidity of the Python community's software.

I also got a chance to run some of my ideas for improving test processes on
the Python interpreter past Brett Cannon, and (to my shock) he was really
open to them.  More on that soon.

That evening, I got a chance to meet up with R. Steven Rainwater
("robogato") and his wife Susan; Steven has taken over `advogato
<http://www.advogato.org>`__.  They took me out to a nice sushi
place, which was really welcome after the heavier food I'd been
eating thus far.  More on that anon.

Post-PyCon: travelling to San Antonio
=====================================

After PyCon, Diane Trout and I shuffled ourselves over to UTSA to talk
with the nice people at the `Computational Biology Initiative
<http://cbi.utsa.edu/>`__.  The CBI is interested in making a
commitment to future development of `Cartwheel
<http://cartwheel.idyll.org/>`__ which is pretty cool.  More anon.

--titus
