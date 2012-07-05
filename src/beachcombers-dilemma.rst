The Beachcomber's Dilemma
#########################

:author: C\. Titus Brown
:tags: science,k-mers,khmer
:date: 2012-07-05
:slug: beachcombers-dilemma
:category: science

Here's a data analysis question for all you Big Data folk.

A beachcomber is interested in obtaining up to 10 examples of every
type of shell present on a beach.  The shells are individually easy to
find, but some types are really rare and some are really abundant.
The beachcomber has access to a large group of helpers, and wants
to know how to most efficiently divide up the helpers across the beach
to gather the shells most quickly, while minimizing discussion and
communication between the helpers.

Or, more generally, given a data set D containing some unknown number
of item types M with an unknown abundance distribution, how can we
most efficiently recover at least N items of each type from D using Z
workers, in the absence of fast communication between the workers?

There is a fairly easy I/O bound streaming online solution for this, I
think, but I'm interested in knowing if this is isomorphic to an
established algorithms problem.

thanks!

-titus
