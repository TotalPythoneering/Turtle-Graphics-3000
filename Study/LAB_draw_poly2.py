# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-06-19 16:09:26
# FILE: LAB_draw_poly2.py
# AUTHOR: tbd.
#

import turtle

turtle.title("LAB_draw_poly2")
def draw_poly(sides, length=50):
    if sides < 1:
        return -1
    zangle = 360/sides
    for side in range(sides):
        turtle.forward(length)
        print(turtle.pos())
        turtle.right(zangle)
    return zangle

draw_poly(3)

turtle.done()


