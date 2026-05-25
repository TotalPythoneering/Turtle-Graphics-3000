# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-06-20 10:11:54
# FILE: DEMO_Fractal_SerpinskiAH.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
import turtle

turtle.title("DEMO_Fractal_SerpinskiAH")

angle = 360/6

def Curve(lines, scale, length):
    if lines > 0:
        lines -= 1
        Curve(lines, -scale, length)
        turtle.left(scale * angle)
        Curve(lines, scale, length)
        turtle.left(scale * angle)
        Curve(lines, -scale, length)
    else:
        turtle.forward(length)

turtle.speed(0) # Zero Fastest Speed!
turtle.hideturtle()
turtle.up();turtle.setpos(0, -300);turtle.down()
turtle.left(angle)
Curve(7, 1, 5)
