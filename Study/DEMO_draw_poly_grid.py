# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-06-19 16:09:26
# FILE: DEMO_draw_poly_grid.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
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


