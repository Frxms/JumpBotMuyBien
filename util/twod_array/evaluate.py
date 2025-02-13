pointBoardTower = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [-0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, -0.1],
    [0.4, 0.6, 0.7, 0.7, 0.7, 0.7, 0.6, 0.4],
    [0.9, 1.1, 1.2, 1.2, 1.2, 1.2, 1.1, 0.9],
    [1.4, 1.6, 1.7, 1.7, 1.7, 1.7, 1.6, 1.4],
    [1.9, 2.1, 2.2, 2.2, 2.2, 2.2, 2.1, 1.9],
    [2.4, 2.6, 2.7, 2.7, 2.7, 2.7, 2.6, 2.4],
    [0, 100, 100, 100, 100, 100, 100, 0]] #in order for red colour
pointBoardPiece = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [-0.1, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, -0.1],
    [0.4, 0.6, 0.7, 0.7, 0.7, 0.7, 0.6, 0.4],
    [0.9, 1.1, 1.2, 1.2, 1.2, 1.2, 1.1, 0.9],
    [1.4, 1.6, 1.7, 1.7, 1.7, 1.7, 1.6, 1.4],
    [1.9, 2.1, 2.2, 2.2, 2.2, 2.2, 2.1, 1.9],
    [2.4, 2.6, 2.7, 2.7, 2.7, 2.7, 2.6, 2.4],
    [0, 100, 100, 100, 100, 100, 100, 0]] #in order for red colour

redList = ["rr", "br"]
blueList = ["bb", "rb"]


def evaluate(board):
    redCount = 0  # red is positive
    blueCount = 0  # blue is negative
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] != "" and board[i][j] != "X":
                if board[i][j] == "r":  # normal piece
                    redCount += 1
                    redCount += posEval(i, j, "r", True)
                elif board[i][j] == "b":
                    blueCount += 1
                    blueCount += posEval(i, j, "b", True)
                elif board[i][j] in redList:  # tower piece
                    redCount += 2
                    redCount += posEval(i, j, "r", False)
                else:
                    blueCount += 2
                    blueCount += posEval(i, j, "b", False)
    return (redCount - blueCount).__round__(2)


def posEval(row, column, col, piece):
    if piece:
        if col == "r":
            return pointBoardPiece[row][column]
        else:
            return pointBoardTower[-row-1][column]
    else:
        if col == "r":
            return pointBoardTower[row][column]
        else:
            return pointBoardTower[-row-1][column]


if __name__ == "__main__":
    a = [['X', '', 'r', 'r', 'r', '', 'r', 'X'],
         ['', 'r', 'rr', '', 'r', 'r', 'r', ''],
         ['', '', '', 'r', '', '', '', ''],
         ['', '', 'b', '', '', '', '', ''],
         ['', '', '', '', 'r', 'b', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', 'b', 'b', 'b', 'b', 'b', 'b', ''],
         ['X', '', 'b', 'b', 'b', 'b', '', 'X']]
    b = [['X', '', 'b', '', '', 'b', '', 'X'],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['', '', '', '', '', '', '', ''],
         ['X', '', 'r', '', '', 'rr', '', 'X']]
    # 2.8 - 1.9
    print(evaluate(b))
