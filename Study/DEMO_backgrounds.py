# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2021-10-03 06:21:04
# FILE: DEMO_backgrounds.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
import turtle as robot

robot.bgcolor("#ffcc04")

robot.textinput("Click to continue", "")
robot.setup(1024, 768)      # Window size
robot.screensize(800, 600)  # Where SCROLL BARS appear
print("1.1", robot.screensize())
robot.bgpic("TreasureCoin.png")  # Background image
print("1.2", robot.screensize())

robot.done()


