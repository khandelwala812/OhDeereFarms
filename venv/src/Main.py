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
PLAYER_SPRITE = ''

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('')
# Setup
camera_group = pygame.sprite.Group()

#############################-Game Loop-######################################
while running:

####################### -Detecting Key Stroke-#############################################
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            running = False
    
    screen.fill((255,255,255))
    pygame.display.flip()
    clock.tick(60)
