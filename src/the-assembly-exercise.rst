The Assembly Exercise - teaching de novo assembly to students
#############################################################

:author: C\. Titus Brown
:tags: ngs,assembly
:date: 2012-09-18
:slug: the-assembly-exercise
:category: science

One of my favorite in-class exercises is The Assembly Exercise, in
which I provided "shotgun sequence" from some English text and ask the
students to assemble it.  Normally I provide a printout of about 10-20
pages of reads with range of read lengths, error rates, and
single/paired end sequences, all from the same sample.  My experience
has been that biology students get a much better visceral sense of the
problems of de novo assembly this way than through any amount of
lectures and problem sets.

Until today, I had always used a crappy set of ad hoc scripts to
generate the data.  I've just put these scripts into a CGI-based Web
form, available here:

   http://lyorn.idyll.org/~t/assembly-exercise/index.cgi

and you can get the source code here,

   https://github.com/ged-lab/assembly-exercise

on github.

The scripts let you put in any text & choose your mutation rate, read
length, and desired coverage.  You can also set whether you want
paired ends, along with the insert size you want.

----

So, you want to try this out, eh?

Making this a class exercise
----------------------------

**Setup**

First, go find a paragraph of text, and then find some sentences that
overlap with that paragraph in some way (so you can get some repeat
sequences in there).

Then, generate ~8-15 base reads with a 1-2% error rate to a combined
coverage of about 5.  Depending on what you want to highlight (the
role of error? the frustration of short reads?) you can generate
another set or two with different parameters.

Finally, generate some paired end reads; I recommend a read length of
about 5, together with an insert size of 15-25.

Print all of these out.

**Instructions**

Print out enough copies so that you can divide your class up into
groups of 3-5 and give each group their own set of copies.

Tell the students:

  a.  Here are a bunch of subsequences, sampled with error, from
      some text.

  b.  These are all from the same text, but they may have different
      read lengths and error rates.

  c.  The word,word output (from paired ends) represent the ends of a
      larger fragment from the text.  That is, you have the additional
      information that each pair of words is some specific distance
      apart.

  d.  Please use pen/paper or a computer notepad to figure out what the
      source sentences are.

  e.  No, you may not use Google.

Also ask them to figure out what a generalizable strategy might be,
and how they can verify that the sequences they get at the end are
correct.

**Duration**

I recommend about 45+ minutes of work in the groups, plus 5 minutes intro
and 10-20 minutes of discussion at the end.  It fits well into an 80 minute
class.

**Discussion**

I usually try to touch on the following points.

Data presentation and information:

 * sorting doesn't actually help all that much.

 * knowing what the coverage is can be helpful, since it lets you detect
   repetitive regions that will lead to misassemblies.

 * longer reads are way more helpful than shorter :)

Algorithms:

 * a word-based algorithm, where you group sentences by shared (long) words
   are great, IF you have low error data.  (This is the de Bruijn graph
   approach.)

 * many students use a greedy algorithm, where they try to find the first
   possible extension of a sentence fragment.  This leads to 

 * no student has ever used an alignment based approach -- it's too slow
   for humans!

 * if you did one pass where you corrected all the errors, your life would
   be way better!

Validation:

 * the results should be English (or whatever language you input).  That's
   really a huge advantage.

 * the paired ends are great for validation, if you *didn't* use them in
   the assembly process.

**Follow-up reading**

I highly recommend assigning "Assembly algorithms for next-generation
sequencing data" (JR Miller et al.),
http://www.ncbi.nlm.nih.gov/pubmed/20211242, for follow-up reading.

---

Enjoy!

--titus
