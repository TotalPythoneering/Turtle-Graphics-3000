# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2021-10-03 06:21:04
# FILE: DEMO_backgrounds.py
# AUTHOR: tbd.
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


