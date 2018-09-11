# First Steps in Querying MySQL

## Instructions

* Create queries to do the following:

  i. Find all the databases available in the current connection

  * `SHOW DATABASES;`

  ii. Select the `mysql` **database**, then show all the tables contained in that database.

  * `USE mysql;`

  * `SHOW TABLES;`

  iii. Switch back to the `sakila` database, then show all the tables contained in that database.

  * `USE sakila;`

  * `SHOW TABLES;` 

  iv. Display all columns and rows from the table `customer`. 

  ```sql
  SELECT *
  FROM customer;
  ```

  v. Display the `email` column from the table `customer`.

  ```sql
  SELECT email
  FROM customer;
  ```

  vi. Display the following columns from the table `customer`: `customer_id`, `first_name`, `last_name`, and `email`. 

  ```sql
  SELECT customer_id, first_name, last_name, email
  FROM customer;
  ```
