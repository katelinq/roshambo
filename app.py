from flask import Flask
from flask_cors import CORS
from roshambo_app import runGame
#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    data = "Welcome to Roshambo!"
    return data
@app.route("/<input>")    
def game(input="None"):
    return runGame(input)
if __name__ == '__main__':
    app.run()
