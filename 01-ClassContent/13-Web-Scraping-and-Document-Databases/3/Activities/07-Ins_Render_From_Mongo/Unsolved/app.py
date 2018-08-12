from flask import Flask, render_template

import pymongo
app = Flask(__name__)
#Connect to Mongo
conn = 'mongodb://localhost:27017'

# Create a mongo client

client = pymongo.MongoClient(conn)

# default to db
db = client.team_db
# there is any data in the collection drop it
db.team.drop()

#  Insert a few rows / documents
# collection name is team
db.team.insert_many(
    [

        {
            'player':'LeBron James',
            'position': 'Forward'
        },
        {
            'player':'Steph Curry',
            'position':'point Guard'
        }
    ]

)

@app.route('/')
def index():
    teams = list(db.team.find())
    print(teams)
    return render_template('index.html',teams = teams)


if __name__ == "__main__":
    app.run(debug=True)