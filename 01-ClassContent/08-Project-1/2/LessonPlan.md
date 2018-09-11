## 8.2 Lesson Plan - Pulling and Merging with Git

### Overview

Today, students will study **pulling from GitHub**; **merging branches with Git**; and **distributed PR workflows**.

### Instructor Priorities

* Install the appropriate text editor plugin to help visualize Git histories: [Git History](https://github.com/DonJayamanne/gitHistoryVSCode) in VS Code, [Git Time Machine](https://github.com/pidu/git-timemachine) for Sublime Text, and [git-time-machine](https://atom.io/packages/git-time-machine) for Atom.

* Students must be able to **pull a branch from GitHub**.

* Students must be able to **merge branches with Git**.

* Students must be able to **open, review, and merge PRs with GitHub**.

#### Instructor Notes

* Students should have most of today to work on projects, and the Git activities require group work.

  * To that end, you will slack out today's activities for groups to work through on their own time, for at most the first half of class.

  * You should, however, reserve some time at the beginning of class to both **demonstrate pull.sh** from [01-Ins_Pull/pull.sh](Activities/01-Ins_Pull/Solved/pull.sh); and **how to merge branches with Git**.

* Have your TAs refer to the [TimeTracker](TimeTracker.xlsx) to stay on track.

### Sample Class Video (Highly Recommended)

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e5096f79-710a-427b-accd-a8630029451d)

- - -

### Class Objectives

* Students will be able to **pull a branch from GitHub**.

* Students will be able to **merge branches with Git**.

* Students will be able to **open, review, and merge PRs with GitHub**.

- - -

### 1. Instructor Do: Git and GitHub (01:20)

* **Files**

  * [README.md](Activities/02-Stu_Pull/README.md)—`pull` activity

  * [README.md](Activities/03-Evr_Merge/README.md)—`merge` activity

  * [README.md](Activities/04-Evr_Pull_Requests/README.md)—PR Workflow activity

#### Instructions

* Welcome the class, and let remind them that today will mostly be dedicated to projects.

* However, explain that:

  * You'll take a few minute from the beginning of class to **demonstrate some new (and crucial!) Git commands**

  * Groups will have a series of collaborative Git assignments to work on through the first half of class.

  * Explain that groups should work on the activities until lunch _at latest_, and spend the rest of class working on projects.

* Get started by asking a student to explain what a **branch** is.

  * Explain that a **branch** is a timeline: Its it's own independent Git history of work.

* Ask a student if the files on `master` and `other_branch` are the same, after branching onto and committing to `other_branch`.

* Explain that the end result of **merging** branches is a _single_ branch with all the changes that have been made on either of the branches that you merged.

* Ask a student to explain how they might get changes made on `other_branch` into `master`.

* Explain that the end result is a _single branch_ with _every change_`made to either`other_branch`or`master\`.

* Briefly explain one way such a merge can proceed.

  * Explain that we can compare every pair  of file's timelines between the two branches, and keep the one with the most recent updates.

* Take a moment to demonstrate this via a text file.

  * Create a new Git repo, and add a simple text file on `master`. Make a series of changes and commits.

  * Checkout a new branch, and change the text file on that branch. Make a different series of changes and commits.

  * Switch back to `master`, and use `git log` to demonstrate the commit history.

  * Then, switch to your development branch, and use `git log` to demonstrate the commit history.

  * Use the appropriate text editor plugin to visualize the differences between the branches: [Git History](https://github.com/DonJayamanne/gitHistoryVSCode) in VS Code, [Git Time Machine](https://github.com/pidu/git-timemachine) for Sublime Text, and [git-time-machine](https://atom.io/packages/git-time-machine) for Atom.

  * Point out that, along the way, we would have to make sure that multiple had never tried to change the same thing all at once.

  * Explain that, if they had, Git will ask which version "wins"—we'll practice **resolving conflicts** in the next session.

  * Otherwise, we can simply **fast-forward** the target branch by updating its history with all of the changes made to the files in _either_ branch.

@TODO ANIMATION

* Open up [pull.sh](Activities/01-Ins_Pull/Solved/pull.sh), and talk through the `Git` commands it contains.

  * Explain that, to pull from GitHub to a branch that we're on, we checkout the branch and write: `git pull origin <branch name>`.

  * Explain that if you run: `git pull origin master` _while on_ `other_branch`, you will **merge the most recent version of** `master` **on GitHub into** `other_branch`.

* Slack out the instructions for each of the activities.

* Slack out the [Pull Workflow](Supplemental/PullWorkflow.md) and [Pull Request Workflow](Supplemental/PullRequestWorkflow.md) documents.

* Dismiss class to work on the GitHub activities.

  * Be sure to check-in with each group throughout the activity period to trouble shoot and/or offer conceptual input.

- - -

### 2. BREAK (0:15)

- - -

### 3. Everyone Do: Continue Project Work (01:25)

* Groups should work on projects for the remainder of class.

- - -

### LessonPlan & Slideshow Instructor Feedback

* Please click the link which best represents your overall feeling regarding today's class. It will link you to a form which allows you to submit additional (optional) feedback.

* [:heart_eyes: Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.2&lp_useful=great)

* [:grinning: Like](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.2&lp_useful=like)

* [:neutral_face: Neutral](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.2&lp_useful=neutral)

* [:confounded: Dislike](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.2&lp_useful=dislike)

* [:triumph: Not Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.2&lp_useful=not%great)

- - -

### Copyright

Coding Boot Camp © 2017. All Rights Reserved.
