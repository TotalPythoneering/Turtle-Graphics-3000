#!/usr/bin/python3
# Classic Fractal
# Colors: Makes 'level' easier to understand!

import turtle

colors = (
    "teal",
    "green",
    "red",
    "brown"
    )

def Draw(level):
    if level > 2: # Higher Trunk! (was 2)
        turtle.pensize(level/10)
        color = int(level % len(colors))
        turtle.color(colors[color])
        turtle.forward(level)
        turtle.right(33)
        Draw(level *.7)
        turtle.left(66)
        Draw(level *.7)
        turtle.right(33)
        turtle.back(level)

turtle.speed(0) # Speed 1: Faster Speed!
turtle.setheading(90)
turtle.up();turtle.goto(0,-300);turtle.down()
Draw(50) # Speed 2: Fewer "Branches" (was 50!)
