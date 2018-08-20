# import necessary libraries
import numpy as np

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
# @TODO: Setup your database here


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")

# @TODO: Create a route to accept your form data and
# save it to your database

# @TODO: Create an api route to query your database and send
# the data needed for your plot


if __name__ == "__main__":
    app.run()
