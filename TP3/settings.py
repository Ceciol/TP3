# settings 
import pygame

powerupImg = {}
powerupImg["fast"] = pygame.image.load("image/fast.png")
powerupImg["color"] = pygame.image.load("image/color.png")
powerupImg["goldCoin"] = pygame.image.load('image/coin_gold.png')
powerupImg["enemy"] = pygame.image.load("image/enemy.png")

enemyImg = {}
enemyImg["up"] = pygame.image.load("image/monster3.png")
enemyImg["down"] = pygame.image.load("image/monster2.png")
enemyImg["left"] = pygame.image.load("image/monster4.png")
enemyImg["right"] = pygame.image.load("image/monster5.png")

poweruptime = 5000
entertime = 5000
opentime = 100000

# colors 

blue = (99,177,192)

HighScoreFile = "highscore.txt"

