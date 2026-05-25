# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:34
# FILE: ex_02_cartesian.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

# Turtle Graphics in Python 3
import turtle

# .home() <> .goto(0,0)
for line in range(4):
    turtle.left(90)
    turtle.forward(100)
    turtle.goto(0,0)

# Same as mainloop()
turtle.done()


