
import turtle

pen = turtle.pen()
pen['pensize'] = 15
pen['pencolor'] = 'green'
turtle.pen(pen)
turtle.forward(100)

turtle.left(90)
turtle.pensize(turtle.pensize() * 2)
turtle.color('red')
turtle.forward(100)

turtle.left(90)
turtle.width(turtle.width()*2)
turtle.color('blue')
turtle.forward(100)

turtle.done()



