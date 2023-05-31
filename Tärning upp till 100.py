import random
playing = True
def roll_dice():
    return random.randint(1, 6)

def show_dices(ds):
    print (f'{ds} = {sum(ds)}')
while playing == True:
    a = 0
    player1_score = 0
    player1_attempts = 0
    player2_score = 0
    player2_attempts = 0
'''
Spelare 1
'''

    while player1_score < 100:
        kasta=(input('kasta tärningar'))
        player1_attempts +=1
        dices = []
        for i in range(5):
            dices.append(roll_dice())
        show_dices(dices)
        playing = True
        for i in range (2):
            n = 0
            kasta_om=list(map(int, input("Vilka tärningar vill du kasta om? ").split()))
            for element in kasta_om:
                if element in dices:
                    dices.remove(element)
                    n +=1
            for i in range(n):
                a = random.randint(1, 6)
                dices.extend([a])
            show_dices(dices)
        player1_score += sum(dices)
        print(f'score: {player1_score}')
        print('')
        print(f'Det tog {player1_attempts} försök')
        print(' ')
        print('Player 2:s tur')
'''
Spelare 2
'''
    while player2_score < 100:
            kasta=(input('kasta tärning'))
            player2_attempts +=1
            dices = []
            for i in range(5):
                dices.append(roll_dice())
            show_dices(dices)
            playing = True
            for i in range (2):
                n = 0
                kasta_om=list(map(int, input("Vilka tärningar vill du kasta om? ").split()))
                for element in kasta_om:
                    if element in dices:
                        dices.remove(element)
                        n +=1
                for i in range(n):
                    a = random.randint(1, 6)
                    dices.extend([a])
                show_dices(dices)
            player2_score += sum(dices)
            print(f'score: {player2_score}')
            print('')
            print(f'Det tog {player2_attempts} försök')
            if player1_attempts < player2_attempts:
                print('Grattis player 1 du van')
            elif player1_attempts > player2_attempts:
                print('Grattis player 2 du van')
            else:
                print('Det blev lika')
            spela_om = input('Vill du spela igen? ')
            if spela_om != 'ja':
                playing = False
