# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-06-19 16:09:26
# FILE: LAB_pen_updown.py
# AUTHOR: tbd.
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

