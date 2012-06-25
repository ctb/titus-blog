Yahoo is bouncing my mail server's e-mail.
##########################################

:author: C\. Titus Brown
:tags: python
:date: 2008-03-27
:slug: yahoo-bouncing-my-mail
:category: python

On top of dreamhost dropping off the 'net just when I posted a bunch of
screencasts... our socal-piggies meeting nearly got whacked because
this month's organizer uses Yahoo, and most of the messages going through
my mail server (which hosts the mailing list) were filed as "spam".

Now Yahoo is actively bouncing my e-mail.

... You can see for yourself that 69.55.232.123 isn't a known spam relay,
isn't open, etc.  It's just Yahoo looking at the volume of mail being
sent and going "hey! wait a sec!" and listing me as a spam host.

Grr.

--titus


----

**Legacy Comments**


Posted by Ewout ter Haar on 2008-03-27 at 06:06. 

::

   This happened to us, and I don't know what to do about it. I also
   suspect that it was the mailing rate that triggered it. It was the
   default setting of postfix, but I guess Yahoo didn't like it. Nobody
   answers the mail or phone and I can't get it resolved.


Posted by Robert on 2008-03-28 at 14:26. 

::

   Yahoo uses domain keys for verification and spf. Make sure you are
   using them or you email provider is.


Posted by Steve on 2008-03-28 at 15:10. 

::

   I think the solution, extreme as it sounds, is some global law (no
   such thing, can't happen, I know) that finally brings a small charges
   for email, a penny or two for each email.    It would largely wipe out
   spam, and thus:    - Relieve the frustration that you described, since
   there would less (or none) incidences of mis-identifying spammers    -
   Less time spent configuring spam filters and checking your junk mail
   box to see if your provider (gmail, yahoo, etc) inaccurately junked
   it.   The only cons would be: putting some employeed programmers out
   of business who work on anti-spam software.    And of course having to
   pay for the email, but if you don't regularly send mail, it could be
   less than 5 bucks a year

