Virtual machines considered harmful for reproducibility
#######################################################

:author: C\. Titus Brown
:tags: reproducibility,should-be-obvious
:date: 2012-11-06
:slug: vms-considered-harmful
:category: science
:status: draft

In his paper, `Reproducible Research and Cloud Computing <http://escience.washington.edu/blog/reproducible-research-and-cloud-computing>`__, Bill Howe asks:

    What happens if you do all your work on a virtual machine hosted
    in the cloud? When it came time to publish, you might make a
    snapshot of the VM, make it public, and cite it in your
    paper. Those who wish to reproduce your experiments would launch
    the virtual machine (on their dime) and have access to your entire
    experimental environment --- the code, the data, the environment,
    log files, notes, etc. There would be no need to install a network
    of complex, version-sensitive inter-dependent prerequisites.

Indeed, `what
<http://ged.msu.edu/angus/diginorm-2012/pipeline-notes.html>`__ a
`good
<http://www.nature.com/ismej/journal/vaop/ncurrent/full/ismej2012123a.html>`__
idea!  But not, I think, sufficient.

This idea -- that posting a VM is sufficient for reproducibility --
has hit my Twitter feed a couple of times now, and each time I feel
compelled to make the point that this isn't *useful* reproducibility.
Mick Watson put it best when he said `you can't install an image for
every pipeline you want
<https://twitter.com/BioMickWatson/status/265037994526928896>`__.

To put it another way, it is certainly *true* that posting a virtual
machine is a way to make your research reproducible.  It's just not a
very *useful* way, in the sense that it effectively blocks remixing
or mashing up the code.  In `my post on the diginorm paper
<http://ivory.idyll.org/blog/replication-i.html>`__ I made this point
in response to some poo-pooing of replicability:

   Fifth, and probably most significant from a practical perspective,
   Graham misses the point of reuse. In bioinformatics, it behooves us
   to reuse proven (aka published) tools -- at least we know they
   worked for someone, at least once, which is not usually the case
   for newly written software.

In essence, providing a gigantic black box of custom installed code
that was installed, set up, and executed by experts just isn't
very useful to many people.

I think `the ENCODE effort <http://scofield.bx.psu.edu/~dannon/encodevm/>`__
did it about 3/4 right --

   As part of the supplementary material for this paper, we have
   established a virtual machine instance of the software, using the
   code bundles from
   ftp.ebi.ac.uk/pub/databases/ensembl/encode/supplementary/, where
   each analysis program has been tested and run.

I could have wished that each bit of code was in a separate git or hg
repository, for example, or that there were small test data sets; this
would have maximized my ability to dive into the code and play with
it.  But this is a giant step forward all on its own, compared to
`what pretty much everyone else does
<http://ivory.idyll.org/blog/anecdotal-science.html>`__!  And it's
*really* fantastic to see it being done by a massive genomics
consortium

A related topic that also comes up occasionally is distributing
software via VM.  Scott Cain gave a great talk at BOSC 2012 on `Tripal
<http://tripal.sourceforge.net/>`__, a Web interface for Chado, and
mentioned that `there's a VM
<http://gmod.org/wiki/Tripal_Tutorial_(v0.3.1b_VM)>`__ available.
During the Q&A I apparently confused him by recommending that instead
of, or in addition to, a VM, he provide a source code repository along
with an install script pinned to a particular Linux install --
something that's really easy to do these days, what with the clouds
and open sourciness.  His response was "why would you need anything
more than the VM?"  Again, the reason comes back to Mick's observation
above: you can't (or at least shouldn't need to) install a VM for
every software package or pipeline you need to execute!

If you think about the dependency chain here, it's *easy* to build a
VM if you automate the install process, and providing that install
script for even *one* OS can demystify the install process for others;
conversely, just because you provide a VM doesn't mean that anyone
*other* than you can install your software.  So why not make life
easy for everyone?

There is a deeper principle at work here: the distinction between a
*user* and a *maker*.  A *user* merely wants to take your software and
run with it; a *maker* wants to probe, remix, and mash up your
software.  To maximize the benefit of our scientific software, we
should be enabling *makers*, not *users*.  To do anything else limits
the use of our software to our own imagination, rather than enabling
serendipity.  And wouldn't that be a shame?

--titus
