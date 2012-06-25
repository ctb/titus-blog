Where should I put scripts for a paper?
#######################################

:author: C\. Titus Brown
:tags: science,bioinformatics,khmer
:date: 2012-03-13
:slug: publishing-paper-pipelines
:category: science


I'm putting together a computational pipeline for a paper - a Makefile
that runs a ton of stuff and outputs files, combined with an ipython
notebook file that takes those output files and turns them into
figures for inclusion in a LaTeX file.  (Yes, very 2000, except for the
ipython notebook which is bleeding edge.)

As we all do, I've written a bunch of paper-specific scripts to process data
and otherwise munge stuff together.  The paper is based on my khmer project,
but the scripts are paper-spec they may morph into something more
project-general.

So where should I put them?

Specifically, should I --

- check them into the paper repository, and make them part of the paper build process?

- check them into the software repository?

- make a special-purpose github repo for them?

My hesitation about combining them with the paper repo is that I write papers
on my laptop and run compute elsewhere, so in my mind they don't belong
together.  Off the top of my head it seems like the best option, though.

If I put them in the software repository, then they will go stale unless I
integrate them into the automated tests.  For that matter, I could put the
paper in the software repo, too, but either way the automated tests for these
scripts will introduce a lot of new and tangential dependencies into the main
software repo.

If I put them in a special-purpose github repo, then they will go stale but
nobody will really care :).  And they will be lost for all eternity.  Which
might be ok.

Does anyone have any experience with this kind of thing?  My last such
scripts+pub effort was before I got the automated testing bug...

(I think we need an "ask the compusciencegeek" service...)

--titus


----

**Legacy Comments**


Posted by Aaron J. Grier on 2012-03-14 at 00:36. 

::

   could you link them between multiple repositories as a git subproject?
   a slight PITA, but they do seem to be a separate code entity from the
   software and the paper.    github for backups, and maybe the
   convenience of external developers... maybe just a cron job that
   resyncs it with whatever branch(es) you deem public.


Posted by Titus Brown on 2012-03-14 at 01:06. 

::

   Aaron -- good question, dunno.  Probably.  Interesting idea.


Posted by Deepak on 2012-03-14 at 01:10. 

::

   If it's specific to the paper, it's part of the paper.  If it's a more
   broadly set of script, I'd recommend putting them in their own
   repository/your script repository and point to them.


Posted by Greg Wilson on 2012-03-14 at 09:51. 

::

   I like the "ask the compusciencegeek" idea: <a href="http://software-
   carpentry.org/2012/03/ask-the-compusciencegeek/">http://software-
   carpentry.org/2012/03/ask-the-compusciencegeek/</a>


Posted by Titus Brown on 2012-03-15 at 12:01. 

::

   Deepak, I think you nailed it.  Thanks.


Posted by Erich Schwarz on 2012-03-15 at 17:36. 

::

   Whatever else you do, make sure you have a static snapshot in your
   supplemental data files.  I know this is useless to **you** and not
   really what you want ... but the great advantage of a static file is
   this: it does not depend on being able to log into a git or whatever
   server N months or years from now.  It just requires the journal's web
   site to not have been nuked.    You can also do all the much better
   stuff -- git repository, branch of your overall code tree, etc. etc.
   etc. -- but **one** snapshot that is just **there**, stuck in the
   permanent archive of supp. data files attached to your paper, will
   mean that there is some minimum that can always be mined out later by
   whoever wants it.  (It's also probably legally useful -- you can point
   to it if you ever need to prove that, yes, on March 16th, 2012, you
   did indeed have this specific set of scripts that you were using --
   but I hope you never need it for that reason...)


Posted by Titus Brown on 2012-03-15 at 22:44. 

::

   Yes, static stuff already planned.  I'm going to host it on S3, also,
   as well as on my own computer.    --titus

