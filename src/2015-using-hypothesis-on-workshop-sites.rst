Using Hypothesis to put annotations on workshop web sites
#########################################################

:author: C\. Titus Brown
:tags: hypothesis,annotation
:date: 2015-11-15
:slug: 2015-using-hypothesis-on-workshop-sites
:category: teaching

I've often wanted to mark up arbitrary Web sites with annotations and
reminders, and it's always been puzzling to me that this is missing
from the Web.  In recent years, I've heard more and more about a small
non-profit called `Hypothesis <https://hypothes.is/>`__, which
provides this general functionality via both a Chrome plugin and
JavaScript (as well as a proxy).

A few weeks back, we invited Jon Udell from Hypothesis out to visit Davis,
and my lab spent a couple of hours with him exploring Hypothesis.  The short
version is it looks totally awesome, and I think
there are dozens of uses, but one *specific* use case that came up several
times was to annotate `Software Carpentry <http://software-carpentry.org>`__
and `Data Carpentry <http://datacarpentry.org>`__ lessons with it.

This should be very do-able, but there's a catch -- the lessons are
duplicated independently across workshops and taught many times over
many years, with slight modifications.  So we don't want to annotate
just one site - we want the annotations to show up across *all* the
copies of a lesson so that we don't have to remember which workshop version
we annotated.

When we discussed this with Jon, he said "yep. Should work!" What he
explained to us was this: in order to tie annotations to text even in
the face of editing and textual updates, Hypothesis uses robust
anchoring techniques to place each annotation within the document.
Moreover, Hypothesis can tie things to *canonical* URLs, so if there's
a single URL specified on all of the classes as the "one true
location" then the annotation will appear on all pages with that
specification.

So, today I tried it out. And it worked!

----

I have two sites, one from a workshop in May and one from a workshop in October
(the October one was actually canceled before I changed any real content,
so the sites are essentially the same ;).  Here are the URLs:

http://2015-oct-nonmodel.readthedocs.org/en/latest/

http://2015-may-nonmodel.readthedocs.org/en/latest/

First, I wanted to enable hypothesis on them.  These are `Sphinx
<http://sphinx-doc.org/>`__ Web sites, constructed from a combination
of `reStructuredText <http://docutils.sourceforge.net/rst.html>`__
marked-up content and `Jinja2 <http://jinja.pocoo.org/>`__ templates,
so to add it to all the pages I just edited the base templates to include the
Hypothesis JavaScript::

   <script async defer src="//hypothes.is/embed.js"></script>

I added this to the May site `(commit)
<https://github.com/ngs-docs/2015-may-nonmodel/commit/d76235ae6d128f42c99db7dbbcb4164174aa0ca6>`__
and the October site `(commit)
<https://github.com/ngs-docs/2015-oct-nonmodel/commit/f12681ae995f88e3a18e8646983300012f57aaa3>`__.

Next, I edited the October site so that its `canonical URL
<https://support.google.com/webmasters/answer/139066?hl=en#2>`__ was
that of the May site `(commit)
<https://github.com/ngs-docs/2015-oct-nonmodel/commit/acfe8b380c9048466f515dcac79f2afdee0b0e3f>`__.
This makes it so that Hypothesis understands that annotations should
be applied to both sites, or, to be more precise, that the October
site is not the master site - the May one is.  (The "right" way to do
this is probably to have a site that is always the latest set of
tutorials and then to set the canonical URL to that, but I didn't want
to do all that work for this test.)

Then, after the sites rebuilt on ReadTheDocs and Hypothesis turned on, I
added three comments: `one on text specific to the October site <https://hypothes.is/a/g06kPoL0TWiiLVV4hTeAkQ>`__, `one on text specific to the May site <https://hypothes.is/a/-8Nq7qhySDiNp-VHnj7qyg>`__, and `one on text that appears on both sites <https://hypothes.is/a/vVjLWMSwTkuqAhupUTB3HQ>`__.

And voila, it works!

(If you want to see them yourself, click the "eye" icon, or otherwise fiddle
about with the hypothesis stuff at the top right of the page.)

In summary,

* I can add annotations to common text on one site, and it will appear
  on the other.

* Annotations specific to text on one site or the other will only be tied
  to that site.

* All is well.

So, this appears to be something that I can just add into all my sites
in the future. Huzzah!

----

For Software and Data Carpentry to use this robustly, they would need
to specify a canonical URL for each lesson - this probably makes sense
to do anyway ;).  Note that the canonical URL probably doesn't need to
actually resolve to anything, although probably it'd be bad form if
it didn't...

SWC and DC don't have to enable Hypothesis on all (or any) of their
lessons; the canonical URL will work just fine with the plugin or the
proxy.  But they could enable Hypothesis on some workshop pages and
have it lurk quietly in the upper right of the page until it's needed
- I envision this being really useful for instructors and TAs who
want to make notes in the heat of the moment.

Note, since Hypothesis makes it straightforward to retrieve
annotations by annotated URL (or at least I think it does - I can't
figure out how to do it, but Jon showed us ;), it is also easy when
revising lessons to go look at all the annotations on a page and use
that to revise the page.  If Hypothesis catches on amongst
instructors, this could become part of the standard lesson update
process.

I've got a bunch of ideas to try out with Hypothesis, so expect more.
But this was a fun (and easy!) start!

--titus
