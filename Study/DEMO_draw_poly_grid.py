# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-06-19 16:09:26
# FILE: DEMO_draw_poly_grid.py
# AUTHOR: tbd.
#

import turtle

turtle.title("DEMO_draw_poly_grid")
def draw_poly(sides, length=50):
    if sides < 1:
        return -1
    zangle = 360/sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(zangle)
    return zangle

def next_row(sides, length=50):
    turtle.left(180)
    turtle.forward(sides * length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)

turtle.speed(9)
turtle.goto(0,-200)
sides = 4; length=50
for high in range(sides * 2):
    next_row(sides, length)
    for wide in range(sides):
        draw_poly(sides, length)
        turtle.forward(length)

turtle.done()


