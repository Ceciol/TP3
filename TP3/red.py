import pygame 
import random 
import math
from obstacle import Obstacle

class RedSquare(Obstacle):
    def __init__(self, w, h, color):
        self.w, self.h = w, h
        self.color = color
        self.image = pygame.Surface((10,10))
        self.image.fill(self.color)
        self.x = random.randrange(0, self.w)
        self.y = -1
        self.speedy = random.randrange(8, 15)
        self.speedx = random.randrange(-3, 3)
        self.mass = 2
        super().__init__(self.image, self.speedx, self.speedy, self.x, self.y, self.mass)

class RedCircle(Obstacle):
    def __init__(self, w, h, color, white):
        self.w, self.h = w, h
        self.color = color
        self.image = pygame.Surface((50,50))
        self.image.fill(self.color)
        self.x = random.randrange(250, self.w - 250)
        self.y = -1
        #ygame.draw.circle(self.image, self.color, (self.x, self.y), 25)
        self.speedy = random.randrange(8, 15)
        self.speedx = random.randrange(-3, 3)
        self.mass = 15
        super().__init__(self.image, self.speedx, self.speedy, self.x, self.y, self.mass)
 

class RedRectangle(pygame.sprite.Sprite):
    def __init__(self, w, h, color, f):
        super().__init__()
        self.w, self.h = w, h
        self.color = color
        ws, we = 100, 200
        hs, he = 50, 80
        rectW = random.randrange(ws, we)
        rectH = random.randrange(hs, he)
        self.image = pygame.Surface((rectW, rectH))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange(-30, -10)
        self.speedx = random.randrange(4, 7)
        self.dir = random.choice((-1,1))
        if self.dir == -1:
            self.rect.x = self.w
        elif self.dir == 1:
            self.rect.x = 0
        elif self.dir == 0:
            self.rect.x = self.w / 2
        self.fast = f
        self.fv = 20
        
    def update(self, v, f):
        self.fast = f
        if self.fast == False:
            self.rect.x += self.dir * self.speedx
            self.rect.y += v + 5
        else:
            self.rect.y += self.fv
        if self.rect.top > self.h or self.rect.top < 0:
            self.kill()
    

        
        