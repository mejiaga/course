# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
app = Flask(__name__)

# @TODO:  Create a route and view function that takes in a list of strings and renders index.html template
# CODE GOES HERE

@app.route("/")
def index():
    m_list = ["Movie_1", "Movie_2", "Movie_3", "Movie_4"]
    print(m_list)
    return render_template("index.html", list = m_list)

if __name__ == "__main__":
    app.run(debug=True)
