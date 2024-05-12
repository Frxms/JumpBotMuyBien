from main import diaCalc


class Spielstein:
    def __init__(self, farbe, farbe2=None, isWhopper=False):
        self.isWhopper = isWhopper
        self.farbe = farbe
        if isWhopper:
            self.farbe2 = farbe2

    def __str__(self):
        if self.isWhopper:
            return self.farbe + self.farbe2
        else:
            return self.farbe

    def __repr__(self):
        if self.isWhopper:
            return self.farbe + self.farbe2
        else:
            return self.farbe


def get_all_moves(row, field, turn, board):
    possibleMoves = []
    r = 0
    c = 0
    s = 0
    if turn == "r":
        c = 0
        r = 6
        s = 1
    elif turn == "b":
        c = 7
        r = 1
        s = -1
#---------------------------------------------------------------------------------------------

    if field.isWhopper:
        # todo: to make it usable for both colors, use (0,5,6) for blue / (7, 2, 1) for red
        # todo: bei jedem Zug checken, ob da ein Turm der selben Farbe steht
        # when in first row
        if row.index == 0:
            possibleMoves.append([row.index + 2, field.index])
            possibleMoves.append([row.index + 2, field.index + 2])
            if field.index == 0:
                possibleMoves.append([row.index + 1, field.index + 3])
            elif field.index - 1 == len(row):
                possibleMoves.append([row.index + 1, field.index - 1])
            else:
                possibleMoves.append([row.index + 1, field.index - 1])
                possibleMoves.append([row.index + 1, field.index + 3])
        # when in row 5
        elif row.index == 5:
            if field.index <= 1:
                possibleMoves.append([row.index + 2, field.index])
                possibleMoves.append([row.index + 1, field.index + 2])
            elif field.index >= 6:
                possibleMoves.append([row.index + 1, field.index - 2])
                possibleMoves.append(([row.index + 2, field.index - 2]))
        # when in row 6
        elif row.index == 6:
            if field.index <= 2:
                possibleMoves.append([row.index + 1, field.index + 1])
            elif field.index >= 5:
                possibleMoves.append([row.index + 1, field.index - 3])
            else:
                possibleMoves.append([row.index + 1, field.index + 1])
                possibleMoves.append([row.index + 1, field.index - 3])
        else:
            if field.index == 1:
                possibleMoves.append([row.index + 2, row.index - 1])
                possibleMoves.append([row.index + 2, row.index + 1])
                possibleMoves.append([row.index + 1, row.index + 2])
            elif field.index <= 0:
                possibleMoves.append([row.index + 2, row.index + 1])
                possibleMoves.append([row.index + 1, row.index + 2])
            elif field.index == 6:
                possibleMoves.append([row.index + 2, row.index + 1])
                possibleMoves.append([row.index + 2, row.index - 1])
                possibleMoves.append([row.index + 1, row.index - 2])
            elif field.index - 1 >= len(row):
                possibleMoves.append([row.index + 2, row.index - 1])
                possibleMoves.append([row.index + 1, row.index - 2])
            else:
                possibleMoves.append([row.index + 2, row.index + 1])
                possibleMoves.append([row.index + 2, row.index - 1])
                possibleMoves.append([row.index + 1, row.index + 2])
                possibleMoves.append([row.index + 1, row.index - 2])


#----------------------------------------------------------------------------------------------------
    else:
        # check if the column is on the edge of the board
        # todo: ist das nicht genau falsch herum??
        if not field.index - 1 < 0:
            possibleMoves.append([row.index, field.index - 1])  # nach links
        elif not field.index + 1 >= len(row):
            possibleMoves.append([row.index, field.index + 1])  # nach rechts
        # andere Regelungen bei der ersten und letzten Reihe
        if row.index == c:
            possibleMoves.append([row.index + 1 * s, field.index + 1])  # normaler Zug
            possibleMoves.append([row.index + 1 * s, field.index + 2])  # zum Schlagen ru/ro
            possibleMoves.append([row.index + 1 * s, field.index])  # zum Schlagen lu/lo
        elif row.index == r:
            if field.index != 0 or field.index != 7:
                possibleMoves.append([row.index + 1 * s, field.index - 1])  # normaler Zug
            elif diaCalc(turn, board[row.index + 1 * s], field.index):
                possibleMoves.append([row.index + 1 * s, field.index])  # zum Schlagen ru/ro
            elif diaCalc(turn, board[row.index + 1 * s], field.index - 2):
                possibleMoves.append([row.index + 1 * s, field.index - 2])  # zum Schlagen lu/lo
        else:
            possibleMoves.append([row.index + 1 * s, field.index])
            possibleMoves.append([row.index + 1 * s, field.index + 1])
            possibleMoves.append([row.index + 1 * s, field.index - 1])


def createSpielsteinFromString(s: str):
    if len(s) == 1:
        return Spielstein(s)
    else:
        return Spielstein(s[0], s[1], True)
