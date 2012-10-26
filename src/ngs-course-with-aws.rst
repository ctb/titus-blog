Running a next-gen sequence analysis course using Amazon Web Services
#####################################################################

:author: C\. Titus Brown
:tags: bioinformatics,ngs-course,teaching,python
:date: 2010-06-08
:slug: ngs-course-with-aws
:category: python


So, I've been teaching a `course
<http://bioinformatics.msu.edu/ngs-summer-course-2010>`__ on
next-generation sequence analysis for the last week, and one of the
issues I had to deal with before I proposed the course was how to deal
with the **volume of data** and the required computation.

You see, next-generation sequence analysis involves analyzing not just
entire genomes (which are, after all, only 3gb or so in size) but data
sets that are 100x or 1000x as big!  We want to not just map these
data sets (which is CPU-intensive), but also perform memory-intensive
steps like assembly.  If you have a class with 20+ students in it, you
need to worry about a lot of things:

 - computational power: how do you provide 24 "good" workstations

 - memory

 - disk space

 - bandwidth

 - "take home" ability

One strategy would be to simply provide some Linux or Mac
workstations, with cut-down data sets.  But then you wouldn't be
teaching reality -- you'd be teaching a cut-down version of reality.
This would make the course particularly irrelevant given that one of
the extra-fun things about next-gen sequence analysis is how hard it
is to deal with the volume of data.  You also have to worry that the
course would be made even *more* irrelevant because the students would
leave the course and be unable to use the information without finding
infrastructure and installing a bunch of software and then administering
the machine.

While I enjoy setting up computers and installing software and
managing users, I'm clearly masochistic.  It's also *entirely besides
the point* for bioinformaticians and biologists - they just want to
analyze data!

The solution I came up with was to use Amazon Web Services and rent
some EC2 machines.  There's a large variety of hardware configurations
available (see `instance types
<http://aws.amazon.com/ec2/#instance>`__) and they're not that
expensive per hour (see `pricing
<http://aws.amazon.com/ec2/#pricing>`__).  

**This has worked out really, really well.** 

It's hard to enumerate the benefits, because there have been so many
of them ;).  A few of the obvious ones --

We've been able to write tutorials (temporary home here:
http://ged.msu.edu/angus/) that make use of specific images and should
be as future-proof as they can be.  We've given students cut and paste
command lines that Just Work, and that they can tweak and modify as
they want.  If it borks, they always just throw it away and start from
a clean install.

It's dirt cheap.  We spent less than \\$50 the first week, for ~30
people using an average of 8 hours of CPU time.  The second week will
increase to an average of 8 hours of CPU time a day, and for larger
instances -- so probably about \\$300 total, or maybe even \\$500 -- but
that's ridiculously cheap, frankly, when you consider that there are
no hardware issues or OS re-install problems to deal with!

Students can choose whatever machine specs they need in order to do
their analysis.  More memory?  Easy.  Faster CPU needed?  No problem.

All of the data analysis takes place off-site.  As long as we can provide
the data sets somewhere else (I've been using S3, of course) the students
don't need to transfer multi-gigabyte files around.

The students can go home, rent EC2 machines, and do their own analyses
-- without their labs buying any required infrastructure.

Home institution computer admins can use the EC2 tutorials as
documentation to figure out what needs to be installed (and
potentially, maintained) in order for their researchers to do next-gen
sequence analysis.

The documentation should even serve as a general set of tutorials,
once I go through and remove the dependence on private data sets!
There won't be any need for students to do difficult or tricky configurations
on their home machines in order to make use of the tutorial info.

So, truly awesome.  I'm going to be using it for all my courses from now
on, I think.

There have been only two minor hitches.

First, I'm using Consolidated Billing to pay for all of the students'
computer use during the class, and Amazon has some rules in place to
prevent abuse of this.  They're limiting me to 20 consolidated billing
accounts per AWS account, which means that I've needed to get a second
AWS account in order to add all 30 students, TAs, and visiting
instructors.  I wouldn't even mention it as a serious issue but for
the fact that *they don't document it anywhere*, so I ran into this on
the first day of class and then had to wait for them to get back to me
to explain what was going on and how to work around it.  Grr.

Second, we had some trouble starting up enough Large instances
simultaneously on the day we were doing assembly.  Not sure what that
was about.

Anyway, so I give a strong +1 on Amazon EC2 for large-ish style data
analysis.  Good stuff.

cheers,
--titus



----

**Legacy Comments**


Posted by Tracy on 2010-07-07 at 12:40. 

::

   Following Titus' success, I used the Amazon EC2 to run a web
   application for a Microbial Metagenomics course.  Having 16 people use
   the web tool on our one server at the same time would have made it
   slow for everyone.  EC2 solved this problem.  I ran 4 servers and it
   was cheap and speedy.      Since I was using a web tool, I wanted
   people to access it through a web interface.  So, to add to Titus'
   notes, I only had the standard Linux issue of enabling cgi-scripts.
   To address this there were just a few steps.    I used a Debian server
   (ami-ed16f984), so these are specific to Debian and things that are
   the same if you're setting up any Debian server.    When I started up
   the server at Amazon, I added a rule to allow http in the security
   settings.    Once the server was started, and I logged in, I installed
   apache  'apt-get -y install apache2'    Then added the ability to do
   cgi, by adding a 'cgi' file to /etc/apache2/conf.d/ that has the line
   "AddHandler cgi-script .cgi"    In the /etc/apache2/sites-
   available/default file, I took out the "AllowOverride None" statements
   in the /var/www directories section    Then to the
   /etc/apache2/apache2.conf file added  "  &lt;Directory "/"&gt;
   AllowOverride All  &lt;/Directory&gt;  "      I added a .htaccess file
   to /var/www with    Options +ExecCGI  AddHandler cgi-script .cgi
   and restarted apache with 'apache2ctl restart'    Then I tested to see
   if cgi was working by creating a test script hello.cgi    "  #!
   /usr/bin/python  print 'Content-type: text/html\n\nhello, world'  "
   and putting it in /var/www    Then I went to
   'http://amazon_server_ip_address/hello.cgi" to see if it was working
   A new web server, ready to go!

