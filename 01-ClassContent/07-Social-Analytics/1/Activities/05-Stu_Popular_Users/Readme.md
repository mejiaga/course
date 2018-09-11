### Popular Users

### Instructions

* In this activity, you are given an incomplete CSV file of Twitter's most popular accounts. You will use this CSV file in conjunction with Tweepy's API to create a pandas DataFrame.

* Consult the Jupyter Notebook file for instructions, but here are your tasks:

  * The "PopularAccounts.csv" file has columns whose info needs to be filled in.

  * Import the CSV into a pandas DataFrame.

  * Iterate over the rows and use Tweepy to retrieve the info for the missing columns.  Add the information to the DataFrame.

  * Export the results to a new CSV file called "PopularAccounts_New.csv"

  * Calculate the averages of each column and create a DataFrame of the averages.

### Hints:

* Make sure to use the appropriate method from the [Tweepy Docs](http://docs.tweepy.org/en/v3.5.0/api.html)

* You may have to use try/except to avoid missing users.
