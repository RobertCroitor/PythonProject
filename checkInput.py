def checkOutOfBound(playerInput):
    if playerInput.isdigit() == 0:
        return 0
    else:
        if int(playerInput) < 1 or int(playerInput) > 9:
            return 0
        else:
            return 1


def checkFree(board, row, collumn):
    if board[row][collumn] == "X" or board[row][collumn] == "0":
        return 0
    else:
        return 1