# Breaking Into the Join

## Instructions

* Now we are getting into one of the more difficult aspects of MySQL, but tell your class that this information will be very useful to them in the homework should they decide to attempt the challenge assignment.

* Joins allow those using MySQL to combine two or more individual tables together using a value that is shared between them.

* Open up [08-Ins_booksDB](Solved/books.sql) and then copy it into MySQL Workbench. Take a moment to demonstrate the structure of the `books` and `authors` tables.

  * Explain that we can utilize joins to combine and display data from both tables. Point out how the `books` table has a foreign key of `authorId` which corresponds to the `id` of a row in the `authors` table. Explain that these tables have what's known as a one-to-many relationship, since a book can only have one author, but an author can have many books.

* Explain that foreign keys are most commonly used to relate tables since primary keys are unique and won't change. Demonstrate each query below, showing students the resulting table, and explaining the differences between each join.

  * INNER JOIN: Combines tables where the specified data-values within a column match one-another

  * LEFT JOIN: Combines tables and shows all of the values of the first table specified while only the values which match on the second side will be shown

  * RIGHT JOIN: Combines tables and shows all of the values of the second table specified while only the values which match on the first table will be shown
