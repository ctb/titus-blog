The three porridge bowls of sustainable scientific software development
#######################################################################

:author: C\. Titus Brown
:tags: khmer,ssi
:date: 2015-04-16
:slug: 2015-on-sustainable-scientific-software
:category: science

(The below issues are very much on my mind as I think about how to
apply for another NIH grant to fund continued development on `the khmer
project <http://github.com/ged-lab/khmer>`__.)

Imagine that we have a graph of novel functionality versus software
engineering effort for a particular project, cast in the shape of a
tower or pyramid, i.e. a support structure for cool science.

----

.. figure:: ../static/images/2015-ssi-1.png
   :width: 250px

   **Fig 1.** Novel functionality (height) vs software engineering effort
   (area under curve).

----

The more novel functionality implemented, the taller the building, and
the broader the software engineering base needs to be to support the
building.  If you have too much novel functionality with too little
software engineering base, the tower will have too little support and
catastrophe can ensue - either no new functionality can be added past
a certain point, or we discover that much of the implemented
functionality is actually unstable and incorrect.

----

.. figure:: ../static/images/2015-ssi-2.png
   :width: 250px

   **Fig 2.** One failure mode for scientific software development, where
   too much novel functionality (height) is supported by too little
   investment in software engineering effort (area under curve).  This
   results in structural instability and incorrectness.

----

Since everybody likes novel functionality - for example, it's how we
grade grants in science -- this is a very common failure mode.  It is
particularly problematic in situations where we have built a larger
structure by placing many of these individual buildings on top of
others; the entire structure is not much stronger than its weakest
(least supported) component.

Another possible failure mode is if the base becomes too big too soon:

----

.. figure:: ../static/images/2015-ssi-4.png
   :width: 250px

   **Fig 3.** Another failure mode for scientific software development,
   where too little novel functionality (height) is developed, relative
   to too much investment in software engineering effort (area under curve).

----

That is, if too much effort is spent on software engineering at the
expense of building novel functionality on top of it, then the
building remains the same height while the base broadens.  This is a
failure for an individual project, because no new functionality gets
built, and the project falls out of funding.

In the worst case, the base can become over-wrought and be designed to
support functionality that doesn't yet exist. In most situations, this
work will be entirely wasted, either because the base was designed for
the wrong functionality, or because the extra work put into the base
will delay the work put into new features.

Where projects are designed to be building blocks from the start, as
opposed to a leap into the unknown like most small-lab computational
science projects, a different structure is worth investing in -- but
I'm skeptical that this is ever the way to start a project.

----

.. figure:: ../static/images/2015-ssi-5.png
   :width: 250px

   **Fig 4.** What a building block might look like - purposely eschewing
   novel functionality (height) for the purpose of building out a
   support platform for other science.

----

Supporting this kind of project is something that Dan Katz has written
and presented about; see (for example) `A Method to Select
e-Infrastructure Components to Sustain
<http://www.slideshare.net/danielskatz/a-method-to-select>`__.

And, of course, the real danger is that we end up in a situation where
a poorly engineered structure is used to support a much larger body of
scientific work:

----

.. figure:: ../static/images/2015-ssi-6.png
   :width: 250px

   **Fig 5.** The danger of the first failure mode is that we build new
   science (bowl-like shape) on top of a bunch of novel functionality
   (height of spike), with too little engineering (area in the spike).

----

The question that I am trying to understand is this: what are the
lifecycle stages for research software, and how should we design for
them (as researchers), and how should we think about funding them (as
reviewers and program officers)?

To bring things back to the title, how do we make sure we mix the
right amount of software development (cold porridge) with novel
functionality (hot porridge) to make something edible for little bears?

--titus
