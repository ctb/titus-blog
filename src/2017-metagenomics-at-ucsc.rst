A (revised and updated) shotgun metagenome workshop at UC Santa Cruz
####################################################################

:author: C\. Titus Brown
:tags: metagenomics,ngs,workshop
:date: 2017-4-24
:slug: 2017-metagenomics-at-ucsc
:category: teaching

We just finished teaching a `second version of our two-day shotgun
metagenome analysis workshop
<https://2017-ucsc-metagenomics.readthedocs.io/en/latest/>`__, this
time at UC Santa Cruz (`the first one was in October 2016, at Scripps
Institute of Oceanography
<https://2016-metagenomics-sio.readthedocs.io/en/latest/>`__).
Harriet Alexander led the workshop and Phillip Brooks and I co-taught;
Luiz Irber, Shannon Joslin, and Taylor Reiter TAed.  The workshop was
hosted by `Professor Marilou Sison-Mangus
<https://oceansci.ucsc.edu/faculty/singleton.php?&singleton=true&cruz_id=msisonma>`__
at the Earth and Marine Sciences Building.

(Note that Harriet will be running `an expanded version of this
workshop
<http://ivory.idyll.org/dibsi/workshops.html#environmental-metagenomics-dibsi-em>`__
at our summer institute, July 17-21. Registration is still open!)

About 30-35 people came the first day, and about 30 were there on the
second.

Some good - new lessons!
------------------------

In addition to our old lessons on `Illumina read QC <https://2017-ucsc-metagenomics.readthedocs.io/en/latest/quality.html>`__, `assembly
with MEGAHIT <https://2017-ucsc-metagenomics.readthedocs.io/en/latest/assemble.html>`__, `annotation with Prokka <https://2017-ucsc-metagenomics.readthedocs.io/en/latest/prokka_tutorial.html>`__, and `quantification
with Salmon <https://2017-ucsc-metagenomics.readthedocs.io/en/latest/salmon_tutorial.html>`__, we introduced two new lessons --

* `binning genomes out of your metagenomes with MaxBin
  <https://2017-ucsc-metagenomics.readthedocs.io/en/latest/binning.html>`__ -
  we used MaxBin, which was fast enough to use in an hour lesson.

* `Quickly searching and comparing your samples with sourmash <https://2017-ucsc-metagenomics.readthedocs.io/en/latest/sourmash.html>`__ - this is the
  first time we've taught `sourmash <http://sourmash.readthedocs.io/en/latest/>`__ to anyone outside the lab, and I think it
  went pretty well. Plus we now have a sourmash tutorial!

For all of this we used `subset data
<https://2017-ucsc-metagenomics.readthedocs.io/en/latest/DATA.html>`__
from `Hu et al. (the Banfield Lab), 2016
<http://mbio.asm.org/content/7/1/e01669-15.full>`__, which is a great
low-complexity metagenome.

More good - using XSEDE Jetstream instead of Amazon Web Services!
-----------------------------------------------------------------

This was the first genomics workshop in many years where we didn't use
Amazon Web Services - we used XSEDE Jetstream instead.  See `our login
instructions here
<https://2017-ucsc-metagenomics.readthedocs.io/en/latest/jetstream/boot.html>`__.

Why are we abandoning Amazon? Two reasons --

* while we've been teaching it for almost 8 years now, the conversion
  rate seems to be very low: AFAICT our students aren't using it,
  because it costs money and their advisors don't want to pay for AWS
  when they can use institutional resources.  (This is anecdotal.)

* since sometime before October 2016, Amazon changed their
  registration system so that newly registered people cannot start up
  instances for a few hours after their first try. This is death on
  half-day and two-days workshops.  `(You can read a bit more about it
  here. <https://www.mail-archive.com/discuss@lists.software-carpentry.org/msg02940.html>`__)
  There seems to be nothing that AWS folk can do to help us so we are
  giving up.

I am happy to report that Jetstream went more smoothly than AWS in
almost every way and seems to perfectly meet our needs for training!
We may have more to say about it after `our summer institute's use
<http://ivory.idyll.org/blog/2017-dibsi-xsede-request.html>`__.

I also suspect that people will be more inclined to use Jetstream if
they can get allocations on it for free; there was significant interest
in this during the workshop.

Other good --
-------------

* As always, the people that attended the workshop were fantastic, and dealt
  with our occasional hiccups pretty well!

* We managed to pretty smoothly move between the command line and the Jupyter
  Notebook for two of the lessons, which was pretty cool.

* We managed to implement a simple demo of a tetramer nucleotide
  frequency clustering system using sourmash and t-SNE - see `the
  notebook on github
  <https://github.com/ngs-docs/2017-ucsc-metagenomics/blob/clustering/files/sourmash_tetramer-cluster-extract.ipynb>`__
  (which should be run `after the initial steps in the binning lesson
  <https://2017-ucsc-metagenomics.readthedocs.io/en/latest/binning.html>`__).

There is no bad or ugly
-----------------------

Nothing went wrong! Which I guess is a 'good' all on its own!

There were a few minor issues with the Jetstream desktop, and some
problems with starting up Jetstream instances every now and then, and
the guest network at UCSC blocked port 8000 (which we used for
Jupyter), but most of the time we could work around these issues.

Feedback from participants
--------------------------

The in-person feedback (which is admittedly always kinder than the
anonymous feedback :) was excellent - students really liked the hands-on
teaching style (Carpentry-style, but with copy/paste) and the slow
teaching pace with lots of time for questions was well received.

Misc notes
----------

As always, our materials are available under CC0 on github - the URL
is `https://github.com/ngs-docs/2017-ucsc-metagenomics
<https://github.com/ngs-docs/2017-ucsc-metagenomics>`__.

--titus
