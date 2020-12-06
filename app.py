from flask import Flask, request
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
@app.route("/game", methods=['POST'])
def game(input="None"):
    if request.method == 'POST':
        return runGame(request.json.get('data'))
if __name__ == '__main__':
    app.run()
