## 18.1: R We There Yet

### Overview

Today's class will be a relatively short, but an impactful introduction to R. Despite some substantial differences, it shares many similarities with Python. By the end of the lesson, students will be able to leverage their knowledge of Python and pandas into revisiting data analysis tasks they performed in the fourth week, this time in R.

##### Instructor Notes

* There is a fair amount of overlap between R and Python. Be sure to highlight the similarities as you go through the lesson. This will help students acclimate to the superficial syntactical differences.

* Navigating the file and directory structure in RStudio is a potential logistical hangup for some students. If students appear to be confused on this topic, feel free to emphasize the graphical interface over the command line. The TAs should be ready to help students.

- - -

### Class Objectives

* Students will learn the basics of R syntax.

* Students will learn the fundamental R data types.

* Students will gain familiarity with RStudio.

* Students will learn how to create tibbles.

* Students will be able to manipulate data in tibbles.

* Students will be able to compare and contrast the features of Python and R.

### 01. Instructor Do: Introduction to R (0:05)

* R is a language used for data analysis, statistics, and machine learning, more popular in academia than Python.

* Whether Python or R is better than the other is debatable. However, R offers compelling features, including piping and ease of plotting. Other benefits of R include speed, specialized statistical packages, as well as great visualization libraries.

### 02. Students Do: Install RStudio (0:10)

* **File:** [prework.R](Activities/00_Stu_Installation/Solved/prework.R)

* RStudio is an Integrated Development Environment, which includes all the tools required to program in R.

* In this activity, students will install RStudio, and install several packages.

* Students will go to <https://www.rstudio.com/products/rstudio/download/#download> to download and install RStudio.

* Next, they will install the packages that will be used for this week's activities. Slack out the `prework.R` file, which students can open by double-clicking on it.

* Once the file is open within studio, students will install the listed packages. There are several ways to run the installation commands in a batch. One is to highlight all the lines in the text editor pane and click on the `Run` button. Another is to press `Ctrl+Shift+Enter` (`Cmd+Shift+Enter` on Macs).

  ![Images/RStudio1.png](Images/RStudio1.png)

* If students should run into error messages with any of the packages, they can type `install.packages(<"package-name">)` in the Console. For example, if an error message with the `tidyverse` package is returned, we would type `install.packages("tidyverse")` in the console.

* Send out this link to R keyboard shortcuts: <https://support.rstudio.com/hc/en-us/articles/200711853-Keyboard-Shortcuts>.

### 03. Instructor Do: Basics of R Syntax (0:10)

* **Directory:** [Activities/01_Ins_RBasics](Activities/01_Ins_RBasics/Solved)

* Walk through the code with the class. Much of the basic syntax bears resemblance to those we have seen in Python and JavaScript. Little of what is covered today should be completely unfamiliar.

* Consult [Activities/01_Ins_RBasics/01_Ins_R_Basics.nb.html](Activities/01_Ins_RBasics/Solved/01_Ins_R_Basics.nb.html) for the complete code, but here is a more complete explanation.

* In R, like Python, we can assign values to variables without specifying the data type. Unlike Python, however, the left-pointing arrow `<-` is used to accomplish this task, in which the value on the right is assigned to the variable on the left. Semantically, it is probably more accurate than the equality symbol. The equality symbol can be used, and is used in certain cases, as we will see. For simple assignment operations, however, `<-` is preferred.

  ```R
  a <- 3
  b < 3.1415
  c <- "This is a string"
  d <- "Yet another string"
  e <- TRUE
  f <- FALSE
  g <- T
  h <- F
  ```

  * Tip: the keyboard shortcut for the assignment operator is `Option-Hyphen` in Macs, and `Alt-Hyphen` in PCs.

* Like Python lists, an R **vector** can hold multiple items. Unlike Python lists, however, a vector must hold items of the same type:

  ```R
  disney_characters <- c("mickey", "minnie", "donald", "goofy")
  presidents <- c("washington", "adams", "jefferson")
  numbers_vector <- c(1, 3, 5, 7, 9, 11)
  ```

  * Even a single item can be a vector, however.

* This point is extremely important: R data structures are indexed at one. Whereas Python and JavaScript arrays are indexed at zero, R differs in that the first item in an R data structure. In this example, `presidents[1]` returns the first item from the vector, `"washington"`, whereas in Python, `"adams"` would be returned.

* As seen above, vectors are created using the `c()`, or concatenate, function. We can combine two vectors into a single vector with the same operation:

  ```R
  combined_vector <- c(disney_characters, presidents)
  ```

* A for-loop in R is similar to that in Python and JavaScript:

  ```R
  for (x in combined_vector){
      print(x)
  }
  ```

* We can likewise create a vector of integers, and even operate them en masse:

  ```R
  numeric_vector <- 1:length(combined_vector)
  squared_vector <- numeric_vector**2
  ```


* An `if` statement works much the same way in R as it does in Python:

  ```R
  for (prez in presidents){
      if (nchar(prez) > 5){
          next
      }
      else {
        print(prez)
      }
  }
  ```

  * `nchar()` returns the number of characters in a string.

* Whereas R vectors can only contain a single data type, a list in R can contain multiple data times.

  ```R
  random_list <- list("movies"=c("Star Wars", "Titanic", "Avatar"),
  						  "states"=c("California", "Oklahoma", "Texas", "Virginia"),
  						  "coins"=c("penny", "dime", "nickel", "quarter"),
  						  "first_presidents"=presidents,
  						  "nums"=c(1,2,3,4,5),
  						  "bools"=c(T,F,T,T,T,F)
  						  )
  ```

  * We can use the bracket notation to access an item in a list:

  ```r
  random_list["states"]
  ```

  * Or a dollar sign to accomplish the same task:

  ```R
  random_list$coins
  ```

* We can verify that `random_list` is indeed a list with `typeof()`:

  ```R
  typeof(random_list)
  ```

### 04. Students Do: We R in Junior High Again (0:15)

* **Directory:** [Activities/02_Stu_RBasics](Activities/02_Stu_RBasics)

* In this activity, students will practice the basics of R syntax. They will create vectors, use for-loops, use if/else statements, identify substrings of strings, and create functions.

### 05. Instructor Do: Review Activity (0:05)

* **Directory:** [Activities/02_Stu_RBasics](Activities/02_Stu_RBasics/Solved)

* Go over the solution with the class and answer any questions.

* In Part I, students were required to research how to access the current date. This can be done with `Sys.Date()`.

* In Part II, students were required to research how to generate a pseudo-random sample of three numbers from 1 through 33. This is accomplished with `sample(33,3)`.

  * The first argument is the range of numbers, i.e. from 1 through 33. We can also specify the range thus: `sample(1:33,3`.
  * The second argument is the number of pseudo-randomly generated numbers to return.

* In Part III, students were required to research how to access a substring of a string. We can do so with `substr(student, 2, 2)`:

  * The first argument is the string. In this case, `student` stands for the name of each student in the for-loop.
  * The second and third arguments denote the start and end points of the substring. In other words, here we begin at the second letter, and also end our substring at the second letter, returning only the second letter. Additionally, `substr(student, 2, 4)` would return a substring of three letters, from the second through the fourth letter.

### 06. Everyone Do: Vectors and Pipes (0:10)

* **Directory:** [Activities/03_Ins_Vectors](Activities/03_Ins_Vectors/Solved)

* In this activity, we will go over how to work with vectors and to run statistical summaries. As you go over each block of code, encourage students to follow along.

* Give special emphasis to the following observations:

  * We can assign `names` to vectors in R, just as in Python, we can assign indexes to a Series. Just as an array can be used to index a Series in pandas, a vector in R can be paired up as names for another vector.

  * `summary()` provides a statistical summary of a data set.

  * We can use the familiar square brackets to index elements in a vector.

* Explain that the pipe operator is a nifty feature that can improve workflow in R. Demonstrate the following example:

  * `summary(precipitation)` is used to obtain a summary of the `precipitation` vector.

  * The same result can be obtained by using the pipe operator: `precipitation %>% summary()`. 

  * This means to take what's on the **left** (`precipitation` vector), and perform the operation on the **right** (the `summary()` function).

  * The keyboard shortcut for the pipe operator, `%>%`, is `Cmd` + `Shift` + `M` in Macs, and `Ctrl` + `Shift` + `M` in Windows.
  
  * While the usefulness of the pipe operator may not be immediately obvious, it becomes more apparent in a sequence of multiple operations.


### 07. Instructor Do: File Structure Navigation (0:10)

* **Directory:** [Activities/04_Ins_Navigation](Activities/04_Ins_Navigation/Solved)

* **File:** [Activities/04_Ins_Navigation/Solved/data.csv](Activities/04_Ins_Navigation/Solved/data.csv)

* In order to work with external data files, such as CSV files, students will need to familiarize themselves with file structure navigation in R. File structure navigation in R shares some similarities to that in Unix-based environments.

* In R, the command to display the current directory is `getwd()`

  * To accomplish the same task in Terminal or Git Bash, one would type `pwd`.

* To display the contents of the current directory, type `dir()`

  * This is the equivalent of `ls` in Unix-flavored environments.

* To change the directory, enter `setwd()`.

  * This is the equivalent of `cd` in Unix.

* A simpler way to set the working directory in RStudio is to select the `Files` tab, then click next to the `up` arrow to move up a directory, or to click on a directory name to select it. Then click on `More` and select `Set As Working Directory`:

  ![Images/setwd.png](Images/setwd.png)

* Navigate to the directory for this activity, and load the `data.csv` file:

  ![Images/read_csv.png](Images/read_csv.png)

* Inform students that to run a cell of code in an Rmd file, they can click on the green play button, or press `Ctrl+Shift+Enter` (`Cmd+Shift+Enter` in Macs).

* Here are some additional command for students to reference, but they are not required to learn them:

  * To create a directory called "data_science" one would enter `dir.create("data_science")`

  * To create a file: `file.create("my_first.R")`

  * To determine whether a file exists: `file.exists()`

  * Obtain additional info on a file: `file.info()`

  * Rename a file: `file.rename(file1, file2)`

  * To copy a file: `file.copy()`

* Finally, send out the R files and `data.csv` to the class. They will need them for the next activity.

### 08. Partners Do: Discussion (0:10)

* In this activity, students will pair up with a partner. Each partner will ensure that his or her partner is able to load `data.csv` in RStudio.

  * The `tidyverse` package is required for the `read_csv()` function. Technically, only the `readr` package, which comes with `tidyverse`, is required, but we use `tidyverse` here for convenience.

  * Students may ask about the difference between `read_csv()` and `read.csv()`, if the latter comes up as an auto-complete option. Inform them that the `read_csv()` is more efficient, and is the de facto standard for reading CSV files in R now.

* Students will also discuss the syntax of R, comparing and contrasting them with those of Python and JavaScript. Which features are similar, and which are different from those Python and JavaScript? Among the topics to discuss are:

  * Assignment operator used to assign a variable
  * Declaring a function
  * Basic data structures
  * Concatenating a string
  * Logical operators (they will have to research on logical operators in R)
  * If/Else statements

* Bring the class back and call on students to summarize points from their discussion. Answer any questions about R syntax or file structure navigation.

### 09. Instructor Do: DataFrames in R (0:10)

* **Directory:** [Activities/05_Ins_Tibble](Activities/05_Ins_Tibble/Solved)

* DataFrames in R are similar to those in Python: data are organized by rows and columns, and allow operations for computation and data-wrangling. However, there are some compelling aspects of R, such as piping, which we will discuss later.

* For our purposes, a `tibble` (a word play on "table"), is a data frame.

* `tibbles.html` provides a complete walk-through of the code, but here are some additional details.

* `library(tidyverse)`: `tidyverse` is a collection of data science-oriented packages.

  * Tibbles are not available in standard R, are enabled by `tidyverse`, and are generally superior to R's standard data frame.
  * The `library()` function loads this package.

* `data(diamonds, package='ggplot2')`: the `data()` function loads data sources. `diamonds` is a sample data set that comes with `ggplot2`, a plotting package for R.

* As this is an important point, be sure to take the time to emphasize it: Unlike other languages that we have encountered so far, R allows the use of periods/dots in regular variable names:

  ```R
  total.volume2 <- mutate(diamonds, total.volume=(x*y*z))
  ```

  * `total.volume2` does not refer to a `volume2` property of `total` object. It is simply a variable name. It is equivalent to `total_volume2`, for example.


* The `mutate()` function adds a new columnar variable to the tibble.

  ![Images/mutate.png](Images/mutate.png)

  * Note that, in the `Rmd` file, it may be necessary to click on the arrow to reveal more columns of a tibble.

### 10. Students Do: Back to School (0:20)

* **Files:** [Activities/06_Stu_Tibble](Activities/06_Stu_Tibble)

* This activity will revisit the PySchool homework assignment from the fourth week: this time in R!

* Students will perform some of the same data operations they ran in the homework assignment, including the following:

  * A list of all schools
  * Calculate the total count of schools
  * Calculate the total number of students
  * Calculate the average reading and math scores
  * Calculate the percentage of students with passing reading scores, i.e. over 70%.
  * Calculate the percentage of students with passing math scores, i.e. over 70%.
  * Calculate the overall passing rate, i.e. the average of math and reading passing percentages

### 11. Instructor Do: Review Activity (0:05)

* **Files:** [Activities/06_Stu_Tibble](Activities/06_Stu_Tibble/Solved)

* Go over the most salient aspects of this activity, which include the following bullet points.

* We first load `tidyverse` with `library(tidyverse)`, then use `read_csv()` to load an external CSV file.

* `head()` and `tail()` can be used to preview the tibble.

* `unique()` is used to display the unique entries across a column.

* `summarize()` provides a basic statistical summary.

* `filter()` can be used to filter rows.

* `group_by()` can be used to perform aggregate calculations, such as mean and sum.

- - -

### 12. BREAK (0:15)

- - -

### 13. Students Do: Project 2 Group Work (0:55)

- - -

### LessonPlan & Slideshow Instructor Feedback

* Please click the link which best represents your overall feeling regarding today's class. It will link you to a form which allows you to submit additional (optional) feedback.


* [:heart_eyes: Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=18.1&lp_useful=great)

* [:grinning: Like](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=18.1&lp_useful=like)

* [:neutral_face: Neutral](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=18.1&lp_useful=neutral)

* [:confounded: Dislike](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=18.1&lp_useful=dislike)

* [:triumph: Not Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=18.1&lp_useful=not%great)

- - -

### Copyright

Data Boot Camp © 2018. All Rights Reserved.
