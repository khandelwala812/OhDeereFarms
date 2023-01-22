import sys
from random import random

import pygame
from tkinter import *
from Tile import *
from Crop import *
from RandomTile import *

pygame.init()

FPS = 80
FramePerSec = pygame.time.Clock()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 660
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

def Paused():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                paused = False
            elif event.type == pygame.QUIT:
                paused = False
                running = False
                pygame.quit()
                sys.exit()

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
        a1 = (self.bgX+625-1280)/-96
        a2 = (self.bgY-275)/-96
        return tile_array[int(a1)][int(a2)]

    def updateTile(self):
        a1 = int((self.bgX+625-1280)/-96)
        a2 = int((self.bgY-275)/-96)
        if(tile_array[a1][a2].condition == "empty"):
            img = pygame.image.load('assets/plot/untilled_plot.png').convert()
        if(tile_array[a1][a2].condition == "tilled" and tile_array[a1][a2].crop == None):
            img = pygame.image.load('assets/plot/tilled_plot.png').convert()
        if(tile_array[a1][a2].condition == "seed" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_1.png').convert()
        if(tile_array[a1][a2].condition == "seedling" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_2.png').convert()
        if(tile_array[a1][a2].condition == "hapling" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_3.png').convert()
        if(tile_array[a1][a2].condition == "harvest" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_4.png').convert()
        if(tile_array[a1][a2].condition == "seed" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_1.png').convert()
        if(tile_array[a1][a2].condition == "seedling" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_2.png').convert()
        if(tile_array[a1][a2].condition == "hapling" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_3.png').convert()
        if(tile_array[a1][a2].condition == "harvest" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_4.png').convert()
        if(tile_array[a1][a2].condition == "seed" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_1.png').convert()
        if(tile_array[a1][a2].condition == "seedling" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_2.png').convert()
        if(tile_array[a1][a2].condition == "hapling" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_3.png').convert()
        if(tile_array[a1][a2].condition == "harvest" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_4.png').convert()
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
    def updateTileGrow(self, x, y):
        a1 = x
        a2 = y
        if(tile_array[a1][a2].condition == "empty"):
            img = pygame.image.load('assets/plot/untilled_plot.png').convert()
        if(tile_array[a1][a2].condition == "tilled" and tile_array[a1][a2].crop == None):
            img = pygame.image.load('assets/plot/tilled_plot.png').convert()
        if(tile_array[a1][a2].condition == "seed" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_1.png').convert()
        if(tile_array[a1][a2].condition == "seedling" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_2.png').convert()
        if(tile_array[a1][a2].condition == "hapling" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_3.png').convert()
        if(tile_array[a1][a2].condition == "harvest" and tile_array[a1][a2].crop.type == "melon"):
            img = pygame.image.load('assets/plants/melon_4.png').convert()
        if(tile_array[a1][a2].condition == "seed" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_1.png').convert()
        if(tile_array[a1][a2].condition == "seedling" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_2.png').convert()
        if(tile_array[a1][a2].condition == "hapling" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_3.png').convert()
        if(tile_array[a1][a2].condition == "harvest" and tile_array[a1][a2].crop.type == "radish"):
            img = pygame.image.load('assets/plants/radish_4.png').convert()
        if(tile_array[a1][a2].condition == "seed" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_1.png').convert()
        if(tile_array[a1][a2].condition == "seedling" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_2.png').convert()
        if(tile_array[a1][a2].condition == "hapling" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_3.png').convert()
        if(tile_array[a1][a2].condition == "harvest" and tile_array[a1][a2].crop.type == "pepper"):
            img = pygame.image.load('assets/plants/pepper_4.png').convert()
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.seed = "melon"
        self.image = pygame.image.load("assets/john/front/front_facing_1.png")
        self.surf = pygame.Surface((30, 50))
        self.rect = self.surf.get_rect(center=(655, 265))

        self.log = pygame.image.load("assets/log.png")
        self.hud = pygame.Surface((1280,500))
        self.hud_rect = self.hud.get_rect(center = (640, 600))

        self.font = pygame.font.Font('assets/Daydream.ttf', 24)
        self.moveText = self.font.render('Movement', True, (0, 200, 0))
        self.wText = self.font.render('W', True, (144, 200, 144))
        self.aText = self.font.render('A', True, (144, 200, 144))
        self.sText = self.font.render('S', True, (144, 200, 144))
        self.dText = self.font.render('D', True, (144, 200, 144))

        #self.hud = pygame.Surface((1280,120))
        #self.hud_rect = self.hud.get_rect(center = (640, 600))
        #self.hud.fill((0,255,255))

    def move(self, pressed_keys):
        moving_up_images = ['assets/john/back/back_facing_move_left.png', 'assets/john/back/back_facing_move_right.png']
        moving_down_images = ['assets/john/front/front_facing_move_left.png', 'assets/john/front/front_facing_move_right.png']
        moving_left_images = ['assets/john/left/left_move_1.png', 'assets/john/left/left_move_2.png']
        moving_right_images = ['assets/john/right/right_move_1.png', 'assets/john/right/right_move_2.png']
        idle_front_images = ['assets/john/front/front_facing_1.png', 'assets/john/front/front_facing_2.png']
        counter = int(timeAni) % 2
        if pressed_keys[pygame.K_w]:
            self.image = pygame.image.load(moving_up_images[counter])
            self.wText = self.font.render('W', True, (144, 180, 216))
        elif pressed_keys[pygame.K_s]:
            self.image = pygame.image.load(moving_down_images[counter])
            self.sText = self.font.render('S', True, (144, 180, 216))
        elif pressed_keys[pygame.K_d]:
            self.image = pygame.image.load(moving_right_images[counter])
            self.dText = self.font.render('D', True, (144, 180, 216))
        elif pressed_keys[pygame.K_a]:
            self.image = pygame.image.load(moving_left_images[counter])
            self.aText = self.font.render('A', True, (144, 180, 216))
        elif pressed_keys[pygame.K_t]:
            tileOn = back_ground.getTile()
            if isinstance(tileOn, Tile) and tileOn.condition == "empty":
                tileOn.setCondition(1)
                back_ground.updateTile()
        elif pressed_keys[pygame.K_p]:
            tileOn = back_ground.getTile()
            if isinstance(tileOn, Tile) and tileOn.condition == "tilled" and tileOn.crop == None:
                print(f"{self.seed}")
                tileOn.crop = Crop(self.seed, 10, 10, 10)
                print(tileOn.crop.type)
                tileOn.setCondition(2)
                back_ground.updateTile()
        elif pressed_keys[pygame.K_h]:
            tileOn = back_ground.getTile()
            if isinstance(tileOn, Tile) and tileOn.condition == "harvest":
                tileOn.setCondition(0)
                tileOn.crop = None
                #get money
                back_ground.updateTile()
        elif pressed_keys[pygame.K_f]:
            tileOn = back_ground.getTile()
            if isinstance(tileOn, Tile) and (tileOn.condition == "seed" or tileOn.condition == "seedling" or tileOn.condition == "hapling"):
                tileOn.fertilizerLevel += .02
                print("fertilized")
                print(f"{tileOn.fertilizerLevel}")

                lastFertilizeTime = time.time()
                #use money
                #add visual effect
        elif pressed_keys[pygame.K_1]:
            self.seed = "melon"
            print(1)
        elif pressed_keys[pygame.K_2]:
            self.seed = "radish"
            print(2)
        elif pressed_keys[pygame.K_3]:
            self.seed = "pepper"
        else:
            self.image = pygame.image.load(idle_front_images[counter])
            self.wText = self.font.render('W', True, (144, 200, 144))
            self.aText = self.font.render('A', True, (144, 200, 144))
            self.sText = self.font.render('S', True, (144, 200, 144))
            self.dText = self.font.render('D', True, (144, 200, 144))


class Rain():
    def __init__(self):
        self.bgimage = pygame.image.load('assets/rain.png')
        self.rectBGimg = self.bgimage.get_rect()

        self.bgY1 = -1000
        self.bgX1 = 0

        self.moving_speed = 5

    def update(self):
        self.bgY1 += self.moving_speed
        if self.bgY1 <= -self.rectBGimg.height:
            self.bgY1 = self.rectBGimg.height

    def render(self):
        SCREEN.blit(self.bgimage, (self.bgX1, self.bgY1))

john = Player()
back_ground = Background()
rain = Rain()

def growStuff():
    for i in range(0, 100):
        for j in range(0, 100):
            timeVar = time.time()

            if isinstance(tile_array[i][j], Tile) and (tile_array[i][j].crop != None) and (tile_array[i][j].condition == "seed" or tile_array[i][j].condition == "seedling" or tile_array[i][j].condition == "hapling") and (tile_array[i][j].crop.growthTime <= timeVar - tile_array[i][j].growthTime):
                tile_array[i][j].growTile()
                #take money
                tile_array[i][j].growthTime = timeVar
                back_ground.updateTileGrow(i, j)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            Paused()
            

    back_ground.update()
    back_ground.render()

    rain.update()
    rain.render()

    SCREEN.blit(john.image, john.rect)
    SCREEN.blit(john.log, john.hud_rect)
    SCREEN.blit(john.moveText, (200,555))
    SCREEN.blit(john.wText, (295, 590))
    SCREEN.blit(john.aText, (265, 620))
    SCREEN.blit(john.sText, (295, 620))
    SCREEN.blit(john.dText, (325, 620))

    growStuff()
    timeAni = pygame.time.get_ticks() / 200
    pressed_keys = pygame.key.get_pressed()
    john.move(pressed_keys)
    # heatmap.show(pressed_keys)

    pygame.display.update()
    FramePerSec.tick(FPS)
