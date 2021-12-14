def checkOutOfBound(playerInput):
    if playerInput.isdigit() == 0:
        return 0
    else:
        playerInput=int(playerInput)
        if playerInput < 1 or playerInput > 9:
            return 0
        else:
            return 1


def checkFree(board, row, collumn):
    if board[row][collumn] == "X" or board[row][collumn] == "0":
        return 0
    else:
        return 1


def difficultyCheck(difficultyInput):
    if difficultyInput.isdigit() == 0:
        return 0
    difficultyInput = int(difficultyInput)
    if 3 < difficultyInput < 1:
        return 0
    return 1


def quitOrPlay(playerInput):
    if playerInput.isdigit() == 0:
        return 0
    playerInput = int(playerInput)
    if 2 < playerInput < 1:
        return 0
    return 1
