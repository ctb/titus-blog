Title: How long does it take to produce scientific software?
Date: 2018-06-10
Category: science
Tags: software, sustainability, ddd
Slug: 2018-how-long-does-it-take-to-produce-scientific-software
Authors: C. Titus Brown
Summary: How long does it take to produce scientific software?

Over here at UC Davis, the Lab for Data Intensive Biology has been on
extended walkabout developing software for, well, doing data intensive
biology.

Over the past two to three years or so, various lab members have been
working on the following *new* pieces of software -

* [dammit](https://dammit.readthedocs.io/en/refactor-1.0/), de novo
  transcriptome annotation pipeline
  [(Camille Scott)](https://twitter.com/camille_codon);

* [kevlar](https://github.com/dib-lab/kevlar), reference free variant
  discovery in large eukaryotic genomes
  [(Daniel Standage)](https://twitter.com/byuhobbes), in collaboration with
  Fereydoun Hormozdiari;

* [sourmash](https://sourmash.readthedocs.io/en/latest/), a
  MinHash-based sequence analysis framework
  ([Luiz Irber](https://twitter.com/luizirber),
  [Phillip Brooks](https://twitter.com/brooksph?lang=en),
  [Taylor Reiter](https://twitter.com/reitertaylor), and several
  others);

* [spacegraphcats](https://github.com/spacegraphcats/spacegraphcats/),
  a compact De Bruijn graph search system (this is a collaboration
  with [Blair Sullivan](https://twitter.com/blairdsullivan?lang=en)
  and her group including Mike O'Brien and
  [Felix Reidl](https://twitter.com/quantumgravitas), as well as
  [Dominik Moritz](https://twitter.com/domoritz?lang=en) of Jeff
  Heer's group);

* boink, a De Bruijn graph processing framework
  [(Camille Scott)](https://twitter.com/camille_codon);

I should say that _all of these_ except for kevlar have been
explicitly supported by my Moore Foundation funding from the
[Data Driven Discovery Initiative](https://www.moore.org/initiative-strategy-detail?initiativeId=data-driven-discovery).

With the possible exception of dammit, every single one of these
pieces of software was developed entirely since the move to UC Davis
(so, since 2015 or later).  And almost all of them are now approaching
some reasonable level of maturity, defined as "yeah, not only does
this work, but it might be something that other people can use."
(Both dammit and sourmash are being used by other people already; kevlar,
spacegraphcats, and boink are being written up now.)

All of these coming together at the same time seems like quite a
coincidence to me, and I would like to make the following proposition:

**It takes a minimum of two to three years for a piece of scientific
software to become mature enough to publicize.**

This fits with my previous experiences with
[khmer](https://github.com/dib-lab/khmer/) and the
FamilyRelations/Cartwheel set of software as well - each took about
two years to get to the point where anyone outside the lab could
use them.

I can think of quite a few reasons why some level of aging could be
necessary -

* often in science one has no real idea of what you're doing at the
  beginning of a project, and that just takes time to figure out;

* code just takes time to get reasonably robust when interfacing with
  real world data;

* there are lots of details that need to be worked out for installation and
  distribution of code, and that also just takes time;
  
but I'm somewhat mystified by the 2-3 year arc.  It could be tied to
the funding timeline (the Moore grant ends in about a year) or career
horizons (the grad students want to graduate, the postdocs want to
move on).

My best guess, tho, is that there is some complex tradeoff
between scope and effort that breaks the overall software development
work into multiple stages - something like,

1. figure out the problem
2. implement a partial solution
3. make an actual solution
4. expand solution cautiously to apply to some other nearby problems.

I'm curious as to whether or not this pattern fits with other people's
experiences!

I do expect these projects to continue maturing as time and
opportunity permits, much like khmer. boink, spacegraphcats, and
sourmash should all result in multiple papers from my lab; kevlar will
probably move with Daniel to his next job, but may be something we
also extend in our lab; etc.  

Another very real question in my mind is: which software do we choose
to maintain and extend? It's clearly dependent on funding, but also on
the existence of interesting problems that the software can still address,
and on who I have in my lab... right now a lot of our planning is pretty
helter skelter, but it would be good to articulate a list of guiding
considerations for when I do see pots of money on the horizon.

Finally: I think this 2-3 year timeline has some interesting
implications for the question of
[whether or not we should require people to release usable software](http://ivory.idyll.org/blog/2015-how-should-we-think-about-research-software.html).
I think it's a major drain on people to expect them to not only come
up with some cool new idea and implement it in software they can use,
but then also make software that is more generally usable.  Both sides
of this take special skills - some people are good at methods &
algorithms development, some people are good at software development,
but very few people are good at both.  And we should value both, but not
require that people be good at both.

--titus
