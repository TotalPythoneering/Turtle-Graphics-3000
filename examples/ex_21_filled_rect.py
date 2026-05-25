# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:58
# FILE: ex_21_filled_rect.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
''' From squares, to rectangles '''

color   = 'blue'
pos     = (-150, 0) 
extents = (200,100)

import turtle as robot

robot.pensize(5)
robot.goto(pos)
robot.pencolor(color)   # Pen (same as .color())
robot.fillcolor('gold')  # New!
robot.begin_fill()
for line in range(2):
    robot.forward(extents[0])
    robot.left(90)
    robot.forward(extents[1])
    robot.left(90)
robot.end_fill()
robot.textinput("Proof:", robot.color())  # Effect

robot.done()




