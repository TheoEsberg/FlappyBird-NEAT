from settings import *

class Base():
    WIDTH = BASE_GFX.get_width()
    IMG = BASE_GFX
    
    def __init__(self, y):
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH
        
    def move(self, score):
        # Basic movement
        self.x1 -= BASE_VELOCITY + (score * DIFFICULTY)
        self.x2 -= BASE_VELOCITY + (score * DIFFICULTY)
        
        # Teleport when out of screen
        if (self.x1 + self.WIDTH < 0):
            self.x1 = self.x2 + self.WIDTH
        if (self.x2 + self.WIDTH < 0):
            self.x2 = self.x1 + self.WIDTH
            
    def render(self, win):
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))