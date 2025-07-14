
import turtle

sides = 3 # Triangle
zangle = 360 / sides
print("Sides #", sides, "angle is", zangle)
for side in range(sides):
    turtle.forward(100)
    turtle.right(zangle)

turtle.done()


