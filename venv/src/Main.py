from random import random

import pygame
from tkinter import *
from Tile import *
from Crop import *
from RandomTile import *

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('John Deer Game')
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

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
                img = pygame.image.load('assets/grass/grass_1.png').convert()
            if(tile_array[i][j].condition == "tilled"):
                img = pygame.image.load('assets/plot/tilled_plot.png').convert()

            screen.blit(img, ((((i-tileX)*96)+(x % 96) + 640), (((j-tileY)*96))+(y%96) + 350))

moving_up_images = ['assets/john/back/back_facing_1.png', 'assets/john/back/back_facing_2.png']
class Player():
    def __init__(self, pos):
        self.image = pygame.image.load('assets/john/front/front_facing_1.png')
        self.rect = self.image.get_rect(center=pos)
        self.pos_x = pos[0]
        self.pos_y = pos[1]
        self.speed = 10
        screen.blit(self.image, (self.pos_x, self.pos_y))

    def input(self):
        keys = pygame.key.get_pressed()
        counter = int(time) % 2 
        if keys[pygame.K_w]:
            self.image = pygame.image.load(moving_up_images[counter])
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
        elif keys[pygame.K_t]:
            x, y = player.getCords()
            offsetX = len(tile_array) / 2
            offsetY = len(tile_array[0]) / 2
            offsetX *= 96
            offsetY *= 96
            offsetX += 640
            offsetY += 350
            tileX = (int) ((offsetX + x) / 96)
            tileY = (int) ((offsetY + y) / 96)
            if tile_array is Tile and tile_array[tileX][tileY].condition == "empty":
                tile_array[tileX][tileY].condition += 1
                Player.till()
        elif keys[pygame.K_p]:
            x, y = player.getCords()
            offsetX = len(tile_array) / 2
            offsetY = len(tile_array[0]) / 2
            offsetX *= 96
            offsetY *= 96
            offsetX += 640
            offsetY += 350
            tileX = (int) ((offsetX + x) / 96)
            tileY = (int) ((offsetY + y) / 96)
            if tile_array is Tile and tile_array[tileX][tileY].condition == "tilled":
                tile_array[tileX][tileY].condition += 1
                Player.plant()
        elif keys[pygame.K_h]:
            x, y = player.getCords()
            offsetX = len(tile_array) / 2
            offsetY = len(tile_array[0]) / 2
            offsetX *= 96
            offsetY *= 96
            offsetX += 640
            offsetY += 350
            tileX = (int) ((offsetX + x) / 96)
            tileY = (int) ((offsetY + y) / 96)
            if tile_array is Tile and tile_array[tileX][tileY].condition == "harvest":
                tile_array[tileX][tileY].condition = 0
                Player.harvest()

        screen.blit(self.image, (640, 350))
    def printCords(self):
        print(f"({self.pos_x}, {self.pos_y})")

    def getCords(self):
        return self.pos_x, self.pos_y

class Menu:
    def __init__(self):
        pass
    def menuBtn(self):
        #draws button in top corner
        pygame.draw.rect(screen, color(200, 200, 200), pygame.Rect(SCREEN_WIDTH-100, 20, 80, 40))
        largeText =pygame.font.Font("assets/Fonts/Daydream.ttf", 35)
        TextPause = text_objects("Paused", largeText)
        TextPause.center = ((SCREEN_WIDTH-50),(40))
        gameDisplay.blit(TextPause)
    def menuScreen(self):
        #draws fullscreen menu
        pass
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
player = Player((640,350))

crop = Crop("corn", 0, 0, 0)

tile_array = [[0] * 100] * 100

for x_parse in range(0, 20):
    for y_parse in range(0, 20):
        rand = random.randint(5, 15)
        perRow = int(rand/5)
        for x_val in range(x_parse*5, x_parse*5+5):
            this_is_a_number = 0
            lands = random.sample(range(5), perRow)
            for y_val in range(y_parse*5, y_parse*5+5):
                if this_is_a_number in lands:
                    tile_array[x_val][y_val] = Tile()
                else:
                    tile_array[x_val][y_val] = RandomTile()
                this_is_a_number += 1




#############################-Game Loop-######################################
while running:


####################### -Detecting Key Stroke-#############################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    background(tile_array)
    player.input()
    time = pygame.time.get_ticks()/600

    pygame.display.flip()
    clock.tick(60)
