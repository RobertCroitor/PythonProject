import math


def getRow(playerInput):
    playerInput=int(playerInput)
    if 4 > playerInput > 0:
        return 0
    if 7 > playerInput > 3:
        return 1
    if 10 > playerInput > 6:
        return 2


def getCollumn(playerInput):
    playerInput=int(playerInput)
    collumn = math.floor(playerInput) % 3 - 1
    if collumn == -1:
        collumn = 2
    return collumn
