import pygame
from tkinter import *


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
PLAYER_SPRITE = 'assets\deer.png'
class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load(PLAYER_SPRITE)
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 10

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.getPos()
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.getPos()
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.getPos()
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.getPos()
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed

    def getPos(self):
        print(f"x: {self.rect.centerx}")
        print(f"y: {self.rect.centery}")

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
Player((650, 250), camera_group)

#############################-Game Loop-######################################
while running:


####################### -Detecting Key Stroke-#############################################
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    
    screen.fill('black')
    camera_group.update()
    camera_group.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
