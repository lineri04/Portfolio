'''
 Monty Hall

'''
from random import randint

def monty_hall(guess, correct, switch=True):
    if not switch:
        return guess == correct

    doors = [1,2,3]
    doors.remove(guess)

    if doors[0] != correct:
        new_guess = doors[1]
    else:
        new_guess = doors[0]

    return new_guess == correct

N = 10000
cnt_stay = 0
cnt_switch = 0
for i in range(N):
    
    car = randint (1,3)
    player = randint (1,3)

    if monty_hall(player,car, switch=False):
        cnt_stay +=1
    if monty_hall(player,car, switch=True):
        cnt_switch +=1

print(f'Stanna: {100*cnt_stay/N}% Byta: {100*cnt_switch/N}%')
