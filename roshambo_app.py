
import random
import time

# send user input to the game
def runGame(userInput):
    return game(userInput)
# return output to the api

def game(userInput):
    d = {'Wins': 0, 'Losses': 0}
    play = True
    while play:
        val = userInput.capitalize()
        if val != 'Rock' and val != 'Paper' and val != 'Scissors':
            raise Exception('Invalid input')

        n = random.randint(1,3)
        if n == 1:
            print('Opponent chose Rock...')
        elif n == 2:
            print('Opponent chose Paper...')
        elif n == 3:
            print('Opponent chose Scissors...')
            
        time.sleep(2)

        if val == 'Rock' and n == 2:
            print('Sorry, you lose.')
            d['Losses'] += 1
        elif val == 'Rock' and n == 1:
            print('Draw, play again.')
        elif val == 'Rock' and n == 3:
            print('You win!')
            d['Wins'] += 1
        elif val == 'Paper' and n == 1:
            print('You win!')
            d['Wins'] += 1
        elif val == 'Paper' and n == 2:
            print('Draw, play again.')
        elif val == 'Paper' and n == 3:
            print('Sorry, you lose.')
            d['Losses'] += 1
        elif val == 'Scissors' and n == 1:
            print('Sorry, you lose.')
            d['Losses'] += 1
        elif val == 'Scissors' and n == 2:
            print('You win!')
            d['Wins'] += 1
        elif val == 'Scissors' and n == 3:
            print('Draw, play again')
        else:
            print('Invalid input.')
            continue
        print(n)
        print(val)
        print('Wins: ' + str(d['Wins']))
        print('Losses: ' + str(d['Losses']))
        play = False
        return(str(d))

        # time.sleep(1)
        # end = True
        # while end:
        #     again = input('Do you want to play again? (Y/N) ').capitalize()
        #     if again == "N":
        #         print('Thanks for playing!')
        #         play = False
        #         quit()
        #     elif again == 'Y':
        #         end = False
        #     else:
        #         continue