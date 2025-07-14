import turtle

turtle.title("DEMO_font_size")
turtle.ht()

glyph = chr(9812) # chr(0x798F)
side = 100; seg = 5
point = (-side, side)

turtle.up();turtle.goto(point);turtle.down()

for sz in range(4):
    bEven = True
    for ref in range(0, side, seg):
        turtle.forward(seg)
        if bEven:
            bEven = False
            turtle.up()
        else:
            bEven = True
            turtle.down()
    turtle.left(90)

font='Times'
turtle.up(); turtle.goto(point)
turtle.color("lightgray")
turtle.write(glyph, font=(font, side, 'normal'))
turtle.goto(point[0]* 1.114, point[1] * 0.725)
turtle.color("red")
turtle.write(glyph, font=(font, side, 'normal'))

turtle.done()



              
