import pygame, sys
from tkinter import *

pygame.init()
pygame.display.set_caption('John Deer Game')

screen = pygame.display.set_mode((1270, 700))
screen_x, screen_y = screen.get_size()

running = True

def isGameRunning(event):
    if event.type == pygame.QUIT:   
        return False
    return True

while running:
    for event in pygame.event.get():
        running = isGameRunning(event)
