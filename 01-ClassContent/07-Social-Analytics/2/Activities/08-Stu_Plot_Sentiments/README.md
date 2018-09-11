# Now Plot It Out

Sentiment Analysis is already crazy fun, but how can we visualize it? In this exercise we will do just that!

## Instructions

* Run a sentiment analysis on tweets from "@SouthwestAir".

* In order to create a plot, you will need values for the x-axis.
  - _Hint_: Use a `counter` variable that increments with each iteration of your for loop and assign it to a "Tweets Ago" key.


* Next store your results in a pandas DataFrame and read the results.

* Finally, create a plot with the following title and labels:
  - Title: "Sentiment Analysis of Tweet (`date`) for `Twitter Handle`.
    - Read up on how to use [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects) to generate a time-stamp.
    - Read up on how to use [strftime](https://docs.python.org/3/library/time.html#time.strftime) to convert the datetime to a string.
  - Y label: "Tweet Polarity"
  - X label: "Tweets Ago"


* When you are finished, look into the [Matplotlib `style` module](https://matplotlib.org/api/style_api.html) for information on how to apply the [`ggplot`](https://matplotlib.org/tutorials/introductory/customizing.html?highlight=customizing%20plots%20style%20sheets) style sheet to your plot.

### Hints

* Make sure you are using the correct method from Tweepy to gather statuses from a specific user.

## Bonus

* Order the tweets from oldest to newest in the plot.

- - -

### Copyright

Trilogy Education Services © 2017. All Rights Reserved.
