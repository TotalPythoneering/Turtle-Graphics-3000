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


