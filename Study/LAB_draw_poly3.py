
import turtle

turtle.title("LAB_draw_poly3")
def draw_poly(sides, length=50):
    if sides < 1:
        return -1
    zangle = 360/sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(zangle)
    return zangle

input("")

# Note: Zero is FASTEST!
bfirst = True
print("Default Speed:", turtle.speed())
for value in range(20):
    turtle.speed(value)
    if turtle.speed() == 0 and not bfirst:
        print("Max Speed:", value - 1)
        break
    print("Speed:", turtle.speed())
    draw_poly(20)
    bfirst = False

turtle.done()


