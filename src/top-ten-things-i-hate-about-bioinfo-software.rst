What I'm REALLY thinking about when I use your bioinformatics software
######################################################################

:author: C\. Titus Brown
:tags: science,reviews,bioinformatics
:date: 2012-01-05
:slug: top-ten-things-i-hate-about-bioinfo-software
:category: science


If you're like me, we pretend to care about the science in
bioinformatics software.  But what we really do is try to find reasons
not to outright loathe the software -- because, lud knows, there are
usually plenty of reasons to hate it.

In no particular order, here are the top 10 things I hate about your
bioinformatics software.  You know who I'm talking about.

1. You posted it on SourceForge (and so I can't download the damn
   thing using a simple URL).

2. You're not using version control (and hence are not a scientist).

3. You put _ in the damned file name unnecessarily (that requires a shift key on my keyboard).

4. fizbam-0.9.3.tar.gz either untars into the current directory, OR a directory named 'fizbam'.  Alternatively, you named it fizbam-0.9.3-2011010101010101010101010101020.tar.gz and it untars into THAT monster of a name (and my ls goes off the screen).

5. You have no README, or, if you do, it's a one-liner that refers to a URL (didn't I already download your damned software?)  OR 5a. Your README file is in HTML (less is better than lynx, dontcha know?)

6. Running 'make' rebuilds everything from scratch every time you run it (seriously?)

7. There are neither tests nor examples; or, if there are, I can't run 'em, and even if they do run, I have no idea if the results are correct.

8. The output is in some weird format and/or location (wait, I have to do a find to find the last file written, and then guess as to its format?)

9. The command line options are poorly labeled and described, use random abbreviations, and/or are sensitive to order (unlike every good command-line parsing library written).

10. You CaMEl-CaSED your software name so that not even tab completion can figure it out (program names should be all lower-case, as Darwin intended).

---

Post your top ten and send me the URLs... :)

--titus


----

**Legacy Comments**


Posted by Paul Agapow on 2012-01-05 at 04:26. 

::

   My complaints are more about the pragmatic issues of using software:
   &lt;<a href="http://biocoders.net/groups/bioinformatics-and-
   computational-biology/forum/topic/what-im-really-thinking-about-when-i
   -use-your-bioinformatics-software/">http://biocoders.net/groups
   /bioinformatics-and-computational-biology/forum/topic/what-im-really-
   thinking-about-when-i-use-your-bioinformatics-software/</a>&gt;


Posted by Ian Holmes on 2012-01-05 at 05:20. 

::

   Re point #8, see also <a href="http://biowiki.org/FileFormatDesign">ht
   tp://biowiki.org/FileFormatDesign</a>


Posted by Egon Willighagen on 2012-01-05 at 07:02. 

::

   Maybe talk to Cameron Neylon to write up a 'user perspective' for Open
   Research Computation?    BTW, SourceForge perfectly well allows
   deeplinking to downloadables with a single URL. I make use of that
   myself.


Posted by Preecha Patumcharoenpol on 2012-01-05 at 07:40. 

::

   I thing I hate most is ad-hoc fetch-and-build.sh


Posted by Ian Holmes on 2012-01-05 at 08:32. 

::

   That "file format design" list was actually a response to a less
   facetious (and far less amusing) post that is more relevant here    <a
   href="http://biowiki.org/BioinformaticsToolDesign">http://biowiki.org/
   BioinformaticsToolDesign</a>


Posted by Aaron Quinlan on 2012-01-05 at 10:51. 

::

   Thanks for the chuckle.  Unfortunately, I think my software suffers
   from a few of these - a resolution for the new year, I suppose.


Posted by Arend Hintze on 2012-01-06 at 08:03. 

::

   Don't forget:  linking to libraries that are not included and can't be
   found anymore    Cheers Arend

