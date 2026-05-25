# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-06-21 10:07:36
# FILE: DEMO_UnicodeTurtleDump.py
# AUTHOR: tbd.
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



              
