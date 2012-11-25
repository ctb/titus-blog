What about the Insight Journal, folks?
######################################

:author: C\. Titus Brown
:tags: science,open science,peer review
:date: 2012-11-24
:slug: what-about-the-insight-journal
:category: science

I recently had the pleasure of reviewing an excellent paper that used
actual data (DATA!) to argue that source code needs to be part of the
review process.  (When it is published I will post again about it; for
now, the process of secret handshakes in smoke-filled back rooms must
run its course.  I don't mind blogging about it now because, as is my
custom, I signed my review.)  More about the paper later.

In the paper, the authors argue that `Image Processing On Line (IPOL) <http://www.ipol.im/>`__ represents one possible future, because:

   Each article contains a text describing an algorithm and source
   code, with an online demonstration facility and an archive of
   online experiments. The text and source code are peer-reviewed and
   the demonstration is controlled. IPOL follows the Open Access and
   Reproducible Research models.

OK, awesome!

But what about the `Insight Journal <http://www.insight-journal.org/>`__?
They've been doing this successfully since 2006, and as far as I can tell,
no one has paid any attention to them!?  And I don't entirely understand
why.

Some background
~~~~~~~~~~~~~~~

I was introduced to the Insight Journal by Alex Gouaillard, a French
software developer that I met at Caltech.  He was one of the few
straight up industry-quality software developers that I knew as a grad
student and postdoc, and a great inspiration and colleague.

As part of the project, Alex was writing an image analysis toolkit,
and had settled on `VTK <http://www.vtk.org/>`__ and `ITK
<http://www.itk.org/>`__ for the underlying libraries.  These
libraries are part of a larger software effort by `Kitware
<http://www.kitware.com/>`__, perhaps best known among software geeks
for the CMake system that I think `KDE still uses CMake
<http://lwn.net/Articles/188693/>`__.  CMake doesn't quite fit my
brain, although I've used it for a few cross-platform projects (before
basically giving up on Windows ;), but it is an impressive piece of
work; VTK and ITK are, in my opinion, two of the most awesome pieces
of software ever built by and for academics with NIH sponsorship.
(I'd love to hear contrasting opinions, though.)

I met the Kitware folk out at a VTK/ITK conference in Utah, and was
struck by their professionalism.  This was just when `I was getting
into testing
<http://ivory.idyll.org/blog/software-quality-death-spiral.html>`__,
and I was, ahem, overwhelmed by their dedication to automated tests;
at our first meeting, they seemed to feel that it was necessary to
sit me down and explain **just how important** this was to software
development, despite my demurrals that I got it, I really did.  An
interesting experience.

Part of what came up at that meeting was the Insight Journal, which is
a venue for publishing VTK and ITK code, among other things.  The key
point is this, from `their FAQ <http://www.insight-journal.org/help/faq_generic>`__:

   Q: Does my IJ submission have to include open-source code and data?

   A: Yes, your submissions must include all the material required to
   verify the reproducibility of the content of your article. This
   includes source code, input data, output data, tests and parameters
   used to run the tests. The goal of the Insight Journal is to
   restore the honest practice of the scientific method, which is
   based on the verification of reproducibility by independent
   individuals. Your article must include all the resources that you
   used to arrive to the conclusions of your article, and they should
   be provided in a form that is suitable to be used by others.

F*** yeah, that's right!

Back to the Journal
~~~~~~~~~~~~~~~~~~~

It's clear that the Insight Journal has been practicing (and
`preaching <http://www.insight-journal.org/home/about_generic>`__) the
same stuff that I and others `have
<http://www.dlib.org/dlib/september04/vandesompel/09vandesompel.html>`__
`been <http://www.scfbm.org/content/7/1/2>`__ `preaching
<http://magazine.amstat.org/blog/2011/07/01/trust-your-science/>`__
`also <http://www.ncbi.nlm.nih.gov/pubmed/22144613>`__.  But I *never*
see them come up in these discussions online, nor are they cited
appropriately.  Why is that??

I have a few guesses --

1. No one knows about them, because they've kept to themselves within the
   image processing community.  Respect <fist bump>.

2. They're viewed as too niche (same as #1, but imposed by others).

3. The journal isn't indexed (?) and/or doesn't have an Impact Factor,
   so lots of people don't see a point in contribution to it.  (The
   somewhat arbitrary rules around getting an IF doomed `Open Research
   Computation <http://www.scfbm.org/content/7/1/2>`__.)

4. The journal is just too "weird" -- see `the FAQ <http://www.insight-journal.org/help/faq_generic>`__ for some examples, like:

      Q: What if people don't like my submission, can I withdraw it?

      A: Even better than withdrawing your submission - you can
      improve it! We welcome revisions at any time. Your submission is
      a dynamic thing - if it goes well, you can add more details. If
      people don't "get it", you can clarify the important
      points. Just follow the handle address to your paper, press
      edit, and upload the improved version of your paper. Please,
      however, do not delete the old version. People can learn from
      the steps you took to reach that now highly regarded new
      version...

   This ain't your granny's journal...

Basically, this seems like a journal that is doing a lot of things
"right", and I'd love to know why it hasn't received more visibility.
It's up to `500 publications as of last year
<http://www.kitware.com/blog/home/post/205>`__, note, so it's clearly
not unsuccessful.

If it's not working out, or not doing something right, I'd love to hear about
it.

If it is working out and we're just not noticing it, well, you've been
served.

If it is working out and "we" are ignoring it for some reason, I'd love
to hear about it (and also please define "we" :).

--titus
