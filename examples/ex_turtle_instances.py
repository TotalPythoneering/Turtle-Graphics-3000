# ex_turtle_shapes.py
import turtle

# ex_turtle_instances
for ss, shape in enumerate(turtle.getshapes()):
    zt = turtle.Turtle()
    zt.up()
    zt.shape(shape)
    zt.forward(30 * ss)


for zt in turtle.turtles():
    zt.color('red')

turtle.done()

