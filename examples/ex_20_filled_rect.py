''' From squares, to rectangles '''

color   = 'green'
pos     = (-150, 0) 
extents = (200,100)

import turtle as robot

robot.goto(pos)
for line in range(2):
    robot.forward(extents[0])
    robot.left(90)
    robot.forward(extents[1])
    robot.left(90)

robot.done()




