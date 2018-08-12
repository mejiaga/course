# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_info

# create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data

    # return template and data
    return


# Route that will trigger scrape functions
@app.route("/scrape")
def scrape():

    # Run scraped functions

    # Store results into a dictionary

    # Insert forecast into database

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
