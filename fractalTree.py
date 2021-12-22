# By: Balram Kandoria
# Contact with Issues: balramkandoria@gmail.com
from turtle import *
import numpy as np
import random
import turtle



# Psuedo Code
# base case
#   Branch length is 1

#recursive case
    # turle draws a line 45 degrees to the last
    # turtle returns to the start of the last move
    # turtle draws a line -45 degrees to the last
    # turtle moves the origin to the start end of the branch

# Inspired by Coding Challenge on Youtube () and some Javascript functions (i.e push and pop)
def push():
    # Set new origin
    tp = t.pos()
    t.setpos(tp)
    heading = t.heading()
    t.setheading(t.heading())

    return tp, heading

def pop(tp, heading):
    # revert push
    t.setpos(tp)
    t.setheading(heading)

def draw(length):
    t.down()
    t.forward(length)
    t.up()

def fractalTree(angle, length, lengthDecrease, stop, size):
    #Base Case Nothing is drawn
    if size < 0:
        size = 1
    if length > stop:
        #Recursive Case
        tp, heading = push()
        t.right(random.uniform(15, 40))
        t.down()
        t.pensize(size)
        draw(length)
        fractalTree(random.uniform(15, 40),length*lengthDecrease,random.uniform(0.3, 1),stop, size-2)
        t.up()
        pop(tp, heading)
        tp, heading = push()
        t.left(random.uniform(15, 30))
        t.pensize(size)
        draw(length)
        fractalTree(random.uniform(15, 40),length*lengthDecrease,random.uniform(0.3, 1),stop,size-2)
        pop(tp, heading)





t = Turtle()
turtle.screensize(canvwidth=1000, canvheight=400,
                  bg="white")
#Set Up
t.speed(0)
t.up()
t.left(90)
#Set Origin
origin = [0,-300]
# Draw First Trunk
t.setpos(origin[0], origin[1])
t.pensize(10)
t.down()
t.forward(100)
t.up()
t.pensize(1)

fractalTree(35,100, .75, 3, 10)
exitonclick()
