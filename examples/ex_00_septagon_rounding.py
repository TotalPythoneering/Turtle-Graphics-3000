
import turtle

def draw_poly(sides, length=50):
    if sides < 1:
        return -1
    zangle = 360/sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(zangle)
    return zangle

angle = draw_poly(7)
print("angle is", angle)

turtle.done()


