
import turtle

# Common Display
def shape_draw(name, x_pos, y_pos):
    turtle.hideturtle()
    turtle.goto(x_pos, y_pos)
    turtle.shape(name)
    turtle.turtlesize(20, 20, 15)
    turtle.pendown()
    turtle.color('green')
    turtle.pensize(10)
    turtle.fillcolor('gold')
    turtle.showturtle()

# Pre-Defined Shapes
shapes = turtle.getshapes()

# Show Each Shape
for shape in shapes:
    turtle.penup()
    turtle.goto(0, 0)
    shape_draw(shape, 100, 0)
    turtle.textinput("Shape: " + shape, "Click to Continue")

turtle.done()

