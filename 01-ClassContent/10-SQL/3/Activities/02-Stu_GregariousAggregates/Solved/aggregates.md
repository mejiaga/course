# Gregarious Aggregates

## Instructions

* Use aggregate functions as you run queries to answer the following questions. You will have to search the internet for some of them. Try to use aliases for more informative column headings!

1. What is the average cost to rent a film in the Sakila stores?

   ```sql
   SELECT AVG(rental_rate) AS 'Average rental rate'
   FROM film;
   ```

2. What is the average rental cost of films by rating? On average, what is the cheapest rating of films to rent? Most expensive?

   ```sql
   SELECT rating, AVG(rental_rate) AS 'Average rental rate'
   FROM film
   GROUP BY rating;
   ```

3. How much would it cost to replace all the films in the database?

   ```sql
   SELECT SUM(replacement_cost) AS 'Total replacement cost'
   FROM film;
   ```

4. How much would it cost to replace all the films in each ratings category?

   ```sql
   SELECT rating, SUM(replacement_cost) AS 'Replacement cost'
   FROM film
   GROUP BY rating;
   ```

5. How long is the longest movie in the database? The shortest?

   ```sql
   SELECT MAX(length)
   FROM film;
   ```

6. For customers with id numbers 1 through 4, display the total amount they have paid.

   ```sql
   SELECT customer_id, SUM(amount)
   FROM payment
   GROUP BY customer_id
   HAVING customer_id < 5; 
   ```

### Hint

* Consult the MySQL documentation on [aggregate functions](https://dev.mysql.com/doc/refman/5.7/en/group-by-functions.html) for a summary of the available functions.

### Bonus

* Look up how to sort the results from the above queries, in both ascending and descending order.
