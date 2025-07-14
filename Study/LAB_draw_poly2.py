
import turtle

turtle.title("LAB_draw_poly2")
def draw_poly(sides, length=50):
    if sides < 1:
        return -1
    zangle = 360/sides
    for side in range(sides):
        turtle.forward(length)
        print(turtle.pos())
        turtle.right(zangle)
    return zangle

draw_poly(3)

turtle.done()


