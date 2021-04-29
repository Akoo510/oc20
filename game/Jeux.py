import pygame
import math, sys, os
from pygame.locals import *


BLACK = (0, 0, 0)
pygame.init()

class Player:
    def __init__(self, dmg, pv = 100):
        self.pv = pv
        self.dmg = dmg

class Ennemi:
    def __init__(self, pv, dmg, speed = 1):
        self.pv = pv
        self.dmg = dmg
        self.speed = speed
        
class Rapido(Ennemi):
    def __init__(self, pv, dmg, speed = 3):
        Ennemi.__init__(self, pv, dmg, speed)
        self.speed = 3
        
class Tankos(Ennemi):
    def __init__(self, pv, dmg, speed):
        Ennemi.__init__(self, dmg, pv = 500, speed = 0.3)
        self.pv = pv
        self.speed = speed
        
class FF(Ennemi):
    def __init__(self, pv, dmg, speed):
        Ennemi.__init__(self, speed, pv, dmg = 50)
        self.dmg = dmg
        
background = pygame.image.load("background.png")
screen = pygame.display.set_mode((1000, 500))

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
    screen.blit(background, [0, 0])
    pygame.display.flip()
    