import turtle

turtle.title("LAB_JosephsSquare")
colors = ("red", "black", "gold", "green")

def josephs_square(xcord, ycord, width):
    hcolor = turtle.color()     # save
    pos = turtle.pos()          # save
    hold = turtle.width()       # save
    turtle.pensize(10)
    turtle.penup();turtle.goto(xcord, ycord)
    turtle.pendown()
    for index in range(4):
        turtle.color(colors[index])
        turtle.left(90)
        turtle.forward(width)
    turtle.penup()
    turtle.color(hcolor[0])     # restore
    turtle.goto(pos[0], pos[1]) # restore
    turtle.width(hold)          # restore
    turtle.pendown()

josephs_square(100, 100, 50)
josephs_square(-100, 100, 50)
josephs_square(100, -100, 50)
josephs_square(-100, -100, 50)


# Same as .done()
turtle.mainloop()

