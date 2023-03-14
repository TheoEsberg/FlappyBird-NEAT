import pygame
import components.bird as Bird
import components.renderer as Renderer
import components.base as Base
import components.pipe as Pipe
from settings import *

def main():
    win = pygame.display.set_mode((MIN_WIDTH, MIN_HEIGHT))
    clock = pygame.time.Clock()
    
    bird = Bird.Bird(230, 350)
    base = Base.Base(730)
    pipes = [Pipe.Pipe(700)]
    
    # Variables
    run = True
    score = 0
    while run:
        clock.tick(FPS)
        add_pipe = False
        remove_list = []
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #bird.move()
        
        # Move the pipes
        for pipe in pipes:
            pipe.hasCollided(bird) # Check if collided
            add_pipe = pipe.addNewPipe(bird) # Check if we need to add a new pipe
            remove_list.append(pipe) if pipe.offScreen(bird) else None # Add pipe to remove list if the pipe is off the screen else do nothing
            pipe.move() # Actually move the pipe
        
        # Add new pipes and increase the score
        if (add_pipe):
            score += 1
            pipes.append(Pipe.Pipe(700))
            
        # Remove old pipes
        for r in remove_list:
            pipes.remove(r)
    
        # Move the base
        base.move()
        
        # Render the game
        Renderer.render_game(win, bird, pipes, base)
    pygame.quit()
    quit()

# RUN
main()    
    

