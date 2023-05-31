
from turtle import *


def rek(x,y,size_x,size_y, c='blue',t='turtle'):
    up()
    goto(x,y)
    down()
    begin_fill()
    speed(0)
    shape(t)
    color(c)
    for _ in range(2):
        fd(size_x)
        left(90)
        fd(size_y)
        left(90)
    end_fill()
    


rek(-400,-300,900,600)
rek(-400,-30,900,60,'yellow')
rek(-90,-300,60,600,'yellow')

def my_write(x,y,size_x,size_y,c='blue'):
    up()
    goto(x,y)
    down()
    begin_fill()
    color(c)
    for _ in range(2):
        fd(size_x)
        left(90)
        fd(size_y)
        left(90)
    end_fill()



my_write(-90,-10,0,0)
ht()
up()
goto(-60,-25)
write('SWEDEN', font=('arial',30,'bold'), align='center')
down()
up()
goto(400,-280)
color('yellow')
write('MADE BY: LINUS ERIKSSON', font=('arial',10,'bold'), align='center')



