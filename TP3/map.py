import pygame
import random 
import math
class Map(pygame.sprite.Sprite):
    def __init__(self, color, x, y, s):
        super(Map, self).__init__()
        self.color = color
        self.image = pygame.Surface((s,s))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vel = pygame.math.Vector2(0,0)
    
    def get_vel(self):
        return self.vel



# generate regular map     
def mapGen(p, num, mode):
    p.pop()
    move = 5
    start = p[0].index(0) - 1
    minimum = 10
    end = 2 
    newS = 2
    newE = 2
    newLst = [ ]
    if mode == "easy":
        for i in range(len(p[0])):
            if i > start and p[0][i] == 1:
                end = i
                break 
        a = random.randint(0,50)
        if a % 2 == 0 and num == 10:
            newS = start + random.choice((-move,move))
            newE = end + random.choice((-move,move))
        
        else:
            newS = start 
            newE = end
        
    elif mode == "medium":
        for i in range(len(p[0])):
            if i > start and p[0][i] == 1:
                end = i
                break 
        a = random.randint(0,50)
        if a % 2 == 0 and num == 8:
            newS = start + random.choice((-move,move))
            newE = end + random.choice((-move,move))
        
        else:
            newS = start 
            newE = end
    
    elif mode == "hard":
        for i in range(len(p[0])):
            if i > start and p[0][i] == 1:
                end = i
                break 
        a = random.randint(0,50)
        if a % 10 == 1 and num == 5:
            newS = start + random.choice((-move,move))
            newE = end + random.choice((-move,move))
        
        else:
            newS = start 
            newE = end
            
    w = newE - newS
        
    
    # if w > len(p[0]) / 3:
    #     for i in range(newS + minimum + 2, newE - minimum - 1):
    #         mid.append(i)
    # print(mid)
    
    if w < minimum:
        if newE < len(p[0]) - minimum - move:
            newE += minimum
        elif newS > minimum + move:
            newS -= minimum
    if newS < 0: newS += move
    elif newS > len(p[0]) - move - 2: newS -= move
    if newE < move + 2: newE += move
    elif newE > len(p[0]) - move: newE -= move
    
    for j in range(len(p[0])):
        if j <= newS: newLst.append(1)
        elif newS < j < newE: newLst.append(0)
        elif newE <= j: newLst.append(1)

    p.insert(0,newLst)
    return p


# generate battle map
def battleMapGen(p, num):
    p.pop()
    start = p[0].index(0) - 1
    size = 5 
    end = 0 
    newLst = [ ]
    
    # find end 
    for i in range(len(p[0])):
        if i > start and p[0][i] == 1:
            end = i
            break 
            
    if num == 5:
        if start > size: start -= size
        if end <= len(p[0]) - size*2: end += size
        
    newS = start 
    newE = end
    
    for j in range(len(p[0])):
        if j <= newS: newLst.append(1)
        elif newS < j < newE: newLst.append(0)
        elif newE <= j: newLst.append(1)
    
    p.insert(0,newLst)
    return p 
    
