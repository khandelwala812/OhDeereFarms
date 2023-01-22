#returns heat map based on input of f for fertilizer, t for tillage, s for same crop
import pygame as pg
import random
from pygame.locals import *


def heatmap5(tiles, levelType):
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
    gameDisplay = pg.display.set_mode((width, height))
    largeText = pg.font.SysFont("comicsansms", 115)
    TextPause = text_objects("Paused", largeText)
    TextPause.center = ((width/2),(height/2))
    gameDisplay.blit(TextPause)
    surfaceHM = pg.display.set_mode(100, 100)
    heatmapMatrix = heatmap5(levelType)
    for i in heatmapMatrix:
        for j in heatmapMatrix[i]:
            if heatmapMatrix[i][j] < 0.5:
                color = (0, 255*(1-heatmapMatrix[i][j]), 0)
            else:
                color = (255*(heatmapMatrix[i][j]), 0, 0)
            pg.draw.rect(surfaceHM, color, pg.rect(i*5, j*5, 5, 5))

# button("Continue", 150, 450, 100, 50, "green", "bright_green", "unpause")
# button("Quit", 550, 450, 100, 50, "red", "bright_red", "quitgame")
pg.init()
screen = pg.display.set_mode((1280, 700))
screen.fill(Color("white"))

startX = 370
startY = 80
x = startX
y = startY
side = 100
spacer = side + 10

# heatMap = heatmap(tile_array, "f")
heatMap = []
for i in range(5):
    row = []
    for j in range(5):
        row.append(random.uniform(0, 1))
    heatMap.append(row)

for row in heatMap:
    for heatMapValue in row:
        surface = pg.display.get_surface()
        box = pg.Rect((x, y), (side, side))
        colorScale = int(round(255 * heatMapValue))
        surface.fill(Color((0, colorScale, 0)), box)
        y += spacer

    x += spacer
    y = startY

def gradientRect(window, left_colour, right_colour, target_rect ):
    colour_rect = pg.Surface((2, 2))
    pg.draw.line( colour_rect, left_colour, (0, 0), (0, 1))
    pg.draw.line( colour_rect, right_colour, (1, 0), (1, 1))
    colour_rect = pg.transform.smoothscale(colour_rect, (target_rect.width, target_rect.height))
    window.blit(colour_rect, target_rect)  

running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.quit:
            running = False

    gradientRect(screen, (0, 0, 0), (0, 255, 0), pg.Rect((0, 0), (50, 50)))

    pg.display.update()