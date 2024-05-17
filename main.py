import random
import re
from util.engine import getAllMoves
import pydevd_pycharm


def generateFEN(board, move, turn):  # startingPoints[i][0], startingPoints[i][0], move[0], move[2]
    print("Before: ")
    for line in board:
        print(line)
    if len(board[move[0]][move[1]]) == 2:  # wenn turm
        board[move[2]][move[3]] = board[move[0]][move[1]][1]
        board[move[0]][move[1]] = board[move[0]][move[1]][
            0]  # Turm wird zu Bauer #TODO: Wie rum? oben geworfen oder unten? darf Turm auf turm schießen
    else:
        board[move[2]][move[3]] = board[move[2]][move[3]] + board[move[0]][move[1]]
        board[move[0]][move[1]] = ""

    print("After: ")
    for line in board:
        print(line)
    FEN_rows = []
    for row in board:
        rows = ""
        empty = 0
        for column in row:
            if column == "X":
                continue
            elif column == "":
                empty += 1
            else:
                if empty > 0:
                    rows += str(empty)
                    empty = 0
                rows += column + "0"
        if empty > 0:
            rows += str(empty)
        FEN_rows.append(rows)

    return "/".join(FEN_rows) + " " + turn


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
    possibleMoves = []
    startingPoints = []
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] != "" and board[i][j][-1] == turn:
                possibleMoves.append(getAllMoves(i, j, turn, board))
                #print(possibleMoves)
                startingPoints.append([j, i])
    possibleMoves2 = []
    for i, moves in enumerate(possibleMoves):
        for move in moves:  # startingPoints[i][0], startingPoints[i][0], move[0], move[2]
            possibleMoves2.append([startingPoints[i][1], startingPoints[i][0], move[0], move[1]])
            #print(f"{alph[startingPoints[i][0]]}{num[startingPoints[i][1]]} - {move[0]}{move[2]}")
            #print(f"{alph[startingPoints[i][0]]}{num[startingPoints[i][1]]} - {alph[int(move[2])]}{num[int(move[0])]}")
            print(refactor_to_readable(possibleMoves2[-1]))

    return possibleMoves2


def refactor_to_readable(points):
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num = ['8', '7', '6', '5', '4', '3', '2', '1']
    return f"{alph[points[1]]}{num[points[0]]} - {alph[points[3]]}{num[points[2]]}"


if __name__ == "__main__":
    FEN = "r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01 r"  #36 Züge
    a = [['X', '', 'r', 'r', 'r', '', 'r', 'X'], ['', 'r', 'rr', '', 'r', 'r', 'r', ''],
         ['', '', '', 'r', '', '', '', ''], ['', '', 'b', '', '', '', '', ''], ['', '', '', '', 'r', 'b', '', ''],
         ['', '', '', '', '', '', '', ''], ['', 'b', 'b', 'b', 'b', 'b', 'b', ''],
         ['X', '', 'b', 'b', 'b', 'b', '', 'X']]
    FEN2 = "3b02/2b05/1b06/1r0rr2b01/8/5r02/1r0r03b01/3r02 b"  #15 Züge
    splitted = FEN.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    #print(board)
    moves = calcMove(board, turn)
    print(moves)
    chosen_one = random.choice(moves)
    print(refactor_to_readable(chosen_one), chosen_one)
    #print(generateFEN(board, chosen_one, turn))
    print(generateFEN(board, [1, 2, 2, 4], turn))
