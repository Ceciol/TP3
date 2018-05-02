import pygame
from settings import *
import math

class Arrow(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super(Arrow, self).__init__()
        self.w = w
        self.h = h
        self.c = 0
        self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/arrow.png').convert_alpha(),
                (20, 20)), 0)
        self.rect = self.image.get_rect()
        self.rect.center = (self.w / 2 + 10, self.h * 4/5)
        self.speedx = 0
        self.speedy = 0 
        self.color_timer = pygame.time.get_ticks()
        self.vel = pygame.math.Vector2(self.speedx, self.speedy)
    
    def get_vel(self):
        return self.vel
    
    
        
    def update(self, keysDown):
        # timeout for powerups 
        if self.c == 1 and pygame.time.get_ticks() - self.color_timer > poweruptime:
            self.c = 0
            self.power_timer = pygame.time.get_ticks()
        if self.c == 1:
            self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/arrow2.png').convert_alpha(),
                (20, 20)), 0)
        if self.c == 0:
            self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/arrow.png').convert_alpha(),
                (20, 20)), 0)
        self.speedx = 0
        self.speedy = 0 
        if keysDown(pygame.K_LEFT):
            self.speedx = -8
        if keysDown(pygame.K_RIGHT):
            self.speedx = 8
        if keysDown(pygame.K_UP):
            self.speedy = -8
        if keysDown(pygame.K_DOWN):
            self.speedy = 8 
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.vel.x = self.speedx
        self.vel.y = self.speedy
    
            
    
    # this function moves the arrow according to action applied
    def moveEffect(self):
        pass
    
    def changeColor(self):
        self.color_timer = pygame.time.get_ticks()
        self.c = 1
    
    

        
    
