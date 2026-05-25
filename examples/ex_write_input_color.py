# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:58
# FILE: ex_write_input_color.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#

for ss in range(100):
    print() #  clear the screen

import turtle

data = turtle.textinput("Get String", "Color:")

if data is not None:
    turtle.color(data)
    turtle.write("This is the color!")
    


