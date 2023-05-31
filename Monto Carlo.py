'''
 Monte Carlo

'''
from random import randint

n = int(input('Hur många försök?'))
fours = 0

for i in range(n):
    # Generate the randomness
    d = randint(1,6)
    print(f'Försök {i} gav en {d}')
    # Count the outcome
    if d == 4:
        fours += 1

# Sum up the total
print(f'Av {n} kast blev {fours} fyror.')
