'''
Activity: draw_vshape
Re-using what we have learned.

File: SETUP_DrawVectors.py
'''
import turtle


def draw_vshape():
    pass # TODO: Copy code here.


from collections import OrderedDict

# Resource: https://github.com/soft9000/PyHershey/
font = None
with open("./symbolic.gsdict") as fh:
    font = eval(fh.readline())


glyphs = (64, 65, 66, 77, 79)
for ss, which in enumerate(glyphs, 1):
    draw_vshape() # TODO: what goes here?
    



              
