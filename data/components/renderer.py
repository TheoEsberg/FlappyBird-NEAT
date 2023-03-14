import pygame
import components.gui as GUI
from settings import *


def render_game(win, bird, pipes, base, score):
    win.blit(BG_GFX, (0, 0))
    
    for pipe in pipes:
        pipe.render(win)
    
    base.render(win)
    bird.render(win)
    GUI.render_score(win, score)
    pygame.display.update()

