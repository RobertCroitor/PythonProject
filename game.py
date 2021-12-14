import numberToMatrix
import ai
import bot
import checkInput
import checkWin
import preGamePrint


def printing(board):
    print("  -----------")
    print(" | " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " | ")
    print(" | " + "---------" + " | ")
    print(" | " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " | ")
    print(" | " + "---------" + " | ")
    print(" | " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " | ")
    print("  -----------" + "\n")


def changeTurn(turn):
    if turn == 0:
        return 1
    else:
        return 0


def resetBoard():
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    return board


def game():
    botWins = 0
    playerWins = 0
    Xor0 = ["X", "0"]
    while 1:
        #Game initialize
        turn = 0
        board = resetBoard()
        preGamePrint.prePrint()
        roundCounter = 0
        winFlag = 0
        isBotSmart = 0
        ###End Game initialize

        #Start Game choices
        choice = input("Your choice : ")
        while checkInput.quitOrPlay(choice) == 0:
            choice = input("Wrong number , try again : ")
        if choice == "1":
            preGamePrint.dificultyPrint()
            difficultyChoice = input("Your choice : ")
            while checkInput.difficultyCheck(difficultyChoice) == 0:
                difficultyChoice = input("Wrong number , try again : ")
            ###End Start Game choices
            printing(board)
            #Actual game
            while roundCounter < 9 and winFlag == 0:
                #Player Choice
                if turn == 0:
                    playerInput = input("Position to place : ")
                    while checkInput.checkOutOfBound(playerInput) == 0:
                        playerInput = input("Wrong choice, pick again : ")
                    row = numberToMatrix.getRow(playerInput)
                    collumn = numberToMatrix.getCollumn(playerInput)

                    while checkInput.checkFree(board, row, collumn) == 0:
                        playerInput = input("Position already used, try again : ")
                        while checkInput.checkOutOfBound(playerInput) == 0:
                            playerInput = input("Wrong position, pick again : ")
                        row = numberToMatrix.getRow(playerInput)
                        collumn = numberToMatrix.getCollumn(playerInput)

                    board[row][collumn] = Xor0[turn]

                    roundCounter += 1
                    winFlag = checkWin.checkWin(board)
                    turn = changeTurn(turn)
                    ###Player Choice
                else:
                    #Bot Choice
                    if difficultyChoice == "1":
                        row, collumn = bot.play_random(board)
                    else:
                        if difficultyChoice == "2":
                            if isBotSmart == 0:
                                row, collumn = bot.play_random(board)
                                isBotSmart = 1
                            else:
                                aiChoice = ai.aiChoice(board, roundCounter)
                                row = numberToMatrix.getRow(aiChoice)
                                collumn = numberToMatrix.getCollumn(aiChoice)
                                isBotSmart = 0
                        else:
                            aiChoice = ai.aiChoice(board, roundCounter)
                            print(aiChoice)
                            row = numberToMatrix.getRow(aiChoice)
                            collumn = numberToMatrix.getCollumn(aiChoice)
                            isBotSmart = 0
                    board[row][collumn] = Xor0[turn]
                    printing(board)
                    roundCounter += 1
                    winFlag = checkWin.checkWin(board)
                    turn = changeTurn(turn)
                    ###End Bot Choice
            #EndGame Stats
            print("\n\n=====ENDGAME=====")
            printing(board)
            if winFlag == 0:
                print("\n===Tie===\n")
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
                    print("\n===Bot Wins===\n")
                    print("Player Wins : " + str(playerWins))
                    print("Bot Wins : " + str(botWins))
                    print()
                    print()
                ###End EndGame Stats
        else:
            return
