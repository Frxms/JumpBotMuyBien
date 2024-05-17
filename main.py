import re
from util.engine import getAllMoves
import pydevd_pycharm


def createVis(FEN):
    boardArray = []
    lines = FEN.split("/")
    for index, row in enumerate(lines):
        line = re.split(r'(r0|b0|rr|bb|rb|br)', row)
        finished = []
        for index2, x in enumerate(line):
            if index == 0:
                if index2 == 0:
                    finished.append('X')
            elif index == 7:
                if index2 == 0:
                    finished.append('X')
            if x.isdigit():
                finished.extend([''] * int(x))
            elif x:
                finished.append(x.replace('r0', 'r').replace('b0', 'b'))
            if index == 0:
                if index2 == len(line) - 1:
                    finished.append('X')
            elif index == 7:
                    if index2 == len(line) - 1:
                        finished.append('X')
        boardArray.append(finished)
    return boardArray


def calcMove(board, turn):
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    possibleMoves = []
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] != "" and board[i][j][-1] == turn:
                possibleMoves.append(getAllMoves(i, j, turn, board))
                print(possibleMoves)
                for moves in possibleMoves:
                    for move in moves:
                        print(f"{alph[int(j)]}{int(i)} - {alph[move[1]], move[0]}")
                #possibleMoves.extend([f"{int(i)}-{int(j)}, {move}" for move in getAllMoves(i, j, turn, board)])
                # possibleMoves.append(f"{int(i)}-{int(j)} :: {getAllMoves(i, j, turn, board)}")
                #.append(f"{int(i)}-{int(j)}, {move}" for move in getAllMoves(i, j, turn, board))
    return possibleMoves

#try:
FEN = "r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01 r"
splitted = FEN.split(" ")
turn = splitted[1]
board = createVis(splitted[0])
print(board)
print(calcMove(board, turn))
# except Exception as e:
#     print(f"An exception occurred: {e}")
#     pydevd_pycharm.settrace('localhost', port=12345, stdoutToServer=True, stderrToServer=True, suspend=True)
#     raise


