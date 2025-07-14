
for ss in range(100):
    print() #  clear the screen

import turtle

data = turtle.textinput("Get String", "Color:")

if data is not None:
    turtle.color(data)
    turtle.write("This is the color!")
    


