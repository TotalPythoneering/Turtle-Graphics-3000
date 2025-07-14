import turtle

def draw_line(pos, length, color):
    turtle.up()
    hold = turtle.color()
    turtle.color(color)
    turtle.goto(pos)
    turtle.down()
    turtle.forward(length)
    turtle.color(hold[0])

def draw_ruler(side):
    default = turtle.width()
    turtle.width(3)
    draw_line((0, side), side*3, "blue")
    draw_line((0, 0), side*3, "green")
    draw_line((0, side* 0.28), side * 3, 'red')
    turtle.width(default)
    turtle.left(90)
    for ss in range(4):
        draw_line((side*ss, 0), side, "lightgray")
    turtle.up()
    turtle.home()

turtle.ht();turtle.up()
turtle.title("DEMO_font_box")

glyph = 'p' # chr(9812)
side = 100
point = (0,0)

draw_ruler(side)

turtle.up();turtle.goto(point)
for face in ('Ariel', 'Times', 'Courier'):
    turtle.write(glyph, font=(face, side, 'normal'))
    turtle.down();turtle.forward(side)

turtle.done()



              
