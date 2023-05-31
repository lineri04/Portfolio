import pgzrun
import pygame
import random
import os
HEIGHT = 600
WIDTH = 900

alien = Actor('alien')
meteors = []
oxygens = []
_final_tune = False
_highscore = 0

alien_ship = Actor('alien_ship', (-100,-100))
alien_ship.drop_x = -1e6

def restart():
    alien.pos = (WIDTH//2,HEIGHT-alien.height//2)
    alien.lifes = 4
    alien.dead = False
    alien.hurt = 0
    alien.shield = 0
    alien.image = 'alien'
    alien.score = 0

    clock.schedule_interval(add_meteor,0.7)
    clock.schedule_interval(add_ship,7)
    meteors.clear()


def add_meteor():
    meteor = Actor('meteorit',(random.randint(10, WIDTH-10),10))
    meteors.append(meteor)

def add_ship():
    alien_ship.pos = (WIDTH, alien_ship.height//2)
    alien_ship.drop_x = random.randint(0,WIDTH)
    animate(alien_ship, duration = 3, pos=(-100,alien_ship.height//2))

def add_oxygen(pos):
    ox = Actor('oxygen_tank',pos)
    animate(ox, tween='accelerate',duration=3,pos=(ox.x-150, HEIGHT))
    oxygens.append(ox)

def draw():
    global _final_tune,_highscore

    screen.clear()
    screen.blit('space',(0,0))
    screen.draw.text(f'Life: {alien.lifes}', (WIDTH-150, 10),fontsize=64)
    screen.draw.text(f'Score: {alien.score}', (0, 10),fontsize=64)
    alien.draw()

    for i in range(alien.lifes):
        screen.blit('heart',(WIDTH-(i+1)*32,10))

    for meteor in meteors:
        meteor.draw()

    for oxygen in oxygens:
        oxygen.draw()

    alien_ship.draw()

    if alien.dead:
        screen.draw.text(f'GAME OVER!',centerx=WIDTH//2,centery=HEIGHT//2, fontsize=100)
        screen.draw.text(f'(Space to exit,\R\ to restart)',centerx=WIDTH//2,centery=HEIGHT//2+50, fontsize=40)
        screen.draw.text(f'Highscore: BLu {_highscore}',centerx=WIDTH//2, centery=HEIGHT//2+200,fontsize=42)
            
    if not _final_tune:
        _final_tune = True

    sounds.mixkit_arcade_retro_game_over_213.play()

    if alien.score > _highscore:
        screen.draw.text(f'NEW HIGHSCORE!!',centerx=WIDTH//2, centery=HEIGHT//2+300,fontsize=64)
        _highscore = max(alien.score,_highscore)

def update():

    if alien.dead:
        if keyboard.space: 
            exit()
        return
    if alien.hurt:
        alien.hurt -=1
        if alien.hurt == 0:
            alien.image = 'alien'

    if keyboard.left:
        alien.x -= 5
    if keyboard.right:
        alien.x += 5

        #boundires
    alien.x = min(max(alien.x,alien.width//2),WIDTH-alien.width//2)

    for meteor in meteors:
        meteor.y += 2
        if meteor.y > HEIGHT:
            meteors.remove(meteor)
            alien.score += 1

    for meteor in meteors:
        if alien.shield > 0:
            if alien.colliderect(meteor):
                meteor.image = 'dust'
        elif alien.colliderect(meteor):
            meteors.remove(meteor)
            alien.lifes -= 1
            if alien.lifes == 0:
                alien.dead = True
                clock.unschedule(add_meteor)
                clock.unschedule(add_ship)
            alien.hurt = 100
            alien.image = 'alien_hurt'
            sounds.sfx_deathscream_robot3.play()
              
            
    for ox in oxygens:
        if alien.colliderect(ox):
            alien.lifes = alien.lifes + 1 if alien.lifes < 4 else 4
            oxygens.remove(ox)
        elif ox.y == HEIGHT:
            oxygens.remove(ox)

    if alien_ship.drop_x > alien_ship.x:
        alien_ship.drop_x = -1e6
        add_oxygen(alien_ship.pos)
    
def on_key_down(key):
    if key == keys.H:
        alien.x = random.randint(0,WIDTH)
    if key == key.S:
        alien.image = 'alien_shield'
        alien.shield = 150
    if key == key.R:
        restart()
        
def on_mouse_down(pos):
    add_oxygen(pos)

os.environ['SDL_VIDEO_CENTERED'] = '1'

restart()
pgzrun.go()