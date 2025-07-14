#!/usr/bin/python3
# Classic Fractal
import turtle

def Draw(level):
    if level > 2:
        turtle.pensize(level/10)
        turtle.forward(level)
        turtle.right(33)
        Draw(level *.7)
        turtle.left(66)
        Draw(level *.7)
        turtle.right(33)
        turtle.back(level)

turtle.setheading(90)
turtle.up();turtle.goto(0,-300);turtle.down()
Draw(50)
