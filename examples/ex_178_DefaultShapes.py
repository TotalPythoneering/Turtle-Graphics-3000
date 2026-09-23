# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_178_DefaultShapes.py
# AUTHOR: Randall Nagy
#
import turtle

shapes = turtle.getshapes()
for ss, shape in enumerate(shapes, 1):
    print(ss, shape)


