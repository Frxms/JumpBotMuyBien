pointBoardTower = []    #in order for red colour
pointBoardPiece = []    # in order for red colour
redList = ["rr", "br"]
blueList = ["bb", "rb"]
def evaluate(board):
    redCount = 0 # red is positive
    blueCount = 0 # blue is negative
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if board[i][j] != "":
                if board[i][j] == "r":  # normal piece
                    redCount += 1
                    redCount += posEval(i, j, "r", True)
                elif board[i][j] == "b":
                    blueCount += 1
                    blueCount += posEval(i, j, "b", True)
                elif board[i][j] in redList:    # tower piece
                    redCount += 2
                    redCount += posEval(i, j, "r", False)
                else:
                    blueCount += 2
                    blueCount += posEval(i, j, "b", False)
    return redCount - blueCount


def posEval(row, column, col, piece):
    if piece:
        if col == "r":
            return pointBoardPiece[row][column]
        else:
            return pointBoardTower[-row][column]
    else:
        if col == "r":
            return pointBoardTower[row][column]
        else:
            return pointBoardTower[-row][column]


if __name__ == "__main__":
    print(evaluate("r0r0rrb0b0bbbb b"))


#     redEval = countMaterial(fen.split(" ")[0], "r")
#     blueEval = countMaterial(fen.split(" ")[0], "b")
#
#     evaluation = blueEval + redEval
#
#     return evaluation
#
#
# def countMaterial(fen: str, color: str) -> float:
#     counted_towers = fen.count(color+color) * 3
#     counted = fen.count(color) - fen.count(color + color) * 2 + counted_towers
#     if color == "b":
#         return counted * -1
#     return counted
