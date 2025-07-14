import turtle

class ZCell:

    @staticmethod
    def goto(zturtle, pos):
        ''' Safe goto '''
        zturtle.up()
        zturtle.goto(pos)
        zturtle.down()


class ZBoard:
    
    ''' Drawing a classic chess / checker game board. '''
    
    def __init__(self, zturtle=turtle.Turtle(), length=500, w='white', b='gray'):
        self.robo = zturtle
        self.length = round(length)
        half = round(self.length/2)
        self.home = (-half, half)
        self.white = w
        self.black = b
        self.scale = 1
        self.robo.ht()
        self.speed()

    def _square(self, pos, length, fill):
        zangle = 90
        hold = self.robo.pos()
        ZCell.goto(self.robo, pos)
        if fill is not None:
            colors = self.robo.color()
            self.robo.color(colors[0], fill)
            self.robo.begin_fill()
        for side in range(4):
            self.robo.forward(length)
            self.robo.right(zangle)
        if fill is not None:
            self.robo.end_fill()
            self.robo.color(colors[0], colors[1])

    def _length(self):
        ''' Calculate & return the scaled / effective length '''
        return round((self.length * self.scale) / 8) + 1
                
    def _draw_checkers(self):
        ZCell.goto(self.robo, self.home)
        cell_length = self._length()
        coord = list(self.home)
        bEven = True
        for zy in range(8):
            for zx in range(8):
                zcolor = self.black
                if bEven:
                    zcolor = self.white
                    bEven = False
                else:
                    zcolor = self.black
                    bEven = True
                self._square(coord, cell_length, zcolor)
                coord[0] += cell_length
            coord[1] -= cell_length
            coord[0] = self.home[0]
            ZCell.goto(self.robo, coord)
            if bEven:
                bEven = False
            else:
                bEven = True
        ZCell.goto(self.robo, self.home)

    def speed(self, speed=0):
        ''' Set the speed for the next rendering. '''
        if speed is 0:
            global turtle
            turtle.tracer()
            turtle.delay(0)
        self.robo.speed(speed)

    def tweak(self, xpos, ypos):
        xpos += 3
        ypos -= 6
        return (xpos, ypos)

    def print(self, x_col, y_col, string):
        offset = self._length()
        pos = self.tweak(self.home[0] + (x_col * offset),
                         self.home[1] - (y_col + 1) * offset)
        ZCell.goto(self.robo, pos)
        self.robo.write(string, font=('Ariel', round(offset * .75), "normal"))
        ZCell.goto(self.robo, self.home)
    
    def draw(self, pos=None, scale=None):
        ''' Main entry point.
        Parameter 'pos' is the x, y coordiante, and
        'scale' is the scaling factor (see below for
        a basic test case - floating point okay.)
        '''
        if pos is not None:
            self.home = pos
        if scale is not None:
            self.scale = scale
        self._draw_checkers()



if __name__ == '__main__':
    turtle.title("Python 3000: LAB_Chess01")
    turtle.ht()
    
    board = ZBoard(w='white', b='gray', length=432)
    board.speed(0)
    board.draw()

    glyphs_white = "♖♘♗♔♕♗♘♖♙"
    glyphs_black = "♜♞♝♚♛♝♞♜♟"

    for col in range(8):
        board.print(col, 1, glyphs_white[8])
        board.print(col, 0, glyphs_white[col])
        board.print(col, 6, glyphs_black[8])
        board.print(col, 7, glyphs_black[col])
        
    turtle.done()


