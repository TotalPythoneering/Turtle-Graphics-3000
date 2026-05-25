# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-07-02 10:03:20
# FILE: SETUP_DrawVectors.py
# AUTHOR: tbd.
#
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
    



              
