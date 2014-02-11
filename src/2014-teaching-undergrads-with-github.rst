Using github for homeworks
##########################

:author: C\. Titus Brown
:tags: git,github,teaching,web dev
:date: 2014-2-11
:slug: 2014-teaching-undergrads-with-github
:category: teaching

This term, I'm once again teaching my upper-division CSE undergrad
course in Web Dev here at MSU.  For the second time, I'm requiring students
to use github for their homework; unlike last year, I now understand pull
requests and have integrated them into the process.

How does it work, basically?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The instructions for handing in homework are as follows:

   Merge hw3 into your master.  Please don't delete the 'hw3' branch :)

   Hand in this homework on branch 'hw4' on your github account, and
   set up a pull request between hw4 and your master branch.  Don't merge
   it, just set up the PR.

This sets up a standing pull request for HW 3 that lets me (and other students
-- more on that in a bit) comment on the commit.

When I go to grade homework, I go into a checkout that I keep of each
student's directory; importantly, it's named for their github repo.
Here I can easily do::

   git fetch
   git checkout hw4

and get their HW 4.

Next, I run stuff, fix minor bugs, comment on code, commit changes,
and otherwise interact with their homework.  I can then push my changes
and comments to a branch on my github repo::

   #! /bin/bash
   dir=$(basename $PWD)
   git push git@github.com:ctb/cse491-serverz.git hw4:hw4-$dir-comments

and create a pull request automatically by constructing the right URL::

   #! /bin/bash
   dir=$(basename $PWD)
   open -a "/Applications/Google Chrome.app/" https://github.com/ctb/cse491-serverz/compare/$dir:hw4...ctb:hw4-$dir-comments?expand=1

I typically send a private e-mail with their grade in it at this point, along
with any requests or general comments I have (fix your tests, think about
refactoring, etc.)

Note that leaving the hw3 branch lying around lets me backtrack and check
old code more easily.  Sure, I could do this with 'git log' but it's
nice to have the branch there.

Code sharing policy
~~~~~~~~~~~~~~~~~~~

The github repos are public, which presents a challenge: how do you prevent
cheating?

Well, my general policy in this class has always been that "code
should work; I don't care where you got it."  My experience has been
that some number of students simply fail to even copy code effectively,
and that level of evaluation is sufficient for me.

That having been said, this year I now require that students have their
own names on the commits -- they can't just completely swap in someone
else's commits.  This is antithetical to the whole version control and
credit-where-credit-is-due thing but I found that git made it *too* easy
to copy functioning code.  I'll let you know how this goes.

Grading only a subset of HWs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Grading this stuff is quite a chore; I can do 5-10 HWs in a single
sitting, but ~40-45 is too much.  I don't hand this off to TAs -- I
prefer to look at the code myself, and I also generally find that my
TAs don't know the material that well (they're usually my grad students
but that doesn't mean they're web devs!)

So, this year, inspired by a post on `Tomorrow's Professor
<http://cgi.stanford.edu/~dept-ctl/tomprof/postings.php>`__, I am only
grading 5-10 homeworks a week.  I am choosing them more or less
randomly, and I expect to grade each person's work a few times during
the term.  As the term goes on I will target people who need a bit
more help.  I do take requests, too, so if people want my feedback I'm
sure to look at their code.

So how do I assign grades to the ones I don't grade? The rule is that
if I don't grade your HW, you automatically get 100%.  However, a key
component of this is that you must have handed in something
approximating the homework, and it must have been handed in on time;
if I find a bunch of empty HW branches (and I _will_ notice), the student
will be in trouble.

Thus far I like the way this is working out.  I've been able to do a
much better (less hurried, better comments) job of grading than in
previous years, and of course the students don't mind.  Because the
homework is cumulative, I expect this approach to still effectively
sort the students.

Grading efficiently
~~~~~~~~~~~~~~~~~~~

I use tests (nose) and code coverage (Ned Batchelder's excellent
`coverage module <http://nedbatchelder.com/code/coverage>`__ ) to
target my grading.  If there are uncovered bits of code, that's the
first place to look for bugs.  I also do some exploratory testing (aka
"clicking on things and waiting for stuff to break) and skim the code,
but targeting missing code coverage is an *amazingly* effective way
to find bugs.

Automation
~~~~~~~~~~

I am planning to set up continuous integration on each repo and pull
request, largely as a tool to help the students.  I'll let you know
how that goes.

To find people who may not have handed in HW, I can run a little
shell script, check.sh ::

   #! /bin/bash
   for i in $(cat github-list.txt)
   do
        cd $i
        echo $i $(git branch -r | grep hw4) >> ../out
        cd ../
   done

that lets me see who does not have a hw4 branch.

I'm thinking about writing a little RSS feed examiner to see who has
turned in stuff, too.  Probably redundant at this point.

Enabling code review, and a crazy idea
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I'd really like to get the students into code review, but it's remarkably
hard to take people who are not that experienced at software development and
get them to critique each other's code.  I don't scale particularly well,
and so I can't really help the students learn to do this 1-1.  So... how?

One thing I'm trying out is to have students do code review in class,
on each others' pull requests.  This works ... OK, but there's not really
enough time in class to do it.

What else could we do?

Since I have a range of student expertise in the class, why not get
the more expert students to help out?  It will give the more expert
students some code review experience, and it will help the less expert
students work through problems.

Here's my idea:

1. if a student is having trouble, they can request an extension.

2. as part of the extension, I will assign them a mentor from a
   pool of people who are generally doing well.

3. the mentor will go through their pull request and make comments.

4. the mentee will then be able to work through the problems, potentially
   with back-and-forth with the mentor.

5. the mentee gets an extension and probably a better grade; the mentor
   gets project credit towards their final grade.

This can be gamed, and undoubtedly will; in particular, I expect
people who are perfectly capable of getting it to work but who just
want an extension to ask for one.  But do the benefits significantly
outweigh the loss from gaming?  I'll let you know how I feel about it
:)

Suggestions on modifications welcome, of course.  I'm thinking that
there will be a non-zero chance that I will refuse the extension
request, which should keep people on their toes.  Other thoughts?

What isn't working?
~~~~~~~~~~~~~~~~~~~

The students are still fairly new to git, and I haven't been forcing
them to do tricky stuff with it -- as we know from Software Carpentry,
git is very difficult to learn, so I'm taking it slow.  (This is the
students' first introduction to distributed version control, and I don't
think many of them are really experienced at version control, period;
we don't introduce it at MSU until 3rd year!)

This leads to one big problem -- the pull requests often contain
significant extraneous code, like entire virtualenvs; and sometimes
the PRs aren't useful for other reasons, like someone swapping in a
whole bunch of new code.  But this is still a fairly rare problem.

Concluding thoughts
~~~~~~~~~~~~~~~~~~~

This is all an experiment, but so far I've been impressed with how
well git and github are working. I'd love to hear about other
experiences; drop me a line or comment below.

In previous years, I've gotten feedback that students really find the
testing and continuous integration stuff useful for their next jobs.
This year, I hope to get the same comments about git and github.

--titus
