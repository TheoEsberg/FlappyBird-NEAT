import pygame, neat
pygame.font.init()

import components.bird as Bird
import components.renderer as Renderer
import components.base as Base
import components.pipe as Pipe
from settings import *

GEN = 0
def main(genomes, config):
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    
    global GEN
    GEN += 1
    
    nets = []
    ge = []
    birds = []
    
    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird.Bird(230, 350))
        g.fitness = 0
        ge.append(g)
    
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
                pygame.quit()
                quit()

        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                pipe_ind = 1
        else:
            run = False
            break
        
        for x, bird in enumerate(birds):
            bird.move()
            ge[x].fitness += 0.1
            
            # Input Nodes to get Output number in tanh
            output = nets[x].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            
            # If output tanh is greater than 0.5 we jump
            if output[0] > 0.5:
                bird.jump()
             
        
        # Move the pipes
        for pipe in pipes:
            pipe.move() # Actually move the pipe
            for x, bird in enumerate(birds):
                if (pipe.collide(bird)):
                    ge[x].fitness -= 1
                    birds.pop(x)
                    nets.pop(x)
                    ge.pop(x)
                
            add_pipe = pipe.add_new_pipe(bird) # Check if we need to add a new pipe                   
            remove_list.append(pipe) if pipe.off_screen() else None # Add pipe to remove list if the pipe is off the screen else do nothing    
        
        # Add new pipes and increase the score
        if (add_pipe):
            score += 1
            for g in ge:
                g.fitness += 5
            pipes.append(Pipe.Pipe(700))
            
        # Remove old pipes
        for r in remove_list:
            pipes.remove(r)
    
        # Check if bird has hit the ground
        for x, bird in enumerate(birds):
            if (bird.y + bird.gfx.get_height() >= 730) or bird.y < 0:
                birds.pop(x)
                nets.pop(x)
                ge.pop(x)
    
        # Move the base
        base.move()
        
        # Render the game
        Renderer.render_game(win, birds, pipes, base, score, GEN)




def run(config_path):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)
    population = neat.Population(config)
    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)
    
    winner = population.run(main, 50)

if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "../res/neat/config-feedforward.txt")
    run(config_path)


