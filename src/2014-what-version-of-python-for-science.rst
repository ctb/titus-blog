What version of Python should we use to for computational science courses?
##########################################################################

:author: C\. Titus Brown
:tags: python,science,teaching
:date: 2014-12-02
:slug: 2014-what-version-of-python-for-science
:category: science

Brian O'Shea (a physics prof at Michigan State) asked me the
following, and I thought I'd post it on my blog to get a broader set
of responses.  I know the answer is "Python 3", but I would appreciate
specific thoughts from people with experience either with the specific
packages below, or in teaching Python 3 more generally.

(For the record, I continue to teach and develop in Python 2, but each
year comes closer to switching to Python 3...)

----

We're going to start teaching courses for the new CMSE [ computational
science] department next year, and we're using Python as the language.
I need to decide whether to teach it using python 2.x or python 3.x.
I'm curious about which one you have chosen to use when teaching your
own courses, and why you made that choice.  (Also, it'd be interesting
to know if/why you regret that choice?)

The intro courses are aimed at students who plan to use computational
and data science for research, other classes, and ultimately in their
academic/industrial careers.  We anticipate that it'll mostly be
science/math and engineering students in the beginning, but there's
significant interest from social science and humanities folks on
campus.  Given the audience and goals, my choice of programming
language is fairly utilitarian - we want to introduce students to
standard numerical packages (numpy, scipy, matplotlib, h5py, pandas,
ipython) and also some of the discipline-specific packages, and get
them into the mindset of "I have a problem, somebody has probably
already written a tool to address this, let's not reinvent the wheel."
So, I want to choose the version of Python that's likely to work well
with pretty much any relatively widely-used Python package.  My
impression, based on a variety of blog posts and articles that I've
found, is that the mainstream libraries work just fine with Python 3
(e.g., matplotlib), but a lot of other stuff simply doesn't work at
this point.

This course is going to be the gateway course for our new minor/major,
and a lot of later courses will be based on it (the graduate version
of the course will be the gateway course for the certificate, and
presumably taken by lots of grad students here at MSU).  I'd like to
make the most sensible choice given that we'll be creating course
materials that will be used by other faculty, and which may stick
around for a while...  Anyway, any thoughts you have would be
appreciated!

----

Thoughts? Comments?

--titus
