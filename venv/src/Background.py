from Main import *
from Tile import *
import pygame 

class Background:
    def __init__(self, screen):
        self.screen = screen
    def draw(self, xPlayer, yPlayer, tiles):
        offsetX = len(tiles) / 2
        offsetY = len(tiles[0]) / 2
        offsetX *= 96
        offsetY *= 96
        offsetX += 640
        offsetY += 350
        tileX = (int) ((offsetX + xPlayer) / 96)
        tileY = (int) ((offsetY + yPlayer) / 96)
        for i in range(tileX-8, tileX+9):
            for j in range(tileY-5, tileY+6):
                img = None
                if(tiles[i][j].condition == "empty"):
                    img = pygame.image.load('venv/src/assets/grass/grass_1.png').convert()
                if(tiles[i][j].condition == "tilled"):
                    img = pygame.image.load('venv/src/assets/plot/tilled_plot.png').convert()

                self.screen.blit(img, ((i*96-offsetX-640)+xPlayer), ((j*96-offsetY-350))+yPlayer)

