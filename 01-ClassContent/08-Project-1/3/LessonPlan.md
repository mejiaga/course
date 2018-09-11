## 8.2 Lesson Plan - Hypothesis Testing and Statistical Tests

### Overview

Today's lesson plan introduces students to basics of Hypothesis testing and a handful of statistical tests.

### Class Objectives

* Students will be able to apply ANOVA to compare the means of three or more groups

### Instructor Notes

* Today's class will introduce students to Hypothesis Testing and statistical tests. Many of the students are looking for statistical rigor to their analysis, and this lesson provides them with a starting point for performing that analysis.

* Today's class is designed to provide a high level overview of Hypothesis Testing, Null Hypothesis, and common statistical tests using the `scipy.stats` model. The activities are designed to walk through the tests at a conceptual level vs. an in-depth mathematical discussion. The activities will provide examples of applying statistical tests through functions available in the scipy.stats library.

* Encourage students to practice these tests by revisiting previous activities and choosing the appropriate test to apply. They will also be required to add at least one statistical test in their first project.

* As always, have your TAs refer to the [Time Tracker](TimeTracker.xlsx) to stay on track.

- - -

### 1. Instructor Do: Welcome Class (0:05)

### 2. Instructor Do: Intro to Hypothesis Testing (0:15)

* Explain that Hypothesis testing is a way to test a theory or question.

* Ask the students for examples of data questions they may ask and then provide the following examples:

  * Does this new medication work?

  * Is the cost of living higher in this city?

  * Does this group score higher than another group?

* Explain that a large part of Statistics and the Scientific Process is to identify a Hypothesis and then try to determine if the observations or effects could be due to chance.

* Explain the following points about Hypothesis Testing:

  * Hypothesis testing applies statistical methods to determine if something happened purely by chance.

  * Scientists and researchers often form a Hypothesis for their observations along with a Null Hypothesis. The Null Hypothesis assumes that observations or effects are simply by chance.

  * The goal of hypothesis testing is to reject the Null Hypothesis through statistical tests. Rejecting the Null Hypothesis presumes that the Hypothesis was true.

  * A Hypothesis is a measurable and testable statement about something that you expect will happen.

  * The Hypothesis is often expressed as an **If**/**Then** statement.

    * "If San Diego, CA is warmer than Austin, TX in July, then the average daily temperature will be higher."

  * The Null Hypothesis is typically stated that **NO** differences exist between the variables or groups of interest.

    * "If San Diego, CA is not warmer than Austin, TX in July, then there will be no difference in the average daily temperatures."

  * Rejecting the Null Hypothesis is never absolute. Instead, statisticians calculate the probability of observing the event. This is called the `P value`. The P value is then compared to a fixed significance level to determine if the Null Hypothesis can be rejected. A smaller P value indicates stronger evidence against the Null Hypothesis.

* Explain the following steps for Hypothesis Testing:

  1. Determine the Hypothesis and Null Hypothesis.

  2. Identify the appropriate statistical test.

  3. Determine the acceptable significance value.

  4. Compute the P-value.

  5. Determine if the P-value rejects the Null Hypothesis by comparing it to the significance value (Typically &lt; 0.05).

### 3. Partners Do: Forming a Null Hypothesis (0:10)

* Ask the students to work in pairs to convert the following questions into Hypothesis and Null Hypothesis

  * **Files**

    * [01-Par_Null_Hypothesis/README.md](Activities/01-Par_Null_Hypothesis/README.md)

  * **Instructions**

    * Convert the following Questions into an Hypothesis and Null Hypothesis

    1. Does Dark Chocolate affect arterial function in healthy individuals?

    2. Does Coffee have anti-aging properties?

### 4. Everyone Do: Review Null Hypothesis (0:05)

* Call on random groups to share their answers

* As they share, guide them to the following answers:

  * Does Dark Chocolate affect arterial function in healthy individuals?

    * Hypothesis - If dark chocolate is related to arterial function in healthy individuals, then consuming 30g of dark chocolate for 1 year will result in improved arterial function.

    * Null Hypothesis - If dark chocolate is not related to arterial function in healthy individuals, then consuming 30g of dark chocolate over for 1 year will show no improvement in arterial function.

  * Does Coffee have anti-aging properties?

    * Hypothesis - If coffee consumption is related to anti-aging properties, then consuming 400 mg of coffee daily will reduce mortality from age related disease such as heart disease.

    * Null Hypothesis - If coffee consumption is not related to anti-aging properties, then consuming 400 mg of coffee daily will not show a reduction in age related disease such as heart disease.

* Take a moment to address any questions before moving on.

### 5. Instructor Do: T-Test (0:10)

* Introduce students to the T-Test and explain the following:

  * A common question in statistics is whether or not one group is significantly different from another group.

  * The set of entities under study is referred to as the `population` while a subset of population is referred to as a `sample`.

  * A T-Test can be used to compare the mean of a sample to the population (1 Sample T-Test) or the difference between population means (Independent T-Test).

  * The null hypothesis assumes that the two means are equal. Therefore, the goal of the t-test is to reject the null hypothesis.

* Open the notebook, [Ins_1samp_ttest.ipynb](Activities/02-Ins_TTest/Solved/Ins_1samp_ttest.ipynb), and highlight the following:

  * The helper code is simply to generate some test data to work with and show its distribution.

  * One Sample T-Tests are used to compare the sample mean to the population mean.

  * The `scipy.stats.ttest_1samp` function will accept an array of samples and compare the sample mean to the population mean.

  * The pvalue of the first example is not statistically significant assuming a significance of `pvalue < 0.05`.

    ```python
    # T-Test Output:
    Ttest_1sampResult(statistic=-0.912976906342992, pvalue=0.36235943886051503)
    ```

  * The second dataset has a larger difference in means which results in a statistically significant pvalue.

    ![ttest_1samp_dataset2](Images/ttest_1samp_dataset2.png)

    ```python
    # T-Test Output:
    Ttest_1sampResult(statistic=-31.293376800980507, pvalue=8.6800698449009275e-79)
    ```

* Explain that we can also use a Two Sample T-Test to compare two population means.

* Open the notebook, [Ins_independent_ttest.ipynb](Activities/02-Ins_TTest/Solved/Ins_independent_ttest.ipynb), and highlight the following:

  * The Independent T-Test can be used to compare the means of two populations.

  * The two groups (populations) should be independent from each other (i.e. a test subject in one group could not be in the second group).

  * The underlying assumptions for this test are independence, normality, and homogeneity.

  * The [scipy.stats.ttest_ind](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) function is used to perform the calculations.

  * The parameter `equal_var=False` performs a Welch's t-test which does not assume equal population variance (homogeneity).

  * The pvalue of 0.096 in the first example is not statistically significant assuming a `p value < 0.05`. However, the second dataset has a larger difference in means which does reject the null hypothesis (`p value < 0.05`).

* Ask students for any remaining questions before moving on.

### 6. Students Do: T-Test (0:15)

* Explain that this activity will use a t-test to compare the differences in Adult Sardine Vertebrae counts from two different locations.

* Slack out the following:

  * **Files**

    * [Stu_Sardines.ipynb](Activities/03-Stu_Sardines/Unsolved/Stu_Sardines.ipynb)

  * **Instructions**

  * Calculate the mean for each population.

  * Use a T-Test to determine if there is a statistically significant difference in the number of vertebrae of Adult Sardines in Alaska vs. San Diego.

  * It is up to you to determine if you should use a One Sample or Independent t-test.

### 7. Everyone Do: Review T-Test (0:05)

* Before opening the solution, ask students if the solution required a One Sample or Independent (Two Sample) T-Test.

* Explain that we are comparing two independent populations, so an Independent T-Test is required.

* Open the solved notebook, [Stu_Sardines.ipynb](Activities/03-Stu_Sardines/Solved/Stu_Sardines.ipynb), and highlight the following:

  * The metadata indicates that `location=1` corresponds to Alaska and `location=6` corresponds to San Diego.

  * The means for both of these populations appear to be very similar.

  * The `pvalue` of 0.607 does not reject the null hypothesis.

* Ask for any remaining questions before moving on.

### 8. Instructor Do: ANOVA (0:10)

* Explain that we often want to compare the means of more than two groups. In the previous activity, we may be interested in knowing if any of the locations had significant differences from the other locations.

* Explain that we can use an Analysis of Variance (ANOVA) test to compare more than one population.

* Highlight the following points about the ANOVA test:

  * Analysis of Variance (ANOVA) is a test to compare the means of multiple groups.

  * ANOVA assumes the Null Hypothesis that there is no difference between groups.

  * Any mean that is significantly different from the rest will result in a low p-value.

* Slack out the link to the following [research paper](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4925378/) and explain the following:

  * This paper compares 5 treatments to reduce Mosquito/Human contact.

  * ANOVA is applied to compare all 5 treatments for statistical significance.

  * ANOVA only implies a statistically significant difference between the group means, but further analysis has to be completed between the groups.

* Open the notebook and walk through the following:

  * The boxplots of each treatment indicate a difference in at least one of the treatments.

    ![mosquito_boxplots](Images/mosquito_boxplots.png)

  * The treatments can be filtered in pandas to separate the groups

  ```python
  # Extract individual groups
  group1 = df[df["treatment"] == 1]
  group2 = df[df["treatment"] == 2]
  group3 = df[df["treatment"] == 3]
  group4 = df[df["treatment"] == 4]
  group5 = df[df["treatment"] == 5]
  ```

  * The `f_oneway` function in scipy.stats is used to test the null hypothesis that two or more groups have the same population mean.

  ```python
  stats.f_oneway(group1, group2, group3, group4, group5)
  ```

  * The p-value of `0.00192` matches the reported p-value from the original paper.

* Remind students that ANOVA only indicates that the group means are different, but additional testing is required to compare specific groups.

* Point out that there are important assumptions that must be satisfied before the p-value can be considered valid. The following assumptions are from the [scipy.stats documentation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.f_oneway.html):

  1. The samples are independent.
  2. Each sample is from a normally distributed population.
  3. The population standard deviations of the groups are all equal.

### 9. Students Do: ANOVA (0:10)

* Explain that this activity will use ANOVA to compare the differences in Pain Threshold for people with different hair colors.

* Slack out the following:

  * **Files**

    * [hair_anova.ipynb](Activities/05-Stu_ANOVA/Unsolved/hair_anova.ipynb)

  * **Instructions**

  * Perform a one-way ANOVA test to determine if there are any significant differences in Hair Color vs. Pain Threshold.

  * Create a Boxplot to show the distribution of pain tolerances for each hair color.

### 10. Everyone Do: Review ANOVA (0:05)

* Open the solved notebook, [hair_anova.ipynb](Activities/05-Stu_ANOVA/Solved/hair_anova.ipynb), and highlight the following:

  * The boxplot indicates that at least two of the hair color types may be significantly different than the rest.

  * The `HairColour` type is used to filter the pain measurements into separate groups.

  * The ANOVA calculation rejects the null hypothesis with a `pvalue < 0.05`.

  * ANOVA does not tell us which hair color types are statistically different; Only that at least one type was significantly different than the rest.

### 11. Instructor Do: Chi Square (0:15)

* **Files:**

  * [Ins-Chi_square.ipynb](Activities/06-Ins_Chi_Square/Solved/Ins-Chi_square.ipynb)

  * [Slide-Shows/Chi_square_test.pptx](Slide-Shows/Chi_square_test.pptx)

* Open the slideshow and explain what the chi-square test is, when it is used, each term in the formula for the chi-square value, and the steps taken in the chi-square test.

### 12. Students Do: Chi Square (0:10)

* **Files:**

  * [07-Stu_Chi_Square/README.md](Activities/07-Stu_Chi_Square/README.md)

  * [Stu-Cafes.ipynb](Activities/07-Stu_Chi_Square/Unsolved/Stu-Cafes.ipynb)

* In this activity, students will perform the chi-square test: first with Python, then by hand.

### 13. Everyone Do: Review Chi Square (0:05)

* State the null hypothesis to the class:

  * In this case, the null hypothesis would be that there is no statistical difference in the number of visits to each of the four cafés.

  * Since the total number of visits to all four cafés is 6,000, the expected number for each café is 6000/4, or 1,500.

  * The expected column is added to the data frame.

  ![Images/chi01.png](Images/chi01.png)

* Explain how to determine the critical value.

  * `stats.chi2.ppf()` is used to establish the value in Python.

  * The p-value is 0.05, so the confidence level is 0.95.

  * The degree of freedom is 3. There are four rows of variables (cafés), and only the values of three of them are necessary to determine the values of all rows.

  ![Images/chi02.png](Images/chi02.png)

  * It is also possible to consult a chi-square distribution table, such as <https://www.medcalc.org/manual/chi-square-table.php> to obtain the critical value.

* Finally, compare the chi-square value to the critical value.

  * Use `stats.chisquare()`; its first argument should be the observed values, and second the expected values.

  ![Images/chi03.png](Images/chi03.png)

  * Compare the chi-square value against the critical value.

  * Since 23.3 is greater than the critical value of 7.8, we can conclude that the differences in the number of café visits are statistically significant.

- - -

### 14. BREAK (0:15)

- - -

### 15. Everyone Do: Project Work (0:45)

* Students should spend the remainder of class working with their groups on their project.

* Be sure to walk around and check in with each project team to get a sense of how they are progressing.

- - -

### LessonPlan & Slideshow Instructor Feedback

* Please click the link which best represents your overall feeling regarding today's class. It will link you to a form which allows you to submit additional (optional) feedback.

* [:heart_eyes: Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.3&lp_useful=great)

* [:grinning: Like](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.3&lp_useful=like)

* [:neutral_face: Neutral](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.3&lp_useful=neutral)

* [:confounded: Dislike](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.3&lp_useful=dislike)

* [:triumph: Not Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=8.3&lp_useful=not%great)

- - -

### Copyright

Trilogy Education Services © 2018. All Rights Reserved.
