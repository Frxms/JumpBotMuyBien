import re

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
            from util.models import get_all_moves
            get_all_moves(row, column, turn)
            if turn == "r":
                if column == "br":      # Türme
                    if row.index == 0:
                        possibleMoves.append([row.index + 2, column.index])
                        possibleMoves.append([row.index + 2, column.index + 2])
                        if column.index == 0:
                            possibleMoves.append([row.index + 1, column.index + 3])
                        elif column.index - 1 == len(row):
                            possibleMoves.append([row.index + 1, column.index - 1])
                        else:
                            possibleMoves.append([row.index + 1, column.index - 1])
                            possibleMoves.append([row.index + 1, column.index + 3])
                    elif row.index == 5:
                        if column.index <= 1:
                            possibleMoves.append([row.index + 2, column.index])
                            possibleMoves.append([row.index + 1, column.index + 2])
                        elif column.index >= 6:
                            possibleMoves.append([row.index + 1, column.index - 2])
                            possibleMoves.append(([row.index + 2, column.index - 2]))
                    elif row.index == 6:
                        if column.index <= 2:
                            possibleMoves.append([row.index + 1, column.index + 1])
                        elif column.index >= 5:
                            possibleMoves.append([row.index + 1, column.index - 3])
                        else:
                            possibleMoves.append([row.index + 1, column.index + 1])
                            possibleMoves.append([row.index + 1, column.index - 3])
                    else:
                        if column.index == 1:
                            possibleMoves.append([row.index + 2, row.index - 1])
                            possibleMoves.append([row.index + 2, row.index + 1])
                            possibleMoves.append([row.index + 1, row.index + 2])
                        elif column.index <= 0:
                            possibleMoves.append([row.index + 2, row.index + 1])
                            possibleMoves.append([row.index + 1, row.index + 2])
                        elif column.index == 6:
                            possibleMoves.append([row.index + 2, row.index + 1])
                            possibleMoves.append([row.index + 2, row.index - 1])
                            possibleMoves.append([row.index + 1, row.index - 2])
                        elif column.index - 1 >= len(row):
                            possibleMoves.append([row.index + 2, row.index - 1])
                            possibleMoves.append([row.index + 1, row.index - 2])
                        else:
                            possibleMoves.append([row.index + 2, row.index + 1])
                            possibleMoves.append([row.index + 2, row.index - 1])
                            possibleMoves.append([row.index + 1, row.index + 2])
                            possibleMoves.append([row.index + 1, row.index - 2])

                elif column == "r":     # normaler Läufer
                    # check if the column is on the edge of the board
                    if not column.index - 1 < 0:
                        possibleMoves.append([row.index, column.index - 1])      # nach links
                    elif not column.index + 1 >= len(row):
                        possibleMoves.append([row.index, column.index + 1])     # nach rechts
                    # andere Regelungen bei der ersten und letzten Reihe
                    if row.index == 0:
                        possibleMoves.append([row.index + 1, column.index + 1])  # normaler Zug
                        possibleMoves.append([row.index + 1, column.index + 2])  # zum Schlagen ru
                        possibleMoves.append([row.index + 1, column.index])      # zum Schlagen lu
                    elif row.index == 6:
                        if column.index != 0 or column.index != 7:
                            possibleMoves.append([row.index + 1, column.index - 1])  # normaler Zug
                        elif diaCalc(turn, board[row.index + 1], column.index):
                            possibleMoves.append([row.index + 1, column.index])      # zum Schlagen ru
                        elif diaCalc(turn, board[row.index + 1], column.index - 2):
                            possibleMoves.append([row.index + 1, column.index - 2])  # zum Schlagen lu
                    else:
                        possibleMoves.append([row.index + 1, column.index])
                        possibleMoves.append([row.index + 1, column.index + 1])
                        possibleMoves.append([row.index + 1, column.index - 1])

            elif turn == "b":
                if column == "rb":  # Türme
                    pass
                elif column == "b": # normaler Läufer
                # check if the column is on the edge of the board
                    if not column.index - 1 < 0:
                        possibleMoves.append([row.index,column.index - 1])  # man kann nach rechts oder links wenn dort eine andere Fabre steht
                    elif not column.index + 1 >= len(row):
                        possibleMoves.append([row.index, column.index + 1])
                        # andere Regelungen bei der ersten und letzten Reihe
                    if row.index == 7:
                        possibleMoves.append([row.index - 1, column.index + 1])  # normaler Zug
                        possibleMoves.append(row.index - 1, column.index + 2)  # zum Schlagen ro
                        possibleMoves.append([row.index - 1, column.index])  # zum Schlagen lo
                    elif row.index == 1:
                        if column.index != 0 or column.index != 7:
                            possibleMoves.append([row.index - 1, column.index - 1])  # normaler Zug
                        elif diaCalc(turn, board[row.index - 1], column.index):
                            possibleMoves.append([row.index - 1, column.index])  # zum Schlagen ru
                        elif diaCalc(turn, board[row.index - 1], column.index - 2):
                            possibleMoves.append([row.index - 1, column.index - 2])  # zum Schlagen lu
                    else:
                        possibleMoves.append([row.index - 1, column.index])
                        possibleMoves.append([row.index - 1, column.index + 1])
                        possibleMoves.append([row.index - 1, column.index - 1])

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
