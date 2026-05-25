# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_shape_register_gif.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
# ex_shape_register_gif.py
#
import turtle


turtle.register_shape("MyImage.gif")

turtle.shape("MyImage.gif")
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)

turtle.done()

