import turtle

turtle.title("ex_draw_filled")

def draw_poly(sides, length=50):
    if sides < 1:
        return -1
    zangle = 360/sides
    for side in range(sides):
        turtle.forward(length)
        turtle.right(zangle)
    return zangle

def draw_poly_full(sides, length=50, fill='gold'):
    colors = turtle.color()
    turtle.color(colors[0], fill)
    turtle.begin_fill()
    zangle = draw_poly(sides, length)
    turtle.end_fill()
    # That 'known state' rule:
    turtle.color(colors[0], colors[1])
    return zangle

for value in range(3, 8):
    draw_poly_full(value)

turtle.done()


