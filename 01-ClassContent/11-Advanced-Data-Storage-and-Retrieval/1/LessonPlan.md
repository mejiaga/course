## 11.1 Lesson Plan - Introduction to SQLAlchemy

### Please take the Mid-Course Instructional Staff Survey

Trilogy, as a company, values transparency and data-driven change quite highly. As we grow, we know there will be areas that need improvement. It’s hard for us to know what these areas are unless we’re asking questions. Your candid input truly matters to us, as you are key members of the Trilogy team. In addition to the individual feedback at the end of lesson plans
we would appreciate your feedback at the following link:
[https://docs.google.com/forms/d/e/1FAIpQLSdWXdBydy047_Ys1wm6D5iJY_J-0Mo0BqCjfGc4Er2Bz9jo5g/viewform](https://docs.google.com/forms/d/e/1FAIpQLSdWXdBydy047_Ys1wm6D5iJY_J-0Mo0BqCjfGc4Er2Bz9jo5g/viewform)

### Overview

Today's lesson will introduce students to the SQLAlchemy library for Python.

### Instructor Notes

* This first day on SQLAlchemy includes a lot of material students will need for the homework whilst day two includes more complex activities for the class to practice on. As such, feel free to mix up the timing/activities for these two lessons so as to ensure students feel comfortable with the SQLAlchemy library and are having an enjoyable experience.

* If SQLAlchemy is not running on a student's computer, simply have them `conda install -c anaconda sqlalchemy` within their terminal/GitBash.

* Students will also need `pymysql` installed in their virtual environments: `conda install -c anaconda pymysql`.

### Troubleshooting Notes

* Please use the provided SQL schema/seed files or Sqlite files as a backup to the remote database links. There are occasionally issues that prevent the remote database connections from working, so you will find these backup resources in the activity `Resources` folders. You can simply create a local database with these, or use the Sqlite database file.

### Sample Class Video (Highly Recommended)

* To view an example class lecture visit (Note video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=740bcdc5-97e4-486a-97e8-81aba3de163f#)

- - -

### Class Objectives

* Students will  be able to connect to a SQL database using SQLAlchemy
* Students will learn to perform basic SQL queries using engine.execute()
* Students will learn how to create Python classes and objects
* Students will  be able to create, read, update, and delete data from a SQL database using SQLAlchemy's ORM

- - -

### 1. Instructor Do: Welcome the Class (0:01)

* Welcome the class back to another fun-filled week of MySQL. Unlike last week, however, the class will be moving back into Python as they will now be creating scripts that will interact with their databases.

### 2. Partners Do: Looking Into SQLAlchemy (0:05)

* Before diving into SQLAlchemy as a class, have students break into groups of two or three and research the following questions...

  * What is an ORM?

  * What are the benefits to using an ORM?

  * What are some of the disadvantages to using an ORM?

* Some of the advantages to using an ORM for SQL databases include...

  * Being able to work across different SQL dialects using the same basic Python query

  * Being able to create command line interfaces which allow users to construct SQL queries without having to know the language

### 3. Instructor Do: Introduction to SQLAlchemy (0:05)

* SQLAlchemy is a Python ORM - Object Relational Mapper - for SQL databases. In much more basic terms, SQLAlchemy essentially allows Python developers to use external scripts to modify SQL databases.

  * Remind the class that there are many different SQL dialects out there. MySQL, PostgreSQL, and SQLite to name a few.

  * SQLAlchemy is able to bridge the gaps between these similar dialects. This means that a single Python program written using SQLAlchemy can be used to affect different databases without having to write new queries each time.

* Open up and slack out the link to the [SQLAlchemy Documentation](http://docs.sqlalchemy.org/en/latest/dialects).

  * Point out to the class how this specific link leads to a list of the SQL dialects that are compatible with SQLAlchemy.

  * To the left side of the page, however, students can find the complete documentation for the SQLAlchemy library.

  * Students should consult this documentation to clarify any questions they may have before consulting the instructional team. They should be able to fix any number of bugs they encounter this way.

* Answer whatever questions the class may have before moving onto the next activity.

### 4. Instructor Do: Building a SQLAlchemy Connection (0:10)

* Let the class know that, for the purposes of today's class, they will only be working with MySQL and SQLite databases.

  * SQLite is a SQL dialect that shares much the same syntax as MySQL but that it is entirely serverless.

  * How can a database be serverless? Well, SQLite reads and writes directly to ordinary disk files which can in-turn be stored on a computer's hard drive. This makes it amazingly easy to perform tests with and share between users.

  * If any students do not have SQLite installed, have them run `conda install -c anaconda sqlite` within their Terminal/GitBash.

  * `pymysql` must also be installed in the virtual environment using `conda install -c anaconda pymysql`.

* Once everyone has installed SQLite, open up [01-Ins_BasicSQL_Connection](Activities/01-Ins_BasicSQL_Connection/Solved/Read_Census_Data.ipynb) within Jupyter Notebook and go through the code with the class.

  * In order to use SQLAlchemy, certain modules from the library must be imported. For example, to create a connection to a SQL database, the `create_engine` module will need to be imported.

  * For Python to read MySQL databases, `pymysql` must also be imported and then the `pymysql.install_as_MySQLdb()` method must be used.

  * After importing in all of the necessary libraries/modules, the connection engine can finally be created using the `create_engine()` method from earlier and passing a connection string into it.

    ![Create Engine](Images/01-Connections_CreateEngine.png)

  * The connection string is composed of five distinct parts and can be constructed by following the following syntax:

    `<Dialect>://<Username>:<Password>@<Host Address>:<Port>/<Database>`

  * Many of these elements should look similar to those students used to connect to their MySQL servers before. The main difference here is that the SQL dialect being used on the server (MySQl, SQLite, Oracle, etc...) and the name of a specific database on the server must be added to the connection string.

  * So, to connect to a MySQL database called "SportsDB" hosted on "localhost" for example, `mysql://<Username>:<Password>@localhost/sportsdb` would be used.

* Once a connection engine has been created, developers can then use `engine.execute()` to run SQL commands from their Python script. Simply pass the code to run into the method as a string and SQLAlchemy will pass the request onto the database.

  * For example, to collect all of the data stored within a table on a database, simply pass `SELECT * FROM <Tablename>` into the `engine.execute()` method.

    ![Engine Execute](Images/01-Connections_Execute.png)

  * Point out how the data being returned in [01-Ins_BasicSQL_Connection](Activities/01-Ins_BasicSQL_Connection/Solved/Read_Census_Data.ipynb) is stored within a variable and then looped through so as to print out the rows from `Census_Data`.

* Answer whatever questions the class may have before moving onto the next activity.

### 5. Students Do: Ice Cream Connection (0:15)

* In this activity, students will be creating a new MySQL database within MySQL Workbench and then creating a connection to it using SQLAlchemy. They will then read the data in with `engine.execute()`.

  ![Ice Cream Output](Images/02-IceCreamConnect_Output.png)

* **Instructions**:

  * Connect to your localhost database in MySQL Workbench.

  * Create a table of 5 or more ice cream flavors, each of which should have a rating out of 100, and price (make sure that a few cost $1.25).

  * Query your table in MySQL Workbench for every flavor of ice cream.

  * Query your table in MySQL for all flavors that cost 1.25 or more.

  * Create a Python script that uses SQLAlchemy to accomplish all of the above queries.

### 6. Everyone Do: Ice Cream Connection Review (0:05)

* Open up [02-Stu_IceCreamStore](Activities/02-Stu_IceCreamStore/Solved/IceCreamConnector.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

* Make sure to hit upon the following points...

    ![Ice Cream Code](Images/02-IceCreamConnect_Code.png)

  * The queries being used by `engine.execute()` are the same that would be used in MySQL Workbench. The only difference is that the data is being stored within a variable and then looped through.

### 7. Instructor Do: SQLAlchemy and Pandas (0:05)

* One of the most impressive aspects of SQLAlchemy is how it integrates with Pandas. Open up [03-Ins_ReadSQL](Activities/03-Ins_ReadSQL/Solved/SQLIntoPandas.ipynb) within Jupyter Notebook in order to show the class how this can be accomplished.

  * Through creating a connection to a database using SQLAlchemy, Pandas can use that engine to pull data directly into a dataframe with the `pd.read_sql()` method.

  * When using the `pd.read_sql()` method, a query string and a connection variable must be passed through. The query string is the same as those written for MySQL Workbench while the connection variable can be declared using `engine.connect()`.

    ![SQL Into Pandas](Images/03-SQLToPandas_Code.png)

  * Through using Pandas alongside SQLAlchemy, developers can more easily perform data cleanup/maintenance on their databases. This also allows them to tinker with changes using Python without having to commit any of those changes to the server itself.

* Answer whatever questions the class may have before continuing onto the next activity.

### 8. Students Do: Read All the SQL (0:10)

* Students will now query an external server using Pandas and SQLAlchemy as they work to create new dataframes based on US census data.

  ![Read All SQL Output](Images/04-ReadAllSQl_Output.png)

* **Instructions**:

  * Using the following connection string, complete the following tasks within a Jupyter Notebook.

    `mysql://k5xunpkmojyzse51:ifagg1gp7e2xyapi@ffn96u87j5ogvehy.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/tq6h098h0ym00zp6`

  * Query all the data from the `Cenus_data` table and load into pandas.

  * Query all the data from the `Zip_data` table and load into pandas.

  * Show the `.head()` of your newly imported dataframes and then come up with the best way in which to merge the data together.

### 9. Everyone Do: Read All the SQL Review (0:05)

* Open up [04-Stu_ReadAllTheSQLs](Activities/04-Stu_ReadAllTheSQLs/Solved/Read_All_The_SQLs.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

### 10. Instructor Do: Preview SQLAlchemy With Classes (0:05)

* So far the class has been using SQLAlchemy in ways that make it work in similar fashion to MySQL Workbench. It takes in strings of SQL code and then performs some tasks based upon that. This, however, is not how it is used in most cases.

* Open up [05-Ins_Preview_SQL_Alchemy](Activities/05-Ins_Preview_SQL_Alchemy/Solved/Alchemy.ipynb) within an IDE and show the class how differently this code looks in comparison to those scripts they wrote previously.

  * The first thing that should stand out as different to students are the two classes near the top of the application. Classes are essentially blueprints for Python objects. In other words, they allow developers to create organized variables with keys, values, and methods on the fly.

  * It is not terribly important for students to understand what this means at the moment. Once the class reconvenes after break, students will be diving much deeper into creating/using classes.

  * What is important is for students to understand that SQLAlchemy uses Python classes as its primary means to communicate and make changes to SQL databases. This is what makes SQLAlchemy an ORM as it uses objects to map changes to SQL tables/databases.

* Let the class know that it is normal to feel intimidated by SQLAlchemy at first. Thankfully this class will be taking a deep look into how the library functions and the whole team will be right there beside them as they become masters of this ORM.

- - -

### 11. BREAK (0:15)

- - -

### 12. Instructor Do: A Schooling on Classes (0:10)

* Once everyone has returned from their break, let the class know that they will now be given a crash course in object oriented programming.

  * Object oriented programming (OOP) is a style of coding based around the concept of "objects". These objects may contain data, often known as attributes, and functions, often known as methods.

  * Python is a class-based programming language. This means that objects can be created according to user-created blueprints, thus allowing developers to rapidly create objects of similar structure/purpose but with differing values.

* Open up [06-Ins_Classes](Activities/06-Ins_Classes/Solved/Dog.ipynb) within an IDE and go through the code line-by-line.

  * To define a class in Python, developers simply have to type `class <ClassName>():`

  * The line `def __init__(self):` is a special method called a "class constructor" that Python calls every time a new instance of the class is created.

  * The parameters declared within `__init__` - excluding "self" - must be passed whenever the developer wishes to create a new instance of the class. This is because each object's values will be defined by these parameters.

    ![Declaring Classes](Images/06-Classes_Declare.png)

  * Creating an instance of a class is quite simple. Simply call the class using the class name and pass in whatever arguments its `__init__` method accepts.

  * Users can then access the object's attributes using dot operators with the object. So, in order to call the `name` attribute of an object, one would use `object.name`

    ![Class Instances](Images/06-Classes_Instance.png)

* Go over this code one more time with the class, answering whatever questions students may have. Once everyone is comfortable with Python classes, move onto the next activity.

### 13. Students Do: Surfer Class (0:15)

* Students will now work on creating their own classes in Python. More specifically, they will be creating a "Surfer" class which will be used more throughout today's lesson.

  ![Surfer Class Output](Images/07-SurferClass_Output.png)

* **Instructions**:

  * Create a class `Surfer` that takes in a name, hometown, and rank.

  * Create an instance of a surfer and then print the following from your surfer object: name, hometown and rank.

* **Bonus**:

  * Create a while loop that will allow you keep taking input that allows you to create new instances of surfers.

  * Keep the loop going until the user specifies otherwise.

### 14. Everyone Do: Surfer Class Review (0:05)

* Open up [07-Stu_Surfer_Class](Activities/07-Stu_Surfer_Class/Solved/Surfer.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

### 15. Instructor Do: A Method to The Classes (0:05)

* Creating and attaching methods to Python classes is also fairly easy to accomplish, thus allowing developers to attach regularly used functions to objects of similar types.

  * Adding methods to a class is very similar to the `__init__` method discussed earlier. Simply define the function using `def`, provide it with a name, and then pass a list of parameters - including self - into the parentheses that follow.

  * To run the method in code, simply call upon the instance of an object created and then, using dot notation, reference the method. For example: `doggy.printHello()` would run the `printHello()` method for the `doggy` object.

* Open up [08-Ins_Classes_With_Methods](Activities/08-Ins_Classes_With_Methods/Solved/Classes_With_Methods.ipynb) within an IDE and go through the code line-by-line, answering whatever questions students may have.

  * The `boast()` method contained within the `Expert` class takes in another object as a parameter and then prints out some statements based upon its contents.

    ![Class Methods](Images/08-ClassMethods_Code.png)

* Answer whatever questions students may have before moving onto the next activity.

### 16. Students Do: Surfer Class Extended (0:10)

* The class will now be reworking their Surfer script from earlier as they add in some methods to perform some specific tasks.

  ![Surfer Methods Output](Images/09-SurferMethods_Output.png)

* **Instructions**:

  * Create a surfer class that has name, hometown, rank, wipeouts, and surfer count.

  * Create a method called `speak` that prints "Hangs loose, bruh!"

  * Create a method called `biography` that prints the surfer's name and hometown.

  * Create a method called `cheer` that will print "I totally rock man, no wipeouts!" if the surfer has no wipeouts. Otherwise, it prints 'Bummer bruh, keep on keeping on!'.

  * Create two surfers that print out all their info and run all the methods.

* **Bonus**:

  * Add a method to your class that prints out how many surfers are currently shredding.

* **Hint**:

  * When dealing with the bonus, make sure to set a variable to keep track of surfers before you initialize but after you declare the class.

### 17. Everyone Do: Surfer Class Extended Review (0:05)

* Open up [09-Stu_Surfer_Class_Extended](Activities/09-Stu_Surfer_Class_Extended/Solved/Surfer_Extended.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

### 18. Everyone Do: Back to the SQL (0:20)

* Now that everyone has a firm grasp on how to create and use Python classes, it is time to dive back into SQLAlchemy and its class-based methodology.

* For the purposes of this activity, start out with a blank Python script and have the class follow along. By the end of the activity, everyone should have code that looks that stored in [10-Ins_SQL_Alchemy_Revisited](Activities/10-Ins_SQL_Alchemy_Revisited/Solved/Alchemy_Annotated.ipynb).

* As with most Python code that uses external libraries, the first step is to import in the modules desired.

  * `create_engine` allows SQLAlchemy to create connections to SQL databases.

  * `declarative_base` allows SQLAlchemy to convert the classes created in Python to SQL tables.

  * The different datatypes used in SQL must also be imported into Python from SQLAlchemy. These datatypes are then used when creating class fields so as to state what datatypes each column in the SQL table should contain.

    ![Imports](Images/10-BackToSQL_Import.png)

* The classes created using SQLAlchemy's "Base" class will serve as the anchor points for SQL tables.

  * When creating classes to be used with SQLAlchemy, a `__tablename__` field must be declared and provided with the name of a table. If the table exists, any new objects created will be added into the existing table. If the table does not yet exist, a new table will be created based upon the class' fields.

  * Each field of a SQLAlchemy class must be declared as a column and the datatype of the field must also be provided.

  * A primary key can also be set by using the `primary_key` value and setting it to either True or False.

    ![Classes](Images/10-BackToSQL_Classes.png)

  * Creating instances of SQLAlchemy classes functions almost identically to creating regular Python objects. It is not necessary to declare fields explicitly within the constructor but this is common practice.

    ![Objects](Images/10-BackToSQL_Objects.png)

* After the SQLAlchemy classes have been made, they can be created on the SQL database by creating a connection engine and then calling `Base.metadata.create_all(engine)`

  * The `create_all` looks through the Python script and checks if the classes declared exist within the database being connected to. If they do not yet exist, the tables will be created at this time.

    ![Connection](Images/10-BackToSQL_Connection.png)

* SQLAlchemy functions much like Git does in how new rows of data can be added/changed within a SQL table.

  * A SQLAlchemy session is created using the `Session` module and bound to the connection engine.

  * New rows of data can then be staged by creating a new instance of a SQLAlchemy class and passing them into `session.add()` as a parameter.

  * When all of the changes desired have been made, simply use `session.commit()` to push them up to the database.

    ![Commit Changes](Images/10-BackToSQL_Commit.png)

* Run through the code as many times as needed so as to ensure that the class fully understands how to use SQLAlchemy to add new data/tables to a SQL database.

  * Feel free to point out how simple it is to collect all of the data from a SQL table using SQLAlchemy as well.

  * Simply use `session.query()` and pass the class/table to query in as a parameter. The returned data can then be looped through and printed to the terminal.

    ![Basic Querying](Images/10-BackToSQL_Query.png)

* When the class seems comfortable with the script they have just written, go through it one final time and have them describe to you what each line does. Upon reaching the end of the script, feel free to move onto the next activity.

### 19. Students Do: Surfing SQL (0:20)

* Students will now test their SQLAlchemy skills as they attempt to turn their Surfer class from earlier into a new table on a SQL database whilst also creating a new Board class.

* **Instructions**:

  * Modify the `Surfer` class created during the previous activity so that it will function with SQLAlchemy.

    * `__tablename__` should be "surfers"
    * `surfer_id` should be an integer and the primary key
    * `name` should be a string capable of holding 255 characters
    * `hometown` should be a string capable of holding 255 characters
    * `rank` should be an integer

  * Create a new class called `Board` which will function with SQLAlchemy and has the following parameters...

    * `__tablename__` should be "surfboards"
    * `id` should be an integer and the primary key
    * `surfer_id` should be an integer that references a surfer_id in the "surfers" column
    * `board_name` should be a string capable of holding 255 characters
    * `color` should be a string capable of holding 255 characters
    * `length` should be an integer

  * Pull a list of all of the surfers and surfboards already inside the database

  * Push a new surfer and surfboard to the tables on the database

### 20. Everyone Do: Surfing SQL Review (0:09)

* Open up [11-Stu_Surfer_SQL](Activities/11-Stu_Surfer_SQL/Solved/Surfer_SQL.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, answering whatever questions students may have.

- - -

### LessonPlan & Slideshow Instructor Feedback

* Please click the link which best represents your overall feeling regarding today's class. It will link you to a form which allows you to submit additional (optional) feedback.

* [:heart_eyes: Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=11.1&lp_useful=great)

* [:grinning: Like](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=11.1&lp_useful=like)

* [:neutral_face: Neutral](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=11.1&lp_useful=neutral)

* [:confounded: Dislike](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=11.1&lp_useful=dislike)

* [:triumph: Not Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=11.1&lp_useful=not%great)

- - -

### Copyright

Trilogy Education Services (C) 2018. All Rights Reserved.
