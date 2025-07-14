# ex_shape_register_gif.py
import turtle


turtle.register_shape("MyImage.gif")

turtle.shape("MyImage.gif")
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)

turtle.done()

