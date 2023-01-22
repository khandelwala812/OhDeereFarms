import pygame as pg
from pygame.locals import *
import random
from RandomTile import RandomTile
from Tile import Tile

#returns heat map based on input of f for fertilizer, t for tillage, s for same crop
def heatmap5(tiles, levelType):
    cols, rows = 20, 20
    heatmap = [[0 for i in range(cols)] for j in range(rows)]
    for i in range(20):
        for j in range(20):
            tileSum = 0
            for k in range(i * 5, i * 5 + 5):
                for l in range(j * 5, j * 5 + 5):
                    if isinstance(tiles[k][l], RandomTile):
                        continue

                    if levelType == "f":
                        tileSum += tiles[k][l].fertilizerLevel
                    elif levelType == "t":
                        tileSum += tiles[k][l].tillage / 25
                    elif levelType == "s":
                        if tiles[k][l].sameCrop < 4:
                            tileSum += tiles[k][l].sameCrop / 3
                        else:
                            tileSum += 1
            heatmap[i][j] = tileSum
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