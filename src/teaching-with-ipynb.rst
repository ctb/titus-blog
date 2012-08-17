Some early experience in teaching using ipython notebook
########################################################

:author: C\. Titus Brown
:tags: python,ipynb,ngs
:date: 2012-06-08
:slug: teaching-with-ipynb
:category: science


As part of the `2012 Analyzing Next-Generation Sequencing Data course
<http://bioinformatics.msu.edu/ngs-summer-course-2012>`__, I've been
trying out ipython notebook for the tutorials.

In previous years, our tutorials all looked like this: `Short read
assembly with Velvet
<http://ged.msu.edu/angus/tutorials-2011/short-read-assembly-velvet.html>`__
-- basically, reStructuredText files integrated with Sphinx.  This had a lot
of advantages, including Googleability and simplicity; but it also meant
that students spent a lot of time copying and pasting commands.

This year, I tried mixing things up with some ipython notebook, using
pre-written notebooks -- see for example a static view of the `BLAST
notebook
<http://ged.msu.edu/angus/tutorials-2012/files/static-ngs-10-blast.html>`__.
The notebooks are sourced at
https://github.com/ngs-docs/ngs-notebooks, and can be automatically
updated and placed on an EC2 instance for the students to run.  The
idea is that the students can simply shift-ENTER through the notebooks;
shell commands can easily be run with '!', and we can integrate in
python code that graphs and explores the outputs.

Once we got past the basic teething pains of badly written notebooks,
broken delivery mechanisms, proper ipython parameters, etc., things seemed
to work really well.  It's been great to be able to add code, annotate
code, and graph stuff interactively!

Along the way, though, a few points have emerged.

**First**, ipython notebook adds a little bit of confusion to the
process.  Even though it's pretty simple, when you're throwing it in
on top of UNIX, EC2, bioinformatics, and Python, people's minds tend
to boggle.

For this reason, it's not yet clear how good an addition ipynb is to
the course.  We can't get away with replacing the shell with ipynb,
for a variety of reasons; so it represents an extra cognitive burden.
I think for an entire term course it will be an unambiguous win, but
for an intensive workshop it may be one thing too many.

I should have a better feeling for this next week.

**Second**, in practice, ipython notebooks need to be written so that
they can be executed multiple times on the same machine.  Workshop
attendees start out very confused about the order of commands vs the
order of execution, and even though ipynb makes this relatively
simple, if they get into trouble it is nice to be able to tell them to
just rerun the entire notebook.  So the notebook commands have to be
designed this way -- for one example, if you're copying a file, make
sure to use 'cp -f' so that it doesn't ask if the file needs to be
copied again.

**Third**, in practice, ipython notebooks cannot contain long
commands.  If the entire notebook can't be re-run in about 1 minute,
then it's too long.  This became really clear with Oases and Trinity,
where Oases could easily be run on a small data set in about 1-2
minutes, while Trinity took an hour or more.  Neither people nor
browsers handle that well.  Moreover, if you accidentally run the
time-consuming task twice, you're stuck waiting for it to finish, and
it's annoying and confusing to put multi-execution guards on tasks.

This point is a known challenge with ipython notebook, of course; I've
been talking with Fernando and Brian, among others, about how to deal
with long running tasks.  I'm converging to the idea that long-running
tasks should be run at the command line (maybe using 'make' or
something better?) and then ipython notebook can be used for data analysis
leading to summaries and/or visualization.

**Fourth**, ipython notebooks are a bit difficult to share in static
form, which makes the site less useful.  Right now I've been printing
to HTML and then serving that HTML up statically, which is slow and
not all that satisfying.  There are probably easy solutions for this
but I haven't invested in them ;).

---

In spite of these teething pains, feedback surrounding ipynb has been
reasonably positive.  Remember, these are biologists who may never
have done any previous shell commands or programming, and we are
throwing a lot at them; but overall the basic concepts of ipynb are
simple, and they recognize that.  Moreover, ipython notebook has
enabled extra flexibility in what we present and make possible for
them to do, and they seem to see and appreciate that.

The good news is that we figured all this out in the first week, and I still
have a whole week with the guinea pigs, ahem, course attendees, under my
thumb.  We'll see how it goes!

--titus

p.s. Totally jonesing for a portfolio system that lets me specify a
machine config, then with a single click spawns the machine,
configures it, sucks down a bunch of ipython notebooks, and points me
at the first one!


----

**Legacy Comments**


Posted by Eric O. Lebigot (EOL) on 2012-06-09 at 00:32. 

::

   Thank you for sharing!



----

**Legacy Comments**


Posted by Eric O. Lebigot (EOL) on 2012-06-09 at 00:32. 

::

   Thank you for sharing!


Posted by Fernando Perez on 2012-06-17 at 22:36. 

::

   Hey Titus,    many thanks for the detailed feedback, and sorry that
   it's taken me this long to reply.  I'm also forwarding this to our dev
   list so others read it and keep it in mind as we work through these
   issues.    I'll try to address your comments marking them as you did
   in the main text:    * First: not much we can do about that one, I
   agree that the notebook is not at this point a proper shell
   replacement for everything.  And it is 'yet another thing to learn',
   so it will add to the cognitive load up front.  Though the new %%bash
   cell magic will help in at least making it easier to replace simple
   shell scripts by cells in the notebook, perhaps moving the bar a
   little bit further in the need to drop into the real unix shell.    *
   Second: in response to this point, we've modified our aliases (rm, cp)
   to now mimic one-to-one the shell, meaning they are non-interactive by
   default.  It doesn't completely solve the issue, as you're really
   pointing out the fact that the **entire** notebook needs to be written
   in a way that is mindful of automatic re-execution.  But it may smooth
   some of the more common pitfalls.    I've also just opened an issue:
   https://github.com/ipython/ipython/issues/1977    that I think may
   help on this front, as it will make it easier to rerun notebooks that
   have an exception somewhere in them.    But still, I think the main
   lesson from your point here is one of 'best practices' when writing
   notebooks.  We can improve the experience somewhat, but these are good
   points to keep in mind in general.    * Third: yes, I think the
   tolerance threshold on the total time will vary with people and
   situations, but it's indeed an issue.  We have a few issues opened
   that may also help mitigate this somewhat:
   https://github.com/ipython/ipython/pull/1825
   https://github.com/ipython/ipython/issues/1975    The first is nearly
   ready to merge, and is basically a full implementation of the hack Min
   did for you in Boulder.  In the second, we'll track progress on how to
   best handle **really** long outputs, though we have no implementation
   yet on that one.    A longer-term attack on this problem is something
   we discussed briefly already, the idea of a server-side process that
   would monitor the evolution of a notebook run and would allow web
   clients to reattach and synchronize at any time.  I think something
   like that is really where we need to end up, but it's harder work that
   will take some time to materialize.    * Fourth: for this one at least
   we are working on a proper, clean solution:
   https://github.com/ipython/nbconvert    It's not ready yet, and pull
   requests are warmly welcome, but it's getting there.  The PDF export
   via pdflatex is already pretty decent, and the others will come
   eventually.  I hope we may get some bodies to hack on this one during
   the Scipy sprints.    When this code is in better shape, we'll merge
   it directly into ipython itself, of course.  For now it's just easier
   to have outsiders hack on this little repo by itself.      Overall,
   I'm glad to see that things went reasonably well.  The notebook in its
   current form is a very new system, and we know we have a ton of work
   still ahead of us.  But this kind of from-the-trenches feedback is
   extremely useful, so many thanks for taking the time to write it all
   down.    In the meantime, I hope some of the tips above, along with
   all the improvements coming with 0.13, will help improve the
   experience.


Posted by Carl Smith on 2012-06-18 at 11:37. 

::

   Hi Titus    I just wanted to say thanks for taking the time to post
   this. It's really interesting stuff and I appreciate it.    &gt;p.s.
   Totally jonesing for a portfolio system that  &gt;lets me specify a
   machine config, then with a  &gt;single click spawns the machine,
   configures it,  &gt;sucks down a bunch of ipython notebooks, and
   &gt;points me at the first one!    I'm working on something similar at
   the moment and have some code that can do a lot of this. I've found
   it's much easier to build an AMI and then just configure it on init,
   rather than have it install everything by script. It just takes
   forever to come online and is very slow to debug. On the other hand,
   you can only maintain so many AMIs.    If you do have a pop at writing
   something like what you've described, get in touch, I'll be happy to
   offer what I have.    Thanks again.    All the best    Carl

