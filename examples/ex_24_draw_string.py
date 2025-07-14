
import turtle as robot

ref = robot.numinput('Press Cancel To Quit', "Rectangle Size?")
if ref is not None:
    color = robot.textinput('Press Cancel To Quit', "Rectangle Color?")
    if color is not None:
        robot.penup()
        robot.goto(-300, 200)
        font = ("Times", 24, "bold")
        robot.write("You entered: " + str(ref) +", " + color, font=font)

robot.done()

