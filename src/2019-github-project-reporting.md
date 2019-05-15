Title: Using GitHub for janky project reporting - some code
Date: 2019-05-15
Category: science
Tags: github, commonspilot, data commons
Slug: 2019-github-project-reporting
Authors: C. Titus Brown
Summary: We scripted GitHub for lightweight project reporting

For the [NIH Data Commons](http://ivory.idyll.org/blog/2019-nih-data-commons-update.html), we needed a way for 10 distinct teams to do reporting at the level of about 50-100 milestones per team, on a monthly basis.

Each team was already using different project management software internally, and we didn't want to require them to switch to something new. We also didn't need a lot of innate functionality in the project reporting system - basically, for each milestone we needed two statuses, "started" and "finished".

So we decided to go with something lightweight and simple that would support programmatic update and automated reporting: GitHub!

We chose to use GitHub for project reporting for several reasons. We were already using GitHub for content stuff, and everyone had accounts. We were also using GitHub for authentication control on static Web sites via a Heroku app.

So what we did was use the [PyGithub package](https://pygithub.readthedocs.io/en/latest/index.html) to write a script to take the project milestones (which were all in a spreadsheet) and load them into GitHub issues.  There was a label for "this task has been started", and when complete, the issue was just closed.

Each issue had some metadata associated with it (this was basically regexp-friendly fields like "id: XYZ") that linked it back to information in the spreadsheet. Other metadata such as the team that "owned" the milestone was layered on with GitHub labels.

We then wrote another script that extracted the issue statuses and output a reporting spreadsheet that we could send to the NIH on a monthly basis.

(Luiz Irber wrote the first version of the scripts as a proof of concept, and then I took over expansion and maintenance as our needs evolved.)

Using GitHub in this way had a number of advantages, some of which were unexpected.

* The main advantage was that the user interface for viewing and updating statuses was super easy. Finding issues could be done github search (and eventually via our project search engine, [centillion](http://nih-data-commons.us/centillion/)).  Permalinks could be bookmarked, too.

* Linking between GitHub issues worked nicely: when you put a link from an issue in some other repo to a milestone, a back-link was automatically provided on GitHub.

* The statuses of milestones were accessible to everyone, i.e. visible across the project.

* People from any team could watch a milestone they were interested in.

* Comments and questions could be posted on milestones, and (potentially) could be provided in the monthly rollup.

* The GitHub Web and project interface went through churn during our project, but the issue API was not affected, so our scripts kept on working.

* Unlike built-in GitHub projects functionality, this  works easily across multiple repositories AND multiple organizations.

## What if we had not used GitHub?

Within the project, there was some pushback. Most of the pushback amounted to "but we are already using System X, can't we just use that?" But there was no consensus on what to use! Since it was all scriptable, we were expecting to write some status importers (but didn't need to within the first phase of the project). It would have been easy to auto-update issue labels using GitHub project management bridges (and I think at least one group did that without involving us).

GitHub enabled everyone to see each other's milestone statuses without having to give permissions beyond existing GitHub project memberships. I don't know how we would have done that another way.

Because we used a lightweight informal format with some simple scripts, we could update reporting formats and details quickly. If we'd used a heavierweight and/or closed source system, we might have had to put more time into configuration and/or bug workarounds.

GitHub is pretty scriptable, which came in really handy for wonky status update situations, or custom reports. I'm not sure how scriptable and well documented other issue tracking software is.

## So where's the code?

I've extracted the core code to [github.com/ctb/2019-dcppc-bot](https://github.com/ctb/2019-dcppc-bot), and made a small running example!

There are two scripts, [`update-milestones.py`](https://github.com/ctb/2019-dcppc-bot/blob/master/update-milestones.py) and [`milestones-gh-to-csv.py`](https://github.com/ctb/2019-dcppc-bot/blob/master/milestones-gh-to-csv.py). The first script parsed the big CSV file full of milestones, and updated the GitHub issues from it. The second script exports the GitHub issues and statuses for monthly reporting.

[`create_issue_body_milestone`](https://github.com/ctb/2019-dcppc-bot/blob/master/update-milestones.py#L45) is what created / updated the actual issues.

[`extract_report`](https://github.com/ctb/2019-dcppc-bot/blob/master/milestones-gh-to-csv.py#L125) built the milestone output reports, which were then output in the [`main` function](https://github.com/ctb/2019-dcppc-bot/blob/master/milestones-gh-to-csv.py#L196).

## Running stuff

Create a token by going to GitHub settings, Developer Settings, Personal Access Tokens, Generate New Token.

Copy / paste the string into an environment variable (you'll need to replace the hex string with your own token).
```
export GITHUB_TOKEN='a6161b3288894522b8930b67231d833295e7d5ba'
```

Check that the token works and the repo exists (you'll want to replace `ctb/example-milestones` with a repository you have write access to!)
```
./update-milestones.py update example-milestones.csv  -f -vv -m ctb/example-milestones
```

Actually create the issues now, by parsing the [`example-milestones.csv` file](https://github.com/ctb/2019-dcppc-bot/blob/master/example-milestones.csv)
```
./update-milestones.py update example-milestones.csv  -f -vv -m ctb/example-milestones --change-github
```

This will create and/or update issues, e.g. like [ctb/example-milestones #1](https://github.com/ctb/example-milestones/issues/1).

Now, run a report:

```
./milestones-gh-to-csv.py  -m ctb/example-milestones example-milestones.csv
```

This will generate reports by team, e.g. [`report-team-White.csv`](https://github.com/ctb/2019-dcppc-bot/blob/master/report-team-White.csv) and [`report-team-Brown.csv`](https://github.com/ctb/2019-dcppc-bot/blob/master/report-team-Brown.csv).

You can see the final set of issues [here](https://github.com/ctb/example-milestones/issues?utf8=%E2%9C%93&q=is%3Aissue).

## Was this a good idea?

The project only ran for ~6 months in the end, and I would argue that scripting our own solution was a good investment of time and effort because of the flexibility it gave us. In particular, it let us iterate and converge on an approach that met the needs of the funders without unduly burdening the project managers.

In the long term, we might have tried to identify commercial software that had built-in visualization and exploration functionality. But I wouldn't have wanted to do that on the timeline we had for phase 1.

The code was hideous because it was all done really fast at the last minute before the first reporting period. Changes were done carefully, mostly by me, because I was the one who would suffer the most if we screwed up. If we'd brought our infrastructure engineer in to the project earlier, I probably would have asked him to put the time in to unit testing and so on, but the code was working well enough for us to just leave it be.

The general idea of using GitHub issues to surface milestone statuses across multiple teams and integrate with individual project trackers is pretty nice and open-sourcey.

The existing code ignores issues without metadata. So while we did not do this, you could salt "issues for reporting" into an existing repository full of issues, and extract info from just the reporting issues just fine.

So: in this case a quick hack worked out ok, and I'm not ashamed of it.

And maybe there are now better ways to do all this with GitHub Projects, but there weren't then :)

Last but not least: you should always be wary of writing code so that you can write code. Before you know it, maintaining your project management system could become someone's full time job... #yakshaving

--titus

Thanks to Luiz Irber for starting the project, and Charles Reid, Matthew Turk, and Tracy Teal for comments on a draft of this post!
