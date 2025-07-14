
import turtle


turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()
turtle.begin_poly()
turtle.pensize("10")
turtle.color("blue")
for seg in range(10, 100, 5):
    turtle.left(45)
    turtle.forward(seg)
turtle.end_poly()

print(turtle.getscreen())
# Tkinter Canvas:
can = turtle.getscreen().getcanvas()
can.postscript(file = "turtle.eps")

turtle.done()

