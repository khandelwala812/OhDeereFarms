import pygame.font
from Main import *


def paused():

    width = screen.get_width()
    height = screen.get_height()
    largeText =pygame.font.SysFont("comicsansms", 115)
    TextPause = text_objects("Paused", largeText)
    TextPause.center = ((width/2),(height/2))
    gameDisplay.blit(TextPause)


    button("Continue",150,450,100,50,green,bright_green,unpause)
    button("Quit",550,450,100,50,red,bright_red,quitgame)
