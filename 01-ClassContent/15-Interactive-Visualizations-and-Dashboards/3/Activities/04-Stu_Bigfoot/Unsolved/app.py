# import necessary libraries
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import (
    Flask,
    render_template,
    jsonify)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///db/bigfoot.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to the table
Bigfoot = Base.classes.bigfoot

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Routes
#################################################
app = Flask(__name__)
# Query the database and send the jsonified results


@app.route("/data")
def data():

    # @TODO: Use a database query to fetch the results and send
    # the data to your plot
    sel = [func.strftime("%Y", Bigfoot.timestamp), func.count(Bigfoot.timestamp)]
    results = session.query(*sel).\
        group_by(func.strftime("%Y", Bigfoot.timestamp)).all()
    # @TODO: YOUR CODE HERE
    return


# create route that renders index.html template
@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
