import pygame 
import random
from settings import * 

class PowerUp(pygame.sprite.Sprite):
    def __init__(self, w, h, f, op):
        super(PowerUp, self).__init__()
        self.w = w 
        self.h = h 
        self.open = op
        if self.open == False:
            self.type = random.choice(["fast","color","goldCoin","enemy"])
        else:
            self.type = random.choice(["fast","color","goldCoin"])
        self.image = powerupImg[self.type]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.w - self.rect.width)
        self.rect.y = -1
        self.fast = f
        self.fv = 20
    
    def update(self, v, f):
        self.fast = f
        if self.fast == False:
            self.rect.y += v 
        if self.fast == True:
            self.rect.y += self.fv
        if self.rect.top > self.h:
            self.kill()
        