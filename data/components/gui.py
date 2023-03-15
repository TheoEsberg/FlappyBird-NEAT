import pygame
from settings import *

def render_score(win, score, gen):
    text = FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 20 - text.get_width(), 10))
    
    text = FONT.render("Gen: " + str(gen), 1, (255, 255, 255))
    win.blit(text, (10, 10))