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
        self.elasticity = 0.9
        self.mask = pygame.mask.from_surface(self.image)
        
    def get_vel(self):
        return self.vel
    
    def get_mass(self):
        return self.mass
    
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
        
        self.velocity = v
    
    def collision(self, x, y, other, type):
        dx = self.pos.x - x
        dy = self.pos.y - y
        rads = math.atan2(-dy, dx)
        other_vel = other.get_vel()
        mag = (other_vel.x ** 2 + other_vel.y ** 2) ** 0.5
        if type == "arrow":
            self.vel.x =  (abs(other_vel.x) + abs(self.vel.x) + 2) * math.cos(rads) 
            self.vel.y = - (abs(other_vel.y) + abs(self.vel.y)) * math.sin(rads)
        if type == "map":
            if self.rect.left < other.rect.left:
                self.vel.x = -abs(self.vel.x) * self.elasticity
            else:
                self.vel.x = abs(self.vel.x) * self.elasticity
            
            if self.vel.y > self.velocity:
                if self.rect.y < other.rect.y:
                    self.vel.y = (- self.vel.y + self.velocity) * self.elasticity
                else:
                    pass
            else:
                if self.rect.y < other.rect.y:
                    pass
                else:
                    if other.rect.midbottom[1] - 10 < self.rect.midtop[1] < other.rect.midbottom[1] + 10:
                        if  0 < self.vel.y:
                            self.vel.y = (self.vel.y + self.velocity) * self.elasticity
                        elif - self.velocity < self.vel.y < 0:
                            self.vel.y = (abs(self.vel.y) * 2 + self.velocity) * self.elasticity
                        else:
                            self.vel.y = (- self.vel.y + self.velocity) * self.elasticity

            if self.vel.x == 0 and self.vel.y == 0:
                self.vel.x, self.vel.y = 1, 1

            
        if type == "obs":
            self.vel.x = (mag + 1) * math.cos(rads) * other.get_mass() / self.mass * self.elasticity
            self.vel.y = (mag + 1) * math.sin(rads + math.pi) * other.get_mass() / self.mass * self.elasticity


            
            
        
        

