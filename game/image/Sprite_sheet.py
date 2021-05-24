import math, random, sys
import pygame
from pygame.locals import *

pygame.init()
            
W, H = 1000,1000
HW, HH = W/2, H/2
AREA = W*H

CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Sprite Sheets - Akoo")
FPS = 5

BLACK = (0, 0,0)
WHITE = (255, 255, 255)

class Spritesheet:
    def __init__(self, filename, cols, rows):
        self.filename = filename
        self.sheet = pygame.image.load(self.filename).convert_alpha()
        self.cols = cols
        self.rows = rows
        self.totalCellCount = cols * rows
        
        self.rect = self.sheet.get_rect()
        w = self.cellWidth = int(self.rect.width / cols)
        h = self.cellHeight = int(self.rect.height / rows)
        hw,hh = self.cellCenter = (int(w / 2), int(h / 2))
        
        self.cells = list([(Index % cols * w, int(Index / cols) * h, w, h) for Index in range(self.totalCellCount)])
        self.handle = list([
            (0, 0), (-hw, 0), (-w, 0),
            (0, -hh), (-hw, -hh), (-w, -hh),
            (0, -h), (-hw, -h), (-w, -h),])
        
    def draw(self, surface, cellIndex, x, y, handle = 0):
        surface.blit(self.sheet, (x + self.handle[handle][0], y + self.handle[handle][1]), self.cells[cellIndex])
        
s = Spritesheet("GreenPlayerRun.png", 8, 1)

CENTER_HANDLE = 4

Index = 0

# Loop

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    
    
    s.draw(DS, Index % s.totalCellCount, HW, HH, CENTER_HANDLE)
    Index += 1
        
    pygame.draw.circle(DS, WHITE, (HW, HH), 2, 0)
        
    pygame.display.update()
    CLOCK.tick(FPS)
    DS.fill(BLACK)

        