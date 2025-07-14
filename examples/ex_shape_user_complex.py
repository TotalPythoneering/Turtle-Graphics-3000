# ex_shape_user_complex.py
import turtle

shape = turtle.Shape("compound")
pointsA = ((30,-30), (0,5), (-30,-30))
pointsB = ((60,-60), (0,10), (-60,-60))
shape.addcomponent(pointsB, "gray", "black")
shape.addcomponent(pointsA, "gold", "green")
turtle.register_shape("MyComplexTriangle", shape)
turtle.shape("MyComplexTriangle")
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)

turtle.done()

