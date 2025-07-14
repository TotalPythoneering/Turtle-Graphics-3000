
# Turtle Graphics in Python 3
import turtle

# .home() <> .goto(0,0)
for line in range(4):
    turtle.left(90)
    turtle.forward(100)
    turtle.goto(0,0)

# Same as mainloop()
turtle.done()


