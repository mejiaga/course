CREATE DATABASE Second_International_Bank;

USE Second_International_Bank;

CREATE TABLE Customers (
	ID int(50) AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Loan BOOLEAN,
    Checking DECIMAL(20,2),
    Savings DECIMAL(20,2),
    primary KEY(ID)
);

INSERT INTO Customers(FirstName,LastName,Loan,Checking,Savings)
VALUES ("Richard", "Rich", TRUE, 1000.00, 20000.50),
("Bob", "Someone", TRUE, 10.75, 2.05),
("Shelly", "RichRich", FALSE, 1000000.00, 50000025.00),
("Ryan", "Middleman", FALSE, 250.00, 10000.00),
("Ryan", "Middleman", FALSE, 250.00, 10000.00),
("Shannon", "Waffles", TRUE, 1000.00, 20000.50);

/* This Solution will also work
INSERT INTO Customers(FirstName,LastName,Loan,Checking,Savings)
VALUES ("Richard", "Rich", TRUE, 1000.00, 20000.50)

INSERT INTO Customers(FirstName,LastName,Loan,Checking,Savings)
VALUES ("Bob", "Someone", TRUE, 10.75, 2.05);

INSERT INTO Customers(FirstName,LastName,Loan,Checking,Savings)
VALUES ("Shelly", "RichRich", FALSE, 1000000.00, 50000025.00);

INSERT INTO Customers(FirstName,LastName,Loan,Checking,Savings)
VALUES ("Ryan", "Middleman", FALSE, 250.00, 10000.00);

INSERT INTO Customers(FirstName,LastName,Loan,Checking,Savings)
VALUES ("Shannon", "Waffles", TRUE, 1000.00, 20000.50);
*/ 
SELECT * FROM Customers;
