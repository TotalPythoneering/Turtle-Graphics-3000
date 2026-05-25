# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:58
# FILE: ex_24_draw_string.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

import turtle as robot

ref = robot.numinput('Press Cancel To Quit', "Rectangle Size?")
if ref is not None:
    color = robot.textinput('Press Cancel To Quit', "Rectangle Color?")
    if color is not None:
        robot.penup()
        robot.goto(-300, 200)
        font = ("Times", 24, "bold")
        robot.write("You entered: " + str(ref) +", " + color, font=font)

robot.done()

