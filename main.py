import copy
import random
import re
from util.engine import getAllMoves
from util.search import Tree, Node


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


def calcMove(board, turn, readable=False):
    possibleMoves = []
    startingPoints = []
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if board[i][j] != "" and board[i][j][-1] == turn:
                possibleMoves.append(getAllMoves(i, j, turn, board))
                #print(possibleMoves)
                startingPoints.append([j, i])
    possibleMoves2 = []
    readableMoves = []
    for i, moves in enumerate(possibleMoves):
        for move in moves:  # startingPoints[i][0], startingPoints[i][0], move[0], move[2]
            possibleMoves2.append([startingPoints[i][1], startingPoints[i][0], move[0], move[1]])
            #print(refactor_to_readable(possibleMoves2[-1]))
            readableMoves.append(refactor_to_readable(possibleMoves2[-1]))

    if readable:
        return readableMoves

    return possibleMoves2


def refactor_to_readable(points):
    alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    num = ['8', '7', '6', '5', '4', '3', '2', '1']
    return f"{alph[points[1]]}{num[points[0]]}-{alph[points[3]]}{num[points[2]]}"


def perfTest():
    import time
    fen = "b01b0b01b0/1b0bb1b0b0b01/3b04/2r05/4b0r02/8/1r0r0r0r0r0r01/1r0r0r0r01 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"early Game took: {elapsed_time} seconds")

    fen = "b02b01b0/3b01b02/b02b02b01/b01b05/5r02/1r02r02r0/2rrr02r01/r03r01 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"mid Game took: {elapsed_time} seconds")

    fen = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
    splitted = fen.split(" ")
    turn = splitted[1]
    start_time = time.time()
    for i in range(1000):
        calcMove(createVis(splitted[0]), turn, True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"end Game took: {elapsed_time} seconds")


def test():
    # r01r0r01r0/1r0rr1r0r0r01/3r04/2b05/4r0b02/8/1b0b0b0b0b0b01/1b0b0b0b01 r
    FEN1 = "1b04/2b03b01/b01rr5/r02b01b02/1b06/1r02b03/8/1r01r0r0r0 b"  # 36 Züge
    FEN2 = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
    FEN3 = "3b02/2b05/1b06/1r0rr2b02/8/5r02/1r0r03b01/3r02 b"
    a = [['X', '', 'r', 'r', 'r', '', 'r', 'X'], ['', 'r', 'rr', '', 'r', 'r', 'r', ''],
         ['', '', '', 'r', '', '', '', ''], ['', '', 'b', '', '', '', '', ''], ['', '', '', '', 'r', 'b', '', ''],
         ['', '', '', '', '', '', '', ''], ['', 'b', 'b', 'b', 'b', 'b', 'b', ''],
         ['X', '', 'b', 'b', 'b', 'b', '', 'X']]
    splitted = FEN3.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    # print(board)
    moves = calcMove(board, turn)
    print(moves)
    # chosen_one = random.choice(moves)
    # print(refactor_to_readable(chosen_one), chosen_one)
    # print(generateFEN(board, chosen_one, turn))
    # print(generateFEN(board, chosen_one, turn))
    for move in moves:
        print(f"this move: {move}")
        print(f"was converted to: {refactor_to_readable(move)}")
        print(generateFEN(board, move, turn))
    perfTest()

def recEndgame(moves, turn):
    endgame = []
    for move in moves:
        if turn == "r":
            if move[3] == "0":
                endgame.append(True)
            else:
                endgame.append(False)

        elif turn == "b":
            if move[3] == "7":
                endgame.append(True)
            else:
                endgame.append(False)

    return endgame


def allMovesFEN(fen):
    splitted = fen.split(" ")
    turn = splitted[1]
    board = createVis(splitted[0])
    moves = calcMove(board, turn)
    fenList = []
    for move in moves:
        fenList.append(generateFEN(board, move, turn))
    return fenList

def createTree(fen):
    fenBoards = allMovesFEN(fen)
    tree = Tree(Node(move=fen))
    for fenStr in fenBoards:
        node = Node(fenStr)
        tree.insert(fen, node)


if __name__ == "__main__":
    fen = "6/rr7/6r01/8/8/8/b0b0b05/6 r"
    test()

