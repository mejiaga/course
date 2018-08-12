# MySQL Warmup

## Instructions

* Create a new database called `Second_International_Bank` using MySQL Workbench

  * Within this new database, create a table called `Customers` with six columns that are capable of holding the following values...

    * `ID`: An integer that will be used as the primary key for the table and automatically increments

    * `FirstName`: A string which will hold a customer's first name

    * `LastName`: A string which will hold a customer's last name

    * `Loan`: A boolean which will let users know if the customer has any unpaid loans

    * `Checking`: A decimal value which will let users know how much money a customer has in their checking account

    * `Savings`: A decimal values which will let users know how much money a customer has in their savings account

* Create five new rows of data to fill up the `Customers` table with some data

## Bonus

* Look into the [decimal](https://dev.mysql.com/doc/refman/5.7/en/precision-math-decimal-characteristics.html) datatype in MySQL and convert the `Checkings` and `Savings` columns so that they can only hold values with two or less numbers after a decimal point
