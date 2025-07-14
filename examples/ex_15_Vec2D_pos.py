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



