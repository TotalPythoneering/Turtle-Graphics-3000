# MISSION: Solution examples for the Python 3000 educational opportunity.
# STATUS: Public Release
# VERSION: 1.0.0
# NOTES: Code: https://github.com/TotalPythoneering/Turtle-Graphics-3000
# DATE: 2018-07-03 05:16:36
# FILE: DEMO_Chess03_SCALE.py
# AUTHOR: Videos: https://www.youtube.com/playlist?list=PLb_nLwX4CF6g56CUJEEhb5WiDUhU_sTi4
#
import turtle
from LAB_Chess02 import ZBoard as ZBoard

if __name__ == '__main__':
    turtle.title("Python 3000: DEMO_Chess03_SCALE")
    turtle.ht()

    for factor in range(1,5):
        turtle.clear()
        board = ZBoard(w='gold', b='blue', zturtle=turtle)
        board.speed(0)
        board.draw(scale=1/factor)
        input("Input to continue...")

    print("done")
    
    turtle.done()


