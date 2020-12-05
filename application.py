play = True
while True:
    val = input('Rock, Paper, or Scissors? ')
    import random
    n = random.randint(1,3)
    if n == 1:
        print('Opponent chose Rock...')
    elif n == 2:
        print('Opponent chose Paper...')
    elif n == 3:
        print('Opponent chose Scissors...')
        
    import time
    time.sleep(2)

    if val == 'Rock' and n == 2:
        print('Sorry, you lose.')
    elif val == 'Rock' and n == 1:
        print('Draw, play again.')
    elif val == 'Rock' and n == 3:
        print('You win!')
    elif val == 'Paper' and n == 1:
        print('You win!')
    elif val == 'Paper' and n == 2:
        print('Draw, play again.')
    elif val == 'Paper' and n == 3:
        print('Sorry, you lose.')
    elif val == 'Scissors' and n == 1:
        print('Sorry, you lose.')
    elif val == 'Scissors' and n == 2:
        print('You win!')
    elif val == 'Paper' and n == 3:
        print('Draw, play again')
        
    time.sleep(1)
    again = input('Do you want to play again? (Y/N) ')
    if again == "N":
        play = False
    if again == 'Y':
        continue