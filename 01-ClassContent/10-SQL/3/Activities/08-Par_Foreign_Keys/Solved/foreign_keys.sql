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

-- Let's create a second table with a foreign key that references the first table
CREATE TABLE customer_email (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    email VARCHAR(30) NOT NULL,
    customer_id INTEGER(10) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customer(id) -- This is where the magic happens
);

-- Let's populate the second table
INSERT INTO customer_email (email, customer_id)
SELECT email, id
FROM customer;

-- View our second table
SELECT * FROM customer_email;

-- Let's create a third table with a foreign key that references the first table
CREATE TABLE customer_phone (
    id INTEGER(11) AUTO_INCREMENT NOT NULL,
    phone VARCHAR(30) NOT NULL,
    customer_id INTEGER(10) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (customer_id) REFERENCES customer(id) -- This is where the magic happens
);

-- Let's populate the third table
INSERT INTO customer_phone (phone, customer_id)
SELECT phone, id
FROM customer;

-- View our third table
SELECT * FROM customer_phone;
