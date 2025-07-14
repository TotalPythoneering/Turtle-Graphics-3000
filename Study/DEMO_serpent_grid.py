import turtle

def draw_grid(zturtle, width, height, cell_size, border=None, border_pen_size=None):
    ylines = int(height / cell_size)
    xlines = int(width / cell_size)
    # y serpentines
    zturtle.home()
    next_angle = -90
    for yy in range(xlines):
        zturtle.forward(height)
        next_angle = next_angle * -1
        zturtle.right(next_angle)
        zturtle.forward(cell_size)
        zturtle.right(next_angle)
    # x serpentines
    zturtle.home()
    next_angle = 90
    zturtle.right(next_angle)
    for xx in range(ylines):
        zturtle.forward(width)
        next_angle = next_angle * -1
        zturtle.right(next_angle)
        zturtle.forward(cell_size)
        zturtle.right(next_angle)
    # Outer Box
    zturtle.home()
    if border is not None:
        zturtle.color(border)
    if border_pen_size is not None:
        zturtle.pensize(border_pen_size)
    zturtle.pen(10)
    zturtle.right(90)
    zturtle.forward(width)
    zturtle.right(-90)
    zturtle.forward(height)
    zturtle.right(-90)
    zturtle.forward(width)
    zturtle.right(-90)
    zturtle.forward(height)
    zturtle.home()


if __name__ == "__main__":
    draw_grid(turtle, 100, 200, 10, border='green', border_pen_size=3)
