## 6.2 Lesson Plan - Working with Weather & City APIs

### Overview

Today's class introduces the class to a number of new APIs whilst also discussing API wrappers, exception handling, and using Pandas with API responses.

##### Instructor Priorities

* Students should be able to familiarize themselves with API documentation effectively.
* Students should be able to use data from the OpenWeatherMap and World Bank APIs.
* Students should be able to load JSON from API responses into a Pandas DataFrame.
* Students should be able to use `try`/`except` blocks to handle exceptions.

##### Instructor Notes

* Have your TAs refer to the [6.2 Time Tracker](TimeTracker.xlsx) to remain on track.

### Sample Class Video (Highly Recommended)

* To view an example class lecture visit (Note: video may not reflect latest lesson plan): [Class Video](https://codingbootcamp.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=bfcc52ae-34d6-4ced-96c5-0f2c05fc5d7c)

- - -

### Class Objectives

* Students will create applications from scratch using nothing but their knowledge of Python and an API documentation
* Students will load JSON from API responses into a Pandas DataFrame
* Students will be able to use `try` and `except` blocks to handle errors

- - -

### 1. Students Do: JSON Traversal (0:10)

* Today's class will begin with a short review of what was covered during the previous lesson. In this activity, students will be traversing a JSON file using their knowledge of Python.

* Open [01-Stu_JSONTraversalReview/youtube_response.json](Activities/01-Stu_JSONTraversalReview/Resources/youtube_response.json) with a text editor to show the class what JSON file they will be working with.

  ![JSON Traversal - YouTube Response](Images/01-JSONReview_JSON.png)

* **Files:**

  * [youtube_response.json](Activities/01-Stu_JSONTraversalReview/Resources/youtube_response.json)

  * [Stu_JSON_Traversal.ipynb](Activities/01-Stu_JSONTraversalReview/Unsolved/Stu_JSON_Traversal.ipynb)

* **Instructions:** [Activities/README.md](Activities/01-Stu_JSONTraversalReview/README.md)

  * Load the provided JSON file.

  * Retrieve the video's title.

  * Retrieve the video's rating.

  * Retrieve the link to the video's thumbnail.

  * Retrieve the number of views.

* **Hints:**

  * In order to load in the data from an external JSON file, simply import the `json` library before using the `json.open(<FILE PATH>)` and `json.load(<JSON VARIABLE>)` methods.

### 2. Everyone Do: Review JSON Traversal (0:05)

* Open up [01-Stu_JSONTraversalReview/Stu_JSON_Traversal.ipynb](Activities/01-Stu_JSONTraversalReview/Solved/Stu_JSON_Traversal.ipynb) in jupyter notebook and run through the code with the class line-by-line, making certain to hit upon the following points.

  * Emphasize that the best way to solve problems like this one is to inspect the JSON manually and pull it apart once its structure is clear.

  * Point out that this activity introduces no new techniques other than importing external JSON files. This challenge merely requires students to carefully read the JSON as they write their scripts.

    ![JSON Traversal Code](Images/01-JSONReview_Code.png)

### 3. Students Do: Requests Review (0:10)

* Explain that students have one more review before they dive into the bulk of the day's lesson. For this activity, students will be making an API call to a NYT scraper and printing out data from the response.

* Open [02-Stu_RequestReview/Stu_RequestReview.ipynb](Activities/02-Stu_RequestReview/Solved/Stu_RequestReview.ipynb) in jupyter notebook and run the code or simply show students the below image to show students what they will be attempting to create.

  ![Requests Review - Output](Images/02-RequestsReview_Output.png)

* **File:**

  * [Stu_RequestReview.ipynb](Activities/02-Stu_RequestReview/Unsolved/Stu_RequestReview.ipynb)

* **Instructions:** [02-Stu_RequestReview/README.md](Activities/02-Stu_RequestReview/README.md)

  * Make a request to the following endpoint (<http://nyt-mongo-scraper.herokuapp.com/api/headlines>), and store the response.

  * JSON-ify the response.

  * Print the JSON representations of the first and last posts.

  * Print number of posts received.

### 4. Instructor Do: Review Requests Review (0:05)

* Open up [02-Stu_RequestReview/Stu_RequestReview.ipynb](Activities/02-Stu_RequestReview/Solved/Stu_RequestReview.ipynb) with Jupyter notebook and run through the code with the class line-by-line, asking different students how they implemented each task in the instructions.

  * Make sure to point out how the first and last responses are being printed to the screen. The index of `[0]` will always contain the first value of a list and the index of `[-1]` will always contain the last.

  * In order to collect the length of the list, simply use the `len()` function and pass the list in as the sole parameter.

    ![Requests Review - Code](Images/02-RequestsReview_Code.png)

### 5. Instructor Do: OpenWeatherMap API (0:10)

* Explain that the next API students will work with is the [OpenWeatherMap API](https://openweathermap.org/api), which provides various sorts of meteorological data for developers to use.

* Explain that, like the New York Times API, the OpenWeatherMap API requires users to [register](https://home.openweathermap.org/users/sign_up) for an API key.

  * Briefly walk students through the [sign-up](https://home.openweathermap.org/users/sign_up) steps and make sure everyone has their API key in-hand before moving on to the demonstration.

  ![Getting an API Key is Easy](Images/03-OpenWeather_Signup.png)

* Open [03-Ins_OpenWeatherRequest/Ins_OpenWeatherRequest.ipynb](Activities/03-Ins_OpenWeatherRequest/Solved/Ins_OpenWeatherRequest.ipynb) with jupyter notebook to show students what the application does.

  ![OpenWeather - Output](Images/03-OpenWeather_Output.png)

  * Remind students that it is good practice to use `config.py` file to shield their api_keys from others' view.

  * Point out that this script repeats the same patterns as those written for APIs the class is already familiar working with.

  * Ask a student to explain what the question mark in the URL indicates before explaining how the question mark represents the beginning of the query string.

  * Ask a student to explain what they think the query URLs is requesting before discussion how the `q` parameter allows the application to search for weather by city name in English.

  * Ask a student to explain the logic of the rest of the file and then explain how the rest of the file simply sends a GET request to the query url, converts the response to JSON, and prints the result.

  ![OpenWeather - Code](Images/03-OpenWeather_Code.png)

### 6. Students Do: Weather in Bujumbura (0:10)

* The class will now work with the OpenWeather API and create an application which provides the user with the current temperature in Bujumbura, the capital city of Burundi.

* Before students complete the next activity, show them the following image or [04-Stu_Bujumbura/Stu_Bujumbura.ipynb](Activities/04-Stu_Bujumbura/Solved/Stu_Bujumbura.ipynb) in jupyter notebook so that students understand the expected output.

  ![Stu_Bujumbura Output](Images/04-Bujumbura_Output.png)

* **File:**

  * [Stu_Bujumbura.ipynb](Activities/04-Stu_Bujumbura/Unsolved/Stu_Bujumbura.ipynb)

* **Instructions:** [04-Stu_Bujumbura/README.md](Activities/04-Stu_Bujumbura/README.md)

  * Save all of your "config" information within some variables. This includes your API key, the base URL, and the query terms desired.

  * Build your query URL. Check the documentation to figure out how to request temperatures in Celsius.

  * Make your request and save the API response.

  * Retrieve the current temperature in Bujumbura from the JSON response.

  * Print the temperature to the console.

* **Hint:**

  * You can find the [OpenWeatherMap Documentation](https://openweathermap.org/current) using the link provided.

* **Bonus:**

  * Augment your code to report the temperature in both Fahrenheit and Celsius.

### 7. Instructor Do: Bujumbura Review (0:05)

* Open up [04-Stu_Bujumbura/Stu_Bujumbura.ipynb](Activities/04-Stu_Bujumbura/Solved/Stu_Bujumbura.ipynb) in jupyter notebook and run through the code with the class line-by-line asking different students how they implemented each task in the instructions.

* Try to focus in upon the following points...

  * Building the query URL. Remind students that this is the most important piece of making an API call as it determines what information will be returned by the request.

  * The `units` query parameter. Remind students that they simply need to dig through documentation to find "options" like this. Encourage them to spend a lot of time reading the documentation of an API before writing code as this will save them time.

    ![Bujumbura Code](Images/04-Bujumbura_Code.png)

  * Ask students to offer explanations of how they solved the Bonus.

### 8. Instructor Do: OpenWeatherMap DataFrame (0:10)

* Remind students that they are not limited to manipulating API responses manually as they can use Pandas to manipulate the large amounts of data returned by APIs in bulk.

* Open [05-Ins_OpenWeatherDataFrame/Ins_OpenWeatherDataFrame.ipynb](Activities/05-Ins_OpenWeatherDataFrame/Solved/Ins_OpenWeatherDataFrame.ipynb) within Jupyter Notebook in order to show students how Pandas can be used to organize/manipulate the data retrieved from an API.

  * Point out that the beginning of this script is no different from before where the configuration information is set and stored.

* Explain that it might be interesting to look at how the temperature in a country changes based upon its latitude.

* Refer to the [OpenWeatherMap API documentation](https://openweathermap.org/current#data) or [sample response](http://samples.openweathermap.org/data/2.5/find?q=London&appid=b6907d289e10d714a6e88b30761fae22) and point out that our responses have both these pieces of data stored within them.

* Explain that a for loop is used to send a request to the Weather API for each city stored within the `cities` list, and then the desired data is appended to respective lists.

  ![OpenWeather Data Collection](Images/05-OpenWeatherDataFrame_Collection.png)

* Since the application has now collected data on each of the cities desired, a dictionary can be created in order to use a Pandas DataFrame to house this data.

    ![OpenWeather Data Creation](Images/05-OpenWeatherDataFrame_Creation.png)

* Point out that the rest is simple matplotlib. Simply call `scatter()` on the DataFrame to create a scatter plot of the temperatures versus the latitudes.

    ![OpenWeather Plot](Images/05-OpenWeather_Plot.png)

### 9. Students Do: TV Ratings (0:15)

* The class will now take some time to create an application that reads in a list of TV shows, makes multiple requests from an API to retrieve rating information, creates a pandas dataframe, and visually displays the data.

* Before students complete [06-Stu_TVRatings/Stu_TVRatings.ipynb](Activities/06-Stu_TVRatings/Unsolved/Stu_TVRatings.ipynb) explain to them that they will be using the [TVmaze API Show Search Endpoint](https://www.tvmaze.com/api#show-search) to iterate through a list of TV shows.

  ![TV Ratings Output](Images/06-TVRatingsOutput.png)

* **File:**

  * [Stu_TVRatings.ipynb](Activities/06-Stu_TVRatings/Unsolved/Stu_TVRatings.ipynb)

* **Instructions:** [06-Stu_TVRatings/README.md](Activities/06-Stu_TVRatings/README.md)

  * You may use the list provided in the starter file or create your own.

  * Request information from the TVmaze API Show Search endpoint (<https://www.tvmaze.com/api#show-search>) on each show and store the name and rating information into lists.

  * Put this data into a dictionary, and load that dict into a Pandas DataFrame.

  * Use matplotlib to create a bar chart comparing the ratings of each show.

### 10. Instructor Do: Review TV_ratings (0:05)

* Open up [06-Stu_TVRatings/Stu_TVRatings.ipynb](Activities/06-Stu_TVRatings/Solved/Stu_TVRatings.ipynb)with Jupyter Notebook and run through the code with the class line-by-line, making certain to discuss the following points.

  * Ask students how data was isolated from each response and loaded it into a Pandas DataFrame.

  * For students who made their own list of TV shows, ask if any requests returned no results thereby causing an error.  This discussion might be a nice lead into the next activity on exception handling.

  * Review how to create a bar chart using matplotlib.

    ![TV Ratings - Code](Images/06-TVRatings_Code.png)

### 11.	Instructor Do: Exception Handling	(0:08)

* Point out that the OpenWeatherMap API is robust enough that it responded with every piece of information the application could have desired. There were no missing values.

  * Not every API is as solid as the OpenWeatherMap API, however, and sometimes responses will not contain all of the data desired.

* Ask a student to explain what would happen if an application tried to look up a key within a dictionary that doesn't exist.

  * If a simple key lookup is performed - such as `data["temp"]` - and the `"temp"` key doesn't exist, Python will throw an exception and terminate the program.

  * It does not make sense for an application to terminate itself just because a dictionary key doesn't exist. It would be much better to simply deal with the error than crash the app.

  * Dealing with these kinds of errors is called exception handling and thankfully Python has built-in tools for these kinds of situations.

* Open [07-Ins_ExceptionHandling/Ins_Exception.ipynb](Activities/07-Ins_ExceptionHandling/Solved/Ins_Exception.ipynb) within Jupyter Notebook so as to show the class how an exception error can be created.

  * Point out that the `students` dictionary does not have a key for `"Jezebel"`. As such, when the application tries to print `students["Jezebel"]`, Python will complain that the key doesn't exist.

  * Run the code within the terminal to demonstrate the error.

    ![Exception Error](Images/07-Exception_Error.png)

* Open [07-Ins_ExceptionHandling/Ins_ExceptionHandling.ipynb](Activities/07-Ins_ExceptionHandling/Solved/Ins_ExceptionHandling.ipynb) within Jupyter Notebook so as to show the class how to handle exception errors.

  * Before discussing the code in detail, simply point out the `try`/`except` keywords to the class. Briefly explain that these keywords let the application recover from errors like the one that killed the program before.

  * Run the file to demonstrate that the final print statement executes, even though the `students["Jezebel"]` line throws an exception.

    ![Exception Error Handling](Images/07-Exception_DealtWith.png)

  * Explain that `try` and `except` statements are like `for` and `if` statements insomuch as they create new indented blocks.

  * Python will try to run any code in the `try` block as normal but if that code throws exceptions, Python will then run the code inside of the `except` block before continuing to run the code that follows.

    ![Exception Handling Code](Images/07-Exception_Code.png)

* Take a moment to emphasize how powerful this is. `try`/`except` allows programmers to anticipate and recover from arbitrary errors whilst preventing programs from crashing due to simple problems that can be anticipated and deal with.

* Point out that the type of exception to check for can be specified within the `except` block. This is completely optional, however, but is generally best practice to specify the precise errors to handle.

  * Catching specific exceptions allows programmers to handle specific errors in very precise ways.

  * In cases where the programmer wants to handle a particular error in a particular fashion, specifying the exception type is best practice.

  * In cases where the programmer wants to intercept any error — like for logging purposes — it is fine to catch a general exception.

* Students will know what exceptions to handle because the name of the exception that killed the program will be printed to the command line.

### 12. Students Do: Making Exceptions (0:05)

* Students will now take some time to create an application that intentionally contains a bunch of errors and, through the use of `try` and `except`, make it so the entire application runs without terminating.

* Explain that students will need to get the final line of the script to print without changing the problem code in the file.

  ![Making Exceptions - Output](Images/08-MakingExceptions_Output.png)

* **File:**

  * [08-Stu_MakingExceptions/Stu_MakingExceptions.ipynb](Activities/08-Stu_MakingExceptions/Unsolved/Stu_MakingExceptions.ipynb)

* **Instructions:** [08-Stu_MakingExceptions/README.md](Activities/08-Stu_MakingExceptions/README.md)

  * Without removing any of the lines from the starter code provided, create `try` and `except` blocks that will allow the application to run without terminating.

- - -

### 13.	BREAK	(0:15)

- - -

### 14. Instructor Do: Making Exceptions Review (0:05)

* Open up [08-Stu_MakingExceptions/Stu_MakingExceptions.ipynb](Activities/08-Stu_MakingExceptions/Solved/Stu_MakingExceptions.ipynb) within Jupyter Notebook and run through the code with the class line-by-line, making certain to discuss the following points.

  * If there is enough time, open the starter file, run it, and wrap each "problem line" within the appropriate `try`/`except` block live to demonstrate the workflow for identifying which exceptions to use in the `except` clause.

  * Replace the `print` calls in each `except` block to `pass` statements. Run the script and demonstrate that the `try`/`except` blocks still work as before — albeit with no friendly console output.

  * This allows programmers to ignore certain errors if they simply don't care that they occurred.

  * Explain that it is good practice to wrap dictionary accesses to responses from API calls in `try`/`except` blocks, just in case not all responses have the desired key.

    ![Making Exceptions - Code](Images/08-MakingExceptions_Code.png)

### 15. Instructor Do: OpenWeatherMap Wrapper (0:10)

* Open a previous example, such as the [04-Stu_Bujumbura/Stu_Bujumbura.ipynb](Activities/04-Stu_Bujumbura/Solved/Stu_Bujumbura.ipynb) solution, and point out that building query strings and dealing manually with various API configurations, while fairly straightforward, can be cumbersome.

  * On top of this, query strings and other API-specific configurations are not very readable without foreknowledge of the API.

  * Explain that there are often third-party wrappers available for popular APIs which make it easier to work with an API by handling configuration details for the programmer.

* Explain that the wrapper the class will be looking at today wraps the OpenWeatherMap API and is called [openweathermapy](http://openweathermapy.readthedocs.io/en/latest/).

  * Since openweathermapy is a third-party library, students will have to install it using `pip install openweathermapy`.

* Open up [09-Ins_OpenWeatherWrapper/Ins_OpenWeatherWrapper.ipynb](Activities/09-Ins_OpenWeatherWrapper/Solved/Ins_OpenWeatherWrapper.ipynb) with Jupyter Notebook to show the class how to use this library.

  * Point out that using this wrapper is much shorter and less cluttered than using the OpenWeatherMap API directly.

  * Before anything else, the library must be imported into the application.

  * Rather than maintaining all of the configuration options, only a `settings` dict is stored which contains the options normally concatenated into the query string.

    ![Weather Wrapper - Config](Images/09-WeatherWrap_Config.png)

  * Rather than calling the API and converting the response to JSON manually, the `own.get_current()` method can be used instead. This method takes city name, id, or geographic coordinates, as well as the settings parameters and returns the same response as the API for that city.  For more information, see the documentation: <http://openweathermapy.readthedocs.io/en/latest/#fetch-current-weather-data>.

  * Explain that the `**settings` syntax allows the programmer to pass as many query options as they want to the method.

  * Slack out [this Stack Overflow discussion](http://stackoverflow.com/questions/1769403/understanding-kwargs-in-python) on the syntax for curious students to peruse.

    ![Weather Wrapper - Code](Images/09-WeatherWrap_Code.png)

* Openweathermapy also makes it easier to _parse_ responses.

  * Point out that the application is able to isolate the `"temp"` value - nested under `"main"` and `"name"` - without having to traverse the JSON manually.

  * Openweathermapy handles traversals on the user's behalf so long as the application is provided with a list of the keys the user is interested within a `summary` list.

  * The `*summary` extracts each item from the array one by one, rather than sending in the whole list.

    ![Weather Wrapper - Parse](Images/09-WeatherWrap_Parse.png)

### 16. Students Do: Map Wrap (0:15)

* In this activity, students will be using the OpenWeatherMap library in order to make requests and parse data from the OpenWeatherMap API.

* Before slacking instructions to students for [10-Stu_MapWrap/Stu_MapWrap.ipynb](Activities/10-Stu_MapWrap/Solved/Stu_MapWrap.ipynb) show then the [image](Images/10-MapWrap_Output.png) below to show them what their application should do.

  ![Map Wrap - Output](Images/10-MapWrap_Output.png)

* **Files:**

  * [cities.csv](Activities/10-Stu_MapWrap/Resources/cities.csv)

* **Instructions:** [10-Stu_MapWrap/README.md](Activities/10-Stu_MapWrap/README.md)

  * Install the openweathermapy API wrapper.

  * Read in the cities.csv using the python csv library in order to create a list of cities.

  * Create a settings object with your API key and preferred units of measurement.

  * Get data for each city that is listed within `cities.csv`.

  * Create a list to get the temperature, latitude, and longitude in each city

  * Create a Pandas DataFrame with the results.

  * Print your summaries to verify that everything went smoothly.

* **Hints:**

  * Don't forget to utilize the openweathermapy documentation where needed: <http://openweathermapy.readthedocs.io/en/latest/>

  * We used the python csv library heavily in Week 3.  You can see the documentation for that library at <https://docs.python.org/2/library/csv.html>.

* **Bonus:**

  * If you finish early, read about and experiment with the `*` syntax.

  * Pass a `columns` parameter to `pd.DataFrame` to provide labels for the temperature and coordinate data.

### 17. Instructor Do: Review Map Wrap (0:05)

* Open up [10-Stu_MapWrap/Stu_MapWrap.ipynb](Activities/10-Stu_MapWrap/Solved/Stu_MapWrap.ipynb) within Jupyter Notebook and run through the code with the class line-by-line by having them describe the application.

  * Ask a student to explain how they solved the problem of firing requests for each city in the CSV and compare their response to the `with` block in the solution.

  * Ask a student to explain how they created a list of column labels.

  * Take a moment to explain the use of a list comprehension to generate the DataFrame in a single line.

    ![Map Wrap - Code](Images/10-MapWrap_Code.png)

### 18. Instructor Do: World Bank API (0:05)

* Explain that the next couple of activities will further familiarize students with APIs and reading complex documentation.

* Navigate to the [World Bank API](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information) website and explain that the World Bank API provides data on variety of topics including lending types, income levels, and much more.

* Open the [Basic Call Structure](https://datahelpdesk.worldbank.org/knowledgebase/articles/898581-api-basic-call-structure) link and explain the documentation's notes on argument-based vs URL-based queries.

  ![Query String vs REST-Style API Calls](Images/11-WorldBank_Docs.png)

  * Argument-based query strings are what the class has been working with thus far today whilst REST based API calls are more like those students utilized during the first class.  Argument-based queries are far more common than url-based queries.

* Open [11-Ins_WorldBankAPI/Ins_WorldBankAPI.ipynb](Activities/11-Ins_WorldBankAPI/Solved/Ins_WorldBankAPI.ipynb) within Jupyter Notebook, running the code once before discussing the application with students line-by-line.

  * Since there is no wrapper installed for this API, the class will have to interface with it directly.

    ![World Bank - Querying](Images/11-WorldBank_Query.png)

* Navigate back to the [top-level documentation page](https://datahelpdesk.worldbank.org/knowledgebase/topics/125589-developer-information) and explain that the other links contain similar documentation for more specific query types.

### 19. Partners Do: Two Calls (0:12)

* For this activity, students will be utilizing the World Bank API to make two API calls in sequence where the second API call depends on the response of the first.

* Before slacking students the instructions for [12-Stu_TwoCalls/Stu_TwoCalls.ipynb](Activities/12-Stu_TwoCalls/Solved/Stu_TwoCalls.ipynb) show them the following [output](Images/12-TwoCalls_Output.png) so they can see what kid of application they will be creating.

  ![Two Calls - Output](Images/12-TwoCalls_Output.png)

* **File:**

* [Stu_TwoCalls.ipynb](Activities/12-Stu_TwoCalls/Unsolved/Stu_TwoCalls.ipynb)

* **Instructions:** [12-Stu_TwoCalls/README.md](Activities/12-Stu_TwoCalls/README.md)

  * Retrieve a list of the lending types the world bank keeps track of, extract the ID key from each of them, and store all IDs in a list.

  * Next, determine how many countries are categorized under each lending type and store this data in a dictionary using the ID as the key and the count as the value.

    * The data for number of countries is stored in the first element of the response array.

  * Finally, print the number of countries of each lending type.

### 20. Instructor Do: Review Two Calls (0:05)

* Open up [12-Stu_Stu_TwoCalls](Activities/12-Stu_TwoCalls/Solved/Stu_TwoCalls.ipynb) within Jupyter Notebook and run through the code with the class line-by-line by having them describe the application.

  * Ask a student to explain how they retrieved the list of lending types.

  * Ask a student to explain how they got a count of how many countries of each lending type the World Bank API has on record.

    ![Two Calls - Code](Images/12-TwoCalls_Code.png)

### 21.	Instructor Do: CitiPy	(0:05)

* As a final activity, open [13-Ins_CitiPy/Ins_CitiPy_Demo.ipynb](Activities/13-Ins_CitiPy/Solved/Ins_CitiPy_Demo.ipynb) with Jupyter Notebook and run the code.

  * Don't discuss the CitiPy API in too great of detail. Students will have to figure out its API for themselves next class.

  * Point out that this code generates a list of city names for us when provided with a list of coordinates.

* Explain that CitiPy is being utilized in the for loop to add cities for every pair of coordinates in our list.

    ![CitiPy Coordinates](Images/13-CitiPy_Coords.png)

  * Emphasize that students will be responsible for determining precisely _how_ to do this in their homework assignment as well.

* Slack out the example file and the citipy documentation (<https://github.com/wingchen/citipy>) before dismissing class.

- - -

### LessonPlan & Slideshow Instructor Feedback

* Please click the link which best represents your overall feeling regarding today's class. It will link you to a form which allows you to submit additional (optional) feedback.

* [:heart_eyes: Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=6.2&lp_useful=great)

* [:grinning: Like](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=6.2&lp_useful=like)

* [:neutral_face: Neutral](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=6.2&lp_useful=neutral)

* [:confounded: Dislike](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=6.2&lp_useful=dislike)

* [:triumph: Not Great](https://www.surveygizmo.com/s3/4381674/DataViz-Instructor-Feedback?section=6.2&lp_useful=not%great)

- - -

### Copyright

Trilogy Education Services © 2018. All Rights Reserved.
