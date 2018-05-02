import pygame 
import math
import random
from obstacle import Obstacle
from settings import * 

class Enemy(Obstacle):
    def __init__(self, w, h, l):
        self.w = w 
        self.h = h
        self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/happy.png').convert_alpha(),
                (50, 50)), 0)
        self.vx = 2
        self.vy = 2
        self.acce = pygame.math.Vector2(0,0)
        self.posx = random.randrange(self.w/3, self.w*2/3)
        self.posy = - 20
        self.mass = 30
        self.l = l 
        self.lives = l
        self.died = False
        super().__init__(self.image, self.vx, self.vy, self.posx, self.posy, self.mass)
        
    def update(self,arrowx, arrowy, timer):
        if self.lives < (self.l / 3):
            self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/confused.png').convert_alpha(),
                (50, 50)), 0)
        elif self.lives < (self.l * 2/3):
            self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/smiling.png').convert_alpha(),
                (50, 50)), 0)
        gap = 5
        limit = 10
        if pygame.time.get_ticks() - timer < entertime:
            if self.rect.y < self.h / 3:
                self.rect.y += self.vel.y 
            if self.rect.x < self.w / 2 - gap:
                self.rect.x += self.vel.x
            elif self.rect.x > self.w / 2 + gap:
                self.rect.x -= self.vel.x
        
        if pygame.time.get_ticks() - timer > entertime:
            dx = self.rect.centerx - arrowx
            dy = self.rect.centery - arrowy
            rads = math.atan2(-dy, dx) 
            
            self.acce.x = 1
            self.acce.y = 1
            self.vel += self.acce
            self.vel.x *= math.cos(rads + math.pi)
            self.vel.y *= -math.sin(rads + math.pi)
            
            if self.vel.x > limit:
                self.vel.x -= 1
            elif self.vel.x < -limit:
                self.vel.x += 1
            
            if self.vel.y > limit:
                self.vel.y -= 1
            elif self.vel.y < -limit:
                self.vel.y += 1
            
            # if self.rect.x > self.w - self.rect.width:
            #     self.vel.x = -abs(self.vel.x)
            # if self.rect.x < limit + gap*2:
            #     self.vel.x = abs(self.vel.x)
            # if self.rect.y < limit + gap*2:
            #     self.vel.y = abs(self.vel.y)
            # if self.rect.y > self.h - self.rect.height:
            #     self.vel.y = -abs(self.vel.y)
        
            self.pos += self.vel 
            
            self.rect.x = self.pos.x 
            self.rect.y = self.pos.y
    
    def collide(self):
        self.lives -= 1
        if self.lives <= 0:
            self.died = True
            self.kill()
    
    def collision(self, x, y, other, type):
        super().collision(x, y, other, type)
        self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/unhappy.png').convert_alpha(),
                (50, 50)), 0)
            
        