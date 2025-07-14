import turtle

turtle.title("LAB_CartesianCross.py")
lines = {'red':10, 'green':15, 'blue':10, 'gold':5}
for line in  lines:
    turtle.color(line)
    turtle.pensize(lines[line])
    turtle.forward(100)
    turtle.backward(100)
    turtle.left(90)

turtle.textinput("Click to continue", "")

# Bonus
turtle.home()
turtle.pensize(3)
turtle.penup()
turtle.goto(-12, -12)
turtle.color('black')
turtle.pendown()
for line in range(4):
    turtle.forward(25)
    turtle.left(90)

turtle.done()
