# MISSION: tbd.
# STATUS: tbd.
# VERSION: 1.0.0
# NOTES: tbd.
# DATE: 2018-07-03 05:16:36
# FILE: DEMO_Chess03_SCALE.py
# AUTHOR: tbd.
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


