'''
Activity: ShapeRotation
Can you invert a set of points?

File: LAB_Vector01.py
'''

points = [(9, 1),(7, 7),(7, 7),(1, 7),(1, 7),
(6, 11),(6, 11),(4, 17),(4, 17),(9, 13),
(9, 13),(14, 17),(14, 17),(12, 11),(12, 11),
(17, 7),(17, 7),(11, 7),(11, 7),(9, 1)]

import turtle

for ss, point in enumerate(points, 1):
    if ss % 2 == 0:
        turtle.down() # "line to"
    else:
        turtle.up()   # "go to"
    turtle.goto(point)

turtle.done()
