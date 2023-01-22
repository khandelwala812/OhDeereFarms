import sys
from random import random

import pygame
from tkinter import *
from Tile import *
from Crop import *
from RandomTile import *

pygame.init()

FPS = 120
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True
rows, cols = 100, 100
tile_array = [[0 for i in range(cols)] for j in range(rows)]
for x_parse in range(0, 20):
    for y_parse in range(0, 20):
        rand = random.randint(5, 15)
        perRow = int(rand/5)
        for x_val in range(x_parse*5, x_parse*5+5):
            this_is_a_number = 0
            for y_val in range(y_parse*5, y_parse*5+5):
                lands = random.sample(range(5), perRow)
                if this_is_a_number in lands:
                    tile_array[x_val][y_val] = Tile()
                else:
                    tile_array[x_val][y_val] = RandomTile()

class Background():
    def __init__(self):
        self.surface = pygame.Surface((9600,9600))
        self.rect = self.surface.get_rect()

        img = None
        for i in range(0, 100):
            for j in range(0, 100):
                if(tile_array[i][j].condition == "empty"):
                    img = pygame.image.load('assets/plot/untilled_plot.png').convert()
                if(tile_array[i][j].condition == "tilled"):
                    img = pygame.image.load('assets/plot/tilled_plot.png').convert()
                if(tile_array[i][j].condition == "pond_1"):
                    img = pygame.image.load('assets/pond/pond_1.png').convert()
                if(tile_array[i][j].condition == "pond_2"):
                    img = pygame.image.load('assets/pond/pond_2.png').convert()
                if(tile_array[i][j].condition == "pond_3"):
                    img = pygame.image.load('assets/pond/pond_3.png').convert()
                if(tile_array[i][j].condition == "grass_1"):
                    img = pygame.image.load('assets/grass/grass_1.png').convert()
                if(tile_array[i][j].condition == "grass_2"):
                    img = pygame.image.load('assets/grass/grass_2.png').convert()
                if(tile_array[i][j].condition == "grass_3"):
                    img = pygame.image.load('assets/grass/grass_3.png').convert()
                if(tile_array[i][j].condition == "grass_4"):
                    img = pygame.image.load('assets/grass/grass_4.png').convert()
                if(tile_array[i][j].condition == "grass_5"):
                    img = pygame.image.load('assets/grass/grass_5.png').convert()
                self.surface.blit(img, (i*96, j*96))

        self.bgY = -4800
        self.bgX = -4800

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            self.bgY += 5
        if pressed_keys[pygame.K_s]:
            self.bgY -= 5
        if pressed_keys[pygame.K_a]:
            self.bgX += 5
        if pressed_keys[pygame.K_d]:
            self.bgX -= 5

    def render(self):
        SCREEN.blit(self.surface, (self.bgX, self.bgY))

    def getCords(self):
        return (self.bgX+640-1280, self.bgY-360)

    def getTile(self):
        a1 = (self.bgX+640-1280)/-96
        a2 = (self.bgY-360)/-96
        return tile_array[int(a1)][int(a2)]
    def updateTile(self):
        a1 = int((self.bgX+640-1280)/-96)
        a2 = int((self.bgY-360)/-96)
        if(tile_array[a1][a2].condition == "empty"):
            img = pygame.image.load('assets/plot/untilled_plot.png').convert()
        if(tile_array[a1][a2].condition == "tilled"):
            img = pygame.image.load('assets/plot/tilled_plot.png').convert()
        if(tile_array[a1][a2].condition == "pond_1"):
            img = pygame.image.load('assets/pond/pond_1.png').convert()
        if(tile_array[a1][a2].condition == "pond_2"):
            img = pygame.image.load('assets/pond/pond_2.png').convert()
        if(tile_array[a1][a2].condition == "pond_3"):
            img = pygame.image.load('assets/pond/pond_3.png').convert()
        if(tile_array[a1][a2].condition == "grass_1"):
            img = pygame.image.load('assets/grass/grass_1.png').convert()
        if(tile_array[a1][a2].condition == "grass_2"):
            img = pygame.image.load('assets/grass/grass_2.png').convert()
        if(tile_array[a1][a2].condition == "grass_3"):
            img = pygame.image.load('assets/grass/grass_3.png').convert()
        if(tile_array[a1][a2].condition == "grass_4"):
            img = pygame.image.load('assets/grass/grass_4.png').convert()
        if(tile_array[a1][a2].condition == "grass_5"):
            img = pygame.image.load('assets/grass/grass_5.png').convert()
        self.surface.blit(img, (int(a1)*96, int(a2)*96))


moving_up_images = ['assets/john/back/back_facing_move_left.png', 'assets/john/back/back_facing_move_right.png']
moving_down_images = ['assets/john/front/front_facing_move_left.png', 'assets/john/front/front_facing_move_right.png']
moving_right_images = ['assets/john/left/left_move_1.png', 'assets/john/left/left_move_2.png']
moving_left_images = ['assets/john/right/right_move_1.png', 'assets/john/right/right_move_2.png']
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/john/front/front_facing_1.png")
        self.surf = pygame.Surface((30, 50))
        self.rect = self.surf.get_rect(center = (640, 357))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        counter = int(time) % 2
        if pressed_keys[pygame.K_w]:
            self.image = pygame.image.load(moving_up_images[counter])
        elif pressed_keys[pygame.K_s]:
            self.image = pygame.image.load(moving_down_images[counter])
        elif pressed_keys[pygame.K_d]:
            self.image = pygame.image.load(moving_right_images[counter])
        elif pressed_keys[pygame.K_a]:
            self.image = pygame.image.load(moving_left_images[counter])

john = Player()
back_ground = Background()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    back_ground.update()
    back_ground.render()

    SCREEN.blit(john.image, john.rect)

    time = pygame.time.get_ticks() / 600
    john.move()

    back_ground.tileType()

    pygame.display.update()
    FramePerSec.tick(FPS)