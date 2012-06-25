The Future of Bioinformatics (in Python), part 1 (b)
####################################################

:author: C\. Titus Brown
:tags: python,bioinformatics
:date: 2008-09-20
:slug: the-future-of-bioinformatics-part-1b
:category: science


My `last post
<http://ivory.idyll.org/blog/sep-08/the-future-of-bioinformatics-part-1a.html>`__
initiated a discussion on `the biology-in-python
<http://lists.idyll.org/listinfo/biology-in-python>`__ mailing list
about BioPython, among other things.  (`Here
<http://lists.idyll.org/pipermail/biology-in-python/2008-September/000359.html>`__
is a link to the discussion, which is kind of long and unfocused.)

I'm happy that the bip list is serving as a place for people to
interact with the BioPython maintainers to discuss the future of
BioPython.  Hopefully it will lead to more involvement with BioPython,
which would be a good thing.

However, I would like to take the time to question the longer-term
utility of the BioPython/Perl approach.

Bioinformatics -- by which I mostly mean sequence analysis -- has
predominantly followed the UNIX scripting/pipeline model, in which
data is kept in simple, easily-manipulated formats (comma- or
tab-separated values, or CSV) and then processed incrementally.  This
approach has a number of advantages:

  - Each step is isolated and so easier to understand.

  - Each step produces a simple, easy-to-parse kind of data.

  - Each step is language neutral (anything can read CSV).

  - New programmers can learn to use each step in isolation.

  - The components are re-usable.

I've used this exact approach for well over a decade: first for
analyzing `Avida data <http://en.wikipedia.org/wiki/Avida>`__, then
`Earthshine <http://en.wikipedia.org/wiki/Planetshine#Earthshine>`__,
and most recently scads of genome data.

This scripting & pipeline approach is what BioPython and BioPerl
facilitate.  They have a lot of tools for running programs to produce
data and loading in different formats, and they serve as a good
library for this purpose.

The scripting/pipeline approach does have some deficiencies as a
general data-analysis approach:

  - Poor (O(n)) scalability: processing CSV files is hard to do
    supra-linearly, and often the easiest analysis approach is
    actually O(``n**2``)

  - Hard to test: generally people do not test their scripts.  Even
    now that I've become `test infected
    <http://junit.sourceforge.net/doc/testinfected/testing.htm>`__, I
    find scripts to be more difficult to test than modules and
    libraries.  I can *do* it, but it's not natural for me, and
    empirical evidence suggests that it's not natural for most people.

  - Hard to re-use: scripts are often quite fragile with respect to
    assumptions about input data, and these assumptions are rarely
    spelled out or asserted within the code.  This leads to hard-to-diagnose
    errors that often occur deep within the tool chain (if they ever
    show up explicitly).

  - Poor metadata support: try attaching metadata to a CSV file.
    You'll end up with something like GFF3, which overloads the
    metadata field to mean something *slightly* different with each
    database.  Awesome.

  - Too easy to map into SQL databases: yes, you can load CSV files
    into SQL databases, but JOINs are a relatively rare form of actual
    *data analysis* -- and that's what SQL databases are best at.  SQL
    databases do a particular poor job of interval analysis
    (overlap/nearest neighbor extraction/etc.)

  - Poor abstraction: when you load something into memory from a CSV
    file, it's easy to treat it as a list.  Lists are, generally, a
    poor way to interact with sequence annotations.  (This is really
    the same problem as the SQL database problem.)

  - Poor user interface: it's hard to put lipstick on a script!
    People who aren't comfortable with UNIX and file munging
    (i.e. most biologists) have a hard time using scripts, and it's
    rather difficult to wrap a script in a GUI or Web site.

  - Poor reproducibility: every scientist I know has trouble keeping
    track of what parameters they used last time they ran a script.
    Even if they keep track of things in a lab notebook, that's a poor
    medium for reference; logging and notebook software don't seem
    to work very well for this, either.

These deficiencies didn't bother me too much when I was first
interacting with genomic data, but they've become glaringly apparent
in the face of massively parallel sequencing data.  The advent of 454
and (particularly) Solexa sequencing data, where you can get tens of
millions of short reads from a DNA sample, means that scalability
concerns dominate; the ready availability of such data means that
everyone has some and needs to analyze it, and they want good, fast,
correct tools to do so.  In the struggle to cope with this data,
things like `maq <http://maq.sf.net/>`__ emerge, which uses a largely
opaque intermediate data format to make Solexa data analysis scalable;
this ends up being a bit of an intermediate model, where you query and
manipulate maq databases from the command line.  It can be scripted,
but it doesn't have the advantages of language neutrality or easy
parse-ability, and so you lose some of the advantages of scripting.
Since maq doesn't really work as a programming library, either, you
don't gain the benefits of abstraction (it's designed on
`extract-transform-load model
<http://en.wikipedia.org/wiki/Extract,_transform,_load>`__ where you
run each command as an isolated operation).  There are lots of pieces
of bioinformatics software like this: they solve one problem well, but
they're not built to output data that can be easily combined with data
from another program -- at which point you run into format and scripting
issues.

For me, the deficiencies of the scripting model largely come down to
the lack of an abstraction layer that separates **how the data is
stored** from **how I want to query and manipulate the data**. The
introduction of a good abstraction layer immediately potentiates
re-usability, because now I can separate data loading from data query
and start using objects to build queries.  It also makes scalability a
matter of building a good, general solution *once*, or perhaps
building specific solutions that all look the same at the API level.
Once the API is firm, it's relatively straightforward to test; once I
can separate the API from implementation I can implement different
backend storage and retrieval mechanisms as I like (pickle, SQL,
whatever); and I can build a GUI interface without having to change
the internals every time I change data storage types or analysis
algorithms.

On the flip side, once move into a framework, you now have the problem
that you're coding at a level well above most newbie programmers and
biologists, so ease-of-use becomes a real issue.  This means that
people need `good documentation
<http://withoutane.com/rants/2008/09/your-documentation-sucks>`__ and
good tutorials, in particular -- the Achilles Heel of open source &
academic software.  And, of course, the framework has to actually
**work well** and **solve problems** well enough to reward the casual
scientist who needs a tool.

So, with respect to BioPython, I appreciate the functionality it has,
but I think the model is wrong for my work (and for work in a world
full of genomes and sequence).  What I really want is a complete
`solution stack <http://en.wikipedia.org/wiki/Solution_stack>`__ for
sequence analysis and annotation: ::

           data storage
                --
	   object layer
                --           
          scripting layer
                --
        user interface tools

I'm out of time now, but next installment, I'll talk about how `pygr
<http://code.google.com/p/pygr/>`__ provides much of this "solution
stack" for me.

If you're interested in a longer, more detailed version of much the
same argument, see Chris Lee's paper with Stott Parker and Michael
Gorlick, `Evolving from Bioinformatics-in-the-Small to
Bioinformatics-in-the-Large
<http://bioinfo.mbi.ucla.edu/pygr/docs/final.pdf>`__.

For a recent overview of pygr's functionality, see the draft paper,
`Pygr: A Python graph framework for highly scalable comparative
genomics and annotation database analysis
<http://www.doe-mbi.ucla.edu/~leec/newpygrdocs/pygr-draft4.pdf>`__.

--titus


----

**Legacy Comments**


Posted by Kevin Teague on 2008-09-20 at 18:05. 

::

   I think you can also add "poor security" to the deficiencies of the
   pipeline/scripting approach. This ties in with the "difficult to wrap
   a script in a GUI or Web site", bioinformaticians will write scripts
   where the concerns of dealing with data input intermix with the
   concerns of the application logic. This makes it difficult to extract
   the logic into a library, so instead they wrap a web interface around
   scripts, but often aren't fully aware about the dangers of passing
   untrusted data to the shell and end up with systems which are easily
   exploitable by unsavoury characters.    Using tools such as setuptools
   and buildout to auto-generate scripts based on an egg's "entry points"
   is a good start to avoiding munging unrelated concerns together in a
   single script. A how-to on this using this approach w/ setuptools:
   <a href="http://concisionandconcinnity.blogspot.com/2008/09/how-to-
   simplify-python-shell-
   scripts.html">http://concisionandconcinnity.blogspot.com/2008/09/how-
   to-simplify-python-shell-scripts.html</a>    I'd suggest that an
   "abstraction layer that separates how the data is stored" can further
   be be separated out into the concerns of data persistence and the
   concerns of how data is described. It's unfortunate that data
   descriptions are all too often closely tied to data persistence. When
   programming Python, all data is contained within Python objects. It's
   very nice to be able to describe the data within a Python object
   regardless of whether that data objects concern is:     * storing data
   in a relational database (MySQL, PostgreSQL)      * storing data in an
   object persistence system (ZODB, shelve, LDAP)     * storing data in a
   binary format (HDF5, PyTables)      * storing data in a plain-text
   format (CSV, XML)     * sending data over the wire (REST, XML-RPC,
   SOAP, HTML)      * describing data input (HTML Forms, Command-line
   parameters, GUI Forms)      * passing data objects around within a
   Python application (API)    With this perspective on objects and the
   interface(s) that they provide, you can rephrase "I can separate the
   API from implementation, I can implement different backend storage and
   retrieval mechanisms" more succinctly as my favorite quotation from
   'Design Patterns: Elements of Reusable Object-Oriented Software':
   "Program to an interface, not an implementation".    Especially
   thinking about interfaces and implementations not strictly in terms of
   "backends" is good. You may want to swap-out front-end implementations
   as well, and the principals of interfaces and implementations applies
   just as well to front-ends as backends.    Unfortunately Java's use of
   the Interface keyword, and the implementation-specific concerns that
   the Java Interface keyword is designed to tackle means that usage of
   the term Interface to apply as "a description of a set of method
   names, signatures and doc strings" has fallen out of favor. Which is a
   shame, since interface is a very good and succinct term for this
   concept.    I notice that you used the term protocol in your Pygr
   paper, which is a term commonly used as a synonm for interface.
   However, I think interface is a better term for describing a contract
   that an object is providing, since protocol is also commonly used as
   "a convention or standard that controls or enables the connection,
   communication, and data transfer between two computing endpoints." (at
   least according to wikipedia). With protocols I think TCP/IP (the
   internet protocol suite) which is about describing things like "if SYN
   is sent, I respond with ACK".    In Python, the zope.interface and
   zope.schema packages do a great job at describing Python objects,
   independant of other concerns an object may have to deal with (e.g. a
   "web service object", "relational database object", "object database
   object", or "HTML form object" can all be described with the same
   interface). Unfortunately, uptake of these packages outside the Zope
   community has been slow, largely I think because people think,
   "Interface == Java" and they equate using interfaces with static-
   typing and loss of the ability to use duck typing (which isn't true),
   and while Zope 3 proved that the Zope developers had learned many
   lessons about separation of concerns  and loose coupling they were
   still doing a terrible job at separation of concerns in terms of
   marketing and branding.


Posted by Titus Brown on 2008-09-20 at 18:56. 

::

   Kevin, thanks!  Great comments.    Anyone else commenting, please drop
   me a note at t@idyll.org letting me know when you comment, so that I
   can approve your comment. I'm getting too many comment spams to watch
   for new people comments now :(


Posted by Andrew Dalke on 2008-09-22 at 06:13. 

::

   What's your view on dataflow systems?  Do they count as "lipstick on a
   script"?    Why haven't object databases and persistent workspaces
   succeeded over flat-file/scripting style of programming?    This is a
   pessimistic viewpoint - given the decades of experience in scientific
   software development and the skills of the people involved, why do you
   think that a layered system of interfaces will change things?  Who are
   your target users and will that have the patience and desire to figure
   out pygr vs. make something up?    Arguing by analogy with some of the
   arguments for ReST over RPC: documents and state transforms are a
   better fit for loose coupled distributed systems, compared to APIs, so
   are file formats a better fit for working between loosely coupled
   programs? It's easier to debug by looking at the file contents, and to
   develop special purpose tools.    Kevin argued "Program to an
   interface, not an implementation".  Every implementation has an
   interface, so I don't find that a helpful guideline.  YAGNI suggests
   to me you should go ahead and program to the single implementation's
   interface and once you have multiple implementations you need to talk
   to, then figure out how to make a more general interface.


Posted by Ryan Raaum on 2008-09-26 at 10:11. 

::

   Unfortunately, I think that most of the issues I raised with BioPython
   in the discussion on the biology-in-python list that you reference
   apply equally well to pygr.    Please correct me if I am wrong, but
   like BioPython, pygr is an all-in-one, solves-all-your-problems
   "solution stack" as you call it. And while it may conceptually have a
   separation of the data storage, object layer, and scripting layer, it
   seems to me that everything is (beneath the scenes) completely
   interconnected. That is, pygr.Data is not an independent module - it
   has dependencies on the rest of the framework.    So, like BioPython,
   what this means is that you are either drinking the kool-aid or you
   are not. And Andrew already implied this point above when he asked
   "Who are your target users and will that have the patience and desire
   to figure out pygr vs. make something up?" Blantantly putting words in
   his mouth, it appears that his impression of pygr, like mine, is that
   it is all or nothing.

