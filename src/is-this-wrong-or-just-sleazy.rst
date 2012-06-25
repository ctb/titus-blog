Intercepting DNS errors
#######################

:author: C\. Titus Brown
:date: 2007-11-13
:slug: is-this-wrong-or-just-sleazy
:category: misc

charter.net, my home ISP, is intercepting name-not-found errors and
replacing them with a host that answers with a Web search page.  This leads to
some "entertaining" problems when trying to ssh to a host that doesn't
exist.

Is this actually wrong or just sleazy?

In fact, it actually breaks my DNS setup, because I have multiple DNS search
domains (idyll.org, caltech.edu) set up on my laptop.  So if I try to ssh to a
host that DOESN'T exist at idyll.org but DOES exist at caltech.edu, Charter
will answer the request that should have failed with a generic Web search host.

I guess I've answered my own question: it's just plain wrong, in addition to
being sleazy, because it breaks DNS.

Bastards.

At least there's an opt-out page... oh, but wait, it relies on browser cookies,
so it doesn't work for ssh.

--titus


----

**Legacy Comments**


Posted by Shannon -jj Behrens on 2007-11-17 at 04:44. 

::

   I forget who it was, but one of the big player tried to do this for
   the whole Internet a few years back.  The whole Internet cried out,
   and eventually they stopped.  It's both sleazy and stupid.

