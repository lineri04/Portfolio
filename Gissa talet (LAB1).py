# LAB 1

''' Gissa talet'''


from random import randint 

def play_one_round(secret):
    attempts = 0
    correct=False

    while correct == False:
        guess=int(input('Gissa talet:  '))
        attempts +=1
        if guess == secret:
            print ('Du gissade rätt')
            correct=True
        elif guess < secret:
            print ('Du gissade lågt försök med ett högre tal')
        else:
            print('Du gissade tyvär för högt testa ett lägre tal')
    return attempts

#Start game

print('gissa talet! Gissa talet (1-100)')

n = 100
playing = True
while playing:
    secretnumber = randint (1,100)

    count = play_one_round(secretnumber)
    print (f' Du behövde {count} försök!')
    if n > count:
        n = count
        print (f'Ditt High score är {n}')

    answer = input(' Vill du spela gissa talet igen? (ja(nej): ')
    if answer !='ja':
        playing = False


    
