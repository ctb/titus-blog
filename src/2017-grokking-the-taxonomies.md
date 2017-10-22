Title: Grokking "custom" taxonomies.
Date: 2017-10-22
Category: science
Tags: bioinformatics, tara, minhash, ngs, metagenomics, taxonomy, smb
Slug: 2017-grokking-the-taxonomies
Authors: C. Titus Brown
Summary: Sometimes things disagree with NCBI. What then?

(Some more Saturday/Sunday Morning Bioinformatics...)

A while back I
[posted some hacky code](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-part-2.html)
to classify genome bins using a custom reference database.  Much to my delight,
Sarah Stevens (a grad student in Trina McMahon's lab) actually tried using it!
And of course it didn't do what she wanted.

The problem is that all of my least-common-ancestor scripts rely
utterly and completely on the taxonomic IDs from NCBI, but anyone who
wants to do classification of new genome bins against their own old
genome bins doesn't have NCBI taxonomic IDs.  (This should have been
obvious to me but I was avoiding thinking about it, because I have a
whole nice pile of Python code that has to change. Ugh.)

So basically my code ends up doing a classification with custom genomes
that is only useful so far as the custom genomes match NCBI's taxonomy.
NOT SO USEFUL.

I'd already noticed that my code for getting taxonomic IDs from the
Tara binned genomes barfed on lots of assignments (see script links after
"used the posted lineages to assign NCBI taxonomic IDs" in
[this blog post](http://ivory.idyll.org/blog/2017-taxonomy-of-tara-ocean-genomes.html)).  This was because the Tully and Delmont genome bins
contained a lot of novel species.  But I didn't know what to do about that
so I punted.

Unfortunately I can punt no more.  So I'm working on fixing that, somehow.
Today's blog post is about the fallout from some initial work.

----

## Statement of Problem, revisited

We want to classify NEW genome bins using Genbank as well as a custom
collection of OLD genome bins that contains both NCBI taxonomy (where
available) *and* custom taxonomic elements.

## My trial solution

The approach I took was to build custom extensions to the NCBI taxonomy
by rooting the custom taxonomies to NCBI taxids.

Basically, given a custom spreadsheet
[like this](https://github.com/ctb/2017-sourmash-lca/blob/master/tara-delmont-SuppTable3.csv)
that contains unique identifiers and a taxonomic lineage, I walk
through each row, and for each row, find the least common ancestor
that shares a name and rank with NCBI.  Then the taxonomy for each row
consists of triples `(rank, name, taxid)` where the taxid below the
least common ancestor is set to None.

This yields assignments like this, one for each row.
```
[('superkingdom', 'Bacteria', 2),
 ('phylum', 'Proteobacteria', 1224),
 ('class', 'Alphaproteobacteria', 28211),
 ('order', 'unclassifiedAlphaproteobacteria', None),
 ('family', 'SAR116cluster', None)]
```

So far so good!

You can see the code [here](https://github.com/ctb/2017-sourmash-lca/blob/e3bda24a3d7131776d0eb1c75b43081bcecd74d2/parse-free-tax.py) if you are interested.

## Problems and challenges with my trial solution

So I ran this on the Delmont and Tully spreadsheets, and by and large
I could compute NCBI-rooted custom taxonomies for most of the rows.
(You can try it for yourself if you like;
[install stuff](http://ivory.idyll.org/blog/2017-classify-genome-bins-with-custom-db-part-2.html),
then run

```
python parse-free-tax.py db/genbank/{names,nodes}.dmp.gz tara-delmont-SuppTable3.csv > tara-delmont-ncbi-disagree.txt
python parse-free-tax.py db/genbank/{names,nodes}.dmp.gz tara-tully-Table4.csv > tara-tully-ncbi-disagree.txt
```
in the `2017-sourmash-lca` directory.)

But! There were a few places where there were apparent disagreements
between what was in NCBI and what was in the spreadsheeet.

Other than typos and parsing errors, these disagreements came in two
flavors.

First, there were things that looked like minor alterations in
spelling - e.g., below, the custom taxonomy file had "Flavobacteria",
while NCBI spells it "Flavobacteriia".

```
confusing lineage #15
    CSV:  Bacteria, Bacteroidetes, Flavobacteria, Flavobacteriales, Flavobacteriaceae, Xanthomarina
    NCBI: Bacteria, Bacteroidetes, Flavobacteriia, Flavobacteriales, Flavobacteriaceae, Xanthomarina
(2 rows in spreadsheet)
```

Second, there were just plain ol' disagreements, e.g. below the custom
taxonomy file says that genus "Haliea" belongs under order
"Alteromonadales_3" while NCBI claims that it belongs under order
"Cellvibrionales".  This could be a situation where the researchers
reused the genus name "Haliea" under a new order, OR (and I think this
is more likely) perhaps the researchers are correcting the NCBI
taxonomy.

```
confusing lineage #12
    CSV:  Bacteria, Proteobacteria, Gammaproteobacteria, Alteromonadales_3, Alteromonadaceae, Haliea
    NCBI: Bacteria, Proteobacteria, Gammaproteobacteria, Cellvibrionales, Halieaceae, Haliea
(2 rows in spreadsheet)
```

See [tara-tully-ncbi-disagree.txt](https://github.com/ctb/2017-sourmash-lca/blob/e3bda24a3d7131776d0eb1c75b43081bcecd74d2/tara-tully-ncbi-disagree.txt) and [tara-delmont-ncbi-disagree.txt](https://github.com/ctb/2017-sourmash-lca/blob/e3bda24a3d7131776d0eb1c75b43081bcecd74d2/tara-delmont-ncbi-disagree.txt) for the full list.

## I have no conclusion.

I'm not sure what to do at this point.  For now, I'll plan to override
the NCBI taxonomy with the researcher-specific taxonomy, but these
disagreements seems like useful diagnostic output.  It would be
interesting to know what the root cause of this is, though; do these
names come from using
[CheckM to assign taxonomy, as in Delmont et al's workflow?](http://merenlab.org/data/2017_Delmont_et_al_HBDs/#taxonomical-inference-of-the-redundant-mags-using-checkm)
And if so, can I resolve a lot of this by just using that taxonomy? :)
Inquiring minds must know!!

Regardless, I'm enthusiastic about the bit where my internal error
checking in the script catches these issues.  (And hopefully I'll
never have to write *that* code again. It's very unpleasant.)

Onwards! Upwards!

--titus
