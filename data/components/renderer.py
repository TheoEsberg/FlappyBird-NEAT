import pygame
from settings import *


def render_game(win, bird, pipes, base):
    win.blit(BG_GFX, (0, 0))
    
    for pipe in pipes:
        pipe.render(win)
    
    base.render(win)
    bird.render(win)
    pygame.display.update()

