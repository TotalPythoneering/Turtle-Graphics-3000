# ex_settiltangle.py
import turtle as xform

xform.setup(width=600, height=200, startx=820, starty=350)
xform.shape("turtle")
xform.up();xform.goto(-200,0)
xform.shapesize(4,4,3)
xform.fillcolor("white")
for ref in range(360):
    xform.settiltangle(ref)
    # xform.tilt(ref) # additive change - spin factors =)
    xform.forward(1)
    if ref % 5 == 0:
        xform.stamp()

xform.mainloop()


