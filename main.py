import re
from util.models import get_all_moves


def createVis(FEN):
    boardArray = []
    lines = FEN.split("/")
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

def calcMove(board, turn):
    possibleMoves = []
    for row in board:
        for column in row:
            possibleMoves.append(move for move in get_all_moves(row, column, turn, board))
    return possibleMoves


# check ob rechts-unten eine Figur steht
def diaCalc(turn, row, cIndex):
    if(turn == "r"):
        if row[cIndex] == "b" or row[cIndex] == "rb":
            return True
        else:
            return False
    elif(turn == "b"):
        if row[cIndex] == "r" or row[cIndex] == "br":
            return True
        else:
            return False


FEN = "r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01 b"
splitted = FEN.split(" ")
turn = splitted[1]
board = createVis(splitted[0])
allMoves = calcMove(board, turn)
print(allMoves)
