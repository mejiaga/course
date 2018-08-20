from lyrics import get_lyrics

from flask import Flask, jsonify, render_template
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/pie")
def rick():

    lyrics = get_lyrics()
    labels, values = zip(*lyrics.items())
    # @TODO: Build a dictionary of the lyric data that you can use to
    # build a plotly pie chart

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
