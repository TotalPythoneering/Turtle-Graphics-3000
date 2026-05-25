# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:19:26
# FILE: ex_35_shape_user_tuple.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

import turtle

turtle.register_shape("MyTriangle", ((30,-30), (0,5), (-30,-30)))
turtle.shape("MyTriangle")
turtle.color('aqua') # color our shape
turtle.stamp()

for shape in turtle.getshapes():
    print("got " + shape)



turtle.done()

