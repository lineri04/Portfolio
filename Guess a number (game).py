"""
Guess a numner game
Describe the game...
"""

from random import randimt

secret = randint(1,100)
correct_guess = False


while not correct_guess:
    guess = int(input('Gissa talet (1-100):'))
    if guess == secret:
        print('Du gissade rätt')
        correct_guess = True
    else:
        print('Tyvärr fel')
        if guess > secret:
            print('Du gissade för högt')
        else:
            print('Du gissade för lågt')
            
   
