'''
Activity: draw_vshape
Re-using what we have learned.

File: LAB_DrawVectors.py
'''
import turtle


def draw_vshape(pos, points, scale=3):
    for ss, point in enumerate(points, 1):
        if ss % 2 == 0:
            turtle.down() # "line to"
        else:
            turtle.up()   # "go to"
        turtle.goto( pos[0] + (point[0] * scale),
                     pos[1] + (point[1] * scale) * -1)


from collections import OrderedDict

# Resource: https://github.com/soft9000/PyHershey/
font = None
with open("./symbolic.gsdict") as fh:
    font = eval(fh.readline())

pos = [0, 300]
glyphs = (64, 65, 66, 77, 79)
for which in glyphs:
    pos[0] += 80
    draw_vshape(pos, font[which])
    
turtle.done()


              
