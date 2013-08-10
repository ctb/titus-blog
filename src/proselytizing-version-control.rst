"Are you doing science as well as you could be?"
################################################

:author: C\. Titus Brown
:tags: software carpentry,git,proselytizing
:date: 2012-10-11
:slug: proselytizing-version-control
:category: science

Since I `attended the entire STAMPS course at MBL this year
<2013-summer-vacation.html>`__, which was an entirely computational
course, I had the opportunity to proselytize computational
reproducibility and good practice to a number of people.

Now, with students I'm usually fairly gentle about this kind of thing,
and try to get my point of view across with education and logic and
examples.  But with faculty, sometimes I'm less gentle :).

When I encounter someone who is entirely computational and does a
significant amount of scripting, I occasionally (depending on mood)
will say something like, "if you're not using version control,
you're not doing science."

Now, you can argue about whether or not this is persuasive (hint: it's
not), or warranted (*shrug* probably in many cases -- the state of
reproducibility in computational science is demonstrably parlous,
although it's pretty clear that version control alone is not going to save
us) but after getting pushback from a fellow course instructor, I'm
thinking it may actually just be wrong.

In this case, Sue Huse took me to task in two ways for this statement.
First, she told me I was being obnoxious and unpersuasive; and second,
she told me about her approach to reproducibility and file tracking,
which doesn't involve version control, and does involve Excel.  And,
you know? It sounds pretty good.  I betcha Sue can pull up any script
and data set you want for any graph in any of her published papers, at
least as fast and perhaps faster than I can for any of mine.  (I'm working
on the obnoxiousness; it's a long haul.)

Don't get me wrong -- there are `plenty of reasons for scientists to
use version control systems
<http://blogs.biomedcentral.com/bmcblog/2013/02/28/version-control-for-scientific-research/>`__
-- Karthik Ram outlines them well in `his paper
<http://blogs.biomedcentral.com/bmcblog/2013/02/28/version-control-for-scientific-research/>`__.
But do you need to use VCS for your scripts in order to be doing
science?

The clear answer is "no".  I think it can help, and it's certainly going
to be more efficient once you get over the learning hump, but it's
probably not necessary.

Which brings me to this conclusion: if I'm going to be an obnoxious
jerk about things like version control, I should probably be saying
something like, "you could be doing computational science better than
you are currently -- more efficiently, more reproducibly, and more
easily."

Or, to put it another way: sure, you don't need to use version control
to write single-person software, or perhaps not even multi-person
software.  It just makes it easier: more robust, more trackable,
easier to bisect to find where bugs were introduced, etc.  And easy to
make public.  But while you don't *need* to, you *should*, both because
it's a good minimum standard, and because odds are that it *will* help
in your research (efficiency, reproducibility, and ease!)

So I think we should perhaps be phrasing our proselytizing as "are you
doing things as well as you could be, and, if not, can we spend a few
minutes showing you some simple ways to improve?" rather than phrasing
things as absolutes when we don't have to.  Software Carpentry is already
doing this, albeit with an emphasis on efficiency, and it seems that
"do science better" gets you more traction than "do better science."

Yeah, I know, it's obvious to all of you.  Just thought I'd share.  Thanks, Sue!

--titus
