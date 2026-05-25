# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-07-03 06:35:36
# FILE: LAB_Vector03.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
'''
Activity: ShapeScale
Can you scale a set of points?

File: LAB_Vector03.py
'''

points = [(9, 1),(7, 7),(7, 7),(1, 7),(1, 7),
(6, 11),(6, 11),(4, 17),(4, 17),(9, 13),
(9, 13),(14, 17),(14, 17),(12, 11),(12, 11),
(17, 7),(17, 7),(11, 7),(11, 7),(9, 1)]

import turtle


scale = 19.75
for ss, point in enumerate(points, 1):
    if ss % 2 == 0:
        turtle.down() # "line to"
    else:
        turtle.up()   # "go to"
    turtle.goto( point[0] * scale,
                (point[1] * scale) * -1)

turtle.done()
