## 8.1 Lesson Plan - Projects & Collaboration with Git

### Overview

Today's lesson plan introduces students to the requirements for Project 1, as well as the basics of collaboration with Git.

### Instructor Priorities

* Students will be able to articulate the requirements for Project 1.
* Students will be able to draw and interpret diagrams of Git branching workflows.
* Students will be able to create new branches with Git.
* Students will be able to push local branches to GitHub.

#### Instructor Notes

* Install the appropriate text editor plugin to help visualize Git histories: [Git History](https://github.com/DonJayamanne/gitHistoryVSCode) in VS Code, [Git Time Machine](https://github.com/pidu/git-timemachine) for Sublime Text, and [git-time-machine](https://atom.io/packages/git-time-machine) for Atom.

* Be sure to refer to the [TimeTracker](TimeTracker.xlsx) to remain on time.

* Be sure to slack out the [Git Branching Workflow](http://nvie.com/posts/a-successful-git-branching-model/) before the end of class.

* Be sure to slack out the [Visual Introduction to Git](https://medium.com/@ashk3l/a-visual-introduction-to-git-9fdca5d3b43a).

  * If possible, share the above links both _before_ today's class, and again at the end of it.

### Sample Class Video (Highly Recommended)

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=aa7716b0-36f5-4f5e-9c90-b3bb4648c749)

- - -

### Class Objectives

* Students must be able to articulate the requirements for Project 1.
* Students must be able to draw and interpret diagrams of Git branching workflows.
* Students must be able to create new branches with Git.
* Students must be able to push local branches to GitHub.

- - -

### 1. Instructor Do: Create Groups (0:05)

* Greet the class, and explain that today is the first day of Project Week.

  * Congratulate the class on having made it this far!

* Explain that, over the next two class weeks, students will work in groups to find and analyze a data set of their choosing.

* Point out that this provides students an opportunity to practice both data analysis and collaborative workflows.

* Explain that the first half of today's class will focus on using Git for collaboration, and that students will have the second half to convene with their groups and start thinking about projects.

* Break students into their groups, and give them a few minutes to rearrange their seating before moving on.

### 2. Instructor Do: Intro to Git (0:30)

* **Files:** [Activities/01-Ins_Workflows/README.md](Activities/01-Ins_Workflows/README.md)

* **N.b.**: If teaching with VS Code, consider using the [Git History](https://marketplace.visualstudio.com/items?itemName=donjayamanne.githistory) extension to illustrate this section's concents.

![Visualizing Git histories with the Git History plugin](https://raw.githubusercontent.com/DonJayamanne/gitHistoryVSCode/master/images/gitLogv2.gif)

* Open the [Introduction to Git](Activities/01-Ins_Workflows/README.md) for reference.

  * Have your TAs slack this file out to students, as well.

* As a review, ask a student to explain what Git is.

  * Git is a tool for saving our work as we develop a project.

  * Git keeps track of our work over time.

* Explain that, whenever we get another piece of a project working, we can save the change with Git.

  * This "save" is called a **commit**, and represents a "checkpoint" for our project.

![A commit is a lot like a changelog note](https://cdn-images-1.medium.com/max/1600/1*zj-d8TopjgBml2QVM-672w.jpeg)

* Explain that, if we break something in our code while developing, this system allows us to restore the working code from before.

  * Since Git remembers these “checkpoints,” we can work on several different concerns all at once.

* Present the following scenario. For our project, let's say on transportation, we need to add an analysis of Uber rider data.

  * If we decide to analyze the average age of riders, Git essentially allows us to write this code, and save it with the name: `age analysis`.

  * This code is _different_ from the code we started with, and that it lives separately from it.

  * In this scenario, we have a version of the code, called `master`, which is the "main" version of our code; and a version, called `age_analysis`, which contains updates.

  * `age_analysis` is a branch based on the `master` branch. That is, it adds or modifies code currently in the main branch.

* Explain that each version of the code lives on a different **branch**.

  * A **branch** is essentially a history of changes.

  * In this case, the `age analysis` branch **diverged** from the `master` branch.

* Take a moment to discuss the benefits of having a separate branch for analyzing Uber rider data.

  * It gives our collaborators a chance to review the branch for errors and offer suggestions.

  * After the proposed change has been reviewed, we can update `master` branch to include the changes in `age analysis` by doing a **merge**.

* Explain that **merging** two branches turns them into one.

  * This is how we can work on new features or bugfixes without affecting the main code.

  * When the code in the new branch (`age_analysis`) is merged, it becomes part of the main code (`master`).

  * Collaborators also avoid stepping on each other's toes by working on different branches.

* Finally, take a moment to review Git's "Snapshot model":

> “...Git thinks of its data more like a set of snapshots of a miniature filesystem. Every time you commit, or save the state of your project in Git, it basically takes a picture of what all your files look like at that moment and stores a reference to that snapshot. To be efficient, if files have not changed, Git doesn’t store the file again, just a link to the previous identical file it has already stored. Git thinks about its data more like a stream of snapshots.”

![Git Snapshot Model](https://git-scm.com/book/en/v2/images/snapshots.png)

### 3. Everyone Do: Creating a Project Repo (0:10)

* Explain that we'll next set up a GitHub repository that students can use for their projects.

* Instruct groups to choose _one_ member to follow along with you. This will be the repo that the group shares through projects.

* Go to [GitHub](https://github.com/), and click on the plus button in the top right to create a new repo.

  ![Creating a new repo on GitHub.](Images/03-add-repo.png)

  * Fill out the fields on the new repo page.

  * Students _should_ initialize with a `.gitignore`.

  * Students should choose `Python` in the gitignore dropdown.

  ![New project configuration.](Images/03-new-project.png)

  * This is sufficient to create a repository that everyone can share.

* Instruct students in charge of creating their group's repository to slack the remote URL (i.e., the link to the repo) to their teammates.

  * Team members will `git clone` this link.

* Explain that, by default, only the creator of the repo can push changes.

* Show how to "open up" the repo by adding **collaborators**.

  * Navigate to the repository settings.

  ![Repository settings](Images/03-settings.png)

  * Navigate to the collaborators tab, and enter your password when prompted.

  ![Repository collaborators](Images/03-collaborators.png)

  * From here, students can search for their teammates by username.

  ![Adding collaborators](Images/03-add-collaborator.png)

  * Everyone in each group should now be able to make changes to the shared repo.

* Remind students again that _everyone in the group must clone the new repository_.

  * Make sure that everyone has done this before moving on.
  
### 4. Students Do: Workflows (0:05)

* **Files:** [Activities/02-Stu_Workflows/README.md](Activities/02-Stu_Workflows/README.md)

* In this activity, students will take a few minutes to review the concepts they have learned.

* At the completion of the activity, send students the [solution](Activities/02-Stu_Workflows/Solved/Solved.md).

### 5. Everyone Do: Creating Branches (0:10)

* **Files:** 
  [Activities/03-Ins_Branches/Solved/BranchDemo.md](Activities/03-Ins_Branches/Solved/BranchDemo.md)

* Check for understanding before moving on.

  * Ask a student to explain the notion of branching.

  * Ask another student to provide two benefits of branching.

* Remind students to navigate into the project directory they just cloned from GitHub.

* Open up the [Branch Demo](Activities/03-Ins_Branches/Solved/BranchDemo.md) for reference.

* Step through each uncommented line in the demonstration.

  * Encourage your students to follow along with their own repositories.

* Explain that we first create a new file, and commit it on the `master` branch.

* Explain that we next create and **checkout** a new branch, on which to work on our data analysis.

  * Instruct students following along to add their name as a prefix when they create this branch, e.g.: `<student name>/data_analysis`.

* Explain that we can then commit files on this branch, _without affecting the code on `master`_.

  * To emphasize the point, ask a student to explain the difference between the code on `master` and that on `data_analysis`.

  * Instruct students to add and commit a text file containing their name to their new branch.

* Explain that, after working on the `data_analysis` branch, we can checkout master; update it with our changes to `data_analysis`; and then delete the `data_analysis` branch, if we don't plan to work on it anymore.

  * Point out that deleting branches like this isn't necessary.

* Take a moment to address any questions before moving on.

### 6. Everyone Do: Pushing to GitHub (0:10)

* Point out that, up until now, students' `data_analysis` branches aren't visible to their teammates—there's no way for their group members to see the work they've done.

* Explain that, in order to share work we do on branches, we can **push** code to from our computers to GitHub, after which our teammates can **pull** it from GitHub to their computers.

* Explain that there are two steps to push our local branch to GitHub.

* First, checkout the branch we want to push to GitHub

* Then, run: `git push origin <branch_name>`

  * Instruct the class to run this line to push their local branches to their shared repository.

* Explain that pushes your local branch to GitHub, allowing your teammates to get access to it later.

* After everyone has pushed to GitHub, instruct the class to checkout master, and then:

  * First, run `git pull`

  * Then, run `git checkout <branch_name>`, where `<branch_name>` is the name of one of their teammates' branches.

  * Give students a minute or two to verify that the code they checked out does indeed come from their teammate's branch.

* Point out that this allows us to easily share different versions of our code across workstations, and allows us to easily test those versions on our local computers.

### 7. Instructor Do: Recap Workflow & Share References (0:05)

* **Files:** [Activities/03-Ins_Branches](Activities/03-Ins_Branches/Solved/BranchDemo.md)

* Take a moment to recap the basic steps of the Git Workflow.

* Review the steps laid out in the [Branch Workflow](Activities/03-Ins_Branches/Solved/BranchDemo.md) cheatsheet.

* Slack out this cheatsheet, as well as the [Git Recipes](Supplemental/GitRecipes.md) document, before moving on.

### 8. Instructor Do: Introduce Projects (0:10)

* Point out that students will need a project to work on if they're to be able to practice Git!

* Step through the [Project 1 Slide Show](Slide-Shows/Project1.pptx), and explain the requirements for Project 1.

  * Be sure to slack out the Project's [Technical Requirements](ProjectGuidelines/TechnicalRequirements.md); the [Presentation Requirements](ProjectGuidelines/PresentationRequirements.md); and the [Projects Overview](ProjectGuidelines/README.md) after going through the slides.

* Take a moment to address any remaining student questions before dismissing the class for break.

- - -

### 9. BREAK (0:15)

- - -

### 10. Everyone Do: Project Work (1:20)

* Students should spend the remainder of class working with their groups to develop a project proposal.

* Be sure to walk around and offer advice on project scope; finding data sources; and what kinds of questions would be interesting, and realistic, for students to investigate.

- - -

### LessonPlan & Slideshow Instructor Feedback

* Please click the link which best represents your overall feeling regarding today's class. It will link you to a form which allows you to submit additional (optional) feedback.

* [:heart_eyes: Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.1&lp_useful=great)

* [:grinning: Like](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.1&lp_useful=like)

* [:neutral_face: Neutral](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.1&lp_useful=neutral)

* [:confounded: Dislike](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.1&lp_useful=dislike)

* [:triumph: Not Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.1&lp_useful=not%great)

- - -

### Copyright

Trilogy Education Services © 2018. All Rights Reserved.
