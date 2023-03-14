import pygame
from settings import *
from components.bird import * 
from components.render import *

def main():
    win = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT))
    clock = pygame.time.Clock()
    
    bird = Bird(200, 200)
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        bird.move()
        render_game(win, bird)
    
    pygame.quit()
    quit()
    
main()    
    

