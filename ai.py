import random


def aiChoice(board, roundCounter):
    if roundCounter == 1:
        if board[1][1] != "X":
            return 5
        else:
            rand = random.randint(0, 3)
            if rand == 0:
                return int(board[0][0])
            if rand == 1:
                return int(board[0][2])
            if rand == 2:
                return int(board[2][0])
            if rand == 3:
                return int(board[2][2])

    else:
        if roundCounter < 3:
            if board[1][1] == "X":
                if board[0][0] != "X":
                    return 1
                else:
                    if board[0][2] != "X":
                        return 3
                    else:
                        if board[2][0] != "X":
                            return 7
                        else:
                            if board[2][2] != "X":
                                return 9
            else:
                if board[0][0] == "0":
                    if board[0][1] != "X" and board[0][2] != "X":
                        return 2
                    else:
                        return 4
        else:

            #CHECK ROW FOR 3 FORMATIONS
            if board[0][1] == "0" and board[0][2] == "0" and board[0][0] != "X" and board[0][0] != "O":
                return 1
            if board[0][0] == "0" and board[0][2] == "0" and board[0][1] != "X" and board[0][1] != "O":
                return 2
            if board[0][0] == "0" and board[0][1] == "0" and board[0][2] != "X" and board[0][2] != "O":
                return 3
            if board[1][2] == "0" and board[1][1] == "0" and board[1][0] != "X" and board[1][0] != "O":
                return 4
            if board[1][0] == "0" and board[1][2] == "0" and board[1][1] != "X" and board[1][1] != "O":
                return 5
            if board[1][0] == "0" and board[1][1] == "0" and board[1][2] != "X" and board[1][2] != "O":
                return 6
            if board[2][1] == "0" and board[2][2] == "0" and board[2][0] != "X" and board[2][0] != "O":
                return 7
            if board[2][0] == "0" and board[2][2] == "0" and board[2][1] != "X" and board[2][1] != "O":
                return 8
            if board[2][0] == "0" and board[2][1] == "0" and board[2][2] != "X" and board[2][2] != "O":
                return 9

            #CHECK COLLUMN FOR 3 FORMATIONS
            if board[2][0] == "0" and board[1][0] == "0" and board[0][0] != "X" and board[0][0] != "O":
                return 1
            if board[2][1] == "0" and board[1][1] == "0" and board[0][1] != "X" and board[0][1] != "O":
                return 2
            if board[2][2] == "0" and board[1][2] == "0" and board[0][2] != "X" and board[0][2] != "O":
                return 3
            if board[0][0] == "0" and board[2][0] == "0" and board[1][0] != "X" and board[1][0] != "O":
                return 4
            if board[0][1] == "0" and board[2][1] == "0" and board[1][1] != "X" and board[1][1] != "O":
                return 5
            if board[0][2] == "0" and board[2][2] == "0" and board[1][2] != "X" and board[1][2] != "O":
                return 6
            if board[0][0] == "0" and board[1][0] == "0" and board[2][0] != "X" and board[2][0] != "O":
                return 7
            if board[0][1] == "0" and board[1][1] == "0" and board[2][1] != "X" and board[2][1] != "O":
                return 8
            if board[0][2] == "0" and board[1][2] == "0" and board[2][2] != "X" and board[2][2] != "O":
                return 9

            #CHECK DIAG FOR 3 FORMATION

            if board[0][0] == "0" and board[1][1] == "0" and board[2][2] != "X" and board[2][2] != "O":
                return 9
            if board[0][0] == "0" and board[2][2] == "0" and board[1][1] != "X" and board[1][1] != "O":
                return 5
            if board[1][1] == "0" and board[2][2] == "0" and board[0][0] != "X" and board[0][0] != "O":
                return 1
            if board[0][2] == "0" and board[1][1] == "0" and board[2][0] != "X" and board[2][0] != "O":
                return 7
            if board[0][2] == "0" and board[2][0] == "0" and board[1][1] != "X" and board[1][1] != "O":
                return 5
            if board[1][1] == "0" and board[2][0] == "0" and board[0][2] != "X" and board[0][2] != "O":
                return 3

            #CHECK 2 IN ADVANCE

            if board[0][0] == "0":
                if board[0][1] != "X" and board[0][1] != "0" and board[0][2] != "X" and board[0][2] != "0":
                    return 3
                if board[1][0] != "X" and board[1][0] != "0" and board[2][0] != "X" and board[2][0] != "0":
                    return 7
            if board[0][1] == "0":
                if board[0][0] != "X" and board[0][0] != "0" and board[0][2] != "X" and board[0][2] != "0":
                    return 3
                if board[1][1] != "X" and board[1][1] != "0" and board[2][1] != "X" and board[2][1] != "0":
                    return 8
            if board[0][2] == "0":
                if board[0][1] != "X" and board[0][1] != "0" and board[0][0] != "X" and board[0][0] != "0":
                    return 1
                if board[1][2] != "X" and board[1][2] != "0" and board[2][2] != "X" and board[2][2] != "0":
                    return 9
            if board[1][0] == "0":
                if board[1][1] != "X" and board[1][1] != "0" and board[1][2] != "X" and board[1][2] != "0":
                    return 6
                if board[0][0] != "X" and board[0][0] != "0" and board[2][0] != "X" and board[2][0] != "0":
                    return 7
            if board[1][1] == "0":
                if board[1][0] != "X" and board[1][0] != "0" and board[1][2] != "X" and board[1][2] != "0":
                    return 6
                if board[0][1] != "X" and board[0][1] != "0" and board[2][1] != "X" and board[2][1] != "0":
                    return 8
            if board[1][2] == "0":
                if board[1][1] != "X" and board[1][1] != "0" and board[1][0] != "X" and board[1][0] != "0":
                    return 4
                if board[0][2] != "X" and board[0][2] != "0" and board[2][2] != "X" and board[2][2] != "0":
                    return 9
            if board[2][0] == "0":
                if board[2][1] != "X" and board[2][1] != "0" and board[2][2] != "X" and board[2][2] != "0":
                    return 9
                if board[1][0] != "X" and board[1][0] != "0" and board[0][0] != "X" and board[0][0] != "0":
                    return 1
            if board[2][1] == "0":
                if board[2][0] != "X" and board[2][0] != "0" and board[2][2] != "X" and board[2][2] != "0":
                    return 9
                if board[1][1] != "X" and board[1][1] != "0" and board[0][1] != "X" and board[0][1] != "0":
                    return 2
            if board[2][2] == "0":
                if board[2][1] != "X" and board[2][1] != "0" and board[2][0] != "X" and board[2][0] != "0":
                    return 7
                if board[1][2] != "X" and board[1][2] != "0" and board[0][2] != "X" and board[0][2] != "0":
                    return 3

            #CHECK 2 IN ADVANCE DIAG

            if board[0][0] == "0":
                if board[1][1] != "X" and board[1][1] != "0" and board[2][2] != "X" and board[2][2] != "0":
                    return 9
            if board[2][2] == "0":
                if board[1][1] != "X" and board[1][1] != "0" and board[0][0] != "X" and board[0][0] != "0":
                    return 1
            if board[1][1] == "0":
                if board[0][0] != "X" and board[0][0] != "0" and board[2][2] != "X" and board[2][2] != "0":
                    return 1
                if board[2][0] != "X" and board[2][0] != "0" and board[0][2] != "X" and board[0][2] != "0":
                    return 3
            if board[0][2] == "0":
                if board[1][1] != "X" and board[1][1] != "0" and board[2][0] != "X" and board[2][0] != "0":
                    return 7
            if board[2][0] == "0":
                if board[1][1] != "X" and board[1][1] != "0" and board[0][2] != "X" and board[0][2] != "0":
                    return 3

            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] != "X" and board[row][col] != "0":
                        return int(board[row][col])
