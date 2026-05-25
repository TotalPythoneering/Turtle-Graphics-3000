# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_shearfactor.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
# ex_shearfactor.py
#
import turtle as xform

xform.hideturtle()
xform.penup()
xform.width(10)
xform.setpos(-400,0)
xform.color("gray")
xform.shape("turtle")
xform.showturtle()
xform.delay(0)
xform.shapesize(4,4,3)
xform.fillcolor("white")
xform.tilt(90)
for ref in range(6):
    xform.forward(100)
    xform.shearfactor(xform.shearfactor() + .13)
    xform.stamp()

xform.mainloop()

