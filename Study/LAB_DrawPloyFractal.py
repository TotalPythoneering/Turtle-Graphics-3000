import turtle

last = turtle.home()
turtle.setup(800, 600)
turtle.title("LAB_DrawPloyFractal")
turtle.setworldcoordinates(0,0,400,600)

def plot_fractal(z, zFloat, scale=7):
    if False:
        if round(zFloat) == int(zFloat):
            return False
    x = round(zFloat)
    y = abs(round((zFloat - x) * 100))
    global last
    this = (x, y)
    if this == last:
        return True # No need to plot twice?
    print("Point:", z, x, y, (zFloat))
    turtle.goto(x * scale, y * scale)
    last = this
    return True

def calc_poly(sides):
    if sides < 1:
        return -1
    zangle = 360/sides
    return zangle

iFrac = 0
turtle.up()
for z in range(1, 360):
    angle = calc_poly(z)
    bFrac = plot_fractal(z, angle)
    if bFrac:
        iFrac += 1
    if z is 1:
        turtle.down()

print("There are", iFrac, "valid points")

turtle.mainloop()



