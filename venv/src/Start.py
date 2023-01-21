import pygame.font
from Main import *


def startMenu():

    width = screen.get_width()
    height = screen.get_height()
    largeText =pygame.font.Font("assets/Fonts/Daydream.ttf", 115)
    title = text_objects("Oh Deere Farms", largeText)
    title.center = ((width/2),(height/2))
    gameDisplay.blit(title)

    smallText = pygame.font.Font("assets/Fonts/Daydream.ttf", 45)
    titleDescription = text_objects("Click to Start", smallText)
    titleDescription.center = ((width/2),(height/2))
    gameDisplay.blit(titleDescription)

