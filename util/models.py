# class Spielstein:
#     def __init__(self, farbe, farbe2=None, isWhopper=False):
#         self.isWhopper = isWhopper
#         self.farbe = farbe
#         if isWhopper:
#             self.farbe2 = farbe2
#
#     def __str__(self):
#         if self.isWhopper:
#             return self.farbe + self.farbe2
#         else:
#             return self.farbe
#
#     def __repr__(self):
#         if self.isWhopper:
#             return self.farbe + self.farbe2
#         else:
#             return self.farbe
#
#
# def get_all_moves(row, field, turn, board):
#     possibleMoves = []
#     r = 0
#     c = 0
#     s = 0
#     if turn == "r":
#         c = 0
#         r = 6
#         s = 1
#     elif turn == "b":
#         c = 7
#         r = 1
#         s = -1
# #---------------------------------------------------------------------------------------------
#
#     if field.isWhopper:
#         # when in first row
#         if row.index == 0:
#             possibleMoves.append([row.index + 2, field.index])
#             possibleMoves.append([row.index + 2, field.index + 2])
#             if field.index == 0:
#                 possibleMoves.append([row.index + 1, field.index + 3])
#             elif field.index - 1 == len(row):
#                 possibleMoves.append([row.index + 1, field.index - 1])
#             else:
#                 possibleMoves.append([row.index + 1, field.index - 1])
#                 possibleMoves.append([row.index + 1, field.index + 3])
#         # when in row 5
#         elif row.index == 5:
#             if field.index <= 1:
#                 possibleMoves.append([row.index + 2, field.index])
#                 possibleMoves.append([row.index + 1, field.index + 2])
#             elif field.index >= 6:
#                 possibleMoves.append([row.index + 1, field.index - 2])
#                 possibleMoves.append(([row.index + 2, field.index - 2]))
#         # when in row 6
#         elif row.index == 6:
#             if field.index <= 2:
#                 possibleMoves.append([row.index + 1, field.index + 1])
#             elif field.index >= 5:
#                 possibleMoves.append([row.index + 1, field.index - 3])
#             else:
#                 possibleMoves.append([row.index + 1, field.index + 1])
#                 possibleMoves.append([row.index + 1, field.index - 3])
#         else:
#             if field.index == 1:
#                 possibleMoves.append([row.index + 2, row.index - 1])
#                 possibleMoves.append([row.index + 2, row.index + 1])
#                 possibleMoves.append([row.index + 1, row.index + 2])
#             elif field.index <= 0:
#                 possibleMoves.append([row.index + 2, row.index + 1])
#                 possibleMoves.append([row.index + 1, row.index + 2])
#             elif field.index == 6:
#                 possibleMoves.append([row.index + 2, row.index + 1])
#                 possibleMoves.append([row.index + 2, row.index - 1])
#                 possibleMoves.append([row.index + 1, row.index - 2])
#             elif field.index - 1 >= len(row):
#                 possibleMoves.append([row.index + 2, row.index - 1])
#                 possibleMoves.append([row.index + 1, row.index - 2])
#             else:
#                 possibleMoves.append([row.index + 2, row.index + 1])
#                 possibleMoves.append([row.index + 2, row.index - 1])
#                 possibleMoves.append([row.index + 1, row.index + 2])
#                 possibleMoves.append([row.index + 1, row.index - 2])
#
#
# #----------------------------------------------------------------------------------------------------
#     else:
#         # check if the column is on the edge of the board
#         if field.index - 1 >= 0:
#             possibleMoves.append([row.index, field.index - 1])  # nach links
#         elif field.index + 1 <= len(row):
#             possibleMoves.append([row.index, field.index + 1])  # nach rechts
#         # erste Reihe für die jeweilige Farbe
#         if row.index == c:
#             possibleMoves.append([row.index + 1 * s, field.index + 1])  # normaler Zug
#             possibleMoves.append([row.index + 1 * s, field.index + 2])  # zum Schlagen ru/ro
#             possibleMoves.append([row.index + 1 * s, field.index])  # zum Schlagen lu/lo
#         # letzte Reihe
#         elif row.index == r:
#             if field.index != 0 or field.index != 7:
#                 possibleMoves.append([row.index + 1 * s, field.index - 1])  # normaler Zug
#             elif diaCalc(turn, board[row.index + 1 * s], field.index):
#                 possibleMoves.append([row.index + 1 * s, field.index])  # zum Schlagen ru/ro
#             elif diaCalc(turn, board[row.index + 1 * s], field.index - 2):
#                 possibleMoves.append([row.index + 1 * s, field.index - 2])  # zum Schlagen lu/lo
#         # mitten auf dem Spielfeld
#         else:
#             possibleMoves.append([row.index + 1 * s, field.index])
#             if diaCalc(turn, board[row.index + 1 * s], field.index + 1):
#                 possibleMoves.append([row.index + 1 * s, field.index + 1])
#             if diaCalc(turn, board[row.index + 1 * s, field.index - 1]):
#                 possibleMoves.append([row.index + 1 * s, field.index - 1])
#
#
# def createSpielsteinFromString(s: str):
#     if len(s) == 1:
#         return Spielstein(s)
#     else:
#         return Spielstein(s[0], s[1], True)
#
#----------------------------------------------------------------------------------------------
# if field.isWhopper:
#     # when in first row
#     if row.index == 0:
#         possibleMoves.append(firstRowTower(row, field, board, turn))
#     # when in row 6
#     elif row.index == 5:
#         possibleMoves.append(sixthRowTower(row, field, board, turn))
#     # when in row 6
#     elif row.index == 6:
#         pass
#     else:
#         pass

#--------------------------------------------------------------------------------------------------
## Tower Func Archive
# first row from the side of the current player
# def firstRowTower(row, field, board, turn):
#     possibleMoves = []
#     # always possible move
#     if legalMoveCheck(board[row.index + 2, field.index], turn):
#         possibleMoves.append([row.index + 2, field.index])
#     if legalMoveCheck(board[row.index + 2, field.index + 2], turn):
#         possibleMoves.append([row.index + 2, field.index + 2])
#     # in the left end of the field
#     if field.index == 0:
#         if legalMoveCheck(board[row.index + 1, field.index + 3], turn):
#             possibleMoves.append([row.index + 1, field.index + 3])
#     # in the right end of the field
#     elif field.index + 1 == len(row):
#         if legalMoveCheck(board[[row.index + 1, field.index - 1]], turn):
#             possibleMoves.append([row.index + 1, field.index - 1])
#     else:
#         if legalMoveCheck(board[row.index + 1, field.index - 1], turn):
#             possibleMoves.append([row.index + 1, field.index - 1])
#         if legalMoveCheck(board[row.index + 1, field.index + 3], turn):
#             possibleMoves.append([row.index + 1, field.index + 3])
#     return possibleMoves
#
#
# # fifth row from the side of the current player
# def sixthRowTower(row, field, board, turn):
#     possibleMoves = []
#     if field.index <= 1:
#         if legalMoveCheck(board[row.index + 2, field.index], turn):
#             possibleMoves.append([row.index + 2, field.index])
#         if legalMoveCheck(board[row.index + 1, field.index + 2], turn):
#             possibleMoves.append([row.index + 1, field.index + 2])
#     elif field.index >= 6:
#         if legalMoveCheck(board[row.index + 1, field.index - 2], turn):
#             possibleMoves.append([row.index + 1, field.index - 2])
#         if legalMoveCheck(board[row.index + 2, field.index - 2], turn):
#             possibleMoves.append(([row.index + 2, field.index - 2]))
#
# def seventhRowTower(row, field, board, turn):
#     possibleMoves = []
#     if field.index <= 2:
#         if legalMoveCheck(board[row.index + 1, field.index + 1], turn):
#             possibleMoves.append([row.index + 1, field.index + 1])
#     elif field.index >= 5:
#         if legalMoveCheck(board[row.index + 1, field.index - 3], turn):
#             possibleMoves.append([row.index + 1, field.index - 3])
#     else:
#         if legalMoveCheck(board[row.index + 1, field.index + 1], turn):
#             possibleMoves.append([row.index + 1, field.index + 1])
#         if legalMoveCheck(board[row.index + 1, field.index - 3], turn):
#             possibleMoves.append([row.index + 1, field.index - 3])
#
# def inFieldTower(row, field, board, turn):
#     possibleMoves = []
#     if field.index == 1:
#         if legalMoveCheck(board[row.index + 2, row.index - 1], turn):
#             possibleMoves.append([row.index + 2, row.index - 1])
#         if legalMoveCheck(board[row.index + 2, row.index + 1], turn):
#             possibleMoves.append([row.index + 2, row.index + 1])
#         if legalMoveCheck(board[row.index + 1, row.index + 2], turn):
#             possibleMoves.append([row.index + 1, row.index + 2])
#     elif field.index <= 0:
#         if legalMoveCheck(board[row.index + 2, field.index + 1], turn):
#             possibleMoves.append([row.index + 2, row.index + 1])
#         if legalMoveCheck(board[row.index + 1, field.index + 2], turn):
#             possibleMoves.append([row.index + 1, row.index + 2])
#     elif field.index == 6:
#         if legalMoveCheck(board[row.index + 2, field.index + 1], turn):
#             possibleMoves.append([row.index + 2, row.index + 1])
#         if legalMoveCheck(board[row.index + 2, row.index - 1], turn):
#             possibleMoves.append([row.index + 2, row.index - 1])
#         if legalMoveCheck(board[row.index + 1, row.index - 2], turn):
#             possibleMoves.append([row.index + 1, row.index - 2])
#     elif field.index - 1 >= len(row):
#         if legalMoveCheck(board[row.index + 2, row.index - 1], turn):
#             possibleMoves.append([row.index + 2, row.index - 1])
#         if legalMoveCheck(board[row.index + 1, row.index - 2], turn):
#             possibleMoves.append([row.index + 1, row.index - 2])
#     else:
#         if legalMoveCheck(board[row.index + 2, field.index + 1], turn):
#             possibleMoves.append([row.index + 2, row.index + 1])
#         if legalMoveCheck(board[row.index + 2, row.index - 1], turn):
#             possibleMoves.append([row.index + 2, row.index - 1])
#         if legalMoveCheck(board[row.index + 1, field.index + 2], turn):
#             possibleMoves.append([row.index + 1, row.index + 2])
#         if legalMoveCheck(board[row.index + 1, row.index - 2], turn):
#             possibleMoves.append([row.index + 1, row.index - 2])
#--------------------------------------------------------------------------------------------------
## Tower Func Archive #2
# def twoUp(row, field, board, turn):
#     moves = []
#     # red
#     if turn == "br" or turn == "rr":
#         if 0 < row < 5:
#             # if field - 1 > 0 and field < len(board[row]) - 1:
#             if 0 < field < 7:
#                 if legalMoveCheck(board[row + 2, field + 1], turn):
#                     moves.append([row + 2, field + 1])
#                 if legalMoveCheck(board[row + 2, field - 1], turn):
#                     moves.append([row + 2, field - 1])
#             # elif field - 1 <= 0:
#             elif field == 0:
#                 if legalMoveCheck(board[row + 2, field + 1], turn):
#                     moves.append([row + 2, field + 1])
#             # elif field >= len(board[row]) - 1:
#             elif field == 7:
#                 if legalMoveCheck(board[row + 2, field - 1], turn):
#                     moves.append([row + 2, field - 1])
#         elif row == 0:
#             if legalMoveCheck(board[row + 2, field], turn):
#                 moves.append([row + 2, field])
#             if legalMoveCheck(board[row + 1, field + 2], turn):
#                 moves.append([row + 2, field + 2])
#         elif row == 5:
#             if 2 <= field <= 5:
#                 if legalMoveCheck(board[row + 2, field], turn):
#                     moves.append([row + 2, field])
#                 if legalMoveCheck(board[row + 2, field - 2], turn):
#                     moves.append([row + 2, field - 2])
#             elif field < 2:
#                 moves.append([row + 2, field])
#             elif field > 5:
#                 moves.append([row + 2, field - 2])
#             # blue
#         elif turn == "rb" or turn == "bb":
#             if 2 < row < 7:
#                 # if field - 1 > 0 and field < len(board[row]) - 1:
#                 if 0 < field < 7:
#                     if legalMoveCheck(board[row - 2, field - 1], turn):
#                         moves.append([row - 2, field - 1])
#                     if legalMoveCheck(board[row - 2, field + 1], turn):
#                         moves.append([row - 2, field + 1])
#                 # elif field - 1 <= 0:
#                 elif field == 0:
#                     if legalMoveCheck(board[row - 2, field + 1], turn):
#                         moves.append([row - 2, field + 1])
#                 # elif field >= len(board[row]) - 1:
#                 elif field == 7:
#                     if legalMoveCheck(board[row - 2, field - 1], turn):
#                         moves.append([row - 2, field - 1])
#             elif row == 7:
#                 if legalMoveCheck(board[row - 2, field], turn):
#                     moves.append([row - 2, field])
#                 if legalMoveCheck(board[row - 2, field + 2], turn):
#                     moves.append([row - 2, field + 2])
#             elif row == 2:
#                 if 2 <= field <= 5:
#                     if legalMoveCheck(board[row - 2, field - 2], turn):
#                         moves.append([row - 2, field - 2])
#                     if legalMoveCheck(board[row - 2, field], turn):
#                         moves.append([row - 2, field])
#                 elif field < 2:
#                     if legalMoveCheck(board[row - 2, field], turn):
#                         moves.append([row - 2, field])
#                 elif field > 5:
#                     if legalMoveCheck(board[row - 2, field - 2], turn):
#                         moves.append([row - 2, field - 2])
#
#         return moves
# def hardTurn(row, field, board, turn):
#     moves = []
#     # red
#     if turn == "br" or turn == "rr":
#         if 0 < row < 6:
#             if 2 <= field <= 5:
#                 if legalMoveCheck(board[row + 1, field + 2], turn):
#                     moves.append([row + 1, field + 2])
#                 if legalMoveCheck(board[row + 1, field - 2], turn):
#                     moves.append([row + 1, field - 2])
#             elif field < 2:
#                 if legalMoveCheck(board[row + 1, field + 2], turn):
#                     moves.append([row + 1, field + 2])
#             elif field > 5:
#                 if legalMoveCheck(board[row + 1, field - 2], turn):
#                     moves.append([row + 1, field - 2])
#         elif row == 0:
#             if 1 <= field <= 4:
#                 if legalMoveCheck(board[row + 1, field - 1], turn):
#                     moves.append([row + 1, field - 1])
#                 if legalMoveCheck(board[row + 1, field + 3], turn):
#                     moves.append([row + 1, field + 3])
#             elif field < 1:
#                 if legalMoveCheck(board[row + 1, field + 3], turn):
#                     moves.append([row + 1, field + 3])
#             elif field > 4:
#                 if legalMoveCheck(board[row + 1, field - 1], turn):
#                     moves.append([row + 1, field - 1])
#         elif row == 6:
#             if 3 <= field <= 4:
#                 if legalMoveCheck(board[row + 1, field - 3], turn):
#                     moves.append([row + 1, field - 3])
#                 if legalMoveCheck(board[row + 1, field + 1], turn):
#                     moves.append([row + 1, field + 1])
#             elif field < 3:
#                 if legalMoveCheck(board[row + 1, field + 1], turn):
#                     moves.append([row + 1, field + 1])
#             elif field > 4:
#                 if legalMoveCheck(board[row + 1, field - 3], turn):
#                     moves.append([row + 1, field - 3])
#     # blue
#     elif turn == "rb" or turn == "bb":
#         if 1 < row < 7:
#             if 2 <= field <= 5:
#                 if legalMoveCheck(board[row - 1, field - 2], turn):
#                     moves.append([row - 1, field - 2])
#                 if legalMoveCheck(board[row - 1, field + 2], turn):
#                     moves.append([row - 1, field + 2])
#             elif field < 2:
#                 if legalMoveCheck(board[row - 1, field + 2], turn):
#                     moves.append([row - 1, field + 2])
#             elif field > 5:
#                 if legalMoveCheck(board[row - 1, field - 2], turn):
#                     moves.append([row - 1, field - 2])
#         elif row == 7:
#             if 1 <= field <= 4:
#                 if legalMoveCheck(board[row - 1, field - 1], turn):
#                     moves.append([row - 1, field - 1])
#                 if legalMoveCheck(board[row - 1, field + 3], turn):
#                     moves.append([row - 1, field + 3])
#             if field < 1:
#                 if legalMoveCheck(board[row - 1, field + 3], turn):
#                     moves.append([row - 1, field + 3])
#             if field > 4:
#                 if legalMoveCheck(board[row - 1, field - 1], turn):
#                     moves.append([row - 1, field - 1])
#         elif row == 1:
#             if 3 <= field <= 4:
#                 if legalMoveCheck(board[row - 1, field - 3], turn):
#                     moves.append([row - 1, field - 3])
#                 if legalMoveCheck(board[row - 1, field + 1], turn):
#                     moves.append([row - 1, field + 1])
#
#     return moves