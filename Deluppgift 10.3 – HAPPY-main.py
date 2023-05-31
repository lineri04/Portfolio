# Imports go at the top
from microbit import *
import music



# Code in a 'while True:' loop repeats forever
while True:
    if pin_logo.is_touched():
        music.play(music.BA_DING)
   
    if button_a.was_pressed():
         music.play(music.ODE)
    
    if button_b.was_pressed():
        music.play(['c', 'd', 'e', 'c'])

    else:
        display.show(Image.HAPPY)
        sleep(1)
        
        
       
