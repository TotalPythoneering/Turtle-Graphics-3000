# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:34
# FILE: ex_TurtleChessOrd.py
# AUTHOR: Randall Nagy
#
import turtle

turtle.setup(800, 800)
turtle.up()
turtle.goto(-300, 300)
for ss in range(9812, 9824):
    turtle.write(chr(ss), font=('Ariel', 48, 'normal'))
    turtle.forward(48)

