# Lab: SpotOn

import turtle

spot=300
turtle.speed(9)
default = turtle.pensize()

# Core:
turtle.penup()
turtle.goto(0, spot * -1)
turtle.pendown()
turtle.width(7)
turtle.fillcolor('gray')
turtle.begin_fill()
turtle.circle(spot)
turtle.end_fill()

turtle.penup()
turtle.home()
turtle.pensize(12)
turtle.penup()
turtle.goto(spot * -1, spot * -1)
turtle.color('black')
turtle.pendown()
for line in range(4):
    turtle.forward(spot * 2)
    turtle.left(90)

turtle.penup()
turtle.home()


# Coin
turtle.pensize(default)
half=spot/4;tweak=(25, 50)
turtle.dot(spot, 'lightgray')
treasure = chr(0x5B9D) # chr(9815) 
turtle.goto(half * -1 - tweak[0], (half * -1) - tweak[1])
turtle.write(treasure, font=('Ariel', round(spot/2), 'normal'))
print(treasure)
turtle.ht()

turtle.done()


