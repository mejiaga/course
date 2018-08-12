# Create a MySQL Database

## Instructions

* Within the MySQL Workbench editor, type `CREATE DATABASE animals_db;`

  * Explain to the class how this line of code will, when executed, create a MySQL database on the server they are connected to.

  * Also make certain to point out the semicolon at the end of the statement that tells MySQL that this line of code has concluded. Forgetting this semicolon will lead to an error being returned.

* Next, find the lightning-bolt symbol just above the editor and click on it to execute the code.

  ![SQL Bar](Images/04-CreatingDatabases_SQLBar.png)

* Point out how, on the bottom of the screen, there is a confirmation stating that the database has successfully been created.

  ![Confirmation](Images/04-CreatingDatabases_Confirmation.png)

* Something seems off though... See if anyone in the class can figure it out and give them a few seconds to think it through before answering.

  * The database never appeared in the navigator on the left side of the page! Does that mean that our code actually failed?

  * Nope! MySQL Workbench just needs to reload the connection and the "animals_db" database will now appear within the navigator.
