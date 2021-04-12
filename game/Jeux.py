import pygame
import math, sys, os
from pygame.locals import *


pygame.init()

class Player:
    def __init__(self, pv = 100, dmg):
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
        Ennemi.__init__(self, pv = 500, dmg, speed = 0.3)
        self.pv = pv
        self.speed = speed
        
class FF(Ennemi):
    def __init__(self, pv, dmg, speed):
        Ennemi.__init__(self, pv, dmg = 50, speed)
        self.dmg = dmg
        
background = pygame.image.load("background.png")
screen = pygame.display.set_mode(size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
    screen.fill(background)
    
pygame.display.update()
    

