import turtle as robot

def draw_rect(pos, extents):
    pass

def draw_filled_rect(pos, extents, color=None):
    pass   

if __name__ == '__main__': 
    size = [100,100]
    draw_filled_rect((-150, 0), size, 'red')
    draw_filled_rect((0, 0), size, 'green')
    draw_filled_rect((0, 150), size, 'blue')

    robot.done()




