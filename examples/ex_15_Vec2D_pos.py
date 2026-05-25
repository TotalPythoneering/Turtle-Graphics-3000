# MISSION: Examples from the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-08-09 05:18:34
# FILE: ex_15_Vec2D_pos.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
import turtle

# Arbitrary floating point location
turtle.goto(11.631, -12.116)

# Returns a 'turtle.Vec2D'
zPos = turtle.pos()
print("1.1", "Result ISA ", type(zPos))
# Floating Point Results, Okay (alias rounding)!
print("1.2",zPos, "(rounding)")

turtle.setpos(12.345, -12.111119)
print("1.3",turtle.pos(), "(again, rounding)")

turtle.done()



