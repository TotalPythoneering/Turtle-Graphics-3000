# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_33_shape_each_turtle_shape.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

import turtle

# Common Display
def shape_draw(name, x_pos, y_pos):
    turtle.hideturtle()
    turtle.goto(x_pos, y_pos)
    turtle.shape(name)
    turtle.turtlesize(20, 20, 15)
    turtle.pendown()
    turtle.color('green')
    turtle.pensize(10)
    turtle.fillcolor('gold')
    turtle.showturtle()

# Pre-Defined Shapes
shapes = turtle.getshapes()

# Show Each Shape
for shape in shapes:
    turtle.penup()
    turtle.goto(0, 0)
    shape_draw(shape, 100, 0)
    turtle.textinput("Shape: " + shape, "Click to Continue")

turtle.done()

