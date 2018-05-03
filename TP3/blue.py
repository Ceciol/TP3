import pygame 
import random 
from obstacle import Obstacle


class BlueSquare(Obstacle):
    def __init__(self, w, h, color):
        self.w = w
        self.h = h 
        self.color = color
        self.image = pygame.Surface((20,20))
        self.image.fill(self.color)
        self.vx = 0
        self.vy = 8
        self.posx = random.randrange(200,400)
        # changed 
        self.posy = 0
        self.mass = 3
        super().__init__(self.image, self.vx, self.vy, self.posx, self.posy, self.mass)
    

    

    
    