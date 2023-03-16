import pygame, os

# Game window settings
WIN_WIDTH = 600
WIN_HEIGHT = 800
FPS = 60
DIFFICULTY = 0.00125

# Pipe settings
PIPE_GAP = 200
PIPE_VELOCITY = 2.5

# Base settings
BASE_VELOCITY = 2.5

# This is the game grafics
PIPE_GFX = pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "pipe.png")))
BASE_GFX = pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "base.png")))
BG_GFX = pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bg.png")))
BIRD_GFX = [pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bird1.png"))), 
            pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bird2.png"))),
            pygame.transform.scale2x(pygame.image.load(os.path.join("res/gfx", "bird3.png")))]

# Fonts 
FONT = pygame.font.SysFont("roboto", 50)

