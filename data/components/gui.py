import pygame
from settings import *

def render_score(win, score):
    text = FONT.render("Score: " + str(score), 1, (255, 255, 255))
    win.blit(text, (WIN_WIDTH - 20 - text.get_width(), 10))