# Setting Up reviews_db

## Instructions

* As the founder/reviewer/editor-in-chief/database administrator/sole-employee of the new website Food, Song, and Film Daily, you are compiling a database of all food, songs, and films that you review and the scores you assign to each item. You will first create a database called `reviews_db`, then create a table for each category.


* For the table `food_reviews`...

  * Create a column called "food," which can take in a 48 character string and cannot be NULL   

  * Create a column called "score", whose data type will be integer

* For the table `song_reviews`...    

  * Create a column called "id" that automatically increments and cannot be null

  * Set the primary key of the table to `id`

  * Create a column called "song," which can take in a 100 character string and cannot be NULL

  * Create a column called "artist," which can take in a 50 character string

  * Create a column called "score," which can take in an integer


* For the table `film_reviews`...

  * Create a column called "film," which can take in a string and cannot be NULL

  * Create a column called `released_on_bluray,` which can take in a boolean

  * Create a column called "score," which can take in an integer
      

### BONUS

* Add a primary key to each table.
