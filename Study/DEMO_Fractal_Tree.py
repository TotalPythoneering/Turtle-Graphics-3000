#!/usr/bin/python3
# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-06-20 10:43:06
# FILE: DEMO_Fractal_Tree.py
# AUTHOR: tbd.
# Classic Fractal
#
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
