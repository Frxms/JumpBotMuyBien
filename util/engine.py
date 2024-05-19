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
    moves = []
    if turn == "r":
        if field - 1 >= 0 and board[row + 1][field - 1] != "" and board[row + 1][field - 1][-1] == "b":
            moves.append([row + 1, field - 1])
        if field + 1 < len(board[row + 1]) and board[row + 1][field + 1] != "" and board[row + 1][field + 1][-1] == "b":
            moves.append([row + 1, field + 1])
    elif turn == "b":
        if field - 1 >= 0 and board[row - 1][field - 1] != "" and board[row - 1][field - 1][-1] == "r":
            moves.append([row - 1, field - 1])
        if field + 1 < len(board[row - 1]) and board[row - 1][field + 1] != "" and board[row - 1][field + 1][-1] == "r":
            moves.append([row - 1, field + 1])
    return moves


# true means legal move
def checkFront(row, field, board, turn):
    if turn == "r":
        if board[row + 1][field] != "" and (len(board[row + 1][field]) > 1 or board[row + 1][field] != turn):
            return False
        if board[row + 1][field] == "X":
            return False
        return [row + 1, field]
    if turn == "b":
        if board[row - 1][field] != "" and (len(board[row - 1][field]) > 1 or board[row - 1][field] != turn):
            return False
        if board[row - 1][field] == "X":
            return False
        return [row - 1, field]


def checkSides(row, field, board, turn, sides):
    if sides:
        #check if figure on the left and not whoppable or enemy figure or out of board
        if field - 1 < 0 or (board[row][field - 1] != "" and (board[row][field - 1] != turn) or len(board[row][field - 1]) > 1 or board[row][field - 1] == "X"):
            return False
    else:
        # check if figure on the right and not whoppable or enemy figure or out of board
        if field + 1 >= len(board[row]) or (board[row][field + 1] != "" and (board[row][field + 1] != turn) or len(board[row][field + 1]) > 1 or board[row][field + 1] == "X"):
            return False

    return True


def twoUp(row, field, board, turn):
    moves = []
    # red
    if turn == "r":
        if (field + 1 < len(board[row + 2]) and not board[row + 2][field + 1] == "X"
                and legalMoveCheck(board[row + 2][field + 1], turn)):
            moves.append([row + 2, field + 1])
        if (field - 1 >= 0 and not board[row + 2][field - 1] == "X"
                and legalMoveCheck(board[row + 2][field - 1], turn)):
            moves.append([row + 2, field - 1])
    # blue
    elif turn == "b":
        if (field - 1 >= 0 and not board[row - 2][field - 1] == "X"
                and legalMoveCheck(board[row - 2][field - 1], turn)):
            moves.append([row - 2, field - 1])
        if (field + 1 < len(board[row - 2]) and not board[row - 2][field + 1] == "X"
                and legalMoveCheck(board[row - 2][field + 1], turn)):
            moves.append([row - 2, field + 1])
    return moves


def hardTurn(row, field, board, turn):
    moves = []
    # red
    if turn == "r":
        if (field + 2 < len(board[row + 1]) and not board[row + 1][field + 2] == "X"
                and legalMoveCheck(board[row + 1][field + 2], turn)):
            moves.append([row + 1, field + 2])
        if (field >= 0 and not board[row + 1][field - 2] == "X"
                and legalMoveCheck(board[row + 1][field - 2], turn)):
            moves.append([row + 1, field - 2])
    # blue
    elif turn == "b":
        if (field - 2 >= 0 and not board[row - 1][field - 2] == "X"
                and legalMoveCheck(board[row - 1][field - 2], turn)):
            moves.append([row - 1, field - 2])
        if (field + 2 < len(board[row - 1]) and not board[row - 1][field + 2] == "X"
                and legalMoveCheck(board[row - 1][field + 2], turn)):
            moves.append([row - 1, field + 2])
    return moves


def legalMoveCheck(targetField, turn):
    if turn == "b":
        if targetField == "" or targetField == "r" or targetField == "br" or targetField == "rr" or targetField == "b":
            return True
        else:
            return False
    elif turn == "r":
        if targetField == "" or targetField == "b" or targetField == "rb" or targetField == "bb" or targetField == "r":
            return True
        else:
            return False
    return False


#------------------------------------------------------------------------------

def getAllMoves(row, field, turn, board):
    moves = []
    currentField = board[row][field]
    # normal Figure
    if currentField != "X" and len(currentField) <= 1:
        front = checkFront(row, field, board, turn)
        diag = diaCalc(row, field, board, turn)
        left = checkSides(row, field, board, turn, True)
        right = checkSides(row, field, board, turn, False)
        if front:  # TODO front False obwohl er nach unten kann ? edge case?
            moves.append(front)
        for i in diag:
            moves.append(i)
        if left:
            moves.append([row, field - 1])
        if right:
            moves.append([row, field + 1])
    # tower
    elif currentField != "X" and len(currentField) > 1:
        for move in hardTurn(row, field, board, turn):
            moves.append(move)
        for move in twoUp(row, field, board, turn):
            moves.append(move)
    #print(moves)
    formatted_moves = []
    formatted_moves = [(move[0], move[1]) for move in moves]
    return formatted_moves
