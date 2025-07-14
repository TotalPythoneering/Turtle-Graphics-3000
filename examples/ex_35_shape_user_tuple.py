
import turtle

turtle.register_shape("MyTriangle", ((30,-30), (0,5), (-30,-30)))
turtle.shape("MyTriangle")
turtle.color('aqua') # color our shape
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)



turtle.done()

