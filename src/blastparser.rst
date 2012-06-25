A new BLAST parser
##################

:author: C\. Titus Brown
:tags: bioinfo,python
:date: 2007-04-30
:slug: blastparser
:category: python


I spent the weekend hacking out a BLAST parsing package with
`pyparsing <http://pyparsing.wikispaces.com/>`__.

BLAST is a really common bioinformatics tool used to search large-ish
sequence databases, and the NCBI BLAST program is probably the single
most heavily used program in bioinformatics by a long shot.
Unfortunately, the NCBI folk have a habit of making tools with
idiosyncratic output formats, and AFAIK the *only* way to obtain all
of the information calculated by BLAST is to parse the
(human-readable) text format.

This text format is not only human-readable (and not very
machine-readable) but it changes fairly regularly, breaking parsers in
packages like BioPython.  Since I'm already using pyparsing in twill,
and I appreciate its very nice syntax, I decided to try writing a
maintainable BLAST parser with pyparsing.  (The other primary goals
were to build a nice Pythonic API and to simplify the use of
introspection.)

It took me a *long* time (all weekend!) to do so, but I've finally got a
nice, simple API and what seems to be a largely functioning parser: ::

   for record in parse_file('blast_output.txt'):
      print '-', record.query_name
      for hit in record.hits:
         print '--', hit.subject_name, hit.subject_length
         for submatch in hit.matches:
            print submatch.expect, submatch.bits

            alignment = submatch.alignment
            print alignment.query_sequence
            print alignment.alignment
            print alignment.subject_sequence

It's not really ready for unsupervised use yet, but if anyone out there
is jonesin' for a BLAST parser and wants to try this one out, please
`let me know <titus@idyll.org>`__ via e-mail and I'll send it your way.
I'd appreciate comments.

--titus


----

**Legacy Comments**


Posted by Andrew Dalke on 2007-05-01 at 04:06. 

::

   I wrote Martel for Biopython for pretty much the same reasons.  That
   was around 2000 or so.  I used Greg Ewing's PLEX syntax as my starter,
   and both have the same style as PyParsing.    I have several
   conclusions from my Martel work.  To start, my interest in data
   validation (being very strict about the output) does not match up with
   the general desire to be mostly right, and skip/ignore outliers.
   Consider this SWISS-PROT record from HAS2_CHICK    """DT  30-MAY-2000
   (REL. 39, Created)""    That "REL" should be "Rel", according to the
   format spec.  Everything else is "Rel", and I wrote my parser to only
   handle "Rel".  When doing my validations I had to weaken the grammar
   to support wild-type records.    For validation, strictness is useful.
   That record was in the wrong format.  But in general use, nearly
   nobody cares.    (Another problem in SWISS-PROT, years ago, had a
   bogus DR line in the comment/CC section.  Again, I had to special case
   that one record.)    Now consider the case of a format family.  For
   example, the SWISS-PROT formats over time.  In that case you only need
   to handle the most recent version of the format, since they do a
   pretty good job of being backwards compatible.    But not always.  The
   BLAST output over time is not backwards compatible with previous
   versions.  The number of spaces, and newlines changes, the layout of
   the output changes, etc.  How then do you write a grammar which
   handles all of those variations?    For example, do you write a single
   grammar for blastn, blastp, tblastx, etc.?  Or do you write different
   grammars for each, hopefully sharing the definitions for the common
   parts.    Martel supported the latter.  I wanted to say "blast_format
   = blastn_format | blastp_format | tblastx_format | ...", and that
   works.  It would work with pyparsing as well.    Now suppose the
   format changes.  Perhaps an older version used a line containing "
   \n" in two different places where the new version uses "\n".
   (Something like this happened in 2.0.14 or so.)    There are two ways
   to handle this.  One is to write an alternation point at the lowest
   level - "this line can either be "  \n" or "\n" (or matches \s+\n).
   Pro: handles both cases.  Another is to write a new format definition
   which supports only the new format.  Pro: better at validation.    The
   first solution ends up allowing other BLAST-like formats to be parsed,
   in this case if the first alternation has "  \n" while the second only
   "\n" - not legal in either format.    The second ends up being hard to
   implement.  I think it's done with a tree grammar: "format Y is format
   X except replace this node in the tree with my new one".    Mmm, this
   comment is getting too lengthy.  I'll summarize what I just wrote as:
   the hard part about using a language grammar for BLAST is supporting
   all of the variations of BLAST and its changes through time.  I don't
   think pyparsing/martel/flex are quite right for this problem.    Jeff
   Chang started to build a collection of BLAST output over time showing
   many different corner cases.  Don't think that every went anywhere.
   Still, you should be able to mine biopython and bioperl test cases for
   variations of BLAST output in formats you might want to handle.
   Depends how far back in time you want to support.  Nice not having
   legacy users :)


Posted by Antonio Cavallo on 2007-05-01 at 04:18. 

::

   This all "parsing" has got me out of the   Bioinformatics field a long
   time ago:  at that time I failed to see any science   in it.


Posted by Titus Brown on 2007-05-01 at 14:02. 

::

   Antonio, yes, it's always nice when you don't have to do the silly
   work in order to do the interesting work.  Still, here we are...
   Andrew, I see your points, and I agree with most of them.  I'm
   focusing on automated tests and maintainability -- or at least I'd
   like to ;) -- and I'm hoping that this will translate into a more
   effective parsing situation.    Down the road I suspect that I will be
   rewriting/refactoring BLAST, but that's a different issue ;)
   --titus


Posted by Paul McGuire on 2007-05-02 at 11:13. 

::

   Some of these vagaries of chance formats are automatically
   accommodated by pyparsing's credo, "whitespace doesn't matter".
   Adding or removing an extra line of whitespace is completely
   transparent to pyparsing's grammar matching logic.  Other changes can
   be anticipated, and coded defensively.  For instance, if a separation
   line of '====' signs might change in length (from 72 to 96 characters,
   say), then specifying this element as Word('=') is more robust than
   Literal('='*72).      Other pyparsing robustness-enhancing techniques
   are to make liberal use of results names, so that later introduction
   of optional fields can be easily inserted into the grammar without
   changing down all references to tokens by index - existing tokens are
   consistently referenced by name.    Lastly, when retrofitting format
   changes for new versions, placeholder Forward's can be inserted into
   the existing grammar, to be modified at parse time if the new version
   is detected - sort of a self-modifying grammar.  A parse action
   attached to the version id field would insert the expression
   definitions for the new version's specialized data into the
   placeholder.    So I'm hoping that this combination of adaptation
   techniques and pyparsing's grammar readability will help Titus to have
   a longer-term success in his BLAST processing.    -- Paul

