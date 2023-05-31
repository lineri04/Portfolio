# Imports go at the top
from microbit import *
import random 
import music

from microbit import *
import speech
r,c = 2,2
life = 9
display.set_pixel(r,c,life)
alive = True
speaker.on()

while True:
    if button_a.was_pressed():
        display.clear()
        r,c = 2,2
        alive = True
        life = 9
    
    dx = accelerometer.get_x()
    dy = accelerometer.get_y()

    if dx > 200:
        r += 1
    elif dx < -200:
        r -= 1

    if dy > 200:
        c += 1
    elif dy < -200:
        c -= 1

    display.clear()
    if r < 0:
        r = 0
        life -= 1
        music.pitch(440)
        sleep(10)
        music.stop()
        
        
    
        
    if r > 4:
        r = 4
        life -= 1
        music.pitch(440)
        sleep(10)
        music.stop()
    if c < 0:
        c = 0
        life -= 1
        music.pitch(440)
        sleep(10)
        music.stop()
    if c > 4:
        c = 4
        life -= 1
        music.pitch(440)
        sleep(10)
        music.stop()
    
    if life <= 0:
        alive = False
        
        
       
        
    else:
        display.set_pixel(r,c,life)
        sleep(300)
        
    if not alive:
        display.show(Image.SAD)
        sleep(3000)
    
    
