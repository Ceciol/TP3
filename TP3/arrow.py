import pygame
from settings import *
import math

class Arrow(pygame.sprite.Sprite):
    def __init__(self, w, h):
        super(Arrow, self).__init__()
        self.w = w
        self.h = h
        self.c = 0
        self.angle = 0 
        self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/arrow.png').convert_alpha(),
                (25, 35)), self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = (self.w / 2 , self.h * 4/5)
        self.speedx = 0
        self.speedy = 0 
        self.acce = 0.1
        self.countAngleLeft = 0
        self.countAngleRight = 0 
        self.dir = ""
        self.color_timer = pygame.time.get_ticks()
        self.vel = pygame.math.Vector2(self.speedx, self.speedy)
        self.mask = pygame.mask.from_surface(self.image)
    
    def get_vel(self):
        return self.vel
    
    
        
    def update(self, keysDown):
        ratio = 20
        decrement = 0 
        # make arrow rotate back to original

        if 0.1 > self.angle > 0.000001 or -0.1 < self.angle < -0.000001:
            if (not keysDown(pygame.K_LEFT)) and (not keysDown(pygame.K_RIGHT)):
                decrement = abs(self.angle) 
                if self.dir == "left":
                    self.angle -= decrement
                elif self.dir == "right":
                    self.angle += decrement
                self.image = pygame.transform.rotate(self.image, self.angle)

        if self.angle > 0.1 or self.angle < -0.1:
            if (not keysDown(pygame.K_LEFT)) and (not keysDown(pygame.K_RIGHT)):
                decrement = abs(self.angle) / 5
                if self.dir == "left":
                    self.angle -= decrement
                elif self.dir == "right":
                    self.angle += decrement
                self.image = pygame.transform.rotate(self.image, self.angle)

        # timeout for powerups 
        if self.c == 1 and pygame.time.get_ticks() - self.color_timer > poweruptime:
            self.c = 0
            self.power_timer = pygame.time.get_ticks()
        if self.c == 1:
            self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/arrow2.png').convert_alpha(),
                (25, 35)), self.angle)
        if self.c == 0:
            self.image = pygame.transform.rotate(pygame.transform.scale(
                pygame.image.load('image/arrow.png').convert_alpha(),
                (25, 35)), self.angle)
        self.speedx = 0
        self.speedy = 0 

        if keysDown(pygame.K_LEFT):
            if self.dir == "left":
                self.countAngleLeft += 1
                self.countAngleRight = 0
            else:
                self.dir = "left"
            self.speedx = -10 - self.angle * self.acce
        if keysDown(pygame.K_RIGHT):
            if self.dir == "right":
                self.countAngleRight += 1
                self.countAngleLeft = 0
            else:
                self.dir = "right"
            self.speedx = 10 + abs(self.angle) * self.acce
        if keysDown(pygame.K_UP):
            self.speedy = -10
        if keysDown(pygame.K_DOWN):
            self.speedy = 10
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.vel.x = self.speedx
        self.vel.y = self.speedy

        if self.countAngleLeft > ratio:
            self.countAngleLeft -= 1

        if self.countAngleRight > ratio:
            self.countAngleRight -= 1
        
        if self.dir == "left" and keysDown(pygame.K_LEFT):
            self.angle = self.countAngleLeft / ratio * 20
            self.image = pygame.transform.rotate(self.image, self.angle)
        elif self.dir == "right" and keysDown(pygame.K_RIGHT):
            self.angle = -self.countAngleRight / ratio * 20
            self.image = pygame.transform.rotate(self.image, self.angle)
    
    # this function moves the arrow according to action applied
    def moveEffect(self):
        pass
    
    def changeColor(self):
        self.color_timer = pygame.time.get_ticks()
        self.c = 1
    
    

        
    
