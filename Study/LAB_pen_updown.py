import turtle

# Draw a dashed line
turtle.title("LAB_pen_updown")
even = True
for seg in range(10, 100, 5):
    if even:
        turtle.penup()
        even = False
    else:
        turtle.pendown()
        even = True
    turtle.forward(12)
turtle.done()

