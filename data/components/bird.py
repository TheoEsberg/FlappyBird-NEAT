from settings import *

class Bird():
    # Getting the bird grafics 
    GFX = BIRD_GFX
    
    # (Rotation / tilt) and animation values 
    MAX_ROTATION = 25
    ROTATION_VELOCITY = 20
    ANIMATION_TIME = 5
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.gfx_count = 0
        self.gfx = self.GFX[0]
        
    def jump(self):
        self.velocity = -10.5
        self.tick_count = 0
        self.height = self.y
        
    def move(self):
        self.tick_count += 1
        
        displacement = self.velocity * self.tick_count + 1.5 * self.tick_count ** 2
        
        # Cap the top speed up and down
        if (displacement >= 16):
            displacement = 16
        
        if (displacement < 0):
            displacement -= 2
        
        # Add smooth jumping    
        self.y += displacement
        
        if (displacement < 0 or self.y < self.height + 50):
            if (self.tilt < self.MAX_ROTATION):
                self.tilt = self.MAX_ROTATION
            else:
                if(self.tilt > -90):
                    self.tilt = self.ROTATION_VELOCITY
                    
    def render(self, win):
        # Bird grafics counter
        self.gfx_count += 1
        
        # ANIMATION (OBS) THIS MIGHT BE WORTH CHANGING 
        if (self.gfx_count < self.ANIMATION_TIME):
            self.gfx = self.GFX[0]
        elif (self.gfx_count < self.ANIMATION_TIME * 2):
            self.gfx = self.GFX[1]
        elif (self.gfx_count < self.ANIMATION_TIME * 3):
            self.gfx = self.GFX[2]
        elif (self.gfx_count < self.ANIMATION_TIME * 4):
            self.gfx = self.GFX[1]
        elif (self.gfx_count == self.ANIMATION_TIME * 4 + 1):
            self.gfx = self.GFX[0]
            self.gfx_count = 0
            
        # If bird is falling (dead) do not flap wings
        if (self.tilt <= -80):
            self.gfx = self.GFX[1]
            self.gfx_count = self.ANIMATION_TIME*2
        
        rotated_gfx = pygame.transform.rotate(self.gfx, self.tilt)
        rotate_position = rotated_gfx.get_rect(center=self.gfx.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_gfx, rotate_position.topleft)
        
    def get_mask(self):
        return(pygame.mask.from_surface(self.gfx))
    
    def hit_ground(self):
        if (self.y + self.gfx.get_height() >= 730):
            pass
        
