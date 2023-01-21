import pygame
import numpy as np
from tkinter import *
from Tile import *
from Crop import *


pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('John Deer Game')
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

#############################-Load Map-######################################
map_sprite = [[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]]
#############################-Camera-######################################
def background(tile_array):
    x, y = player.getCords()
    offsetX = len(tile_array) / 2
    offsetY = len(tile_array[0]) / 2
    offsetX *= 96
    offsetY *= 96
    offsetX += 640
    offsetY += 350
    tileX = (int) ((offsetX + x) / 96)
    tileY = (int) ((offsetY + y) / 96)
    for i in range(tileX-8, tileX+9):
        for j in range(tileY-5, tileY+6):
            img = None
            if(tile_array[i][j].condition == "empty"):
                img = pygame.image.load('venv/src/assets/grass/grass_1.png').convert()
            if(tile_array[i][j].condition == "tilled"):
                img = pygame.image.load('/venv/src/assets/plot/tilled_plot.png').convert()

            screen.blit(img, ((((i-tileX)*96)+(x % 96) + 640), (((j-tileY)*96))+(y%96) + 350))


PLAYER_SPRITE = 'assets\deer.png'
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load(PLAYER_SPRITE)
        self.rect = self.image.get_rect(center=pos)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = 10

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.pos_y += self.speed
            self.getCords()
        elif keys[pygame.K_s]:
            self.pos_y -= self.speed
            self.getCords()
        elif keys[pygame.K_d]:
            self.pos_x -= self.speed
            self.getCords()
        elif keys[pygame.K_a]:
            self.pos_x += self.speed
            self.getCords()

    def update(self):
        self.input()

    def printCords(self):
        print(f"({self.pos_x}, {self.pos_y})")

    def getCords(self):
        return self.pos_x, self.pos_y

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
            super().__init__()
    
    def draw_sprite(self):
        #Map

        #Active Elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            self.display_durface.blit(sprite.image, sprite.rect)
            
# Setup
camera_group = CameraGroup()
player = Player((650, 250), camera_group)

crop = Crop("corn", 0, 0, 0)

tile_array = [[0] * 100] * 100

for i in range(0, 100):
    for j in range(0, 100):
        tile_array[i][j] = Tile(0, 0, crop)




#############################-Game Loop-######################################
while running:


####################### -Detecting Key Stroke-#############################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    camera_group.update()
    camera_group.draw(screen)
    background(tile_array)


    pygame.display.flip()
    clock.tick(60)
