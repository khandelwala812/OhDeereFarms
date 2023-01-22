import sys
from random import random

import pygame
from pygame.locals import Color
from pygame import mixer
from Tile import *
from Crop import *
from RandomTile import *
from HeatMap import heatmap5

pygame.init()
mixer.init()
musicPlaylist = [
    "assets/music/out-on-the-farm.mp3",
    "assets/music/merry-farm.mp3",
    "assets/music/country-fun.mp3",
]
startTime = time.time()
mixer.music.load(musicPlaylist[0])
mixer.music.set_volume(0.7)
coins = 100
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
        perRow = int(rand / 5)
        for x_val in range(x_parse * 5, x_parse * 5 + 5):
            this_is_a_number = 0
            for y_val in range(y_parse * 5, y_parse * 5 + 5):
                lands = random.sample(range(5), perRow)
                if this_is_a_number in lands:
                    tile_array[x_val][y_val] = Tile()
                else:
                    tile_array[x_val][y_val] = RandomTile()


class PausedClass:
    def __init__(self):
        self.font = pygame.font.Font("assets/Daydream.ttf", 80)

        self.r, self.g, self.b = 160, 0, 0

        self.descriptionText = self.font.render(
            "PAUSED", True, (self.r, self.g, self.b)
        )

    def Paused(self):
        paused = True
        while paused:
            SCREEN.blit(pauser.descriptionText, (SCREEN_WIDTH/2-250, SCREEN_HEIGHT/2-50))
            pygame.display.update()
            FramePerSec.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    paused = False
                elif event.type == pygame.QUIT:
                    paused = False
                    running = False
                    pygame.quit()
                    sys.exit()
            SCREEN.blit(
                pauser.descriptionText, (SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT / 2 - 50)
            )
            if self.b == 0 and not self.r == 0:
                if self.r == 160 and self.g < 160:
                    self.g += 1
                elif self.r > 0 and self.g == 160:
                    self.r -= 1
            elif self.r == 0 and not self.g == 0:
                if self.g == 160 and self.b < 160:
                    self.b += 1
                elif self.g > 0 and self.b == 160:
                    self.g -= 1
            elif self.g == 0:
                if self.b == 160 and self.r < 160:
                    self.r += 1
                elif self.b > 0 and self.r == 160:
                    self.b -= 1
            self.descriptionText = self.font.render(
                "PAUSED", True, (self.r, self.g, self.b)
            )

class EndClass:
    def __init__(self):
        self.ended = False
        self.font = pygame.font.Font("assets/Daydream.ttf", 80)
        self.endTime = 0
        self.r, self.g, self.b = 160, 0, 0

        self.descriptionText = self.font.render(
            "END", True, (self.r, self.g, self.b)
        )
        self.font = pygame.font.Font("assets/Daydream.ttf", 40)
        self.timeText = self.font.render(f"You finished in {self.endTime}", True, (50, 215, 255))

    def Paused(self):
        paused = True
        while paused:
            SCREEN.blit(ender.descriptionText, (SCREEN_WIDTH/2-150, SCREEN_HEIGHT/2-150))
            SCREEN.blit(ender.timeText, (SCREEN_WIDTH/2-450, SCREEN_HEIGHT/2+150))
            pygame.display.update()
            FramePerSec.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
                    pygame.quit()
                    sys.exit()
            SCREEN.blit(
                ender.descriptionText, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 150)
            )
            SCREEN.blit(ender.timeText, (SCREEN_WIDTH/2-450, SCREEN_HEIGHT/2+150))
            if self.b == 0 and not self.r == 0:
                if self.r == 160 and self.g < 160:
                    self.g += 1
                elif self.r > 0 and self.g == 160:
                    self.r -= 1
            elif self.r == 0 and not self.g == 0:
                if self.g == 160 and self.b < 160:
                    self.b += 1
                elif self.g > 0 and self.b == 160:
                    self.g -= 1
            elif self.g == 0:
                if self.b == 160 and self.r < 160:
                    self.r += 1
                elif self.b > 0 and self.r == 160:
                    self.b -= 1
            self.font = pygame.font.Font("assets/Daydream.ttf", 80)
            self.descriptionText = self.font.render(
                "END", True, (self.r, self.g, self.b)
            )
            SCREEN.blit(ender.timeText, (SCREEN_WIDTH/2-450, SCREEN_HEIGHT/2+150))


class Background:
    def __init__(self):
        self.surface = pygame.Surface((9600, 9600))
        self.rect = self.surface.get_rect()

        img = None
        for i in range(0, 100):
            for j in range(0, 100):
                if tile_array[i][j].condition == "empty":
                    img = pygame.image.load("assets/plot/untilled_plot.png").convert()
                if tile_array[i][j].condition == "tilled":
                    img = pygame.image.load("assets/plot/tilled_plot.png").convert()
                if tile_array[i][j].condition == "pond_1":
                    img = pygame.image.load("assets/pond/pond_1.png").convert()
                if tile_array[i][j].condition == "pond_2":
                    img = pygame.image.load("assets/pond/pond_2.png").convert()
                if tile_array[i][j].condition == "pond_3":
                    img = pygame.image.load("assets/pond/pond_3.png").convert()
                if tile_array[i][j].condition == "grass_1":
                    img = pygame.image.load("assets/grass/grass_1.png").convert()
                if tile_array[i][j].condition == "grass_2":
                    img = pygame.image.load("assets/grass/grass_2.png").convert()
                if tile_array[i][j].condition == "grass_3":
                    img = pygame.image.load("assets/grass/grass_3.png").convert()
                if tile_array[i][j].condition == "grass_4":
                    img = pygame.image.load("assets/grass/grass_4.png").convert()
                if tile_array[i][j].condition == "grass_5":
                    img = pygame.image.load("assets/grass/grass_5.png").convert()
                self.surface.blit(img, (i * 96, j * 96))

        self.bgY = -4800
        self.bgX = -4800

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            if not self.bgY + 5 > 0:
                self.bgY += 5
        if pressed_keys[pygame.K_s]:
            if not self.bgY - 5 < -8300:
                self.bgY -= 5
        if pressed_keys[pygame.K_a]:
            if not self.bgX + 5 > 0:
                self.bgX += 5
        if pressed_keys[pygame.K_d]:
            if not self.bgX - 5 < -8300:
                self.bgX -= 5

    def render(self):
        SCREEN.blit(self.surface, (self.bgX, self.bgY))

    def getCords(self):
        return self.bgX + 640 - 1280, self.bgY - 360

    def getTile(self):
        a1 = (self.bgX + 625 - 1280) / -96
        a2 = (self.bgY - 275) / -96
        return tile_array[int(a1)][int(a2)]

    def updateTile(self):
        a1 = int((self.bgX + 625 - 1280) / -96)
        a2 = int((self.bgY - 275) / -96)
        if tile_array[a1][a2].condition == "empty":
            img = pygame.image.load("assets/plot/untilled_plot.png").convert()
        if tile_array[a1][a2].condition == "tilled" and tile_array[a1][a2].crop == None:
            img = pygame.image.load("assets/plot/tilled_plot.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_4.png").convert()
        if tile_array[a1][a2].condition == "pond_1":
            img = pygame.image.load("assets/pond/pond_1.png").convert()
        if tile_array[a1][a2].condition == "pond_2":
            img = pygame.image.load("assets/pond/pond_2.png").convert()
        if tile_array[a1][a2].condition == "pond_3":
            img = pygame.image.load("assets/pond/pond_3.png").convert()
        if tile_array[a1][a2].condition == "grass_1":
            img = pygame.image.load("assets/grass/grass_1.png").convert()
        if tile_array[a1][a2].condition == "grass_2":
            img = pygame.image.load("assets/grass/grass_2.png").convert()
        if tile_array[a1][a2].condition == "grass_3":
            img = pygame.image.load("assets/grass/grass_3.png").convert()
        if tile_array[a1][a2].condition == "grass_4":
            img = pygame.image.load("assets/grass/grass_4.png").convert()
        if tile_array[a1][a2].condition == "grass_5":
            img = pygame.image.load("assets/grass/grass_5.png").convert()

        self.surface.blit(img, (int(a1) * 96, int(a2) * 96))

    def updateTileGrow(self, x, y):
        a1 = x
        a2 = y
        if tile_array[a1][a2].condition == "empty":
            img = pygame.image.load("assets/plot/untilled_plot.png").convert()
        if tile_array[a1][a2].condition == "tilled" and tile_array[a1][a2].crop == None:
            img = pygame.image.load("assets/plot/tilled_plot.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "melon"
        ):
            img = pygame.image.load("assets/plants/melon_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "radish"
        ):
            img = pygame.image.load("assets/plants/radish_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "pepper"
        ):
            img = pygame.image.load("assets/plants/pepper_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "cantaloupe"
        ):
            img = pygame.image.load("assets/plants/cantaloupe_4.png").convert()
        if (
                tile_array[a1][a2].condition == "seed"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_1.png").convert()
        if (
                tile_array[a1][a2].condition == "seedling"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_2.png").convert()
        if (
                tile_array[a1][a2].condition == "hapling"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_3.png").convert()
        if (
                tile_array[a1][a2].condition == "harvest"
                and tile_array[a1][a2].crop.type == "grape"
        ):
            img = pygame.image.load("assets/plants/grape_4.png").convert()
        if tile_array[a1][a2].condition == "pond_1":
            img = pygame.image.load("assets/pond/pond_1.png").convert()
        if tile_array[a1][a2].condition == "pond_2":
            img = pygame.image.load("assets/pond/pond_2.png").convert()
        if tile_array[a1][a2].condition == "pond_3":
            img = pygame.image.load("assets/pond/pond_3.png").convert()
        if tile_array[a1][a2].condition == "grass_1":
            img = pygame.image.load("assets/grass/grass_1.png").convert()
        if tile_array[a1][a2].condition == "grass_2":
            img = pygame.image.load("assets/grass/grass_2.png").convert()
        if tile_array[a1][a2].condition == "grass_3":
            img = pygame.image.load("assets/grass/grass_3.png").convert()
        if tile_array[a1][a2].condition == "grass_4":
            img = pygame.image.load("assets/grass/grass_4.png").convert()
        if tile_array[a1][a2].condition == "grass_5":
            img = pygame.image.load("assets/grass/grass_5.png").convert()

        self.surface.blit(img, (int(a1) * 96, int(a2) * 96))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.seeds = ["pepper", "radish", "cantaloupe", "melon", "grape"]
        self.seedIndex = 0
        self.seedIndexMax = 0
        self.toggle = True

        self.wcurrency = 300
        self.ccurrency = 100
        self.image = pygame.image.load("assets/john/front/front_facing_1.png")
        self.surf = pygame.Surface((30, 50))
        self.rect = self.surf.get_rect(center=(655, 265))

        self.log = pygame.image.load("assets/log.png")
        self.hud = pygame.Surface((1280, 500))
        self.hud_rect = self.hud.get_rect(center=(640, 600))

        self.font = pygame.font.Font("assets/Daydream.ttf", 24)

        self.wText = self.font.render("W", True, (144, 200, 144))
        self.aText = self.font.render("A", True, (144, 200, 144))
        self.sText = self.font.render("S", True, (144, 200, 144))
        self.dText = self.font.render("D", True, (144, 200, 144))

        self.font = pygame.font.Font("assets/Daydream.ttf", 16)
        self.mapText = self.font.render("(M,N,B) Map", True, (218, 112, 214))

        self.font = pygame.font.Font("assets/Daydream.ttf", 24)

        self.tillText = self.font.render("(J) Till", True, (233, 116, 80))
        self.plantText = self.font.render("(K) Plant", True, (152, 251, 152))
        self.harvestText = self.font.render("(L) Harvest", True, (221, 160, 221))
        self.fertilizeText = self.font.render("(I) Fertilize", True, (255, 215, 0))

        self.cropText = self.font.render("(O) Crop Selected", True, (173, 216, 230))
        self.cropIcon = pygame.image.load("assets/plants/icons/pepper.png")
        self.cropRect = self.cropIcon.get_rect(center=(1142, 565))

        self.upgradeText = self.font.render("(P) Next Upgrade", True, (255, 114, 118))
        self.upgradeIcon = pygame.image.load("assets/plants/icons/radish.png")
        self.upgradeRect = self.upgradeText.get_rect(center=(1305, 615))
        self.upgradeCost = self.font.render("$15", True, (255, 160, 122))

        self.coinText = self.font.render("Coins:", True, (255, 165, 0))
        self.coinAmount = self.font.render(str(self.ccurrency), True, (255, 255, 102))

        self.waterText = self.font.render("Water:", True, (65, 105, 225))
        self.waterAmount = self.font.render(str(self.wcurrency), True, (0, 191, 255))

        # self.hud = pygame.Surface((1280,120))
        # self.hud_rect = self.hud.get_rect(center = (640, 600))
        # self.hud.fill((0,255,255))

    def increaseW(self, water):
        self.wcurrency += water

    def decreaseW(self, water):
        self.wcurrency -= water

    def getW(self, water):
        return self.wcurrency

    def increaseC(self, coin):
        self.ccurrency += coin

    def decreaseC(self, coin):
        self.ccurrency -= coin

    def getC(self, coin):
        return self.ccurrency

    def move(self, pressed_keys):
        moving_up_images = [
            "assets/john/back/back_facing_move_left.png",
            "assets/john/back/back_facing_move_right.png",
        ]
        moving_down_images = [
            "assets/john/front/front_facing_move_left.png",
            "assets/john/front/front_facing_move_right.png",
        ]
        moving_left_images = [
            "assets/john/left/left_move_1.png",
            "assets/john/left/left_move_2.png",
        ]
        moving_right_images = [
            "assets/john/right/right_move_1.png",
            "assets/john/right/right_move_2.png",
        ]
        idle_front_images = [
            "assets/john/front/front_facing_1.png",
            "assets/john/front/front_facing_2.png",
        ]
        action_images = ["assets/john/action_1.png", "assets/john/action_2.png"]
        counter = int(timeAni) % 2
        if pressed_keys[pygame.K_w]:
            self.image = pygame.image.load(moving_up_images[counter])
            self.wText = self.font.render("W", True, (144, 180, 216))
        elif pressed_keys[pygame.K_s]:
            self.image = pygame.image.load(moving_down_images[counter])
            self.sText = self.font.render("S", True, (144, 180, 216))
        elif pressed_keys[pygame.K_d]:
            self.image = pygame.image.load(moving_right_images[counter])
            self.dText = self.font.render("D", True, (144, 180, 216))
        elif pressed_keys[pygame.K_a]:
            self.image = pygame.image.load(moving_left_images[counter])
            self.aText = self.font.render("A", True, (144, 180, 216))
        elif pressed_keys[pygame.K_j]:  # till
            tileOn = back_ground.getTile()

            if isinstance(tileOn, Tile) and tileOn.condition == "empty":
                tileOn.setCondition(1)
                back_ground.updateTile()
                self.image = pygame.image.load(action_images[counter])
                sound1 = pygame.mixer.Sound("assets/music/action.wav")
                pygame.mixer.find_channel(True).play(sound1)
            elif isinstance(tileOn, RandomTile):
                sound3 = pygame.mixer.Sound("assets/music/laser.wav")
                pygame.mixer.find_channel(True).play(sound3)
        elif pressed_keys[pygame.K_k]:  # plant
            tileOn = back_ground.getTile()
            if (
                    isinstance(tileOn, Tile)
                    and tileOn.condition == "tilled"
                    and tileOn.crop == None
                    and self.wcurrency >= 10
            ):
                sound4 = pygame.mixer.Sound("assets/music/plant.wav")
                pygame.mixer.find_channel(True).play(sound4)
                tileOn.crop = Crop(self.seeds[self.seedIndex], 2*(self.seedIndex+1), 15*(self.seedIndex+1), 10*(self.seedIndex+1))
                self.decreaseW(2*(self.seedIndex+1))
                tileOn.setCondition(2)
                back_ground.updateTile()
                self.image = pygame.image.load(action_images[counter])
            elif isinstance(tileOn, RandomTile):
                sound3 = pygame.mixer.Sound("assets/music/laser.wav")
                pygame.mixer.find_channel(True).play(sound3)
        elif pressed_keys[pygame.K_l]:  # harvest
            tileOn = back_ground.getTile()
            if isinstance(tileOn, Tile) and tileOn.condition == "harvest":
                sound3 = pygame.mixer.Sound("assets/music/harvest.wav")
                pygame.mixer.find_channel(True).play(sound3)
                tileOn.setCondition(0)
                tileOn.crop = None
                self.increaseC(10)
                back_ground.updateTile()
                self.image = pygame.image.load(action_images[counter])
            elif isinstance(tileOn, RandomTile):
                sound3 = pygame.mixer.Sound("assets/music/laser.wav")
                pygame.mixer.find_channel(True).play(sound3)
        elif pressed_keys[pygame.K_i]:  # fertilize
            tileOn = back_ground.getTile()
            if (
                    isinstance(tileOn, Tile)
                    and (
                    tileOn.condition == "seed"
                    or tileOn.condition == "seedling"
                    or tileOn.condition == "hapling"
            )
                    and tileOn.crop.growthTime > 1
                    and self.ccurrency > 0
            ):
                sound2 = pygame.mixer.Sound("assets/music/fertilizer.wav")
                pygame.mixer.find_channel(True).play(sound2)
                tileOn.addFertilizer(0.02)

                tileOn.lastFertilizeTime = time.time()
                self.decreaseC(1)
                self.image = pygame.image.load(action_images[counter])
                # add visual effect
            elif isinstance(tileOn, RandomTile):
                sound2 = pygame.mixer.Sound("assets/music/laser.wav")
                pygame.mixer.find_channel(True).play(sound2)
        elif pressed_keys[pygame.K_p]:  # upgrade
            if self.toggle:
                if self.seedIndexMax < 1 and self.ccurrency >= 15:
                    self.decreaseC(15)
                    self.seedIndexMax = 1
                    self.upgradeIcon = pygame.image.load(
                        "assets/plants/icons/cantaloupe.png"
                    )
                    self.upgradeCost = self.font.render("$30", True, (255, 160, 122))
                elif self.seedIndexMax < 2 and self.ccurrency >= 30:
                    self.decreaseC(30)
                    self.seedIndexMax = 2
                    self.upgradeIcon = pygame.image.load(
                        "assets/plants/icons/melon.png"
                    )
                    self.upgradeCost = self.font.render("$50", True, (255, 160, 122))
                elif self.seedIndexMax < 3 and self.ccurrency >= 50:
                    self.decreaseC(50)
                    self.seedIndexMax = 3
                    self.upgradeIcon = pygame.image.load(
                        "assets/plants/icons/grape.png"
                    )
                    self.upgradeCost = self.font.render("$80", True, (255, 160, 122))
                elif self.seedIndexMax < 4 and self.ccurrency >= 80:
                    self.decreaseC(80)
                    self.seedIndexMax = 4
                    self.upgradeIcon = pygame.image.load("assets/plants/icons/x.png")
                    self.upgradeCost = self.font.render("MAX", True, (255, 160, 122))
                self.toggle = False
        elif pressed_keys[pygame.K_o]:  # cycle
            if self.toggle:
                if self.seedIndex != self.seedIndexMax:
                    self.seedIndex += 1
                    self.cropIcon = pygame.image.load(
                        "assets/plants/icons/" + self.seeds[self.seedIndex] + ".png"
                    )
                elif self.seedIndex == self.seedIndexMax:
                    self.seedIndex = 0
                    self.cropIcon = pygame.image.load(
                        "assets/plants/icons/" + self.seeds[self.seedIndex] + ".png"
                    )
                self.toggle = False

        else:
            self.image = pygame.image.load(idle_front_images[counter])
            self.wText = self.font.render("W", True, (144, 200, 144))
            self.aText = self.font.render("A", True, (144, 200, 144))
            self.sText = self.font.render("S", True, (144, 200, 144))
            self.dText = self.font.render("D", True, (144, 200, 144))


class Rain:
    def __init__(self):
        self.bgimage = pygame.image.load("assets/rain.png")
        self.rectBGimg = self.bgimage.get_rect()
        self.raining = False
        self.randWait = 25
        self.lastRain = time.time()
        self.DEFAULT_IMAGE_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.bgimage = pygame.transform.scale(self.bgimage, self.DEFAULT_IMAGE_SIZE)
       
    def render(self):
        SCREEN.blit(self.bgimage, (0, 0))

def showHeatMap(tiles, levelType):
    startX = 342.5
    startY = 60
    x = startX
    y = startY
    side = 25
    spacer = side + 5

    mapTitle = ""
    titleX = 0
    if levelType == "f":
        mapTitle = "Fertilizer Map"
        titleX = 380
    elif levelType == "t":
        mapTitle = "Tillage Map"
        titleX = 450
    else:
        mapTitle = "Same Crop Map"
        titleX = 380

    font = pygame.font.Font("assets/Daydream.ttf", 40)
    title = font.render(mapTitle, True, (255, 255, 255))
    titleSurface = pygame.display.get_surface()
    titleSurface.blit(title, (titleX, 0))

    heatMap = heatmap5(tiles, levelType)
    for row in heatMap:
        for heatMapValue in row:
            surface = pygame.display.get_surface()
            box = pygame.Rect((x, y), (side, side))
            colorScale = min(int(255 * heatMapValue), 255)
            surface.fill(Color((0, colorScale, 0)), box)
            y += spacer

        x += spacer
        y = startY


john = Player()
back_ground = Background()
rain = Rain()


def growStuff():
    for i in range(0, 100):
        for j in range(0, 100):
            timeVar = time.time()
            if (
                    isinstance(tile_array[i][j], Tile)
                    and (tile_array[i][j].crop != None)
                    and (
                    tile_array[i][j].condition == "seed"
                    or tile_array[i][j].condition == "seedling"
                    or tile_array[i][j].condition == "hapling"
            )
                    and (
                    tile_array[i][j].crop.growthTime
                    <= timeVar - tile_array[i][j].growthTime
            )
            ):
                tile_array[i][j].growTile()
                # take money
                tile_array[i][j].growthTime = timeVar
                back_ground.updateTileGrow(i, j)


class startScreenCls:
    def __init__(self):
        self.start = True
        self.img1 = pygame.image.load("assets/background.png").convert()
        self.DEFAULT_IMAGE_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
        self.img1 = pygame.transform.scale(self.img1, self.DEFAULT_IMAGE_SIZE)

        self.r, self.g, self.b = 160, 0, 0

        self.font = pygame.font.Font("assets/Daydream.ttf", 80)
        self.titleText = self.font.render("Oh Deere", True, (self.r, self.g, self.b))
        self.titleText2 = self.font.render("Farms", True, (self.r, self.g, self.b))
        self.font = pygame.font.Font("assets/Daydream.ttf", 40)
        self.descriptionText = self.font.render(
            "Push Any Key to Start", True, (60, 60, 60)
        )

    def startScreenCall(self):
        SCREEN.blit(self.img1, (0, 0))
        if self.b == 0 and not self.r == 0:
            if self.r == 160 and self.g < 160:
                self.g += 1
            elif self.r > 0 and self.g == 160:
                self.r -= 1
        elif self.r == 0 and not self.g == 0:
            if self.g == 160 and self.b < 160:
                self.b += 1
            elif self.g > 0 and self.b == 160:
                self.g -= 1
        elif self.g == 0:
            if self.b == 160 and self.r < 160:
                self.r += 1
            elif self.b > 0 and self.r == 160:
                self.b -= 1
        self.font = pygame.font.Font("assets/Daydream.ttf", 80)
        self.titleText = self.font.render("Oh Deere", True, (self.r, self.g, self.b))
        self.titleText2 = self.font.render("Farms", True, (self.r, self.g, self.b))


strt = startScreenCls()
pauser = PausedClass()
ender = EndClass()
mixer.music.play()
musicIndex = 0
while running:
    strt.startScreenCall()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            john.toggle = False
        else:
            john.toggle = True
        if event.type == pygame.KEYDOWN:
            strt.start = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            SCREEN.blit(
                pauser.descriptionText, (SCREEN_WIDTH / 2 - 250, SCREEN_HEIGHT / 2 - 50)
            )
            pauser.Paused()
            pygame.display.update()
            FramePerSec.tick(FPS)
            continue
        if john.ccurrency >= 1000 and not ender.ended:
            if ender.endTime == 0:
                ender.timeText = ender.font.render(f"You finished in  {int(time.time()-startTime)}  seconds", True, (50, 215, 255))
                ender.endTime = int(time.time() - startTime)

            SCREEN.blit(
                ender.descriptionText, (SCREEN_WIDTH / 2 - 150, SCREEN_HEIGHT / 2 - 150)
            )
            SCREEN.blit(ender.timeText, (SCREEN_WIDTH/2-450, SCREEN_HEIGHT/2+150))
            ender.Paused()
            pygame.display.update()
            FramePerSec.tick(FPS)
            continue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_z:
            if musicIndex == 0 or musicIndex == 1:
                musicIndex += 1
                mixer.music.load(musicPlaylist[musicIndex])
                mixer.music.play()
            else:
                musicIndex = 0
                mixer.music.load(musicPlaylist[musicIndex])
                mixer.music.play()

    if strt.start:
        strt.startScreenCall()

        SCREEN.blit(strt.titleText, (SCREEN_WIDTH / 2 - 300, SCREEN_HEIGHT / 2 - 280))
        SCREEN.blit(strt.titleText2, (SCREEN_WIDTH / 2 - 210, SCREEN_HEIGHT / 2 - 175))
        SCREEN.blit(
            strt.descriptionText, (SCREEN_WIDTH / 2 - 400, SCREEN_HEIGHT / 2 + 140)
        )
        pygame.display.update()
        FramePerSec.tick(FPS)
        continue
    back_ground.update()
    back_ground.render()

    john.coinAmount = john.font.render(str(john.ccurrency), True, (255, 255, 102))
    john.waterAmount = john.font.render(str(john.wcurrency), True, (0, 191, 255))

    SCREEN.blit(john.image, john.rect)

    if rain.raining:
        rain.render()
    if not rain.raining and time.time() - rain.lastRain > rain.randWait:
        john.increaseW(100)
    if (
            time.time() - rain.lastRain > rain.randWait
            and time.time() - rain.lastRain < rain.randWait + 5
    ):
        rain.raining = True
    elif time.time() - rain.lastRain > rain.randWait + 5:
        rain.raining = False
        rain.lastRain = time.time()
        rain.randWait = random.randint(20, 80)

    SCREEN.blit(john.log, john.hud_rect)

    SCREEN.blit(john.wText, (70, 540))
    SCREEN.blit(john.aText, (40, 570))
    SCREEN.blit(john.sText, (70, 570))
    SCREEN.blit(john.dText, (100, 570))

    SCREEN.blit(john.mapText, (15, 620))

    SCREEN.blit(john.tillText, (170, 525))
    SCREEN.blit(john.plantText, (185, 560))
    SCREEN.blit(john.harvestText, (200, 595))
    SCREEN.blit(john.fertilizeText, (210, 630))

    SCREEN.blit(john.cropText, (755, 550))
    SCREEN.blit(john.cropIcon, john.cropRect)

    SCREEN.blit(john.upgradeText, (760, 600))
    SCREEN.blit(john.upgradeIcon, john.upgradeRect)
    SCREEN.blit(john.upgradeCost, (1170, 600))

    SCREEN.blit(john.coinText, (500, 550))
    SCREEN.blit(john.coinAmount, (640, 550))

    SCREEN.blit(john.waterText, (490, 600))
    SCREEN.blit(john.waterAmount, (640, 600))

    growStuff()
    timeAni = pygame.time.get_ticks() / 200
    pressed_keys = pygame.key.get_pressed()
    john.move(pressed_keys)

    if pressed_keys[pygame.K_m]:
        showHeatMap(tile_array, "f")
    elif pressed_keys[pygame.K_n]:
        showHeatMap(tile_array, "t")
    elif pressed_keys[pygame.K_b]:
        showHeatMap(tile_array, "s")

    pygame.display.update()
    FramePerSec.tick(FPS)