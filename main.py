import re

def createVis(FEN):
    lines = FEN.split("/")
    boardArray = []
    for row in lines:
        line = re.split(r'(r0|b0|rr|bb|rb|br)', row)
        finished = []
        for x in line:
            if x.isdigit():
                finished.extend([''] * int(x))
            elif x:
                finished.append(x.replace('r0', 'r').replace('b0', 'b'))
        boardArray.append(finished)

    return boardArray

FEN = "r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01"
board = createVis(FEN)
