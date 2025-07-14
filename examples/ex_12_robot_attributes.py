import turtle

# Default Robot Location
print(turtle.pos())
# Default Orientation
print(turtle.heading())
turtle.right(90)
print("NOW:", turtle.heading())

# Show the Pen's Attributes
pen = turtle.pen()
for ref in pen:
    print(ref, pen[ref])

