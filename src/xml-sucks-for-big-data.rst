XML sucks for big data, or hadn't you noticed?
##############################################

:author: C\. Titus Brown
:tags: python
:date: 2009-08-25
:slug: xml-sucks-for-big-data
:category: python


Courtesy of Rich Enbody, this blog post, `How XML Threatens Big Data -- Dataspora <http://dataspora.com/blog/xml-and-big-data/>`__, elicited a big "duh" from me.

You don't solve any of the semantic problems with data by elaborating on a
textual format.  You may bring them into the light, but along with the
visibility comes "bureaucracy" -- technology, acronyms, proponents and
opponents, and the usual cruft.

I find the "embrace lazy data modeling" rule rather funny, personally, because
it is the data-world's counterpart to agile methodologies in software
development: solve problems you actually have, rather than all the potential
ones you see.

I do like the "15 minute" rule: if I can't parse *some* useful information
out of your data format in 15 minutes, you've done something very wrong.

--titus


----

**Legacy Comments**


Posted by Carl T. on 2009-08-26 at 10:36. 

::

   The decision to go with XML for big data is often a strategic one made
   without the dev's or dba's consent.  Ease of use and common sense
   often aren't big factors in these decisions.    At that point, it's up
   to the end user to get creative with text processing to circumvent the
   performance limitations (not that I've ever done this sort of thing .
   . .).    But yes, it does suck.    Carl T.


Posted by Harry on 2009-08-26 at 17:26. 

::

   "I do like the "15 minute" rule: if I can't parse some useful
   information out of your data format in 15 minutes, you've done
   something very wrong."    +1

