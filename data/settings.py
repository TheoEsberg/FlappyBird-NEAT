import pygame, os

# Game window settings
MIN_WIDTH = 600
MIN_HEIGHT = 800
FPS = 60

# This is the game grafics
PIPE_GFX = pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "pipe.png")))
BASE_GFX = pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "base.png")))
BG_GFX = pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bg.png")))
BIRD_GFX = [pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bird1.png"))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bird3.png")))]

