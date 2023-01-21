import pygame, sys
from tkinter import *

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption('John Deer Game')
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 700
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
running = True

#############################-Load Map-######################################

#############################-Camera-######################################
PLAYER_SPRITE = 'assets\deer.png'

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load(PLAYER_SPRITE)
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.speed = 10

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed

# Setup
camera_group = pygame.sprite.Group()
Player((635,350), camera_group)

#############################-Game Loop-######################################
while running:

####################### -Detecting Key Stroke-#############################################
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
        
    camera_group.update()
    camera_group.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)
