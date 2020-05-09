Title: How open is too open?
Date: 2018-06-26
Category: science
Tags: sustainability,software,cpr
Slug: 2018-how-open-is-too-open
Authors: C. Titus Brown
Summary: How open is too open?

When I look at open source projects, I divide the people involved into
three categories: the investors, the contributors, and
the users. The contributors do the work on the project, while the
investors (if any) support the contributors in some way. The users are
those who simply use the project without contributing to it.

For example, in sourmash, the investors are (primarily) the Moore
Foundation, because they support most of the people working on the
project via the Moore grant that I have. There are the contributors -
myself, Luiz Irber, and many others in and out of my lab - who have
submitted code, documentation, tutorials, or bug reports. And then
there are the users, who have used the project and not contributed to
it. (Projects can have many investors, many contributors, and many
users, of course.)

I consider anybody who used sourmash and then contacted us - with a
bug report, a question, or a suggestion - as a contributor. They may
have made a *small* contribution, but it is a contribution
nonetheless. I should add that those who cite us or build on us are
contributing back in a reasonably significant way, by
providing a formal indication that they found our code useful. This is
a good signal of utility that is quite helpful when discussing new
investments.

Users are interesting, because they *contribute* nothing to
the project but also *cost us nothing*. If someone downloads sourmash,
installs it, runs it, and gets a result, but for whatever reason never
publishes their use and cites us, then they are a zero-cost user. If
they file a bug report, that’s potentially a small burden on the
project (someone has to pay attention to it), but - especially if they
file a *good* bug report that makes it easy to track down the bug -
then I think they are contributing back to the project, by helping us
meet our long-term goals of less-buggy / more correct code.

Some (rare) contributors are more burden than help. They are the
contributors who discover an interesting project, try it out, find
that it doesn’t quite fit their needs, and then ask the developers
to adjust it for them without putting any effort into it. Or, they ask
many questions via private e-mail, consuming the time and energy of
developers in private without contributing to the public discussion of
the software’s scope and functionality.  Or, they argue passionately
about planned features without putting any other time into the project
themselves. I call these *extractive* contributors.

These extractive contributors are far more of a burden then you might
think.  They consume the effort of the project with no gain to the
project. Sometimes feature requests, questions, and high-energy
discussions lead the project in new, worthwhile directions, but quite
often they’re simply a waste of time and energy for everyone
involved. (We don’t have any such contributors in sourmash,
incidentally, but I’ve seen them in many other projects - the more
well known and useful your project is, the more likely you are to have
people who demand things of the project.) Quote from a friend: “They
don’t contribute much code, but boy do they have strong opinions!"

You could certainly imagine an extractive contributor who implements
some big new feature and then dumps it on the project with a request
to merge (these are often called “code bombs”). If the feature was
discussed beforehand and aligns with the direction of the project,
that’s great!  But sometimes people submit a merge request that simply
won’t get merged - perhaps it’s misaligned with the project’s
roadmap, or it adds a significant maintenance burden. Or, perhaps
the project developers don’t know and trust the submitter enough to
merge their code without a lot of review.  Again, this is not a
problem we’ve had in sourmash, but I know this happens with some
frequency in the bigger Python projects.

You could even imagine a significant regular code contributor being
extractive if they are not contributing to the maintenance of the
code.  If someone is working for a company, for example, and that
company is asking them to implement features X, Y, and Z in a project,
but not giving them time to contribute to the overall project
maintenance and infrastructure as part of the core team, then they may
be extracting more from the project than they are putting in. Again,
on the big projects, I’m told this is a serious problem. To quote a
friend, “sometimes pull requests are more effort than they are worth."

I don’t know what the number or cost of extractive contributors is on
big projects, but at least by legend they are a significant part of
the software sustainability problem. Part of the problem is on the
side of the core maintainers of any project, of course, who don’t
protect their own time - in the open source world, developers are
taught to value all users, and will often bend over backwards to meet
user’s needs. But a larger part of the problem is on the side of the
extractive contributors, who are effectively sapping valuable effort
from the project’s contributors.

I don’t think it’s necessarily easy to identify extractive
contributors, nor do I think it’s straightforward to draw
well-considered boundaries around an open project in which you
indicate exactly which contributions are welcome, and how. And some
extractive contributors can turn into net positive contributors with a
little bit of mentoring and effort; we could think of such an effort
as incurring contributor debt that could be recouped if more "effort" is
brought into the project than is lost, over the long term.

Looking at things through this lens, some features of the Python core
dev group come into sharp focus. Python has a ‘python-ideas’ list
where potentially crackpot ideas can be floated and killed without
much effort if they are misaligned with the project. If an idea passes
some threshold of critical review there, it can potentially move into
a formal suggestion for python implementation via a Python Enhancement
Proposal, which must follow certain formatting and content guidelines
before it can even be considered.  These two mechanisms seem to me to
be progressive gating mechanisms that serve to block extractive users
from sapping effort from the project: before a major change request
will be taken seriously, first the low threshold of a successful
python-ideas discussion has to be met, and then the significant burden
of writing a PEP needs to be undertaken.

A few (many?) years ago, I seem to recall Martin von Löwis offering
to review one externally contributed patch for every ten other patches
reviewed by the submitter. (I can’t find the link, sorry!) This imposes
*work requirements* on would-be contributors that obligate them to
contribute substantively to the project maintenance, before their
pet feature gets implemented.

Projects can also decrease the cost of extractive contributors by
lowering the cost of engagement. For example, the
[“pull request hack”](https://news.ycombinator.com/item?id=5357417)
makes it possible for anyone who has made a small "minimally viable"
contribution to a project to become a committer on the project. While
it probably wouldn't work for big complex projects, on smaller
projects you could imagine it working well, especially for bug fixes
and documentation-centric issues.

Another mechanism of blocking extractive contributors is to gate
contributions on tests: in sourmash and khmer, as in many other open
source projects, we don’t even consider reviewing pull requests until
they pass the continuous integration tests. We do help people who are
having trouble with them, in general, but I almost never ask Luiz to
review my own PRs until they pass tests.  When applied to potential
contributors, this imposes a minimum level of engagement and effort on
the part of that contributor before they consume the time and energy
of the central project.

I suspect there are actually a bunch of techniques that are used in
this way, even if they serve purposes beyond gating contributors (we
also care if our tests pass!). I’d be really interested in hearing
from people if they have encountered strategies that seem to be aimed
at blocking or lowering the cost of extractive contributors.

How does this connect with the title, "How open is too open?" Well,
this question of sustainability and "extractive" contributors seems to
apply to all putatively "open" projects, but techniques aimed at
blocking extractive contributors seem to trading openness for
sustainability. And I’m curious if that’s something we need to pay
attention to when building open communities, and how we should measure and
evaluate the tradeoffs, and what clever social hacks people have for
doing this.

—titus
