# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_38_shape_properties.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

import turtle


turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.begin_poly()
turtle.pensize("10")
turtle.color("blue")
for seg in range(10, 100, 5):
    turtle.left(45)
    turtle.forward(seg)
turtle.end_poly()

print(turtle.getscreen())
# Tkinter Canvas:
can = turtle.getscreen().getcanvas()
can.postscript(file = "turtle.eps")

turtle.done()

