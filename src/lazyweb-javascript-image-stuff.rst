Dear Lazyweb: JavaScript "imagemaps" and/or image subselection?
###############################################################

:author: C\. Titus Brown
:tags: python,bioinformatics
:date: 2008-05-07
:slug: lazyweb-javascript-image-stuff
:category: science


Dear Lazyweb, help!

I'm embarking on a number of summer projects in my `new lab at MSU
<http://ged.cse.msu.edu/>`__, and several of them focus on using `pygr
<http://code.google.com/p/pygr>`__ to do cool genomic stuff.  In
particular, I'm planning to build a personal genome annotation system
that will let people run their own full genome Web sites and annotate
the genomes with private information such as Solexa data, cDNA/EST
projects, ChIP-seq, cis-regulatory reporter constructs, ncRNA
predictions, etc. etc.  (If you're interested in this sort of thing,
`get in touch <mailto:ctb@msu.edu>`__ -- it will, of course, be open
source and open development, albeit in Python :)

As I've been thinking more about how to do the display side of things,
I've been running headfirst into a serious lack of knowledge.  I would
like to make an interface that looks somewhat like your standard
genome browser/GMOD/UCSC interface, such as `this UCSC view of the
chicken genome
<http://genome.ucsc.edu/cgi-bin/hgTracks?hgsid=107080583&clade=vertebrate&org=Chicken&db=galGal3&position=chr8%3A28%2C563%2C111-28%2C563%2C687&pix=620&Submit=submit&hgsid=107080583>`__.
I already have the basics of that view working; for example, see this
`simple example
<http://iorich.caltech.edu/~t/transfer/pygr-draw/doc/simple-example.html>`__
and `a group-feature example
<http://iorich.caltech.edu/~t/transfer/pygr-draw/doc/group-example.html>`__.
But I'd like to add more - a LOT more -- interactivity.

Ideally I'd like to be able to draw simple objects (squares, rectangles,
lines) on some sort of canvas and then use JavaScript and AJAX to pop
up windows and display bits of information.  But I don't really know this
space of functionality very well.

So I'm turning to the lazyweb.

Are JavaScript+image maps the right way to go (for example, `this
<http://www.sbrady.com/hotsource/javascript/mapdis.html>`__, `this
<http://www.w3schools.com/js/js_image_maps.asp>`__, and `this
<http://www.webmonkey.com/webmonkey/98/29/index3a_page2.html?tw=programming>`__)?
Do they work well with multiple browsers?  Or are there good JS
libraries for *drawing* images on the fly in the browser?  Is SVG a
good thing to look at?  Were you stuck with this task, what would you use?

The most important things for this project are, in order of importance:

 - basic functionality (JS image maps seem fine for this)

 - cross-browser functionality

 - selection (e.g. `GMOD RubberBandSelection <http://www.gmod.org/wiki/index.php/RubberBandSelection>`__)

 - flexibility: reordering and redrawing of images.  

Your thoughts are much appreciated!  Please `drop me a line <mailto:ctb@msu.edu>`__ or comment, whichever is most convenient.  I'll summarize the options.

thanks,

--titus

p.s. I'm perfectly fine with "Google this, dumby!"  I just don't have much
in the way of google keyword knowledge in this area...


----

**Legacy Comments**


Posted by Theran on 2008-05-07 at 20:55. 

::

   Image maps work on all modern browsers. You can calculate the regions
   on the server side at the same time you generate the image. Doing it
   on the server means you can use Python instead of JS. This method does
   not allow click-and-drag creation of windows etc.    For click-and-
   drag windows, I would use the YUI image cropper JS widget: <a href="ht
   tp://developer.yahoo.com/yui/imagecropper/">http://developer.yahoo.com
   /yui/imagecropper/</a>  and avoid having to reinvent the wheel.    I
   would steer clear of SVG for now. It's here, it's standard, but it's
   not broadly well implemented.     The &lt;canvas&gt; element works
   well for drawing with JS, but it is not quite standard and does not
   work on IE IIRC.


Posted by Mike Pirnat on 2008-05-07 at 21:29. 

::

   I've not monkeyed with it personally, but Dojo has <a
   href="http://dojotoolkit.org/book/dojo-book-0-9/part-3-programmatic-
   dijit-and-dojo/drawing-gfx">a graphics library</a> that might be
   decent for drawing on the fly in the browser.  I like a lot of the
   other bits of Dojo, so... maybe worth a look?


Posted by Clint on 2008-05-07 at 21:56. 

::

   Hi Titus.    I haven't tried this specific plugin, but I'm a big
   JQuery fan.    <a href="http://plugins.jquery.com/project/Draw">http:/
   /plugins.jquery.com/project/Draw</a>    -Clint


Posted by Noah Gift on 2008-05-07 at 23:39. 

::

   I second the JQuery idea.  This is my current favorite javascript
   library, and I find it sucks less than many.


Posted by Sean Gillies on 2008-05-08 at 12:53. 

::

   You can do cool stuff with OpenLayers. For example: <a
   href="http://hackmap.blogspot.com/2008/04/comparative-genomics-with-
   openlayers.html">http://hackmap.blogspot.com/2008/04/comparative-
   genomics-with-openlayers.html</a>


Posted by Dean Landolt on 2008-05-08 at 13:09. 

::

   Thirded...but isn't that MochiKit's tagline ("sucks less")?    Image
   maps are almost as old as HTML, so I'd imagine their cross browser
   support is solid. I've never stressed them as hard as you're
   suggesting, but they see a ton of use in sites like Facebook.    Even
   if you do choose to go down this route, resist the temptation to roll
   your own image map library. Lean on the idioms of a library plugin
   that addresses your problems (http://drupal.org/project/jq_maphilight
   perhaps?)


Posted by brentp on 2008-05-08 at 17:15. 

::

   good to hear there'll be work on pygr.    as Sean says, dont look past
   openlayers.   i have a modest addition which restricts the scrolling
   to horizontal:  <a href="http://128.32.8.100/genome-
   browser/">http://128.32.8.100/genome-browser/</a>  and a Genomic.js
   Layer.   it's pretty easy to use with any cgi script as it sends a
   request like:  ?chr=7&amp;layers=gene,CDS&amp;version=6&amp;start=5070
   56&amp;stop=539824&amp;width=512    and by making use of openlayers,
   you tap into a very well tested, well supported system with a good
   developer community, and you get lots of cool stuff for free:  <a href
   ="http://openlayers.org/dev/examples/">http://openlayers.org/dev/examp
   les/</a>


Posted by Doug Napoleone on 2008-05-09 at 19:42. 

::

   Just released, just in time for this question:    <a href="http://ejoh
   n.org/blog/processingjs/">http://ejohn.org/blog/processingjs/</a>
   check it out...

