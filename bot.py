import random


def play_random(board):
    empty = []
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] != "X" and board[row][col] != "0":
                empty.append((row, col))
    if empty:
        return random.choice(empty)
    else:
        return
