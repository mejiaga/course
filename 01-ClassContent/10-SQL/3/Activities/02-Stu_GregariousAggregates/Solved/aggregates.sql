-- 1. What is the average cost to rent a film in the Sakila stores?
SELECT AVG(rental_rate) AS 'Average rental rate'
FROM film;

-- 2. What is the average rental cost of films by rating? On average, what is the cheapest rating of films to rent? Most expensive?
SELECT rating, AVG(rental_rate) AS 'Average rental rate'
FROM film
GROUP BY rating;

-- 3. How much would it cost to replace all the films in the database?
SELECT SUM(replacement_cost) AS 'Total replacement cost'
FROM film;

-- 4. How much would it cost to replace all the films in each ratings category?
SELECT rating, SUM(replacement_cost) AS 'Replacement cost'
FROM film
GROUP BY rating;

-- 5. How long is the longest movie in the database? The shortest?
SELECT MAX(length)
FROM film;

-- 6. For customers with id numbers 1 through 4, display the total amount they have paid.
SELECT customer_id, SUM(amount)
FROM payment
GROUP BY customer_id
HAVING customer_id < 5;
