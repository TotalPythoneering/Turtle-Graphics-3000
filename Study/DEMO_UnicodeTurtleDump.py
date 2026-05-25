# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-06-21 10:07:36
# FILE: DEMO_UnicodeTurtleDump.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
import turtle

data = ''
for char in range(9812, 9824):
    try:
       data += chr(char) 
    except:
        pass
turtle.goto(-300, 0)
turtle.write(data, font=("Ariel", 48, "normal"))



              
