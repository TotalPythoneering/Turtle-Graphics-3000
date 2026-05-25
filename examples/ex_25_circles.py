# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_25_circles.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

import turtle as robot

robot.color('purple')
robot.fillcolor('gold')
robot.hideturtle()
robot.begin_fill()
robot.pensize(10)
robot.circle(100)
robot.end_fill()

robot.goto(100, -100)
robot.dot(50, "aqua")

robot.done()


