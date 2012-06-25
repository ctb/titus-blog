Proposal: the Python Buildhaus
##############################

:author: C\. Titus Brown
:tags: python,testing
:date: 2009-05-15
:slug: buildhaus-proposal
:category: python


I just submitted a `Mellon Award for Tech Collaboration nomination <http://matc.mellon.org/>`__ for the Python Buildhaus.  What's that, you ask?

   The Python Buildhaus is a project to systematically build, test and
   release Open Source Python packages on Windows, Mac OS X, and a
   wide array of other UNIX architectures and operating systems (see
   snakebite.org for list). In addition to providing machine access,
   software support, and process support, we hope to create a set of
   best practices and process documentation to help the community
   address cross-platform compatibility issues. We will also build
   tools to extend the impact of this effort beyond Michigan State by
   providing longer-lasting developer resources, e.g. tools to
   auto-build Python eggs and installers across multiple platforms.

   This will be an open resource for the Python community.

See `the Python Buildhaus <http://moss.wikidot.com/buildhaus>`__ and
`our proposal
<http://moss.wikidot.com/buildhaus:mellon09-proposal>`__.

This is basically an attempt to use Snakebite to push specifically to
help with the cross-platform distribution problem.

--titus


----

**Legacy Comments**


Posted by Tarek Ziade on 2009-05-16 at 13:20. 

::

   What about having python's Distutils as your first use case ? ;)
   -&gt; every time a package is uploaded in PyPI, your infrastructure
   downloads it, then tries to run various distutils commands, and
   eventually install it under various platforms.    Of course, this
   probably means you have to do every test in a fresh OS, then re-
   initialize it for security reasons.


Posted by Titus Brown on 2009-05-16 at 13:23. 

::

   Exactly right.    Getting the infrastructure etc. to do that properly
   is tough, however, especially when you're trying to have students
   learn from the work ;)    Not sure how to deal with the security
   concerns.  It should be possible on i386 archs with VMs, but I don't
   know what to do about other archs.


Posted by Tarek Ziade on 2009-05-17 at 09:47. 

::

   Yes it's a complex topic.    If the buildbot is run into a VM, I don't
   think it's possible for some code to bypass it or brake the host. I
   think that the only thing a code can do is knowing it's running inside
   a VM.    Then, if the VM is isolated from the network, (which should
   not harm the tests) the security of the server should not be broken.
   Now if the code has network features I don't know :)..    For the
   arch, I use VMWare here to simulate 64bits on 32bits servers and vice-
   versa, but I don't know about other virtual systems.    For the re-
   initialize part, VMWare has snapshots, but maybe a more elegant and
   fast way to re-initialize the VMs would be to use a ZFS. Never tried
   it though.    Anyways,  very interesting project

