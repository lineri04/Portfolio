# Imports go at the top
from microbit import *
import random 
n = ['1','2','3','4','5','6']

while True:
    if accelerometer.was_gesture('shake'):
        display.show(random.choice(n))

    


 
    
    
