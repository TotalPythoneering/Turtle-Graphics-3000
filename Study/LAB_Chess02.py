import turtle

class ZCell:
    ''' A self-contained, 'tweekable' cell on ZBoard '''
    def __init__(self, x_pos, y_pos, length):
        self.x = x_pos
        self.y = y_pos
        self.length = length

    @staticmethod
    def goto(zturtle, pos):
        ''' Safe goto '''
        zturtle.up()
        zturtle.goto(pos)
        zturtle.down()
        
    def print(self, zturtle, string, zfont=('Ariel', 60, 'normal'), tweak=None):
        ''' Designed for a SINGLE character. '''
        hold = zturtle.pos()
        zfont = list(zfont)
        zfont[1] = round(self.length * 0.7)
        if tweak is not None:
            ZCell.goto(zturtle, tweak(self.x, self.y - zfont[1]))
        else:
            ZCell.goto(zturtle, (self.x, self.y - zfont[1]))
        zturtle.write(string, font=zfont)
        ZCell.goto(zturtle, hold)
        
    def draw(self, zturtle, fill=None):
        ''' Draw the cell, with an optional color. '''
        zangle = 90
        hold = zturtle.pos()
        ZCell.goto(zturtle, (self.x, self.y))
        if fill is not None:
            colors = zturtle.color()
            zturtle.color(colors[0], fill)
            zturtle.begin_fill()
        for side in range(4):
            zturtle.forward(self.length)
            zturtle.right(zangle)
        if fill is not None:
            zturtle.end_fill()
            zturtle.color(colors[0], colors[1])
        

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

    def locate(self, x_col, y_col):
        ''' Return ZCell from a zero-based, 8 x 8, cell coordinate '''
        factor = self._length()
        return ZCell(
            self.home[0] + (factor * x_col),
            self.home[1] - (factor * y_col),
            factor
            )
    
    def draw(self, pos=None, scale=None):
        ''' Main entry point.
        Parameter 'pos' is the x, y coordiante, and
        'scale' is the scaling factor.
        '''
        if pos is not None:
            self.home = pos
        if scale is not None:
            self.scale = scale
        self._draw_checkers()


def ChessFixup(xpos, ypos):
    xpos += 3
    ypos -= 28
    return (xpos, ypos)

def Fixup(xpos, ypos):
    xpos += 13
    ypos -= 28
    return (xpos, ypos)


if __name__ == '__main__':
    turtle.title("Python 3000: LAB_Chess02")
    turtle.ht()
    
    board = ZBoard(w='gold', b='blue')
    board.speed(0)
    board.draw()

    points = ((3,3, 'red'),(4,4, 'white'))
    '''for point in points:
        cell = board.locate(point[0], point[1])
        cell.draw(turtle, point[2])
        cell.print(turtle, 'X', tweak=Fixup)
    '''
    glyphs_white = "♖♘♗♔♕♗♘♖♙"
    glyphs_black = "♜♞♝♚♛♝♞♜♟"

    for col in range(8):
        turtle.color('white')
        board.locate(col, 1).print(turtle, glyphs_white[8], tweak=ChessFixup)
        board.locate(col, 0).print(turtle, glyphs_white[col], tweak=ChessFixup)
        turtle.color('black')
        board.locate(col, 6).print(turtle, glyphs_black[8], tweak=ChessFixup)
        board.locate(col, 7).print(turtle, glyphs_black[col], tweak=ChessFixup)
        
    turtle.done()


