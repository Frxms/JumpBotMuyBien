import random
import re
from util.engine import getAllMoves
import pydevd_pycharm


def generateFEN(board, move, turn):
    letter_to_index = {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6,
        "H": 7
    }
    move = move.split(" - ")
    move[0] = move[0].replace(move[0][0], str(letter_to_index[move[0][0]]))
    move[1] = move[1].replace(move[1][0], str(letter_to_index[move[1][0]]))
    board[int(move[0][0])][int(move[0][1]) + 1] = ""
    board[int(move[1][0])][int(move[1][1]) + 1] = turn + str(board[int(move[1][0])][int(move[1][1])])
    print(board)
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
                print(possibleMoves)
                startingPoints.append([j, i])
    possibleMoves2 = []
    for i, moves in enumerate(possibleMoves):
        for move in moves:  # startingPoints[i][0-1] move[0]move[2]
            #print(f"{alph[startingPoints[i][0]]}{num[startingPoints[i][1]]} - {move[0]}{move[2]}")
            #print(f"{alph[startingPoints[i][0]]}{num[startingPoints[i][1]]} - {alph[int(move[2])]}{num[int(move[0])]}")
            print(refactor_to_readable(startingPoints, i, move))

    return possibleMoves


def refactor_to_readable(startingPoints, index, move):
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num = ['8', '7', '6', '5', '4', '3', '2', '1']
    return f"{alph[startingPoints[index][0]]}{num[startingPoints[index][1]]} - {alph[int(move[2])]}{num[int(move[0])]}"


if __name__ == "__main__":
    FEN = "1r0r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01 b"  #36 Züge
    a = [['X', '', 'r', 'r', 'r', '', 'r', 'X'], ['', 'r', 'rr', '', 'r', 'r', 'r', ''],
         ['', '', '', 'r', '', '', '', ''], ['', '', 'b', '', '', '', '', ''], ['', '', '', '', 'r', 'b', '', ''],
         ['', '', '', '', '', '', '', ''], ['', 'b', 'b', 'b', 'b', 'b', 'b', ''],
         ['X', '', 'b', 'b', 'b', 'b', '', 'X']]
    print(generateFEN(a, "C5 - C6", "r"))
    FEN2 = "3b02/2b05/1b06/1r0rr2b01/8/5r02/1r0r03b01/3r02 b"  #15 Züge
    splitted = FEN.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    print(board)
    calcMove(board, turn)
