import game

def main():
    turn = 0
    Xor0 = ["X", "0"]
    print("\n  Tic Tac Toe")
    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    game.game(board,Xor0,turn)


main()
