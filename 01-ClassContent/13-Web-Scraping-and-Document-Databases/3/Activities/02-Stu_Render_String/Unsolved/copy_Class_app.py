# import necessary libraries
from flask import Flask, render_template

# @TODO: Initialize your Flask app here
# CODE GOES HERE
# create instance of Flask app
app = Flask(__name__)
# @TODO:  Create a route and view function that takes in a string and renders index.html template
# CODE GOES HERE
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == "__main__":
    app.run(debug=True)
