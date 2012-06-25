The Scientific Public License?
##############################

:author: C\. Titus Brown
:tags: python,bioinformatics
:date: 2007-09-29
:slug: scientific-public-license
:category: science


After our long `software licensing <software-licensing.html>`__ discussion
on the biology-in-python list, I realized that I wanted something different
in a license for scientific software.

Specifically, I would like to attach the following clause to either a
BSD or L/GPL style license: ::

   Publications relying on derivative works of this software must
   publish all such derivative works under this same license.

The intent is that Dr. Joe Blow, if he chooses to use *and modify* my
software to support his data analysis or computation and then
publishes his results, *must* republish the software with his
modifications.

Has anyone seen anything like this?

I should also link to the `Bayh-Dole Act
<http://en.wikipedia.org/wiki/Bayh-Dole_Act>`__, which -- for
scientists -- is an extremely important law, because it grants
universities copyright to source code produced under federal funding.
This is why Caltech and MSU own my code, rather than the government,
and it's why they can force me to release my code under the GPL.

--titus


----

**Legacy Comments**


Posted by Jonathan Eisen on 2007-09-29 at 17:25. 

::

   I want the same type of license for DATA.  I have written about this
   but never gotten anywhere.  I think it is worth raising with the
   Science Commons folks.     See <a
   href="http://sciencecommons.org/">http://sciencecommons.org/</a>


Posted by Paul Boddie on 2007-09-29 at 20:50. 

::

   To make an amendment as you suggest would be, in effect, to claim that
   conveying the output of the software is equivalent to providing some
   kind of interaction with the software, and that recipients of the
   output have the right to receive the source code, similar to what is
   described in the Affero GPL version 3, section 13 (in the context of
   interaction over a network, however).    Given the predisposition in
   some parts of the academic community to offer data files (and
   services) without any substantial indication of how they were produced
   (apart from hand-waving in a paper), I'd welcome an initiative like
   this, provided it doesn't start to have negative licence
   interoperability effects like the various invalid "non-commercial"
   amendments to the GPL that one sees from various academic software
   producers.


Posted by Titus Brown on 2007-10-01 at 14:33. 

::

   Jonathan, I think data is already covered to some extent, no?  I
   realize not everyone actually adheres to the guidelines, but that
   needs to be enforced by the journals.    Source code is a big problem
   for me, because it's freakin' **methodology**.  Gotta reveal.  Grr.
   Paul, I think you have put it into suitably lawerly language, although
   bear in mind that the requirement only comes into effect if you've
   actually modified the software (at least under my proposal).  Does
   that change the language?  Not sure...


Posted by Paul Boddie on 2007-10-03 at 05:38. 

::

   Titus, I believe that there are some aspects of the GPLv3 which permit
   developers to nominate other parties who will then provide the source
   code for the covered programs:    <a href="http://www.gnu.org/licenses
   /gpl-
   faq.html#SourceAndBinaryOnDifferentSites">http://www.gnu.org/licenses
   /gpl-faq.html#SourceAndBinaryOnDifferentSites</a>    What this means
   is that someone who doesn't modify existing software could still fall
   within the copyleft system by arranging for someone else - possibly
   the original developers - to offer the source code for that software.
   Applying this to an Affero GPL-style licence would mean that someone
   offering data produced by an unmodified program could also make a
   similar arrangement.


Posted by Matt on 2007-12-12 at 15:49. 

::

   Titus, this is a great idea.  I work in a simulation-based community,
   and one of my annoyances is the idea of the Black Box computing,
   wherein one group will publish results and then they will be
   essentially unverifiable without a complete reimplementation of the
   algorithm -- and as I'm sure you're aware, this is non-trivial and
   sometimes impossible.  Part of the peer review process should be code
   inspection, not simply inspection of the results.

