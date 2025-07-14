''' From squares, to rectangles '''

color   = 'blue'
pos     = (-150, 0) 
extents = (200,100)

import turtle as robot

robot.pensize(5)
robot.goto(pos)
robot.pencolor(color)   # Pen (same as .color())
robot.fillcolor('gold')  # New!
robot.begin_fill()
for line in range(2):
    robot.forward(extents[0])
    robot.left(90)
    robot.forward(extents[1])
    robot.left(90)
robot.end_fill()
robot.textinput("Proof:", robot.color())  # Effect

robot.done()




