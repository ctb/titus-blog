Install gplots in R 2.1X
########################

:author: C\. Titus Brown
:tags: installation sucks
:date: 2013-11-18
:slug: 2013-installing-gplots
:category: science

I've been using EBSeq for a few things lately, and have had trouble getting
some of the dependencies installed -- in particular, gplots doesn't seem
to be readily available for R 2.14, 2.15, etc.  Judging by my Google searches,
others have been having the same problems; see e.g.

   http://stackoverflow.com/questions/16091096/can-not-install-ggplot-package-in-r-2-14-1

The general error message is of the form::

  Warning in install.packages :
     package 'gplots' is not available (for R version 2.14.1)

Since I'm not an R expert, it took me a long time to find a solution;
here's what I cooked up::

   curl -O http://cran.ma.imperial.ac.uk/src/contrib/Archive/gplots/gplots_2.6.0.tar.gz
   tar xzf gplots_2.6.0.tar.gz

   cat <<EOF > /tmp/inst.sh

   options(repos=structure(c(CRAN="http://cran.ma.imperial.ac.uk")))

   install.packages("gtools")
   install.packages("gdata")
   install.packages("gplots", repos = NULL, type="source")
   EOF

   Rscript /tmp/inst.sh

Hope this saves someone some time!  Comments and updates welcome -- I'm
sure this isn't the best way to do it.

--titus

p.s. I hate R.

p.p.s. Although to be fair this kind of problem crops up everywhere in
any useful programming language, because SOFTWARE SUCKS.
