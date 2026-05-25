# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-07-12 02:56:28
# FILE: LAB_JosephsSquare_stack2.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
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

