Code Layout and Version Control
###############################

:author: C\. Titus Brown
:tags: python
:date: 2007-09-26
:slug: code-layout-and-version-control
:category: python


So, a few people commented on my `how to write Python code that
doesn't suck <http://ivory.idyll.org/blog/sep-07/not-sucking>`__ post,
and I thought I'd respond here rather than in the comments.

First, John Camara suggests adding the MIT license as an option.  I
chose the BSD because it's essentially equivalent to the MIT license,
except for the no-attribution clause, which I think is pretty reasonable;
read more `here <http://www.opensource.org/licenses/bsd-license.php>`__.

Next, John Dawson asks, 

  In the article, you said: "Note that you can always organize your
  actual files in as deep a hierarchy as you want, while keeping the
  public API shallow and easy to use."

  How is this technique best accomplished?

I cover this in a bit more detail in the `Advanced SWC section on
packages <http://ivory.idyll.org/articles/advanced-swc/#packages>`__,
but the essential idea is that you import as many
objects/functions/classes as you can in the top-level package's
``__init__.py``.  This makes them available as ``toplevel.symbol`` as
opposed to ``toplevel.lower1.lower2.symbol``, even if they actually reside
in ``toplevel/lower1/lower2.py::symbol``.

One counterargument to this approach is that you may not want to
import "optional" sub-packages, i.e. packages that may not be used by
everyone using your top-level package, as a matter of performance.  I
contend that (except in extreme cases) this is an issue of usability
over performance, and I tend to weight those 80/20 (that is, usability
is more important than performance, in general).  So I choose better
layouts over performance improvements.

Are there other reasons to keep symbols confined below the top level?
I understand from `Baiju's post
<http://baijum81.livejournal.com/22412.html>`__ that the Zope
community has done so simply to manage the proliferation of names,
which seems sensible.  I like the idea, but until Baiju's post it
always confused me a bit; maybe others haven't been confused and it's
just me.

Finally, Gael Varoquaux asked me (in private e-mail) about version control.
He was hoping that I had some killer text that would convince people to
use version control, instead of (for example) having every file in the
directory tagged by date.

Unfortunately, I don't have any really convincing text.  I feel that
I'm most convincing when I'm talking about the need for testing,
although that's apparently so much less obvious than version control
that my arguments still don't work well ;).  (Yes, it's
counterintuitive to me, but every serious programmer I know uses
version control, while many of them don't write any automated tests at
all!)

Moreover, I think -- at least in academia -- that switching approaches
often comes down to a matter of ego.  **People don't want to change,
because they think they know better than you.** (This is as opposed to
the somewhat more understandable reason of them being unwilling to
spend the time to learn the new technique.)  As you can probably tell
from my frustration in the `first
<http://ivory.idyll.org/blog/sep-07/not-sucking>`__ and `second
<http://ivory.idyll.org/blog/sep-07/not-sucking-v2>`__ drafts of the
original article, I am in favor of submerging your own ego regarding
code *appearance*; the same is true of tool use.  I strongly believe
that individual programmers usually *don't* know best and that they
should be open to new approaches; the rare times when I listen to
other people is when I make the most headway on my big problems!
Overcoming ego demands a certain delicacy of approach.

What to say, then, in favor of version control?  Forget the arguments
that will appeal to experienced programmers - we're talking about
people newly off the boat, so to speak. What we need are arguments
that sidestep ego as much as possible while pushing the rewards of
putting in the necessary effort to learn a VCS.

My arguments would be:

 1. Using version control will let you figure out what has changed
    between two versions.  This comes in particularly handy when you
    need to track down bugs, or figure out precisely what changes you've
    made since your last release.

    Yes, you can keep dated copies of individual files, or even your entire
    archive, but version control will do this more quickly and easily and
    moreover provide a better interface to querying them.

 2. Using version control through a public site like SourceForge or
    Google Code gets your code out there in the search engines and
    encourages people to collaborate with you.  It's also a good way
    to build your resume: for example, I'm unlikely to consider hiring
    someone who has no verifiable open source project experience.

 3. Using version control is a great way to quickly and automatically
    back up your code.  Since most VCS explicitly support remote
    repositories, off-site backups are built into the code!  You can even
    have Google or SourceForge back up your code *for* you, which is
    pretty dang convenient.

 4. When you *do* get collaborators, version control is going to be
    necessary.  Be optimistic -- plan ahead!

Comments welcome, either `privately <mailto:titus@idyll.org>`__ or on this
post.

thanks,

--titus


----

**Legacy Comments**


Posted by Tennessee Leeuwenburg on 2007-09-26 at 20:04. 

::

   I find that version control is essentially mandatory in a team
   environment. It simply becomes part of the workflow, supporting and
   simplifying the job of coding.    It is also a form of backup. Have
   your CVS repository somewhere other than your own computer and relax a
   little.


Posted by michael schurter on 2007-09-27 at 13:46. 

::

   CVS?  Try bzr.  :)  It can be used in a centralized or distributed way
   (or best yet: both at once!).    Senseless fanboying aside, there are
   a number of great VCSes out there and no good reason **not** to use
   them.    Thanks for the great post!  As a relatively new Python
   developer (coming from PHPland), learning how to organize my projects
   has been very difficult.


Posted by Titus Brown on 2007-09-27 at 14:26. 

::

   Michael, thanks for the kind comment!    With respect to bzr, the key
   words are "everyone has  clients for them and everyone knows how to
   use them."  I don't feel like this is true for **any** of the
   distributed VCS, while it is certainly true of both CVS and SVN... but
   I'll add something about using a distributed VCS.    thanks,  --titus


Posted by Carl Friedrich Bolz on 2007-09-27 at 14:27. 

::

   The py-lib contains a nifty (if maybe hackish) approach to separate
   the directory/file hierarchy and the exposed namespace of a package.
   See the <em>_init_</em>.py file of the py-lib itself as an example:
   <a href="http://codespeak.net/svn/py/dist/py/<em>_init_</em>.py">http:
   //codespeak.net/svn/py/dist/py/<em>_init_</em>.py</a>    The
   "exportdefs" dictionary maps names in the "py" package to names in
   files. Those files are imported lazily when the package is accessed.
   This means you  can say "import py" and then use all the subpackages
   of the py-lib and have them loaded on demand.


Posted by Paddy3118 on 2007-09-27 at 16:05. 

::

   Maybe the experienced programmers should act as if VCS is like
   breathing air - done witout thought (or question). The new programmers
   might then adopt the same view.    - Paddy.

