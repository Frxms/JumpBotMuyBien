import copy
import re


def generateFEN(boardc, move, turn):  # startingPoints[i][0], startingPoints[i][0], move[0], move[2]
    board = copy.deepcopy(boardc)
    print("Before: ")
    for line in board:
        print(line)
    if len(board[move[0]][move[1]]) == 2:  # wenn turm
        board[move[2]][move[3]] = board[move[0]][move[1]][1]
        board[move[0]][move[1]] = board[move[0]][move[1]][0]
        # Turm wird zu Bauer #TODO: Wie rum? oben geworfen oder unten? darf Turm auf turm schießen
    else:
        board[move[2]][move[3]] = board[move[2]][move[3]] + board[move[0]][move[1]]
        board[move[0]][move[1]] = ""

    print("After: ")
    for line in board:
        print(line)
    FEN_rows = []
    for row in reversed(board):
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
                if len(column) > 1:
                    rows += column
                else:
                    rows += column + "0"
        if empty > 0:
            rows += str(empty)
        FEN_rows.append(rows)
    if turn == "r":
        return "/".join(FEN_rows) + " " + "b"
    else:
        return "/".join(FEN_rows) + " " + "r"

def generateBoard(boardc, move, turn):
    board = copy.deepcopy(boardc)
    if len(board[move[0]][move[1]]) == 2:  # wenn turm
        board[move[2]][move[3]] = board[move[0]][move[1]][1]
        board[move[0]][move[1]] = board[move[0]][move[1]][0]
        # Turm wird zu Bauer #TODO: Wie rum? oben geworfen oder unten? darf Turm auf turm schießen
    else:
        board[move[2]][move[3]] = board[move[2]][move[3]] + board[move[0]][move[1]]
        board[move[0]][move[1]] = ""

    return board

def createVis(FEN):
    boardArray = []
    lines = FEN.split("/")
    for index, row in enumerate(reversed(lines)):
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
