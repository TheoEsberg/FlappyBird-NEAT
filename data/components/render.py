import pygame, os
from settings import *


def render_game(win, bird):
    win.blit(BG_GFX, (0, 0))
    bird.draw(win)
    
    pygame.display.update()

