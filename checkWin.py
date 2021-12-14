def checkWinRow(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return 1
    else:
        if board[1][0] == board[1][1] == board[1][2]:
            return 1
        else:
            if board[2][0] == board[2][1] == board[2][2]:
                return 1
            else:
                return 0


def checkWinCollumn(board):
    if board[0][0] == board[1][0] == board[2][0]:
        return 1
    else:
        if board[0][1] == board[1][1] == board[2][1]:
            return 1
        else:
            if board[0][2] == board[1][2] == board[2][2]:
                return 1
            else:
                return 0


def checkWinDiag(board):
    if (board[0][2] == board[1][1] == board[2][0]):
        return 1
    else:
        if (board[0][0] == board[1][1] == board[2][2]):
            return 1
        else:
            return 0


def checkWin(board):
    if checkWinRow(board) == 1 or checkWinCollumn(board) == 1 or checkWinDiag(board) == 1:
        return 1
    else:
        return 0
