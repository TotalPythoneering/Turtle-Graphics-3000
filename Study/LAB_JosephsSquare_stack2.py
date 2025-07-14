import turtle

colors = ("red", "black", "gold", "green")

def josephs_square(xcord, ycord, width):
    from StateSaver2 import State
    stack = State()
    stack.push()
    turtle.pensize(10)
    turtle.penup();turtle.goto(xcord, ycord)
    turtle.pendown()
    for index in range(4):
        turtle.color(colors[index])
        turtle.left(90)
        turtle.forward(width)
    stack.pop()


josephs_square(100, 100, 50)
josephs_square(-100, 100, 50)
josephs_square(100, -100, 50)
josephs_square(-100, -100, 50)


# Same as .done()
turtle.mainloop()

