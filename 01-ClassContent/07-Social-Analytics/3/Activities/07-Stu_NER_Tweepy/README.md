## Named Entity Recognition with Twitter

### Instructions

* Load in the `en` model and create a dictionary to hold text and label entities.

* Use Tweepy to get a user's timeline of tweets.

* Loop through the user's tweets and do the following:

  * Use the `nlp()` function on each tweet and store in a variable.

  * Handle any tweets that won't return entities.

  * Loop through the entities in each tweet and store the `text`, in the previously created dictionary `label_`.

  * Display a visualization for the tweets with its entities.

  * Store the text and labels dictionary into a DataFrame.

### Bonus

* Group the entities DataFrame by label using the Pandas `groupby` function.

* Plot the counts of each label type as a bar chart to show which labels were dominant in the data.
