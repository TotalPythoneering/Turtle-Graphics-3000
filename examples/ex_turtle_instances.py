# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_turtle_instances.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
# ex_turtle_shapes.py
#
import turtle

# ex_turtle_instances
for ss, shape in enumerate(turtle.getshapes()):
    zt = turtle.Turtle()
    zt.up()
    zt.shape(shape)
    zt.forward(30 * ss)


for zt in turtle.turtles():
    zt.color('red')

turtle.done()

