import math, random, sys
import pygame
from pygame.locals import *

pygame.init()

running = True

while running :
    for event in pygame.event.get :
        if event.type == QUIT:
            running = False
            
W, H = 1920,1080
HW, HH = W/2, H/2
AREA = W*H

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sprite Sheets - Akoo")
FPS = 3

BLACK = (0, 0,0)
WHITE = (255, 255, 255)

class spritesheet:
    def __init__(self, filename, cols, rows):
        self.sheet = pygame.image.load("Player.png").convert_alpha()
        
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols*rows
        
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = self.rect.width/cols
        h = self.cellHeight = self.rect.height/rows

        