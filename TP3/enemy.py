import pygame 
import math
import random
from obstacle import Obstacle
from settings import * 


class Enemy(Obstacle):
    def __init__(self, w, h, l):
        self.w = w 
        self.h = h

        self.image = enemyImg["down"]
        self.vx = 3
        self.vy = 3
        self.mag = 4
        self.posx = random.randrange(int(self.w/3), int(self.w*2/3))
        self.posy = - 20
        self.mass = 30
        self.l = l 
        self.lives = l
        self.died = False
        super().__init__(self.image, self.vx, self.vy, self.posx, self.posy, self.mass)
        
    def update(self,arrowx, arrowy, timer):
        limit = 10
        gap = 100
        if pygame.time.get_ticks() - timer < entertime:
            if self.rect.y < self.h / 3:
                self.rect.y += self.vel.y 
            if self.rect.x < self.w / 2 :
                self.rect.x += self.vel.x
            elif self.rect.x > self.w / 2:
                self.rect.x -= self.vel.x
        
        if pygame.time.get_ticks() - timer > entertime:
            dx = self.rect.x - arrowx
            dy = self.rect.y - arrowy
            rads = math.atan2(-dy, dx) 

            self.vel.x = self.mag * math.cos(rads + math.pi)
            self.vel.y = - self.mag * math.sin(rads + math.pi)

        # change image 
        if arrowy < self.rect.y - gap:
            self.image = enemyImg["up"]
        elif arrowy > self.rect.y + gap:
            self.image = enemyImg["down"]
        elif arrowx < self.rect.x:
            self.image = enemyImg["left"]
        elif arrowx > self.rect.x:
            self.image = enemyImg["right"]
        self.mask = pygame.mask.from_surface(self.image)


            
        self.rect.x += self.vel.x 
        self.rect.y += self.vel.y 
    
    def collide(self):
        self.lives -= 1
        if self.lives <= 0:
            self.died = True
            self.kill()
            
        