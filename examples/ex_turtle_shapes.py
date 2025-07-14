# ex_turtle_shapes.py
import turtle


def jot(str):
    turtle.hideturtle()
    pos = turtle.pos() # save where we are
    turtle.goto(pos[0] - 20, pos[1] - 80)
    turtle.write(str)
    turtle.goto(pos[0], pos[1])
    turtle.showturtle()


# Pre-Defined Shapes
shapes = turtle.getshapes()

turtle.turtlesize(4, 4, 1)
turtle.color('green')
turtle.fillcolor('gold')
turtle.penup()
turtle.goto(-400, -60)
for shape in shapes:
    turtle.forward(100)
    turtle.shape(shape)
    id = turtle.stamp()
    jot(shape + " = " + str(id))

turtle.done()

