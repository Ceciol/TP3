import pygame 
import math

    
class Obstacle(pygame.sprite.Sprite):
    
    def __init__(self, image, v_x, v_y, pos_x, pos_y, mass):
        super(Obstacle, self).__init__()
        self.vel = pygame.math.Vector2(v_x, v_y)
        self.pos = pygame.math.Vector2(pos_x, pos_y)
        self.image = image
        self.baseImage = image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.friction_coeff = 0.1
        self.mass = mass
        
    def get_vel(self):
        return self.vel
    
    def get_pos(self):
        return self.pos
    
    def get_acce(self):
        return self.acce
        
    def update(self, v):
        if self.vel.y != v:
            if self.vel.y == 0:
                self.vel.y = 1
            if self.vel.y > 0:
                if self.vel.y > v:
                    self.vel.y -= self.vel.normalize().y * (self.friction_coeff * self.mass)
                elif self.vel.y < v:
                    self.vel.y += self.vel.normalize().y * (self.friction_coeff * self.mass)
            if self.vel.y < 0:
                self.vel.y -= self.vel.normalize().y * (self.friction_coeff * self.mass)
        
        if self.vel.x != 0:
            self.vel.x -= self.vel.normalize().x * (self.friction_coeff * self.mass)
        
        self.pos += self.vel
            
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
            
    
    def collision(self, x, y, other, type):
        speed = 0
        dx = self.pos.x - x
        dy = self.pos.y - x
        rads = math.atan2(-dy, dx)
        other_vel = other.get_vel()
        mag = (other_vel.x ** 2 + other_vel.y ** 2) ** 0.5
        if type == "arrow":
            self.vel.x =  (self.vel.x + 30) * math.cos(rads)
            self.vel.y = self.vel.y * math.sin(rads)
        if type == "map":
            if self.rect.x > other.rect.x: self.vel.x = abs(self.vel.x) + speed
            elif self.rect.x < other.rect.x: self.vel.x = -abs(self.vel.x) - speed
            if self.rect.y >= other.rect.y: self.vel.y = abs(self.vel.y) + speed
            elif self.rect.y < other.rect.y: self.vel.y = -abs(self.vel.y) - speed
        if type == "obs":
            self.vel.x = (mag) * math.cos(rads)
            self.vel.y = (mag) * math.sin(rads)
        if type == "obs1":
            self.vel.x = (mag) * math.cos(rads + math.pi)
            self.vel.y = (mag) * math.sin(rads + math.pi)

            
            
        
        

