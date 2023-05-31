

import turtle
import random

def up():
    hugo.setheading(90)
    hugo.forward(100)

def down():
    hugo.setheading(270)
    hugo.forward(100)

def left():
    hugo.setheading(180)
    hugo.forward(100)

def right():
    hugo.setheading(0)
    hugo.forward(100)

def clickMiddle(x, y):
    colors.append(hugo.color()[0])
    hugo.color(colors.pop(0))   

def clickRight(x, y):
    hugo.pensize(random.randint(3,16))
    
def clickCircle(x, y):
    hugo.pu()
    hugo.setpos(x,y)
    hugo.pd()
    hugo.circle(50)

def clickFirst(x, y):
    hugo.pu()
    hugo.setpos(x,y)
    hugo.pd()
    ws.onclick(clickSecond,1)

def clickSecond(x, y):
    hugo.goto(x,y)
    ws.onclick(clickFirst,1)

def clickRect(x, y):
    hugo.pu()
    hugo.setpos(x,y)
    d = 0
    hugo.pd()
    for _ in range(4):
        hugo.setheading(d)
        hugo.fd(100)
        d += 90

    return

def r():
    hugo.speed(4)
    ws.onclick(clickRect,1)
    hugo.shape('classic')

def c():
    hugo.speed(4)
    ws.onclick(clickCircle,1)
    hugo.shape('classic')
    
def l():
    hugo.speed(4)
    ws.onclick(clickFirst,1)
    hugo.shape('classic')

def d():
    hugo.pencolor('white')
    hugo.pensize(100)
    hugo.speed(0)
    ws.onclick(None,1)
    hugo.shape('turtle')


def b():
    hugo.write('Linus Eriksson',font=("Arial", 20, "normal"))
def dragging(x, y):
    hugo.ondrag(None)
    hugo.setheading(hugo.towards(x, y))
    hugo.goto(x, y)
    hugo.ondrag(dragging)

colors = ["red", "blue", "green", "yellow", "black"]
click_state = None

hugo = turtle.Turtle()

ws = turtle.Screen()
ws.listen()             

ws.onclick(clickCircle,1)
ws.onclick(clickMiddle,2)
ws.onclick(clickRight,3)
ws.onkey(up, "Up") 
ws.onkey(down, "Down")
ws.onkey(left, "Left")
ws.onkey(right, "Right")
ws.onkey(c, 'c')
ws.onkey(r, 'r')
ws.onkey(d, 'd')
ws.onkey(l, 'l')
ws.onkey(b, 'b')
hugo.ondrag(dragging)

ws.mainloop()  
