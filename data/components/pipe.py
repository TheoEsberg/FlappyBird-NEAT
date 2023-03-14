import pygame, random
from settings import * 

class Pipe():
    
    def __init__(self, x):
        self.x = x
        self.height = 0
        
        self.top = 0
        self.bottom = 0
        self.PIPE_TOP = pygame.transform.flip(PIPE_GFX, False, True)
        self.PIPE_BOTTOM = PIPE_GFX
        
        self.passed = False
        self.set_height()
        
    def set_height(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + PIPE_GAP
        
    def move(self):
        self.x -= PIPE_VELOCITY
        
    def render(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
        
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))
        
        # Check for collision
        top_collision_point = bird_mask.overlap(top_mask, top_offset)
        bottom_collision_point = bird_mask.overlap(bottom_mask, bottom_offset)
        
        # If collision return true else return false
        if(top_collision_point or bottom_collision_point):
            return True
        return False
    
    def has_collided(self, bird):
        pass
    
    def add_new_pipe(self, bird):
        if not self.passed and self.x < bird.x:
            self.passed = True
            return True
        return False        
    
    def off_screen(self, bird):
        if (self.x + self.PIPE_TOP.get_width() < 0):
            return True
        return False

