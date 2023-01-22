import pygame as pg
from pygame.locals import *
import random
from RandomTile import RandomTile

#returns heat map based on input of f for fertilizer, t for tillage, s for same crop
def heatmap5(tiles, levelType):
    heatmap = [[0] * 20] * 20
    # gives weights for color
    for i in range(0, len(tiles), 5):
        for j in range(0, len(tiles[i]), 5):
            tileSum = 0
            for k in range(5):
                for l in range(5):
                    if isinstance(tiles[k][l], RandomTile):
                        continue

                    if levelType == "f":
                        tileSum += tiles[k][l].fertilizerLevel
                        print(tileSum)
                    elif levelType == "t":
                        tileSum += tiles[k][l].tillage
                    elif levelType == "s":
                        if tiles[k][l].sameCrop < 4:
                            tileSum += tiles[k][l].sameCrop / 3
                        else:
                            tileSum += 1
            x = int(i / 5)
            y = int(j / 5)
            heatmap[x][y] = tileSum / 25

    return heatmap

# returns average value based on input of f for fertilizer, t for tillage, s for same crop
def heatmap(tiles, levelType):
    tileSum = 0
    # gives weights for color
    for i in tiles:
        for j in tiles[i]:
            if levelType == "f":
                tileSum += tiles[i][j].fertilizer
            elif levelType == "t":
                tileSum += tiles[i][j].overTilled()
            elif levelType == "s":
                if tiles[i][j].sameCrop < 4:
                    tileSum += tiles[i][j].sameCrop / 3
                else:
                    tileSum += 1

    return tileSum/100