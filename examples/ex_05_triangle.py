# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:34
# FILE: ex_05_triangle.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

import turtle

sides = 3 # Triangle
zangle = 360 / sides
print("Sides #", sides, "angle is", zangle)
for side in range(sides):
    turtle.forward(100)
    turtle.right(zangle)

turtle.done()


