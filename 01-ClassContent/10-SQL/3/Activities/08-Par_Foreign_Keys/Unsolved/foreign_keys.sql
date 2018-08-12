-- Let's create a new database
CREATE DATABASE customer_data;

USE customer_data;

-- Let's make a new table
CREATE TABLE customer (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    phone VARCHAR(30) NOT NULL,
    PRIMARY KEY (id)
);

-- And then populate that table
INSERT INTO customer (first_name, last_name, email, phone)
VALUES
("Bob", "Smith", "bobsmith@email.com", "435-344-2245"),
("Jane", "Davidson", "jdavids@email.com", "332-776-4678"),
("Jimmy", "Bell", "jimmyb@email.com", "221-634-7753"),
("Stephanie", "Duke", "sd@email.com", "445-663-5799");

-- View our table
SELECT * FROM customer;

/*
TO DO:
  1. Create a new table to hold customers' emails with a foreign key that references the customer table
  2. Populate the email table with data from the customer table
  3. Create a new table to hold customers' phones with a foreign key that references the customer table
  4. Populate the phone table with data from the customer table
*/
