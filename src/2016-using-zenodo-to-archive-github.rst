You can make GitHub repositories archival by using Zenodo or Figshare!
######################################################################

:author: C\. Titus Brown
:tags: github,zenodo,doi,datalib
:date: 2016-11-16
:slug: 2016-using-zenodo-to-archive-github
:category: science

Bioinformatics researchers are increasingly pointing reviewers and
readers at their GitHub repositories in the Methods sections of their
papers. Great!  Making the scripts and source code for methods
available via a public version control system is a vast improvement
over the methods of yore ("e-mail me for the scripts" or "here's a
tarball that will go away in 6 months").

A common point of concern, however, is that GitHub repositories are
not *archival*.  That is, you can modify, rewrite, delete, or
otherwise irreversibly mess with the contents of a git repository.
And, of course, GitHub could go the way of Sourceforge and Google Code
at any point.

So GitHub is not a solution to the problem of making scripts and software
available as part of the permanent record of a publication.

But! Never fear! The folk at `Zenodo <https://zenodo.org/>`__ and
`Mozilla Science Lab (in collaboration with Figshare)
<https://mozillascience.github.io/code-research-object/>`__ have
solutions for you!

I'll tell you about the Zenodo solution, because that's the one we
use, but the Figshare approach should work as well.

How Zenodo works
----------------

Briely, at Zenodo you can set up a connection between Zenodo and
GitHub where Zenodo watches your repository and produces a tarball and
a DOI every time you cut a release.

For example, see https://zenodo.org/record/31258, which
archives https://github.com/dib-lab/khmer/releases/tag/v2.0 and
has the DOI http://doi.org/10.5281/zenodo.31258.

When we release khmer 2.1 (soon!), Zenodo will automatically detect
the release, pull down the tar file of the repo at that version, and
produce a new DOI.

The DOI and tarball will then be independent of GitHub and I cannot
edit, modify or delete the contents of the Zenodo-produced archive
from that point forward.

Yes, automatically.  All of this will be done *automatically*. We just
have to make a release.

Yes, the DOI is permanent and Zenodo is archival!
-------------------------------------------------

Zenodo is an open-access archive that is `recommended by Peter Suber
<https://cyber.harvard.edu/hoap/How_to_make_your_own_work_open_access#Deposit_in_an_OA_repository_.28.22green.22_OA.29>`__
(as is Figshare).

While I cannot quickly find a good high level summary of how DOIs and
archiving and LOCKSS/CLOCKSS all work together, here is what I understand
to be the case:

* Digital object identifiers are permanent and persistent. (See
  `Wikipedia on DOIs
  <https://en.wikipedia.org/wiki/Digital_object_identifier>`__)

* Zenodo policies `say <https://zenodo.org/policies>`__:

  "Retention period

  Items will be retained for the lifetime of the repository. This is
  currently the lifetime of the host laboratory CERN, which currently
  has an experimental programme defined for the next 20 years at
  least."

So I think this is at least as good as any other archival solution I've
found.

Why is this better than journal-specific archives and supplemental data?
------------------------------------------------------------------------

Some journals request or require that you upload code and data to their
own internal archive.  This is often done in painful formats like PDF or
XLSX, which may guarantee that a human can look at the files but does
little to encourage reuse.

At least for source code and smallish data sets, having the code and data
available in a version controlled repository is far superior.  This is
(hopefully :) the place where the code and data is actually being used
by the original researchers,
so having it kept in that format can only lower barriers to reuse.

And, just as importantly, getting a DOI for code and data means that
people can be more granular in their citation and reference sections -
they can cite the specific software they're referencing, they can
point at specific versions, and they can indicate exactly which data
set they're working with.  This prevents readers from going down the
citation network rabbit hole where they have to read the cited paper
in order to figure out what data set or code is being reused and how
it differs from the remixed version.

Bonus: Why is the combination of GitHub/Zenodo/DOI better than an institutional repository?
-------------------------------------------------------------------------------------------

I've had a few discussions with librarians who seem inclined to point
researchers at their own institutional repositories for archiving code
and data.  Personally, I think having GitHub and Zenodo do all of this
automatically for me is the
perfect solution:

* quick and easy to configure (it takes about 3 minutes);

* polished and easy user interface;

* integrated with our daily workflow (GitHub);

* completely automatic;

* independent of whatever institution happens to be employing me today;

so I see no reason to switch to using anything else unless it solves
even more problems for me :).  I'd love to hear contrasting
viewpoints, though!

thanks!

--titus
