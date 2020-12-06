
import random
import time

def runGame(data):
    try:
        return game(data)
    except:
        raise Exception


# Sample data
# data = {
#         "ai_choice": 0,
#         "wins": 0,
#         "losses": 0,
#         "input": None,
#         "outcome": None
#         }

def game(data):

    val = data['input'].capitalize()
    if val != 'Rock' and val != 'Paper' and val != 'Scissors':
        raise Exception

    n = random.randint(1,3)
    data['ai_choice'] = n

    if val == 'Rock' and n == 2:
        data['outcome'] = 'lose'
    elif val == 'Rock' and n == 1:
        data['outcome'] = 'draw'
    elif val == 'Rock' and n == 3:
        data['outcome'] = 'win'
    elif val == 'Paper' and n == 1:
        data['outcome'] = 'win'
    elif val == 'Paper' and n == 2:
        data['outcome'] = 'draw'
    elif val == 'Paper' and n == 3:
        data['outcome'] = 'lose'
    elif val == 'Scissors' and n == 1:
        data['outcome'] = 'lose'
    elif val == 'Scissors' and n == 2:
        data['outcome'] = 'win'
    elif val == 'Scissors' and n == 3:
        data['outcome'] = 'draw'

    if (data['outcome'] == 'win'):
        data['wins'] += 1
    elif (data['outcome'] == 'lose'):
        data['losses'] += 1
    return {"data": data}