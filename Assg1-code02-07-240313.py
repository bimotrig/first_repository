import turtle
import random

# 
def screenLeftClick(x,y):
    global r, g, b
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
    global r, g, b 
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()

#section2
pSize = 10
r, g, b = 0.0,0.0,0.0

#section2
turtle.title('Draw with your Heart')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
    