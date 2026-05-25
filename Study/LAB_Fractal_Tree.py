#!/usr/bin/python3
# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-06-20 10:59:04
# FILE: LAB_Fractal_Tree.py
# AUTHOR: tbd.
# Classic Fractal
# Colors: Makes 'level' easier to understand!
#

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
