class Spielstein:
    def __init__(self, farbe1, farbe2=None, isWhopper=False):
        self.isWhopper = isWhopper
        self.farbe1 = farbe1
        if isWhopper:
            self.farbe2 = farbe2

    def __str__(self):
        if self.isWhopper:
            return self.farbe1 + self.farbe2
        else:
            return self.farbe1

    def __repr__(self):
        if self.isWhopper:
            return self.farbe1 + self.farbe2
        else:
            return self.farbe1


#------------------------- Checking Functions -------------------------------

def diaCalc(row, field, board, turn):
    if turn == "r":

        if row == 6:
            if board[row + 1][field - 2][-1] == "b":
                return [row + 1, field - 2]
            if board[row + 1][field][-1] == "b":
                return [row + 1, field]

        else:
            if board[row + 1][field - 1][-1] == "b":
                return [row + 1, field - 1]
            if board[row + 1][field + 1][-1] == "b":
                return [row + 1, field + 1]

        return False
    elif turn == "b":
        if row == 1:
            if board[row - 1][field - 2][-1] == "r":
                return [row - 1, field - 2]
            if board[row - 1][field][-1] == "r":
                return [row - 1, field]
        else:
            if board[row - 1][field - 1][-1] == "r":
                return [row - 1, field - 1]
            if board[row - 1][field + 1][-1] == "r":
                return [row - 1, field + 1]

        return False


# true means legal move
def checkFront(row, field, board, turn):
    if turn == "r":
        if board[row + 1][field] != turn or len(board[row + 1][field]) > 1 :
            return False
        if board[row][field] == board[6][0] or board[row][field] == board[6][7]:
            return False
        if row == 0:
            return [row + 1, field + 1]
        if row == 6:
            return [row + 1, field - 1]
        return [row + 1, field]
    if turn == "b":
        if board[row - 1][field] != turn or len(board[row - 1][field]) > 1:
            return False
        if board[row][field] == board[1][0] or board[row][field] == board[1][7]:
            return False
        if row == 1:
            return [row - 1, field - 1]
        if row == 7:
            return [row - 1, field + 1]
        return [row + 1, field]



def checkSides(row, field, board, turn, sides):
    if sides:
        #check if figure on the left and not whoppable or enemy figure or out of board
        if board[row][field - 1] != turn or len(board[row][field - 1]) > 1 or field - 1 < 0:
            return False
    else:
        # check if figure on the right and not whoppable or enemy figure or out of board
        if board[row][field + 1] != turn or len(board[row][field + 1]) > 1 or field + 1 >= len(board[row]):
            return False

    return True

def twoUp(row, field, board, turn):
    moves = []
    # red
    if turn == "br" or turn == "rr":
        if 0 < row < 5:
            # if field - 1 > 0 and field < len(board[row]) - 1:
            if 0 < field < 7:
                if legalMoveCheck(board[row + 2, field + 1], turn):
                    moves.append([row + 2, field + 1])
                if legalMoveCheck(board[row + 2, field - 1], turn):
                    moves.append([row + 2, field - 1])
            # elif field - 1 <= 0:
            elif field == 0:
                if legalMoveCheck(board[row + 2, field + 1], turn):
                    moves.append([row + 2, field + 1])
            # elif field >= len(board[row]) - 1:
            elif field == 7:
                if legalMoveCheck(board[row + 2, field - 1], turn):
                    moves.append([row + 2, field - 1])
        elif row == 0:
            if legalMoveCheck(board[row + 2, field], turn):
                moves.append([row + 2, field])
            if legalMoveCheck(board[row + 1, field + 2], turn):
                moves.append([row + 2, field + 2])
        elif row == 5:
            if 2 <= field <= 5:
                if legalMoveCheck(board[row + 2, field], turn):
                    moves.append([row + 2, field])
                if legalMoveCheck(board[row + 2, field - 2], turn):
                    moves.append([row + 2, field - 2])
            elif field < 2:
                moves.append([row + 2, field])
            elif field > 5:
                moves.append([row + 2, field - 2])
    # blue
    elif turn == "rb" or turn == "bb":
        if 2 < row < 7:
            # if field - 1 > 0 and field < len(board[row]) - 1:
            if 0 < field < 7:
                if legalMoveCheck(board[row - 2, field - 1], turn):
                    moves.append([row - 2, field - 1])
                if legalMoveCheck(board[row - 2, field + 1], turn):
                    moves.append([row - 2, field + 1])
            # elif field - 1 <= 0:
            elif field == 0:
                if legalMoveCheck(board[row - 2, field + 1], turn):
                    moves.append([row - 2, field + 1])
            # elif field >= len(board[row]) - 1:
            elif field == 7:
                if legalMoveCheck(board[row - 2, field - 1], turn):
                    moves.append([row - 2, field - 1])
        elif row == 7:
            if legalMoveCheck(board[row - 2, field], turn):
                moves.append([row - 2, field])
            if legalMoveCheck(board[row - 2, field + 2], turn):
                moves.append([row - 2, field + 2])
        elif row == 2:
            if 2 <= field <= 5:
                if legalMoveCheck(board[row - 2, field - 2], turn):
                    moves.append([row - 2, field - 2])
                if legalMoveCheck(board[row - 2, field], turn):
                    moves.append([row - 2, field])
            elif field < 2:
                if legalMoveCheck(board[row - 2, field], turn):
                    moves.append([row - 2, field])
            elif field > 5:
                if legalMoveCheck(board[row - 2, field - 2], turn):
                    moves.append([row - 2, field - 2])

    return moves


def hardTurn(row, field, board, turn):
    moves = []
    # red
    if turn == "br" or turn == "rr":
        if 0 < row < 6:
            if 2 <= field <= 5:
                if legalMoveCheck(board[row + 1, field + 2], turn):
                    moves.append([row + 1, field + 2])
                if legalMoveCheck(board[row + 1, field - 2], turn):
                    moves.append([row + 1, field - 2])
            elif field < 2:
                if legalMoveCheck(board[row + 1, field + 2], turn):
                    moves.append([row + 1, field + 2])
            elif field > 5:
                if legalMoveCheck(board[row + 1, field - 2], turn):
                    moves.append([row + 1, field - 2])
        elif row == 0:
            if 1 <= field <= 4:
                if legalMoveCheck(board[row + 1, field - 1], turn):
                    moves.append([row + 1, field - 1])
                if legalMoveCheck(board[row + 1, field + 3], turn):
                    moves.append([row + 1, field + 3])
            elif field < 1:
                if legalMoveCheck(board[row + 1, field + 3], turn):
                    moves.append([row + 1, field + 3])
            elif field > 4:
                if legalMoveCheck(board[row + 1, field - 1], turn):
                    moves.append([row + 1, field - 1])
        elif row == 6:
            if 3 <= field <= 4:
                if legalMoveCheck(board[row + 1, field - 3], turn):
                    moves.append([row + 1, field - 3])
                if legalMoveCheck(board[row + 1, field + 1], turn):
                    moves.append([row + 1, field + 1])
            elif field < 3:
                if legalMoveCheck(board[row + 1, field + 1], turn):
                    moves.append([row + 1, field + 1])
            elif field > 4:
                if legalMoveCheck(board[row + 1, field - 3], turn):
                    moves.append([row + 1, field - 3])
    # blue
    elif turn == "rb" or turn == "bb":
        if 1 < row < 7:
            if 2 <= field <= 5:
                if legalMoveCheck(board[row - 1, field - 2], turn):
                    moves.append([row - 1, field - 2])
                if legalMoveCheck(board[row - 1, field + 2], turn):
                    moves.append([row - 1, field + 2])
            elif field < 2:
                if legalMoveCheck(board[row - 1, field + 2], turn):
                    moves.append([row - 1, field + 2])
            elif field > 5:
                if legalMoveCheck(board[row - 1, field - 2], turn):
                    moves.append([row - 1, field - 2])
        elif row == 7:
            if 1 <= field <= 4:
                if legalMoveCheck(board[row - 1, field - 1], turn):
                    moves.append([row - 1, field - 1])
                if legalMoveCheck(board[row - 1, field + 3], turn):
                    moves.append([row - 1, field + 3])
            if field < 1:
                if legalMoveCheck(board[row - 1, field + 3], turn):
                    moves.append([row - 1, field + 3])
            if field > 4:
                if legalMoveCheck(board[row - 1, field - 1], turn):
                    moves.append([row - 1, field - 1])
        elif row == 1:
            if 3 <= field <= 4:
                if legalMoveCheck(board[row - 1, field - 3], turn):
                    moves.append([row - 1, field - 3])
                if legalMoveCheck(board[row - 1, field + 1], turn):
                    moves.append([row - 1, field + 1])

    return moves

def legalMoveCheck(targetField, turn):
    if turn == "b":
        if targetField == "" or targetField == "r" or targetField == "br" or targetField == "rr":
            return True
        else:
            return False
    elif turn == "r":
        if targetField == "" or targetField == "b" or targetField == "rb" or targetField == "bb":
            return True
        else:
            return False
    return False


#------------------------------------------------------------------------------

def getAllMoves(row, field, turn, board):
    moves = []
    currentField = board[row][field]

    if len(currentField) <= 1:
        front = checkFront(row, field, board, turn)
        diag = diaCalc(row, field, board, turn)
        left = checkSides(row, field, board, turn, True)
        right = checkSides(row, field, board, turn, False)
        if front != False:
            moves.append(front)
        if diag != False:
            moves.append(diag)
        if left:
            moves.append([row, field - 1])
        if right:
            moves.append([row, field + 1])

    elif len(currentField) > 1:
        moves.append(hardTurn(row, field, board, turn))
        moves.append(twoUp(row, field, board, turn))
