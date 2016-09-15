A draft genome for the tule elk
###############################

:author: Ben Sacks, Zach Lounsberry, Jessica Mizzi, C\. Titus Brown, 
:tags: streaming elk
:date: 2016-09-14
:slug: 2016-tule-elk-draft
:category: science

(Please contact us at bnsacks@ucdavis.edu if you are interested in access
to any of this data.  We're still working out how and when to make it
public.)

The tule elk (Cervus elaphus nannodes) is a California-endemic
subspecies that underwent a major genetic bottleneck when its numbers
were reduced to as few as 3 individuals in the 1870s (McCullough 1969;
Meredith et al. 2007).  Since then, the population has grown to an
estimated 4,300 individuals which currently occur in 22 distinct herds
(Hobbs 2014).  Despite their higher numbers today, the historical loss
of genetic diversity combined with the increasing fragmentation of
remaining habitat pose a significant threat to the health and
management of contemporary populations.  As populations become
increasingly fragmented by highways, reservoirs, and other forms of
human development, risks intensify for genetic impacts associated with
inbreeding.  By some estimates, up to 44% of remaining genetic
variation could be lost in small isolated herds in just a few
generations (Williams et al. 2004).  For this reason, the Draft Elk
Conservation and Management Plan and California Wildlife Action Plan
prioritize research aimed at facilitating habitat connectivity, as
well as stemming genetic diversity loss and habitat fragmentation
(Hobbs 2014; CDFW 2015).

....

We obtained 377,980,276 raw reads (i.e., 300 bp sequences from random
points in the genome), containing a total of 113.394 Gbp of sequence,
or approximately 40X coverage of the tule elk genome. More than 98% of
these data passed quality filtering.  The reads (and coverage) were
distributed approximately equally among the 4 elk, resulting in
approximately 10X coverage for each of the 4 elk.

...

The tule elk reads were de novo assembled into 602,862 contiguous
sequences ("contigs") averaging 3,973 bp in length (N50 = 6,885 bp,
maximum contig length = 72,391 bp), for a total genome sequence size
of 2.395 billion bp (Gbp).  All scaffolds and raw reads will be made
publicly available on Genbank or a similar public database pending
publication.  Alignment of all elk reads back to these contigs
revealed 3,571,069 polymorphic sites (0.15% of sites).  Assuming a
similar ratio of heterozygous (in individuals) to polymorphic (among
the 4 elk) sites as we observed in the subsample aligned to the sheep
genome, this would translate to a genome-wide heterozygosity of
approximately 5e-4, which was about 5 times higher than that observed
in the 25% of the genome mapping to the sheep genome.  This magnitude
of heterozygosity is in line with other bottlenecked mammal
populations, including several of the island foxes (Urocyon
littoralis), cheetah (Acinonyx jubatus), Tasmanian devil (Sarcophilus
harrisii), and mountain gorilla (Gorilla beringei beringei; Robinson
et al. 2016 and references therein).  Although these interspecific
comparisons provide a general reference, heterozygosity can vary
substantially according to life-history, as well as demographic
history, and does not necessarily imply a direct relationship to
genetic health.  Therefore, sequencing the closely related Rocky
Mountain (C. elaphus nelsoni) and Roosevelt (C. elaphus roosevelti)
elk in the future is necessary to provide the most meaningful
comparison to the tule elk heterozygosity reported here.

----

Note, assembly method details are `available on github <https://github.com/jessicamizzi/tule-elk>`__.
