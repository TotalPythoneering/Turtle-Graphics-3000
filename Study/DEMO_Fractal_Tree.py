#!/usr/bin/python3
# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-06-20 10:43:06
# FILE: DEMO_Fractal_Tree.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
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
