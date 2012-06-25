Galileo, Open Science, and History
##################################

:author: C\. Titus Brown
:tags: science,science20
:date: 2010-08-26
:slug: science-and-open-science
:category: science


I'm a big believer in open science -- see this `great polemic
<http://www.mendeley.com/blog/open-access/researcher-which-side-of-history/>`__
over at Mendeley for a good read -- but it's always interesting to
think about how such things as "data release" can be perverted by
clever scientists.  I'm currently in France working on some ascidians
with `Billie Swalla <http://faculty.washington.edu/bjswalla/>`__ --
more on that later -- and we've been talking about what data we plan
to release, and how.  During these talks (leisurely conducted over
cafe au lait and chausson pomme, of course!) Billie brought up an
interesting historical parallel.

The story, as I understand it, is this: when Galileo Galilei first
looked through `a good quality telescope
<http://en.wikipedia.org/wiki/Galileo_Galilei#Astronomy>`__ and
discovered Jupiter's moons, nobody believed him.  Since he was the
only person able to make such good telescopes, he actually made and
distributed them to other scientists -- not just as a profitable
sideline, but so that the other scientists could confirm his
observations!

One could see this a first step towards "open science": in order to
reproduce Galileo's observations, astronomers had to have a telescope
that only Galileo could make.  So Galileo had to make telescopes and
send them out, thus allowing others to both reproduce his observations
and build upon them.

The story takes on a different aura, however, when you realize that
Galileo could have just given out the actual manufacturing
instructions for the telescopes, but didn't.  Two possible reasons are
money (he made money selling the telescopes to others) and scientific
miserliness: he didn't want others to get credit for building on his
results.  As long as he withheld the details necessary to reproduce
his instruments, he ensured that no one could build on his results,
and that he would have preeminence in astronomy.  (The parables between
this and source code are uncanny, no?)

It was quite a balancing act.
To quote from Dr. Biagioli's "Replication or Monopoly" (`pdf here
<http://www.fas.harvard.edu/~hsdept/bios/biagioli_replic_monopoly.pdf>`__),

   "His primary worry was not that some people might reject his claims,
   but rather that those able to replicate them could too easily
   proceed to make further discoveries on their own and deprive him of
   future credit (Galilei 1989, 17). Consequently, he tried to slow
   down potential replicators to prevent them from becoming
   competitors. He did so by not providing other practitioners access
   to high-power telescopes and by withholding detailed information
   about how to build them.

   But as important as it was for Galileo to keep his fellow
   astronomers in the dark, such negative tactics alone would not have
   allowed him to gain credit from his discoveries and move from his
   post at the university of Padua to a position at the Medici court
   in Florence as mathematician and philosopher of the grand duke -
   goals clearly on his mind in 1610.He needed proactive tactics as
   well. First, he did his best to make sure the grand duke saw the
   satellites of Jupiter (which Galileo had named "Medicean Stars") by
   sending detailed instructions to Florence on how to conduct these
   observations, and then by going to court himself at Easter time
   (Galilei 1890- 1909, X:281, 304). Second, through the prompt
   publication of the Sidereus nuncius in March of 1610 he tried to
   establish priority and international visibility - resources he
   needed to impress his prospective patron, not just the republic of
   letters.

   The Nuncius was carefully crafted to maximize the credit
   Galileo could expect from readers while minimizing the information
   given out to potential competitors."

Here you can see calculation as fine as any modern professor, trying to
decide if they should release *all* their data, or only *some* of it;
*all* of their source code, or only a crippled version.

Billie also observes that one potential irony in this story is that
Galileo, by so strongly taking sole credit for his discoveries, made
himself a clear target for the Catholic Church...

An even more pernicious approach, seeking priority while avoiding
embarrassment by publishing hashes (well, anagrams ;) of formulae or
observations, was common in the 17th century.  In `The Newton
Handbook, by Derek Gjertsen
<http://books.google.com/books?id=cqIOAAAAQAAJ&pg=PA16&lpg=PA16&dq=newton+published+anagram&source=bl&ots=Se6LS3COaK&sig=1DB05ZJrF_hJwiH6jNrGCw-V8gQ&hl=en&ei=SOV0TP6UN8KblgfC7_HYBw&sa=X&oi=book_result&ct=result&resnum=3&ved=0CB0Q6AEwAg#v=onepage&q=newton%20published%20anagram&f=false>`__,
Gjertsen writes:

   "It was not uncommon for seventeenth-century scientists to record
   their more valued results in the form of anagrams.  Thus, Galileo
   published his discovery in 1610 of the phases of Venus in a
   thirty-five letter anagram, Huygens announced his 1656 observation
   that Saturn was surrounded by a ring in a sixty-three letter
   anagram, while, in England, Robert Hooke and Christopher Wren
   resorted to similar stratagems.  The advantages of the ploy are
   obious.  Priority was established, yet nothing was given away to
   potential rivals.  If, by chance, the work failed to stand up to
   further analysis it could be quietly forgotten without the
   embarrassment public failures tended to incur."

One can only wonder how many one-shot awesome Science and Nature
papers, using software that was and remains unavailable, are entirely
unreplicable or otherwise uninteresting -- for example, I like to pick
on one of `Eran Segal's publications
<http://www.nature.com/nature/journal/v451/n7178/full/nature06496.html>`__,
because it's so neat and yet very very difficult to replicate without
source code.  (A colleague is trying.)

Compare this to the recent discussion of the (leaked) P != NP proof,
now shown to be erroneous - see, e.g., `Greg Baker's blog post, P !=
NP <http://gregbaker.ca/blog/2010/08/07/p-n-np/>`__.  Now *this* is
the way science is supposed to work!  Quick, thoughtful commentary by
experts, highlighting potential problems with your work -- and
allowing or enabling others to build off of it.

It's clear to see that by withholding the manufacturing instructions,
Galileo may well have held back astronomy as a whole.  And by
publishing their equations in anagram form, it's likely that Newton
and the others did damage to science as a whole.

Today, intellectual reputations like that are in some ways less
important (at least in my bottom-feeding scientific world).
Publications and citations are more important, since they're
measurable by Promotion & Tenure committees.  I (and probably many
other scientists) are continually worrying about the line between
publishing good stuff that enables citations, and giving away all of
our future research directions.  It takes a real act of faith to throw
yourself off the cliff and offer up your latest & greatest source code
and data to the world, in the hopes that somehow the resulting
"usefulness" will provide lift to your career.  We'll see how that
goes: road kill?  Or tenure?

Back to Galileo -- I think the Galileo example is why, as wonderful as
the `Panton Principles <http://pantonprinciples.org/>`__ are for data,
for truly open science it's critical to provide not only the raw data,
but the source code used to do the analysis.  And not only the source
code, but *useful* source code: *documented* and *tested* source code
[1].  To do anything else would be the equivalent of selling
telescopes while withholding the manufacturing instructions that would
let others build on your own ideas.

Interesting stuff to think about!  Now, back to science...

--titus

[1] Yeah, I realize that most scientific source code probably isn't
documented *or* tested.  Draw your own conclusions there ;).


----

**Legacy Comments**


Posted by Shanti on 2010-08-26 at 18:17. 

::

   Three cheers for open science. The telescope was invented by
   Lippersley (and independently by Jacob Metius) in the Netherlands in
   1608. Lippersley published and widely distributed the manufacturing
   instructions. Galileo improved it with better optical tolerancing in
   1609 and looked up at the planets. Galileo published his observations,
   Kepler heard about them, and made an even better telescope.
   Development of optics in Europe moved exceedingly fast after Galileo's
   discovery. The early telescopes were made by guess and check -- you
   move the lenses around until you get an image. It was only 8 years
   later that the Europeans were designing telescopes using ray tracing,
   which got smart folks like Newton involved. Until Newton came along,
   there wasn't much language for communicating about optical design.
   Snell didn't even figure out refraction until 1621.


Posted by Erich Schwarz on 2010-08-27 at 19:00. 

::

   First of all, genuinely good ideas just don't get stolen.  Because
   they look <i>weird</i> and people can barely stand them at first.  For
   some months after he invented it, Kary Mullis could barely get anybody
   to pay attention to PCR.    My own experiences with innovation are
   microscopic, but I can nevertheless attest that it has been a pain in
   the neck, in the last few months, to come up with something creative
   and have to pitch it even to a coauthor or to labmates in group
   meeting.  I sure don't worry about being scooped after getting the
   comments I've gotten; I worry that my stuff'll come out in print and
   then be quietly forgotten for years, unless I myself follow it up!
   "Not Invented Here" is very real, and scientists are generally as
   susceptible to it as Detroit.    Second, people who are trying to
   scoop you in your own area of expertise are likely to have a miserable
   time.  You're doing what you do because you actually care about it and
   enjoy it.  They're doing it because they're scared epigones.  That's
   not a formula for winnitude.    Third, I've seen a lot of people stay
   closed-source or outright not-available-source in genomics.  I have
   never seen it end well.  Generally, the field treats them as damage
   and works around them.  Because it has to!  Irreproducible science may
   get a Nature article if the authors are from the Coolkids Institute of
   Technocruft, but it's still irreproducible, which leaves everybody
   else in the field having to redo the whole thing to reproduce it.  The
   second person who has to do that is likely to not want to deal with
   that nonsense again later.    Finally, there are people who will use
   your code and do cool things.  But they'll generally do things you
   weren't going to think of anyway.  Seeing your work used to do things
   better than you'd have thought of yourself is quite humiliating.  But
   it's also one of the main points of science.


Posted by Titus Brown on 2010-08-28 at 14:29. 

::

   @Shanti, I guess the question is, would they have moved faster or not
   if Galileo had communicated better?    @Erich, well, yes, we agree. I
   don't find it humiliating on the (rare) occasions that other people
   use my code to do more clever things than me, though; I find it
   inspiring!

