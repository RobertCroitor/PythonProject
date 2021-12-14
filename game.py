import math

import bot
import checkInput
import checkWin


def printing(board):
    print("  -----------")
    print(" | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | ")
    print(" | " + "---------" + " | ")
    print(" | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | ")
    print(" | " + "---------" + " | ")
    print(" | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | ")
    print("  -----------" + "\n")


def getRow(playerInput):
    if 4 > int(playerInput) > 0:
        return 0
    if 7 > int(playerInput) > 3:
        return 1
    if 10 > int(playerInput) > 6:
        return 2


def getCollumn(playerInput):
    collumn = math.floor(int(playerInput)) % 3 - 1
    if collumn == -1:
        collumn = 2
    return collumn


def changeTurn(turn):
    if turn == 0:
        return 1
    else:
        return 0


def game(board, Xor0, turn):
    botWins = 0
    playerWins = 0

    roundCounter = 0
    winFlag = 0
    printing(board)
    while roundCounter < 9 and winFlag == 0:
        if turn == 0:
            playerInput = input("Position to place : ")
            while checkInput.checkOutOfBound(playerInput) == 0:
                playerInput = input("Wrong choice, pick again : ")
            row = getRow(playerInput)
            collumn = getCollumn(playerInput)

            while checkInput.checkFree(board, row, collumn) == 0:
                playerInput = input("Position already used, try again : ")
                while checkInput.checkOutOfBound(playerInput) == 0:
                    playerInput = input("Wrong position, pick again : ")
                row = getRow(playerInput)
                collumn = getCollumn(playerInput)

            board[row][collumn] = Xor0[turn]

            roundCounter += 1
            winFlag = checkWin.checkWin(board)
            turn = changeTurn(turn)
        else:
            row, collumn = bot.play_random(board)
            board[row][collumn] = Xor0[turn]
            printing(board)
            roundCounter += 1
            winFlag = checkWin.checkWin(board)
            turn = changeTurn(turn)
    print("\n\n=====ENDGAME=====")
    printing(board)
    if winFlag == 0:
        print("\n Tie \n")
        print("Player Wins : " + str(playerWins))
        print("Bot Wins : " + str(botWins))
    else:
        turn = changeTurn(turn)
        if turn == 0:
            playerWins += 1
            print("\n===Player Wins===\n")
            print("Player Wins : " + str(playerWins))
            print("Bot Wins : " + str(botWins))
        else:
            botWins += 1
            print("\n Player Wins \n")
            print("Player Wins : " + str(playerWins))
            print("Bot Wins : " + str(botWins))
