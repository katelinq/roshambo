from flask import Flask, request, jsonify
from flask_cors import CORS
from roshambo_app import runGame
from exception import InvalidInput
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
        try:
            return runGame(request.json.get('data'))
        except:
            raise InvalidInput("Invalid input, please enter Rock, Paper, or Scissors", 400)

@app.errorhandler(InvalidInput)
def handle_invalid_input(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

if __name__ == '__main__':
    app.run()
