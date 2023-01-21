#returns heat map based on input of f for fertilizer, t for tillage, s for same crop
import pygame.display
from Main import *


def heatmap5(levelType):
    heatmap = [[],[]]
    #gives weights for color
    for i in tiles:
        for j in tiles[i]:
            tileSum = 0
            for k in range(5):
                for l in range(5):
                    if levelType == "f":
                        tileSum += tiles[k][l].fertilizer
                    elif levelType == "t":
                        tileSum += tiles[k][l].tillage
                    elif levelType == "s":
                        if tiles[i][j].sameCrop < 4:
                            tileSum += tiles[i][j].sameCrop / 3
                        else:
                            tileSum += 1
            heatmap[i/5][j/5] = tileSum/25
            j += 5
            i += 5
    return heatmap
#returns average value based on input of f for fertilizer, t for tillage, s for same crop
def heatmap(tiles, levelType):
    tileSum = 0
    #gives weights for color
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

def showHeatMap(levelType):
    width = screen.get_width()
    height = screen.get_height()
    largeText =pygame.font.SysFont("comicsansms", 115)
    TextPause = text_objects("Paused", largeText)
    TextPause.center = ((width/2),(height/2))
    gameDisplay.blit(TextPause)
    surfaceHM = pygame.display.set_mode(100, 100)
    heatmapMatrix = heatmap5(levelType)
    for i in heatmapMatrix:
        for j in heatmapMatrix[i]:
            if heatmapMatrix[i][j] < 0.5:
                color = (0, 255*(1-heatmapMatrix[i][j]), 0)
            else:
                color = (255*(heatmapMatrix[i][j]), 0, 0)
            pygame.draw.rect(surfaceHM, color, pygame.rect(i*5, j*5, 5, 5))

    #button("Continue",150,450,100,50,green,bright_green,unpause)
    #button("Quit",550,450,100,50,red,bright_red,quitgame)