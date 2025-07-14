'''
Activity: ShapeMove
Can you move a set of points?

File: LAB_Vector04.py
'''

points = [(9, 1),(7, 7),(7, 7),(1, 7),(1, 7),
(6, 11),(6, 11),(4, 17),(4, 17),(9, 13),
(9, 13),(14, 17),(14, 17),(12, 11),(12, 11),
(17, 7),(17, 7),(11, 7),(11, 7),(9, 1)]

import turtle

pos = (10, -10)
scale = 12.34
for ss, point in enumerate(points, 1):
    if ss % 2 == 0:
        turtle.down() # "line to"
    else:
        turtle.up()   # "go to"
    turtle.goto( pos[0] + (point[0] * scale),
                 pos[1] + (point[1] * scale) * -1)

turtle.done()
