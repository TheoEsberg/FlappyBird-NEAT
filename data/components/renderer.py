import pygame
import components.gui as GUI
from settings import *


def render_game(win, birds, pipes, base, score, gen):
    win.blit(BG_GFX, (0, 0))
    
    for pipe in pipes:
        pipe.render(win)
    
    base.render(win)
    
    if (pipes[0].x < 150): 
        i = 1 
    else:
        i = 0
    
    for bird in birds:
        bird.render(win)
    
        # DRAW LINES
        pygame.draw.line(win, (255, 0, 0), (bird.x + bird.gfx.get_width()/2, bird.y + bird.gfx.get_height()/2), (pipes[i].x + (pipes[i].PIPE_TOP.get_width()/2), pipes[i].height), 2)
        pygame.draw.line(win, (255, 0, 0), (bird.x + bird.gfx.get_width()/2, bird.y + bird.gfx.get_height()/2), (pipes[i].x + (pipes[i].PIPE_BOTTOM.get_width()/2), pipes[i].bottom), 2)
    
    GUI.render_score(win, score, gen)
    pygame.display.update()

