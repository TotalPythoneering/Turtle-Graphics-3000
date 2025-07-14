import turtle
''' NEW: Also adding location & robot visibility concepts '''

class SlowGrid:
    ''' Overlapping rectangles - Very Slow! '''
    @staticmethod
    def draw_square(zturtle, side_len):
        zturtle.down()
        for ss in range(4):
            zturtle.forward(side_len)
            zturtle.left(90)
        zturtle.up()

    @staticmethod
    def slow_row(zturtle, nelem, cell_len):
        for ss in range(nelem):
            SlowGrid.draw_square(zturtle, cell_len)
            zturtle.forward(cell_len)
        zturtle.penup()
        zturtle.left(180)
        zturtle.forward(nelem * cell_len)
        zturtle.left(180)

    @staticmethod
    def draw(zturtle, high, width, box_size):
        for ss in range(high):
            SlowGrid.slow_row(zturtle, width, box_size)
            zturtle.penup()
            zturtle.left(90)
            zturtle.forward(box_size)
            zturtle.right(90)
            zturtle.pendown()
        zturtle.penup()
        zturtle.right(90)
        zturtle.forward(high * box_size)
        zturtle.left(90)


class SnakeGrid:
    ''' Serpentine lines =w= a bounding box: Faster! '''
    @staticmethod
    def draw_rectangle(zturtle, x, y, width, height, border=None, border_pen_size=None):
        # Option A: Option B (below) draws the same.
        adir = zturtle.heading()
        zturtle.up()
        zturtle.home()
        if border:
            zturtle.color(border)
        if border_pen_size:
            zturtle.pensize(border_pen_size)
        zturtle.goto(x, y)
        zturtle.down()
        zturtle.pen(10)
        zturtle.right(90)
        zturtle.forward(width)
        zturtle.right(-90)
        zturtle.forward(height)
        zturtle.right(-90)
        zturtle.forward(width)
        zturtle.right(-90)
        zturtle.forward(height)
        zturtle.up()
        zturtle.setheading(adir)
        zturtle.goto(x, y)

    @staticmethod
    def draw_snake(zturtle, x, y, height, cell_size, xlines, next_angle):
        direct = zturtle.heading()
        zturtle.up()
        zturtle.goto(x, y)
        zturtle.down()

        # Option B
        for yy in range(xlines):
            zturtle.forward(height)
            next_angle = next_angle * -1
            zturtle.right(next_angle)
            zturtle.forward(cell_size)
            zturtle.right(next_angle)

        zturtle.up()
        zturtle.setheading(direct)
        zturtle.goto(x, y)

    @staticmethod
    def draw_grid(zturtle, x, y, width, height, cell_size, border=None, border_pen_size=None):
        direct = zturtle.heading()
        zturtle.setheading(0)
        ylines = int(height / cell_size)
        xlines = int(width / cell_size)
        SnakeGrid.draw_snake(zturtle, x, y, height, cell_size, xlines, -90)
        zturtle.setheading(0)
        zturtle.right(90)
        SnakeGrid.draw_snake(zturtle, x, y, width, cell_size, ylines, 90)
        # SnakeGrid.draw_rectangle(zturtle, x, y, width, height, border=border, border_pen_size=border_pen_size)
        zturtle.setheading(direct)



if __name__ == "__main__":
    turtle.delay(9)
    t1 = turtle.Turtle()
    t1.ht()
    t1.up()
    if False:
        t1.goto(0, -100)
        SlowGrid.draw(t1, 40, 30, 10)
    else:
        SnakeGrid.draw_grid(t1, -200, 200,
                            100, 200, 10,
                            border='brown',
                            border_pen_size=3)

