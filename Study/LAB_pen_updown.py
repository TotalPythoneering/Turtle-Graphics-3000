# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-06-19 16:09:26
# FILE: LAB_pen_updown.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
import turtle

# Draw a dashed line
turtle.title("LAB_pen_updown")
even = True
for seg in range(10, 100, 5):
    if even:
        turtle.penup()
        even = False
    else:
        turtle.pendown()
        even = True
    turtle.forward(12)
turtle.done()

