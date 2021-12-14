import math


def printing(board):
    print("  -----------")
    print(" | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | ")
    print(" | " + "---------" + " | ")
    print(" | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | ")
    print(" | " + "---------" + " | ")
    print(" | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | ")
    print("  -----------" + "\n")


def getRow(playerInput):
    if int(playerInput) < 4 and int(playerInput) > 0:
        return 0
    if int(playerInput) < 7 and int(playerInput) > 3:
        return 1
    if int(playerInput) < 10 and int(playerInput) > 6:
        return 2


def getCollumn(playerInput):
    collumn = math.floor(int(playerInput)) % 3 - 1
    if collumn == -1:
        collumn = 2
    return collumn


def changeTurn(turn):
    if (turn == 0):
        return 1
    else:
        return 0


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


def game(board, Xor0, turn):
    roundCounter = 0
    while roundCounter < 9:
        printing(board)
        playerInput = input("Position to place : ")
        while checkOutOfBound(playerInput) == 0:
            playerInput = input("Wrong choice, pick again : ")
        row = getRow(playerInput)
        collumn = getCollumn(playerInput)

        while checkFree(board, row, collumn) == 0:
            playerInput = input("Position already used, try again : ")
            while checkOutOfBound(playerInput) == 0:
                playerInput = input("Wrong position, pick again : ")
            row = getRow(playerInput)
            collumn = getCollumn(playerInput)

        board[row][collumn] = Xor0[turn]
        roundCounter += 1
        turn = changeTurn(turn)
        printing(board)


def main():
    turn = 0
    Xor0 = ["X", "0"]
    print("\n  Tic Tac Toe")
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    game(board,Xor0,turn)


main()
