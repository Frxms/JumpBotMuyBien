import re
from util.engine import getAllMoves


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
            if board[row][column][-1] == turn:
                possibleMoves.append((f"{row}-{column}", move) for move in getAllMoves(row, column, turn, board))
    return possibleMoves


FEN = "r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01 b"
splitted = FEN.split(" ")
turn = splitted[1]
board = createVis(splitted[0])
print(board)
print(board[1][2][-1])
allMoves = calcMove(board, turn)
print(allMoves)

#Formatierung
